#!/usr/bin/python3
"""
This lists all d states from d database hbtn_0e_0_usa
dat starts with 'N'
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetcha11()
    for row in rows:
        print(row)
    cur.close()
    db.close()
