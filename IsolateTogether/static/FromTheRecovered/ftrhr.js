let counter = 0,
    slides = document.querySelectorAll("li"),
    prevSlide = slides[0],
    numSlides = slides.length - 1;

const enterBtn = document.querySelector("#enter-slideshow"),
      prevBtn = document.querySelector("#prev"),
      nextBtn = document.querySelector("#next");

enterBtn.addEventListener("click", next);
nextBtn.addEventListener("click", next);
prevBtn.addEventListener("click", prev);

function next(){
  counter++;
  btnDisplay();
  setSlides();
};

function prev(){
  counter--;
  btnDisplay();
  setSlides();
};

function btnDisplay() {
  counter == 0 ? enterBtn.style.display="block" : enterBtn.style.display="none";
  counter == 0 ? prevBtn.hidden = true : prevBtn.hidden = false;
  counter == numSlides || counter == 0 ? nextBtn.hidden = true : nextBtn.hidden = false;
}

function setSlides() {
  prevSlide.classList.remove("show");
  slides[counter].classList.add("show");
  prevSlide = slides[counter];
}