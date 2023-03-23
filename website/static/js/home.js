$(".waiterbutton").click(function() {
    $.ajax({
        url: '/call_waiter',
        type: 'POST',
        data: {},
        success: function(data) {
          // change this later to show a notification saying the review is submitted
          $(".content").prepend('<div class="notification"><div class="notification-message"></div></div>');
          $(".notification-message").html("Waiter has been called!");
        },
        error: function(error) {
          console.log(error);
        }
      });
});