
$(window).scroll (e) ->
  if $(window).scrollTop() > 128
    $('.header-nav').addClass 'collapsed'
  else
    $('.header-nav').removeClass 'collapsed'
