import unittest
import docker_hello


class TestCase(unittest.TestCase):
    def setUp(self):
        docker_hello.app.config["TESTING"] = True
        self.app = docker_hello.app.test_client()

    def test_get_mainpage(self):
        page = self.app.post("/", data=dict(name="Moby Dock"))      
        assert page.status_code == 200
        assert "Hello" in str(page.data)
        assert "Moby Dock" in str(page.data)

    def test_html_escaping(self):
        page = self.app.post("/", data=dict(name='"><b>TEST</b><!--'))
        assert "<b>" not in str(page.data)


if __name__ == "__main__":
    unittest.main()
