const dropdowns = document.querySelectorAll('.dropdown');
const dropdownMenu = document.querySelector('.dropdown-menu');
const tableButtons = document.querySelectorAll('.action');

// ----------------------------------------

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

dropdownMenu.addEventListener('click', function(event) {
  
  const selectedOption = event.target.innerText; // get the text of the clicked dropdown item

  
  tableButtons.forEach(function(button) { // loop through all the table buttons
    
    const colorDot = button.querySelector('.numcircle');
    
    if (selectedOption === "Show all") { // show the color dot element if "Show all" is selected
      button.style.display = "block";
    } 
   
    else if (selectedOption === "Occupied" && colorDot.classList.contains('red-dot')) {  // show the red dot element if "A" is selected
      button.style.display = "block"; 
    }
    
    else if (selectedOption === "Reserved for the next two hours" && colorDot.classList.contains('yellow-dot')) { // show the yellow dot element if "B" is selected
      button.style.display = "block";
    }
    
    else if (selectedOption === "Available" && colorDot.classList.contains('green-dot')) { // show the green dot element if "C" is selected
      button.style.display = "block"; 
    }
  
    else {
      button.style.display = "none";
    }
  });
});
