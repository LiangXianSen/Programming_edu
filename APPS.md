#  apps directory
+ create new python package
```
move your apps to apps\
```

+ mark apps as source root
```
if you use pycharm right click the directory and mark it as source root
```
+ add path in setting.py
```python
import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
```

