from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    address = request.form['address']
    note = request.form['note']
    checkbox = request.form.get('checkbox', 'unchecked')
    print("Họ và tên:", name)
    print("Số điện thoại:", phone)
    print("Email:", email)
    print("Ghi chú:", note)
    print("Checkbox:", checkbox)
    if address:
        print("Địa chỉ giao hàng:", address)
    else:
        print("Địa chỉ giao hàng: 150 Bùi Thị Xuân, quận 1, TP. Hồ Chí Minh")

    return 'Đã nhận thông tin!'

if __name__ == '__main__':
    app.run(debug=True)
