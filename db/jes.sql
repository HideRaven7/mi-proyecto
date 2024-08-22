-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 22, 2024 at 05:21 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jes`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id_admin` int NOT NULL,
  `nombre_admin` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `a_apellido` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `a_email` varchar(140) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `a_genero` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `a_direccion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `a_telefono` char(14) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `a_img_perfil` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `matricula` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `contraseña` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id_admin`, `nombre_admin`, `a_apellido`, `a_email`, `a_genero`, `a_direccion`, `a_telefono`, `a_img_perfil`, `matricula`, `contraseña`) VALUES
(1, 'Jhon Mike', 'Peña Ramos', 'jhonmip2@gmail.com', 'Masculino', 'Calle 16 de Agosto #01', '809-101-0000', 'https://plus.unsplash.com/premium_photo-1671656349322-41de944d259b?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'a-0223', 'admin2330');

-- --------------------------------------------------------

--
-- Table structure for table `asignaturas`
--

CREATE TABLE `asignaturas` (
  `id_asignatura` int NOT NULL,
  `nom_asignatura` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Dumping data for table `asignaturas`
--

INSERT INTO `asignaturas` (`id_asignatura`, `nom_asignatura`) VALUES
(2401, 'Lengua Española'),
(2402, 'Matematicas'),
(2403, 'Ciencias Sociales'),
(2404, 'Ciencias Naturales'),
(2405, 'Ingles'),
(2406, 'Frances'),
(2407, 'Educacion Fisica'),
(2408, 'Arte '),
(2409, 'Formacion Humana');

-- --------------------------------------------------------

--
-- Table structure for table `asignatura_curso`
--

CREATE TABLE `asignatura_curso` (
  `id` int NOT NULL,
  `id_curso` int NOT NULL,
  `id_asignatura` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------

--
-- Table structure for table `asistencias`
--

CREATE TABLE `asistencias` (
  `id_asistencia` int NOT NULL,
  `id_estudiante` int NOT NULL,
  `id_curso` int NOT NULL,
  `id_asignatura` int NOT NULL,
  `Sect_Oct` char(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `Nov_Dic` char(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `Ene_Feb` char(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `Marz_Abril` char(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `May_Jun` char(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `Total_de_asistencias` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `calificaciones`
--

CREATE TABLE `calificaciones` (
  `id_calificacion` int NOT NULL,
  `id_estudiante` int NOT NULL,
  `id_asignatura` int NOT NULL,
  `C1` int NOT NULL,
  `C2` int NOT NULL,
  `C3` int NOT NULL,
  `C4` int NOT NULL,
  `c_final` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Dumping data for table `calificaciones`
--

INSERT INTO `calificaciones` (`id_calificacion`, `id_estudiante`, `id_asignatura`, `C1`, `C2`, `C3`, `C4`, `c_final`) VALUES
(1, 2, 2403, 100, 100, 100, 100, 100),
(2, 2, 2404, 100, 100, 90, 89, 95),
(3, 2, 2405, 99, 91, 96, 97, 96);

-- --------------------------------------------------------

--
-- Table structure for table `cursos`
--

CREATE TABLE `cursos` (
  `id_curso` int NOT NULL,
  `nombre` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Dumping data for table `cursos`
--

INSERT INTO `cursos` (`id_curso`, `nombre`) VALUES
(1, '1ro A'),
(2, '2do A'),
(3, '3ro A'),
(4, '4to A'),
(5, '5to A'),
(6, '6to A'),
(7, '1ro B'),
(8, '2do B'),
(9, '3ro B'),
(10, '4to B'),
(11, '5to B'),
(12, '6to B');

-- --------------------------------------------------------

--
-- Table structure for table `dias`
--

CREATE TABLE `dias` (
  `id_dias` int NOT NULL,
  `dia` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Dumping data for table `dias`
--

INSERT INTO `dias` (`id_dias`, `dia`) VALUES
(100, 'Lunes'),
(101, 'Martes'),
(102, 'Miercoles'),
(103, 'Jueves'),
(104, 'Viernes');

-- --------------------------------------------------------

--
-- Table structure for table `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id_estudiante` int NOT NULL,
  `id_curso` int NOT NULL,
  `matricula` char(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `nombre` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `apellidos` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `direccion` text CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `genero` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `email` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `telefono` char(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `imagen_perfil` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `contraseña` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Dumping data for table `estudiantes`
--

INSERT INTO `estudiantes` (`id_estudiante`, `id_curso`, `matricula`, `nombre`, `apellidos`, `direccion`, `fecha_nacimiento`, `genero`, `email`, `telefono`, `imagen_perfil`, `contraseña`) VALUES
(2, 1, 'e-9990', 'Albiery', 'Rodriguez', 'calle 16 de agosto #1', '2010-10-19', 'masculino', 'albieryr@gmail.com', '8095889924', 'https://images.unsplash.com/photo-1521119989659-a83eee488004?q=80&w=1923&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'estudiante123');

-- --------------------------------------------------------

--
-- Table structure for table `hora`
--

CREATE TABLE `hora` (
  `id_hora` int NOT NULL,
  `hora` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Dumping data for table `hora`
--

INSERT INTO `hora` (`id_hora`, `hora`) VALUES
(1, '7:30-8:30'),
(2, '8:30-9:30'),
(3, '9:30-10:00'),
(4, '10:00-11:00'),
(5, '11:00-12:00');

-- --------------------------------------------------------

--
-- Table structure for table `horario`
--

CREATE TABLE `horario` (
  `id_horario` int NOT NULL,
  `id_estudiante` int NOT NULL,
  `id_hora` int NOT NULL,
  `id_curso` int NOT NULL,
  `id_asignatura` int NOT NULL,
  `id_dias` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Dumping data for table `horario`
--

INSERT INTO `horario` (`id_horario`, `id_estudiante`, `id_hora`, `id_curso`, `id_asignatura`, `id_dias`) VALUES
(1, 2, 1, 1, 2403, 100);

-- --------------------------------------------------------

--
-- Table structure for table `libros`
--

CREATE TABLE `libros` (
  `id_libro` int NOT NULL,
  `id_asignatura` int NOT NULL,
  `id_curso` int NOT NULL,
  `titulo` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `subir_libro` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `portada` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Dumping data for table `libros`
--

INSERT INTO `libros` (`id_libro`, `id_asignatura`, `id_curso`, `titulo`, `subir_libro`, `portada`) VALUES
(1, 2408, 1, 'Don quijote', '', 'https://static.arteinformado.com/resources/app/docs/profesional/75/185475/obras/308.d._quijote_y_sancho_en_el_camino.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `material_estudio`
--

CREATE TABLE `material_estudio` (
  `id_material` int NOT NULL,
  `id_curso` int NOT NULL,
  `titulo` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `material_subido` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `fondo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `id_asignatura` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Dumping data for table `material_estudio`
--

INSERT INTO `material_estudio` (`id_material`, `id_curso`, `titulo`, `material_subido`, `fondo`, `descripcion`, `id_asignatura`) VALUES
(1, 1, 'Investigacion', '', '', 'Ciencia de la Naturales es una asignatura que se enfoca en comprender los procesos y fenómenos que ocurren en nuestro entorno natural. Los estudiantes aprenden sobre la estructura y funcionamiento de los seres vivos, las sustancias químicas que componen el mundo, las fuerzas físicas y los procesos geológicos que modelan nuestro planeta.', 2404);

-- --------------------------------------------------------

--
-- Table structure for table `profesores`
--

CREATE TABLE `profesores` (
  `id_profesor` int NOT NULL,
  `id_asignatura` int NOT NULL,
  `matricula` char(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `nombre` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `apellido` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `direccion` text CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `cedula` char(14) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `genero` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `email` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `telefono` char(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `contraseña` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `imagen_perfil` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Dumping data for table `profesores`
--

INSERT INTO `profesores` (`id_profesor`, `id_asignatura`, `matricula`, `nombre`, `apellido`, `direccion`, `cedula`, `genero`, `email`, `telefono`, `contraseña`, `imagen_perfil`) VALUES
(10011, 2401, 'p001', 'Juan', ' Gonzalez Perez', 'calle la española #233', '001-1234567-1', 'Masculino', 'juangonzales@gmail.com', '809-458-1265', 'juan123', 'https://th.bing.com/th/id/R.88eb21cb4e3694341e75bbac7a265ffb?rik=GoCReAF3TNW6yQ&riu=http%3a%2f%2fwww.misimagenesde.com%2fwp-content%2fuploads%2f2011%2f01%2fimagenes-de-personas.jpg&ehk=n6NLhejqcpA8k7ZO9wqa7PSmXl2m9Pg7Q46wXW50UaU%3d&risl=&pid=ImgRaw&r=0'),
(10012, 2402, 'p002', 'Maria', 'Lopez Garcia', '', '002-2345678-2', 'Femenino', 'mARIlopez@gmail.com', '809-234-5678', 'maria123', ''),
(10013, 2403, 'p003', 'Carlos', 'Dominguez Fernandez', '', '003-3456789-3', 'Masculino', 'carlos.dominguezfernandez@gmail.com', '809-345-6789', 'carlos123', ''),
(10014, 2404, 'p004', 'Ana', 'Sanchez Ruiz', '', '004-4567890-4', 'Femenino', 'anaruiz@gmail.com', '809-456-7890', 'ana123', ''),
(10015, 2405, 'p005', 'Luis Mario ', 'Martinez Gomez', '', '005-5678901-5', 'Masculino', 'luismartinez@gmail.com', '809-567-8901', 'luismario123', ''),
(10016, 2406, 'p006', 'Macarena', 'Ramirez Torres', '', ' 006-6789012-6', 'Femenino', 'ramireztorresMac@gmail.com', '809-678-9012', 'macarena123', ''),
(10017, 2407, 'p007', 'Javier', 'Dias Morales', '', ' 007-7890123-7', 'Masculino', 'javiDiazmorales@gmail.com', '809-789-0123', 'javier123', ''),
(10018, 2408, 'p008', 'Maria Elena', 'Hernandez Castro', '', '008-8901234-8', 'Femenino', 'elenahernandezcastro@example.com', '809-890-1234', 'mariaElena123', ''),
(10019, 2409, 'p009', 'Isabel', ' Navarro Vá\\azquez', '', '010-0123456-0', 'Femenino', 'isabelvazquez@example.com', '809-456-6461', 'isabel123', '');

-- --------------------------------------------------------

--
-- Table structure for table `profesor_asignado`
--

CREATE TABLE `profesor_asignado` (
  `id_profesor-asignado` int NOT NULL,
  `id_profesor` int NOT NULL,
  `id_curso` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Dumping data for table `profesor_asignado`
--

INSERT INTO `profesor_asignado` (`id_profesor-asignado`, `id_profesor`, `id_curso`) VALUES
(1, 10011, 1),
(2, 10014, 1);

-- --------------------------------------------------------

--
-- Table structure for table `reporte_profesor`
--

CREATE TABLE `reporte_profesor` (
  `id_report` int NOT NULL,
  `id_profesor-asignado` int NOT NULL,
  `asistencia` varchar(600) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `calificaciones` varchar(600) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tareas_estudiante`
--

CREATE TABLE `tareas_estudiante` (
  `id_tarea` int NOT NULL,
  `id_estudiante` int NOT NULL,
  `id_curso` int NOT NULL,
  `tarea` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------

--
-- Table structure for table `videos`
--

CREATE TABLE `videos` (
  `id` int NOT NULL,
  `titulo` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL,
  `id_curso` int NOT NULL,
  `id_asignatura` int NOT NULL,
  `video` text CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish2_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Dumping data for table `videos`
--

INSERT INTO `videos` (`id`, `titulo`, `id_curso`, `id_asignatura`, `video`) VALUES
(2, 'Don quijote', 1, 2408, '<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/ir6A-Ns5Em8?si=y-I8_Uain9fbW5vZ\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe>'),
(3, 'La naturaleza', 1, 2404, '<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/j6LunB9d2Bo?si=JaIb5RaXyWx1I_-p\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" referrerpolicy=\"strict-origin-when-cross-origin\" allowfullscreen></iframe>');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indexes for table `asignaturas`
--
ALTER TABLE `asignaturas`
  ADD PRIMARY KEY (`id_asignatura`);

--
-- Indexes for table `asignatura_curso`
--
ALTER TABLE `asignatura_curso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_curso` (`id_curso`),
  ADD KEY `id_asignatura` (`id_asignatura`);

--
-- Indexes for table `asistencias`
--
ALTER TABLE `asistencias`
  ADD PRIMARY KEY (`id_asistencia`),
  ADD KEY `id_estudiante` (`id_estudiante`),
  ADD KEY `id_curso` (`id_curso`),
  ADD KEY `id_asignatura` (`id_asignatura`);

--
-- Indexes for table `calificaciones`
--
ALTER TABLE `calificaciones`
  ADD PRIMARY KEY (`id_calificacion`),
  ADD KEY `id_estudiante` (`id_estudiante`),
  ADD KEY `id_asignatura` (`id_asignatura`);

--
-- Indexes for table `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id_curso`);

--
-- Indexes for table `dias`
--
ALTER TABLE `dias`
  ADD PRIMARY KEY (`id_dias`);

--
-- Indexes for table `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id_estudiante`),
  ADD KEY `id_curso_seccion` (`id_curso`);

--
-- Indexes for table `hora`
--
ALTER TABLE `hora`
  ADD PRIMARY KEY (`id_hora`);

--
-- Indexes for table `horario`
--
ALTER TABLE `horario`
  ADD PRIMARY KEY (`id_horario`),
  ADD KEY `id_horas` (`id_hora`),
  ADD KEY `id_cursos` (`id_curso`),
  ADD KEY `id_asignaturas` (`id_asignatura`),
  ADD KEY `id_dias` (`id_dias`),
  ADD KEY `id_curso_seccion` (`id_curso`),
  ADD KEY `id_estudiante` (`id_estudiante`);

--
-- Indexes for table `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`id_libro`),
  ADD KEY `id_asignatura` (`id_asignatura`),
  ADD KEY `id_curso` (`id_curso`);

--
-- Indexes for table `material_estudio`
--
ALTER TABLE `material_estudio`
  ADD PRIMARY KEY (`id_material`),
  ADD KEY `id_curso` (`id_curso`),
  ADD KEY `id_asignatura` (`id_asignatura`);

--
-- Indexes for table `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`id_profesor`),
  ADD KEY `id_asignatura` (`id_asignatura`);

--
-- Indexes for table `profesor_asignado`
--
ALTER TABLE `profesor_asignado`
  ADD PRIMARY KEY (`id_profesor-asignado`),
  ADD KEY `id_profesor` (`id_profesor`),
  ADD KEY `id_curso_seccion` (`id_curso`);

--
-- Indexes for table `reporte_profesor`
--
ALTER TABLE `reporte_profesor`
  ADD PRIMARY KEY (`id_report`),
  ADD KEY `id_profesor-asignado` (`id_profesor-asignado`);

--
-- Indexes for table `tareas_estudiante`
--
ALTER TABLE `tareas_estudiante`
  ADD PRIMARY KEY (`id_tarea`),
  ADD KEY `id_estudiante` (`id_estudiante`),
  ADD KEY `id_curso` (`id_curso`);

--
-- Indexes for table `videos`
--
ALTER TABLE `videos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_curso` (`id_curso`),
  ADD KEY `id_asignatura` (`id_asignatura`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id_admin` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `asignaturas`
--
ALTER TABLE `asignaturas`
  MODIFY `id_asignatura` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2410;

--
-- AUTO_INCREMENT for table `asignatura_curso`
--
ALTER TABLE `asignatura_curso`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `asistencias`
--
ALTER TABLE `asistencias`
  MODIFY `id_asistencia` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `calificaciones`
--
ALTER TABLE `calificaciones`
  MODIFY `id_calificacion` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `cursos`
--
ALTER TABLE `cursos`
  MODIFY `id_curso` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `dias`
--
ALTER TABLE `dias`
  MODIFY `id_dias` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

--
-- AUTO_INCREMENT for table `estudiantes`
--
ALTER TABLE `estudiantes`
  MODIFY `id_estudiante` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hora`
--
ALTER TABLE `hora`
  MODIFY `id_hora` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `horario`
--
ALTER TABLE `horario`
  MODIFY `id_horario` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `libros`
--
ALTER TABLE `libros`
  MODIFY `id_libro` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `material_estudio`
--
ALTER TABLE `material_estudio`
  MODIFY `id_material` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `profesores`
--
ALTER TABLE `profesores`
  MODIFY `id_profesor` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10020;

--
-- AUTO_INCREMENT for table `profesor_asignado`
--
ALTER TABLE `profesor_asignado`
  MODIFY `id_profesor-asignado` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tareas_estudiante`
--
ALTER TABLE `tareas_estudiante`
  MODIFY `id_tarea` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `videos`
--
ALTER TABLE `videos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `asignatura_curso`
--
ALTER TABLE `asignatura_curso`
  ADD CONSTRAINT `asignatura_curso_ibfk_1` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`),
  ADD CONSTRAINT `asignatura_curso_ibfk_2` FOREIGN KEY (`id_asignatura`) REFERENCES `asignaturas` (`id_asignatura`);

--
-- Constraints for table `asistencias`
--
ALTER TABLE `asistencias`
  ADD CONSTRAINT `asistencias_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`),
  ADD CONSTRAINT `asistencias_ibfk_2` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`),
  ADD CONSTRAINT `asistencias_ibfk_3` FOREIGN KEY (`id_asignatura`) REFERENCES `asignaturas` (`id_asignatura`);

--
-- Constraints for table `calificaciones`
--
ALTER TABLE `calificaciones`
  ADD CONSTRAINT `calificaciones_ibfk_1` FOREIGN KEY (`id_asignatura`) REFERENCES `asignaturas` (`id_asignatura`),
  ADD CONSTRAINT `calificaciones_ibfk_2` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`);

--
-- Constraints for table `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD CONSTRAINT `estudiantes_ibfk_1` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`);

--
-- Constraints for table `horario`
--
ALTER TABLE `horario`
  ADD CONSTRAINT `horario_ibfk_1` FOREIGN KEY (`id_hora`) REFERENCES `hora` (`id_hora`),
  ADD CONSTRAINT `horario_ibfk_2` FOREIGN KEY (`id_dias`) REFERENCES `dias` (`id_dias`),
  ADD CONSTRAINT `horario_ibfk_4` FOREIGN KEY (`id_asignatura`) REFERENCES `asignaturas` (`id_asignatura`),
  ADD CONSTRAINT `horario_ibfk_6` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`),
  ADD CONSTRAINT `horario_ibfk_7` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`);

--
-- Constraints for table `libros`
--
ALTER TABLE `libros`
  ADD CONSTRAINT `libros_ibfk_1` FOREIGN KEY (`id_asignatura`) REFERENCES `asignaturas` (`id_asignatura`),
  ADD CONSTRAINT `libros_ibfk_2` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`);

--
-- Constraints for table `material_estudio`
--
ALTER TABLE `material_estudio`
  ADD CONSTRAINT `material_estudio_ibfk_1` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`),
  ADD CONSTRAINT `material_estudio_ibfk_2` FOREIGN KEY (`id_asignatura`) REFERENCES `asignaturas` (`id_asignatura`);

--
-- Constraints for table `profesores`
--
ALTER TABLE `profesores`
  ADD CONSTRAINT `profesores_ibfk_1` FOREIGN KEY (`id_asignatura`) REFERENCES `asignaturas` (`id_asignatura`);

--
-- Constraints for table `profesor_asignado`
--
ALTER TABLE `profesor_asignado`
  ADD CONSTRAINT `profesor_asignado_ibfk_2` FOREIGN KEY (`id_profesor`) REFERENCES `profesores` (`id_profesor`),
  ADD CONSTRAINT `profesor_asignado_ibfk_3` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`);

--
-- Constraints for table `reporte_profesor`
--
ALTER TABLE `reporte_profesor`
  ADD CONSTRAINT `reporte_profesor_ibfk_1` FOREIGN KEY (`id_profesor-asignado`) REFERENCES `profesor_asignado` (`id_profesor-asignado`);

--
-- Constraints for table `tareas_estudiante`
--
ALTER TABLE `tareas_estudiante`
  ADD CONSTRAINT `tareas_estudiante_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiantes` (`id_estudiante`),
  ADD CONSTRAINT `tareas_estudiante_ibfk_2` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`);

--
-- Constraints for table `videos`
--
ALTER TABLE `videos`
  ADD CONSTRAINT `videos_ibfk_1` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`),
  ADD CONSTRAINT `videos_ibfk_2` FOREIGN KEY (`id_asignatura`) REFERENCES `asignaturas` (`id_asignatura`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
