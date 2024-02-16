-- Lists all the records that are in d table second-table with a score >= 10 in My MySQL server.
-- Records are ordered by descending score.
SELECT `score` `name` FROM `second_table`
WHERE `score` >=10
ORDER BY `score` DESC;
