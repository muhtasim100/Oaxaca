var originalWidth;

window.onload = function () {
    var nav = document.getElementsByClassName("navbar")[0];
    originalWidth = 50;
    nav.style.width = originalWidth + "px";
}

function toggleSidebar() {
    var nav = document.getElementsByClassName("navbar")[0];
    if (nav.classList.contains("expand")) {
        nav.style.width = originalWidth + "px";
        nav.classList.remove("expand");
    } else {
        nav.style.width = "16rem";
        nav.classList.add("expand");
    }
}
