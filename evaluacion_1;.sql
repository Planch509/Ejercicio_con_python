CREATE DATABASE evaluacion_1;
CREATE TABLE pasaporte
(
  nuemro_pasaporte INT PRIMARY NOT NULL,
  fecha_emision DATE,
  fecha_vencimiento DATE,
  pais_emision INT,
  foto VARCHAR(30)
)