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

// Helper Buttons
$(".popup-btn").click(function() {
    $(".helper-popup").css("opacity", "0%");
    let popup = $(this).attr("popup");
    if ($("#" + popup).length) {
        if ($("#" + popup).css("opacity") == "1") {
            return;
        } else {
            $("#" + popup).css("opacity", "100%");
            let left = $(this).offset().left;
            let width = $("#" + popup).width();
            let position = left - width;
            $("#" + popup).css("left", position + "px");
        }
    }
});

function reloadBasket() {

}

$(".basket-item .minus").click();
$(".basket-item .plus").click(function() {

    $.ajax({
        url: '/add_cart_quantity',
        type: 'POST',
        data: {id: $(this).attr("item_id")},
        success: function(data) {
        },
        error: function(error) {
          console.log(error);
        }
      });
});
