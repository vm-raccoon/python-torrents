from requests_html import HTMLSession


class URI:

    def __init__(self, data, debug=False):
        self.id = data["id"]
        self.name = data["name"]
        self.uri = data["uri"]
        self.selector = data["selector"]
        self.value = data["value"]
        self.trash = data["trash"]

    def getUpdate(self):
        session = HTMLSession()
        page = session.get(self.uri)
        element = page.html.xpath(self.selector, first=True)
        try:
            text = element.text

            if "\n" in text:
                index = text.index("\n")
                text = text[0:index]
            return text
        except Exception as e:
            print(e)
            return self.value
