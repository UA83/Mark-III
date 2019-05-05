# Populates the library system with books.
# id(h) | isbn | title(h) | author | year(h) | on_loan
# id(h) | title(h) | year(h) | isbn | author
# id    | Name  | Address | list of books???
from User import User
from Book import Book
from Periodical import Periodical



# List of books
list_of_book = [Book('1', 'A Game of Thrones', '1996', '9780553573404', 'George R. R. Martin', 'No'),
                Book('12', 'A Clash of Kings', '1998', '9753407447831', 'George R. R. Martin', 'No'),
                Book('3', 'A Storm of Swords', '2000', '9789573029348', 'George R. R. Martin', 'No'),
                Book('4', 'A Feast for Crows', '2005', '9786857302245', 'George R. R. Martin', 'No'),
                Book('6', 'Test for ID', '2019', '7823612876545', 'Ulisses Alves', 'No'),
                Book('5', 'A Dance with Dragons', '2011', '9798310843234', 'George R. R. Martin', 'No')]

# Periodicals have a ID, title, year, an editor, volume, issue.
# Periodicals can’t be loaned.
list_of_periodical = [Periodical('35', 'How does it work?', '1983', 'Ulisses Mirage', '3', '123'),
                      Periodical('43', 'IronMan, Nano Technology', '2017', 'Stan Lee', '1', '32'),
                      Periodical('32', 'The power of food', '2018', 'John Dee', '1', '21'),
                      Periodical('88', 'Adventures of a dog called Suki', '2019', 'Stephanie Enders', '7', '456')]


# List of the Library's users
list_users = [User('4', 'Ulisses Alves', '1983 California Upper DB'),
              User('3', 'Stephanie Enders', '168 New York Corner DB'),
              User('5', 'Tony Stark', '10880 Malibu Point CL'),
              User('1', 'Ayrton Senna', '1993 Interlagos SP'),
              User('2', 'Joe Ramone', '315 Bowery Ny')]
