#!/usr/bin/env python2.7

import time
import datetime
import psycopg2

# Constant variable for the database name
DBNAME = "news"


def connect_query_db(query):
    # Connects to the database and execute a single query (input parameter)

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    query_results = c.fetchall()
    db.close()
    return query_results


def get_popular_3_articles():
    # Provides a query to capture the most popular three articles
    # and prints answer in formatted text
    query_articles = '''SELECT
                            articles.title,
                            COUNT(log.id) AS number_of_successful_GET
                        FROM
                            articles, log
                        WHERE
                            articles.slug = SUBSTRING(log.path,10)
                        AND method = 'GET'
                        AND status = '200 OK'
                        GROUP BY articles.title
                        ORDER BY number_of_successful_GET DESC
                        LIMIT 3;
                      '''
    top_3_popular_articles = connect_query_db(query_articles)

    print "\n1. What are the most popular three articles of all time?\n"

    for item in top_3_popular_articles:
        print '"' + item[0] + '"' + " - " + str(item[1]) + " views"

    return


def get_most_popular_article_authors():
    # Provides a query to capture the most popular article authors
    # and prints answer in formatted text
    query_authors = '''
                    SELECT
                      authors.name,
                      COUNT(log.id) as count
                    FROM
                      authors,
                      articles,
                      log
                    WHERE
                      authors.id = articles.author
                      AND articles.slug = SUBSTRING(log.path,10)
                    GROUP BY authors.name
                    ORDER BY count DESC;
                    '''

    most_popular_article_authors = connect_query_db(query_authors)

    print "\n2. Who are the most popular article authors of all time?\n"

    for item in most_popular_article_authors:
        print item[0] + " - " + str(item[1]) + " views"

    return


def get_more_than_1_precent_errors():
    # Provides a query to capture the days with more than 1% of
    # requests that led to errors and prints answer in formatted text
    query_percentage = '''
                        SELECT
                            total_request_count.totalcountdate,
                            (total_error_count.errorcount * 1.0 /
                                total_request_count.totalrequestcount) * 100
                        AS errorpercentage
                        FROM total_request_count
                        LEFT JOIN total_error_count
                        ON total_request_count.totalcountdate =
                            total_error_count.errordate
                        WHERE ((total_error_count.errorcount * 1.0 /
                            total_request_count.totalrequestcount) * 100 > 1)
                        ORDER BY total_request_count.totalcountdate DESC;
                        '''

    more_than_1_percent = connect_query_db(query_percentage)

    print "\n3. On which days did more than 1% of requests lead to errors?\n"
    for item in more_than_1_percent:
        print item[0].strftime("%B %d, %Y") \
            + " - " \
            + str(round(item[1], 2)) \
            + " %\n"

    return


get_popular_3_articles()
get_most_popular_article_authors()
get_more_than_1_precent_errors()
