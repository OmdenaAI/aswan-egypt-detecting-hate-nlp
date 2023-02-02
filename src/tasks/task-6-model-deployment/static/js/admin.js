$(function(){
    $("#uploadFile").on('click',function(){
        let fileExt = $("#zip-file").val();
        if (!fileExt.endsWith(".zip")) {
            $("#zip-error").modal("show");
        }
        else{
            let myFile = $('#zip-file').prop('files');
            console.log(`uploaded file ${myFile[0]}`)
        }
    });
    
});


