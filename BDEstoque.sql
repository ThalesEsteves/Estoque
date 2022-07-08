drop database db_estoque;
create database db_estoque;
use db_estoque;

create table Produtos(
id int auto_increment,
descricao varchar(100) not null,
quantidade int,
primary key (id)
);

create table Fabricante(
id int auto_increment,
nome varchar(100) not null,
primary key (id)
);

alter table Produtos
add column id_fabricante int unique;
alter table Produtos
drop primary key;
alter table Produtos
add primary key(id,id_fabricante);
alter table Produtos
add foreign key(id_fabricante) references Fabricante(id);

select * from Fabricante;
select * from Produtos;