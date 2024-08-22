import os
import pymysql
from flask import Flask, render_template, request, redirect, session, send_from_directory, url_for, flash
from werkzeug.utils import secure_filename
from datetime import datetime
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# Crear la aplicación
app = Flask(__name__)

# Crear una llave secreta
app.secret_key = 'JES'

# Configurar la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'jes'

# Carpeta para subir los archivos, fotos, pdf, etc.
UPLOAD_FOLDER = '/static/documentos'  
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Crear la carpeta si no existe
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])
    
#-----------------------------------------------------

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


@app.route('/ver/libro/<int:id_libro>')
def ver_libro(id_libro):

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    
    cursor = connection.cursor()
    cursor.execute('SELECT libros.id_libro,libros.titulo FROM libros WHERE id_libro=%s', (id_libro))
    libros = cursor.fetchone()
    connection.commit()
    cursor.close()
    return render_template('./profesor/p-libro-refuerzo.html', libros=libros)

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

@app.route('/profesor/agregar/libros/')
def agregar_libro():
    return render_template('/profesor/p-agregar-libro.html')

@app.route('/profesor/agregar/libros/', methods=['GET', 'POST'])
def p_agregar_libro():
    portada = request.files.get('portada_libro')
    titulo = request.form.get('titulo-libro')
    libro = request.files.get('subir-libro')
    return render_template('p-agregar-libro.html')


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