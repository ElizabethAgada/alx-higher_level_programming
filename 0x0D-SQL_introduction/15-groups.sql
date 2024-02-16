-- Lists d nums of records with d same score in d table second_table in my MySQL server.
--Records are ordered by descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number' DESC;
