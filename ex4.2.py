def make_ruler(length):
    h_line, nums, res = '|', '', ''
    for i in range(length):
        h_line += '....|'
        
    for i in range(length + 1):
        nums += str(i) + '    '
    res = (h_line + '\n' + nums + '\n') 
    return res

def create_matrix(length, width):
    h_line, v_line, square = '+', '|', ''
    for i in range(width):
        h_line += '---+'
        v_line += '   |'

    square += (h_line + '\n' + v_line + '\n') * \
              length + h_line
    return square

print(create_matrix(7, 5))
 
print('\n')

print(make_ruler(10))
