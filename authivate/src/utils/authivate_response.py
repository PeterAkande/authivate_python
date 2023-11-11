class AuthivateResponse:
    def __init__(self, status_code: int, json_data: dict):
        self.status_code = status_code
        self.json_data = json_data

        # Only successful for status codes lesser than 300 but equal to
        # Or greater than 200 (200 - 299)
        self.was_successful = 200 <= status_code < 300
        self.message = json_data.get('message', None)
