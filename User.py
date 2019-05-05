class User():

	def __init__(self, id, name, address):

		self._id = id
		self._name = name
		self._address = address
		self._books_on_loan = []

	def get_id(self):
		return self._id

	def get_name(self):
		return self._name

	def get_address(self):
		return self._address

	def get_book_on_loan(self):
		return self._books_on_loan

	# Should I have this option here? I dont think so. but just for the sake I will leave it here
	def set_id(self, id):
		self._id = id

	def set_name(self, name):
		self._name = name

	def set_address(self, address):
		self._address = address


	def borrow_book(self, book):
		self._books_on_loan.append(book.get_title())
		book._on_loan = True




	def __str__(self):

		# I am not sure if should slice the list here
		# But couldn't find another way.
		l_books = ''
		if self.get_book_on_loan():
			for l in self.get_book_on_loan():
				l_books = l_books + l + ', '

			l_books = l_books[:-2]

		if l_books == '':
			l_books = 'None'

		return f' ID:{self.get_id()},' \
			f' Name: {self.get_name()},' \
			f' Address: {self.get_address()}\n' \
			f' Books on loan: {str(l_books)}'
