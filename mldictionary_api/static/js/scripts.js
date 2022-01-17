let $move = document.querySelector('.flier')
$move.addEventListener('click', () =>{
    let $creator = document.querySelector('.creator')
    $creator.classList.toggle('move')
    let $footer = document.querySelector('.footer')
    $footer.classList.toggle('z-index-3')
})

let $image = document.querySelector('.image')
$image.addEventListener('click', ()=>{
    window.open('https://www.linkedin.com/in/pabloemidio/', target='_blank')
})