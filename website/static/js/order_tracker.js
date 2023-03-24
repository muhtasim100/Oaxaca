let currentIndex = 0;
const images = document.getElementsByClassName("image");
const dropdowns = document.querySelectorAll('.dropdown');

// ----------------------------------------

function nextImage() {
  images[currentIndex].classList.remove("visible");
  images[currentIndex].classList.add("hidden");
  currentIndex = (currentIndex + 1) % images.length;
  images[currentIndex].classList.remove("hidden");
  images[currentIndex].classList.add("visible");
}


// Code for the review modal + submitting reviews

var modal = document.getElementById("reviewModal");
var review_btn = document.getElementById("review-btn");
var review_modal_btn = document.querySelector(".reviewbutton");
var stars = Array.from(document.querySelectorAll(".stars img"));
var selectedStar = -1;

review_modal_btn.onclick = function () {
    // To open review modal
    modal.style.display = "block";
}

review_btn.onclick = function () {
    // submitting review
    $.ajax({
      url: '/review_store',
      type: 'POST',
      data: {stars: selectedStar+1, review: $("#review-text").val()},
      success: function(data) {
        // change this later to show a notification saying the review is submitted
        $(".content").prepend('<div class="notification"><div class="notification-message"></div></div>');
        $(".notification-message").html("Review succesfully submitted!");
      },
      error: function(error) {
        console.log(error);
      }
    });
    modal.style.display = "none";
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
