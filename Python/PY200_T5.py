#Description: TaskPY200_T5: Chessboard with Numbers Input: N Print an N x N grid: 
# • If (row+col) is even → print 1 
# • else → print 0 
# But if row == col → print X instead.

def print_chessboard(n):
    for row in range(n):
        row_output = []
        for col in range(n):
            if row == col:
                row_output.append('X')
            elif (row + col) % 2 == 0:
                row_output.append('1')
            else:
                row_output.append('0')
        print(' '.join(row_output))


n = int(input("Enter n for dimensions of grid : "))
print(f"\n *** {n} X {n} Chessboard : ***")
print_chessboard(n)