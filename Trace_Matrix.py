def trace_of_matrix(order,matrix):
    trace=0
    for i in range(order):
        trace += matrix[i][i]
    return trace
        
NUM_ROWS = 25
NUM_COLS = 25

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)
 

    
print(trace_of_matrix(NUM_ROWS,my_matrix))