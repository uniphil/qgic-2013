var filter_path;

$(window).scroll(function(e) {
  if ($(window).scrollTop() > 128) {
    return $('.header-nav').addClass('collapsed');
  } else {
    return $('.header-nav').removeClass('collapsed');
  }
});

filter_path = function(string) {
  return string.replace(/^\//, '').replace(/(index|default).[a-zA-Z]{3,4}$/, '').replace(/\/$/, '');
};

$('a[href*=#]').each(function() {});
