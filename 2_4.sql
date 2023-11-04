SELECT country, COUNT(customer_id) AS number_of_customers, AVG(age) AS average_age
FROM Customers
GROUP BY country;  -- 결과를 "country"별로 그룹화합니다.
/*
"country", "number_of_customers", "average_age" 칼럼을 출력한다.
"Customers" 테이블에서 데이터를 가져온다.
결과를 "country"별로 그룹화한다.
*/
