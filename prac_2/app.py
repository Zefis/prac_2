from flask import Flask, render_template,request
app =Flask(__name__)
#ruta de la raiz y envio de variables
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/curso")
def curso():
    return render_template("curso.html")

@app.route("/usuario")
def usuario():
    return render_template("usuario.html")

@app.route("/producto")
def producto():
    return render_template("producto.html")

@app.route("/libro")
def libro():
    return render_template("libro.html")

@app.route("/proceso_1",methods = ['POST'])
def proceso_1():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    clase_seleccionada = request.form.get('clase')
    return render_template("salida_1.html", nombre=nombre, apellido=apellido,  clase_seleccionada=clase_seleccionada)

@app.route("/proceso_2",methods = ['POST'])
def proceso_2():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    email = request.form.get('email')
    password = request.form.get('password')
    return render_template("salida_2.html", nombre=nombre, apellido=apellido,  email=email,password=password)

@app.route("/proceso_3",methods = ['POST'])
def proceso_3():
    producto = request.form.get('producto')
    categoria = request.form.get('categoria')
    existencia = request.form.get('existencia')
    precio = float(request.form.get('precio'))
    return render_template("salida_3.html", producto=producto,categoria=categoria,existencia=existencia,precio=precio)

@app.route("/proceso_4",methods = ['POST'])
def proceso_4():
    titulo = request.form.get('titulo')
    autor = request.form.get('autor')
    resumen = request.form.get('resumen')
    roles = request.form.get('roles')
    return render_template("salida_4.html", titulo=titulo,autor=autor,resumen=resumen,roles=roles)

#debemos poner todas las rutas dentro de el index
if __name__ == "__main__":
    app.run(debug=True)