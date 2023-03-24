var originalSidebarWidth;

window.onload = function () {
    var nav = document.getElementsByClassName("navbar")[0];
    var content = document.getElementsByClassName("content")[0];
    originalSidebarWidth = 40;
    nav.style.width = originalSidebarWidth + "px";

    if (!isScreenSmall()) {
        content.style.marginLeft = originalSidebarWidth + "px";
    } else {
        content.style.marginLeft = "0px";
    }
}

function toggleSidebar() {
    var nav = document.getElementsByClassName("navbar")[0];
    var content = document.getElementsByClassName("content")[0];

    if (nav.classList.contains("expand")) {
        nav.style.width = originalSidebarWidth + "px";
        
        if (!isScreenSmall()) {
            content.style.marginLeft = originalSidebarWidth + "px";
        } else {
            content.style.marginLeft = "0px";
        }

        nav.classList.remove("expand");
    } else {
        nav.style.width = "16rem";
        content.style.marginLeft = "16rem";
        nav.classList.add("expand");
    }
}

function isScreenSmall() {
    var displayWidth = (window.innerWidth > 0) ? window.innerWidth : screen.width;
    return displayWidth < 800;
}

window.onclick = function (event) {
    if (event.target.classList.contains("modal")) {
        let modals = Array.from(document.getElementsByClassName("modal"));
        modals.forEach(function(modal) {
            modal.style.display = "none";
        });
    }
}

$(".toplogo-container-parent").click(function() {
    window.location.href = '/';
});


// Call Waiter Buttons
$(".waiterbutton").click(function() {
    $.ajax({
        url: '/call_waiter',
        type: 'POST',
        data: {},
        success: function(data) {
          $(".content").prepend('<div class="notification"><div class="notification-message"></div></div>');
          $(".notification-message").html("Waiter has been called!");
        },
        error: function(error) {
          console.log(error);
        }
      });
});

// Dropdown Buttons
$(document).on("click", ".dropdown-button", function() {
    $(this).closest(".dropdown-menu").toggleClass("show");
});


// Helper Buttons
$(".popup-btn").click(function() {
    $(".helper-popup").css("opacity", "0%");
    $(".helper-popup").css("z-index", "-1000");
    let popup = $(this).attr("popup");
    if ($("#" + popup).length) {
        if ($("#" + popup).css("opacity") == "1") {
            return;
        } else {
            $("#" + popup).css("opacity", "100%");
            $(".helper-popup").css("z-index", "10");
            let left = $(this).offset().left;
            let width = $("#" + popup).width();
            let position = left - width;
            $("#" + popup).css("left", position + "px");
        }
    }
});


// Add Table Code
$(document).on("click", "#add-table-btn", function() {
    $.ajax({
        url: '/add_table',
        type: 'POST',
        data: {seats: $("#table_seats").val()},
        success: function(data) {
            $(".content").prepend('<div class="notification"><div class="notification-message"></div></div>');
            $(".notification-message").html("The table has been added!");
        },
        error: function(error) {
          console.log(error);
        }
      });
});

// Basket Code

function reloadBasket() {
    $.ajax({
        url: '/cart_products',
        type: 'POST',
        success: function(data) {
            $("#basket-popup .helper-content").html(data);
        },
        error: function(error) {
          console.log(error);
        }
      });
}

$(document).on("click", ".basket-item .minus", function() {
    $.ajax({
        url: '/minus_cart_quantity',
        type: 'POST',
        data: {id: $(this).attr("item_id")},
        success: function(data) {
            reloadBasket();
        },
        error: function(error) {
          console.log(error);
        }
      });
});

$(document).on("click", ".basket-item .plus", function() {
    $.ajax({
        url: '/add_cart_quantity',
        type: 'POST',
        data: {id: $(this).attr("item_id")},
        success: function(data) {
            reloadBasket();
        },
        error: function(error) {
          console.log(error);
        }
      });
});

$(document).on("click", "#basket-pay-now", function() {
    window.location.href = "/payment";
});
