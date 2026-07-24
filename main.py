# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd


# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Select employeeNumber and lastName from employees
df_first_five = pd.read_sql(
	"""
	SELECT employeeNumber, lastName
	FROM employees
	""",
	conn,
)

# STEP 3
# Same as step 2 but with lastName first
df_five_reverse = pd.read_sql(
	"""
	SELECT lastName, employeeNumber
	FROM employees
	""",
	conn,
)

# STEP 4
# Alias employeeNumber as ID
df_alias = pd.read_sql(
	"""
	SELECT lastName, employeeNumber AS ID
	FROM employees
	""",
	conn,
)

# STEP 5
# Use CASE to mark Executives vs Not Executive
df_executive = pd.read_sql(
	"""
	SELECT *,
		CASE
			WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing' THEN 'Executive'
			ELSE 'Not Executive'
		END AS role
	FROM employees
	""",
	conn,
)

# STEP 6
# Length of lastName as name_length
df_name_length = pd.read_sql(
	"""
	SELECT LENGTH(lastName) AS name_length
	FROM employees
	""",
	conn,
)

# STEP 7
# First two letters of jobTitle as short_title
df_short_title = pd.read_sql(
	"""
	SELECT SUBSTR(jobTitle, 1, 2) AS short_title
	FROM employees
	""",
	conn,
)

# STEP 8
# Sum of rounded priceEach * quantityOrdered
_tmp = pd.read_sql(
	"""
	SELECT ROUND(priceEach * quantityOrdered) AS total_price
	FROM orderdetails
	""",
	conn,
)
# produce a single-item list so sum_total_price[0] returns the total
sum_total_price = [int(_tmp['total_price'].sum())]

# STEP 9
# Return orderDate and day/month/year derived columns from orders table
df_day_month_year = pd.read_sql(
	"""
	SELECT orderDate,
		strftime('%d', orderDate) AS day,
		strftime('%m', orderDate) AS month,
		strftime('%Y', orderDate) AS year
	FROM orders
	""",
	conn,
)


# Close the connection
conn.close()
