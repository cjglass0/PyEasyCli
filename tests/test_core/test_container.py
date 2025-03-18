from core.widgets import Container
from tests.test_utility import TestUtility

class TestContainer:
    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_container_no_margin(self):
        container:Container = TestUtility.create_container(0, 0, 10, 10)
        assert container.get_margin_size() == 0

        assert not container.row_in_border(0)
        assert not container.row_in_border(1)
        assert not container.row_in_padding(0)
        assert not container.row_in_padding(1)

    def test_container_border_margin(self):
        container:Container = TestUtility.create_container(0, 0, 10, 10)
        container.border_size = 1
        assert container.get_margin_size() == 1

        assert container.row_in_border(0)
        assert not container.row_in_border(1)
        assert not container.row_in_padding(0)
        assert not container.row_in_padding(1)

    def test_container_padding_margin(self):
        container:Container = TestUtility.create_container(0, 0, 10, 10)
        container.padding_size = 1
        assert container.get_margin_size() == 1

        assert not container.row_in_border(0)
        assert not container.row_in_border(1)
        assert container.row_in_padding(0)
        assert not container.row_in_padding(1)

    def test_container_border_padding_margin(self):
        container:Container = TestUtility.create_container(0, 0, 10, 10)
        container.border_size = 1
        container.padding_size = 1
        assert container.get_margin_size() == 2

        assert container.row_in_border(0)
        assert not container.row_in_border(1)
        assert not container.row_in_padding(0)
        assert container.row_in_padding(1)

        assert container.row_in_border(9)
        assert not container.row_in_padding(9)
        assert container.row_in_padding(8)

    def test_container_in_content_no_margin(self):
        container:Container = TestUtility.create_container(0, 0, 10, 5)
        assert container.row_in_content(0)
        assert container.row_in_content(1)
        assert container.row_in_content(2)
        assert container.row_in_content(3)
        assert container.row_in_content(4)

    def test_container_in_content_border_margin(self):
        container:Container = TestUtility.create_container(0, 0, 10, 5)

        container.border_size = 1

        assert not container.row_in_content(0)
        assert container.row_in_content(1)
        assert container.row_in_content(2)
        assert container.row_in_content(3)
        assert not container.row_in_content(4)

    def test_container_in_content_padding_margin(self):
        container:Container = TestUtility.create_container(0, 0, 10, 5)

        container.padding_size = 1

        assert not container.row_in_content(0)
        assert container.row_in_content(1)
        assert container.row_in_content(2)
        assert container.row_in_content(3)
        assert not container.row_in_content(4)

    def test_container_in_content_border_padding_margin(self):
        container:Container = TestUtility.create_container(0, 0, 10, 5)

        container.border_size = 1
        container.padding_size = 1

        assert not container.row_in_content(0)
        assert not container.row_in_content(1)
        assert container.row_in_content(2)
        assert not container.row_in_content(3)
        assert not container.row_in_content(4)

    def test_container_no_content_border_padding_margin(self):
        container:Container = TestUtility.create_container(0, 0, 10, 5)

        container.border_size = 2
        container.padding_size = 1

        assert not container.row_in_content(0)
        assert not container.row_in_content(1)
        assert not container.row_in_content(2)
        assert not container.row_in_content(3)
        assert not container.row_in_content(4)