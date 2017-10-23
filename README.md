Overview: This program prints out reports based on the data in the given database. SQL functions are run for three separate queries, each searching the database for different pieces of information. 

Log Analysis

To run the program:

Launch the vagrant VM by typing : $ vagrant up 
Then log in using command: $ vagrant ssh
And change into the /vagrant directory using: cd /vagrant 

To Set up the database and to Create the views:

Load the data into the database using command: sql -d news -f newsdata.sql

To create view article_view:
create view article_view as select title,author,count(*) as views from articles,log where 
  log.path like concat('%',articles.slug) group by articles.title,articles.author 
  order by views desc;

To create view error_log_view:
create view error_log_view as select date(time),round(100.0*sum(case log.status when '200 OK' 
  then 0 else 1 end)/count(log.status),2) as "Percent Error" from log group by date(time) 
  order by "Percent Error" desc;


Then, from the vagrant directory, run the program using command: $ python log.py
