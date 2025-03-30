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
    
    def overlay_string(self, base_string:str, start_index:int, overlay_string:str, fill_char:str='!') -> str:
        visible_base_string = ""
        fill_string = ""
        # new idea: figure out the visible base string and if it goes before or after the overlay string
        if start_index >= len(base_string):
            # start index past base string
            visible_base_string = base_string
            fill_string = fill_char * (start_index - len(base_string))
            return visible_base_string + fill_string + overlay_string
        elif start_index + len(overlay_string) <= 0:
            # overlay ends before base string
            visible_base_string = base_string
            fill_string = fill_char * (-start_index - len(overlay_string))
            return overlay_string + fill_string + visible_base_string
        elif start_index <= 0 and start_index + len(overlay_string) > len(base_string):
            # overlay completely covers base string
            return overlay_string
        else:
            # base string is partially visible
            if start_index <= 0 and start_index + len(overlay_string) <= len(base_string):
                # overlay starts before base string, ends before base string does
                visible_base_string = base_string[start_index + len(overlay_string):]
                return overlay_string + visible_base_string
            elif start_index > 0 and start_index + len(overlay_string) > len(base_string):
                # overlay starts after base string, ends after base string does
                visible_base_string = base_string[:start_index]
                return visible_base_string + overlay_string
            else:
                # overlay starts and ends inside base string
                pre_string = base_string[:start_index]
                post_string = base_string[start_index + len(overlay_string):]
                return pre_string + overlay_string + post_string

    def get_content_string(self, container:Container, row:int) -> str:
        if container.row_in_content(row):
            if container.children is not None:
                children_row = ""
                for elem in container.children:
                    child:Container = elem
                    child_full_row = self.get_full_row_string(child, row - container.get_margin_size() - child.y)
                
                    children_row = self.overlay_string(children_row, child.x, child_full_row, container.content_character)
                    
                    # trim the front if necessary
                    if child.x < 0:
                        children_row = children_row[-child.x:]
                
                return children_row + (container.content_character * container.get_content_width())

            return container.content_character * container.get_content_width()
        return ""