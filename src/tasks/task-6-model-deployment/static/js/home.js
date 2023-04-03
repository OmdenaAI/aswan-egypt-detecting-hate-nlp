
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
    $("#check-btn").on('click', function (evt) {
        evt.preventDefault();
        $('.hateful').hide()
        $('.risk').hide()
        $('.neutral').hide()
        const text = $('#textfield').val();
        if(!text){
            alert('Please enter the text to check!');
            return;
        }
        //ajax to send the statement to flask server for hateful level detection
        $.ajax({
            url: '/check-statement',
            data: {text: text},
            type: 'post'
        }).then(data => {
            if(data.prediction === 2){
                $('.hateful').show()
            }
            else if(data.prediction === 1){
                $('.risk').show()
            }
            else{
                $('.neutral').show()
            }
        }).catch(err => console.log('Error: ', err));
    });

    $("#dislike-Btn").on("click", function () {
        // ajax to post a current likes
        // in success add increment to likes
        dislikes++;
        setdisLikes(dislikes);
    });

    $("#likeBtn").on("click", function () {
        // ajax to post a current likes
        // in success add increment to likes
        likes++;
        setLikes(likes);
    });

});


function setLikes(count) {
    $(".totalLikes").text(count);
};


function setdisLikes(count) {
    $(".totalDislikes").text(count);
};