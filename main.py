# Create a program witch takes 5 different (minmum)  variables containing strings for username and password.
# The string should look like : "username='', password=''; username='',password='';....etc"
# Start Endless loop allowing to enter username and password and 
# check if credentials are correct stop endless loop and print greeting message, otherwise print 'wrong credentials'
# and ask to enter password and username again. The program should show numbers of times you tried to enter both credentials.

# "username='algirdas', password='fffff'; username='Vytautas', password='45645ertwe'; "username='', password=''; username='', password=''; username='', password=''"

usernames = input("Please write at least five username and password combinations in a format 'username="", password="";'")
usernames_list = usernames.split("; ")
print(usernames_list)
usernames_dict = {}
for combination in usernames_list:
    splited_combination = combination.split(", ")
    print(splited_combination)
    username = splited_combination[0].strip("username=")
    print(username)
    password = splited_combination[1].strip("password=")
    print(password)
    usernames_dict[username] = password
    # username_dict[]

while True:
    user_input = input("Enter your username and password: ")
    if len(user_input) != 0:
        break
user_input_name = user_input.split(" ")
print(f"You entered incorect crediantials for username {user_input_name[0] }, enter password and username again")








print(usernames_dict)