CREATE TABLE piloto (
	pilotoid	 SERIAL,
	nome		 VARCHAR(512),
	nacionalidade VARCHAR(512),
	nascimento	 DATE,
	foto		 VARCHAR(512),
	PRIMARY KEY(pilotoid)
);

CREATE TABLE construtor (
	construtorid	 BIGSERIAL,
	nome		 VARCHAR(512),
	nacionalidade VARCHAR(512),
	logo		 VARCHAR(512),
	criadoem	 DATE,
	PRIMARY KEY(construtorid)
);

CREATE TABLE corrida (
	ronda		 SERIAL,
	nome		 VARCHAR(512) NOT NULL,
	voltas		 INTEGER,
	ocorreem		 DATE,
	horas		 VARCHAR(512) NOT NULL,
	temperatura	 INTEGER,
	temperaturacircuito INTEGER,
	precipitacao	 INTEGER,
	humidade		 INTEGER,
	exposicaosolar	 INTEGER,
	epoca_ano		 INTEGER NOT NULL,
	circuito_circuitoid INTEGER NOT NULL,
	PRIMARY KEY(ronda)
);

CREATE TABLE circuito (
	circuitoid	 SERIAL,
	nome	 VARCHAR(512),
	criadoem	 DATE,
	comprimento DOUBLE PRECISION,
	curvas	 INTEGER,
	foto	 VARCHAR(512),
	PRIMARY KEY(circuitoid)
);

CREATE TABLE epoca (
	ano INTEGER,
	PRIMARY KEY(ano)
);

CREATE TABLE resultados (
	resultadoid	 SERIAL,
	posinicio	 INTEGER NOT NULL,
	posfinal	 INTEGER,
	tempototal	 INTEGER,
	voltarapida	 INTEGER,
	corrida_ronda	 INTEGER,
	piloto_pilotoid INTEGER,
	PRIMARY KEY(resultadoid,corrida_ronda,piloto_pilotoid)
);

CREATE TABLE comentario (
	comentarioid			 SERIAL,
	nome				 VARCHAR(80),
	corpo				 VARCHAR(2000),
	criadoem			 DATE,
	corrida_ronda			 INTEGER,
	noticia_noticiaid		 INTEGER,
	noticia_circuito_circuitoid	 INTEGER,
	noticia_corrida_ronda		 INTEGER,
	noticia_construtor_construtorid BIGINT,
	noticia_piloto_pilotoid	 INTEGER,
	PRIMARY KEY(comentarioid,corrida_ronda,noticia_noticiaid,noticia_circuito_circuitoid,noticia_corrida_ronda,noticia_construtor_construtorid,noticia_piloto_pilotoid)
);

CREATE TABLE noticia (
	noticiaid		 SERIAL,
	titulo			 VARCHAR(50) NOT NULL,
	corpo			 VARCHAR(5000),
	foto			 VARCHAR(512),
	criadoem		 DATE,
	circuito_circuitoid	 INTEGER,
	corrida_ronda		 INTEGER,
	construtor_construtorid BIGINT,
	piloto_pilotoid	 INTEGER,
	PRIMARY KEY(noticiaid,circuito_circuitoid,corrida_ronda,construtor_construtorid,piloto_pilotoid)
);

CREATE TABLE equipa (
	equipaid		 BIGSERIAL,
	chefe			 VARCHAR(512),
	chefetecnico		 VARCHAR(512),
	chassis		 VARCHAR(512),
	foto_carro		 VARCHAR(512),
	construtor_construtorid BIGINT,
	epoca_ano		 INTEGER NOT NULL,
	PRIMARY KEY(equipaid,construtor_construtorid)
);

CREATE TABLE piloto_equipa (
	piloto_pilotoid		 INTEGER,
	equipa_equipaid		 BIGINT,
	equipa_construtor_construtorid BIGINT,
	PRIMARY KEY(piloto_pilotoid,equipa_equipaid,equipa_construtor_construtorid)
);

ALTER TABLE corrida ADD CONSTRAINT corrida_fk1 FOREIGN KEY (epoca_ano) REFERENCES epoca(ano);
ALTER TABLE corrida ADD CONSTRAINT corrida_fk2 FOREIGN KEY (circuito_circuitoid) REFERENCES circuito(circuitoid);
ALTER TABLE resultados ADD CONSTRAINT resultados_fk1 FOREIGN KEY (corrida_ronda) REFERENCES corrida(ronda);
ALTER TABLE resultados ADD CONSTRAINT resultados_fk2 FOREIGN KEY (piloto_pilotoid) REFERENCES piloto(pilotoid);
ALTER TABLE comentario ADD CONSTRAINT comentario_fk1 FOREIGN KEY (corrida_ronda) REFERENCES corrida(ronda);
ALTER TABLE comentario ADD CONSTRAINT comentario_fk2 FOREIGN KEY (noticia_noticiaid, noticia_circuito_circuitoid, noticia_corrida_ronda, noticia_construtor_construtorid, noticia_piloto_pilotoid) REFERENCES noticia(noticiaid, circuito_circuitoid, corrida_ronda, construtor_construtorid, piloto_pilotoid);
ALTER TABLE noticia ADD CONSTRAINT noticia_fk1 FOREIGN KEY (circuito_circuitoid) REFERENCES circuito(circuitoid);
ALTER TABLE noticia ADD CONSTRAINT noticia_fk2 FOREIGN KEY (corrida_ronda) REFERENCES corrida(ronda);
ALTER TABLE noticia ADD CONSTRAINT noticia_fk3 FOREIGN KEY (construtor_construtorid) REFERENCES construtor(construtorid);
ALTER TABLE noticia ADD CONSTRAINT noticia_fk4 FOREIGN KEY (piloto_pilotoid) REFERENCES piloto(pilotoid);
ALTER TABLE equipa ADD CONSTRAINT equipa_fk1 FOREIGN KEY (construtor_construtorid) REFERENCES construtor(construtorid);
ALTER TABLE equipa ADD CONSTRAINT equipa_fk2 FOREIGN KEY (epoca_ano) REFERENCES epoca(ano);
ALTER TABLE piloto_equipa ADD CONSTRAINT piloto_equipa_fk1 FOREIGN KEY (piloto_pilotoid) REFERENCES piloto(pilotoid);
ALTER TABLE piloto_equipa ADD CONSTRAINT piloto_equipa_fk2 FOREIGN KEY (equipa_equipaid, equipa_construtor_construtorid) REFERENCES equipa(equipaid, construtor_construtorid);

