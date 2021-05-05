# widget.bind(event, handler)
# widget.focus()

def downer(event, entry):
    widget = str(event.widget)
    i = int(widget[1])
    j = int(widget[2])
    if i < 8:
        entry[i+1][j]['obj'].focus()

def upper(event, entry):
    widget = str(event.widget)
    i = int(widget[1])
    j = int(widget[2])
    if i > 0:
        entry[i-1][j]['obj'].focus()

def righter(event, entry):
    widget = str(event.widget)
    i = int(widget[1])
    j = int(widget[2])
    if j < 8:
        entry[i][j+1]['obj'].focus()

def lefter(event, entry):
    widget = str(event.widget)
    i = int(widget[1])
    j = int(widget[2])
    if j > 0:
        entry[i][j-1]['obj'].focus()        