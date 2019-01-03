CREATE TABLE `channel` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `channel_id` varchar(50) NOT NULL DEFAULT '',
  `title` varchar(255) NOT NULL DEFAULT '',
  `published_at` datetime DEFAULT NULL,
  `country` varchar(5) DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `channel_id` (`channel_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;