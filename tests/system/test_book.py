import json

from tests.base_test import BaseTest, URL


class TestBookID(BaseTest):
    def test_get_not_found(self):
        with self.app_context():
            with self.app() as client:
                pass