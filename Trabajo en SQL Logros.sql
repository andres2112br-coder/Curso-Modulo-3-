CREATE TABLE Departamentos (
    id_depto INT          PRIMARY KEY AUTO_INCREMENT,
    nombre   VARCHAR(80)  NOT NULL
);

CREATE TABLE Empleados (
    id_empleado    INT           PRIMARY KEY AUTO_INCREMENT,
    nombre         VARCHAR(100)  NOT NULL,
    salario        DECIMAL(10,2) NOT NULL,
    fecha_contrato DATE          NOT NULL,
    id_depto       INT,
    CONSTRAINT fk_depto
        FOREIGN KEY (id_depto)
        REFERENCES Departamentos(id_depto)
);




INSERT INTO Departamentos (nombre)
VALUES
    ('Tecnología'),
    ('Recursos Humanos'),
    ('Finanzas'),
    ('Marketing');



INSERT INTO Empleados (nombre, salario, fecha_contrato, id_depto)
VALUES
    ('Ana Torres',     3500.00, '2021-03-15', 1),
    ('Luis Pérez',     2800.00, '2018-07-01', 2),  
    ('María López',    5200.00, '2022-11-20', 3),
    ('Carlos Ruiz',    4800.00, '2020-05-10', 1),
    ('Sofía Méndez',   6100.00, '2023-01-08', 4),
    ('Pedro Castillo', 3100.00, '2017-09-25', 2),  
    ('Laura Gómez',    4500.00, '2021-06-30', 3),
    ('Jorge Vargas',   5900.00, '2022-03-14', 1),
    ('Elena Ramos',    2600.00, '2019-12-01', 4),  
    ('Diego Flores',   7200.00, '2023-08-19', 3);




SELECT nombre, salario
FROM   Empleados
WHERE  salario > 3000;



UPDATE Empleados
SET    salario = salario * 1.10
WHERE  id_empleado = 1;



DELETE FROM Empleados
WHERE  fecha_contrato < '2020-01-01';



SELECT   nombre, salario
FROM     Empleados
ORDER BY salario DESC
LIMIT    5;



SELECT
    e.nombre AS 'Nombre Empleado',
    d.nombre AS 'Nombre Departamento'
FROM       Empleados    e
INNER JOIN Departamentos d
    ON e.id_depto = d.id_depto;




SELECT
    d.nombre             AS Departamento,
    COUNT(e.id_empleado) AS Total_Empleados,
    SUM(e.salario)       AS Gasto_Total
FROM       Empleados    e
INNER JOIN Departamentos d
    ON e.id_depto = d.id_depto
GROUP BY   d.id_depto, d.nombre;



SELECT
    d.nombre       AS Departamento,
    AVG(e.salario) AS Salario_Promedio
FROM       Empleados    e
INNER JOIN Departamentos d
    ON e.id_depto = d.id_depto
GROUP BY   d.id_depto, d.nombre
HAVING     AVG(e.salario) > 4000;