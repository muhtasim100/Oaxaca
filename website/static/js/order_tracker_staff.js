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
});


// Loop through all dropdown elements
dropdowns.forEach(dropdown => {
  // Get inner elements from each dropdown
  const select = dropdown.querySelector('.select');
  const caret = dropdown.querySelector('.caret');
  const menu = dropdown.querySelector('.dropdown-menu');
  const options = dropdown.querySelectorAll('.dropdown-menu li');
  const selected = dropdown.querySelector('.selected');

  /*
    We are using this method in order to have
    multiple dropdown menus on the page work
  */

  // Add a click event to the select element
  select.addEventListener('click', () => {
    console.log("clicked");
    // Add the clicked select styles to the select element
    select.classList.toggle('select-clicked');
    // Add the rotate styles to the caret element
    caret.classList.toggle('caret-rotate');
    // Add the open styles to the menu element
    menu.classList.toggle('menu-open');
  });

  // Loop through all option elements
  options.forEach(option => {
    // Add a click event to the option element
    option.addEventListener('click', () => {
      // Change selected inner text to clicked option inner text
      selected.innerText = option.innerText;
      // Add the clicked select styles to the select element
      select.classList.remove('select-clicked');
      // Add the rotate styles to the caret element
      caret.classList.remove('caret-rotate');
      // Add the open styles to the menu element
      menu.classList.remove('menu-open');
      // Remove active class from all option elements
      options.forEach(option => {
        option.classList.remove('active');
      });
      // Add active class to clicked option element
      option.classList.add('active');
    });
  });
});







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





