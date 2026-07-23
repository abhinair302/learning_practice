# Leetcode Problem No: 175- Combine Two Tables

select Person.firstName,Person.lastName,Address.city,Address.state from Person LEFT JOIN Address USING (personId);



# Leetcode Problem No: 182- Duplicate Eamils

select email AS Email from Person group by email having count(email)>1;



# Leetcode Problem No: 183- Customer who Never Ordered

Select name as Customers from Customers where id not in (select customerId from Orders);


# Leetcode Problem No: 577- Employee Bonus

select Employee.name,Bonus.bonus from Employee LEFT JOIN Bonus using(empId) where Bonus.bonus<1000 or Employee.empId NOT IN (Select empId from Bonus);
