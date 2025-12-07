// auth.js: login/signup logic
const USERS_KEY = 'users';

function getUsers() {
  return JSON.parse(localStorage.getItem(USERS_KEY)) || [];
}
function saveUsers(users) {
  localStorage.setItem(USERS_KEY, JSON.stringify(users));
}
function showMessage(msg, isError) {
  const box = document.getElementById('messageBox');
  box.textContent = msg;
  box.style.color = isError ? '#e74c3c':'#28a745';
}
document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('loginForm');
  const signupForm = document.getElementById('signupForm');
  document.getElementById('showSignup').onclick = () => {
    loginForm.style.display = 'none';
    signupForm.style.display = 'block';
  };
  document.getElementById('showLogin').onclick = () => {
    signupForm.style.display = 'none';
    loginForm.style.display = 'block';
  };
  loginForm.onsubmit = function(e) {
    e.preventDefault();
    const email = document.getElementById('loginEmail').value.trim();
    const password = document.getElementById('loginPassword').value.trim();
    const users = getUsers();
    const user = users.find(u=>u.email===email && u.password===password);
    if(user){
      localStorage.setItem('loggedInUser', JSON.stringify(user));
      window.location.href = 'home.html';
    } else {
      showMessage('Invalid credentials',true);
    }
  }
  signupForm.onsubmit = function(e) {
    e.preventDefault();
    const name = document.getElementById('signupName').value.trim();
    const email = document.getElementById('signupEmail').value.trim();
    const phone = document.getElementById('signupPhone').value.trim();
    const password = document.getElementById('signupPassword').value.trim();
    const confirmPassword = document.getElementById('signupConfirmPassword').value.trim();
    if(password.length<8) return showMessage('Password must be at least 8 characters',true);
    if(password!==confirmPassword) return showMessage('Passwords do not match',true);
    if(!/^[0-9]{10}$/.test(phone)) return showMessage('Enter valid 10 digit phone number',true);
    let users = getUsers();
    if(users.some(u=>u.email===email)) return showMessage('Email already exists',true);
    const user = { id: Date.now(), name, email, password, phone, addresses: [], orders: [] };
    users.push(user); saveUsers(users);
    localStorage.setItem('loggedInUser', JSON.stringify(user));
    showMessage('Signup successful! Logging you in...');
    setTimeout(()=>window.location.href = 'home.html',1000);
  }
});
