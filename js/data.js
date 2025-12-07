// data.js: Product, category, user, cart, and order demo data

const categories = [
  "Fruits & Vegetables",
  "Dairy & Eggs",
  "Beverages",
  "Snacks & Packaged Foods",
  "Personal Care",
  "Household Items",
  "Bakery & Bread",
  "Meat & Seafood"
];

const products = [
  {id:1,name:"Fresh Bananas",category:"Fruits & Vegetables",price:40,unit:"per dozen",description:"Fresh yellow bananas rich in potassium and vitamins",stock:true,rating:4.5},
  {id:2,name:"Fresh Milk",category:"Dairy & Eggs",price:56,unit:"1 Liter",description:"Pure and fresh full cream milk",stock:true,rating:4.7},
  {id:3,name:"Brown Eggs",category:"Dairy & Eggs",price:72,unit:"12 pieces",description:"Farm fresh brown eggs",stock:true,rating:4.6},
  {id:4,name:"Red Apples",category:"Fruits & Vegetables",price:150,unit:"1 Kg",description:"Crispy and sweet red apples",stock:true,rating:4.8},
  {id:5,name:"Fresh Tomatoes",category:"Fruits & Vegetables",price:35,unit:"1 Kg",description:"Fresh and ripe tomatoes",stock:true,rating:4.3},
  {id:6,name:"Basmati Rice",category:"Snacks & Packaged Foods",price:180,unit:"1 Kg",description:"Premium quality basmati rice",stock:true,rating:4.7},
  {id:7,name:"Orange Juice",category:"Beverages",price:95,unit:"1 Liter",description:"Fresh orange juice with no added sugar",stock:true,rating:4.4},
  {id:8,name:"Coca Cola",category:"Beverages",price:80,unit:"2 Liter",description:"Refreshing cold drink",stock:true,rating:4.5},
  {id:9,name:"Potato Chips",category:"Snacks & Packaged Foods",price:20,unit:"50g",description:"Crispy and tasty potato chips",stock:true,rating:4.2},
  {id:10,name:"Bread",category:"Bakery & Bread",price:35,unit:"400g",description:"Soft and fresh white bread",stock:true,rating:4.6},
  {id:11,name:"Shampoo",category:"Personal Care",price:185,unit:"200ml",description:"Nourishing hair shampoo",stock:true,rating:4.3},
  {id:12,name:"Dish Soap",category:"Household Items",price:95,unit:"500ml",description:"Effective dishwashing liquid",stock:true,rating:4.5},
  {id:13,name:"Chicken Breast",category:"Meat & Seafood",price:280,unit:"500g",description:"Fresh boneless chicken breast",stock:true,rating:4.7},
  {id:14,name:"Green Grapes",category:"Fruits & Vegetables",price:120,unit:"500g",description:"Sweet and seedless green grapes",stock:true,rating:4.6},
  {id:15,name:"Yogurt",category:"Dairy & Eggs",price:45,unit:"400g",description:"Creamy and fresh yogurt",stock:true,rating:4.5},
  {id:16,name:"Cookies",category:"Snacks & Packaged Foods",price:50,unit:"200g",description:"Delicious chocolate chip cookies",stock:true,rating:4.4},
  {id:17,name:"Green Tea",category:"Beverages",price:120,unit:"25 bags",description:"Healthy and refreshing green tea",stock:true,rating:4.6},
  {id:18,name:"Cake",category:"Bakery & Bread",price:250,unit:"500g",description:"Delicious vanilla cake",stock:true,rating:4.7},
  {id:19,name:"Toothpaste",category:"Personal Care",price:85,unit:"150g",description:"Fresh mint toothpaste",stock:true,rating:4.4},
  {id:20,name:"Detergent",category:"Household Items",price:320,unit:"1 Kg",description:"Powerful laundry detergent",stock:true,rating:4.5},
  {id:21,name:"Fresh Fish",category:"Meat & Seafood",price:350,unit:"500g",description:"Fresh sea fish",stock:true,rating:4.6},
  {id:22,name:"Onions",category:"Fruits & Vegetables",price:30,unit:"1 Kg",description:"Fresh red onions",stock:true,rating:4.2},
  {id:23,name:"Butter",category:"Dairy & Eggs",price:52,unit:"100g",description:"Creamy salted butter",stock:true,rating:4.5},
  {id:24,name:"Coffee",category:"Beverages",price:280,unit:"200g",description:"Premium instant coffee",stock:true,rating:4.7},
  {id:25,name:"Peanut Butter",category:"Snacks & Packaged Foods",price:180,unit:"350g",description:"Creamy peanut butter",stock:true,rating:4.6}
];

const deliveryCharge = 50;
const orderStatuses = ["Order Placed","Processing","Shipped","Out for Delivery","Delivered"];

// Users, cart, and orders to be stored in memory via JS code
