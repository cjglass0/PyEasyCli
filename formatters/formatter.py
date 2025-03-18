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
                content_string = self.get_content_string(container, row)
                if len(content_string) > container.get_content_width():
                    content_string = content_string[:container.get_content_width()]
                result += content_string

            # right padding
            result += container.padding_character * container.padding_size

        # right border
        result += container.border_character * container.border_size

        return result
    
    def get_content_string(self, container:Container, row:int) -> str:
        if container.row_in_content(row):
            return container.content_character * container.get_content_width()
        return ""