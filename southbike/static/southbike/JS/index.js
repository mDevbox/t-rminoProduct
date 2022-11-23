const MySun = () => {
    const sun = window.document.querySelector('.sun')
    sun.addEventListener('click', () =>  {
    window.document.body.classList.toggle('dark')
    sun.innerHTML = 'Modo Dark'
    console.log('hello')
})
}