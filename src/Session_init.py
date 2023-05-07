import psycopg2
from flask import Flask, render_template, request, session, redirect, url_for

# Conectar a la base de datos
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_username",
    password="your_password"
)

# Definimos la variable global de sesión
app.secret_key = 'clave_secreta_para_la_sesion'

# Establecer un cursor para interactuar con la base de datos
cur = conn.cursor()

# Ejecutar una consulta para buscar el usuario y la contraseña en la tabla correspondiente
cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))

# Obtener los resultados de la consulta
result = cur.fetchone()

# Cerrar el cursor y la conexión a la base de datos
cur.close()
conn.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validamos el usuario en la base de datos
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Usuario o contraseña incorrectos')
    else:
        return render_template('login.html')

@app.route('/index')
def index():
    # Validamos si el usuario tiene una sesión activa
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

# Desconectar sesión después de 10 minutos de inactividad
@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)
    session.modified = True