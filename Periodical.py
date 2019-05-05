from LibraryItem import LibraryItem


# To be easy to find what is inherited, I am using the '(h)' as a hint
# id(h) | title(h) | year(h) | editor | volume | issue
class Periodical(LibraryItem):

	def __init__(self, item_id, title, year, editor, volume, issue):
		LibraryItem.__init__(self, item_id, title, year)
		self._editor = editor
		self._volume = volume
		self._issue = issue

	def get_editor(self):
		return self._editor

	# get
	def get_volume(self):
		return self._volume

	def get_issue(self):
		return self._issue

	def set_editor(self, editor):
		self._editor = editor

	def set_volume(self, volume):
		self._volume = volume

	def set_issue(self, issue):
		self._issue = issue

	def __str__(self):
		return f'ID:{self.get_item_id()},' \
			f' Editor:{self.get_editor()},' \
			f' Title:{self.get_title()},' \
			f' Volume:{self.get_volume()},' \
			f' Year:{self.get_year()},' \
			f' Issue:{self.get_issue()}'
