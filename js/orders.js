// orders.js: Order list logic (demo)
document.addEventListener('DOMContentLoaded',()=>{
  let orders = [{orderId:'ORD10190',date:'2025-10-29',status:'Delivered',total:620,count:7},{orderId:'ORD11221',date:'2025-10-18',status:'Processing',total:390,count:3}];
  let ordersList = document.getElementById('ordersList');
  if(!orders.length){
    document.getElementById('noOrders').style.display='block';
    return;
  }
  orders.forEach(o=>{
    let div=document.createElement('div');
    div.className='order-card';
    div.innerHTML = `<div><strong>Order ID:</strong> ${o.orderId}</div>
      <div><strong>Date:</strong> ${o.date}</div>
      <div><strong>Status:</strong> <span class='order-status'>${o.status}</span></div>
      <div><strong>Items:</strong> ${o.count}</div>
      <div><strong>Total:</strong> ₹${o.total}</div>
      <button class='btn btn-secondary'>View Details</button>`;
    ordersList.appendChild(div);
  });
});
