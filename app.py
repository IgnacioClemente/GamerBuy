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
def listadoProductos():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM PRODUCTOS')
    respuesta = cursor.fetchall()
    return render_template('listadoProductos.html',productos = respuesta)

@app.route('/listadoDirecciones')
def listadoDirecciones():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM DIRECCION')
    respuesta = cursor.fetchall()
    return render_template('listadoDirecciones.html',direccion = respuesta)

@app.route('/listadoFormasDePago')
def listadoFormasDePago():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM FORMA_DE_PAGO')
    respuesta = cursor.fetchall()
    return render_template('listadoFormasDePago.html',forma = respuesta)

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

@app.route('/administrarUsuarios',methods = ['GET'])
def administrarUsuarios():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM CLIENTE')
        respuesta = cursor.fetchall()
        return render_template('administrarUsuarios.html',cliente = respuesta)
    
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
def actualizarCliente(dni):
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
def eliminarCliente(dni):
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
        cur = mysql.connection.cursor()
        cur.execute('''SELECT 
        productos.nombre,
        productos.precio_por_unidad,
        productos.stock,
        productos.imagen,
        proveedor.nombre,
        marcas.nombre FROM PRODUCTOS, MARCAS, PROVEEDOR WHERE marcas.id = id_marcas AND proveedor.id = id_proveedor''')
        respuesta = cur.fetchall()
        flash('Direccion Registrada')
        return render_template('index.html',productos = respuesta)
    
@app.route('/editarDireccion/<id>')  #el id es lo que le pase entre llaves en el html
def editarDireccion(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM DIRECCION WHERE id = %s' % (id)) #el numero que tengo en id lo igualo a nro
    respuesta = cursor.fetchall()
    return render_template('editarDireccion.html',direccion = respuesta[0])

@app.route('/actualizarDireccion/<id>',methods = ['POST'])#pasarle la variable como esta escrita en la base de datos
def actualizarDireccion(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        altura = request.form['altura']
        localidad = request.form['localidad']
        cursor = mysql.connection.cursor()
        cursor.execute("""UPDATE DIRECCION SET
        nombre = %s,
        altura = %s,
        localidad = %s
        WHERE id = %s""",(nombre,altura,localidad,id)) #traigo los valores que tengo en la base de datos y se los paso en el update
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
    
@app.route('/eliminarDireccion/<string:id>')  #el id es lo que le pase entre llaves en el html lo convierto en string
def eliminarDireccion(id):
    cursor = mysql.connection.cursor()
    curs = mysql.connection.cursor()
    cursor.execute('DELETE FROM DIRECCION WHERE id = {0}'.format(id)) 
    curs.execute('DELETE FROM CLIENTE WHERE id_direccion = {0}'.format(id)) #el numero que tengo en id lo igualo a nro
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
    flash('Dirección Eliminada')
    return render_template('index.html',productos = respuesta)

@app.route('/registrarFormaDePago',methods = ['POST','GET'])
def registrarFormaDePago():
    if request.method == 'GET':
        return render_template('registrarFormaDePago.html')
    if request.method == 'POST':
        numero = request.form['numero']
        tipo = request.form['tipo']
        nombre = request.form['nombre']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO FORMA_DE_PAGO (nro_tarjeta,tipo,nombre_tarjeta)VALUES(%s, %s, %s)",
        (numero,tipo,nombre)) #el porcentaje s significa que vas a poner los valores que te paso a continuacion
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
        flash('Forma de pago Agregada')
        return render_template('index.html',productos = respuesta)
    
@app.route('/editarFormaDePago/<nro_tarjeta>')  #el id es lo que le pase entre llaves en el html
def editarFormaDePago(nro_tarjeta):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM FORMA_DE_PAGO WHERE nro_tarjeta = %s' % (nro_tarjeta)) #el numero que tengo en id lo igualo a nro
    respuesta = cursor.fetchall()
    return render_template('editarFormaDePago.html',forma = respuesta[0])

@app.route('/actualizarFormaDePago/<nro_tarjeta>',methods = ['POST'])#pasarle la variable como esta escrita en la base de datos
def actualizarFormaDePago(nro_tarjeta):
    if request.method == 'POST':
        tipo = request.form['tipo']
        nombre = request.form['nombre']
        cursor = mysql.connection.cursor()
        cursor.execute("""UPDATE FORMA_DE_PAGO SET
        tipo = %s,
        nombre_tarjeta = %s
        WHERE nro_tarjeta = %s""",(tipo,nombre,nro_tarjeta)) #traigo los valores que tengo en la base de datos y se los paso en el update
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
        flash('Forma de pago Actualizado')
        return render_template('index.html',productos = respuesta)
    
@app.route('/eliminarFormaDePago/<string:nro_tarjeta>')  #el id es lo que le pase entre llaves en el html lo convierto en string
def eliminarFormaDePago(nro_tarjeta):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM FORMA_DE_PAGO WHERE nro_tarjeta = {0}'.format(nro_tarjeta)) 
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
    flash('Forma de pago Eliminada')
    return render_template('index.html',productos = respuesta)

@app.route('/registrarCarrito',methods = ['POST','GET'])
def registrarCarrito():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cur = mysql.connection.cursor()
        cu = mysql.connection.cursor()
        cursor.execute('SELECT * FROM FORMA_DE_PAGO')
        cur.execute('SELECT * FROM CLIENTE')
        cu.execute('SELECT * FROM PRODUCTOS')
        respuesta = cursor.fetchall()
        resp = cur.fetchall()
        res = cu.fetchall()
        return render_template('registrarCarrito.html', forma = respuesta,cliente = resp, productos = res )
    if request.method == 'POST':
        id = request.form['id']
        fecha = request.form['fecha']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        precio_total = request.form['precio_total']
        forma = request.form['forma']
        dni = request.form['dni']
        codigo = request.form['codigo']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO CARRITO (id,fecha,cantidad,precio,precio_total,nro_forma_de_pago,dni_cliente,codigo_producto)VALUES(%s, %s, %s, %s, %s, %s,%s,%s)",
        (id,fecha,cantidad,precio,precio_total,forma,dni,codigo)) #el porcentaje s significa que vas a poner los valores que te paso a continuacion
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
        flash('Carrito Agregado')
        return render_template('index.html',productos = respuesta)
    
if __name__ == '__main__':
    app.run(port=3000, debug=True)