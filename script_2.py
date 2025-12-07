
# Generate confirmation.html
confirmation_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order Confirmation - FreshCart Online Grocery</title>
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
        <div class="confirmation-box">
            <div class="success-icon">✓</div>
            <h1>Order Placed Successfully!</h1>
            <p class="success-message">Thank you for your order. Your groceries will be delivered soon.</p>
            
            <div class="order-info">
                <div class="info-row">
                    <strong>Order ID:</strong>
                    <span id="orderId"></span>
                </div>
                <div class="info-row">
                    <strong>Order Date:</strong>
                    <span id="orderDate"></span>
                </div>
                <div class="info-row">
                    <strong>Estimated Delivery:</strong>
                    <span id="deliveryDate"></span>
                </div>
                <div class="info-row">
                    <strong>Total Amount:</strong>
                    <span id="totalAmount"></span>
                </div>
            </div>

            <div class="order-details">
                <h3>Order Items</h3>
                <div id="orderItems"></div>
            </div>

            <div class="confirmation-actions">
                <a href="orders.html" class="btn btn-primary">Track Order</a>
                <a href="products.html" class="btn btn-secondary">Continue Shopping</a>
            </div>
        </div>
    </div>

    <footer class="footer">
        <p>&copy; 2025 FreshCart Online Grocery. All rights reserved.</p>
    </footer>

    <script src="js/data.js"></script>
    <script src="js/common.js"></script>
    <script src="js/confirmation.js"></script>
</body>
</html>"""

# Generate orders.html
orders_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Orders - FreshCart Online Grocery</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-brand">🛒 FreshCart</div>
            <ul class="nav-menu">
                <li><a href="home.html">Home</a></li>
                <li><a href="products.html">Products</a></li>
                <li><a href="orders.html" class="active">My Orders</a></li>
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
        <h1>My Orders</h1>

        <div id="noOrders" class="empty-state" style="display: none;">
            <h2>No orders yet</h2>
            <p>Start shopping to place your first order!</p>
            <a href="products.html" class="btn btn-primary">Start Shopping</a>
        </div>

        <div id="ordersList" class="orders-list">
            <!-- Orders will be loaded here -->
        </div>
    </div>

    <!-- Order Details Modal -->
    <div id="orderModal" class="modal">
        <div class="modal-content modal-large">
            <span class="close">&times;</span>
            <div id="orderDetail">
                <!-- Order details will be loaded here -->
            </div>
        </div>
    </div>

    <footer class="footer">
        <p>&copy; 2025 FreshCart Online Grocery. All rights reserved.</p>
    </footer>

    <script src="js/data.js"></script>
    <script src="js/common.js"></script>
    <script src="js/orders.js"></script>
</body>
</html>"""

# Generate profile.html
profile_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile - FreshCart Online Grocery</title>
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
                <li><a href="profile.html" class="active">Profile</a></li>
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
        <h1>My Profile</h1>

        <div class="profile-layout">
            <div class="profile-section">
                <h2>Personal Information</h2>
                <div id="profileView" class="profile-view">
                    <div class="profile-field">
                        <strong>Name:</strong>
                        <span id="profileName"></span>
                    </div>
                    <div class="profile-field">
                        <strong>Email:</strong>
                        <span id="profileEmail"></span>
                    </div>
                    <div class="profile-field">
                        <strong>Phone:</strong>
                        <span id="profilePhone"></span>
                    </div>
                    <button class="btn btn-primary" id="editProfileBtn">Edit Profile</button>
                </div>

                <form id="profileEditForm" class="profile-edit-form" style="display: none;">
                    <div class="form-group">
                        <label for="editName">Full Name</label>
                        <input type="text" id="editName" required>
                    </div>
                    <div class="form-group">
                        <label for="editEmail">Email</label>
                        <input type="email" id="editEmail" required>
                    </div>
                    <div class="form-group">
                        <label for="editPhone">Phone</label>
                        <input type="tel" id="editPhone" pattern="[0-9]{10}" required>
                    </div>
                    <div class="form-actions">
                        <button type="submit" class="btn btn-primary">Save Changes</button>
                        <button type="button" class="btn btn-secondary" id="cancelEditBtn">Cancel</button>
                    </div>
                </form>
            </div>

            <div class="profile-section">
                <h2>Change Password</h2>
                <form id="passwordForm">
                    <div class="form-group">
                        <label for="currentPassword">Current Password</label>
                        <input type="password" id="currentPassword" required>
                    </div>
                    <div class="form-group">
                        <label for="newPassword">New Password</label>
                        <input type="password" id="newPassword" minlength="8" required>
                    </div>
                    <div class="form-group">
                        <label for="confirmPassword">Confirm New Password</label>
                        <input type="password" id="confirmPassword" required>
                    </div>
                    <button type="submit" class="btn btn-primary">Update Password</button>
                </form>
            </div>

            <div class="profile-section">
                <h2>Saved Addresses</h2>
                <div id="savedAddressesList">
                    <!-- Saved addresses will be displayed here -->
                </div>
                <p id="noAddresses" style="display: none;">No saved addresses</p>
            </div>

            <div class="profile-section">
                <h2>Order Statistics</h2>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-value" id="totalOrders">0</div>
                        <div class="stat-label">Total Orders</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-value" id="totalSpent">₹0</div>
                        <div class="stat-label">Total Spent</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div id="messageBox" class="message-box"></div>

    <footer class="footer">
        <p>&copy; 2025 FreshCart Online Grocery. All rights reserved.</p>
    </footer>

    <script src="js/data.js"></script>
    <script src="js/common.js"></script>
    <script src="js/profile.js"></script>
</body>
</html>"""

# Save remaining HTML files
with open("online-grocery-system/confirmation.html", "w", encoding="utf-8") as f:
    f.write(confirmation_html)

with open("online-grocery-system/orders.html", "w", encoding="utf-8") as f:
    f.write(orders_html)

with open("online-grocery-system/profile.html", "w", encoding="utf-8") as f:
    f.write(profile_html)

print("HTML files created: confirmation.html, orders.html, profile.html")
print("\nAll HTML pages generated successfully!")
