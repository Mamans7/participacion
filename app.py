from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

# Clave secreta para manejar la sesión
app.secret_key = 'supersecretkey'

# Datos de ejemplo para usuarios
users = {
    'carlos': 'carlos1',
    'daniel': 'daniel2'
}

# Ruta para la página de inicio de sesión
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verificar si el usuario y contraseña son correctos
        if username in users and users[username] == password:
            # Almacenar el nombre de usuario en la sesión
            session['username'] = username
            return redirect(url_for('bienvenido'))
        else:
            flash('Usuario o contraseña incorrectos. Intenta de nuevo.')
    
    return render_template('index.html')

# Ruta para la página de bienvenida (requiere autenticación)
@app.route('/bienvenido')
def bienvenido():
    if 'username' in session:
        username = session['username']
        return render_template('bienvenido.html', username=username)
    else:
        return redirect(url_for('index'))

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('username', None)  # Eliminar el usuario de la sesión
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
