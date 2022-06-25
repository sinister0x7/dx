import sqlite3


def get_sqli_output(form_user_id):
    #Connects the database
    db = sqlite3.connect('webvuldatabase.db')

    temp = ""

    for i in range(0, len(form_user_id)):
        if(int(form_user_id[i].isdigit() == True)):
            temp = temp + str(form_user_id[i])

    # SQL Statement: Used to fetch data from database
    get_user_query = "SELECT user_id, first_name, last_name FROM users WHERE 'user_id' = '"