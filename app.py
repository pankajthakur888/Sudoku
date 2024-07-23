from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample Sudoku board (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

@app.route('/')
def index():
    return render_template('sudoku.html', board=board)

@app.route('/update', methods=['POST'])
def update():
    global board
    for i in range(9):
        for j in range(9):
            val = request.form.get(f'cell-{i}-{j}')
            if val:
                board[i][j] = int(val)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
