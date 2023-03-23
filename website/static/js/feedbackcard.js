// $(".reviews-action").click(function() {

    var modal = document.getElementById("reviewCard");
    var review_btn = document.getElementById("review-btn");
    var review_modal_btn = document.querySelector(".reviews-action");

    review_modal_btn.onclick = function () {
    // To open review modal
        modal.style.display = "block";
}

review_btn.onclick = function () {
    $.ajax({
        url: '/review_store',
        type: 'POST',
        data: {review: $("#review-text").val()},
        success: function(data) {
          // change this later to show a notification saying the review is submitted
          $(".content").prepend('<div class="notification"><div class="notification-message"></div></div>');
          $(".notification-message").html("OPENED NOOTIFICATION!");
        },
        error: function(error) {
          console.log(error);
        }
      });
      modal.style.display = "none";
}
