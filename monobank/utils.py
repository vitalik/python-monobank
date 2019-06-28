import time


def to_timestamp(dtime):
    "Converts datetime to utc timestamp"
    return int(time.mktime(dtime.timetuple()))
