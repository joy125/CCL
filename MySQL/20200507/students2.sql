BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "students" (
	"cID"	TEXT,
	"cName"	TEXT,
	"cSex"	TEXT,
	"cBirthday"	TEXT,
	"cEmail"	TEXT,
	"cPhone"	TEXT,
	"cAddr"	TEXT
);
INSERT INTO "students" VALUES ('"01"','"dog"','"M"','"1111-11-11"','NULL','"wowowo"','NULL');
INSERT INTO "students" VALUES ('"13"','"mimi"','"F"','"1111-11-11"','NULL','"nayanynay"','NULL');
INSERT INTO "students" VALUES ('"14"','"14"','"F"','"1111-11-11"','NULL','NULL','NULL');
INSERT INTO "students" VALUES ('"15"','"15"','"F"','"2020-05-01"','NULL','NULL','NULL');
COMMIT;
