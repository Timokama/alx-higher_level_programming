#!/usr/bin/python3
"""SQL injection safe query to get rows of states where name matches
an argument.
"""

if __name__ == "__main__":
        import MySQLdb
        import sys

        db = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2],
                             database=sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states "
                    "ORDER BY id ASC")
        for row in cur.fetchall():
            if (state[1] == sys.arvg[4]):
                print(row)
        cur.close()
        db.close()
