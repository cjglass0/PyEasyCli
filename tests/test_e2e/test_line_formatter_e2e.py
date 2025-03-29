import pytest

from core.widgets import Container
from formatters.formatter import LineContainerFormatter
from tests.test_utility import TestUtility

class TestLineFormatterEndToEnd:
    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_container_happy_path(self):
        container = Container()
        container.width = 5
        container.height = 5

        line_formatter = LineContainerFormatter()
        lines = line_formatter.format(container)

        expected_lines = [
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

    def test_container_border(self):
        container = Container()
        container.width = 5
        container.height = 5
        container.border_size = 0

        line_formatter = LineContainerFormatter()
        lines = line_formatter.format(container)

        expected_lines = [
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

        container.border_size = 1

        lines = line_formatter.format(container)

        expected_lines = [
            "#####",
            "#XXX#",
            "#XXX#",
            "#XXX#",
            "#####"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

    def test_container_padding(self):
        container = Container()
        container.width = 5
        container.height = 5
        container.padding_size = 0

        line_formatter = LineContainerFormatter()
        lines = line_formatter.format(container)

        expected_lines = [
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

        container.padding_size = 1

        lines = line_formatter.format(container)

        expected_lines = [
            "     ",
            " XXX ",
            " XXX ",
            " XXX ",
            "     "
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

    def test_container_border_padding(self):
        container = Container()
        container.width = 5
        container.height = 5
        container.border_size = 0
        container.padding_size = 0

        line_formatter = LineContainerFormatter()
        lines = line_formatter.format(container)

        expected_lines = [
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

        container.border_size = 1
        container.padding_size = 1

        lines = line_formatter.format(container)

        expected_lines = [
            "#####",
            "#   #",
            "# X #",
            "#   #",
            "#####"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

    def test_container_child(self):
        container = Container()
        container.width = 5
        container.height = 5
        
        child = Container()
        child.width = 4
        child.height = 4
        child.border_size = 1
        child.content_character = 'Z'

        container.add_child(child)

        line_formatter = LineContainerFormatter()
        lines = line_formatter.format(container)

        expected_lines = [
            "####X",
            "#ZZ#X",
            "#ZZ#X",
            "####X",
            "XXXXX"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

    def test_container_multiple_children(self):
        container:Container = TestUtility.create_container(0,0,5,5)
        
        child1:Container = TestUtility.create_container(0,0,1,1)
        child1.content_character = 'Z'

        child2:Container = TestUtility.create_container(0,0,2,1)
        child2.content_character = 'Y'

        container.add_child(child1)
        container.add_child(child2)

        line_formatter = LineContainerFormatter()
        lines = line_formatter.format(container)

        expected_lines = [
            "ZYYXX",
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

    def test_container_viewport_x(self):
        container:Container = TestUtility.create_container(0,0,5,5)
        
        child1:Container = TestUtility.create_container(0,0,1,1)
        child1.content_character = 'Z'

        child2:Container = TestUtility.create_container(0,0,2,1)
        child2.content_character = 'Y'

        container.add_child(child1)
        container.add_child(child2)

        line_formatter = LineContainerFormatter()
        lines = line_formatter.format(container)

        expected_lines = [
            "ZYYXX",
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

        container.viewport_x = 1
        lines = line_formatter.format(container)

        expected_lines = [
            "XZYYX",
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

        container.viewport_x = -1
        lines = line_formatter.format(container)

        expected_lines = [
            "YYXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

    def test_container_viewport_y(self):
        container:Container = TestUtility.create_container(0,0,5,5)
        
        child1:Container = TestUtility.create_container(0,0,1,1)
        child1.content_character = 'Z'

        child2:Container = TestUtility.create_container(0,0,2,1)
        child2.content_character = 'Y'

        container.add_child(child1)
        container.add_child(child2)

        line_formatter = LineContainerFormatter()
        lines = line_formatter.format(container)

        expected_lines = [
            "ZYYXX",
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

        container.viewport_y = 1
        lines = line_formatter.format(container)

        expected_lines = [
            "XXXXX",
            "ZYYXX",
            "XXXXX",
            "XXXXX",
            "XXXXX"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

        container.viewport_y = -1
        lines = line_formatter.format(container)

        expected_lines = [
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX",
            "XXXXX"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

    def test_container_viewport_margins(self):
        container:Container = TestUtility.create_container(0,0,8,8)
        container.border_size = 1
        container.padding_size = 1

        child1:Container = TestUtility.create_container(0,0,1,1)
        child1.content_character = 'Z'

        child2:Container = TestUtility.create_container(0,0,2,1)
        child2.content_character = 'Y'

        container.add_child(child1)
        container.add_child(child2)

        line_formatter = LineContainerFormatter()
        lines = line_formatter.format(container)

        expected_lines = [
            "########",
            "#      #",
            "# ZYYX #",
            "# XXXX #",
            "# XXXX #",
            "# XXXX #",
            "#      #",
            "########"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

        container.viewport_x = 1
        container.viewport_y = 1
        lines = line_formatter.format(container)

        expected_lines = [
            "########",
            "#      #",
            "# XXXX #",
            "# XZYY #",
            "# XXXX #",
            "# XXXX #",
            "#      #",
            "########"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

        container.viewport_x = -1
        lines = line_formatter.format(container)

        expected_lines = [
            "########",
            "#      #",
            "# XXXX #",
            "# YYXX #",
            "# XXXX #",
            "# XXXX #",
            "#      #",
            "########"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)

        container.viewport_x = 2
        lines = line_formatter.format(container)

        expected_lines = [
            "########",
            "#      #",
            "# XXXX #",
            "# XXZY #",
            "# XXXX #",
            "# XXXX #",
            "#      #",
            "########"
        ]

        TestUtility.assert_string_lists_match(lines, expected_lines)