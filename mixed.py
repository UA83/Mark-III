from Book import Book

list_of_book = [Book('10', 'Python BG', '2019', '123456789123', 'Ulisses Alves'),
                Book('20', 'Python MT', '2018', '987654321987', 'Stephanie Enders'),
                Book('30', 'Python AA', '2019', '143567833456', 'Suki Dog')]

#display all books


#add book
id, title, year, isbn, author = '22', 'new book', '2000', '777777777777', 'Marvel'
list_of_book.append(Book(id, title, year, isbn, author))

#for b in list_of_book:
#    print(b)

to_search = '20001'

x = Book.find_book(list_of_book, str(to_search))
if not x:
    print('no found')
else:
    for b in x:
        print(b)



#search book
#delete book


# [1] Display Users
# [2] Add User
# [3] Delete USer
# [4] Search User
# [5] Add Book
# [6] Borrow Book
# [7] Delete Book
# [8] Display Books
# [9] Return Book
# [10] Search Book
# [11] Add Periodical
# [12] Delete Periodical
# [13] Display Periodicals
# [14] Search Periodical



