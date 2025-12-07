// cart.js: Shopping cart page logic

document.addEventListener('DOMContentLoaded', () => {
  let cart = JSON.parse(localStorage.getItem('cart'))||[];
  let cartItems = document.getElementById('cartItems'), subtotal=0;
  cartItems.innerHTML = '';
  if(!cart.length){
    document.getElementById('emptyCart').style.display='block';
    document.getElementById('cartContent').style.display='none';
    return;
  }
  document.getElementById('emptyCart').style.display='none';
  document.getElementById('cartContent').style.display='flex';
  cart.forEach(item => {
    subtotal += item.product.price * item.qty;
    let div=document.createElement('div');
    div.className='cart-item';
    div.innerHTML = `<div class='cart-item-image'>🍔</div>
      <div class='cart-item-info'>${item.product.name}<br>₹${item.product.price} x ${item.qty}</div>`;
    cartItems.appendChild(div);
  });
  document.getElementById('subtotal').textContent = `₹${subtotal}`;
  document.getElementById('deliveryCharge').textContent = '₹50';
  document.getElementById('total').textContent = `₹${subtotal+50}`;
  document.getElementById('cartBadge').textContent = cart.reduce((s,c)=>s+c.qty,0);
  document.getElementById('checkoutBtn').onclick = () => window.location.href = 'address.html';
});
