#----Data Cleaning
SELECT * FROM world_layoffs.layoffs;

#Step 1- Remove duplicates
#Step 2 -Standardize data
#Step 3- Null value or blank values
#Step 4- Remove any column or row not needed

# Created a staging table to perform all operations and original table will stay intact
CREATE TABLE world_layoffs.layoff_staging LIKE  world_layoffs.layoffs;
INSERT INTO world_layoffs.layoff_staging SELECT * FROM world_layoffs.layoffs;

SELECT * FROM world_layoffs.layoff_staging;

#Creating staging table's copy to find the duplicate rows
CREATE TABLE world_layoffs.layoff_staging02 (
  `company` text,
  `location` text,
  `industry` text,
  `total_laid_off` int DEFAULT NULL,
  `percentage_laid_off` text,
  `date` text,
  `stage` text,
  `country` text,
  `funds_raised_millions` int DEFAULT NULL,
  `row_num` int
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

#Remove duplicate -> Added row num (partition by all columns in the table )
		#	and removed rows with row num>2
# When we write a over and partition by all column and get row_number, we will get>1 value in row_num for duplicate rows
INSERT INTO  world_layoffs.layoff_staging02   
SELECT *, ROW_NUMBER() 
		OVER(PARTITION BY company, location, industry, 
			total_laid_off,percentage_laid_off, 'date', stage, country, funds_raised_millions)
            FROM  world_layoffs.layoff_staging ;
            
SELECT * FROM world_layoffs.layoff_staging02 WHERE row_num>1  ;

# validate one or two records from above result
SELECT * FROM world_layoffs.layoff_staging02 WHERE company ='Yahoo';
SELECT * FROM world_layoffs.layoff_staging02 WHERE company ='Cazoo';

DELETE FROM world_layoffs.layoff_staging02 WHERE row_num>1  ;

#Data standardization, remove white spaces in company column
SELECT DISTINCT(TRIM(company)) FROM world_layoffs.layoff_staging02 ;

UPDATE world_layoffs.layoff_staging02 SET company = TRIM(company);
SELECT * FROM world_layoffs.layoff_staging02 ;

##Data standardization, Update crypto or crypto currency to "Crypto"
SELECT DISTINCT(industry) FROM world_layoffs.layoff_staging02 ;
SELECT * FROM world_layoffs.layoff_staging02 
WHERE industry LIKE 'Crypto%' ORDER BY industry;

UPDATE world_layoffs.layoff_staging02  SET industry = 'Crypto' WHERE industry LIKE 'Crypto%' ;

#Validate updates
SELECT DISTINCT(industry) FROM world_layoffs.layoff_staging02 ;

### Data Standardization Update country name remove space and . at the end
# in this United states has . in the end
SELECT DISTINCT(country) FROM world_layoffs.layoff_staging02 ;

SELECT DISTINCT country, TRIM(TRAILING '.' FROM country)  FROM world_layoffs.layoff_staging02 ORDER BY 1;

UPDATE world_layoffs.layoff_staging02  
	SET country = TRIM(TRAILING '.' FROM country) 
    WHERE country LIKE 'United States%';
    
####Data Standardization : Date column is TEXT type so we need to convert to DATE type like 
SELECT `date` , STR_TO_DATE(`date`,'%m/%d/%Y') FROM  world_layoffs.layoff_staging02  ;

UPDATE world_layoffs.layoff_staging02  SET `date` =STR_TO_DATE(`date`,'%m/%d/%Y') ;

#Never do it on raw table you can do it on staging table , 
#we will now change the data type of date columnt to DATE
ALTER TABLE world_layoffs.layoff_staging02 MODIFY COLUMN `date` DATE;


#####Data Standardization : industry column is blank for some rows 
#and for the same company name industry column present in other rows
SELECT * FROM world_layoffs.layoff_staging02 t1 
			JOIN world_layoffs.layoff_staging02 t2
            ON t1.company = t2.company 
	WHERE (t1.industry IS NULL OR t1.industry ='')AND t2.industry IS NOT NULL;
    
  #  update t1.industry (value null or blank '') with t2.industry (Self join)
  UPDATE  world_layoffs.layoff_staging02 t1 
		SET t1.industry = null
	WHERE t1.industry ='';
  
  UPDATE  world_layoffs.layoff_staging02 t1 
		JOIN world_layoffs.layoff_staging02 t2
            ON t1.company = t2.company 
		SET t1.industry = t2.industry
	WHERE (t1.industry IS NULL OR t1.industry ='')AND t2.industry IS NOT NULL;
    
#To  check if there are any nulls in industry. There is one, we will check by company name now
SELECT * FROM world_layoffs.layoff_staging02 t1 
    WHERE t1.industry IS NULL;

#As there is only one row so we do not know the industry and hencce we will keep it as is
SELECT * FROM world_layoffs.layoff_staging02 t1 
    WHERE t1.company LIKE 'Bally%';    
    
######Data Standardization : total laid off and percentage laid off null, which means no layoffs
    SELECT * FROM world_layoffs.layoff_staging02
		WHERE total_laid_off IS NULL AND percentage_laid_off IS NULL;

DELETE FROM world_layoffs.layoff_staging02
		WHERE total_laid_off IS NULL AND percentage_laid_off IS NULL;

######Data Standardization : We dont need the row num column now
SELECT * FROM world_layoffs.layoff_staging02;
ALTER TABLE world_layoffs.layoff_staging02 DROP COLUMN row_num;
