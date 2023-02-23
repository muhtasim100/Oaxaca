var modal = document.getElementById("reviewModal");
var pay_btn = document.getElementById("paynow-btn");
var review_btn = document.getElementById("review-btn");
var stars = Array.from(document.querySelectorAll(".stars img"));
var selectedStar = -1;

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

stars.forEach(function(star) {
    star.addEventListener("mouseover", function() {
        let id = parseInt(star.getAttribute("id")) - 1;
        for (let i = 0; i < stars.length; i++) {
            if (i <= id) {
                stars[i].src = "/static/images/payment/star-full.png";
            } else {
                stars[i].src = "/static/images/payment/star-blank.png";
            }
        }
    });

    star.addEventListener("mouseout", function() {
        for (let i = 0; i < stars.length; i++) {
            if (i <= selectedStar) {
                stars[i].src = "/static/images/payment/star-full.png";
            } else {
                stars[i].src = "/static/images/payment/star-blank.png";
            }
        }
    });

    star.addEventListener("click", function() {
        let id = parseInt(star.getAttribute("id")) - 1
        if (selectedStar == id) {
            selectedStar = -1;
        } else {
            selectedStar = id;
        }
    });
});
