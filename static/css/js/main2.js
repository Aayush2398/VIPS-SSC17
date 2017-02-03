nav_value ="#home";
nav_bg = "";

function anim_bg_content() {
  $(document).ready(function(){
    var height = $(window).width(); 
    if(height > 900) {
      $('.nav').show();
      $('.logo-di').show();
    }
    $('.logo').show();
  });
}

$(document).ready(function(){
    $('.home').click(function(){
      if(nav_value != ".home") {
        $("#home").addClass('active');
        $(nav_value).removeClass('active');
        $(nav_bg).delay(800).slideUp(800);
        nav_value=".home";
        nav_bg="";
      }
    });

    $(".about").click(function(){
      if(nav_value != ".about"){
        $(".bg-about").slideDown(800);
        $('#about').addClass('active');
        $(nav_value).removeClass('active');
        if(nav_bg != "")
          $(nav_bg).delay(800).slideUp(800);
        nav_value=".about";
        nav_bg=".bg-about";
      }
    });

    $(".spon").click(function(){
      if(nav_value != ".spon"){
        $(".bg-spon").slideDown(800);
        $('#spon').addClass('active');
        $(nav_value).removeClass('active');
        if(nav_bg != "")
          $(nav_bg).delay(800).slideUp(800);
        nav_value=".spon";
        nav_bg=".bg-spon";
      }
    });

    $(".contact").click(function(){
      if(nav_value != ".contact"){
        $(".bg-contact").slideDown(800);
        $('#contact').addClass('active');
        $(nav_value).removeClass('active');
        if(nav_bg != "")
          $(nav_bg).delay(800).slideUp(800);
        nav_value=".contact";
        nav_bg=".bg-contact";
      }
    });

    $(".map").click(function(){
      if(nav_value != ".map"){
        $(".bg-map").slideDown(800);
        $('#map').addClass('active');
        $(nav_value).removeClass('active');
        if(nav_bg != "")
          $(nav_bg).delay(800).slideUp(800);
        nav_value=".map";
        nav_bg=".bg-map";
      }
    });

    $(".evento").click(function(){
      if(nav_value != ".evento"){
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
  var h1 = "#rule"+sim+" h1";
  var h2 = "#rule"+sim+" h2";
  $(h1).html("RULE BOOK");
  $(h2).css("display", "inline-block");
  $(document).ready(function(){
    $(rule).fadeOut();
    $(simple).fadeIn();
  });  
}

function reg(sim) {
  var simple = "#simple"+sim;
  var detail = "#detail"+sim;
  var rule = "#rule"+sim;
  var reg = "#reg"+sim;
  var check = "#checkReg"+sim;
  $(document).ready(function(){
    $(reg).slideDown(800);
    $(check).fadeOut();
  });  
}

function regCheck(sim) {
  var simple = "#simple"+sim;
  var detail = "#detail"+sim;
  var rule = "#rule"+sim;
  var reg = "#checkReg"+sim;
  var check = "#checkReg"+sim;
  $(document).ready(function(){
    $(reg).slideDown(800);
    $(simple).fadeOut();
  });  
}

function regJoin(sim) {
  var simple = "#simple"+sim;
  var detail = "#detail"+sim;
  var rule = "#rule"+sim;
  var reg = "#regJoin"+sim;
  var check = "#checkReg"+sim;
  $(document).ready(function(){
    $(reg).slideDown(800);
    $(check).fadeOut();
  });  
}

function regJoinClose(sim) {
  var simple = "#simple"+sim;
  var detail = "#detail"+sim;
  var rule = "#rule"+sim;
  var reg = "#regJoin"+sim;
  $(document).ready(function(){
    $(reg).fadeOut();
    $(simple).fadeIn();
  });
  var teams = "#regJoin"+sim+" .teams";
  var codes = "#regJoin"+sim+" .codes";
  var events = "#regJoin"+sim+" .events";
  var emails = "#regJoin"+sim+" .emails";
  var contacts = "#regJoin"+sim+" .contacts";
  var colleges = "#regJoin"+sim+" .colleges";
  var years = "#regJoin"+sim+" .years";
  var courses = "#regJoin"+sim+" .courses";
  var songnames = "#regJoin"+sim+" .songname";
  var h1 = "#rule"+sim+" h1";
  var h2 = "#rule"+sim+" h2";
  $(h2).css("display", "none");
  var team = $(teams).val();
  var event = $(events).val();
  var email = $(emails).val();
  var code = $(codes).val();
  var contact = $(contacts).val();
  var college = $(colleges).val();
  var year = $(years).val();
  var course = $(courses).val();
  var songname = $(songnames).val();
  var statusMsg = 0;
  $.ajax({
    type : "POST",
    url: '/join_team/',
    data: {
      'team': team,
      //'code': code,
      'email': email,
      'event': event,
      'contact': contact,
      'college': college,
      'year': year,
      'course':course,
      'songname': songname
    },
    dataType: 'json',
    success: function (data) {
      statusMsg = data.status;
      $(h1).html(statusMsg);
      $(rule).slideDown(800);
    }
  });

}

function regClose(sim) {
  var simple = "#simple"+sim;
  var detail = "#detail"+sim;
  var rule = "#rule"+sim;
  var reg = "#reg"+sim;
  $(document).ready(function(){
    $(reg).fadeOut();
    $(simple).fadeIn();
  });
  var teams = "#reg"+sim+" .teams";
  var codes = "#reg"+sim+" .codes";
  var events = "#reg"+sim+" .events";
  var emails = "#reg"+sim+" .emails";
  var contacts = "#reg"+sim+" .contacts";
  var colleges = "#reg"+sim+" .colleges";
  var years = "#reg"+sim+" .years";
  var h1 = "#rule"+sim+" h1";
  var h2 = "#rule"+sim+" h2";
  $(h2).css("display", "none");
  var team = $(teams).val();
  var event = $(events).val();
  var email = $(emails).val();
  var code = $(codes).val();
  var contact = $(contacts).val();
  var college = $(colleges).val();
  var year = $(years).val();
  $.ajax({
    type : "POST",
    url: '/validate_team/',
    data: {
      'team': team,
      'code': code,
      'event': event,
      'email': email
      //'contact': contact,
      //'college': college,
      //'year': year
    },
    dataType: 'json',
    success: function (data) {
      if (data.is_taken) {
        $(h1).html('Oops! Someone is already using this name or code :/ or you have already created a team :|');
        $(rule).slideDown(800);
      }
      else {
        $(h1).html('Registeration Confirmed.Please check your email for further details');
        $(rule).slideDown(800);
      }
    }
  });


}

$(document).ready(function(){
  var toggleCheck = 0;
  $('#nav-icon').click(function(){
    $(this).toggleClass('open');
    if(toggleCheck == 0){
      $('.nav-mob').slideDown(800);
      toggleCheck = 1;
    }
    else {
      $('.nav-mob').slideUp(800);
      toggleCheck = 0;
    }
  });

  $(".nav-back").click(function(){
    $('.nav-mob').fadeOut();
    $('#nav-icon').toggleClass('open');
    toggleCheck = 0;
  });  
});

$('.contact-check').bind('keyup blur',function(){ 
    var node = $(this);
    node.val(node.val().replace(/[^0-9]/g,'') ); }
);

$('.college-check').bind('keyup blur',function(){ 
    var node = $(this);
    node.val(node.val().replace(/[^a-zA-Z\s]/g,'') ); }
);

$('.year-check').bind('keyup blur',function(){ 
    var node = $(this);
    node.val(node.val().replace(/[^1-6\s]/g,'') ); }
);

function closeAll(sim) {
  var simple = "#simple"+sim;
  var reg = "#reg"+sim;
  var regJoin = "#regJoin"+sim;
  var checkReg = "#checkReg"+sim;
  $(document).ready(function(){
    $(simple).fadeIn();
    $(reg).fadeOut();
    $(regJoin).fadeOut();
    $(checkReg).fadeOut();
  });  
}

var target_date = new Date("Jan 21, 2017").getTime();
var days, hours, minutes, seconds;
var countdown = document.getElementById("countdown");
setInterval(function () {
    var current_date = new Date().getTime();
    var seconds_left = (target_date - current_date) / 1000;
    days = parseInt(seconds_left / 86400);
    seconds_left = seconds_left % 86400;
    hours = parseInt(seconds_left / 3600);
    seconds_left = seconds_left % 3600;
    minutes = parseInt(seconds_left / 60);
    seconds = parseInt(seconds_left % 60);
    countdown.innerHTML = days + "d " + hours + "h "
    + minutes + "m " + seconds + "s ";
}, 1000);