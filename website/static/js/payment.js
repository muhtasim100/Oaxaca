var pay_btn = document.getElementById("paynow-btn");

pay_btn.onclick = function () {
    $.ajax({
        url: '/create_order',
        type: 'POST',
        data: {},
        success: function(data) {
            window.location.href = "/order_tracker/" + data;
        },
        error: function(error) {
            $(".content").prepend('<div class="notification"><div class="notification-message"></div></div>');
            $(".notification-message").html("There was an error processing your order!");
        }
    });
}
