# Create a program witch takes 5 different (minmum)  variables containing strings for username and password.
# The string should look like : "username='', password=''; username='',password='';....etc"
# Start Endless loop allowing to enter username and password and 
# check if credentials are correct stop endless loop and print greeting message, otherwise print 'wrong credentials'
# and ask to enter password and username again. The program should show numbers of times you tried to enter both credentials.

usernames = input("Please write at least five username and password combinations in a format 'username="", password="";'")
usernames_dict = usernames.split(";")








print(usernames_dict)