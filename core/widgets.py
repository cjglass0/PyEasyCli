class Container:
    def __init__(self):
        self.children = []
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.parent = None
        self.border_size = 0
        self.padding_size = 0
        self.border_character = '#'
        self.padding_character = ' '
        self.content_character = 'X'
        # TODO layout types?
        #   free, horizontal, vertical
        # TODO alignment?
        #   left, center, right
        #   top, center, bottom
        self.title = ''
        self.data = None
        self.viewport_x = 0
        self.viewport_y = 0

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def remove_child(self, child):
        self.children.remove(child)
        child.parent = None

    def get_margin_size(self):
        return self.border_size + self.padding_size
    
    def get_content_width(self):
        return self.width - self.get_margin_size()*2
    
    def get_content_height(self):
        return self.height - self.get_margin_size()*2
    
    def row_in_border(self, row:int) -> bool:
        if row < 0 or row >= self.height:
            return False
        return row < self.border_size or row >= self.height - self.border_size
    
    def row_in_padding(self, row:int) -> bool:
        if row < 0 or row >= self.height:
            return False
        return not self.row_in_border(row) and (row < self.border_size + self.padding_size or row >= self.height - self.border_size - self.padding_size)
    
    def row_in_content(self, row:int) -> bool:
        if row < 0 or row >= self.height:
            return False
        return not self.row_in_border(row) and not self.row_in_padding(row)

class TextList(Container):
    def __init__(self):
        super().__init__()
        self.data = []
        self.content_character = '^'