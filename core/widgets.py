from enum import Enum

class LayoutType(Enum):
    FREE = 0
    HORIZONTAL = 1
    VERTICAL = 2

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
        self.layout_type = LayoutType.HORIZONTAL
        # TODO alignment?
        #   left, center, right
        #   top, center, bottom
        self.title = ''
        self.data = None
        self.viewport_x = 0
        self.viewport_y = 0

    def add_child(self, child:'Container'):
        x_offset = 0
        y_offset = 0

        if self.layout_type == LayoutType.HORIZONTAL:
            x_offset = self.get_children_width()
        elif self.layout_type == LayoutType.VERTICAL:
            y_offset = self.get_children_height()

        child.x = x_offset
        child.y = y_offset

        self.children.append(child)
        child.parent = self

    def remove_child(self, child):
        self.children.remove(child)
        child.parent = None

    def apply_layout(self, layout:LayoutType):
        self.layout_type = layout
        
        current_children = self.children
        self.children = []
        for child in current_children:
            self.add_child(child)

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
    
    def get_children_width(self) -> int:
        width = 0
        for elem in self.children:
            child:Container = elem
            width += child.width
        return width
    
    def get_children_height(self) -> int:
        height = 0
        for elem in self.children:
            child:Container = elem
            height += child.height
        return height

class TextList(Container):
    def __init__(self):
        super().__init__()
        self.data = []
        self.content_character = '^'