# import functions from password manager
from password_functions import *

def main():
    # show splash screen
    show_splash()
    while True:
        print('\n\n1: Add password\n2: Display Passwords\n3: Delete Password\n4: Find passwords by name\n5: Delete duplicate passwords\n6: Add Note\n0: Exit\n')
        # t: Test with random password
        # del: DELETE DATABASE
        # test: developer testing, run all functions
        choice = input(red('Choice: '))
        # add username and password to database
        if choice == '1':
            link_account()
        elif choice == '2':
            # display all passwords in alphabetical order by username
            show_passwords()
        elif choice == '3':
            # delete password from database using username
            delete_password()
        elif choice == '4':
            # search for password by username
            find_password()
        elif choice == '5':
            # delete duplicate passwords
            delete_duplicates()
        elif choice == '6':
            # add note to password
            add_note()
        elif choice == '0':
            print('Exiting...')
            exit(1)
        # dev options below
        elif choice == 'test':
            # developer testing, run all functions
            test()
        elif choice == 't':
            # add random passwords to database by number
            random_passwords()
        elif choice == 'del':
            # NUKE OPTION delete Entire database
            delete_database()
        else:
            print('\nInvalid choice\n')

if __name__ == "__main__":
    main()