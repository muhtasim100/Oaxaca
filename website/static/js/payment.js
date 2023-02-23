var modal = document.getElementById("reviewModal");
var pay_btn = document.getElementById("paynow-btn");
var review_btn = document.getElementById("review-btn");

pay_btn.onclick = function () {
    modal.style.display = "block";
}

review_btn.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
