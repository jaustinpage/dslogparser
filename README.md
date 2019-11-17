# dslog
Python parser for FRC DSLog files.

install dslog
```shell
pip install dslog
# or
pip install git+https://github.com/jaustinpage/dslog
```


Then, in python:

```python

events = dslog.DSEventParser('/path/to/my/2018_07_27_08_25_26 Fri.dsevents')
for t, rec in events.read_records():
    print(t, rec)

logs = dslog.DSLogParser('/path/to/my/2018_07_27_08_25_26 Fri.dslog')
for rec in logs.read_records():
    print(rec)

```

# Reference Sources:
  https://www.chiefdelphi.com/t/alternate-viewer-for-driver-station-logs-dslog/120629

  https://www.chiefdelphi.com/forums/showthread.php?p=1556451

Particularly:
  https://www.chiefdelphi.com/forums/showpost.php?p=1556451&postcount=11
  
