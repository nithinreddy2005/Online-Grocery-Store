// confirmation.js: Confirmation page population

document.addEventListener('DOMContentLoaded', () => {
  // Populate order details for demo (simulate what a real app would pull)
  // Fill IDs: orderId, orderDate, deliveryDate, totalAmount, orderItems
  document.getElementById('orderId').textContent = 'ORD' + Math.floor(Math.random()*89999+10000);
  document.getElementById('orderDate').textContent = new Date().toLocaleDateString();
  let eta = new Date();
  eta.setDate(eta.getDate() + 3);
  document.getElementById('deliveryDate').textContent = eta.toLocaleDateString();
  document.getElementById('totalAmount').textContent = '₹' + (500 + Math.floor(Math.random()*500));
  let orderItems = document.getElementById('orderItems');
  orderItems.innerHTML = `<ul><li>Products will be shown here in a real app</li></ul>`;
});
