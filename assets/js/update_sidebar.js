$('.nav-item').click(function(x){
    previous_active = $('.nav-item.active');
    
    previous_active.removeClass('active');
    $('.' + previous_active.attr("value")).addClass('removed');

    $(this).addClass('active');
    $('.' + $(this).attr("value")).removeClass('removed');
})