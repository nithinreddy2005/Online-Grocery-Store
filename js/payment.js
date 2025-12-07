// payment.js: Cart, payment and order logic

document.addEventListener('DOMContentLoaded', () => {
  // Payment method details toggle logic
  document.querySelectorAll("input[name='paymentMethod']").forEach(el => {
    el.onchange = () => {
      document.getElementById('cardDetails').style.display = el.id==='card'?'block':'none';
      document.getElementById('upiDetails').style.display = el.id==='upi'?'block':'none';
      document.getElementById('netbankingDetails').style.display = el.id==='netbanking'?'block':'none';
    };
  });
  document.getElementById('paymentForm').onsubmit = function(e){
    e.preventDefault();
    // Simulate order placement and confirmation
    document.getElementById("processingModal").style.display = "block";
    setTimeout(()=>{
      document.getElementById("processingModal").style.display = "none";
      window.location.href = 'confirmation.html';
    },1500);
  }
});
