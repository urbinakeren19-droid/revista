/* =========================================================================
   AURA — comportamiento de interfaz
   Sin dependencias. Se carga con `defer`.
   ========================================================================= */

(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------------------------------------------------------------
     Menú en pantallas pequeñas
     --------------------------------------------------------------------- */
  function initNav() {
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.getElementById('nav');
    if (!toggle || !nav) return;

    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    });

    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  /* ---------------------------------------------------------------------
     Diagrama de capas del hero
     Cada .layer-slab lleva sus datos en atributos data-*.
     --------------------------------------------------------------------- */
  function initLayers() {
    var root = document.querySelector('.layers');
    if (!root) return;

    var slabs = Array.prototype.slice.call(root.querySelectorAll('.layer-slab'));
    var elName = root.querySelector('[data-out="name"]');
    var elIdx = root.querySelector('[data-out="idx"]');
    var elBody = root.querySelector('[data-out="body"]');
    var elSpecs = root.querySelector('[data-out="specs"]');
    if (!slabs.length || !elName) return;

    function show(slab, byUser) {
      if (byUser) root.setAttribute('data-touched', '');

      slabs.forEach(function (s) {
        var on = s === slab;
        s.classList.toggle('is-active', on);
        s.setAttribute('aria-pressed', on ? 'true' : 'false');
        var shift = on ? s.getAttribute('data-shift') || '-14' : '0';
        s.style.transform = 'translateY(' + shift + 'px)';
      });

      root.setAttribute('data-active', slab.getAttribute('data-idx'));
      elName.textContent = slab.getAttribute('data-name') || '';
      if (elIdx) elIdx.textContent = slab.getAttribute('data-idx') || '';
      if (elBody) elBody.textContent = slab.getAttribute('data-body') || '';

      if (elSpecs) {
        elSpecs.innerHTML = '';
        var specs = (slab.getAttribute('data-specs') || '').split('|');
        specs.forEach(function (pair) {
          if (!pair.trim()) return;
          var parts = pair.split(':');
          var li = document.createElement('li');
          var b = document.createElement('b');
          b.textContent = parts[0].trim();
          li.appendChild(b);
          li.appendChild(document.createTextNode(' ' + (parts[1] || '').trim()));
          elSpecs.appendChild(li);
        });
      }
    }

    slabs.forEach(function (slab) {
      slab.setAttribute('role', 'button');
      slab.setAttribute('tabindex', '0');
      slab.setAttribute('aria-pressed', 'false');
      slab.setAttribute('aria-label', 'Capa ' + slab.getAttribute('data-idx') + ': ' + slab.getAttribute('data-name'));

      slab.addEventListener('click', function () { show(slab, true); });
      slab.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); show(slab, true); }
      });
    });

    // Orden visual, no orden de dibujo: la capa 01 es la superficie.
    slabs.sort(function (a, b) {
      return a.getAttribute('data-idx').localeCompare(b.getAttribute('data-idx'));
    });

    show(slabs[0], false);
  }

  /* ---------------------------------------------------------------------
     Aparición al hacer scroll
     --------------------------------------------------------------------- */
  function initReveal() {
    var items = document.querySelectorAll('.rise');
    if (!items.length) return;

    if (reduce || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var delay = parseInt(el.getAttribute('data-delay') || '0', 10);
        setTimeout(function () { el.classList.add('is-in'); }, delay);
        io.unobserve(el);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });

    items.forEach(function (el) { io.observe(el); });
  }

  /* ---------------------------------------------------------------------
     Barra de progreso de lectura (solo en artículos)
     --------------------------------------------------------------------- */
  function initProgress() {
    var bar = document.querySelector('.progress');
    var body = document.querySelector('.article__body');
    if (!bar || !body) return;

    var ticking = false;

    function update() {
      var rect = body.getBoundingClientRect();
      var total = rect.height - window.innerHeight;
      var done = -rect.top;
      var pct = total > 0 ? Math.min(Math.max(done / total, 0), 1) : 0;
      bar.style.width = (pct * 100).toFixed(2) + '%';
      ticking = false;
    }

    window.addEventListener('scroll', function () {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });

    window.addEventListener('resize', update, { passive: true });
    update();
  }

  /* ---------------------------------------------------------------------
     Calculadora de residuo evitado
     Base: 2,4 g de plástico por toalla convencional (medición Natracare).
     El usuario define cuántas toallas usa por ciclo.
     --------------------------------------------------------------------- */
  function initCalc() {
    var input = document.getElementById('calc-pads');
    if (!input) return;

    var PLASTIC_G = 2.4;   // gramos de plástico por toalla convencional
    var CYCLES = 13;       // ciclos por año (aprox.)
    var BAG_G = 8;         // gramos de una bolsa plástica de supermercado

    var outVal = document.querySelector('[data-calc="val"]');
    var outYear = document.querySelector('[data-calc="year"]');
    var outBags = document.querySelector('[data-calc="bags"]');
    var outLife = document.querySelector('[data-calc="life"]');

    function fmt(n, dec) {
      return n.toLocaleString('es-HN', {
        minimumFractionDigits: dec || 0,
        maximumFractionDigits: dec || 0
      });
    }

    function run() {
      var perCycle = parseInt(input.value, 10);
      var perYear = perCycle * CYCLES;
      var gramsYear = perYear * PLASTIC_G;

      if (outVal) outVal.textContent = perCycle;
      if (outYear) outYear.textContent = fmt(gramsYear / 1000, 1) + ' kg';
      if (outBags) outBags.textContent = fmt(gramsYear / BAG_G);
      if (outLife) outLife.textContent = fmt((gramsYear * 38) / 1000) + ' kg';
    }

    input.addEventListener('input', run);
    run();
  }

  /* ---------------------------------------------------------------------
     Año actual en el pie
     --------------------------------------------------------------------- */
  function initYear() {
    var el = document.querySelector('[data-year]');
    if (el) el.textContent = new Date().getFullYear();
  }

  /* --------------------------------------------------------------------- */
  function boot() {
    initNav();
    initLayers();
    initReveal();
    initProgress();
    initCalc();
    initYear();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
