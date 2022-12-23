select * from circuito;



insert into circuito values(1, 'Bahrain International Circuit', TO_DATE('17/03/2004', 'DD/MM/YYYY'), 5.412, 15, 'https://a.espncdn.com/i/venues/f1/day/243.svg'  );
insert into circuito values(2, 'Jeddah Street Circuit', TO_DATE('3/12/2021', 'DD/MM/YYYY'), 5.154, 27, 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Jeddah_Street_Circuit_2021.svg/250px-Jeddah_Street_Circuit_2021.svg.png');
insert into circuito values(3, 'Albert Park Circuit' , TO_DATE('20/11/1953', 'DD/MM/YYYY'), 5.303, 16, 'https://a.espncdn.com/i/venues/f1/day/241.svg'  );
insert into circuito values(4,'Autodromo Internazionale Enzo e Dino Ferrari' , TO_DATE('25/04/1953', 'DD/MM/YYYY'), 4.909, 17, 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Imola_2009.svg/1920px-Imola_2009.svg.png');
insert into circuito values(5, 'Miami International Autodrome' , TO_DATE('6/05/2022', 'DD/MM/YYYY'), 5.41, 19, 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Hard_Rock_Stadium_Circuit_2022.svg/1920px-Hard_Rock_Stadium_Circuit_2022.svg.png');
insert into circuito values(6, 'Circuit de Barcelona-Catalunya', TO_DATE('10/09/1991', 'DD/MM/YYYY'), 4.665, 16, 'https://a.espncdn.com/i/venues/f1/day/238.svg');
insert into circuito values(7, 'Circuit de Monaco',TO_DATE('14/12/1929', 'DD/MM/YYYY'), 3.337, 19, 'https://a.espncdn.com/i/venues/f1/day/255.svg');
insert into circuito values(8, 'Baku City Circuit',TO_DATE('17/06/2016', 'DD/MM/YYYY'), 6.003, 20, 'https://a.espncdn.com/i/venues/f1/day/402.svg');
insert into circuito values(9, 'Circuit Gilles-Villeneuve',TO_DATE('06/10/1978', 'DD/MM/YYYY'), 4.361, 14, 'https://a.espncdn.com/i/venues/f1/day/51.svg');
insert into circuito values(10, 'Silverstone Circuit',TO_DATE('06/10/1978', 'DD/MM/YYYY'), 4.361, 14, 'https://a.espncdn.com/i/venues/f1/day/51.svg');


select * from corrida;
select * from epoca;

insert into corrida values(1, 'Gulf Air Bahrain Grand Prix',57, TO_DATE('20/03/2022', 'DD/MM/YYYY'), '21:30', 29, 49, 0, 10,0, 2022,1);
insert into corrida values(2, 'STC Saudi Arabian GP',57, TO_DATE('27/03/2022', 'DD/MM/YYYY'), '21:30', 31, 48, 0, 14,0, 2022,2)
insert into corrida values(3, 'Heineken Australian GP',58, TO_DATE('10/04/2022', 'DD/MM/YYYY'), '06:00', 22, 40, 0,33 38, 2022,3);
insert into corrida values(4, 'Rolex Emilia Romagna GP',62, TO_DATE('24/04/2022', 'DD/MM/YYYY'), '14:00', 25, 51, 0, 13,57, 2022,4);
insert into corrida values(5, 'Crypto.com Miami GP',57, TO_DATE('08/05/2022', 'DD/MM/YYYY'), '20:30', 25, 43, 0, 13,55, 2022,5);
insert into corrida values(6, 'Pirelli Spanish GP',62, TO_DATE('22/05/2022', 'DD/MM/YYYY'), '14:00', 35, 55, 0, 9,70, 2022,6);
insert into corrida values(7, 'Monaco GP',64, TO_DATE('29/05/2022', 'DD/MM/YYYY'), '14:00', 20, 40, 38, 60,7, 2022,7);
insert into corrida values(8, 'Azerbaijão GP',51, TO_DATE('12/06/2022', 'DD/MM/YYYY'), '21:00', 30, 48, 0, 12,0, 2022,8);
insert into corrida values(9, 'Pirelli Spanish GP',62, TO_DATE('22/05/2022', 'DD/MM/YYYY'), '14:00', 35, 55, 0, 9,70, 2022,6);
insert into corrida values(10, 'Pirelli Spanish GP',62, TO_DATE('22/05/2022', 'DD/MM/YYYY'), '14:00', 35, 55, 0, 9,70, 2022,6);


