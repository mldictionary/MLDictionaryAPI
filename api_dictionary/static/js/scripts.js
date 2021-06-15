let $move = document.querySelector('.flier')
$move.addEventListener('click', (event)=>{
    let $footer = document.querySelector('.footer')
    $footer.classList.toggle('move')
})