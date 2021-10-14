CREATE_DATABASE_SQL = """\
DROP DATABASE IF EXISTS cadastros;
CREATE DATABASE cadastros;
USE cadastros;
"""

CREATE_TABLE_SQL = """\
CREATE TABLE IF NOT EXISTS usuario (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(100),
  email VARCHAR(100),
  nome_usuario VARCHAR(50),
  senha VARCHAR(50),
  data_nascimento DATE,
  idade SMALLINT,
  telefone VARCHAR(20)
);
"""

INSERT_DATA_SQL = """\
INSERT INTO usuario
  (nome, email, nome_usuario, senha, data_nascimento, idade, telefone)
VALUES
"""
