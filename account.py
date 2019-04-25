class Account:
	# """docstring for ClassName"""	
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.balance = 0

	def welcome(self):
		return "Heey {} {} your account balance is {}".format(self.first_name,self.last_name,self.balance)


	def deposit(self,x):
		deposit = x
		self.balance = self.balance + x

		deposit = "Dear {} {} deposit of ksh {} was successful ".format(self.first_name,self.last_name,x,self.balance)
		return deposit
		

	def withdraw(self,m):
		withdraw = m
		if m>self.balance:
			return "can't withdraw"
		else:
			self.balance = self.balance - m
			message = "Dear {} {} withdrawal of ksh {} was successful ".format(self.first_name,self.last_name,m,self.balance)
		return message



	def show_balance(self):
		show_balance = self.balance
		text = "Dear {} {} your current balance is {}".format(self.first_name,self.last_name,self.balance)
		return text