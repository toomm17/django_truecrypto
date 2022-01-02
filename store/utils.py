def diff_dates(current_date: str, last_date: str) -> list:
    # 2022-1-8 - 2021-6-22 == [11, 12, 1]
    current_year, current_month, current_day = map(int, current_date.split('-'))
    last_year, last_month, last_day = map(int, last_date.split('-'))
    rtn_list = []  # list for return
    if last_year > current_year:
        for next_month in range(current_month, 12 + 1 + last_month):
            if next_month > 12:
                next_month -= 12
            rtn_list.append(next_month)
    else:
        for next_month in range(current_month, last_month + 1):
            rtn_list.append(next_month)

    return [i - 1 for i in rtn_list]  # for fucking js Date();


def ajax_renderer_date(date: str):
    #  date format: %Y-%m-%d
    months_ru = {
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
    year, month, day = map(int, date.split('-'))
    return f"{day} {months_ru[month-1]['multiple']}"
