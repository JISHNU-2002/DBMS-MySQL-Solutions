# Setup MySQL

### **01 Install MySQL Server**

```bash
sudo apt update
```

```bash
sudo apt install mysql-server
```

### **02 Start the MySQL Service**

```bash
sudo service mysql start
```

- To enable MySQL to start on boot

```bash
sudo systemctl enable mysql
```

### **03 Secure MySQL Installation**
- MySQL provides a security script to improve the security of your MySQL installation

```bash
sudo mysql_secure_installation
```

- You'll be prompted to set up a root password, remove anonymous users, disallow root login remotely, remove test databases, and reload privilege tables. It's recommended to answer 'Yes' to all prompts

### **04 Access MySQL from the Terminal**

```bash
mysql -u root -p
```

- **`-u root`** specifies the username (root)
- **`-p`** prompts you to enter the root password you set during installation

### **Access MySQL as the System Root User**
- You need to log in to MySQL as the system's root user without requiring a password

```bash
sudo mysql
```

- This command should give you direct access to the MySQL shell

### **Change the Authentication Method for MySQL Root User**
- Once inside the MySQL shell, change the root user's authentication method to the traditional password-based method

```sql
USE mysql;
```

```SQL
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';
```

```SQL
FLUSH PRIVILEGES;
```

```SQL
exit;
```

- Replace `'your_password'` with a secure password of your choice

### **Reattempt Login with Password**
- Now, try logging in again with the new password you set

```bash
mysql -u root -p
```

- This process changes the root user's authentication method from `auth_socket` to `mysql_native_password`, allowing you to log in with a password
- After this, you should be able to access MySQL as the root user using the password you set

### **Optional: Revert Back to auth_socket**
- If you want to revert to the `auth_socket` method 

```bash
sudo mysql
```

```sql
USE mysql;
```

```SQL
ALTER USER 'root'@'localhost' IDENTIFIED WITH auth_socket;
```

```SQL
FLUSH PRIVILEGES;
```

```SQL
exit;
```

- This will revert the authentication method to the default `auth_socket`

### **05 Create a User and Grant Privileges (Optional)**
- You can create a new MySQL user and grant privileges

```sql
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

- Replace `'newuser'` with the desired username
- Replace `'password'` with the desired password

### **06 Access MySQL with the New User (Optional)**
- You can now access MySQL using the new user account

```bash
mysql -u newuser -p
```

- Enter the password you set for the new user

### **07 Exit MySQL**
To exit the MySQL shell, type:

```sql
exit;
```

# Database Initialization Using Bulk Import
- Using MySQL command-line
- **Bulk Import** in MySQL Workbench allows you to quickly load large amounts of data into a database table from a file, such as a CSV or SQL dump file

```SQL
SHOW VARIABLES LIKE "secure_file_priv"
```

![bulk](images/bulk_import.png)

- Move the CSV file to `/var/lib.mysql-files/`

```bash
sudo cp table_name.csv /var/lib.mysql-files/
```

- Load data into table (table_name)

```SQL
LOAD DATA INFILE '/var/lib.mysql-files/table_name.csv' 
INTO TABLE table_name 
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY "\n"
IGNORE 1 ROWS;
```


# MySQL Backup

**1. Using `mysqldump`**
- The `mysqldump` utility is the most commonly used method to back up MySQL databases
- It creates a text file with SQL statements to recreate the database schema and insert the data

**Basic Syntax:**
```bash
mysqldump -u [username] -p [database_name] > [backup_file.sql]
```

**Example:**
```bash
mysqldump -u root -p DEMO > DEMO.sql
```

- The `backup_file.sql` (in this case, `DEMO.sql`) will be saved in the current working directory from which you run the `mysqldump` command
- If you want to specify a different directory, you can provide a full path to the file:

```sql
mysqldump -u root -p demo > /path/to/your/backup/DEMO.sql
```


**2. Backing Up Multiple Databases**
- To back up multiple databases, use the `--databases` option

```bash
mysqldump -u root -p --databases db1 db2 > multiple_databases_backup.sql
```


**3. Backing Up All Databases**
- To back up all databases on the MySQL server, use the `--all-databases` option

```bash
mysqldump -u root -p --all-databases > all_databases_backup.sql
```


**4. Options for `mysqldump`**
- `--single-transaction`: Ensures a consistent backup by using a single transaction
- `--routines`: Includes stored routines and functions in the backup
- `--triggers`: Includes triggers in the backup

# MySQL Restore

**1. Using `mysql`**
- To restore a database from a backup file created by `mysqldump`, use the `mysql` command.

**Basic Syntax:**
```bash
mysql -u [username] -p [database_name] < [backup_file.sql]
```

**Example:**
```bash
mysql -u root -p DEMO < DEMO.sql
```


**2. Restoring to a New Database:**
- First create the database:
```sql
CREATE DATABASE new_database;
```
- Then restore it:
```bash
mysql -u root -p new_database < DEMO.sql
```

### Tips
- **Compression:** For large databases, consider compressing the backup file to save disk space. For example, use gzip:
  ```bash
  mysqldump -u root -p demo | gzip > demo_backup.sql.gz
  ```
- To restore:
  ```bash
  gunzip < demo_backup.sql.gz | mysql -u root -p demo
  ```

