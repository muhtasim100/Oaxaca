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
    if (!event.target.classList.contains("circle-btn")) {
        let helpers = Array.from(document.getElementsByClassName("helper-popup"));
        helpers.forEach(function(helper) {
            helper.style.opacity = "0%";
        });
    }

    if (event.target.classList.contains("modal")) {
        let modals = Array.from(document.getElementsByClassName("modal"));
        modals.forEach(function(modal) {
            modal.style.display = "none";
        });
    }
}


// Helper Buttons
$(".question-btn").click(function () {
    $(".helper-popup").css("opacity", "0%");
    $(".table-popup").css("opacity", "100%");
});
