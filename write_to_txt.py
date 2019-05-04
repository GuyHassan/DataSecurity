
def write_to_file(string):
    '''
    this method get string and print it to a file
    u need to see the location of the txt file
    :param string: a string to print to file
    :return: a txt file with the string
    '''
    if string != None:
        with open('user_pass.txt','w') as user_pass_file:
            user_pass_file.write(string)