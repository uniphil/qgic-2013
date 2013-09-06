$(window).scroll(function(e) {
  if ($(window).scrollTop() > 128) {
    return $('.header-nav').addClass('collapsed');
  } else {
    return $('.header-nav').removeClass('collapsed');
  }
});
