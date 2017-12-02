-- phpMyAdmin SQL Dump
-- version 4.4.15.9
-- https://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-11-2017 a las 20:51:42
-- Versión del servidor: 5.6.37
-- Versión de PHP: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `almacenamiento-votos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `votos`
--

DROP TABLE IF EXISTS `votos`;
CREATE TABLE `votos` (
  `voto_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `votacion_id` int(11) NOT NULL,
  `pregunta_id` int(11) NOT NULL,
  `respuesta_id` int(11) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `votos`
--

INSERT INTO `votos` (`voto_id`, `usuario_id`, `votacion_id`, `pregunta_id`, `respuesta_id`) VALUES
(13, 1, 1, 1, 1),
(14, 1, 1, 2, 2),
(15, 2, 1, 1, 2),
(16, 2, 1, 2, 2),
(17, 3, 1, 1, 2),
(18, 3, 1, 2, 1),
(19, 4, 1, 1, NULL),
(20, 5, 1, 2, NULL),
(23, 13, 2, 1, 1),
(30, 13, 2, 2, 1),
(31, 14, 2, 2, 1),
(32, 15, 2, 2, 1);

--
-- Índices para tablas volcadas
--

--
-- AUTO_INCREMENT de las tablas volcadas
--

ALTER TABLE `votos` CHANGE `voto_id` `voto_id` int(11) AUTO_INCREMENT;

--
-- Indices de la tabla `votos`
--
ALTER TABLE `votos`
  ADD PRIMARY KEY (`voto_id`),
  ADD UNIQUE KEY `usuario_id, votacion_id, pregunta_id` (`usuario_id`,`votacion_id`,`pregunta_id`) USING BTREE;

--
-- AUTO_INCREMENT de la tabla `votos`
--
ALTER TABLE `votos`
  MODIFY `voto_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=33;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
