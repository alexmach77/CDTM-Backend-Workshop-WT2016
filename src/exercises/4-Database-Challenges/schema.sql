PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Cookies;
DROP TABLE IF EXISTS Users;
CREATE TABLE Users(
  id          INTEGER      PRIMARY KEY AUTOINCREMENT,
  name        TEXT         NOT NULL UNIQUE,
  created     TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

PRAGMA foreign_keys = ON;

CREATE TABLE Cookies(
  cookie_id   INTEGER      PRIMARY KEY AUTOINCREMENT,
  owner       INTEGER	   ,
  type        TEXT         NOT NULL DEFAULT "Zimtstern",
  FOREIGN KEY(owner)       REFERENCES Users(id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS Lists;
DROP TABLE IF EXISTS Tasks;
CREATE TABLE Lists(
  id          INTEGER      PRIMARY KEY AUTOINCREMENT,
  title       TEXT         NOT NULL,
  revision    INTEGER      NOT NULL DEFAULT 1,
  inbox       INTEGER      NOT NULL DEFAULT 0,
  created     TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Tasks(
  id          INTEGER      PRIMARY KEY AUTOINCREMENT,
  list        INTEGER      NOT NULL,
  title       TEXT         NOT NULL,
  status      TEXT	       NOT NULL,
  description TEXT	       NOT NULL DEFAULT '',
  due         TIMESTAMP    ,
  revision    INTEGER      NOT NULL DEFAULT 1,
  created     TIMESTAMP    DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(list)        REFERENCES lists(id) ON DELETE CASCADE 
);

