var originalSidebarWidth;

window.onload = function () {
    var nav = document.getElementsByClassName("navbar")[0];
    originalSidebarWidth = 40;
    nav.style.width = originalSidebarWidth + "px";
}

function toggleSidebar() {
    var nav = document.getElementsByClassName("navbar")[0];
    if (nav.classList.contains("expand")) {
        nav.style.width = originalSidebarWidth + "px";
        nav.classList.remove("expand");
    } else {
        nav.style.width = "16rem";
        nav.classList.add("expand");
    }
}

function isScreenSmall() {
    var displayWidth = (window.innerWidth > 0) ? window.innerWidth : screen.width;
    return displayWidth < 600;
}
