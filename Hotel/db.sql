create database Hotel_Room_Management;
use Hotel_Room_Management;
CREATE TABLE RoomDetails
(
  roomNo VARCHAR(10) primary key,
  name VARCHAR(45) not null,
  email VARCHAR(80) not null,
  phone VARCHAR(20) not null
);
insert into RoomDetails values (101,'Swetha','swetha@gmail.com',6382280320);
insert into RoomDetails values (102,'Nandhu','nandhu@gmail.com',9865260970);
insert into RoomDetails values (103,'Priya','priya@gmail.com',7373465231);
select * from RoomDetails;