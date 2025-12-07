// products.js: Product listing and details logic

document.addEventListener('DOMContentLoaded', () => {
  let catFilter = document.getElementById('categoryFilter');
  categories.forEach(cat=>{
    let opt=document.createElement('option'); opt.value=cat; opt.text=cat;
    catFilter.appendChild(opt);
  });

  function renderProducts(filteredCat) {
    let prodGrid=document.getElementById('productGrid');
    prodGrid.innerHTML='';
    let filtered = filteredCat === 'all' ? products : products.filter(p=>p.category===filteredCat);
    filtered.forEach(p=>{
      let card=document.createElement('div'); card.className='product-card';
      card.innerHTML = `<div class='product-image'>🍅</div>
        <div class='product-name'>${p.name}</div>
        <div class='product-category'>${p.category}</div>
        <div class='product-price'>₹${p.price}</div>
        <button class='add-cart-btn'>Add to Cart</button>
        <button class='view-details-btn'>View Details</button>`;
      prodGrid.appendChild(card);
    });
  }

  catFilter.addEventListener('change',()=>renderProducts(catFilter.value));
  renderProducts('all');
  getUserGreeting();
  let cart = JSON.parse(localStorage.getItem('cart'))||[];
  document.getElementById('cartBadge').textContent = cart.reduce((s,c)=>s+c.qty,0);
});
