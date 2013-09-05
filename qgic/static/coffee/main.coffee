
$(window).scroll (e) ->
  if $(window).scrollTop() > 212
    $('.header-nav').addClass 'collapsed'
  else
    $('.header-nav').removeClass 'collapsed'
