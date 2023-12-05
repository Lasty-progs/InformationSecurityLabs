CREATE TABLE IF NOT EXISTS Users (
     id INTEGER PRIMARY KEY,
     username TEXT NOT NULL,
     password TEXT NOT NULL,
     surname TEXT NOT NULL,
     name TEXT NOT NULL,
     fathername TEXT NOT NULL,
     birthday TEXT NOT NULL,
     birthplace TEXT NOT NULL,
     telnumber TEXT NOT NULL)