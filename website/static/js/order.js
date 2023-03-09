let currentIndex = 0;
const images = document.getElementsByClassName("image");

function nextImage() {
  images[currentIndex].classList.remove("visible");
  images[currentIndex].classList.add("hidden");
  currentIndex = (currentIndex + 1) % images.length;
  images[currentIndex].classList.remove("hidden");
  images[currentIndex].classList.add("visible");
}
