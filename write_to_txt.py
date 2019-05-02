
def write_to_file(string):
    if string != None:
        with open('user_pass.txt','w') as user_pass_file:
            user_pass_file.write(string)