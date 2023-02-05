
let likes = 0;
let dislikes = 0;
$(document).ready(function () {
    // ajax to get current likes
    // let likes from server are 10
    // assign the current likes to variable
    likes = 0;
    dislikes = 0; 
    setLikes(likes);
    setdisLikes(likes);
});

$("#likeBtn").on("click", function () {
    // ajax to post a current likes
    // in success add increment to likes
    likes++;
    setLikes(likes);
});

function setLikes(count) {
    $(".totalLikes").text(count);
};

$("#dislike-Btn").on("click", function () {
    // ajax to post a current likes
    // in success add increment to likes
    dislikes++;
    setdisLikes(dislikes);
});

function setdisLikes(count) {
    $(".totalDislikes").text(count);
};

$("#check-btn").click(function () {
   // alert("ohk");
});
