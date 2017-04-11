$(document).ready(function () {
    $('select').material_select();

    $('a#note-del').click(function (e) {
        e.preventDefault();
        var url = $(this).attr('href');
        $.ajax({
            type: 'delete',
            url: url,
            success: function(response){
                console.log('success');
                // $(this).closest('div#note-card').fadeOut();
            }
        });
        $(this).closest('div#note-card').fadeOut();
        return true;
    })
});