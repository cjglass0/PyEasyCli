import pytest

from formatters.formatter import LineContainerFormatter

class TestLineFormatter:
    def test_overlay_string(self):
        base_string = 'abcde'
        start_index = 0
        overlay_string = '123'

        formatter = LineContainerFormatter()
        result = formatter.overlay_string(base_string, start_index, overlay_string)

        expected_result = '123de'
        assert result == expected_result

    def test_overlay_string_negative_index(self):
        base_string = 'abcde'
        start_index = -1
        overlay_string = '123'

        formatter = LineContainerFormatter()
        result = formatter.overlay_string(base_string, start_index, overlay_string)

        expected_result = '123cde'
        assert result == expected_result

    def test_overlay_string_positive_index(self):
        base_string = 'abcde'
        start_index = 1
        overlay_string = '123'

        formatter = LineContainerFormatter()
        result = formatter.overlay_string(base_string, start_index, overlay_string)

        expected_result = 'a123e'
        assert result == expected_result

    def test_overlay_string_after_bounds(self):
        base_string = 'abcde'
        start_index = 6
        overlay_string = '123'

        formatter = LineContainerFormatter()
        result = formatter.overlay_string(base_string, start_index, overlay_string)

        expected_result = 'abcde!123'
        assert result == expected_result

    def test_overlay_string_before_bounds(self):
        base_string = 'abcde'
        start_index = -6
        overlay_string = '123'

        formatter = LineContainerFormatter()
        result = formatter.overlay_string(base_string, start_index, overlay_string)

        expected_result = '123!!!abcde'
        assert result == expected_result

    def test_overlay_string_full_overlap(self):
        base_string = 'abcde'
        start_index = 0
        overlay_string = '123456'

        formatter = LineContainerFormatter()
        result = formatter.overlay_string(base_string, start_index, overlay_string)

        expected_result = '123456'
        assert result == expected_result

        start_index = -1
        result = formatter.overlay_string(base_string, start_index, overlay_string)

        expected_result = '123456'
        assert result == expected_result

    def test_overlay_string_extend_after(self):
        base_string = 'abcde'
        start_index = 3
        overlay_string = '1234'

        formatter = LineContainerFormatter()
        result = formatter.overlay_string(base_string, start_index, overlay_string)

        expected_result = 'abc1234'
        assert result == expected_result