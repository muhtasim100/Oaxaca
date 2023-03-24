// Get the slider container and the right arrow button
const sliderContainer = document.querySelector(".slider-container");
const rightArrow = sliderContainer.querySelector(".slider-arrow-right");

// Get all the images in the slider
const images = sliderContainer.querySelectorAll(".slider img");

// Set the current image index to 0
let currentImageIndex = 0;

// Show the first image
images[currentImageIndex].style.display = "block";

// Add a click event listener to the right arrow button
rightArrow.addEventListener("click", function () {
  nextImage(true);
});


function nextImage(db=false) {
  // Hide the current image
  images[currentImageIndex].style.display = "none";

  // Increment the current image index
  currentImageIndex++;

  // If the current image index is greater than or equal to the number of images, set it back to 0
  if (currentImageIndex >= images.length) {
    currentImageIndex = 0;
  }

  // Show the new current image
  images[currentImageIndex].style.display = "block";

  if (db) {
    $.ajax({
      url: '/update_status',
      type: 'POST',
      data: {id: order_id},
      success: function(data) {
        $(".content").prepend('<div class="notification"><div class="notification-message"></div></div>');
        $(".notification-message").html("Order status changed!");
      },
      error: function(error) {
        console.log(error);
      }
    });
  }
}