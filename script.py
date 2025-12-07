
import os
import zipfile
from datetime import datetime

# Create directory structure
os.makedirs("online-grocery-system", exist_ok=True)
os.makedirs("online-grocery-system/css", exist_ok=True)
os.makedirs("online-grocery-system/js", exist_ok=True)
os.makedirs("online-grocery-system/images", exist_ok=True)

# Generate index.html (Login/Signup Page)
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - FreshCart Online Grocery</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body class="auth-page">
    <div class="auth-container">
        <div class="auth-card">
            <div class="auth-header">
                <h1>🛒 FreshCart</h1>
                <p>Your Online Grocery Store</p>
            </div>

            <!-- Login Form -->
            <form id="loginForm" class="auth-form">
                <h2>Login</h2>
                <div class="form-group">
                    <label for="loginEmail">Email Address</label>
                    <input type="email" id="loginEmail" required>
                </div>
                <div class="form-group">
                    <label for="loginPassword">Password</label>
                    <input type="password" id="loginPassword" required>
                </div>
                <button type="submit" class="btn btn-primary">Login</button>
                <p class="toggle-form">Don't have an account? <a href="#" id="showSignup">Sign Up</a></p>
            </form>

            <!-- Signup Form -->
            <form id="signupForm" class="auth-form" style="display: none;">
                <h2>Sign Up</h2>
                <div class="form-group">
                    <label for="signupName">Full Name</label>
                    <input type="text" id="signupName" required>
                </div>
                <div class="form-group">
                    <label for="signupEmail">Email Address</label>
                    <input type="email" id="signupEmail" required>
                </div>
                <div class="form-group">
                    <label for="signupPhone">Phone Number</label>
                    <input type="tel" id="signupPhone" pattern="[0-9]{10}" required>
                </div>
                <div class="form-group">
                    <label for="signupPassword">Password</label>
                    <input type="password" id="signupPassword" minlength="8" required>
                </div>
                <div class="form-group">
                    <label for="signupConfirmPassword">Confirm Password</label>
                    <input type="password" id="signupConfirmPassword" required>
                </div>
                <button type="submit" class="btn btn-primary">Sign Up</button>
                <p class="toggle-form">Already have an account? <a href="#" id="showLogin">Login</a></p>
            </form>

            <div id="messageBox" class="message-box"></div>
        </div>
    </div>

    <script src="js/auth.js"></script>
</body>
</html>"""

# Generate home.html
home_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - FreshCart Online Grocery</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-brand">🛒 FreshCart</div>
            <ul class="nav-menu" id="navMenu">
                <li><a href="home.html" class="active">Home</a></li>
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

    <div class="hero-section">
        <div class="hero-content">
            <h1>Shop Fresh Groceries Online</h1>
            <p>Get fresh groceries delivered to your doorstep</p>
            <a href="products.html" class="btn btn-primary btn-large">Start Shopping</a>
        </div>
    </div>

    <div class="container">
        <section class="categories-section">
            <h2>Shop by Category</h2>
            <div class="category-grid" id="categoryGrid">
                <!-- Categories will be loaded by JavaScript -->
            </div>
        </section>

        <section class="products-section">
            <h2>Featured Products</h2>
            <div class="product-grid" id="featuredProducts">
                <!-- Products will be loaded by JavaScript -->
            </div>
        </section>
    </div>

    <footer class="footer">
        <p>&copy; 2025 FreshCart Online Grocery. All rights reserved.</p>
    </footer>

    <script src="js/data.js"></script>
    <script src="js/common.js"></script>
    <script src="js/home.js"></script>
</body>
</html>"""

# Generate products.html
products_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Products - FreshCart Online Grocery</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-brand">🛒 FreshCart</div>
            <ul class="nav-menu">
                <li><a href="home.html">Home</a></li>
                <li><a href="products.html" class="active">Products</a></li>
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
        <div class="page-header">
            <h1>Our Products</h1>
            <div class="filters">
                <select id="categoryFilter" class="filter-select">
                    <option value="all">All Categories</option>
                </select>
            </div>
        </div>

        <div class="product-grid" id="productGrid">
            <!-- Products will be loaded by JavaScript -->
        </div>
    </div>

    <!-- Product Detail Modal -->
    <div id="productModal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <div id="productDetail">
                <!-- Product details will be loaded here -->
            </div>
        </div>
    </div>

    <footer class="footer">
        <p>&copy; 2025 FreshCart Online Grocery. All rights reserved.</p>
    </footer>

    <script src="js/data.js"></script>
    <script src="js/common.js"></script>
    <script src="js/products.js"></script>
</body>
</html>"""

# Save HTML files
with open("online-grocery-system/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

with open("online-grocery-system/home.html", "w", encoding="utf-8") as f:
    f.write(home_html)

with open("online-grocery-system/products.html", "w", encoding="utf-8") as f:
    f.write(products_html)

print("HTML files created: index.html, home.html, products.html")
