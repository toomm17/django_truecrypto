const date = new Date()
const monthsArray = JSON.parse(document.getElementById('months').textContent)
const allDates = JSON.parse(document.getElementById('dates').textContent)
const deadlineDates = JSON.parse(document.getElementById('deadline_dates').textContent)
const prevBtn = document.getElementById('prev_link')
const nextBtn = document.getElementById('next_link')


const ruDictMonths = {
    0: {'single': 'Январь', 'multiple': 'Января'}, 
    1: {'single': 'Февраль', 'multiple': 'Февраля'}, 
    2: {'single': 'Март', 'multiple': 'Марта'}, 
    3: {'single': 'Апрель', 'multiple': 'Апреля'}, 
    4: {'single': 'Май', 'multiple': 'Мая'}, 
    5: {'single': 'Июнь', 'multiple': 'Июня'}, 
    6: {'single': 'Июль', 'multiple': 'Июля'}, 
    7: {'single': 'Август', 'multiple': 'Августа'}, 
    8: {'single': 'Сентябрь', 'multiple': 'Сентября'}, 
    9: {'single': 'Октябрь', 'multiple': 'Октября'}, 
    10: {'single': 'Ноябрь', 'multiple': 'Ноября'}, 
    11: {'single': 'Декабрь', 'multiple': 'Декабря'}, 
}

for (const [key, value] of Object.entries(ruDictMonths)) {
    if (monthsArray.indexOf(parseInt(key)) < 0) {
        delete ruDictMonths[key]
    }
};

function formatUrl(strDate) {
    let list = strDate.split(' ')
    const formatUrlDict = {
        'Января': 1,
        'Февраля': 2,
        'Марта': 3,
        'Апреля': 4,
        'Мая': 5,
        'Июня': 6,
        'Июля': 7,
        'Августа': 8,
        'Сентября': 9,
        'Октября': 10,
        'Ноября': 11,
        'Декабря': 12
    }
    let month = formatUrlDict[list[list.length-1]]
    console.log(month)
    let year = date.getFullYear()
    const currentYearMonths = ['Ноября', 'Декабря']
    if (currentYearMonths.indexOf(list[list.length - 1]) >= 0){
        return `${year}-${month}-${list[0]}/`
    } else {
        return `${year + 1}-${month}-${list[0]}/`
    }

}

const renderCalendar = () => {
    const monthDay = document.querySelector('div.calendar__months')
    const countDays = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate()

    // Удаляем прошедшие дни в текущем месяце
    const checkedTags = document.querySelectorAll('.checkbox-active')
    let i = 1
    checkedTags.forEach(li => {
        let input = li.querySelector('.filter-list__input')
        if (input.value == 'uniqueOn') {
            if (new Date().getMonth() == date.getMonth()) {
                i = date.getDate()
            } else {
                i = 1
            }
        } else {
            i = 1
        }
    })

    document.getElementById('getMonth').textContent = ruDictMonths[date.getMonth()]['single']
    
    let days = ''
    console.log(allDates, deadlineDates)
    for (i; i <= countDays; i++) {
        if ((new Date().getMonth() == date.getMonth() && i < date.getDate()) || (new Date().getMonth() - 1 == date.getMonth())) {
            card_class = 'calendar-months__block calendar-red'
        } else {
            card_class = 'calendar-months__block'
        }
        let formatDate = `${i.toString()} ${ruDictMonths[date.getMonth()]['multiple']}`
        console.log(formatDate)
        if (deadlineDates.indexOf(formatDate) >= 0){
            card_class = 'calendar-months__block calendar-orange'
        }
        if (allDates.indexOf(formatDate) >= 0) {
            card_class = 'calendar-months__block calendar-green'
        }
        days += `<a href="${date.getFullYear()}-${date.getMonth() + 1}-${i}/" class="${card_class}">${formatDate}</a>`
        monthDay.innerHTML = days
    }

    
    let indexForPrevBtn = 0
    if (date.getMonth() == 0) {
        indexForPrevBtn + 11 
    } else {
        indexForPrevBtn = date.getMonth() - 1 
    }

    if (monthsArray.indexOf(indexForPrevBtn) < 0) {
        prevBtn.hidden = true
        $('.calendar-filter__btn').prop('disabled', false)
        $('.calendar-filter__btn').css('color', 'white')
    }

    let indexForNextBtn = 0
    if (date.getMonth() == 0) {
        indexForNextBtn + 1 
    } else {
        indexForPrevBtn = date.getMonth() + 1 
    }
    if (monthsArray.indexOf(indexForNextBtn) < 0) {
        nextBtn.hidden = true
        $('.calendar-filter__btn').prop('disabled', false)
        $('.calendar-filter__btn').css('color', 'white')
        $('div.checkbox-item').each(function() {
            this.style.pointerEvents = 'auto' 
        })
    }

}

nextBtn.addEventListener('click', () => {
    date.setMonth(date.getMonth() + 1)
    renderCalendar()
    console.log(date.getMonth(), new Date().getMonth())
    if (date.getMonth() != new Date().getMonth()) {
        $('.filter-list__item').removeClass('checkbox-active');
        $('.calendar-filter__btn').html('Найти')
        $('.calendar-filter__btn').prop('disabled', true)
        $('.calendar-filter__btn').css('color', 'grey')    
    } 
    prevBtn.hidden = false;
    const newMonthIndex = new Date(date.getFullYear(), date.getMonth() + 1, 1)
    if (monthsArray.indexOf(newMonthIndex.getMonth()) < 0) {
        nextBtn.hidden = true
    }
})

prevBtn.addEventListener('click', () => {
    date.setMonth(date.getMonth() - 1)
    renderCalendar()
    if (date.getMonth() != new Date().getMonth()) {
        $('.filter-list__item').removeClass('checkbox-active');
        $('.calendar-filter__btn').html('Найти')
        $('.calendar-filter__btn').prop('disabled', true)
        $('.calendar-filter__btn').css('color', 'grey')    
        $('.filter-list__item').removeClass('checkbox-active');
        $('.calendar-filter__btn').html('Найти')
        $('div.checkbox-item').each(function() {
            this.style.pointerEvents = 'none' 
        })
    }
    nextBtn.hidden = false
})

function fliterCheckboxEvents(){
  let checkboxItems = document.querySelectorAll('.filter-list__item');

  checkboxItems.forEach(li => {
    li.querySelector('.checkbox-item').addEventListener('click', function(){
      let input = li.querySelector('.filter-list__input');
      this.parentElement.classList.toggle('checkbox-active')
      if (input.checked == false){
        input.checked = 'true'
        if (input.value == 'uniqueOn') {
            renderCalendar()
        }
        numCounterInTheFilterUl()
      } else if (input.checked){
        input.checked = ''
        if (input.value == 'uniqueOn') {
            renderCalendar()
        }
        numCounterInTheFilterUl()
      }
      
    })
  });
}
fliterCheckboxEvents()

function numCounterInTheFilterUl(){
    document.querySelectorAll('.filter-list').forEach(list => {
      let countActiveItems = list.querySelectorAll('.checkbox-active').length;
      list.querySelector('.filter-list__title > span').innerText = countActiveItems
    })
  }

const searchBtn = document.querySelector('.calendar-filter__btn')
searchBtn.addEventListener('click', function() {
    const checkedTags = document.querySelectorAll('.checkbox-active')
    let arr = ''
    checkedTags.forEach(li => {
        let input = li.querySelector('.filter-list__input')
        if (input.value != 'uniqueOn') {
            arr += `${input.value},`
        }
    })
    
    if (searchBtn.textContent == 'Найти') {
        $.ajax({
            method: 'GET',
            url: 'tags-date',
            dataType: 'json',
            data: {
             'tags': arr
            },
            success: function(response) {
                if (document.body.clientWidth <= 768){
                    document.querySelector('.calendar__filter-block').style.display = 'none';
                }
                $('.calendar-months__block').remove()
                var dates = Array.from(new Set(response.tags.split(',')))
                dates.pop(-1)
                dates.forEach(date => {
                    $('div.calendar__months').append(
                        '<a href="'+ formatUrl(date) + '" class="calendar-months__block calendar-green">'+ date + '</a>')
                })
                $('.calendar-filter__btn').html('Сбросить')
                $('div.checkbox-item').each(function() {
                    this.style.pointerEvents = 'none' 
                })
            }
        })
    } else {
        $('.filter-list__item').removeClass('checkbox-active');
        $('.calendar-filter__btn').html('Найти')
        $('div.checkbox-item').each(function() {
            this.style.pointerEvents = 'auto' 
        })
        renderCalendar()
    }

})


numCounterInTheFilterUl()

renderCalendar()
