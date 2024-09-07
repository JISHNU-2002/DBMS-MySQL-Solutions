# CASE STUDY - COMPANY 02

# Set Operators, Nested Queries & Joins
## 1. **Set Operators**

- **UNION**

```sql
SELECT name FROM EMPLOYEES
UNION
SELECT project_name FROM PROJECTS;
```

![union](images/union.png)

- **INTERSECT**

```sql
SELECT employee_id  FROM EMPLOYEES 
INTERSECT 
SELECT employee_id FROM PROJECTS;
```

![intersect](images/intersect.png)

- **EXCEPT**

```sql
SELECT name FROM EMPLOYEES
EXCEPT
SELECT 'Alice' AS name FROM PROJECTS;
```

![except](images/except.png)

## 2. **Nested Queries (Subqueries)**

- **Subquery in a WHERE Clause**
	- This query finds all employees who work in the same department as 'Alice'

```sql
SELECT name FROM EMPLOYEES
WHERE department = (SELECT department FROM EMPLOYEES WHERE name = 'Alice');
```

![sub1](images/sub1.png)

- **Subquery with `IN`**
	- This query finds the names of employees who are working on 'Project Alpha'

```sql
SELECT name FROM EMPLOYEES
WHERE employee_id IN 
	(SELECT employee_id FROM PROJECTS WHERE project_name = 'Project Alpha');
```

![sub2](images/sub2.png)

## 3. **Joins**

![update](images/update.png)

- **INNER JOIN**
	- This query retrieves the names of employees and their respective project names

```sql
SELECT EMPLOYEES.name, PROJECTS.project_name
FROM EMPLOYEES
INNER JOIN PROJECTS ON EMPLOYEES.employee_id = PROJECTS.employee_id;
```

![inner_join](images/inner_join.png)

- **LEFT JOIN** (or **LEFT OUTER JOIN**)
	- This query retrieves all employees, even those who are not assigned to any projects

```sql
SELECT EMPLOYEES.name, PROJECTS.project_name
FROM EMPLOYEES
LEFT JOIN PROJECTS ON EMPLOYEES.employee_id = PROJECTS.employee_id;
```

![left_join](images/left_join.png)

- **RIGHT JOIN** (or **RIGHT OUTER JOIN**)
	- This query retrieves all projects, including those that do not have any employees assigned

```sql
SELECT EMPLOYEES.name, PROJECTS.project_name
FROM EMPLOYEES
RIGHT JOIN PROJECTS ON EMPLOYEES.employee_id = PROJECTS.employee_id;
```

![right_join](images/right_join.png)

- **FULL JOIN** (or **FULL OUTER JOIN**)
	- This query retrieves all employees and all projects, matching them where possible

```sql
SELECT EMPLOYEES.name, PROJECTS.project_name
FROM EMPLOYEES
LEFT JOIN PROJECTS ON EMPLOYEES.employee_id = PROJECTS.employee_id

UNION

SELECT EMPLOYEES.name, PROJECTS.project_name
FROM PROJECTS
RIGHT JOIN EMPLOYEES ON EMPLOYEES.employee_id = PROJECTS.employee_id;
```

![full_join](images/full_join.png)