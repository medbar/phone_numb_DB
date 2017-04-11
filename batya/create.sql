/*
create database db_Russian_Numbering_plan;
use db_Russian_Numbering_plan;
*/


DROP TABLE IF EXISTS phone_numbers;
DROP TABLE IF EXISTS regions;
DROP TABLE IF EXISTS operators;


create table regions(
    id int unique not null  primary key,
	`name` varchar(255) CHARACTER SET utf8
);

create table operators(
	id int  unique not null primary key,
	`name` varchar(255) CHARACTER SET utf8
); 

create table phone_numbers(
id int not null auto_increment primary key,
ABC smallint not null,
`from` int not null,
`to` int not null,
operator_id int,
region_id  int,
Foreign key (region_id) references regions(`id`),
foreign key (operator_id) references operators(`id`)
);


/*-------------------------------PROCEDURES---------------------------------------*/


DROP procedure IF EXISTS Capacity;
DROP procedure IF EXISTS insert_new_record;
DELIMITER //
create procedure Capacity(curr_id int)
begin
	select pn.to-pn.from 
    from phone_number as pn 
    where pn.id = curr_id;
end//



DELIMITER //
create procedure insert_new_record(_ABC smallint,
								   `_from` int ,
								   `_to` int,
                                   _operator varchar(255),
								   region_name varchar(255))

begin
	
	
    insert ignore into  regions (`name`) values(region_name);
	set @last_region_id = LAST_INSERT_ID();
    insert ignore into  operators (`name`) values(_operator);
	set @last_operator_id = LAST_INSERT_ID();
    insert into phone_numbers(ABC, `from`, `to`,operator_id, region_id) values(_ABC, `_from`, `_to`, @last_region_id , @last_region_id); 
    
end//
