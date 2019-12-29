# URL Shortener
URL Shortener Project
Honestly this project has been just sitting there.
This project will short any URL you will pass into it.

## Installation
Use [pip](https://pip.pypa.io/en/stable/) to install the requirements (use pip inside of folder installation)

```bash
pip install -f requirements.txt
```


## Usage
Open the handler.py file and switch the <your-ip> with your lan IP.
Then simply run handler.py.
After the handler is running, create a new python file and import url.py,
Type the following code:
```python
from url import url

# Creating an URL object
link = url("https://github.com/MrSSHH", host=<your-ip>) # Pass the URL
link.short() # Returns a shorted version of a link.
```



## License
[MIT](https://choosealicense.com/licenses/mit/)
