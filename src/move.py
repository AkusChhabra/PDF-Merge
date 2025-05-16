"""

Supporting class to handle row movement.

"""

class move:
    def shiftDown(self, event):
        self.tv = event
        select = [self.tv.widget.index(s) for s in self.tv.widget.selection()]
        select.append(self.tv.widget.index(self.tv.widget.identify_row(self.tv.y)))
        select.sort()
        for i in range(select[0],select[-1]+1,1):
            self.tv.widget.selection_add(self.tv.widget.get_children()[i])

    def down(self, event):
        self.tv = event
        if self.tv.widget.identify_row(self.tv.y) not in self.tv.widget.selection():
            self.tv.widget.selection_set(self.tv.widget.identify_row(self.tv.y))    

    def up(self, event):
        self.tv = event
        if self.tv.widget.identify_row(self.tv.y) in self.tv.widget.selection():
            self.tv.widget.selection_set(self.tv.widget.identify_row(self.tv.y))    

    def moveR(self, event):
        self.tv = event
        moveto = self.tv.widget.index(self.tv.widget.identify_row(self.tv.y))    
        for s in self.tv.widget.selection():
            self.tv.widget.move(s, "", moveto)
    
    def shiftUp(self, event):
        pass