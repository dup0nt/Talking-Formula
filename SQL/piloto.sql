insert into piloto(nome, nacionalidade, nascimento, foto) values 
('Max Verstappen', 'Paises Baixos', TO_DATE('30/09/1997', 'DD/MM/YYYY'), 'https://www.formula1.com/content/fom-website/en/drivers/max-verstappen/jcr:content/image.img.1920.medium.jpg/1670841844162.jpg');
insert into piloto_equipa values (1,1,1);

insert into piloto(nome, nacionalidade, nascimento, foto) values 
('Sergio Perez', 'México', TO_DATE('26/01/1990', 'DD/MM/YYYY'), 'https://www.formula1.com/content/fom-website/en/drivers/sergio-perez/jcr:content/image.img.1920.medium.jpg/1669048529570.jpg'
);
insert into piloto_equipa values (2,1,1);

insert into piloto(nome, nacionalidade, nascimento, foto) values 
('Lewis Hamilton', 'Reino Unido', TO_DATE('07/01/1985', 'DD/MM/YYYY'), 'https://www.formula1.com/content/fom-website/en/drivers/lewis-hamilton/jcr:content/image.img.1920.medium.jpg/1647334259839.jpg'
);
insert into piloto_equipa values (3,2,2);

insert into piloto(nome, nacionalidade, nascimento, foto) values 
('George Russel', 'Reino Unido', TO_DATE('15/02/1998', 'DD/MM/YYYY'), 'https://www.formula1.com/content/fom-website/en/drivers/george-russell/jcr:content/image.img.1920.medium.jpg/1670253611700.jpg'
);
insert into piloto_equipa values (4,2,2);

insert into piloto(nome, nacionalidade, nascimento, foto) values 
('Michael Schumacher', 'Alemanha', TO_DATE('03/01/1969', 'DD/MM/YYYY'), 'https://prabook.com/web/show-photo-icon.jpg?id=1918771&width=220&cache=false');

select * from piloto