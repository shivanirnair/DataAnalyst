# Core Python
Bank system project is created with following concepts:
1- Class
2- Function
3- File handling
4- Collections
5- Exception


Details of the program: 
Create new account function:
Input: Name, aadhar card, location and user id
Validations:
	i-For aadhar number: aadhar card digits only
	ii-If the user_id is created in the file and user tries to create it again  then error "user id already 		exist" is displayed

All good scenario -> entry clreated in accfile (all for items in comma separated format)

Signup functions:
Input: user id and password
Validations:
	i- user id should exist in the accfile
	ii- pwd should be alphanumeric with one special char from the list (!@#$%^&*()-+?_=,<>) and password's 			character lengths should be between 6 and 10
	iii- dict varible named dLogin is updated to keep the track of user_id and password
	iv-  dict variable named dBal is updated to keep initial balance 5000Rs for each user Id

Credit function:
	Input amount to be credited
	If the user id exist in dBal then amount will be added to the balance. Final balance will be displayed

Debit function:
	Input amount to be debited
	If the user id exist in dBal then amount will be deducted from the balance. will be displayed



