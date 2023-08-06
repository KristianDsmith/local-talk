function toggleContent(id) {
  var content = document.getElementById(id);
  content.style.display = (content.style.display === 'none' || content.style.display === '') ? 'block' : 'none';
}

$(document).ready(function(){
    $('.news-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        dots: true,
    });
});