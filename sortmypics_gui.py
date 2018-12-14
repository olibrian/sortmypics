from appJar import gui
from sortmypics import SortMyPics

def press(btn):
        print(app.getEntry("d1"))
	
app=gui()


app.setTitle("sortmypics")
app.addLabel("title", "Welcome to sortmypics")
app.addDirectoryEntry("d1")
app.addDirectoryEntry("d2")

app.addButton("Sort", press)

app.go()

