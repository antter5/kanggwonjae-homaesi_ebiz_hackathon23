SELECT Customers.first_name, Customers.country, Shippings.status
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id
JOIN Shippings ON Customers.customer_id = Shippings.customer
WHERE Orders.item = 'Keyboard';
/*
"first_name", "country", "status" 칼럼을 출력한다.
"Customers" 테이블에서 데이터를 가져온다.
"Orders" 테이블을 "Customers" 테이블과 결합하고, "customer_id"를 기준으로 한다.
"Shippings" 테이블을 "Customers" 테이블과 결합하고, "customer_id"를 기준으로 한다.
"Orders" 테이블의 "item"이 'Keyboard'인 행만 선택한다.
*/
