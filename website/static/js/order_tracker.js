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


//Loop through all dropdown elements
dropdowns.forEach(dropdown => {
  //Get inner elements from each dropdown
  const select = dropdown.querySelector('.select');
  const caret = dropdown.querySelector('.caret');
  const menu = dropdown.querySelector('.dropdown-menu');
  const options = dropdown.querySelectorAll('.dropdown-menu li');
  const selected = dropdown.querySelector('.selected');
  
  /*
    We are using this method in order to have 
    multiple dropdown menus on the page work
  */
  
  //Add a click event to the select element
  select.addEventListener('click', () => {
    console.log("clikedd");
    //Add the clicked select styles to the select element
    select.classList.toggle('select-clicked');
    //Add the rotate styles to the caret element
    caret.classList.toggle('caret-rotate');
    //Add the open styles to the menu element
    menu.classList.toggle('menu-open');
  });
  
  //Loop through all option elements
  options.forEach(option => {
    //Add a click event to the option element
    option.addEventListener('click', () => {
      //Change selected inner text to clicked option inner text
      selected.innerText = option.innerText;
      //Add the clicked select styles to the select element
      select.classList.remove('select-clicked');
      //Add the rotate styles to the caret element
      caret.classList.remove('caret-rotate');
      //Add the open styles to the menu element
      menu.classList.remove('menu-open');
      //Remove active class from all option elements
      options.forEach(option => {
        option.classList.remove('active');
      });
      //Add active class to clicked option element
      option.classList.add('active');
    });
  });
});


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
        // console.log("Review submitted");
      },
      error: function(error) {
        console.log(error);
      }
    });
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
