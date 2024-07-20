import pandas as pd

class Person:
    def __init__(self, person_id, first_name, middle_name, last_name, job_title, person_city, person_state, person_country, email_pattern, homepage_base_url, duration_in_current_job, duration_in_current_company):
        self.person_id = person_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.job_title = job_title
        self.person_city = person_city
        self.person_state = person_state
        self.person_country = person_country
        self.email_pattern = email_pattern
        self.homepage_base_url = homepage_base_url
        self.duration_in_current_job = duration_in_current_job
        self.duration_in_current_company = duration_in_current_company

    @staticmethod
    def load_data(file_path):
        return pd.read_csv(file_path)
