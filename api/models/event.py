import pandas as pd

class Event:
    def __init__(self, event_id, event_name, event_url, event_start_date, event_end_date, event_venue, event_country, event_description, event_logo_url):
        self.event_id = event_id
        self.event_name = event_name
        self.event_url = event_url
        self.event_start_date = event_start_date
        self.event_end_date = event_end_date
        self.event_venue = event_venue
        self.event_country = event_country
        self.event_description = event_description
        self.event_logo_url = event_logo_url

    @staticmethod
    def load_data(file_path):
        return pd.read_csv(file_path)
