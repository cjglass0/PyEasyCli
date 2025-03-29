from core.widgets import Container

class ContainerFormatter:
    def __init__(self):
        pass

    def format(self, container:Container) -> list:
        pass

class LineContainerFormatter(ContainerFormatter):
    def __init__(self):
        super().__init__()

    def format(self, container:Container) -> list:
        result = []
        for i in range(0, container.height):
            row_string = self.get_full_row_string(container, i)
            result.append(row_string)
        return result
    
    def get_full_row_string(self, container:Container, row:int) -> str:
        if row < 0 or row >= container.height:
            return ''
        
        result = ''

        # top and bottom borders
        if container.row_in_border(row):
            result += container.border_character * container.width
            return result
    
        # left border
        result += container.border_character * container.border_size

        # top and bottom padding
        if container.row_in_padding(row):
            result += container.padding_character * (container.width - container.border_size*2)
        
        if container.row_in_content(row):
            # left padding
            result += container.padding_character * container.padding_size

            # content, if there is space for it
            if container.get_content_width() > 0:
                y_adjusted_row = row - container.viewport_y
                content_string = self.get_content_string(container, y_adjusted_row)
                if container.viewport_x > 0:
                    # shift all content to the right
                    content_string = (container.content_character * container.viewport_x) + content_string
                elif container.viewport_x < 0:
                    # shift all content to the left
                    content_string = content_string[-container.viewport_x:] + (container.content_character * -container.viewport_x)
                if len(content_string) > container.get_content_width():
                    content_string = content_string[:container.get_content_width()]
                elif len(content_string) < container.get_content_width():
                    content_string = content_string + (container.content_character * (container.get_content_width() - len(content_string)))
                result += content_string

            # right padding
            result += container.padding_character * container.padding_size

        # right border
        result += container.border_character * container.border_size

        return result
    
    def get_content_string(self, container:Container, row:int) -> str:
        if container.row_in_content(row):
            if container.children is not None:
                children_row = ""
                for elem in container.children:
                    #TODO get container layout
                    child:Container = elem
                    children_row += self.get_full_row_string(child, row - container.get_margin_size())
                
                return children_row + (container.content_character * container.get_content_width())

            return container.content_character * container.get_content_width()
        return ""