document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('toggle');
    const body = document.body;

    toggle.addEventListener('change', () => {
        if (toggle.checked) {
            body.classList.remove('dark-mode');
            body.classList.add('light-mode');
        } else {
            body.classList.remove('light-mode');
            body.classList.add('dark-mode');
        }
    });
});

function toggleMenu() {
    const menu = document.getElementById('menu');
    const burger = document.querySelector('.burger');
    menu.classList.toggle('open');
    burger.classList.toggle('open');
}

document.addEventListener("DOMContentLoaded", function() {
    const faqItems = document.querySelectorAll(".faq-item");

    faqItems.forEach(item => {
        item.querySelector(".faq-question").addEventListener("click", () => {
            item.classList.toggle("active");

            faqItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove("active");
                }
            });
        });
    });
});










