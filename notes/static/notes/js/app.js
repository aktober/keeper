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
                $.ajax({
                    type: 'get',
                    url: '/ajax/notes/',
                    success: function() {
                        console.log('ajax success');
                        $('div#ajax_notes_list').html('<h2>Ajax</h2>');
                    }
                });
            }
        });
        // $(this).closest('div.card').fadeOut();
        return true;
    });
});