# DNS-model
Simple DNS server model using MySQL database.
## Installation 
Download and install MySQL from
 - [Download MySQL](https://www.mysql.com/downloads/)
## Creating Database in MySQL

#### Create new Database

```http
  create database DNS
```

#### Create new Table

```http
//use DNS database
  use DNS
//create Table
  create table dns-model(
  domain_name varchar(200) not null primary key,
  ip_address varchar(100) not null
  );
```

#### Insert values in Table

```http
//insert values
  insert into dns-model values(
  'www.google.com',
  '127.00.01.05'
  );
```
#### Select from Table

```http
//select from dns-model table
  select * from dns-model;
```
| domain_name | ip_address     | 
| :-------- | :------- | 
| www.google.com | 127.00.01.05 |
#### Select ip_address 

```http
//select from dns-model table
  select ip_address from dns-model where domain_name = 'www.google.com';
```
| ip_address     | 
| :------- | 
| 127.00.01.05 |
