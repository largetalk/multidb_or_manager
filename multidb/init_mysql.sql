
create database if not exists main_db;
grant all privileges on main_db.* to 'multidb'@'%' identified by '1234';
grant all privileges on main_db.* to 'multidb'@'localhost' identified by '1234';

create database if not exists sub_db1;
grant all privileges on sub_db1.* to 'sub1'@'%' identified by '1234';
grant all privileges on sub_db1.* to 'sub1'@'localhost' identified by '1234';

create database if not exists sub_db2;
grant all privileges on sub_db2.* to 'sub2'@'%' identified by '1234';
grant all privileges on sub_db2.* to 'sub2'@'localhost' identified by '1234';

BEGIN;
use main_db;
CREATE TABLE if not exists `project` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `project_code` varchar(20) NOT NULL UNIQUE,
    `db_name` varchar(50) NOT NULL,
    `db_user` varchar(50) NOT NULL,
    `db_passwd` varchar(50) NOT NULL,
    `db_host` varchar(50) NOT NULL,
    `db_port` integer NOT NULL
);


delete from project where project_code = 'abcd';
insert into project (project_code, db_name, db_user, db_passwd, db_host, db_port) 
values ("abcd", "sub_db1", "sub1", "1234", "localhost", 3306);

delete from project where project_code = 'efgh';
insert into project (project_code, db_name, db_user, db_passwd, db_host, db_port) 
values ("efgh", "sub_db2", "sub2", "1234", "localhost", 3306);

CREATE TABLE if not exists `django_session` (
    `session_key` varchar(40) NOT NULL PRIMARY KEY,
    `session_data` longtext NOT NULL,
    `expire_date` datetime NOT NULL
);

CREATE TABLE if not exists `main_entry` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL
);
COMMIT;

BEGIN;
use sub_db1;
CREATE TABLE if not exists `main_entry` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL
);

truncate table main_entry;
insert into main_entry ( name ) values ('sub1111111 main_entry');
COMMIT;

BEGIN;
use sub_db2;
CREATE TABLE if not exists `main_entry` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL
);

truncate table main_entry;
insert into main_entry ( name ) values ('sub2222222 main_entry');
COMMIT;

