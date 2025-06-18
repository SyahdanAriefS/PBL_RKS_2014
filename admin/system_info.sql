-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 18 Jun 2025 pada 12.46
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `browsewatch`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `system_info`
--

CREATE TABLE `system_info` (
  `id` int(11) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `hostname` varchar(100) DEFAULT NULL,
  `os` varchar(100) DEFAULT NULL,
  `local_ip` varchar(50) DEFAULT NULL,
  `public_ip` varchar(50) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `region` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `bytes_sent` bigint(20) DEFAULT NULL,
  `bytes_recv` bigint(20) DEFAULT NULL,
  `packets_sent` bigint(20) DEFAULT NULL,
  `packets_recv` bigint(20) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `chrome_history` longtext DEFAULT NULL,
  `firefox_history` longtext DEFAULT NULL,
  `edge_history` longtext DEFAULT NULL,
  `url` longtext DEFAULT NULL,
  `usernames` longtext DEFAULT NULL,
  `passwords` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `system_info`
--

INSERT INTO `system_info` (`id`, `username`, `hostname`, `os`, `local_ip`, `public_ip`, `city`, `region`, `country`, `latitude`, `longitude`, `bytes_sent`, `bytes_recv`, `packets_sent`, `packets_recv`, `created_at`, `chrome_history`, `firefox_history`, `edge_history`, `url`, `usernames`, `passwords`) VALUES
(1, 'user', 'Lenovo', 'windows 11', '192.168.1.1', '10.17.6.43', 'batam', 'kepulauan riau', 'indonesia', '109859303', '939395939', 22206, 29588, 23049, 28730, '2025-06-18 17:46:24', 'https://netacad.com/\r\nhttp://google.com\r\nhttps://www.google.com/maps', 'https://netacad.com/\r\nhttp://google.com\r\nhttps://www.google.com/maps', 'https://netacad.com/\r\nhttp://google.com\r\nhttps://www.google.com/maps', 'https://netacad.com/\r\nhttp://google.com\r\nhttps://www.google.com/maps', 'ikangorengsambaladi\r\nadisukaikan\r\nikankehebatan', '');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `system_info`
--
ALTER TABLE `system_info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `system_info`
--
ALTER TABLE `system_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
