matrix = [ [1,2,3],[4,5,6],[7,8,9] ] 
def matrix_maker(list): 
  for x in list:
    for y in x:
      print(y, end = ' ')
    print()
    

    
matrix_maker(matrix)