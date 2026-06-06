#node
class node:
    def __init__(self, url):
        self.url=url
        self.prev=None
        self.next=None

class BrowserNavigation:
    def __init__(self,home):
        self.current=node(home)

    def visit(self, url):
        new_node = node(url)
        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node

    def back(self, steps):
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps):
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.url

    def __str__(self):
        temp = self.current
        while temp.prev:
            temp = temp.prev
        
        result = []
        while temp:
            if temp == self.current:
                result.append(f"[{temp.url}]")
            else:
                result.append(temp.url)
            temp = temp.next
        return " <-> ".join(result)

if __name__ == "__main__":
    browser = BrowserNavigation("google.com")
    browser.visit("github.com")
    browser.visit("stackoverflow.com")
    print(f"History: {browser}")
    browser.back(1)
    print(f"After back(1): {browser}")
    browser.forward(1)
    print(f"After forward(1): {browser}")
    browser.back(2)
    print(f" after 2 back : {browser}")