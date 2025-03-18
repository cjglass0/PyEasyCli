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