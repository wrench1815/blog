/*
 *  Author : Hardeep Kumar   
 *  Created On : Tue Jul 06 2021
 *  File : main.js

*/

// Initialize rellax js
if (document.querySelector('.rellax')) {
  let rellax = new Rellax('.rellax');
}

// Typed js
if (document.getElementById('Multi-Lang-Hello')) {
  let multiLangHelloTyped = new Typed('#Multi-Lang-Hello', {
    strings: ['Hello', 'こんにちは', 'Ciao', '你好', 'नमस्ते', 'Bonjour'],
    typeSpeed: 60,
    backSpeed: 60,
    backDelay: 700,
    loop: true,
  });
}

// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  'use strict';

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation');

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms).forEach((form) => {
    form.addEventListener(
      'submit',
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      },
      false
    );
  });
})();
