function toggleSidebar() {
    var nav = document.getElementsByClassName("navbar")[0];
    if (nav.classList.contains("expand")) {
        nav.classList.remove("expand");
    } else {
        nav.classList.add("expand");
    }
}
