CREATE TABLE `net_test`.`symantec` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `x_description` VARCHAR(45) NULL,
  `x_link` VARCHAR(100) NULL,
  `x_title` VARCHAR(45) NULL,
  `Updated` VARCHAR(45) NULL,
  `Risk_Impact` VARCHAR(10) NULL,
  `Infection_Length` VARCHAR(45) NULL,
  `x_pubDate` VARCHAR(15) NULL,
  `Type` VARCHAR(45) NULL,
  `System_Affected` VARCHAR(100) NULL,
  `Name` VARCHAR(75) NULL,
  `Writeup_By` VARCHAR(55) NULL,
  `Version` VARCHAR(30) NULL,
  `Publisher` VARCHAR(60) NULL,
  `File_Names` VARCHAR(110) NULL,
  `Discovered` VARCHAR(20) NULL,
  `Also_Known_As` VARCHAR(110) NULL,
  `Target_Platform` VARCHAR(35) NULL,
  `Characteristics` VARCHAR(65) NULL,
  `Region_Reported` VARCHAR(30) NULL,
  `Area_of_infection` VARCHAR(65) NULL,
  `Likelihood` VARCHAR(45) NULL,
  `Package_name` VARCHAR(25) NULL,
  `CVE_References` VARCHAR(15) CHARACTER SET 'utf8' NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC));

  CREATE TABLE `net_test`.`Malware` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(45) NULL,
  `link` VARCHAR(100) NULL,
  `Risk_Impact` VARCHAR(10) NULL,
  `Updated` VARCHAR(45) NULL,
  `pubDate` VARCHAR(15) NULL,
  `Version` VARCHAR(30) NULL,
  `Publisher` VARCHAR(60) NULL,
  `File_Names` VARCHAR(110) NULL,
  `Discovered` VARCHAR(20) NULL,
  `Also_Known_As` VARCHAR(35) NULL,
  `Characteristics` VARCHAR(65) NULL,
  `Region_Reported` VARCHAR(30) NULL,
  `Area_of_infection` VARCHAR(65) NULL,
  `Likelihood` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

insert into `Malware` (`type`, `link`, `Risk_Impact`, `Updated`, `pubDate`, `Version`,
`Publisher`, `File_Names`, `Discovered`, `Also_Known_As`, `Characteristics`, `Region_Reported`, `Area_of_infection`,
`Likelihood`) values


CREATE TABLE `net_test`.`vertex` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type` INT NULL,
  `id_search` INT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vertex_unique` (`type`, `id_search`),
  UNIQUE INDEX `idvertex_UNIQUE` (`id` ASC));

  insert into vulnerability (`cveId`, `publishedDatetime`, `lastModifiedDatetime`, `summary`, `type`) values 
            ("CVE-2005-2120", "2005-10-13T06:02:00.000-04:00", "2018-10-12T17:37:05.517-04:00", "Stack-based buffer overflow in the Plug and Play (PnP) service (UMPNPMGR.DLL) in Microsoft Windows 2000 SP4, and XP SP1 and SP2, allows remote or local authenticated attackers to execute arbitrary code via a large number of \"\\" (backslash) characters in a registry key name, which triggers the overflow in a wsprintfW function call.", 1);


-- delete
-- from
-- 	vulnerability
-- where
-- 	cveId in (
-- 		select * from(
--         select 
-- 			cveId
-- 		from
-- 			vulnerability
-- 		group by
-- 			cveId
-- 		having
-- 			count(cveId) > 1
--         ) b 
--     ) and id not in(
-- 		select * from(
--         select
-- 			min(id)
-- 		from
-- 			vulnerability
-- 		group by
-- 			cveId
-- 		having
-- 			count(cveId) > 1
--         ) c 
--     );