BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "students" (
	"cID"	TEXT,
	"cName"	TEXT,
	"cSex"	TEXT,
	"cBirthday"	TEXT,
	"cEmail"	TEXT,
	"cPhone"	TEXT,
	"cAddr"	TEXT,
	"cHeight"	TEXT,
	"cWeight"	TEXT
);
INSERT INTO "students" VALUES ('"1"','"張惠玲"','"F"','"1987-04-04"','"elven@superstar.com"','"0922988876"','"台北市濟洲北路12號"','"160"','"49"');
INSERT INTO "students" VALUES ('"2"','"彭建志"','"M"','"1987-07-01"','"jinglun@superstar.com"','"0918181111"','"台北市敦化南路93號5樓"','"175"','"72"');
INSERT INTO "students" VALUES ('"3"','"謝耿鴻"','"M"','"1987-08-11"','"sugie@superstar.com"','"0914530768"','"台北市中央路201號7樓"','"162"','"65"');
INSERT INTO "students" VALUES ('"4"','"蔣志明"','"M"','"1984-06-20"','"shane@superstar.com"','"0946820035"','"台北市建國路177號6樓"','"178"','"72"');
INSERT INTO "students" VALUES ('"5"','"王佩珊"','"F"','"1988-02-15"','"ivy@superstar.com"','"0920981230"','"台北市忠孝東路520號6樓"','"164"','"45"');
INSERT INTO "students" VALUES ('"6"','"林志宇"','"M"','"1987-05-05"','"zhong@superstar.com"','"0951983366"','"台北市三民路1巷10號"','"172"','"75"');
INSERT INTO "students" VALUES ('"7"','"李曉薇"','"F"','"1985-08-30"','"lala@superstar.com"','"0918123456"','"台北市仁愛路100號"','"158"','"56"');
INSERT INTO "students" VALUES ('"8"','"賴秀英"','"F"','"1986-12-10"','"crystal@superstar.com"','"0907408965"','"台北市民族路204號"','"166"','"48"');
INSERT INTO "students" VALUES ('"9"','"張雅琪"','"F"','"1988-12-01"','"peggy@superstar.com"','"0916456723"','"台北市建國北路10號"','"168"','"50"');
INSERT INTO "students" VALUES ('"10"','"許朝元"','"M"','"1993-08-10"','"albert@superstar.com"','"0918976588"','"台北市北環路2巷80號"','"169"','"68"');
INSERT INTO "students" VALUES ('"11"','"李柏恩"','"M"','"1981-06-15"','"born@superstar.com"','"0929011234"','"台中市美村南路12號"','"174"','"92"');
INSERT INTO "students" VALUES ('"12"','"周柔揉"','"F"','"1994-07-18"','" yoyo@superstar.com "','"0988647834"','"台北縣永和路8號"','"174"','"60"');
INSERT INTO "students" VALUES ('"13"','"吳政傑"','"M"','"1985-09-08"','"tahai@superstar.com"','"0912678884"','"高雄縣三多路49號"','"168"','"58"');
INSERT INTO "students" VALUES ('"14"','"楊伯承"','"M"','"1990-08-01"','"evo@superstar.com"','"0955689145"','"桃園縣中正二路10號"','"171"','"61"');
INSERT INTO "students" VALUES ('"15"','"陳鈺嬋"','"F"','"1992-06-16"','"silvia@superstar.com"','"0932564379"','"新竹縣中山路100號"','"162"','"49"');
INSERT INTO "students" VALUES ('"19"',NULL,'"F"','"0000-00-00"','NULL','NULL','NULL','NULL','NULL');
INSERT INTO "students" VALUES ('"18"',NULL,'"M"','"0000-00-00"','NULL','NULL','NULL','NULL','NULL');
COMMIT;
