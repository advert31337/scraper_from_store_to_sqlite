# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class PolPipeline(object):
    
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('floor.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists laminat_tb """)
        self.curr.execute("""create table laminat_tb(
                            title  TEXT,
                            link TEXT,
                            price text
                        )""")
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO laminat_tb VALUES (?,?,?)""",
                                (item['title'],
                                item['price'][0],
                                'https://polvamvdom.ru/laminat/' + item['link']))
        self.conn.commit()
