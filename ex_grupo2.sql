
# Execício 1
SELECT c.name, COUNT(o.id) FROM customers c, orders o WHERE c.id = o.customer_id AND o.orders_date < '2016-07-01' GROUP BY c.id;

# Execício 2
SELECT p.name product_name, c.name category_name FROM products p, categories c WHERE p.category_id = c.id AND p.amount > 100 AND c.id IN (1, 2, 3, 6, 9) ORDER BY c.id;
## A troca dos nomes das colunas é para evitar erros de ambiguidade/confusão na hora de ler o resultado.

# Execício 3
SELECT c.name, sum(p.ammount) FROM categories c, products p WHERE c.id = p.category_id GROUP BY c.id;