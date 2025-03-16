from datetime import *
x = datetime.now()

f = x - timedelta(days=5)
m = f.replace(microsecond=0)
hb = datetime(2007, 5, 15)
now = datetime(2025, 3, 14)
dif = now - hb
total = dif.total_seconds()
print(m)
print(total)