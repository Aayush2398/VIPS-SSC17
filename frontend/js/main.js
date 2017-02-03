nav_value ="#home";
nav_bg = "";

function anim_bg_content() {
  $(document).ready(function(){
    $('.nav').show();
    $('.logo').show();
    $('.logo-di').show();
  });
}

$(document).ready(function(){
    $('#home').click(function(){
      if(nav_value != "#home") {
        $("#home").addClass('active');
        $(nav_value).removeClass('active');
        $(nav_bg).delay(800).slideUp(800);
        nav_value="#home";
        nav_bg="";
      }
    });

    $("#about").click(function(){
      if(nav_value != "#about"){
        $(".bg-about").slideDown(800);
        $('#about').addClass('active');
        $(nav_value).removeClass('active');
        if(nav_bg != "")
          $(nav_bg).delay(800).slideUp(800);
        nav_value="#about";
        nav_bg=".bg-about";
      }
    });

    $("#spon").click(function(){
      if(nav_value != "#spon"){
        $(".bg-spon").slideDown(800);
        $('#spon').addClass('active');
        $(nav_value).removeClass('active');
        if(nav_bg != "")
          $(nav_bg).delay(800).slideUp(800);
        nav_value="#spon";
        nav_bg=".bg-spon";
      }
    });

    $("#contact").click(function(){
      if(nav_value != "#contact"){
        $(".bg-contact").slideDown(800);
        $('#contact').addClass('active');
        $(nav_value).removeClass('active');
        if(nav_bg != "")
          $(nav_bg).delay(800).slideUp(800);
        nav_value="#contact";
        nav_bg=".bg-contact";
      }
    });

    $("#map").click(function(){
      if(nav_value != "#map"){
        $(".bg-map").slideDown(800);
        $('#map').addClass('active');
        $(nav_value).removeClass('active');
        if(nav_bg != "")
          $(nav_bg).delay(800).slideUp(800);
        nav_value="#map";
        nav_bg=".bg-map";
      }
    });

    $(".evento").click(function(){
      if(nav_value != "#event"){
        $(".bg-event").slideDown(800);
        $('.event').addClass('active');
        $(nav_value).removeClass('active');
        if(nav_bg != "")
          $(nav_bg).delay(800).slideUp(800);
        nav_value=".evento";
        nav_bg=".bg-event";
      }
    });

    $(".get").click(function(){
      if(nav_value != ".sec-get"){
        $(".bg-get").slideDown(800);
        $('.sec-get').addClass('active');
        $(nav_value).removeClass('active');
        if(nav_bg != "")
          $(nav_bg).delay(800).slideUp(800);
        nav_value=".sec-get";
        nav_bg=".bg-get";
      }
    });
});

function anim() {  
  $(document).ready(function(){
    $('.intro-anim').delay(6000).fadeOut(2800);
    $('.intro-anim-2').delay(6000).fadeOut(2800);
    $('.intro').delay(9500).fadeOut(3000);
    setTimeout(anim_bg_content, 9000);
  });
}

anim();

function simple(sim) {
  var simple = "#simple"+sim;
  var detail = "#detail"+sim;
  var rule = "#rule"+sim;
  $(document).ready(function(){
    $(simple).fadeOut();
    $(detail).slideDown(800);
  });  
}

function detail(sim) {
  var simple = "#simple"+sim;
  var detail = "#detail"+sim;
  var rule = "#rule"+sim;
  $(document).ready(function(){
    $(rule).slideDown(800);
    $(detail).fadeOut();
  });  
}

function rule(sim) {
  var simple = "#simple"+sim;
  var detail = "#detail"+sim;
  var rule = "#rule"+sim;
  $(document).ready(function(){
    $(rule).slideUp(800);
    $(simple).fadeIn();
  });  
}

function reg(sim) {
  var simple = "#simple"+sim;
  var detail = "#detail"+sim;
  var rule = "#rule"+sim;
  var reg = "#reg"+sim;
  $(document).ready(function(){
    $(reg).slideDown(800);
    $(simple).fadeOut();
  });  
}

function regClose(sim) {
  var simple = "#simple"+sim;
  var detail = "#detail"+sim;
  var rule = "#rule"+sim;
  var reg = "#reg"+sim;
  $(document).ready(function(){
    $(reg).slideUp(800);
    $(simple).fadeIn();
  });  
}