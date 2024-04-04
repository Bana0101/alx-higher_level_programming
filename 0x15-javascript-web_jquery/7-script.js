$.get('https://swapi.co/api/people/5/?format=json', function(d) {
  $('DIV#character').text(d.name);
});
