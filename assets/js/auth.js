/* WebServicers — account pages (sign in / sign up / reset password)
   These screens are front-end only until an auth backend is connected,
   so submitting explains that instead of pretending to sign anyone in. */
(function () {
  'use strict';

  var forms = document.querySelectorAll('.auth-form');
  if (!forms.length) return;

  Array.prototype.forEach.call(forms, function (form) {
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      var feedback = form.querySelector('.auth-feedback');
      if (!feedback) return;
      feedback.hidden = false;
      feedback.textContent = form.getAttribute('data-feedback') ||
        'This is a preview of the sign-in screen — accounts are not connected yet.';
    });
  });
})();
