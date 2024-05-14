0x14. MySQL
DevOps SysAdmin MySQL

Task 00:
Installation of MySQL 5.7.x on both web-01 and web-02 servers.

Task 01:
Creates a user and password for both MySQL databases which will allow the checker access to them.

Task 02:
Creates a database=tyrell_corp having table=nexus6
Gives the user holberton_user SELECT permissions on the table

Task 03:
Create a new user for the replica server.
user=replica_user, hostname=%, password
replica_user must have the appropriate permissions to replicate your primary MySQL server.
holberton_user will need SELECT privileges on the mysql.user table in order to check that replica_user was created with the correct permissions.
