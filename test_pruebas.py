from database import conectar_db


class DBWriter(object):
    counter = 0

    def __init__(self):
        self.db = conectar_db()

    def commit_to_db(self, sql):
        self.counter += 1
        self.db.commit(sql)

    def save(self, string):
        sql = "INSERT INTO tokens SET token = '{}'".format(string)
        self.commit_to_db(sql)

    def drop(self, string):
        sql = "DELETE FROM tokens WHERE token = '{}'".format(string)
        self.commit_to_db(sql)