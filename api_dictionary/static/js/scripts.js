let $move = document.querySelector('.flier')
$move.addEventListener('click', () =>{
    let $creator = document.querySelector('.creator')
    $creator.classList.toggle('move')
    let $footer = document.querySelector('.footer')
    $footer.classList.toggle('z-index-3')
})