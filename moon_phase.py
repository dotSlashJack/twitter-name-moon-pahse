import ephem
from datetime import date, timedelta, datetime

def get_phase():
    # get dates and visibilities for each date
    today = datetime.now()
    curr_date = today.strftime("%Y/%m/%d %H:%M:%S.%f")[:-4]

    ephem_date = ephem.date(curr_date)
    moon = ephem.Moon(ephem_date)
    visibility = moon.moon_phase # % visible
    perc_visible = visibility * 100

    yesterday = datetime.now() - timedelta(1)
    yesterdays_date = ephem.date(yesterday.strftime("%Y/%m/%d %H:%M:%S.%f")[:-4])
    yesterdays_moon = ephem.Moon(yesterdays_date)
    yesterdays_visibility_perc = yesterdays_moon.moon_phase * 100
    tomorrow = datetime.now() + timedelta(1)
    tomorrows_date = ephem.date(tomorrow.strftime("%Y/%m/%d %H:%M:%S.%f")[:-4])
    tomorrows_moon = ephem.Moon(tomorrows_date)
    tomorrows_visibility_perc = tomorrows_moon.moon_phase * 100

    # now get the moon phase
    if perc_visible < yesterdays_visibility_perc and perc_visible < tomorrows_visibility_perc:
            return "New"
    elif perc_visible > yesterdays_visibility_perc and perc_visible > tomorrows_visibility_perc:
        return "Full"
    elif perc_visible > yesterdays_visibility_perc:
        if abs(perc_visible-50) < abs(yesterdays_visibility_perc-50) and abs(perc_visible-50) < abs(tomorrows_visibility_perc-50):
            return "First Quarter"
        elif perc_visible < 50:
            return "Waxing Crescent"
        elif perc_visible > 50:
            return "Waxing Gibbous"
    elif perc_visible < yesterdays_visibility_perc:
        if abs(perc_visible-50) < abs(yesterdays_visibility_perc-50) and abs(perc_visible-50) < abs(tomorrows_visibility_perc-50):
            return "Last Quarter"
        elif perc_visible > 50:
            return "Waning Gibbous"
        elif perc_visible < 50:
            return "Waning Crescent"
    else:
        return "ERROR"

    #print(curr_date)
    #print(yesterdays_visibility_perc)
    #print(perc_visible)
    #print(tomorrows_visibility_perc)

#print(get_phase())
