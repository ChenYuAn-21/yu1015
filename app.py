from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    # 模擬假資料
    total_assets = 1000000
    roi = 8.5
    records = [
        {"date": "2025-10-01", "item": "台積電", "category": "股票", "amount": 50000},
        {"date": "2025-10-05", "item": "元大高股息", "category": "基金", "amount": 20000},
        {"date": "2025-10-10", "item": "現金存入", "category": "現金", "amount": 30000}
    ]
    return render_template("index.html", total_assets=total_assets, roi=roi, records=records)

if __name__ == "__main__":
    app.run(debug=True)

