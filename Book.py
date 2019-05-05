from LibraryItem import LibraryItem


# To be easy to find what is inherited, I am using the '(h)' as a hint
# id(h) | title(h) | year(h) | isbn | author
class Book(LibraryItem):

	def __init__(self, item_id, title, year, isbn, author, on_loan):
		LibraryItem.__init__(self, item_id, title, year)
		self._isbn = isbn
		self._author = author
		self._on_loan = on_loan

	def get_isbn(self):
		return self._isbn

	def get_author(self):
		return self._author

	def get_on_loan(self):
		return self._on_loan

	def set_isbn(self, isbn):
		self._isbn = isbn

	def set_author(self, author):
		self._author = author

	def set_on_loan(self, on_loan):
		self._on_loan = on_loan

	def __str__(self):
		return f' ID: {self.get_item_id()},' \
			f' ISBN: {self.get_isbn()},' \
			f' Title: {self.get_title()},' \
			f' Author: {self.get_author()},' \
			f' Year: {self.get_year()},' \
			f' On Loan: {self.get_on_loan()}'
