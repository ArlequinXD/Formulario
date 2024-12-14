from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def forms():
    return render_template("forms.html")

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        # Recibir datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        universidad = request.form['universidad']

        # Procesar los datos (aquí solo los mostramos)
        return f"""
        <h1>Datos recibidos:</h1>
        <p><strong>Nombre:</strong> {nombre}</p>
        <p><strong>Apellido:</strong> {apellido}</p>
        <p><strong>Edad:</strong> {edad}</p>
        <p><strong>Universidad:</strong> {universidad}</p>
        <a href="/">Volver</a>
        """
    return render_template('forms.html')

if __name__ == '__main__':
    app.run(debug=True)
