def compare_day_night_demand(df, course):
    day_course_name = course + ' - Diurno'
    night_course_name = course + ' - Noturno'

    day_course_demand = df[df['Course'] == day_course_name]['Demand'].values
    night_course_demand = df[df['Course'] == night_course_name]['Demand'].values

    if not (day_course_demand.size or night_course_demand.size):
        return 'Course not found'
    elif not day_course_demand.size:
        return 'Day course not found'
    elif not night_course_demand.size:
        return 'Night course not found'
    elif day_course_demand > night_course_demand:
        return 'Day course has higher demand'
    elif day_course_demand < night_course_demand:
        return 'Night course has higher demand'
    else:
        return 'Same demand'
