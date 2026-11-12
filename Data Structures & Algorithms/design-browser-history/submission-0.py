class Webpage:
    def __init__(self, url: str):
        self.url = url

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.historyLen = 1
        self.historyIdx = 0
        initPage = Webpage(homepage)
        self.history.append(initPage)

    def visit(self, url: str) -> None:
        newPage = Webpage(url)
        if self.historyIdx == len(self.history) - 1:
            self.history.append(newPage)
        else:
            self.history[self.historyIdx + 1] = newPage
            
        self.historyIdx += 1
        self.historyLen = self.historyIdx + 1

    def back(self, steps: int) -> str:
        resIdx = self.historyIdx - steps

        if resIdx <= 0:
            resIdx = 0
        
        self.historyIdx = resIdx

        return self.history[resIdx].url

    def forward(self, steps: int) -> str:
        resIdx = self.historyIdx + steps

        if resIdx >= self.historyLen:
            resIdx = self.historyLen - 1

        self.historyIdx = resIdx

        return self.history[resIdx].url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)