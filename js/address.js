// address.js: Address management logic

document.addEventListener('DOMContentLoaded', () => {
  // List saved addresses and add new address form logic
  const addrForm = document.getElementById('addressForm');
  addrForm.onsubmit = function(e){
    e.preventDefault();
    // Gather address fields
    const fullName = document.getElementById('fullName').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const line1 = document.getElementById('addressLine1').value.trim();
    const line2 = document.getElementById('addressLine2').value.trim();
    const city = document.getElementById('city').value.trim();
    const state = document.getElementById('state').value.trim();
    const pincode = document.getElementById('pincode').value.trim();
    const addressType = document.querySelector('input[name="addressType"]:checked').value;
    // Validate required fields
    if(!fullName||!phone||!line1||!city||!state||!/^[0-9]{6}$/.test(pincode)){
      alert('Please fill all required fields with valid data');
      return;
    }
    // Save address in localStorage (simulating backend)
    let user = JSON.parse(localStorage.getItem('loggedInUser'));
    const addrObj = {fullName, phone, line1, line2, city, state, pincode, addressType};
    user.addresses = user.addresses || [];
    user.addresses.push(addrObj);
    localStorage.setItem('loggedInUser',JSON.stringify(user));
    window.location.href = 'payment.html';
  };
});
