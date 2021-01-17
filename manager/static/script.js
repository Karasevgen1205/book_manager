$('document').ready(function () {
    $('.like-comment').on('click', function () {

        let id=$(this).attr('id');

        console.log('hello click', id)
    });
});