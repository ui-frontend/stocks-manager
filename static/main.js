$(document).ready( function() {

  $("td.val:contains('-')").addClass('r');
  $("td.val:contains('+')").addClass('g');
});

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, options);
  });

  // Or with jQuery

  $(document).ready(function(){
    $('.modal').modal();
  });



  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.autocomplete');
    var instances = M.Autocomplete.init(elems, options);
  });


  // Or with jQuery

  $(document).ready(function(){
    $('input.autocomplete').autocomplete({
      data: {
        "Apple": null,
        "NVDA": 'https://w7.pngwing.com/pngs/733/607/png-transparent-nvidia-logo-geforce-intel-graphics-processing-unit-nvidia-electronics-text-computer.png',
        "Microsoft": null,
        "Google": 'https://placehold.it/250x250'
      },
    });
  });