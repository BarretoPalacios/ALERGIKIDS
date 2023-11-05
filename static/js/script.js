
// animaciones con el scroll 
var propiedades = {
  origin: 'top',
  duration: 400,
  reset:true,
  scale: .1,
  easing:'ease-in-out',
  };    
  ScrollReveal().reveal('.aparecer', propiedades);





// codigo para el menu desplegable 
const button = document.getElementById("btn-menu")
const links    = document.querySelector('.header_links')
const icono    = document.querySelector('.icono')

let iconoCambiado = true

button.addEventListener('click',(e)=>{
    links.classList.toggle('mostrar')

    if (iconoCambiado) {
        icono.classList.remove("bi-list");
        icono.classList.add("bi-x-lg");
      } else {
        icono.classList.remove("bi-x-lg");
        icono.classList.add("bi-list");
      }
      iconoCambiado = !iconoCambiado;
})



