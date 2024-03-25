window.addEventListener("DOMContentLoaded", () => {
	const carousel = document.getElementById("myCarousel");
	const prevBtn = document.getElementById("prevBtn");
	const nextBtn = document.getElementById("nextBtn");
	const slides = document.querySelectorAll(".carousel-item");
	let currentIndex = 0;

	function showSlide(index) {
		slides.forEach((slide, i) => {
			slide.style.transform = `translateX(${100 * (i - index)}%)`;
		});
	}

	function nextSlide() {
		currentIndex = (currentIndex + 1) % slides.length;
		showSlide(currentIndex);
	}

	function prevSlide() {
		currentIndex = (currentIndex - 1 + slides.length) % slides.length;
		showSlide(currentIndex);
	}

	nextBtn.addEventListener("click", nextSlide);
	prevBtn.addEventListener("click", prevSlide);
});
