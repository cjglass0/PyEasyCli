from core.widgets import Container

class TestUtility:
    def create_container(x:int, y:int, width:int, height:int) -> Container:
        container = Container()
        container.x = x
        container.y = y
        container.width = width
        container.height = height
        return container
    
    def assert_string_lists_match(list1:list, list2:list):
        if len(list1) != len(list2):
            assert False
        for i in range(0, len(list1)):
            assert list1[i] == list2[i]