from flask import Flask, render_template, request, redirect, url_for
from datetime import date

app = Flask(__name__)

# 模擬資料庫
records = [
    {"date": "2025-10-01", "item": "午餐", "category": "飲食", "amount": 120},
    {"date": "2025-10-02", "item": "股票買入", "category": "投資", "amount": 5000},
]

def calculate_roi(records):
    investment_records = [r for r in records if r['category'] == '投資']
    if not investment_records:
        return 0
    total_invested = sum(r['amount'] for r in investment_records)
    total_return = total_invested * 0.1  # 假設報酬率 10%
    roi = (total_return / total_invested) * 100
    return round(roi, 2)

@app.route('/')
def dashboard():
    total_assets = sum(r['amount'] for r in records)
    roi = calculate_roi(records)
    return render_template("render.html", total_assets=total_assets, roi=roi, records=records)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    date_str = request.form.get('date')
    item = request.form.get('item')
    category = request.form.get('category')
    amount = request.form.get('amount')
    try:
        amount = float(amount)
    except:
        amount = 0
    if date_str and item and category:
        records.append({
            "date": date_str,
            "item": item,
            "category": category,
            "amount": amount
        })
    return redirect(url_for('dashboard'))

@app.route('/post/<int:index>')
def post_detail(index):
    record = records[index]
    return render_template("post.html", record=record)

if __name__ == "__main__":
    app.run(debug=True)

