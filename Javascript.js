/* ===========================================================
   BARÇABOT — main.js
   Funcions comunes a totes les pàgines: menú mòbil + enllaç actiu
   =========================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // --- Menú hamburguesa per a mòbil ---
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');

  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const isOpen = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Tanca el menú en clicar un enllaç (mòbil)
    links.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        links.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // --- Marca l'enllaç actiu segons la pàgina actual ---
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach((link) => {
    const href = link.getAttribute('href');
    if (href === currentPage) {
      link.classList.add('active');
    }
  });

  // --- Any actual al peu de pàgina ---
  const yearSpan = document.querySelector('[data-year]');
  if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
  }
});
