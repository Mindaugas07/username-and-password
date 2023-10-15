# Create a program witch takes 5 different (minmum)  variables containing strings for username and password.
# The string should look like : "username='', password=''; username='',password='';....etc"
# Start Endless loop allowing to enter username and password and 
# check if credentials are correct stop endless loop and print greeting message, otherwise print 'wrong credentials'
# and ask to enter password and username again. The program should show numbers of times you tried to enter both credentials.

#    username="algirdas", password="fffff"; username="Vytautas", password="45645ertwe"      ;      "username='', password=''; username='', password=''; username='', password=''"

usernames = input("Please write at least five username and password combinations in a format username='', password=''....etc ")
usernames_list = usernames.split("; ")

usernames_dict = {}
for combination in usernames_list:
    splited_combination = combination.split(",")
    username = splited_combination[0].strip("username=")
    password = splited_combination[1].strip(" password=")
    usernames_dict[username] = password

full_dict = {key.replace('"', ''):val.replace('"', '') for key, val in usernames_dict.items()}    

while True:
    user_input = input("Enter your username and password: ")
    user_pass_list = user_input.split(" ")
    username_entered = user_pass_list[0]
    print(type(username_entered))
    password_entered = user_pass_list[1]
    print(password_entered)
    if username_entered in full_dict and full_dict[username_entered] == password_entered:
        print(f"Correct password, you are now logged in as {username_entered}")
        break
    else:
        break

# print(f"You entered incorect crediantials for username {user_input_name[0] }, enter password and username again")


print(full_dict)