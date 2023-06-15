drop database if exists gamerbuy;
create database gamerbuy;
use gamerbuy;

create table carrito(
id int primary key not null,
fecha date not null,
cantidad int,
precio int,
precio_total int,
nro_forma_de_pago int not null,
dni_cliente int not null,
codigo_producto int not null
);

create table cliente(
dni int primary key not null,
nombre varchar(50) not null,
id_direccion int not null
);

create table direccion(
id int primary key not null,
nombre varchar(50) not null,
altura int not null,
localidad varchar(50) not null
);

create table productos(
codigo int primary key not null,
nombre varchar(50) not null,
precio_por_unidad int,
stock int,
imagen varchar(255),
id_proveedor int not null,
id_marcas int not null
);

create table proveedor(
id int primary key not null,
nombre varchar(50) not null,
id_direccion int not null
);

create table marcas(
id int primary key not null,
nombre varchar(50) not null
);

create table forma_de_pago(
nro_tarjeta int primary key not null,
tipo enum('Efectivo','Debito') not null,
nombre_tarjeta varchar(50) not null
);

alter table cliente
add foreign key(id_direccion)
references direccion(id);

alter table productos
add foreign key(id_proveedor)
references proveedor(id);

alter table productos
add foreign key(id_marcas)
references marcas(id);

alter table proveedor
add foreign key(id_direccion)
references direccion(id);

alter table carrito
add foreign key(nro_forma_de_pago)
references forma_de_pago(nro_tarjeta);

alter table carrito
add foreign key(dni_cliente)
references cliente(dni);

alter table carrito
add foreign key(codigo_producto)
references productos(codigo);




