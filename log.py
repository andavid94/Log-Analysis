#!/usr/bin/env

import psycopg2


dbName = "news"


#  Define each of the required queries
query1 = "select title, views from article_view"
query2 = """select authors.name, sum(article_view.views) as views from
    article_view, authors where authors.id = article_view.author
    group by authors.name order by views desc"""
query3 = "select * from error_log_view where \"Percent Error\" > 1"


#  Define method to execute query 1
def executeQuery1(query):
    db = psycopg2.connect(database=dbName)
    c = db.cursor()
    c.execute(query1)
    results = c.fetchall()
    print('1. The 3 most popular articles of all time are: ')
    for x in range(0, 3):
        articleTitle = results[x][0]
        articleViews = results[x][1]
        print('%s--->%d views' % (articleTitle, articleViews))
    print('\n')
    db.close()


#  Define a method to execute query 2
def executeQuery2(query):
    db = psycopg2.connect(database=dbName)
    c = db.cursor()
    c.execute(query2)
    results = c.fetchall()
    print('2. The most popular article authors of all time are: ')
    count = len(results)
    x = 0
    while x < count:
        authorName = results[x][0]
        authorViews = results[x][1]
        print('%s--->%d views' % (authorName, authorViews))
        x = x + 1
    print('\n')
    db.close()


#  Define function to execute query 3
def executeQuery3(query):
    db = psycopg2.connect(database=dbName)
    c = db.cursor()
    c.execute(query3)
    results = c.fetchall()
    print('Days with more than 1% of requests that lead to an error: ')
    count = len(results)
    x = 0
    while x < count:
        date = results[x][0]
        percent_error = results[x][1]
        print('%s--->%.2f %% views' % (date, percent_error))
        x = x + 1
    db.close()


if __name__ == '__main__':
    executeQuery1(query1)
    executeQuery2(query2)
    executeQuery3(query3)
