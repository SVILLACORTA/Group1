# Team Big Fit
# Created by: Serena Villacorta
# main program

from User import User
from BigFitDAO import BigFitDAO

def main():
    bfDAO = BigFitDAO()
    insert_user = User('Gaga', 'Lady', 120, 114, 5, 2, '02-FEB-1985', 'F', '91001', 'gaga.lady@gmail.com', '14-OCT-2018', None, 'g1234')
    conn = bfDAO.create_connection()

    with conn:
        all_users = bfDAO.select_all_users(conn)
        for x in all_users:
            print(x)

        single_user = bfDAO.select_user_by_user_id(conn, 1)
        for x in single_user:
            print(x)

        bfDAO.insert_user(conn, insert_user)


if __name__ == "__main__":
    main()
