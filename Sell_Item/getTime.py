from datetime import datetime

def getTime(widget):
    widget = widget.lower()
    
    if widget == 'year':
        return datetime.now().year
    
    elif widget == 'month':
        return datetime.now().month
    
    elif widget == 'day':
        return datetime.now().day
    
    elif widget == 'hour':
        return datetime.now().hour
    
    elif widget == 'minute':
        return datetime.now().minute
    
    elif widget == 'second':
        return datetime.now().second
    
    elif widget == 'date':
        date_now = '{0:02d}/{1:02d}/{2:d}'.format(datetime.now().day , datetime.now().month , datetime.now().year)
        return date_now
    
    elif widget == 'time':
        time_now = '{0:02d}:{1:02d}:{2:02d}'.format(datetime.now().hour , datetime.now().minute , datetime.now().second)
        return time_now

    elif widget == 'timeall':
        return datetime.now()
