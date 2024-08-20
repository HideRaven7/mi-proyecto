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
@app.route('/home/profesor/', methods=['GET','POST'])
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
    
    # Manejar la selección del curso
    curso_seleccionado = request.form.get('cursos', cursos[0]['id_curso'] if cursos else None)
    
    # Obtener la información de estudiantes y asistencias basados en el curso seleccionado
    if curso_seleccionado:
        cursor.execute("""
            SELECT estudiantes.id_estudiante, estudiantes.nombre, estudiantes.apellidos
            FROM estudiantes
            WHERE estudiantes.id_curso = %s
        """, (curso_seleccionado,))
        estudiantes = cursor.fetchall()

        cursor.execute("""
            SELECT a.id_estudiante, a.Sect_Oct, a.Nov_Dic, a.Ene_Feb, a.Marz_Abril, a.May_Jun, a.Total_de_asistencias
            FROM asistencias AS a
            WHERE a.id_curso = %s
        """, (curso_seleccionado,))
        asistencias = cursor.fetchall()
    else:
        estudiantes = []
        asistencias = []
        
    cursor.execute('SELECT imagen_perfil FROM profesores WHERE id_profesor = %s', (id_profesor,))  
    perfil = cursor.fetchone()
    cursor.close()
    connection.close()

    return render_template('./profesor/p-home-a.html', cursos=cursos, curso_seleccionado=curso_seleccionado, estudiantes=estudiantes, asistencias=asistencias, perfil=perfil)


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
    cursor.execute('SELECT * FROM `profesores` WHERE id_profesor = %s', (id_profesor,))
    perfil = cursor.fetchall()
    
    cursor.close()
    
    return render_template('./profesor/p-perfil.html', perfil=perfil[0])

@app.route('/profesor/refuerzo/libros/', methods=['GET'])
def p_refuerzo_libros():
    if 'user_id' not in session or session.get('role') != 'profesor':
        return redirect('/')

    curso_seleccionado = request.args.get('curso_seleccionado')

    id_profesor = session['user_id']

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = """
        SELECT libros.*, asignaturas.nombre
        FROM libros
        JOIN asignaturas ON libros.id_asignatura = asignaturas.id_asignatura
        JOIN profesores ON profesores.id_asignatura = libros.id_asignatura
        WHERE libros.id_curso = %s and profesores.id_profesor
    """
    cursor.execute(sql, (curso_seleccionado, id_profesor))

    libros = cursor.fetchall()
    cursor.close()
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


@app.route('/profesor/refuerzo/videos/')
def p_refuerzo_videos():

    if 'user_id' not in session or session.get('role') != 'profesor':
        return redirect('/')
    
    curso_seleccionado = request.args.get('curso_seleccionado')

    id_profesor = session['user_id']

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    cursor = connection.cursor()

    sql = ('''
        SELECT 
            videos.id AS id_video,
            videos.titulo, 
            asignaturas.nom_asignatura
        FROM 
            videos 
        JOIN 
            profesor_asignado ON profesor_asignado.id_curso = videos.id_curso 
        JOIN 
            profesores ON profesores.id_profesor = profesor_asignado.id_profesor 
        JOIN 
            asignaturas ON asignaturas.id_asignatura = videos.id_asignatura 
        WHERE 
            profesores.id_profesor = %s AND videos.id_curso = %s
    ''')

    cursor.execute(sql, (id_profesor, curso_seleccionado))

    videos = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template('./profesor/p-refuerzo-videos.html', videos=videos)

@app.route('/profesor/refuerzo/videos/')
def mostrar_videos():
    sql = 'SELECT * FROM videos'
    
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='jes'
    )
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    videos = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return render_template('p-refuerzo-videos.html', videos=videos)

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

@app.route('/profesor/agregar/material/')
def p_agregar_material():
    return render_template('./profesor/p-agregar-material.html')

@app.route('/profesor/agregar/material', methods=['GET', 'POST'])
def agregar_material():
    if request.method == 'POST':
        fondo_material = request.files['fondo-material']
        nombre_material = request.form['nombre-material']
        recurso_de_estudio = request.files['recurso-de-estudio']
        descripcion_material = request.form['descripcion-material']

        tiempo = datetime.now()
        horaActual = tiempo.strftime('%Y%H%M%S')
        nombreArchivo = horaActual + "_" + secure_filename(recurso_de_estudio.filename)
        recurso_de_estudio.save(os.path.join(app.config['UPLOAD_FOLDER'], nombreArchivo))
        
        sql = "INSERT INTO material_estudio (id_curso, id_asignatura, titulo, fondo, material, descripcion) VALUES (2, %s, %s, %s, %s, %s)"
        datos = (nombre_material, secure_filename(fondo_material.filename), nombreArchivo, descripcion_material)
        
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='jes'
        )
        
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, datos)
        connection.commit()
        cursor.close()

        return redirect(url_for('p-refuerzo-libros'))
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

@app.route('/profesor/reporte/')
def p_report_a():
    return render_template('./profesor/p-report-a.html')

@app.route('/profesor/reporte/admin/', methods=['GET', 'POST'])
def reporte():
    return render_template('p-report-a.html')  


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