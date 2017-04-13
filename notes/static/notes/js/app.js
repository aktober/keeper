$(document).ready(function () {
    $('select').material_select();

    $('a#note-del').click(function (e) {
        e.preventDefault();
        var url = $(this).attr('href');
        $.ajax({
            type: 'delete',
            url: url,
            success: function(){
                console.log('success');
                // $(this).closest('div#note-card').fadeOut();
            }
        });
        $(this).closest('div#note-card').fadeOut();
        return true;
    });

    $('#tag-form').on('submit', function (e) {
        e.preventDefault();
        var url = $(this).attr('action');
        var value = $('#tag-text').val();
        $.ajax({
            type: 'post',
            url: url,
            data: { tag: value },
            success: function() {
                console.log('success');
                $('div.tags-list').append("<div class='chip'>" +
                value + "<i class='close material-icons'>close</i></div>");
                $('#tag-text').val("");
            }
        });
    })
});