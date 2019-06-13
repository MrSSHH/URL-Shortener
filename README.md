# URL Shortener
 URL Shortener is a project that shorts URLS.

## Installation
Use [pip](https://pip.pypa.io/en/stable/) to install the requirements (use pip inside of folder installation)

```bash
pip install -f requirements.txt
```


## Usage
Start up the handler 

After the handler is running, import the url.py
```python
from url import url

# Creating an URL object
link = url("https://github.com/MrSSHH") # Pass the URL
link.short() # Returns a shorted version of a link.
```



## License
[MIT](https://choosealicense.com/licenses/mit/)
