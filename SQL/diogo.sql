insert into epoca values (2022);

insert into construtor(nome,nacionalidade,logo,criadoem) values 
('Red Bull Racing', 'Milton Keynes, Reino Unido', 'https://www.formula1.com/content/fom-website/en/teams/Red-Bull-Racing/_jcr_content/logo.img.jpg/1645620474276.jpg', TO_DATE('2004', 'YYYY'));
insert into equipa(chefe,chefetecnico,chassis,foto_carro,construtor_construtorid, epoca_ano) values
('Christian Horner', 'Pierre Waché', 'RB18', 'https://img.redbull.com/images/c_fill,w_2880,h_1460,g_auto,f_auto,q_auto/redbullcom/2022/4/29/rts6bfco94systkflbvf/rb18-hero',1, 2022);

insert into construtor(nome,nacionalidade,logo,criadoem) values 
('Mercedes-AMG Formula One Team', 'Brackley, Reino Unido', 'https://www.formula1.com/content/fom-website/en/teams/Mercedes/_jcr_content/logo.img.jpg/1582638425211.jpg', TO_DATE('1970', 'YYYY'));
insert into equipa(chefe,chefetecnico,chassis,foto_carro,construtor_construtorid, epoca_ano) values
('Toto Wolff', 'Mike Elliott', 'W13', 'https://cdn-1.motorsport.com/images/amp/2d1n8D5Y/s1000/formula-1-mercedes-launch-2022-2.jpg',2, 2022);

insert into construtor(nome,nacionalidade,logo,criadoem) values 
('Scuderia Ferrari', 'Maranello, Itália', 'https://www.formula1.com/content/fom-website/en/teams/Ferrari/_jcr_content/logo.img.jpg/1521797474166.jpg', TO_DATE('1950', 'YYYY'));
insert into equipa(chefe,chefetecnico,chassis,foto_carro,construtor_construtorid, epoca_ano) values
('Mattia Binotto', 'Enrico Gualtieri', 'F1-75', 'https://www.razaoautomovel.com/wp-content/uploads/2022/03/Ferrari-F1-75-6.jpg',3, 2022);



/*
insert into construtor(nome,nacionalidade,logo,criadoem) values 
('', ', Reino Unido', '', TO_DATE('2004', 'YYYY'));
insert into construtorequipa(chefe,chefetecnico,chassis,foto_carro,construtor_construtorid, epoca_ano) values
('', '', '', '',2, 2022);
*/

