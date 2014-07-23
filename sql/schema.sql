 CREATE TABLE dbrecords (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  dbtran_id INT NOT NULL,
  server_name varchar(32) COLLATE utf8_turkish_ci NOT NULL,
  dbname varchar(32) COLLATE utf8_turkish_ci DEFAULT NULL,
  table_name varchar(100) COLLATE utf8_turkish_ci DEFAULT NULL,
  table_type varchar(100) COLLATE utf8_turkish_ci DEFAULT NULL,
  engine varchar(100) COLLATE utf8_turkish_ci DEFAULT NULL,
  rowcount bigint(20) DEFAULT NULL,
  rowsize bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;
CREATE TABLE dbtransaction (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  record_time TIMESTAMP
 );

