insert into forma_de_pago(nro_tarjeta,tipo,nombre_tarjeta) values(342432432,'Efectivo','Visa');

insert into direccion(id,nombre,altura,localidad) values(345252,'Penyo',4242,'Deboto');

insert into cliente(dni,nombre,id_direccion) values(535326,'Esteban',345252);

insert into proveedor(id,nombre,id_direccion) values(24242,'Expoyo',345252);

insert into marcas(id,nombre) values(532,'AMD');

insert into productos(codigo,nombre,precio_por_unidad,stock,imagen,id_proveedor,id_marcas) values(35232,'Procesador',424524,4,null,24242,532);

insert into carrito(id,fecha,cantidad,precio,precio_total,nro_forma_de_pago,dni_cliente,codigo_producto) values(2424,'2012-04-16',1,424524,424524,342432432,535326,35232);