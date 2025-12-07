// home.js: Home page scripts

document.addEventListener('DOMContentLoaded', () => {
  // Populate categories
  const grid = document.getElementById('categoryGrid');
  categories.forEach(cat => {
    const div = document.createElement('div');
    div.className = 'category-card';
    div.textContent = cat;
    div.onclick = () => { window.location.href = 'products.html?cat=' + encodeURIComponent(cat); };
    grid.appendChild(div);
  });
  // Featured products: first 8 products
  const feat = document.getElementById('featuredProducts');
  products.slice(0,8).forEach(p => {
    let card = document.createElement('div');
    card.className='product-card';
    card.innerHTML = `
      <div class='product-image'>🍎</div>
      <div class='product-name'>${p.name}</div>
      <div class='product-price'>₹${p.price}</div>
      <button class='add-cart-btn'>Add to Cart</button>
      <button class='view-details-btn'>View Details</button>
    `;
    feat.appendChild(card);
  });
  // Greet user and update cart badge
  getUserGreeting();
  const badge = document.getElementById('cartBadge');
  let cart = JSON.parse(localStorage.getItem('cart'))||[];
  badge.textContent = cart.reduce((s,c)=>s+c.qty,0);
})
