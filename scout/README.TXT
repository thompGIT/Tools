scout
 - Agent used to monitor web forums for interesting posts.

Usage
=====
1. Configure the database to specify the forum url and regex patterns to pull data fields.
2. Configure the database to specify key words to search for.
3. Make sure the outbound SNMP server is usable.
4. Update the email recipient for interesting matches.
4. Run scout.py

- To create default database:
sqlite3 scout.db -init create_db.sql


