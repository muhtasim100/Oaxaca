function togglePassword() {
    var x = document.getElementById("password");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
}

const passwordInput = document.getElementById("password");
passwordInput.addEventListener("keypress", function(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
    document.querySelector("#login-btn").click();
  }
});
