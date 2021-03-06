#!/usr/bin/env python2


from pysqlcipher import dbapi2 as sqlite

db = 'output_db.db'
output = 'output_encrypted_db.db'

key = '0123456'

print "Please change the 'key', 'db', and 'output' first!"
print "key='"+key+"'"


try:
    conn = sqlite.connect(db)
    c = conn.cursor()

    # c.execute("PRAGMA key = '" + '' + "';")
    # c.execute("PRAGMA cipher_use_hmac = OFF;")
    # c.execute("PRAGMA cipher_page_size = 1024;")
    # c.execute("PRAGMA kdf_iter = 4000;")
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")

    c.execute("ATTACH DATABASE '" + output + "' AS db KEY '" + key + "';")

    # https://www.zetetic.net/sqlcipher/sqlcipher-api/#sqlcipher_export
    c.execute("PRAGMA db.cipher_use_hmac = OFF;")
    c.execute("PRAGMA db.cipher_page_size = 1024;")
    c.execute("PRAGMA db.kdf_iter = 4000;")

    c.execute("SELECT sqlcipher_export('db');")
    c.execute("DETACH DATABASE db;")
    print "Decrypt and dump database to {} ... ".format(output)
    print key
    print('OK!!!!!!!!!')
    # with open('CRACKED_PASS.txt', 'a') as f:
    #     f.write(key)
    #     f.write('\n')
except Exception as e:
    print(str(e))
    # pass
finally:
    conn.close()
