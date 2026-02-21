-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 21, 2026 at 04:34 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fitwise`
--

-- --------------------------------------------------------

--
-- Table structure for table `activity_logs`
--

CREATE TABLE `activity_logs` (
  `activity_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `steps` int(11) DEFAULT NULL,
  `water` int(11) DEFAULT NULL,
  `sleep` float DEFAULT NULL,
  `log_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `activity_logs`
--

INSERT INTO `activity_logs` (`activity_id`, `user_id`, `steps`, `water`, `sleep`, `log_date`) VALUES
(4, 9, 7000, 7, 6, '2026-02-18'),
(5, 9, 10000, 10, 10, '2026-02-20'),
(6, 9, 10000, 12, 10, '2026-02-20'),
(7, 9, 5000, 10, 5, '2026-02-21');

-- --------------------------------------------------------

--
-- Table structure for table `foods`
--

CREATE TABLE `foods` (
  `food_id` int(11) NOT NULL,
  `food_name` varchar(100) DEFAULT NULL,
  `calories` int(11) DEFAULT NULL,
  `protein` float DEFAULT NULL,
  `carbs` float DEFAULT NULL,
  `fat` float DEFAULT NULL,
  `fiber` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `foods`
--

INSERT INTO `foods` (`food_id`, `food_name`, `calories`, `protein`, `carbs`, `fat`, `fiber`) VALUES
(1, 'rice cooked', 1, 0.027, 0.28, 0.003, 0.004),
(2, 'chapati', 1, 0.031, 0.2, 0.037, 0.025),
(3, 'dal cooked', 1, 0.09, 0.2, 0.004, 0.08),
(4, 'paneer', 3, 0.183, 0.012, 0.208, 0),
(5, 'milk', 1, 0.032, 0.05, 0.033, 0),
(6, 'curd', 1, 0.11, 0.034, 0.043, 0),
(7, 'oats', 4, 0.169, 0.663, 0.069, 0.106),
(8, 'banana', 1, 0.011, 0.23, 0.003, 0.026),
(9, 'apple', 1, 0.003, 0.14, 0.002, 0.024),
(10, 'peanut butter', 6, 0.25, 0.2, 0.5, 0.06),
(11, 'boiled egg', 2, 0.13, 0.011, 0.11, 0),
(12, 'brown rice', 1, 0.026, 0.23, 0.009, 0.018),
(13, 'soy chunks', 3, 0.52, 0.33, 0.005, 0.13),
(14, 'almonds', 6, 0.21, 0.22, 0.5, 0.125),
(15, 'broccoli', 1, 0.037, 0.11, 0.006, 0.038),
(16, 'idli', 1, 0.02, 0.12, 0.004, 0.005),
(17, 'dosa plain', 2, 0.045, 0.28, 0.037, 0.01),
(18, 'upma', 1, 0.035, 0.22, 0.045, 0.025),
(19, 'poha', 2, 0.03, 0.34, 0.03, 0.015),
(20, 'vegetable pulao', 2, 0.04, 0.28, 0.04, 0.025),
(21, 'khichdi', 2, 0.05, 0.27, 0.02, 0.035),
(22, 'rajma cooked', 1, 0.087, 0.228, 0.005, 0.064),
(23, 'chole cooked', 2, 0.089, 0.274, 0.026, 0.076),
(24, 'tofu', 1, 0.08, 0.019, 0.048, 0.003),
(25, 'sweet potato boiled', 1, 0.016, 0.2, 0.001, 0.03),
(26, 'potato boiled', 1, 0.019, 0.201, 0.001, 0.018),
(27, 'carrot', 0, 0.009, 0.1, 0.002, 0.028),
(28, 'spinach', 0, 0.029, 0.036, 0.004, 0.022),
(29, 'cabbage', 0, 0.013, 0.06, 0.001, 0.025),
(30, 'tomato', 0, 0.009, 0.039, 0.002, 0.012),
(31, 'cucumber', 0, 0.007, 0.038, 0.001, 0.005),
(32, 'orange', 0, 0.009, 0.12, 0.001, 0.024),
(33, 'mango', 1, 0.008, 0.15, 0.004, 0.016),
(34, 'papaya', 0, 0.005, 0.11, 0.003, 0.017),
(35, 'guava', 1, 0.026, 0.14, 0.01, 0.054),
(36, 'roasted peanuts', 6, 0.26, 0.16, 0.49, 0.085),
(37, 'cashew nuts', 6, 0.18, 0.3, 0.44, 0.033),
(38, 'walnuts', 7, 0.15, 0.14, 0.65, 0.067),
(39, 'flax seeds', 5, 0.18, 0.29, 0.42, 0.27),
(40, 'chia seeds', 5, 0.17, 0.42, 0.31, 0.34),
(41, 'buttermilk', 0, 0.033, 0.048, 0.01, 0),
(42, 'lassi sweet', 1, 0.035, 0.18, 0.03, 0),
(43, 'paneer bhurji', 3, 0.18, 0.05, 0.21, 0.005),
(44, 'vegetable salad', 1, 0.02, 0.1, 0.005, 0.03),
(45, 'moong sprouts', 0, 0.03, 0.06, 0.002, 0.018),
(46, 'multigrain bread', 2, 0.13, 0.41, 0.042, 0.07),
(47, 'white bread', 3, 0.09, 0.49, 0.032, 0.027),
(48, 'peanut chikki', 5, 0.15, 0.45, 0.32, 0.045),
(49, 'besan chilla', 2, 0.09, 0.18, 0.08, 0.03),
(50, 'thepla', 2, 0.055, 0.3, 0.075, 0.04),
(51, 'handvo', 2, 0.07, 0.25, 0.07, 0.035),
(52, 'dhokla', 2, 0.06, 0.28, 0.03, 0.02),
(53, 'khaman', 2, 0.07, 0.32, 0.035, 0.022),
(54, 'sev khamani', 2, 0.08, 0.3, 0.07, 0.03),
(55, 'vegetable sandwich', 3, 0.08, 0.35, 0.09, 0.035),
(56, 'veg burger', 3, 0.09, 0.38, 0.12, 0.03),
(57, 'veg pizza slice', 3, 0.12, 0.33, 0.11, 0.025),
(58, 'pasta boiled', 1, 0.05, 0.25, 0.011, 0.013),
(59, 'macaroni cooked', 2, 0.06, 0.31, 0.012, 0.015),
(60, 'noodles cooked', 1, 0.045, 0.25, 0.021, 0.012),
(61, 'vegetable soup', 1, 0.025, 0.1, 0.01, 0.02),
(62, 'tomato soup', 0, 0.015, 0.08, 0.005, 0.015),
(63, 'corn soup', 1, 0.03, 0.16, 0.01, 0.02),
(64, 'popcorn plain', 4, 0.11, 0.74, 0.043, 0.15),
(65, 'dark chocolate', 5, 0.049, 0.61, 0.31, 0.07),
(66, 'milk chocolate', 5, 0.076, 0.59, 0.3, 0.03),
(67, 'ice cream vanilla', 2, 0.035, 0.24, 0.11, 0),
(68, 'kulfi', 3, 0.06, 0.28, 0.13, 0),
(69, 'jalebi', 5, 0.05, 0.65, 0.19, 0.01),
(70, 'gulab jamun', 3, 0.06, 0.45, 0.12, 0.005),
(71, 'rasgulla', 2, 0.04, 0.4, 0.02, 0),
(72, 'kheer', 2, 0.04, 0.22, 0.05, 0.002),
(73, 'halwa sooji', 2, 0.045, 0.35, 0.09, 0.012),
(74, 'halwa carrot', 2, 0.035, 0.32, 0.08, 0.02),
(75, 'energy bar', 4, 0.1, 0.45, 0.12, 0.05);

-- --------------------------------------------------------

--
-- Table structure for table `food_logs`
--

CREATE TABLE `food_logs` (
  `log_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `food_id` int(11) DEFAULT NULL,
  `quantity` float DEFAULT NULL,
  `log_date` date DEFAULT NULL,
  `meal_type` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `food_logs`
--

INSERT INTO `food_logs` (`log_id`, `user_id`, `food_id`, `quantity`, `log_date`, `meal_type`) VALUES
(17, 9, 16, 0.5, '2026-02-20', 'Breakfast'),
(18, 9, 8, 0.5, '2026-02-21', 'Breakfast'),
(19, 9, 4, 120, '2026-02-21', 'Breakfast'),
(20, 9, 17, 0.5, '2026-02-21', 'Breakfast'),
(21, 9, 22, 120, '2026-02-21', 'Lunch');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `height` float DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `diet_type` varchar(20) DEFAULT NULL,
  `goal` varchar(20) DEFAULT NULL,
  `bmi` float DEFAULT NULL,
  `daily_calorie_goal` int(11) DEFAULT NULL,
  `daily_steps_goal` int(11) DEFAULT NULL,
  `daily_water_goal` int(11) DEFAULT NULL,
  `daily_sleep_goal` int(11) DEFAULT NULL,
  `target_weight` float DEFAULT NULL,
  `goal_months` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `daily_protein_goal` float DEFAULT NULL,
  `daily_carbs_goal` float DEFAULT NULL,
  `daily_fat_goal` float DEFAULT NULL,
  `daily_fiber_goal` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `phone`, `city`, `age`, `height`, `weight`, `diet_type`, `goal`, `bmi`, `daily_calorie_goal`, `daily_steps_goal`, `daily_water_goal`, `daily_sleep_goal`, `target_weight`, `goal_months`, `created_at`, `daily_protein_goal`, `daily_carbs_goal`, `daily_fat_goal`, `daily_fiber_goal`) VALUES
(9, 'Vivek Soni', 'sonivivek2007@gmail.com', 'Vivek@17', '8511491278', 'New Ranip', 10, 177, 85, 'Veg', 'Weight Loss', NULL, 1266, 10000, 12, 8, 80, 1, '2026-02-20 15:50:01', 95, 126.6, 42.2, 17.7),
(10, 'Vraj Patel', 'vrajppatel25@gmail.com', 'Vr@j25606', '9825425606', 'Ahmedabad City', 19, 175, 78.5, 'Veg', 'Weight Loss', NULL, 1264, 8000, 12, 8, 70, 2, '2026-02-21 04:09:51', 94.8, 126.4, 42.1, 17.7),
(11, 'Shah Vishwa', 'vrshah0603@gmail.com', 'Vihsu06@', '9638699741', 'Ahmedabad', 19, 164, 68, 'Veg', 'Weight Loss', NULL, -13, 1000, 1, 1, 60, 1, '2026-02-21 04:22:57', -1, -1.3, -0.4, -0.2),
(12, 'Shah Bhavya', 'tempvraj0625@gmail.com', 'VrajPatel@13', '9825099741', 'Ahmedabad', 20, 155, 80, 'Veg', 'Weight Loss', NULL, -2733, 1000, 1, 1, 60, 1, '2026-02-21 04:24:39', -205, -273.3, -91.1, -38.3);

-- --------------------------------------------------------

--
-- Table structure for table `weight_logs`
--

CREATE TABLE `weight_logs` (
  `weight_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `log_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `weight_logs`
--

INSERT INTO `weight_logs` (`weight_id`, `user_id`, `weight`, `log_date`) VALUES
(1, 9, 87, '2026-02-08'),
(2, 9, 88, '2026-02-07'),
(3, 9, 85, '2026-02-20'),
(4, 9, 86, '2026-02-21');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `activity_logs`
--
ALTER TABLE `activity_logs`
  ADD PRIMARY KEY (`activity_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `foods`
--
ALTER TABLE `foods`
  ADD PRIMARY KEY (`food_id`);

--
-- Indexes for table `food_logs`
--
ALTER TABLE `food_logs`
  ADD PRIMARY KEY (`log_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `food_id` (`food_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `weight_logs`
--
ALTER TABLE `weight_logs`
  ADD PRIMARY KEY (`weight_id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activity_logs`
--
ALTER TABLE `activity_logs`
  MODIFY `activity_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `foods`
--
ALTER TABLE `foods`
  MODIFY `food_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- AUTO_INCREMENT for table `food_logs`
--
ALTER TABLE `food_logs`
  MODIFY `log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `weight_logs`
--
ALTER TABLE `weight_logs`
  MODIFY `weight_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `activity_logs`
--
ALTER TABLE `activity_logs`
  ADD CONSTRAINT `activity_logs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `food_logs`
--
ALTER TABLE `food_logs`
  ADD CONSTRAINT `food_logs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `food_logs_ibfk_2` FOREIGN KEY (`food_id`) REFERENCES `foods` (`food_id`);

--
-- Constraints for table `weight_logs`
--
ALTER TABLE `weight_logs`
  ADD CONSTRAINT `weight_logs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
