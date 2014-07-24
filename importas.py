#
#
#
'''set of functions that provide different file import methods.
'''
def list_of_chars(filename):
    '''file -> list of chars
    '''
    f = open(filename, 'r')
    file_list = list(f.read())
    f.close()
    return file_list

