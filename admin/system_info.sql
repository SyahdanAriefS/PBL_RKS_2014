-- phpMyAdmin SQL Dump
-- version 5.0.4deb2+deb11u2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 08, 2025 at 11:59 AM
-- Server version: 10.5.28-MariaDB-0+deb11u2
-- PHP Version: 7.4.33

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
-- Table structure for table `system_info`
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
-- Dumping data for table `system_info`
--

INSERT INTO `system_info` (`id`, `username`, `hostname`, `os`, `local_ip`, `public_ip`, `city`, `region`, `country`, `latitude`, `longitude`, `bytes_sent`, `bytes_recv`, `packets_sent`, `packets_recv`, `created_at`, `chrome_history`, `firefox_history`, `edge_history`, `url`, `usernames`, `passwords`) VALUES
(1, 'user', 'DESKTOP-QC6V89G', 'Windows 10', '192.168.10.10', '180.252.59.96', 'Batam', 'Riau', 'ID', '1.1494', '104.0249', 22723969, 2455656895, 270837, 1669073, '2025-07-01 21:13:58', '[2394-05-26 18:12:54] Login - Akun Google - https://accounts.google.com/AddSession?Email=arifb8237%40gmail.com&continue=https%3A%2F%2Fwww.google.com%2F\n[2394-05-26 18:12:54] Login - Akun Google - https://accounts.google.com/v3/signin/identifier?Email=arifb8237%40gmail.com&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S1377869702%3A1748257989585150\n[2394-05-26 18:11:52] Keamanan - https://myaccount.google.com/security?origin=3\n[2394-05-26 18:11:50] Aktivitas keamanan terbaru - https://myaccount.google.com/notifications/eid/6827717354195028356?origin=3&continue=https%3A%2F%2Fmyaccount.google.com%2Fsecurity\n[2394-05-26 18:11:44] Keamanan - https://myaccount.google.com/security\n[2394-05-26 18:11:36] Data & privasi - https://myaccount.google.com/data-and-privacy\n[2394-05-26 18:11:35] Akun Google - https://myaccount.google.com/data-and-privacy?utm_source=chrome-profile-chooser\n[2394-05-26 18:11:31] Akun Google - https://accounts.google.com/AccountChooser?Email=arifb8237%40gmail.com&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dchrome-profile-chooser\n[2394-05-26 18:11:31] Akun Google - https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dchrome-profile-chooser&sacu=1&passive=1209600&authuser=0\n[2394-05-26 18:11:31] Akun Google - https://myaccount.google.com/accounts/SetOSID?authuser=0&continue=https://myaccount.google.com/?utm_source%3Dchrome-profile-chooser%26pli%3D1&osidt=ALWU2csUVbAPmmlqfgEzbOD2YB9sa3qwllSomqPMZOadA3PUoiqOFezLKZp8iG8zit0rqOWVx2ajUW4evU9zItYvp9W3dRCuOrC_6eWXQK5qdI7-K8rbXlIUY6XIwWfaR4Cb-oetCRf4IB-kKB3xEwxqt68LOOFlEd5X3vNoO-8PZxgUl7qB-ke506_eY1hq5L5mA6mEihlbLfRbljKRIgtQPTJxHOf02wxU-33YhJSwI4bPCLvyALKNerc8z35xFDQrtOu8jOmWxKpOjtBX64usAQ1aZzNOi8lEevCg8pI7FJTLwUIvO4Jh_2fIbppLbWDRBOFfoANLWZAhHeTeRZ2qp2KmhY2fQ4nBVvy9YGDoevnqL81tn63oRfO865FA_wRccA5mb_A7KM2PyFbu5hWKBpvAeib83JQgveyP55l7m5hHPkNf0xykvtd0uYCKLzgYudltDGc_S6KdxAsIWFF0hBm1Sv8VAYRbrvmmtGlhWCiKHaupTdo&ifkv=ASKV5MhVhC6jBPjaYxwXp3OkRAp2oqfXrKm4TaXmN4vOvlRf2lL3g9TlagmdzwzWYdtUkGikCFPqHg\n[2394-05-26 18:11:31] Akun Google - https://myaccount.google.com/?utm_source=chrome-profile-chooser&pli=1\n[2394-05-26 18:09:11] localhost / 127.0.0.1 / browsewatch / system_info | phpMyAdmin 5.2.1 - http://localhost/phpmyadmin/index.php?route=/sql&pos=0&db=browsewatch&table=system_info\n[2394-05-26 17:57:00] Login - Akun Google - https://accounts.google.com/v3/signin/challenge/pwd?TL=AArrULS21j_WwVCEJIFjunXGkWTF8z0_fTr7fp-s3sfUv7Z9X0yLyiKIBKRfjPzn&checkConnection=youtube%3A706&checkedDomains=youtube&cid=1&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Fchrome%2Fsync%2Ffinish%3Fest%3DABhSNjlKB-DRS4vegtXAs4z2qdIPmU0ZGOuA-WOsnqB3WYZJTD3ICBPQYOfCwjgOwRQWaOYfBnjp_IQYAEaBScs%26continue%3Dhttps%3A%2F%2Fwww.google.com%2F&dsh=S924094285%3A1748257021560666&flowName=GlifDesktopChromeSync&pstMsg=1\n[2394-05-26 17:56:46] Login - Akun Google - https://accounts.google.com/signin/chrome/sync?ssp=1&continue=https%3A%2F%2Fwww.google.com%2F\n[2394-05-26 17:56:46] Login - Akun Google - https://accounts.google.com/v3/signin/identifier?continue=https://accounts.google.com/signin/chrome/sync/finish?est%3DABhSNjlKB-DRS4vegtXAs4z2qdIPmU0ZGOuA-WOsnqB3WYZJTD3ICBPQYOfCwjgOwRQWaOYfBnjp_IQYAEaBScs%26continue%3Dhttps://www.google.com/&dsh=S924094285:1748257021560666&ffgf=1&ssp=1&flowName=GlifDesktopChromeSync\n[2394-05-26 17:53:40] localhost / 127.0.0.1 / browsewatch | phpMyAdmin 5.2.1 - http://localhost/phpmyadmin/index.php?route=/import\n[2394-05-26 17:53:29] localhost / 127.0.0.1 / browsewatch | phpMyAdmin 5.2.1 - http://localhost/phpmyadmin/index.php?route=/database/import&db=browsewatch\n[2394-05-26 17:53:26] localhost / 127.0.0.1 / browsewatch | phpMyAdmin 5.2.1 - http://localhost/phpmyadmin/index.php?route=/server/databases\n[2394-05-26 17:52:41] localhost / 127.0.0.1 | phpMyAdmin 5.2.1 - http://localhost/phpmyadmin/index.php?route=/server/import\n[2394-05-26 17:49:21] localhost / 127.0.0.1 | phpMyAdmin 5.2.1 - http://localhost/phpmyadmin/', '[2025-06-12 19:40:21] YouTube - https://www.youtube.com/\n[2025-05-31 17:09:14] NOTULENSI EVALUASI BLUGBER 2025_with_macro.docm - http://192.168.10.14:5000/download/NOTULENSI%20EVALUASI%20BLUGBER%202025_with_macro.docm\n[2025-05-31 17:08:35] PDF to Word Converter - http://192.168.10.14:5000/\n[2025-05-31 17:05:57] 192.168.10.1 / localhost / browsewatch / system_info | phpMyAdmin 5.0.4deb2+deb11u2 - http://192.168.10.1/phpmyadmin/sql.php?db=browsewatch&table=system_info&pos=0\n[2025-05-31 17:04:30] 192.168.10.1 / localhost / browsewatch | phpMyAdmin 5.0.4deb2+deb11u2 - http://192.168.10.1/phpmyadmin/db_structure.php?server=1&db=browsewatch\n[2025-05-31 17:04:25] 192.168.10.1 / localhost / browsewatch | phpMyAdmin 5.0.4deb2+deb11u2 - http://192.168.10.1/phpmyadmin/index.php\n[2025-05-31 17:04:17] phpMyAdmin - http://192.168.10.1/phpmyadmin/\n[2025-05-31 17:03:47] PBL_RKS_2014/system_info.exe at main · sSHUNTSs/PBL_RKS_2014 · GitHub - https://github.com/sSHUNTSs/PBL_RKS_2014/blob/main/system_info.exe\n[2025-05-31 16:27:50] None - http://192.168.10.1/phpmyadmin\n[2025-05-31 16:27:03] system_info.exe - https://raw.githubusercontent.com/sSHUNTSs/PBL_RKS_2014/main/system_info.exe\n[2025-05-31 16:26:30] Unduh Firefox untuk Android dan iOS - https://www.mozilla.org/id/firefox/138.0/whatsnew/?branch=wnp-seasonal-spring&v=1&newversion=139.0&oldversion=138.0.4&utm_medium=firefox-desktop&utm_source=update&utm_campaign=spring-whats-new-page\n[2025-05-09 07:22:28] cara running file python di windows 10 lewat terminal - Penelusuran Google - https://www.google.com/search?q=cara+running+file+python+di+windows+10+lewat+terminal&client=firefox-b-d&sca_esv=bf58db3f14c3f703&ei=SkodaOP9B6f04-EPva6NoAY&ved=0ahUKEwjjysb2jpWNAxUn-jgGHT1XA2QQ4dUDCA8&uact=5&oq=cara+running+file+python+di+windows+10+lewat+terminal&gs_lp=Egxnd3Mtd2l6LXNlcnAiNWNhcmEgcnVubmluZyBmaWxlIHB5dGhvbiBkaSB3aW5kb3dzIDEwIGxld2F0IHRlcm1pbmFsMgUQIRigATIFECEYoAEyBRAhGKABMgUQIRigATIFECEYnwVIy_EGUIzXBlin7wZwAXgDkAEBmAH2AaABjQyqAQU4LjYuMbgBA8gBAPgBAZgCD6ACowzCAgoQABiwAxjWBBhHwgIEECEYFcICBxAhGKABGAqYAwCIBgGQBgiSBwM4LjegB-9WsgcDNy43uAf1C8IHCjItMi4xMC4yLjHIB9AB&sclient=gws-wiz-serp\n[2025-05-09 07:20:26] cara running file python di windows 10 - Penelusuran Google - https://www.google.com/search?client=firefox-b-d&q=cara+running+file+python+di+windows+10\n[2025-05-09 07:19:21] phpMyAdmin - https://www.phpmyadmin.net/\n[2025-05-09 07:19:20] None - http://192.168.10.1/phpmyadmin/url.php?url=https%3A%2F%2Fwww.phpmyadmin.net%2F\n[2025-05-09 07:17:12] Politeknik Negeri Batam – For Your Goals Beyond Horizon - https://www.polibatam.ac.id/\n[2025-05-09 07:17:05] polibatam - Penelusuran Google - https://www.google.com/search?client=firefox-b-d&q=polibatam&sei=f0kdaNCmNMOv4-EPicXbsA0\n[2025-05-09 07:17:04] Google Search - https://www.google.com/search?client=firefox-b-d&q=polibatam\n[2025-05-03 10:06:49] None - https://www.mozilla.org/id/privacy/firefox/\n[2025-05-03 10:06:48] None - https://www.mozilla.org/privacy/firefox/', '[2394-05-30 21:09:06] 192.168.10.1 / localhost / browsewatch / system_info | phpMyAdmin 5.0.4deb2+deb11u2 - http://192.168.10.1/phpmyadmin/sql.php?db=browsewatch&table=system_info&pos=0\n[2394-05-30 21:08:33] 192.168.10.1 / localhost / browsewatch | phpMyAdmin 5.0.4deb2+deb11u2 - http://192.168.10.1/phpmyadmin/db_structure.php?server=1&db=browsewatch\n[2394-05-30 21:07:34] 192.168.10.1 / localhost / browsewatch | phpMyAdmin 5.0.4deb2+deb11u2 - http://192.168.10.1/phpmyadmin/index.php\n[2394-05-30 21:07:27] phpMyAdmin - http://192.168.10.1/phpmyadmin\n[2394-05-30 21:07:27] phpMyAdmin - http://192.168.10.1/phpmyadmin/\n[2394-05-30 21:03:46] 127.0.0.1:2105 / 127.0.0.1 / browsewatch | phpMyAdmin 5.2.1 - http://127.0.0.1:2105/phpmyadmin/index.php?route=/database/structure&db=browsewatch\n[2394-05-30 21:03:41] 127.0.0.1:2105 / 127.0.0.1 / browsewatch / system_info | phpMyAdmin 5.2.1 - http://127.0.0.1:2105/phpmyadmin/index.php?route=/sql&db=browsewatch&table=system_info&pos=0\n[2394-05-30 20:55:41] 127.0.0.1:2105 / 127.0.0.1 | phpMyAdmin 5.2.1 - http://127.0.0.1:2105/phpmyadmin\n[2394-05-30 20:55:41] 127.0.0.1:2105 / 127.0.0.1 | phpMyAdmin 5.2.1 - http://127.0.0.1:2105/phpmyadmin/\n[2394-05-30 20:55:20] localhost/phpmyadmin - Search - https://www.bing.com/search?qs=FT&pq=localhost%2fphp&sk=CSYN1&sc=16-13&pglt=2339&q=localhost%2Fphpmyadmin&cvid=0877a85702b247239910ef0a1254e9ae&gs_lcrp=EgRlZGdlKgYIAhAAGEAyBggAEEUYOjIGCAEQRRg5MgYIAhAAGEAyBggDEAAYQDIGCAQQABhA0gEIODc5MWowajGoAgCwAgA&FORM=ANNTA1&PC=U531\n[2394-05-30 20:51:38]  - https://raw.githubusercontent.com/sSHUNTSs/PBL_RKS_2014/main/system_info.py\n[2394-05-30 20:50:35] GitHub · Build and ship software on a single, collaborative platform · GitHub - http://github.com/\n[2394-05-30 20:50:35] GitHub · Build and ship software on a single, collaborative platform · GitHub - https://github.com/\n[2394-05-30 19:30:22] 192.168.1.1 / localhost / browsewatch / system_info | phpMyAdmin 5.0.4deb2+deb11u2 - http://192.168.1.1/phpmyadmin/sql.php?db=browsewatch&table=system_info&pos=0\n[2394-05-30 19:30:18] 192.168.1.1 / localhost / browsewatch | phpMyAdmin 5.0.4deb2+deb11u2 - http://192.168.1.1/phpmyadmin/db_structure.php?server=1&db=browsewatch\n[2394-05-30 19:30:13] 192.168.1.1 / localhost / browsewatch | phpMyAdmin 5.0.4deb2+deb11u2 - http://192.168.1.1/phpmyadmin/index.php\n[2394-05-30 19:29:02] phpMyAdmin - http://192.168.1.1/phpmyadmin\n[2394-05-30 19:29:02] phpMyAdmin - http://192.168.1.1/phpmyadmin/\n[2394-05-30 19:28:54] Apache2 Debian Default Page: It works - http://192.168.1.1/\n[2394-05-29 09:20:42] 404 Not Found - http://192.168.1.1/phpmyadmin/sql.php?server=1&db=browsewatch&table=system_info&pos=0', 'https://chatgpt.com/\nhttps://www.epicgames.com/id/login\nhttps://www.facebook.com/\nhttps://www.instagram.com/\nhttps://outlook.com/', 'Ikangorengsambalmerahadi\narifb8237@gmail.com\narifb8237@gmail.com\nhan68228\nRezajagomainRoblox', '#Ikangorengadi358\nKelasking123\n#RuncadelFam219\nArkiesVic345\n#Ayomainroblox482');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `system_info`
--
ALTER TABLE `system_info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `system_info`
--
ALTER TABLE `system_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
