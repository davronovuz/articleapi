// Initialize Reveal.js
Reveal.initialize({
  hash: true,
  slideNumber: true,
  plugins: [ RevealHighlight ]
});

// Set today date in title slide
(function setToday() {
  const span = document.getElementById('date-span');
  if (span) {
    const d = new Date();
    span.textContent = d.toLocaleDateString();
  }
})();

// Re-trigger typewriter animation when its slide becomes active
Reveal.on('slidechanged', (event) => {
  const codeBlock = event.currentSlide.querySelector('.typewriter');
  if (codeBlock) {
    // restart animation by cloning node
    const parent = codeBlock.parentElement;
    const clone = codeBlock.cloneNode(true);
    parent.replaceChild(clone, codeBlock);
  }

  // Confetti on last slide
  if (event.indexh === 11) { // slide 12 (0-based)
    launchConfetti();
  }
});

function launchConfetti() {
  if (window.__confettiDone) return;
  window.__confettiDone = true;
  const duration = 5 * 1000;
  const end = Date.now() + duration;

  (function frame() {
    confetti({
      particleCount: 3,
      angle: 60,
      spread: 55,
      origin: { x: 0 },
    });
    confetti({
      particleCount: 3,
      angle: 120,
      spread: 55,
      origin: { x: 1 },
    });
    if (Date.now() < end) {
      requestAnimationFrame(frame);
    }
  })();
}