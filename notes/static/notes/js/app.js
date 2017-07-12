$(document).ready(function () {

    $('a#note-del').click(function (e) {
        e.preventDefault();
        var url = $(this).attr('href');
        $.ajax({
            type: 'delete',
            url: url,
            success: function(){
                console.log('success');
                // $(this).closest('div#note-card').fadeOut();
            //    todo: rearrange cards
            }
        });
        $(this).closest('div.card').fadeOut();
        return true;
    });
});