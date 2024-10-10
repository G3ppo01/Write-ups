# 2022 Challenge #3 Anonymize Data
## Process
- Created a script that connects to the .db file, retrieves data from a query, and generates a csv as an output.
- Created a template for other exercises like this one. The only thing to do is open the code in an IDE, change the query, and launch the script.
- I'll change that in the template, I want the query to be asked to the user. It would be cool to permit the user to have multiple lines in the input field instead of a long one-line query.
- For yet it works.

  ## Other, faster way to do it
- Open the de file with DB Browser (SQLite)
- Create a query
```
SELECT 
    t_customer.gender AS gender,
    SUBSTR(t_customer.lastname, 1, 2) || '--------' AS lastname,
    SUBSTR(t_customer.birthdate, 7, 4) AS birthdate,
    SUBSTR(t_location.zip, 1, 2) || '00' AS zip,
    t_customer_status.status AS status
FROM 
    t_customer
JOIN 
    t_location 
    ON t_customer.fk_location = t_location.pk_location
JOIN 
    t_customer_status 
    ON t_customer.fk_customer_status = t_customer_status.pk_customer_status;

```

- Export the output as a csv from the software

## Query explanation:
- ``` t_customer.gender AS gender```: Selects the gender of the customer.
- ```substr(t_customer.lastname, 1, 2) || '--------' AS lastname```: Masks the lastname to keep only the first two characters and replaces the rest with 8 dashes, which is suitable for anonymization.
- ```substr(t_customer.birthdate, -4) AS birthyear```: Extracts the last four characters of the birthdate, which is assumed to represent the year.
- ```substr(t_location.zip, 1, 2) || '00' AS zip```: Adjusts the zip code to keep the first two digits and changes the last two digits to '00', reducing its precision.
- ```t_customer_status.status AS status```: Retrieves the status of the customer without modification.
- Use an Inner Join to correlate the data from every table thank to their foreign/private keys
