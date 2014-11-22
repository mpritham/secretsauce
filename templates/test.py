class Entry:
    def __init__(self, title, path,description):
        self.title=title
        self.path=path
        self.description=description
#    def getTitle(self):
#        return self.title
#    def getDescription(self):
#        return self.description
#    def getPath(self):
#        return self.path
x= [Entry("test","test","test"),Entry("test","test","test")]
print x[0].title