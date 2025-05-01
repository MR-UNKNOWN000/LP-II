def issafe(arr,x,y,n):
    for row in range(x):
        if arr[row][y] ==1:
            # Checking column attack
            return False
    row = x
    col = y
    #Checking Diagonal Attack
    while row>=0 and col>=0:
        if arr[row][col]==1:
            return False
        row-=1
        col-=1

    row = x
    col = y
    #Checking Anti Diagonal Attack
    while row>=0 and col<n:
        if arr[row][col]==1:
            return False
        row-=1
        col+=1

    return True

def nQueen(arr,x,n):
    if x>=n:
        return True

    for col in range(n):
        if issafe(arr,x,col,n):
            arr[x][col]=1
            if nQueen(arr,x+1,n):
                return True
            arr[x][col] = 0

    return False

def main():
    n = int(input("Enter number of Queens : "))
    arr = [[0]*n for i in range(n)]

    if nQueen(arr,0,n):
        for i in range(n):
            for j in range(n):
                print(arr[i][j],end=" ")
            print()

if __name__ == '__main__':
    main()

'''✅ Title:
N-Queens Problem using Backtracking

✅ Algorithm Steps:
Start with an empty n x n board.

Try to place a queen in each row one by one.

For each cell in the row, check if placing a queen is safe:

No other queen in the same column

No queen in the same left diagonal

No queen in the same right diagonal

If safe, place the queen and recursively try placing the next one.

If placing the next queen fails, backtrack by removing the queen and trying the next cell.

Repeat until all n queens are placed.

✅ Sample Output (For n = 4):
typescript
Copy
Edit
Enter number of Queens : 4
0 1 0 0 
0 0 0 1 
1 0 0 0 
0 0 1 0 
Each 1 represents a queen's position.

✅ Time and Space Complexity:
Time Complexity: O(N!)

Space Complexity: O(N²) (for storing the board)

✅ Short Theory:
The N-Queens problem is a classic backtracking problem where we place N queens on an N x N chessboard so that no two queens threaten each other. A queen can attack horizontally, vertically, and diagonally. The algorithm recursively places queens row by row and backtracks when a conflict occurs.

✅ Features:
Uses backtracking to explore and undo choices.

Guarantees a valid solution if one exists.

Highly recursive but efficient for small N.

✅ Viva Questions & Answers:
Q1: What is the N-Queens problem?
A1: Placing N queens on an N×N chessboard such that no two queens attack each other.

Q2: Which algorithm is used?
A2: Backtracking.

Q3: How does a queen attack?
A3: Horizontally, vertically, and diagonally.

Q4: What is backtracking?
A4: Trying a possibility and undoing it if it doesn’t lead to a solution.

Q5: Time complexity of the N-Queens algorithm?
A5: O(N!) in the worst case.

Q6: How do you check if placing a queen is safe?
A6: Check column, left diagonal, and right diagonal above the current row.

Q7: Can N-Queens be solved using a greedy approach?
A7: No, because it's not optimal for greedy; it requires checking future consequences.

Q8: What is the base case in your recursion?
A8: When x >= n, it means all queens have been successfully placed.'''