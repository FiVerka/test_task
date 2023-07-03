# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import psycopg2
import time


class SavingToPostgresPipeline:

    def __init__(self):
        self.connection = self.create_connection()
        self.cur = self.connection.cursor()
        # Create flats table if none exists
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS flat(
                id serial PRIMARY KEY,
                title text,
                image_url text
            )
            """
        )
        # Delete flats table contents if data exists
        self.cur.execute("""
                DELETE FROM flat *
                """)

    def create_connection(self):
        hostname = '127.0.0.1'
        username = 'myuser'
        password = '1234'
        database = 'sreality'

        conn = None
        while not conn:
            try:
                # conn = psycopg2.connect(
                #     dbname=database,
                #     user=username,
                #     password=password,
                #     host=hostname
                # )
                conn = psycopg2.connect('postgresql://myuser:1234@database:5432/sreality')
                print("Scraper: Database connection successful")
            except psycopg2.OperationalError as e:
                print(e)
                time.sleep(5)
        return conn

    def process_item(self, item, spider):
        self.store_in_db(item)
        return item

    def store_in_db(self, item):
        self.cur.execute(
            """ insert into flat (title, image_url) values (%s,%s)""", (
                item["title"],
                str(item["image_url"])
            )
        )

        self.connection.commit()

    def close_spider(self, spider):
        # Close cursor & connection to database
        self.cur.close()
        self.connection.close()
