! function(s) {
  var e = s(window),
    a = s("body"),
    l = s("#main");
  breakpoints({
    xlarge: ["1281px", "1680px"],
    large: ["981px", "1280px"],
    medium: ["737px", "980px"],
    small: ["481px", "736px"],
    xsmall: ["361px", "480px"],
    xxsmall: [null, "360px"]
  }), e.on("load", function() {
    window.setTimeout(function() {
      a.removeClass("is-preload")
    }, 100)
  });
  var t = s("#nav");
  if (0 < t.length) {
    l.scrollex({
      mode: "top",
      enter: function() {
        t.addClass("alt")
      },
      leave: function() {
        t.removeClass("alt")
      }
    });
    var i = t.find("a");
    i.scrolly({
      speed: 1e3,
      offset: function() {
        return t.height()
      }
    }).on("click", function() {
      var e = s(this);
      "#" == e.attr("href").charAt(0) && (i.removeClass("active").removeClass("active-locked"), e.addClass("active").addClass("active-locked"))
    }).each(function() {
      var e = s(this),
        a = e.attr("href"),
        l = s(a);
      l.length < 1 || l.scrollex({
        mode: "middle",
        initialize: function() {
          browser.canUse("transition") && l.addClass("inactive")
        },
        enter: function() {
          l.removeClass("inactive"), 0 == i.filter(".active-locked").length ? (i.removeClass("active"), e.addClass("active")) : e.hasClass("active-locked") && e.removeClass("active-locked")
        }
      })
    })
  }
  s(".scrolly").scrolly({
    speed: 1e3
  })
}(jQuery);


// File dop
var $fileInput = $('.file-input');
var $droparea = $('.file-drop-area');

// highlight drag area
$fileInput.on('dragenter focus click', function() {
  $droparea.addClass('is-active');
});

// back to normal state
$fileInput.on('dragleave blur drop', function() {
  $droparea.removeClass('is-active');
});

// change inner text
$fileInput.on('change', function() {
  var filesCount = $(this)[0].files.length;
  var $textContainer = $(this).prev();

  if (filesCount === 1) {
    // if single file is selected, show file name
    var fileName = $(this).val().split('\\').pop();
    $textContainer.text(fileName);
  } else {
    // otherwise show number of files
    $textContainer.text(filesCount + ' files selected');
  }
});

function uploadFile(file) {
  let url = '/filenames'
  let formData = new FormData()

  formData.append('file', file)

  fetch(url, {
    method: 'POST',
    body: formData
  })
  .then(() => { /* Done. Inform the user */ })
  .catch(() => { /* Error. Inform the user */ })
}
