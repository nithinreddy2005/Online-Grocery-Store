// common.js: shared utilities for online grocery app
function logoutUser() {  
  localStorage.removeItem('loggedInUser');
  localStorage.removeItem('cart');
  window.location.href = 'index.html';
}

function getUserGreeting() {
  const user = JSON.parse(localStorage.getItem('loggedInUser')) || {};
  document.querySelectorAll('#userGreeting').forEach(g=>g.textContent = `Welcome, ${user.name||'Guest'}!`);
}

document.addEventListener('DOMContentLoaded', ()=>{
  if (document.getElementById('logoutBtn')) {
    document.getElementById('logoutBtn').addEventListener('click', logoutUser);
  }
  getUserGreeting();
});
