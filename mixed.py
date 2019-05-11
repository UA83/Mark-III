import re
r = re.compile("^[A-Za-z0-9 ,-]*[A-Za-z0-9][A-Za-z0-9 ,-]*$")
#r = re.compile("^[A-Za-z ]*[A-Za-z][A-Za-z ]*$")
x = input('fisrt time')
while r.match(x) is None:
    print('fff')
    x = input('again')




    #search_index = input(f' Enter User ID to Return:')
    #u_index = get_user_index(search_index)
    #
    # x = list_users[u_index].get_book_on_loan()
    #
    # search_book = input(f' Enter Book ID to Return:')
    # b_index = get_book_index(search_book)
    #
    # if list_of_book[b_index].get_on_loan() == list_users[u_index].get_name():
    #     print('Trrrrru')
    #
    # print(x)
    # x.remove('A Game of Thrones')
    #
    # list_users[u_index].return_book('A Game of Thrones')
    # list_of_book[b_index].set_on_loan('No')


