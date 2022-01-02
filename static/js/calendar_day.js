const eventTime = document.querySelectorAll('span.calendar-day__time-nums');
let eventMap = new Map();

function counts() {
    eventTime.forEach(span => {
        let now = new Date();
        if (span.dataset.time != null) {
            let date = new Date(span.dataset.time);
            gap = date - now;

            let days = Math.floor(gap / 1000 / 60 / 60 / 24);
            let hours = Math.floor(gap / 1000 / 60 / 60);
            let minutes = Math.floor(gap / 1000 / 60) % 60;
            let seconds = Math.floor(gap / 1000) % 60;
            
            if (days == 0){
                // span.innerHTML = `${hours}:${minutes}:${seconds}`
            } else {
                let hoursWithDays = Math.floor(gap / 1000 / 60 / 60) % 24;
                // span.innerHTML = `${days}:${hoursWithDays}:${minutes}`
            }
        }     
        if (span.innerHTML.startsWith('-')){
            if (span.dataset.deadline != null) {
                let date = new Date(span.dataset.deadline)
                gap = date - now;

                let days = Math.floor(gap / 1000 / 60 / 60 / 24);
                let hours = Math.floor(gap / 1000 / 60 / 60);
                let minutes = Math.floor(gap / 1000 / 60) % 60;
                let seconds = Math.floor(gap / 1000) % 60;
                
                if (days == 0){
                    // span.innerHTML = `${hours}:${minutes}:${seconds}`
                } else {
                    let hoursWithDays = Math.floor(gap / 1000 / 60 / 60) % 24;
                    // span.innerHTML = `${days}:${hoursWithDays}:${minutes}`
                }
                document.querySelector('span.calendar-day__time-text').textContent = 'До конца'
                let div = span.parentElement.parentElement
                div.classList.remove('calendar-green')
                div.classList.add('calendar-orange')
            }
            
        } else {
            //setInterval(counts, 100000)
        }
    })
}

counts()
