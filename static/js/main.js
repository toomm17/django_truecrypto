// burger menu animation and appearance

function burgerToggleAnimation(){
  let burger      = document.querySelector('.burger'),
      navbarMenu  = document.querySelector('.navbar__menu'),
      navbarLinks = document.querySelectorAll('.navbar__link');

  burger.addEventListener('click', function(){
    document.querySelector('body').classList.toggle('hidden')
    burger.classList.toggle('burger-toggle')
    navbarMenu.classList.toggle('navbar-active')

    navbarLinks.forEach( (link, index) => {
      if (link.style.animation) {
        link.style.animation = ''
      } else {
        link.style.animation = `navbarItemsFade .5s ease forwards ${index / navbarLinks.length + 0.3}s`
      }
    })
  })
}

burgerToggleAnimation()

// modal calendar day
function getRightModal(blockText) {

  let modals = document.querySelectorAll('.calendar-block-modal')
  let modalsArray = Array.apply(null, modals)
  return modalsArray.find(item => item.dataset.event === blockText)
}
    

function calendarDayModal() {
  document.querySelectorAll('.calendar__day').forEach(block => {
    block.addEventListener('click', function(){
      console.log('тык на блок')
      let modal = getRightModal(block.querySelector('span.calendar-day__time-nums').dataset.event)
      console.log(modal)
      document.querySelector('body').classList.add('hidden')
      document.querySelector('.mask').style.display = 'block'
      modal.style.display = 'block'

      data = [
        '.calendar-day__date',
        '.calendar-day__time-nums',
        '.calendar-day__title',
        '.calendar-day__descrption'
      ]

      data.forEach(className => {
        modal.querySelector(className).innerText = block.querySelector(className).textContent
      })
      modal.querySelector('.btn-orange').addEventListener('click', function(){
        document.querySelector('body').classList.remove('hidden')
        document.querySelector('.mask').style.display = 'none'
        modal.style.display = 'none'
    })
      area = document.querySelector('div.mask')
      area.addEventListener('click', function() {
	document.querySelector('body').classList.remove('hidden')
	document.querySelector('.mask').style.display = 'none'
	modal.style.display = 'none'
      })
  })
  })
}

calendarDayModal()

jQuery(document).ready(function($){
   
  /* toggle nav */
  $(".calendar__filter-btn").on("click", function(){
    if ($('button.btn-orange').text() == 'Сбросить') {
      $('.calendar__filter-block').css({'top': '25%'});
    } else {
      $('.calendar__filter-block').css('top', '5%')
    }
    $(".calendar__filter-block").slideToggle();
    $(this).toggleClass("calendar-filter__list");
    $('.filter-modal-cross').on('click', function() {
      document.querySelector('.calendar__filter-block').style.display = 'none';
    })
  });
   
});
