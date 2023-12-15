from flask import Flask
from flask import Blueprint, render_template, request, redirect, url_for,flash
import random
app = Flask(__name__)
app.secret_key = 'your-secret-key'

products = [
    {
        'id': 1,
        'name': 'Private Jet',
        'description': 'Le paaoge ??',
        'price': 111123456777777777,
        'image': '/static/image/product_image.jpg'
    },
    {
        'id': 2,
        'name': 'Ferrari',
        'description': 'Dream car',
        'price': 1234567,
        'image': '/static/image/product_image2.jpg'
    },
    {
        'id': 3,
        'name': 'Cruise',
        'description': 'Plan your vacation here',
        'price': 19.99,
        'image': '/static/image/product_image3.jpg'
    },
    {
        'id': 4,
        'name': 'Private Jet',
        'description': 'Le paaoge ??',
        'price': 111123456777777777,
        'image': '/static/image/product_image.jpg'
    },
    {
        'id': 5,
        'name': 'Ferrari',
        'description': 'Dream car',
        'price': 1234567,
        'image': '/static/image/product_image2.jpg'
    },
    {
        'id': 6,
        'name': 'Cruise',
        'description': 'Plan your vacation here',
        'price': 19.99,
        'image': '/static/image/product_image3.jpg'
    },
]
cart_items = [
    
]

# Calculate the total cart value
cart_total = sum(item['price'] * item['quantity'] for item in cart_items)
# Initialize the cart as an empty list



@app.route('/login', methods=['POST', 'GET'])
def login():
     return render_template('login.html')
    

@app.route('/authenticate', methods=['POST', 'GET'])
def authenticate():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        print(username)
        print(password)
        # Verify the username and password (you can implement your own logic here)
        if username == 'username@1' and password == '1234':
            # Generate a random 6-digit OTP
            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            email = 'recipient@example.com'  # Replace with the recipient's email address

            # Send the OTP via email
            # send_otp_email(email, otp)
            flash('OTP sent via email. Check your inbox.')
            # session['otp'] = otp

            # Redirect to the OTP verification page
            return redirect("/verify_otp")
        else:
            flash('Login failed. Check your username and password.')
            redirect('/login') 

    return render_template('login.html')
def send_otp_email(email, otp):
    msg = Message('Your OTP for Verification', recipients=[email])
    msg.body = f'Your OTP is: {otp}'
    mail.send(msg)


@app.route('/signup', methods=['GET', 'POST'])
def signUp():
    # Registration logic here
    return render_template('login.html')

@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    # Registration logic here
    return render_template('verify_otp.html')


@app.route('/forgotpassword', methods=['GET', 'POST'])
def forgotPassword():
    # Registration logic here
    return render_template('forgotPassword.html')


@app.route('/product_page')
def product_page():
    return render_template('product_page.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    else:
        print()
        return 'Product not found'

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart_items.append(product)
    return redirect('/')

@app.route('/cart')
def cart():
    return render_template('cart.html', cart_items=cart_items, cart_total=cart_total)
if __name__ == '__main__':
    app.run(debug=True)
