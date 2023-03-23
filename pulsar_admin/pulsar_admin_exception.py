class PulsarAdminException(Exception):
    DEFAULT_STATUS_CODE = 500

    def __init__(self, message=None, status_code=None, cause=None):
        super().__init__(message, cause)
        self.status_code = status_code or PulsarAdminException.DEFAULT_STATUS_CODE
