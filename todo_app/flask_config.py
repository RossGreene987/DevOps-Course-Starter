import os


class Config:
    def __init__(self):
        """Base configuration variables."""
        self.TRELLO_BOARD_ID = os.environ.get("TRELLO_BOARD_ID")
        self.TRELLO_API_KEY = os.environ.get("TRELLO_API_KEY")
        self.TRELLO_TOKEN = os.environ.get("TRELLO_TOKEN")

        if not (self.TRELLO_BOARD_ID and self.TRELLO_API_KEY and self.TRELLO_TOKEN):
            raise ValueError(
                "Missing Trello config. Did you follow the setup instructions?"
            )
