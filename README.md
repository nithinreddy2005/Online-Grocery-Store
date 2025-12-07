# 🛒 Online Grocery Store

A modern, responsive web-based e-commerce platform for online grocery shopping. This full-stack application enables users to browse products, manage shopping carts, and complete purchases with a seamless user experience.

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [Frontend Pages](#frontend-pages)
- [Backend Functionality](#backend-functionality)
- [Data & Categories](#data--categories)
- [Color Scheme & Design](#color-scheme--design)
- [API Integration](#api-integration)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

### User Management
- **User Authentication**: Secure signup and login system
- **User Profiles**: Manage personal information, addresses, and preferences
- **Account Security**: Password protection and session management

### Shopping Experience
- **Product Catalog**: Browse 25+ fresh grocery items across 8 categories
- **Search & Filter**: Filter products by category and search functionality
- **Product Details**: View product descriptions, pricing, units, and ratings
- **Shopping Cart**: Add/remove items, update quantities with real-time total calculation
- **Wishlist Support**: Save favorite products for later

### Checkout & Payment
- **Multi-step Checkout**: Login → Products → Cart → Address → Payment → Confirmation
- **Address Management**: Save and manage multiple delivery addresses
- **Payment Processing**: Secure payment gateway integration
- **Order Confirmation**: Order ID generation and confirmation details
- **Delivery Charges**: Automatic delivery cost calculation (₹50 base charge)

### Order Management
- **Order Tracking**: View order status with real-time updates
- **Order History**: Complete purchase history with order details
- **Order Statuses**: Order Placed → Processing → Shipped → Out for Delivery → Delivered

### Product Categories
- Fruits & Vegetables
- Dairy & Eggs
- Beverages
- Snacks & Packaged Foods
- Personal Care
- Household Items
- Bakery & Bread
- Meat & Seafood

---

## 💻 Tech Stack

### Frontend
- **HTML5**: Semantic markup structure
- **CSS3**: Modern responsive design with CSS Grid and Flexbox
- **JavaScript (ES6+)**: Client-side interactivity and state management
- **Color Tokens**: Advanced design system with CSS variables
- **Responsive Design**: Mobile-first approach with media queries

### Backend
- **Python**: Server-side logic and data processing
- **Flask/FastAPI**: Web framework (if applicable)
- **Session Management**: In-memory data storage

### Additional Tools
- **Git**: Version control
- **Browser DevTools**: Testing and debugging
- **Responsive Design Testing**: Cross-browser compatibility

---

## 📁 Project Structure

```
online-grocery-system/
├── index.html              # Login/Signup page (entry point)
├── home.html              # Home page with hero section
├── products.html          # Product listing and filtering
├── cart.html              # Shopping cart management
├── address.html           # Delivery address management
├── payment.html           # Payment processing page
├── confirmation.html      # Order confirmation page
├── orders.html            # Order history and tracking
├── profile.html           # User profile management
│
├── style.css              # Global styles and design system
│
├── js/
│   ├── auth.js            # Authentication logic
│   ├── data.js            # Product catalog and category data
│   ├── common.js          # Shared utility functions
│   ├── home.js            # Home page functionality
│   ├── products.js        # Product filtering and display
│   ├── cart.js            # Cart operations and calculations
│   ├── address.js         # Address management
│   ├── payment.js         # Payment processing
│   ├── confirmation.js    # Order confirmation logic
│   ├── orders.js          # Order tracking functionality
│   └── profile.js         # Profile management
│
└── python/
    ├── script.py          # Main backend server
    ├── script_1.py        # Database operations
    ├── script_2.py        # API endpoints
    ├── script_3.py        # Payment processing
    └── script_4.py        # Email/notification service
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Node.js (optional, for local server)
- Git (optional, for version control)

### Step 1: Clone or Download the Repository
```bash
git clone <repository-url>
cd online-grocery-system
```

### Step 2: Setup Backend (Python)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies (if requirements.txt exists)
pip install -r requirements.txt

# Run the backend server
python script.py
```

### Step 3: Run Frontend (HTML/CSS/JS)
Open `index.html` in your web browser or use a local server:

```bash
# Using Python 3
python -m http.server 8000

# Using Node.js (if installed)
npx http-server
```

Then navigate to `http://localhost:8000` in your browser.

### Step 4: Database Setup (if applicable)
```bash
# Initialize database
python script_1.py
```

---

## 📖 Usage Guide

### 1. **User Registration & Login**
   - Open the application and go to the signup page
   - Enter email, password, and basic information
   - Create an account or login with existing credentials
   - Session is maintained throughout the shopping experience

### 2. **Browsing Products**
   - Navigate to the Products page
   - Use category filters to narrow down items
   - Click on product cards to view details (description, price, ratings)
   - Products are organized by 8 major categories

### 3. **Managing Shopping Cart**
   - Click "Add to Cart" on product cards
   - View cart summary (total items, subtotal)
   - Update quantities or remove items
   - Cart persists during the session

### 4. **Checkout Process**
   - Click "Proceed to Checkout"
   - **Step 1**: Verify login credentials
   - **Step 2**: Review selected products
   - **Step 3**: Add or select delivery address
   - **Step 4**: Choose payment method and complete payment
   - **Step 5**: View order confirmation with Order ID

### 5. **Order Tracking**
   - Go to "My Orders" section
   - View order history with dates and statuses
   - Track delivery status in real-time
   - View order details (items, pricing, delivery address)

### 6. **Profile Management**
   - Access profile from navigation menu
   - Update personal information
   - Manage saved addresses
   - View account preferences

---

## 🎨 Frontend Pages

| Page | Route | Purpose |
|------|-------|---------|
| **Login/Signup** | `index.html` | User authentication entry point |
| **Home** | `home.html` | Landing page with featured products |
| **Products** | `products.html` | Browse all items with filters |
| **Shopping Cart** | `cart.html` | Review and modify cart items |
| **Address** | `address.html` | Manage delivery addresses |
| **Payment** | `payment.html` | Process payment transactions |
| **Confirmation** | `confirmation.html` | Display order details |
| **Orders** | `orders.html` | View order history & tracking |
| **Profile** | `profile.html` | Manage user account |

---

## 🔧 Backend Functionality

### Data Management (`script_1.py`)
- User account creation and management
- Product inventory tracking
- Order data persistence
- Address storage

### API Endpoints (`script_2.py`)
- `/api/products` - Get all products
- `/api/categories` - Get product categories
- `/api/cart` - Manage shopping cart
- `/api/orders` - Create and retrieve orders
- `/api/users` - User profile management
- `/api/addresses` - Address management

### Payment Processing (`script_3.py`)
- Payment validation
- Transaction logging
- Order creation from cart
- Receipt generation

### Notifications (`script_4.py`)
- Order confirmation emails
- Shipping notifications
- Delivery updates
- Account alerts

---

## 📦 Data & Categories

### Product Categories (8 Total)
1. **Fruits & Vegetables** - Fresh, seasonal produce
2. **Dairy & Eggs** - Milk, cheese, eggs, yogurt
3. **Beverages** - Juices, drinks, tea, coffee
4. **Snacks & Packaged Foods** - Ready-to-eat items
5. **Personal Care** - Shampoo, toothpaste, soaps
6. **Household Items** - Cleaning supplies, detergents
7. **Bakery & Bread** - Fresh bread, cakes, pastries
8. **Meat & Seafood** - Fresh chicken, fish, meat

### Sample Products (25 Items)
- Fresh Bananas (₹40)
- Fresh Milk (₹56)
- Brown Eggs (₹72)
- Red Apples (₹150)
- Basmati Rice (₹180)
- Premium Coffee (₹280)
- And 19 more items...

### Pricing
- Delivery Charge: ₹50 (flat rate)
- GST: Calculated on subtotal (if applicable)
- Price range: ₹20 - ₹350

---

## 🎨 Color Scheme & Design

### Design System Features
- **Modern Color Palette**: Teal primary, cream backgrounds
- **CSS Variables**: 50+ design tokens for consistency
- **Dark Mode Support**: Automatic dark/light mode detection
- **Responsive Grid**: Flexible layouts for all screen sizes
- **Accessibility**: WCAG compliant contrast ratios
- **Typography**: Custom font family with multiple weights
- **Shadows & Spacing**: Professional elevation and spacing

### Key Colors
| Token | Color | Usage |
|-------|-------|-------|
| `--color-primary` | Teal (#208D8D) | CTAs, links, highlights |
| `--color-error` | Red (#C0152F) | Error messages, warnings |
| `--color-success` | Teal (#208D8D) | Success confirmations |
| `--color-background` | Cream (#FCFCF9) | Page backgrounds |

---

## 🔌 API Integration

### Frontend-Backend Communication
- **Fetch API**: AJAX requests for data
- **JSON Format**: Request/response data format
- **Session Storage**: User session management
- **LocalStorage**: Client-side caching

### Sample API Calls
```javascript
// Get all products
fetch('/api/products')
  .then(response => response.json())
  .then(data => displayProducts(data));

// Create order
fetch('/api/orders', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(orderData)
});
```

---

## 🎯 Key Features In Detail

### Real-Time Cart Calculations
- Subtotal computation
- Tax calculations
- Delivery charge addition
- Final total with all costs

### Address Management
- Save multiple addresses
- Set default delivery address
- Edit/delete saved addresses
- Address validation

### Order Status Tracking
- 5-stage order pipeline
- Real-time status updates
- Estimated delivery time
- Customer support integration

### Search & Discovery
- Full-text product search
- Category-based filtering
- Product ratings and reviews
- Related items suggestions

---

## 🚀 Future Enhancements

### Planned Features
- [ ] Advanced search with AI recommendations
- [ ] Customer reviews and ratings system
- [ ] Promotional codes and coupon management
- [ ] Subscription/repeat orders
- [ ] Multiple payment gateway support
- [ ] Real-time inventory management
- [ ] Admin dashboard
- [ ] Analytics and reporting
- [ ] Mobile app (React Native/Flutter)
- [ ] Push notifications
- [ ] Live chat support
- [ ] User referral program

### Performance Improvements
- [ ] Database optimization
- [ ] Caching strategies
- [ ] API rate limiting
- [ ] Load balancing
- [ ] CDN integration

---

## 🤝 Contributing

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Reporting Issues
Please use the GitHub Issues tab to report bugs with:
- Steps to reproduce
- Expected vs actual behavior
- Browser/device information
- Screenshots if applicable

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Design inspiration from modern e-commerce platforms
- Community feedback and contributions
- Open-source libraries and frameworks

---

## 📞 Support

For questions or support:
- Create an issue on GitHub
- Email: support@onlinegrocery.com
- Documentation: [docs/](./docs/)

---

## 📊 Project Statistics

- **Total Files**: 26
- **HTML Pages**: 9
- **JavaScript Files**: 11
- **Python Modules**: 5
- **CSS Files**: 1
- **Product Catalog**: 25 items
- **Categories**: 8
- **Responsive Breakpoints**: Mobile, Tablet, Desktop

---

**Last Updated**: December 2025  
**Version**: 1.0.0  
**Status**: Active Development
