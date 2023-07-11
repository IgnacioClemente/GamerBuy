-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-07-2023 a las 07:11:00
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gamerbuy`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito`
--

CREATE TABLE `carrito` (
  `id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `precio_total` int(11) DEFAULT NULL,
  `nro_forma_de_pago` int(11) NOT NULL,
  `dni_cliente` int(11) NOT NULL,
  `codigo_producto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carrito`
--

INSERT INTO `carrito` (`id`, `fecha`, `cantidad`, `precio`, `precio_total`, `nro_forma_de_pago`, `dni_cliente`, `codigo_producto`) VALUES
(2423, '2014-04-14', 4, 3252, 3532, 12, 5765487, 6363),
(2424, '2012-04-16', 1, 424524, 424524, 342432432, 535326, 35232),
(2525, '2022-06-12', 4, 325235, 23563, 2, 2536436, 6363),
(2532, '2010-06-14', 4, 8546, 9143, 134, 5765487, 35232);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `dni` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `id_direccion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`dni`, `nombre`, `id_direccion`) VALUES
(535326, 'Esteban', 345252),
(543634, 'Jimena', 52),
(2534263, 'Diego', 45),
(2536436, 'Oscar', 45),
(5765487, 'Marcos', 525);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `direccion`
--

CREATE TABLE `direccion` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `altura` int(11) NOT NULL,
  `localidad` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `direccion`
--

INSERT INTO `direccion` (`id`, `nombre`, `altura`, `localidad`) VALUES
(12, 'Palermo', 543, 'Buenos Aires'),
(45, 'Belgrano', 63, 'Capital'),
(52, 'Chaco', 52, 'Chaco'),
(525, 'Caballito', 532, 'Provincia'),
(4536, 'Pilar', 532, 'Provincia'),
(5235, 'San Justo', 2653, 'Provincia'),
(345252, 'Penyo', 4242, 'Deboto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `forma_de_pago`
--

CREATE TABLE `forma_de_pago` (
  `nro_tarjeta` int(11) NOT NULL,
  `tipo` enum('Efectivo','Debito') NOT NULL,
  `nombre_tarjeta` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `forma_de_pago`
--

INSERT INTO `forma_de_pago` (`nro_tarjeta`, `tipo`, `nombre_tarjeta`) VALUES
(1, 'Efectivo', 'MasterCard'),
(2, 'Debito', 'American Express'),
(12, 'Efectivo', 'MasterCard'),
(123, 'Efectivo', 'Debito'),
(134, 'Debito', 'MasterCard'),
(776, 'Efectivo', 'American Express'),
(342432432, 'Efectivo', 'Visa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `marcas`
--

CREATE TABLE `marcas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `marcas`
--

INSERT INTO `marcas` (`id`, `nombre`) VALUES
(1, 'Nvidia'),
(2, 'Intel'),
(3, 'ASUS'),
(4, 'Genius'),
(5, 'Razer'),
(6, 'Logitech'),
(7, 'SteelSeries'),
(8, 'Gigabyte'),
(9, 'MSI'),
(10, 'HP'),
(532, 'AMD');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `codigo` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `precio_por_unidad` int(11) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `id_proveedor` int(11) NOT NULL,
  `id_marcas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`codigo`, `nombre`, `precio_por_unidad`, `stock`, `imagen`, `id_proveedor`, `id_marcas`) VALUES
(4525, 'Placa', 436743, 2, 'None', 1, 1),
(6363, 'Auriculares', 24245, 2, 'None', 2, 5),
(25235, 'Procesador', 2352, 4, 'None', 5, 3),
(35232, 'Procesador', 424524, 4, NULL, 24242, 532),
(45345, 'Teclado', 23532, 2, 'None', 3, 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE `proveedor` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `id_direccion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`id`, `nombre`, `id_direccion`) VALUES
(1, 'DaleViejo', 45),
(2, 'Honga', 525),
(3, 'Nomepaso', 12),
(4, 'Umita', 52),
(5, 'Planco', 5235),
(24242, 'Expoyo', 345252);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nro_forma_de_pago` (`nro_forma_de_pago`),
  ADD KEY `dni_cliente` (`dni_cliente`),
  ADD KEY `codigo_producto` (`codigo_producto`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`dni`),
  ADD KEY `id_direccion` (`id_direccion`);

--
-- Indices de la tabla `direccion`
--
ALTER TABLE `direccion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `forma_de_pago`
--
ALTER TABLE `forma_de_pago`
  ADD PRIMARY KEY (`nro_tarjeta`);

--
-- Indices de la tabla `marcas`
--
ALTER TABLE `marcas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`codigo`),
  ADD KEY `id_proveedor` (`id_proveedor`),
  ADD KEY `id_marcas` (`id_marcas`);

--
-- Indices de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_direccion` (`id_direccion`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD CONSTRAINT `carrito_ibfk_1` FOREIGN KEY (`nro_forma_de_pago`) REFERENCES `forma_de_pago` (`nro_tarjeta`),
  ADD CONSTRAINT `carrito_ibfk_2` FOREIGN KEY (`dni_cliente`) REFERENCES `cliente` (`dni`),
  ADD CONSTRAINT `carrito_ibfk_3` FOREIGN KEY (`codigo_producto`) REFERENCES `productos` (`codigo`);

--
-- Filtros para la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `cliente_ibfk_1` FOREIGN KEY (`id_direccion`) REFERENCES `direccion` (`id`);

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`id_proveedor`) REFERENCES `proveedor` (`id`),
  ADD CONSTRAINT `productos_ibfk_2` FOREIGN KEY (`id_marcas`) REFERENCES `marcas` (`id`);

--
-- Filtros para la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD CONSTRAINT `proveedor_ibfk_1` FOREIGN KEY (`id_direccion`) REFERENCES `direccion` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
