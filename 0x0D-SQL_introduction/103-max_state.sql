--displays the max temperature of each state
SELECT state, MAX(value) AS max_temp
FROM temperatures
WHERE value IS NOT NULL
GROUP BY state
ORDER BY state ASC;
