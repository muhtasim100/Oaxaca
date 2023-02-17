
const dropdown = document.querySelector('.dropdown');
const dropdownMenu = document.querySelector('.dropdown-menu');
const tableButtons = document.querySelectorAll('.action');


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


