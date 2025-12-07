
# Generate cart.html
cart_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopping Cart - FreshCart Online Grocery</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-brand">🛒 FreshCart</div>
            <ul class="nav-menu">
                <li><a href="home.html">Home</a></li>
                <li><a href="products.html">Products</a></li>
                <li><a href="orders.html">My Orders</a></li>
                <li><a href="profile.html">Profile</a></li>
            </ul>
            <div class="nav-actions">
                <span class="user-greeting" id="userGreeting">Welcome!</span>
                <a href="cart.html" class="cart-icon active">
                    🛒 <span class="cart-badge" id="cartBadge">0</span>
                </a>
                <button class="btn btn-secondary" id="logoutBtn">Logout</button>
            </div>
        </div>
    </nav>

    <div class="container">
        <h1>Shopping Cart</h1>
        
        <div id="emptyCart" class="empty-state" style="display: none;">
            <h2>Your cart is empty</h2>
            <p>Add some products to get started!</p>
            <a href="products.html" class="btn btn-primary">Start Shopping</a>
        </div>

        <div id="cartContent" class="cart-layout">
            <div class="cart-items" id="cartItems">
                <!-- Cart items will be loaded here -->
            </div>

            <div class="cart-summary">
                <h3>Order Summary</h3>
                <div class="summary-row">
                    <span>Subtotal:</span>
                    <span id="subtotal">₹0</span>
                </div>
                <div class="summary-row">
                    <span>Delivery Charges:</span>
                    <span id="deliveryCharge">₹50</span>
                </div>
                <div class="summary-row total">
                    <span>Total:</span>
                    <span id="total">₹0</span>
                </div>
                <a href="products.html" class="btn btn-secondary btn-block">Continue Shopping</a>
                <button id="checkoutBtn" class="btn btn-primary btn-block">Proceed to Checkout</button>
            </div>
        </div>
    </div>

    <footer class="footer">
        <p>&copy; 2025 FreshCart Online Grocery. All rights reserved.</p>
    </footer>

    <script src="js/data.js"></script>
    <script src="js/common.js"></script>
    <script src="js/cart.js"></script>
</body>
</html>"""

# Generate address.html
address_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delivery Address - FreshCart Online Grocery</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-brand">🛒 FreshCart</div>
            <ul class="nav-menu">
                <li><a href="home.html">Home</a></li>
                <li><a href="products.html">Products</a></li>
                <li><a href="orders.html">My Orders</a></li>
                <li><a href="profile.html">Profile</a></li>
            </ul>
            <div class="nav-actions">
                <span class="user-greeting" id="userGreeting">Welcome!</span>
                <a href="cart.html" class="cart-icon">
                    🛒 <span class="cart-badge" id="cartBadge">0</span>
                </a>
                <button class="btn btn-secondary" id="logoutBtn">Logout</button>
            </div>
        </div>
    </nav>

    <div class="container">
        <div class="checkout-steps">
            <div class="step active">1. Address</div>
            <div class="step">2. Payment</div>
            <div class="step">3. Confirmation</div>
        </div>

        <div class="checkout-layout">
            <div class="checkout-main">
                <h2>Delivery Address</h2>

                <div id="savedAddresses" class="saved-addresses">
                    <h3>Saved Addresses</h3>
                    <div id="addressList">
                        <!-- Saved addresses will be displayed here -->
                    </div>
                </div>

                <h3>Add New Address</h3>
                <form id="addressForm" class="address-form">
                    <div class="form-row">
                        <div class="form-group">
                            <label for="fullName">Full Name *</label>
                            <input type="text" id="fullName" required>
                        </div>
                        <div class="form-group">
                            <label for="phone">Phone Number *</label>
                            <input type="tel" id="phone" pattern="[0-9]{10}" required>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="addressLine1">Address Line 1 *</label>
                        <input type="text" id="addressLine1" required>
                    </div>

                    <div class="form-group">
                        <label for="addressLine2">Address Line 2</label>
                        <input type="text" id="addressLine2">
                    </div>

                    <div class="form-row">
                        <div class="form-group">
                            <label for="city">City *</label>
                            <input type="text" id="city" required>
                        </div>
                        <div class="form-group">
                            <label for="state">State *</label>
                            <input type="text" id="state" required>
                        </div>
                        <div class="form-group">
                            <label for="pincode">PIN Code *</label>
                            <input type="text" id="pincode" pattern="[0-9]{6}" required>
                        </div>
                    </div>

                    <div class="form-group">
                        <label>Address Type *</label>
                        <div class="radio-group">
                            <label><input type="radio" name="addressType" value="Home" checked> Home</label>
                            <label><input type="radio" name="addressType" value="Work"> Work</label>
                            <label><input type="radio" name="addressType" value="Other"> Other</label>
                        </div>
                    </div>

                    <div class="form-group">
                        <label>
                            <input type="checkbox" id="saveAddress" checked>
                            Save this address for future orders
                        </label>
                    </div>

                    <button type="submit" class="btn btn-primary btn-large">Continue to Payment</button>
                </form>
            </div>

            <div class="checkout-sidebar">
                <h3>Order Summary</h3>
                <div class="order-items" id="orderItems">
                    <!-- Order items will be displayed here -->
                </div>
                <div class="summary-row">
                    <span>Subtotal:</span>
                    <span id="subtotal">₹0</span>
                </div>
                <div class="summary-row">
                    <span>Delivery:</span>
                    <span>₹50</span>
                </div>
                <div class="summary-row total">
                    <span>Total:</span>
                    <span id="total">₹0</span>
                </div>
            </div>
        </div>
    </div>

    <footer class="footer">
        <p>&copy; 2025 FreshCart Online Grocery. All rights reserved.</p>
    </footer>

    <script src="js/data.js"></script>
    <script src="js/common.js"></script>
    <script src="js/address.js"></script>
</body>
</html>"""

# Generate payment.html
payment_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Payment - FreshCart Online Grocery</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-brand">🛒 FreshCart</div>
            <ul class="nav-menu">
                <li><a href="home.html">Home</a></li>
                <li><a href="products.html">Products</a></li>
                <li><a href="orders.html">My Orders</a></li>
                <li><a href="profile.html">Profile</a></li>
            </ul>
            <div class="nav-actions">
                <span class="user-greeting" id="userGreeting">Welcome!</span>
                <a href="cart.html" class="cart-icon">
                    🛒 <span class="cart-badge" id="cartBadge">0</span>
                </a>
                <button class="btn btn-secondary" id="logoutBtn">Logout</button>
            </div>
        </div>
    </nav>

    <div class="container">
        <div class="checkout-steps">
            <div class="step completed">1. Address</div>
            <div class="step active">2. Payment</div>
            <div class="step">3. Confirmation</div>
        </div>

        <div class="checkout-layout">
            <div class="checkout-main">
                <div class="delivery-address-box">
                    <h3>Delivery Address</h3>
                    <div id="selectedAddress"></div>
                    <a href="address.html" class="btn btn-secondary btn-small">Change Address</a>
                </div>

                <h2>Payment Method</h2>
                <p class="payment-disclaimer">⚠️ This is a demo application. Do not use real payment information.</p>

                <form id="paymentForm">
                    <div class="payment-methods">
                        <div class="payment-option">
                            <input type="radio" id="cod" name="paymentMethod" value="Cash on Delivery" checked>
                            <label for="cod">
                                <strong>Cash on Delivery</strong>
                                <span>Pay when you receive your order</span>
                            </label>
                        </div>

                        <div class="payment-option">
                            <input type="radio" id="card" name="paymentMethod" value="Credit/Debit Card">
                            <label for="card">
                                <strong>Credit/Debit Card</strong>
                                <span>Visa, MasterCard, RuPay</span>
                            </label>
                        </div>

                        <div id="cardDetails" class="payment-details" style="display: none;">
                            <div class="form-group">
                                <label for="cardNumber">Card Number</label>
                                <input type="text" id="cardNumber" pattern="[0-9]{16}" placeholder="1234 5678 9012 3456">
                            </div>
                            <div class="form-group">
                                <label for="cardName">Cardholder Name</label>
                                <input type="text" id="cardName">
                            </div>
                            <div class="form-row">
                                <div class="form-group">
                                    <label for="expiry">Expiry Date</label>
                                    <input type="text" id="expiry" placeholder="MM/YY">
                                </div>
                                <div class="form-group">
                                    <label for="cvv">CVV</label>
                                    <input type="text" id="cvv" pattern="[0-9]{3}" placeholder="123">
                                </div>
                            </div>
                        </div>

                        <div class="payment-option">
                            <input type="radio" id="upi" name="paymentMethod" value="UPI">
                            <label for="upi">
                                <strong>UPI</strong>
                                <span>Google Pay, PhonePe, Paytm</span>
                            </label>
                        </div>

                        <div id="upiDetails" class="payment-details" style="display: none;">
                            <div class="form-group">
                                <label for="upiId">UPI ID</label>
                                <input type="text" id="upiId" placeholder="yourname@upi">
                            </div>
                        </div>

                        <div class="payment-option">
                            <input type="radio" id="netbanking" name="paymentMethod" value="Net Banking">
                            <label for="netbanking">
                                <strong>Net Banking</strong>
                                <span>All major banks</span>
                            </label>
                        </div>

                        <div id="netbankingDetails" class="payment-details" style="display: none;">
                            <div class="form-group">
                                <label for="bankSelect">Select Bank</label>
                                <select id="bankSelect">
                                    <option value="">Choose Bank</option>
                                    <option value="SBI">State Bank of India</option>
                                    <option value="HDFC">HDFC Bank</option>
                                    <option value="ICICI">ICICI Bank</option>
                                    <option value="Axis">Axis Bank</option>
                                    <option value="PNB">Punjab National Bank</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <button type="submit" class="btn btn-primary btn-large" id="placeOrderBtn">Place Order</button>
                </form>
            </div>

            <div class="checkout-sidebar">
                <h3>Order Summary</h3>
                <div class="order-items" id="orderItems">
                    <!-- Order items will be displayed here -->
                </div>
                <div class="summary-row">
                    <span>Subtotal:</span>
                    <span id="subtotal">₹0</span>
                </div>
                <div class="summary-row">
                    <span>Delivery:</span>
                    <span>₹50</span>
                </div>
                <div class="summary-row total">
                    <span>Total:</span>
                    <span id="total">₹0</span>
                </div>
            </div>
        </div>
    </div>

    <div id="processingModal" class="modal" style="display: none;">
        <div class="modal-content processing">
            <div class="loader"></div>
            <h3>Processing your order...</h3>
            <p>Please wait</p>
        </div>
    </div>

    <footer class="footer">
        <p>&copy; 2025 FreshCart Online Grocery. All rights reserved.</p>
    </footer>

    <script src="js/data.js"></script>
    <script src="js/common.js"></script>
    <script src="js/payment.js"></script>
</body>
</html>"""

# Save more HTML files
with open("online-grocery-system/cart.html", "w", encoding="utf-8") as f:
    f.write(cart_html)

with open("online-grocery-system/address.html", "w", encoding="utf-8") as f:
    f.write(address_html)

with open("online-grocery-system/payment.html", "w", encoding="utf-8") as f:
    f.write(payment_html)

print("HTML files created: cart.html, address.html, payment.html")
