from tests.utils.TestClient import TestClient


class Get:
    class Returns200:
        def when_default_request(self, app):
            # given
            auth_request = TestClient(app.test_client())

            # when
            response = auth_request.get('/health')

            print(response)

            # then
            assert response.status_code == 200
