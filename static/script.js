let indice = 0;
const slides = document.querySelectorAll(".slide");
const totalSlides = slides.length;

function moverSlide(direccion) {
    const slider = document.querySelector(".slider-container");

    indice += direccion;

    if (indice >= totalSlides) {
        indice = 0;  // Si llega al final, vuelve al inicio
    } else if (indice < 0) {
        indice = totalSlides - 1;  // Si está en la primera, va a la última
    }

    slider.style.transform = `translateX(${-indice * 100}%)`;
}

// Auto-slide cada 4 segundos
let intervalo = setInterval(() => moverSlide(1), 4000);

document.querySelectorAll(".btn-slider").forEach(btn => {
    btn.addEventListener("click", () => {
        clearInterval(intervalo);
        intervalo = setInterval(() => moverSlide(1), 4000);
    });
});
