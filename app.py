from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'gamerbuy'
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT 
    productos.nombre,
    productos.precio_por_unidad,
    productos.stock,
    productos.imagen,
    proveedor.nombre,
    marcas.nombre FROM PRODUCTOS, MARCAS, PROVEEDOR WHERE marcas.id = id_marcas AND proveedor.id = id_proveedor''')
    respuesta = cursor.fetchall()
    return render_template('index.html',productos = respuesta)

@app.route('/listadoProductos')
def listado():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM PRODUCTOS')
    respuesta = cursor.fetchall()
    return render_template('listadoProductos.html',productos = respuesta)

@app.route('/registrarCliente',methods = ['GET','POST'])
def registrarCliente():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM DIRECCION')
        respuesta = cursor.fetchall()
        return render_template('registrarCliente.html', direccion = respuesta)
    if request.method == 'POST':
        dni = request.form['dni']
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO CLIENTE (dni,nombre,id_direccion)VALUES(%s, %s, %s)",
        (dni,nombre,direccion)) #el porcentaje s significa que vas a poner los valores que te paso a continuacion
        mysql.connection.commit()
        cur = mysql.connection.cursor()
        cur.execute('''SELECT 
        productos.nombre,
        productos.precio_por_unidad,
        productos.stock,
        productos.imagen,
        proveedor.nombre,
        marcas.nombre FROM PRODUCTOS, MARCAS, PROVEEDOR WHERE marcas.id = id_marcas AND proveedor.id = id_proveedor''')
        respuesta = cur.fetchall()
        flash('Cliente Registrado')
        return render_template('index.html',productos = respuesta)

@app.route('/loginCliente',methods = ['GET'])
def loginCliente():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM CLIENTE')
        respuesta = cursor.fetchall()
        return render_template('login.html',cliente = respuesta)
    
@app.route('/obtenerCliente/<dni>')  #el id es lo que le pase entre llaves en el html
def obtenerCliente(dni):
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM CLIENTE WHERE dni = %s' % (dni)) #el numero que tengo en id lo igualo a nro
        respuesta = cursor.fetchall()
        return render_template('eliminarEditar.html',cliente = respuesta[0])
    
@app.route('/editarEliminar/<dni>', methods = ['GET'])
def editarEliminar(dni):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM CLIENTE where dni = %s' % (dni))
        respuesta = cursor.fetchall()
        return render_template('index.html', cliente = respuesta)
    
@app.route('/editarCliente/<dni>')  #el id es lo que le pase entre llaves en el html
def editarCliente(dni):
    cursor = mysql.connection.cursor()
    cur= mysql.connection.cursor()
    cursor.execute('SELECT * FROM CLIENTE WHERE dni = %s' % (dni)) #el numero que tengo en id lo igualo a nro
    cur.execute('SELECT * FROM DIRECCION')
    respuesta = cursor.fetchall()
    res = cur.fetchall()
    return render_template('editarCliente.html',cliente = respuesta[0],direccion = res)

@app.route('/actualizarCliente/<dni>',methods = ['POST'])#pasarle la variable como esta escrita en la base de datos
def actualizar(dni):
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        cursor = mysql.connection.cursor()
        cursor.execute("""UPDATE CLIENTE SET
        nombre = %s,
        id_direccion = %s
        WHERE dni =%s""",(nombre,direccion,dni)) #traigo los valores que tengo en la base de datos y se los paso en el update
        mysql.connection.commit()
        cur = mysql.connection.cursor()
        cur.execute('''SELECT 
        productos.nombre,
        productos.precio_por_unidad,
        productos.stock,
        productos.imagen,
        proveedor.nombre,
        marcas.nombre FROM PRODUCTOS, MARCAS, PROVEEDOR WHERE marcas.id = id_marcas AND proveedor.id = id_proveedor''')
        respuesta = cur.fetchall()
        flash('Cliente Actualizado')
        return render_template('index.html',productos = respuesta)
    
@app.route('/eliminarCliente/<string:dni>')  #el id es lo que le pase entre llaves en el html lo convierto en string
def eliminar(dni):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM CLIENTE WHERE dni = {0}'.format(dni)) #el numero que tengo en id lo igualo a nro
    mysql.connection.commit()#lo elimino
    cur = mysql.connection.cursor()
    cur.execute('''SELECT 
    productos.nombre,
    productos.precio_por_unidad,
    productos.stock,
    productos.imagen,
    proveedor.nombre,
    marcas.nombre FROM PRODUCTOS, MARCAS, PROVEEDOR WHERE marcas.id = id_marcas AND proveedor.id = id_proveedor''')
    respuesta = cur.fetchall()
    flash('Cliente Eliminado')
    return render_template('index.html',productos = respuesta)

@app.route('/registrarProducto',methods = ['GET','POST'])
def registrarProducto():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cur = mysql.connection.cursor()
        cursor.execute('SELECT * FROM PROVEEDOR')
        cur.execute('SELECT * FROM MARCAS')
        respuesta = cursor.fetchall()
        res = cur.fetchall()
        return render_template('registrarProducto.html', proveedor = respuesta,marcas = res)
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        imagen = request.form['imagen']
        proveedor = request.form['proveedor']
        marcas = request.form['marca']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PRODUCTOS (codigo,nombre,precio_por_unidad,stock,imagen,id_proveedor,id_marcas)VALUES(%s, %s, %s, %s, %s, %s,%s)",
        (codigo,nombre,precio,stock,imagen,proveedor,marcas)) #el porcentaje s significa que vas a poner los valores que te paso a continuacion
        mysql.connection.commit()
        curs = mysql.connection.cursor()
        curs.execute('''SELECT 
        productos.nombre,
        productos.precio_por_unidad,
        productos.stock,
        productos.imagen,
        proveedor.nombre,
        marcas.nombre FROM PRODUCTOS, MARCAS, PROVEEDOR WHERE marcas.id = id_marcas AND proveedor.id = id_proveedor''')
        respuesta = curs.fetchall()
        flash('Producto Registrado')
        return render_template('index.html',productos = respuesta)
    
@app.route('/editarProducto/<codigo>')  #el id es lo que le pase entre llaves en el html
def obtenerProducto(codigo):
    cursor = mysql.connection.cursor()
    cur= mysql.connection.cursor()
    cu= mysql.connection.cursor()
    cursor.execute('SELECT * FROM PRODUCTOS WHERE codigo = %s' % (codigo)) #el numero que tengo en id lo igualo a nro
    cur.execute('SELECT * FROM PROVEEDOR')
    cu.execute('SELECT * FROM MARCAS')
    respuesta = cursor.fetchall()
    res = cur.fetchall()
    re = cu.fetchall()
    return render_template('editarProducto.html',producto = respuesta[0],proveedor = res, marcas = re)

@app.route('/actualizarProducto/<codigo>',methods = ['POST'])#pasarle la variable como esta escrita en la base de datos
def actualizarProducto(codigo):
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        imagen = request.form['imagen']
        proveedor = request.form['proveedor']
        marcas = request.form['marca']
        cursor = mysql.connection.cursor()
        cursor.execute("""UPDATE PRODUCTOS SET
        nombre = %s,
        precio_por_unidad = %s,
        stock = %s,
        imagen = %s,
        id_proveedor = %s,
        id_marcas = %s
        WHERE codigo = %s""",(nombre,precio,stock,imagen,proveedor,marcas,codigo)) #traigo los valores que tengo en la base de datos y se los paso en el update
        mysql.connection.commit()
        cur = mysql.connection.cursor()
        cur.execute('''SELECT 
        productos.nombre,
        productos.precio_por_unidad,
        productos.stock,
        productos.imagen,
        proveedor.nombre,
        marcas.nombre FROM PRODUCTOS, MARCAS, PROVEEDOR WHERE marcas.id = id_marcas AND proveedor.id = id_proveedor''')
        respuesta = cur.fetchall()
        flash('Producto Actualizado')
        return render_template('index.html',productos = respuesta)
    
@app.route('/eliminarProducto/<string:codigo>')  #el id es lo que le pase entre llaves en el html lo convierto en string
def eliminarProducto(codigo):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM PRODUCTOS WHERE codigo = {0}'.format(codigo)) #el numero que tengo en id lo igualo a nro
    mysql.connection.commit()#lo elimino
    cur = mysql.connection.cursor()
    cur.execute('''SELECT 
    productos.nombre,
    productos.precio_por_unidad,
    productos.stock,
    productos.imagen,
    proveedor.nombre,
    marcas.nombre FROM PRODUCTOS, MARCAS, PROVEEDOR WHERE marcas.id = id_marcas AND proveedor.id = id_proveedor''')
    respuesta = cur.fetchall()
    flash('Producto Eliminado')
    return render_template('index.html',productos = respuesta)

@app.route('/registrarDireccion',methods=['POST', 'GET'])
def registrarDireccion():
    if request.method == 'GET':
        return render_template('registrarDireccion.html')
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        altura = request.form['altura']
        localidad = request.form['localidad']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO DIRECCION (id,nombre,altura,localidad)VALUES(%s, %s, %s, %s)",
        (id,nombre,altura,localidad)) #el porcentaje s significa que vas a poner los valores que te paso a continuacion
        mysql.connection.commit()
        flash('Direccion Registrada')
        cur = mysql.connection.cursor()
        cur.execute('''SELECT 
        productos.nombre,
        productos.precio_por_unidad,
        productos.stock,
        productos.imagen,
        proveedor.nombre,
        marcas.nombre FROM PRODUCTOS, MARCAS, PROVEEDOR WHERE marcas.id = id_marcas AND proveedor.id = id_proveedor''')
        respuesta = cur.fetchall()
        return render_template('index.html',productos = respuesta)

"""
 @app.route('/registrarFormaDePago',methods = ['POST'])
def registrarDireccion():
    if request.method == 'POST':
        numero = request.form['numero']
        fecha = request.form['fecha']
        hora = request.form['hora']
        ciudad = request.form['ciudad']
        personal = request.form['personal']
        patente = request.form['patente']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO VUELOS (nro,fecha,hora,ciudad,personal,patente)VALUES(%s, %s, %s, %s, %s, %s)",
        (numero,fecha,hora,ciudad,personal,patente)) #el porcentaje s significa que vas a poner los valores que te paso a continuacion
        mysql.connection.commit()
        flash('Registro Agregado')
        return redirect(url_for('index'))
        
@app.route('/registrarCarrito',methods = ['POST'])
def registrarCarrito():
    if request.method == 'POST':
        numero = request.form['numero']
        fecha = request.form['fecha']
        hora = request.form['hora']
        ciudad = request.form['ciudad']
        personal = request.form['personal']
        patente = request.form['patente']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO VUELOS (nro,fecha,hora,ciudad,personal,patente)VALUES(%s, %s, %s, %s, %s, %s)",
        (numero,fecha,hora,ciudad,personal,patente)) #el porcentaje s significa que vas a poner los valores que te paso a continuacion
        mysql.connection.commit()
        flash('Registro Agregado')
        return redirect(url_for('index'))
""" 
if __name__ == '__main__':
    app.run(port=3000, debug=True)