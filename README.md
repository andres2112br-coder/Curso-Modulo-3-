# Base de Datos: Empleados y Departamentos

Modelo relacional en SQL (MySQL) para gestionar la plantilla de una empresa, con su esquema, datos de prueba y un set de consultas de explotación.

## Modelo de datos

```
Departamentos                    Empleados
─────────────                    ─────────
id_depto  (PK, AUTO_INCREMENT)   id_empleado     (PK, AUTO_INCREMENT)
nombre    (NOT NULL)             nombre          (NOT NULL)
                                 salario         (DECIMAL 10,2)
        1 ────────────────< N    fecha_contrato  (DATE)
                                 id_depto        (FK -> Departamentos)
```

Relación **uno a muchos**: un departamento tiene muchos empleados; cada empleado pertenece a un departamento.

## Decisiones de diseño

- **Clave foránea con constraint nombrado** (`fk_depto`) → garantiza la integridad referencial: no se puede asignar un empleado a un departamento que no existe.
- **`DECIMAL(10,2)` para el salario** en lugar de `FLOAT` → evita los errores de redondeo del punto flotante, inaceptables cuando se trata de dinero.
- **Departamentos en tabla aparte** en lugar de repetir el nombre en cada empleado → elimina la duplicación de datos y permite renombrar un departamento en un solo lugar.

## Contenido del script

| Sección | Qué hace |
|---|---|
| DDL | Creación de las 2 tablas con PK, FK y constraints |
| Datos de prueba | 4 departamentos y 10 empleados |
| Consultas | Filtrado por salario, ranking Top 5, agrupación por departamento |
| Modificaciones | UPDATE con incremento salarial del 10%, DELETE por antigüedad |
| JOIN | Cruce de empleados con el nombre de su departamento |

## Cómo ejecutarlo

```bash
mysql -u tu_usuario -p nombre_base_datos < bd_empleados.sql
```

O pegar el contenido en MySQL Workbench / phpMyAdmin.

## Consultas destacadas

**Top 5 salarios más altos**
```sql
SELECT   nombre, salario
FROM     Empleados
ORDER BY salario DESC
LIMIT    5;
```

**Empleados con el nombre de su departamento (JOIN)**
```sql
SELECT e.nombre AS 'Nombre Empleado',
       d.nombre AS 'Departamento'
FROM   Empleados e
JOIN   Departamentos d ON e.id_depto = d.id_depto;
```

## Qué aprendí

Que el diseño de la base de datos condiciona todo lo demás: separar los departamentos en su propia tabla parecía trabajo extra al principio, pero es lo que hace posible el JOIN y lo que evita tener que actualizar diez filas cuando un departamento cambia de nombre.

## Tecnologías

`SQL` · `MySQL` · `Modelado relacional` · `JOIN` · `Integridad referencial`

---
Andrés Barros · Estudiante de Ingeniería de Sistemas
