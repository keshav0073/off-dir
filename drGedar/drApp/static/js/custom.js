
jQuery(function () {


	jQuery(window).scroll(function () {
		if (jQuery(this).scrollTop()) {
			jQuery('#back-top').fadeIn();
		} else {
			jQuery('#back-top').fadeOut();
		}
	});

	jQuery("#back-top").click(function () {

		//1 second of animation time
		//html works for FFX but not Chrome
		//body works for Chrome but not FFX
		//This strange selector seems to work universally
		jQuery("html, body").animate({ scrollTop: 0 }, 1500);
	});
	jQuery('#back-bottom').on('click', function() {
		var headerHeight = jQuery('#myHeader').outerHeight();
		var target = jQuery(this).attr('href');
		var offsetTop = jQuery(target).offset().top;
		offsetTop = offsetTop - headerHeight;
		jQuery('html, body').animate({ scrollTop: offsetTop}, 1500);

	});

	jQuery('.owl-carousel-review').owlCarousel({
		loop: true,
		margin: 10,
		nav: false,
		dots: false,
		responsive: {
			0: {
				items: 1
			},
			575: {
				items: 2
			},
			
			767: {
				items: 2
			},
			850: {
				items: 3
			},
		}
	})

});



// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the header
var header = document.getElementById("myHeader");

// Get the offset position of the navbar
var sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset > 100) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}
