/* WebServicers — static forms: account pages (sign in / sign up / reset)
   and the contact page. None of them have a backend yet, so submitting
   explains that instead of pretending to send anything. */
(function () {
  'use strict';

  var forms = document.querySelectorAll('.auth-form, .contact-form');
  if (!forms.length) return;

  Array.prototype.forEach.call(forms, function (form) {
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      var feedback = form.querySelector('.auth-feedback, .contact-feedback');
      if (!feedback) return;
      feedback.hidden = false;
      feedback.textContent = form.getAttribute('data-feedback') ||
        'This is a preview of the sign-in screen — accounts are not connected yet.';
    });
  });
})();
