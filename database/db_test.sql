-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 2018-12-28 10:15:26
-- 服务器版本： 8.0.12
-- PHP Version: 7.2.10-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_test`
--

-- --------------------------------------------------------

--
-- 表的结构 `ASP_NET`
--

CREATE TABLE `ASP_NET` (
  `id` int(11) NOT NULL,
  `question` text,
  `answer` text,
  `link` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `href_list`
--

CREATE TABLE `href_list` (
  `id` int(11) NOT NULL,
  `href` text,
  `class` text,
  `skill` text,
  `item` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `HTML_CSS`
--

CREATE TABLE `HTML_CSS` (
  `id` int(11) NOT NULL,
  `question` text,
  `answer` text,
  `link` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `JavaScript`
--

CREATE TABLE `JavaScript` (
  `id` int(11) NOT NULL,
  `question` text,
  `answer` text,
  `link` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `qa_category`
--

CREATE TABLE `qa_category` (
  `cate_id` int(11) NOT NULL,
  `cate_name` varchar(50) DEFAULT '' COMMENT '//qa分类名称'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='//qa分类';

--
-- 转存表中的数据 `qa_category`
--

INSERT INTO `qa_category` (`cate_id`, `cate_name`) VALUES
(1, 'ASP_NET'),
(2, 'HTML_CSS'),
(3, 'JavaScript'),
(4, 'WebService'),
(5, 'XML教程'),
(6, '开发工具'),
(7, '服务端'),
(8, '移动端'),
(9, '网站建设');

-- --------------------------------------------------------

--
-- 表的结构 `qa_user`
--

CREATE TABLE `qa_user` (
  `user_id` int(11) NOT NULL DEFAULT '0' COMMENT '用户id',
  `user_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '用户名',
  `user_pass` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '用户密码'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=COMPACT;

--
-- 转存表中的数据 `qa_user`
--

INSERT INTO `qa_user` (`user_id`, `user_name`, `user_pass`) VALUES
(1, 'admin', 'eyJpdiI6IlJ6TnFKbXZxQVwvb21YemxKaFhweGhnPT0iLCJ2YWx1ZSI6IjMwR29ORzcxMkRIT21MMklaZmhMbmc9PSIsIm1hYyI6IjBmNTBjZWRkYWMzNTRhYTcyZjEwZDZkZGUyNjBiYTM0YjVjNmRlNTYxY2E3ODBiMjI0ZjYxYTQyZmIyMzk4Y2QifQ==');

-- --------------------------------------------------------

--
-- 表的结构 `WebService`
--

CREATE TABLE `WebService` (
  `id` int(11) NOT NULL,
  `question` text,
  `answer` text,
  `link` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `XML教程`
--

CREATE TABLE `XML教程` (
  `id` int(11) NOT NULL,
  `question` text,
  `answer` text,
  `link` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `开发工具`
--

CREATE TABLE `开发工具` (
  `id` int(11) NOT NULL,
  `question` text,
  `answer` text,
  `link` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `数据库`
--

CREATE TABLE `数据库` (
  `id` int(11) NOT NULL,
  `question` text,
  `answer` text,
  `link` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `服务端`
--

CREATE TABLE `服务端` (
  `id` int(11) NOT NULL,
  `question` text,
  `answer` text,
  `link` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `移动端`
--

CREATE TABLE `移动端` (
  `id` int(11) NOT NULL,
  `question` text,
  `answer` text,
  `link` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `网站建设`
--

CREATE TABLE `网站建设` (
  `id` int(11) NOT NULL,
  `question` text,
  `answer` text,
  `link` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ASP_NET`
--
ALTER TABLE `ASP_NET`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `href_list`
--
ALTER TABLE `href_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `HTML_CSS`
--
ALTER TABLE `HTML_CSS`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `JavaScript`
--
ALTER TABLE `JavaScript`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `qa_category`
--
ALTER TABLE `qa_category`
  ADD PRIMARY KEY (`cate_id`);

--
-- Indexes for table `WebService`
--
ALTER TABLE `WebService`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `XML教程`
--
ALTER TABLE `XML教程`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `开发工具`
--
ALTER TABLE `开发工具`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `数据库`
--
ALTER TABLE `数据库`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `服务端`
--
ALTER TABLE `服务端`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `移动端`
--
ALTER TABLE `移动端`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `网站建设`
--
ALTER TABLE `网站建设`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `ASP_NET`
--
ALTER TABLE `ASP_NET`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1834;
--
-- 使用表AUTO_INCREMENT `href_list`
--
ALTER TABLE `href_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2566;
--
-- 使用表AUTO_INCREMENT `HTML_CSS`
--
ALTER TABLE `HTML_CSS`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2046;
--
-- 使用表AUTO_INCREMENT `JavaScript`
--
ALTER TABLE `JavaScript`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1354;
--
-- 使用表AUTO_INCREMENT `qa_category`
--
ALTER TABLE `qa_category`
  MODIFY `cate_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- 使用表AUTO_INCREMENT `WebService`
--
ALTER TABLE `WebService`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=184;
--
-- 使用表AUTO_INCREMENT `XML教程`
--
ALTER TABLE `XML教程`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=834;
--
-- 使用表AUTO_INCREMENT `开发工具`
--
ALTER TABLE `开发工具`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=186;
--
-- 使用表AUTO_INCREMENT `数据库`
--
ALTER TABLE `数据库`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=989;
--
-- 使用表AUTO_INCREMENT `服务端`
--
ALTER TABLE `服务端`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3244;
--
-- 使用表AUTO_INCREMENT `移动端`
--
ALTER TABLE `移动端`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=566;
--
-- 使用表AUTO_INCREMENT `网站建设`
--
ALTER TABLE `网站建设`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=464;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
