# Delete duplicate passwords from database
import time
import sqlite3
import random
import string as s
from pyfiglet import Figlet
from random import choice



def show_splash():
    '''
    Display splash screen
    '''
    clear_screen()
    title = 'Pasword MGR'
    figlet = Figlet()
    fonts = figlet.getFonts()
    f = Figlet(font='3-d')
    print(f.renderText(title))
    sleep(2)
    clear_screen()


def delete_duplicates():
    clear_screen()
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    # create table called passwords if it does not exist
    create_database()
    c.execute(
        "DELETE FROM passwords WHERE rowid NOT IN (SELECT MIN(rowid) FROM passwords GROUP BY username)")
    conn.commit()
    c.close()
    conn.close()
    print(red('\nDuplicate passwords deleted'))
    sleep()
    clear_screen()


# add note to password
def add_note():
    clear_screen()
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    username = input("Enter username: ")
    note = input("Enter note: ")
    # create table called passwords if it does not exist
    c.execute("CREATE TABLE IF NOT EXISTS passwords (username, password, notes)")
    # add note to password
    c.execute("UPDATE passwords SET notes = ? WHERE username = ?",
            (note, username))
    conn.commit()
    c.close()
    conn.close()
    print(red('Note added'))
    sleep()
    clear_screen()


# clear screen
def clear_screen():
    print('\n' * 100)

# change print color to red


def red(string):
    return '\033[91m' + string + '\033[0m'
# sleep for 2 seconds


def sleep(num=2):
    time.sleep(num)


def delete_database():
    clear_screen()
    choice = input('ARE YOU SURE YOU WANT TO DELETE THE DATABASE? Y or N :')
    if choice == 'Y'.lower():
        conn = sqlite3.connect('passwords.db')
        c = conn.cursor()
        c.execute("DROP TABLE IF EXISTS passwords")
        conn.commit()
        c.close()
        conn.close()
        print(red('Database deleted'))
        sleep()
        clear_screen()


# Add random username and passwords to the database using for loop  (for testing)
def random_passwords():
    clear_screen()
    length = int(input('Enter number of passwords to add to database: '))
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    # create table called passwords if it does not exist
    c.execute("CREATE TABLE IF NOT EXISTS passwords (username, password, notes)")
    for i in range(length):
        #create a random word and assign it to variable
        random_user = ''.join(random.choice(s.ascii_letters)
                            for i in range(random.randint(5, 10)))
        # get random password with letters and numbers
        random_pas = ''.join(random.choice(
            s.ascii_letters + s.digits) for i in range(random.randint(15, 25)))
        user = random_user
        pas = random_pas
        note = 'Empty note'
        c.execute("INSERT INTO passwords VALUES (?, ?, ?)", (user, pas, note))
    conn.commit()
    c.close()
    conn.close()
    print(red('Random passwords added to database'))
    sleep()
    clear_screen()


def delete_password():
    clear_screen()
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    username = input("Enter username: ")
    try:
        c.execute("DELETE FROM passwords WHERE username = ?", (username,))
        conn.commit()
        print(red('Password deleted'))
    except:
        print(red('\nError deleting password'))
    c.close()
    conn.close()
    sleep()
    clear_screen()

# Display all passwords in alphabetical order by username


def show_passwords():
    clear_screen()
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    print("Displaying passwords...\n")
    print('Username      Passwords       Notes')
    # Display passwords in alpha numerical order if table passwords exist in database
    # if table passwords does not exist, create table passwords
    create_database()
    # Display passwords in alpha numerical order
    c.execute("SELECT * FROM passwords ORDER BY username")
    for i, row in enumerate(c.fetchall()):
        print(f'{i + 1}: {row}')
    c.close()
    conn.close()
    sleep()

# create database
def create_database():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS passwords (username, password, notes)")
    conn.commit()
    c.close()
    conn.close()


# Find all username and passwords that start with the inputted letter
def find_password():
    clear_screen()
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    name = input("Search for: ")
    clear_screen()
    # create table called passwords if it does not exist
    create_database()
    print(red('Found passwords:'))
    # Search username or password for word
    c.execute("SELECT * FROM passwords WHERE username LIKE ? OR notes LIKE ?",
            ('%' + name + '%', '%' + name + '%'))
    for row in c.fetchall():
        print(row)
    c.close()
    conn.close()
    sleep()


# link username to password
def link_account():
    clear_screen()
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    user = input("Enter username: ")
    pas = input("Enter password: ")
    # create table called passwords if it does not exist
    create_database()
    c.execute("INSERT INTO passwords VALUES (?, ?, ?)",
            (user, pas, 'Empty note'))
    conn.commit()
    c.close()
    conn.close()
    print(red('\nPassword added to database'))
    sleep()
    clear_screen()

# create tests for password manager
def test():
    clear_screen()
    print(red('\nTesting...\n'))
    # test add password
    link_account()
    # test find password by name
    find_password()
    # test display passwords
    show_passwords()
    # test delete password
    delete_password()
    # test add random passwords
    random_passwords()
    # test delete database
    delete_database()
    clear_screen()




