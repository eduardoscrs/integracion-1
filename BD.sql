CREATE TABLE Usuario (
    ID smallint(5) unsigned autoincrement,
    Nombre varchar(50),
    Apellido varchar(50),
    Correo varchar(255),
    Contraseña varchar(16)
);


CREATE TABLE Productos (
    ID smallint(5) unsigned autoincrement,
    Nombre varchar(50),
    Descripcion text(1800),
    Precio mediumint(8) unsigned,
    PorcentajeDescuento decimal(3,2),
    Almacenamiento int(10), 
);  

CREATE TABLE Envio(
    ID smallint(5) unsigned autoincrement,
    ID Producto smallint(5) unsigned,
    Pais varchar(50),
    Ciudad varchar(50),
    Calle varchar(50),
    FechaCompra datetime,
    FechaLlegada datetime,
    Precio mediumint(8) unsigned,
    CantidadTotalProductos mediumint(4)

    FOREIGN KEY (ID_Prducto) REFERENCES Producto(ID)
);

CREATE TABLE CarritoCompra(
    ID smallint(5) unsigned autoincrement,
    ID_Usuario smallint(5) unsigned,
    ID_Prducto smallint(5) unsigned,
    Precio mediumint(8) unsigned,
    PreciTotal mediumint(8) unsigned,
    Cantidad mediumint(4) unsigned,
)

CREATE TABLE Boleta(
    ID smallint(5) unsigned autoincrement,
    ID_Prducto smallint(5) unsigned,
    Fecha_Hora datetime,
    Precio mediumint(8) unsigned,
    PreciTotal mediumint(8) unsigned,

    FOREIGN KEY (ID_Prducto) REFERENCES Producto(ID)
)

CREATE TABLE HistorialCompras(
    ID smallint(5) unsigned autoincrement,
    ID_Usuario smallint(5) unsigned,
    ID_Prducto smallint(5) unsigned,
    ID_Envio smallint(5) unsigned,
)

CREATE TABLE Envio(
    ID smallint(5) unsigned autoincrement,
    Pais varchar(50),
    Ciudad varchar(50),
)