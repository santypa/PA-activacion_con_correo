-- --------------------------------------------------------
-- Host:                         academia.c1mebdhdxytu.us-east-1.rds.amazonaws.com
-- Versión del servidor:         10.4.21-MariaDB-log - Source distribution
-- SO del servidor:              Linux
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para p4
CREATE DATABASE IF NOT EXISTS `p4` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `p4`;

-- Volcando estructura para tabla p4.imagenes
CREATE TABLE IF NOT EXISTS `imagenes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `img` varchar(500) DEFAULT NULL,
  `id_imagen` int(11) DEFAULT NULL,
  `peso` varchar(50) DEFAULT NULL,
  `extencion` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_imagenes_usuarios` (`id_imagen`) USING BTREE,
  CONSTRAINT `FK_imagenes_usuarios` FOREIGN KEY (`id_imagen`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla p4.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(1000) DEFAULT NULL,
  `activo` varchar(50) DEFAULT NULL,
  `id_imagen` int(11) DEFAULT NULL,
  `toke` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
