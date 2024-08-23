import os
import pymysql
from flask import Flask, render_template, request, redirect, session, send_from_directory, url_for, flash
from werkzeug.utils import secure_filename
import datetime
# Crear la aplicación
app = Flask(__name__)

# Crear una llave secreta
app.secret_key = 'JES'

# Configurar la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'jes'

# Para guardar archivos en la carpeta documentos
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static', 'documentos')

# Crear la carpeta si no existe
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
#-----------------------------------------------------
    
@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def Index():
    session.clear()
    return render_template('index.html')
    
@app.route('/login', methods=['POST'])
def login():
    matricula = request.form['matricula-sesion']
    password = request.form['pass-sesion']
    
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    # Verificación de estudiantes
    cursor.execute("SELECT * FROM estudiantes WHERE matricula = %s", (matricula,))
    estudiante = cursor.fetchone()
    if estudiante and estudiante['contraseña'] == password:
        session['user_id'] = estudiante['id_estudiante']
        session['role'] = 'estudiante'
        return redirect('/home/estudiante/')

    # Verificación de profesores
    cursor.execute("SELECT * FROM profesores WHERE matricula = %s", (matricula,))
    profesor = cursor.fetchone()
    if profesor and profesor['contraseña'] == password:
        session['user_id'] = profesor['id_profesor']
        session['role'] = 'profesor'
        return redirect('/home/profesor/')

    # Verificación de administradores
    cursor.execute("SELECT * FROM admin WHERE matricula = %s", (matricula,))
    admin = cursor.fetchone()
    if admin and admin['contraseña'] == password:
        session['user_id'] = admin['id_admin']
        session['role'] = 'admin'
        return redirect('/home/admin/')
    return redirect('/')
# # =========================================================

# HOME ESTUDIANTE
@app.route('/home/estudiante/', methods=['GET'])
def home_estudiante():
    if 'user_id' not in session or session.get('role') != 'estudiante':
        return redirect('/')

    estudiante_id = session['user_id']

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT imagen_perfil FROM estudiantes WHERE id_estudiante = %s", (estudiante_id,))
    estudiante = cursor.fetchone()

    # calificacion estudiante
    cursor.execute("""
        SELECT 
            calificaciones.id_estudiante,
            asignaturas.nom_asignatura AS nom_asignatura,
            calificaciones.C1,
            calificaciones.C2,
            calificaciones.C3,
            calificaciones.C4,
            calificaciones.c_final
        FROM 
            calificaciones
        JOIN 
            asignaturas ON calificaciones.id_asignatura = asignaturas.id_asignatura
        WHERE 
            calificaciones.id_estudiante = %s
    """, (estudiante_id,))
    calificaciones = cursor.fetchall()
    
    # asistencias estudiante
    cursor.execute("SELECT Sect_Oct, Nov_Dic, Ene_Feb, Marz_Abril, May_Jun, Total_de_asistencias FROM asistencias WHERE id_estudiante = %s", (estudiante_id,))

    asistencias = cursor.fetchall()

    # Inicializar contadores para las asistencias y los días de clase
    total_asistencias = 0
    total_periodos = 0
    total_registros = len(asistencias)

    # Sumar todas las asistencias y los días de clase
    for asistencia in asistencias:
        total_asistencias += (
            int(asistencia['Sect_Oct']) +
            int(asistencia['Nov_Dic']) +
            int(asistencia['Ene_Feb']) +
            int(asistencia['Marz_Abril']) +
            int(asistencia['May_Jun'])
        )
        total_periodos += 5 * int(asistencia['Total_de_asistencias'])

    # Calcular el porcentaje de asistencia
    if total_periodos > 0:
        porcentaje_asistencia = (total_asistencias / total_periodos) * 100
    else:
        porcentaje_asistencia = 0
    
    # horario estudiante
    sql = ("SELECT h.hora, d.dia, a.nom_asignatura  FROM horario AS hor JOIN hora AS h ON hor.id_hora = h.id_hora JOIN dias AS d ON hor.id_dias = d.id_dias JOIN asignaturas AS a ON hor.id_asignatura = a.id_asignatura JOIN estudiantes AS e ON hor.id_curso = e.id_curso WHERE e.id_estudiante = %s ORDER BY h.id_hora, d.id_dias")
    
    cursor.execute(sql,estudiante_id)
    
    horarios = cursor.fetchall()
    
    horario_por_hora = {}

    for horario in horarios:
        hora = horario['hora']
        dia = horario['dia']
        asignatura = horario['nom_asignatura']
        
        if hora not in horario_por_hora:
            horario_por_hora[hora] = {"Lunes": "", "Martes": "", "Miércoles": "", "Jueves": "", "Viernes": ""}
        
        horario_por_hora[hora][dia] = asignatura


    cursor.close()

    return render_template('estudiante/e-home.html', calificaciones=calificaciones, horario_por_hora=horario_por_hora, porcentaje=porcentaje_asistencia, estudiante=estudiante)


@app.route('/estudiante/perfil/')
def e_perfil():
    if 'user_id' not in session or session.get('role') != 'estudiante':
        return redirect('/')
    
    estudiante_id = session['user_id']
    
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM `estudiantes` WHERE id_estudiante = %s', (estudiante_id,))
    perfil = cursor.fetchall()
    
    cursor.execute('''
    SELECT cursos.nombre
    FROM estudiantes
    JOIN cursos ON estudiantes.id_curso = cursos.id_curso
    WHERE estudiantes.id_estudiante = %s''', (estudiante_id,))
    curso = cursor.fetchone()
    
    cursor.close()
    
    return render_template('./estudiante/e-perfil.html', perfil=perfil[0], curso=curso)

@app.route('/estudiante/material/', methods=['GET', 'POST'])
def e_material():
    if 'user_id' not in session or session.get('role') != 'estudiante':
        return redirect('/')

    estudiante_id = session['user_id']
    
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    # las asignaturas disponibles
    cursor.execute('''
    SELECT asignaturas.id_asignatura, asignaturas.nom_asignatura
    FROM asignaturas
    JOIN material_estudio ON asignaturas.id_asignatura = material_estudio.id_asignatura
    JOIN estudiantes ON estudiantes.id_curso = material_estudio.id_curso
    WHERE estudiantes.id_estudiante = %s''', (estudiante_id,))
    asignaturas = cursor.fetchall()

    # materiales vacío
    materiales = []

    if request.method == 'POST':
        materia_seleccionada = request.form.get('materias-agg')

        # Buscar materiales para la asignatura seleccionada
        cursor.execute('''
            SELECT material_estudio.*, asignaturas.nom_asignatura
            FROM material_estudio
            JOIN estudiantes ON material_estudio.id_curso = estudiantes.id_curso
            JOIN asignaturas ON material_estudio.id_asignatura = asignaturas.id_asignatura
            WHERE material_estudio.id_asignatura = %s AND estudiantes.id_estudiante = %s''', (materia_seleccionada, estudiante_id))
        materiales = cursor.fetchall()

    cursor.close()
    
    return render_template('./estudiante/e-material_estudio.html', asignaturas=asignaturas, materiales=materiales)

@app.route('/estudiante/material/<titulo>')
def ver_materia(titulo):
    if 'user_id' not in session or session.get('role') != 'estudiante':
        return redirect('/')

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # Obtener detalles del material por título
    cursor.execute('''
        SELECT material_estudio.*, asignaturas.nom_asignatura
        FROM material_estudio
        JOIN asignaturas ON material_estudio.id_asignatura = asignaturas.id_asignatura
        WHERE material_estudio.titulo = %s
    ''', (titulo,))
    material = cursor.fetchone()

    cursor.close()

    return render_template('estudiante/e-ver_materias.html', material=material)

@app.route('/estudiante/enviar/tarea/', methods=['POST'])
def enviar_tarea():
    if 'user_id' not in session or session.get('role') != 'estudiante':
        return redirect('/')

    estudiante_id = session['user_id']
    material_id = request.form.get('material_id')

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # Obtener la información del material
    cursor.execute('''
        SELECT id_curso
        FROM material_estudio
        WHERE id_material = %s
    ''', (material_id,))
    material = cursor.fetchone()

    if material:
        id_curso = material['id_curso']
    else:
        cursor.close()
        flash('Material no encontrado')
        return redirect('/estudiante/material/')

    # Procesar el archivo subido
    if 'subir-tarea' not in request.files:
        cursor.close()
        flash('No se ha subido ningún archivo')
        return redirect('/estudiante/material/')

    tarea = request.files['subir-tarea']
    if tarea.filename == '':
        cursor.close()
        flash('No se seleccionó ningún archivo')
        return redirect('/estudiante/material/')

    if tarea:
        archivos = secure_filename(tarea.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], archivos)
        tarea.save(file_path)

        cursor.execute('''
            INSERT INTO tareas_estudiante (id_estudiante, id_curso, tarea)
            VALUES (%s, %s, %s)
        ''', (estudiante_id, id_curso, archivos))

        connection.commit()
        cursor.close()

        flash('Tarea enviada exitosamente')
        return redirect('/estudiante/material/')

    cursor.close()
    flash('Error al subir el archivo')
    return redirect('/estudiante/material/')

@app.route('/estudiante/refuerzo/libros/')
def e_refuerzo_libros():
    if 'user_id' not in session or session.get('role') != 'estudiante':
        return redirect('/')

    estudiante_id = session['user_id']
    
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    cursor.execute(
    '''
        SELECT libros.*, asignaturas.nom_asignatura
        FROM libros
        JOIN estudiantes ON libros.id_curso = estudiantes.id_curso
        JOIN asignaturas ON libros.id_asignatura = asignaturas.id_asignatura
        WHERE estudiantes.id_estudiante = %s
    ''', (estudiante_id,))
    
    libros = cursor.fetchall()
    cursor.close()
    
    return render_template('./estudiante/e_refuerzo_libros.html', libros=libros)

@app.route('/estudiante/libro/<titulo>')
def e_libro(titulo):
    if 'user_id' not in session or session.get('role') != 'estudiante':
        return redirect('/')

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # Obtener detalles del libro por título
    cursor.execute('''
        SELECT libros.*, asignaturas.nom_asignatura
        FROM libros
        JOIN asignaturas ON libros.id_asignatura = asignaturas.id_asignatura
        WHERE libros.titulo = %s
    ''', (titulo,))
    
    libro = cursor.fetchone()
    cursor.close()

    return render_template('estudiante/e-libro-refuerzo.html', libro=libro)

@app.route('/estudiante/refuerzo/videos/')
def e_refuerzo_videos():
    estudiante_id = session['user_id']
    if 'user_id' not in session or session.get('role') != 'estudiante':
        return redirect('/')

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    cursor.execute(
        '''
        SELECT videos.*, asignaturas.nom_asignatura
        FROM videos
        JOIN estudiantes ON videos.id_curso = estudiantes.id_curso
        JOIN asignaturas ON videos.id_asignatura = asignaturas.id_asignatura
        WHERE estudiantes.id_estudiante = %s
        ''', (estudiante_id,)
    )
    
    videos = cursor.fetchall()
    cursor.close()
    return render_template('./estudiante/e_refuerzo_videos.html', videos=videos)

@app.route('/estudiante/video/<titulo>')
def e_videos(titulo):
    if 'user_id' not in session or session.get('role') != 'estudiante':
        return redirect('/')

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    cursor.execute('''
        SELECT videos.*, asignaturas.nom_asignatura
        FROM videos
        JOIN asignaturas ON videos.id_asignatura = asignaturas.id_asignatura
        WHERE videos.titulo = %s
    ''', (titulo,))
    
    video = cursor.fetchone()
    cursor.close()
    
    return render_template('./estudiante/e-video-clase.html', video = video)


# APARTADO DEL PROFESORES EN PYTHON Smailyn 
@app.route('/home/profesor/', methods=['GET', 'POST'])
def p_home():
    id_profesor = session['user_id']
    
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    cursor.execute("""
        SELECT DISTINCT c.id_curso, c.nombre
        FROM cursos c
        JOIN profesor_asignado pa ON c.id_curso = pa.id_curso
        WHERE pa.id_profesor = %s
    """, (id_profesor,))
    cursos = cursor.fetchall()
    
    if request.method == 'POST':
        curso_seleccionado = request.form.get('curso_seleccionado')
        session['curso_seleccionado'] = curso_seleccionado
    else:
        curso_seleccionado = session.get('curso_seleccionado')
        if not curso_seleccionado and cursos:
            curso_seleccionado = cursos[0]['id_curso'] if isinstance(cursos[0], dict) else cursos[0][0]
            session['curso_seleccionado'] = curso_seleccionado
    
    cursor.execute("""
        SELECT estudiantes.id_estudiante, estudiantes.nombre, estudiantes.apellidos, estudiantes.matricula
        FROM estudiantes
        WHERE estudiantes.id_curso = %s
    """, (curso_seleccionado,))
    estudiantes = cursor.fetchall()

    cursor.execute("""
        SELECT a.id_estudiante, a.Sect_Oct, a.Nov_Dic, a.Ene_Feb, a.Marz_Abril, a.May_Jun, a.Total_de_asistencias
        FROM asistencias AS a
        WHERE a.id_curso = %s
    """, (curso_seleccionado,))
    asistencia = cursor.fetchall()

    # Convertir la lista de asistencias en un diccionario
    asistencias = {a['id_estudiante']: a for a in asistencia}

    # Obtener las calificaciones previas de cada estudiante
    calificaciones = {}
    for estudiante in estudiantes:
        cursor.execute("""
            SELECT c1, c2, c3, c4, c_final
            FROM calificaciones
            WHERE id_estudiante = %s
        """, (estudiante['id_estudiante'],))
        calificaciones[estudiante['id_estudiante']] = cursor.fetchone()
        
    cursor.execute('SELECT imagen_perfil, nombre, apellido FROM profesores WHERE id_profesor = %s', (id_profesor,))  
    perfil = cursor.fetchone()
    
    cursor.close()
    connection.close()

    return render_template('./profesor/p-home-a.html', estudiantes=estudiantes, asistencias=asistencias, calificaciones=calificaciones, perfil=perfil, curso_seleccionado=curso_seleccionado, cursos=cursos)


@app.route('/profesor/perfil/')
def p_perfil():
    if 'user_id' not in session or session.get('role') != 'profesor':
        return redirect('/')
    
    id_profesor = session['user_id']
    
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('''
        SELECT profesores.*, asignaturas.nom_asignatura
        FROM profesores
        JOIN asignaturas ON asignaturas.id_asignatura = profesores.id_asignatura
        WHERE profesores.id_profesor = %s
    ''', (id_profesor,))
    perfil = cursor.fetchall()
    
    cursor.close()
    return render_template('./profesor/p-perfil.html', perfil=perfil[0])

# @app.route('/home/profesor/asistencia/', methods=['POST'])
# def p_asistencia():
#     if 'user_id' not in session or session.get('role') != 'profesor':
#         return redirect('/')
#     id_profesor = session['user_id']
#     return redirect('/home/profesor/')

@app.route('/profesor/refuerzo/libros/', methods=['GET', 'POST'])
def p_refuerzo_libros():
    if 'user_id' not in session or session.get('role') != 'profesor':
        return redirect('/')

    curso_seleccionado = session['curso_seleccionado']
    id_profesor = session['user_id']

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    if request.method == 'POST':
        id_libro_a_eliminar = request.form.get('id_libro')
        if id_libro_a_eliminar:
            cursor.execute('''
                DELETE FROM libros
                WHERE id_libro = %s AND id_curso = %s
            ''', (id_libro_a_eliminar, curso_seleccionado))
            connection.commit()
            return redirect('/profesor/refuerzo/libros/')
    
    sql = """
        SELECT libros.*, asignaturas.nom_asignatura
        FROM libros
        JOIN asignaturas ON libros.id_asignatura = asignaturas.id_asignatura
        JOIN profesores ON profesores.id_asignatura = libros.id_asignatura
        WHERE libros.id_curso = %s AND profesores.id_profesor = %s
    """
    cursor.execute(sql, (curso_seleccionado, id_profesor))
    libros = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return render_template('./profesor/p-refuerzo-libros.html', libros=libros)


@app.route('/ver/libro/')
def ver_libro():

    id_libro = request.args.get('id_libro')

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )

    cursor = connection.cursor()
    cursor.execute('SELECT libros.id_libro, libros.titulo, libros.subir_libro FROM libros WHERE id_libro = %s', (id_libro,))
    libro = cursor.fetchone()
    cursor.close()
    connection.close()
    return render_template('./profesor/p-libro-refuerzo.html', libro=libro)

@app.route('/eliminar/libro/<int:libro_id>', methods=['POST'])
def eliminar_libro(libro_id):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor()
    return redirect('/profesor/refuerzo/libros/')


@app.route('/profesor/refuerzo/videos/', methods=['GET', 'POST'])
def p_refuerzo_videos():
    if 'user_id' not in session or session.get('role') != 'profesor':
        return redirect('/')

    id_profesor = session['user_id']
    curso_seleccionado = session['curso_seleccionado']
    
    if not curso_seleccionado:
        return redirect('/home/profesor/')  # Redirige si no hay curso seleccionado

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    # Obtener el id_asignatura del profesor
    cursor.execute('''
        SELECT asignaturas.id_asignatura
        FROM profesores
        JOIN asignaturas ON asignaturas.id_asignatura = profesores.id_asignatura
        WHERE profesores.id_profesor = %s
    ''', (id_profesor,))
    
    asignatura = cursor.fetchone()
    if not asignatura:
        cursor.close()
        connection.close()
        return redirect('/home/profesor/')

    id_asignatura = asignatura['id_asignatura']

    sql = '''
        SELECT 
            videos.id AS id_video,
            videos.titulo, 
            asignaturas.nom_asignatura
        FROM 
            videos 
        JOIN 
            asignaturas ON asignaturas.id_asignatura = videos.id_asignatura
        WHERE 
            videos.id_curso = %s AND asignaturas.id_asignatura = %s
    '''
    cursor.execute(sql, (curso_seleccionado, id_asignatura))

    videos = cursor.fetchall()

    if request.method == 'POST':
        id_video_a_eliminar = request.form.get('id_video')
        if id_video_a_eliminar:
            cursor.execute('''
                DELETE FROM videos
                WHERE id = %s AND id_asignatura = %s
            ''', (id_video_a_eliminar, id_asignatura))
            connection.commit()
            return redirect('/profesor/refuerzo/videos/')

    cursor.close()
    connection.close()

    return render_template('./profesor/p-refuerzo-videos.html', videos=videos)

@app.route('/profesor/video/')
def p_mostrar_videos():
    if 'user_id' not in session or session.get('role') != 'profesor':
        return redirect('/')
    
    id_video = request.args.get('id_video')

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM videos WHERE id = %s', (id_video,))
    video = cursor.fetchone()
    cursor.close()
    connection.close()
    
    return render_template('./profesor/p-ver-videos.html', video=video)

@app.route('/agregar/libros/')
def p_agg_libro():
    if 'user_id' not in session or session.get('role') != 'profesor':
        return redirect('/')
    
    curso_seleccionado = session['curso_seleccionado']

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute('SELECT nombre FROM cursos WHERE id_curso = %s', (curso_seleccionado,))
    curso = cursor.fetchone()

    return render_template('./profesor/p-agregar-libro.html', curso = curso)


@app.route('/add/libros/', methods=['POST'])
def agregar_libro():
    if 'user_id' not in session or session.get('role') != 'profesor':
        return redirect('/')

    id_profesor = session['user_id']
    curso_seleccionado = session['curso_seleccionado']

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    portada = request.files.get('portada')
    titulo = request.form.get('titulo')
    libro = request.files.get('libro')

    cursor.execute("SELECT * FROM asignaturas JOIN profesores ON profesores.id_asignatura = asignaturas.id_asignatura WHERE id_profesor = %s", (id_profesor,))
    id_asignatura_result = cursor.fetchone()
    if id_asignatura_result:
        id_asignatura = id_asignatura_result['id_asignatura']

    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    portada_filename = f'portada_{timestamp}_{portada.filename}' if portada else None
    libro_filename = f'libro_{timestamp}_{libro.filename}' if libro else None

    if portada_filename:
        portada_path = os.path.join(app.config['UPLOAD_FOLDER'], portada_filename)
        portada.save(portada_path)

    if libro_filename:
        libro_path = os.path.join(app.config['UPLOAD_FOLDER'], libro_filename)
        libro.save(libro_path)

    cursor.execute(" INSERT INTO libros (id_libro, id_asignatura, id_curso, titulo, subir_libro, portada) VALUES (%s, %s, %s, %s, %s, %s)", ('NULL', id_asignatura, curso_seleccionado, titulo, libro_filename, portada_filename))

    connection.commit()
    cursor.close()
    connection.close()

    return redirect('/profesor/refuerzo/libros/')
    



@app.route('/profesor/agregar/video/')
def p_agregar():
    return render_template('./profesor/p-agregar-video.html')

@app.route('/agregar/video/profesor/', methods=['POST'])
def agregar_video():
    return redirect('/profesor/refuerzo/videos/')

@app.route('/profesor/materiales/')
def p_material_estudio():
    return render_template('/profesor/p-material_estudio.html')


@app.route('/profesor/agregar/material', methods=['GET', 'POST'])
def agregar_material():
    fondo_material = request.files['fondo-material']
    nombre_material = request.form['nombre-material']
    recurso_de_estudio = request.files['recurso-de-estudio']
    descripcion_material = request.form['descripcion-material']
    return render_template('./profesor/p-agregar-material.html')

@app.route('/profesor/recurso/estudio/')
def p_recurso_estudio():
    return render_template('./profesor/p-recurso_estudio.html')

@app.route('/profesor/material/subido/')
def p_material_de_curso_subido():
    return render_template('./profesor/p-material-de-curso-subido.html')

@app.route('/profesor/clases/enviadas/')
def p_clases_enviadas():
    return render_template('./profesor/p-clases-enviada.html')

@app.route('/profesor/tarea/estudiante/')
def p_tarea_e():
    return render_template('./profesor/p-tarea-e.html')


@app.route('/profesor/perfil/estudiante/<int:id_estudiante>')
def p_perfil_e(id_estudiante):
    connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='jes'
        )
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute("""
            SELECT *, cursos.nombre AS nom_curso
            FROM estudiantes
            JOIN cursos ON cursos.id_curso = estudiantes.id_curso
            WHERE id_estudiante = %s
        """, (id_estudiante,))
    estudiante = cursor.fetchone()

    return render_template('./profesor/p-perfil-e.html', estudiante=estudiante)




if __name__ == '__main__':
    app.run(port = 3000, debug=True)