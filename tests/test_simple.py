from context import url

class OpenWebBrowser:
    def __init__(self, link):
        self.link = url(link).short()

    def open(self):
        print(f"Opening shorted link: {self.link}")
        webbrowser.open(self.link)


if __name__ == "__main__":
    import webbrowser
    site = OpenWebBrowser("https://stackoverflow.com/questions/21434332/how-to-extend-inheritance-a-module-in-python")
    site.open()
