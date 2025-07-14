from flask import Flask, render_template, request

app = Flask(__name__)

# Store all expenses in a list
expenses = []

@app.route('/')
def index():
    total = sum([e['amount'] for e in expenses])
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/submit', methods=['GET'])
def submit():
    expense_name = request.args.get('expense_name')
    expense_amt = request.args.get('expense_amt')

    if expense_name and expense_amt:
        try:
            expense_amt = float(expense_amt)
            expenses.append({'name': expense_name, 'amount': expense_amt})
        except ValueError:
            return "Amount must be a number."

    # Redirect back to home to show updated list and total
    total = sum([e['amount'] for e in expenses])
    return render_template('index.html', expenses=expenses, total=total)

if __name__ == '__main__':
    app.run(debug=True)