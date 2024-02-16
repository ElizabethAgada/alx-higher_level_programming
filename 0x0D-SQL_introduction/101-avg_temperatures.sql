-- DIsplays d avg temp (in Fahrenheit) by d city ordered by descending
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC
