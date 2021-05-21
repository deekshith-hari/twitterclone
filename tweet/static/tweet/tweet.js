$(document).ready(function () {
  $(".menu").click(function () {
    $(this).next().toggle();
  });

  $("#createButton").click(function () {
    var serializedData = $("#likeTweet").serialize();
    var url = $("#likeTweet").data("url");
    console.log(serializedData);

    $.ajax({
      url: url,
      data: serializedData,
      type: "post",
      success: function (response) {
        $("#likeCount").append(response.tweet.likes.all.count);
      },
    });
  });
});
