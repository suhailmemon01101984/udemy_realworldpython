import logging
import logging.config
import configparser
import psycopg2
class PersistData:
    logging.config.fileConfig("resources/configs/logging.conf")
    logger=logging.getLogger("Persist")
    config=configparser.ConfigParser()
    config.read("resources/fileprocessor.ini")
    def __init__(self,dbType):
        self.logger.debug("init of persistdata")
        self.db_Type=dbType
    def store_data(self):
        try:
            target_table=self.config.get("DATABASE_CONFIGS","PG_TABLE")
            self.logger.debug(f"target tablename is : {target_table}")
            self.logger.debug(f"storing data in db: {self.db_Type}")
            self.write_to_pg(target_table)
            self.read_from_pg(target_table)
            #var1=100/0
        except Exception as exp:
            self.logger.error(f"An error has occurred: {str(exp)}")
    def read_from_pg(self,targettable):
        connection=psycopg2.connect(user='postgres',password='admin',host='localhost',database='postgres')
        curs=connection.cursor()
        select_query=f"select * from {targettable}"
        curs.execute(select_query)
        records=curs.fetchall()
        for item in records:
            print(item)
            print("printed one new record")
        curs.close()
        connection.commit()

    def write_to_pg(self,targettable):
        connection=psycopg2.connect(user='postgres',password='admin',host='localhost',database='postgres')
        curs=connection.cursor()
        insert_query=f"insert into {targettable} \
                        (course_id, course_name, author_name, course_section, creation_date) \
                        values(%s,%s,%s,%s,%s)"
        insert_tuple=(4,'Java Microservices', 'futurexskill', '{}','2020-10-20')
        print("Inserting into pg")
        curs.execute(insert_query,insert_tuple)
        curs.close()
        connection.commit()
