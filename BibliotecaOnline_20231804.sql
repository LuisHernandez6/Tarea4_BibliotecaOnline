CREATE DATABASE BibliotecaOnline_20231804;
GO
USE BibliotecaOnline_20231804;
GO

CREATE TABLE Libros (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Titulo NVARCHAR(255),
    Autor NVARCHAR(255),
    Precio DECIMAL(10,2),
    Stock INT
);

CREATE TABLE Usuarios (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    NombreUsuario NVARCHAR(50) NOT NULL,
    [Password] NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) NOT NULL,
    Rol NVARCHAR(20) NOT NULL
);

INSERT INTO Usuarios (NombreUsuario, [Password], Email, Rol)
VALUES ('admin', '1234', 'admin@mail.com', 'Admin');

INSERT INTO Libros (Titulo, Autor, Precio, Stock)
VALUES ('Harry Potter', 'J. K. Rowling', '59.0', '5');
