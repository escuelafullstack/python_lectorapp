from datetime import datetime
import pytz

dt = datetime(2020, 7, 1, 12)
t = pytz.timezone("America/Lima")
t_la = pytz.timezone("America/Los_Angeles")

dt = t.localize(dt)
print(dt)

dt_utc = dt.astimezone(pytz.UTC)
print(dt_utc)

dt_los_angeles = dt.astimezone(t_la)
print(dt_los_angeles)