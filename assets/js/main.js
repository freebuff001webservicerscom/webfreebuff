/* WebServicers — front page interactions */
(function () {
  'use strict';

  var header = document.querySelector('.site-header');
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('primary-nav');
  var menus = Array.prototype.slice.call(document.querySelectorAll('.has-menu'));

  /* Sticky header shadow */
  function onScroll() {
    if (!header) return;
    header.classList.toggle('is-scrolled', window.scrollY > 8);
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* Mobile navigation */
  function closeNav() {
    if (!nav || !toggle) return;
    nav.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open menu');
    document.body.classList.remove('nav-open');
    closeMenus();
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      document.body.classList.toggle('nav-open', open);
    });
  }

  /* Dropdown menus (click / keyboard) */
  function closeMenus(except) {
    menus.forEach(function (item) {
      if (item === except) return;
      item.classList.remove('open');
      var btn = item.querySelector('.nav-link[aria-expanded]');
      if (btn) btn.setAttribute('aria-expanded', 'false');
    });
  }

  menus.forEach(function (item) {
    var btn = item.querySelector('.nav-link[aria-expanded]');
    if (!btn) return;
    btn.addEventListener('click', function (event) {
      event.preventDefault();
      var willOpen = !item.classList.contains('open');
      closeMenus(item);
      item.classList.toggle('open', willOpen);
      btn.setAttribute('aria-expanded', String(willOpen));
    });
  });

  document.addEventListener('click', function (event) {
    if (!event.target.closest('.has-menu')) closeMenus();
    if (nav && nav.classList.contains('is-open') && (!event.target.closest('.site-header') || event.target.closest('a'))) closeNav();
  });

  document.addEventListener('keydown', function (event) {
    if (event.key !== 'Escape') return;
    closeMenus();
    if (nav && nav.classList.contains('is-open')) {
      closeNav();
      if (toggle) toggle.focus();
    }
  });

  /* Close the mobile menu after choosing a link */
  if (nav) {
    nav.addEventListener('click', function (event) {
      if (event.target.closest('a') && window.matchMedia('(max-width: 980px)').matches) {
        closeNav();
        closeMenus();
      }
    });
  }

  window.addEventListener('resize', function () {
    if (window.matchMedia('(min-width: 981px)').matches) closeNav();
  });

  /* Reveal on scroll */
  var revealItems = document.querySelectorAll('[data-reveal]');
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!('IntersectionObserver' in window) || reduceMotion) {
    revealItems.forEach(function (el) { el.classList.add('is-visible'); });
  } else {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

    revealItems.forEach(function (el) { observer.observe(el); });
  }

  /* Keep only one FAQ answer open at a time */
  var faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(function (item) {
    item.addEventListener('toggle', function () {
      if (!item.open) return;
      faqItems.forEach(function (other) {
        if (other !== item) other.open = false;
      });
    });
  });
})();
