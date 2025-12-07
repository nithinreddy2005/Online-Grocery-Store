// profile.js: User profile logic (demo)
document.addEventListener('DOMContentLoaded',()=>{
  let user = {name:'Demo User', email:'demo@demo.com', phone:'9876543210', addresses:[], orders:[]};
  document.getElementById('profileName').textContent=user.name;
  document.getElementById('profileEmail').textContent=user.email;
  document.getElementById('profilePhone').textContent=user.phone;
  document.getElementById('totalOrders').textContent='2';
  document.getElementById('totalSpent').textContent='₹1010';
  document.getElementById('noAddresses').style.display='block';
});
