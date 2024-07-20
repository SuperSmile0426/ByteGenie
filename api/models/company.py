import pandas as pd

class Company:
    def __init__(self, company_id, company_name, company_industry, company_revenue, company_n_employees, company_phone, company_founding_year, company_address, company_overview, company_logo_url, company_logo_text, relation_to_event, event_url, homepage_url, linkedin_company_url, homepage_base_url, company_logo_url_on_event_page, company_logo_match_flag):
        self.company_id = company_id
        self.company_name = company_name
        self.company_industry = company_industry
        self.company_revenue = company_revenue
        self.company_n_employees = company_n_employees
        self.company_phone = company_phone
        self.company_founding_year = company_founding_year
        self.company_address = company_address
        self.company_overview = company_overview
        self.company_logo_url = company_logo_url
        self.company_logo_text = company_logo_text
        self.relation_to_event = relation_to_event
        self.event_url = event_url
        self.homepage_url = homepage_url
        self.linkedin_company_url = linkedin_company_url
        self.homepage_base_url = homepage_base_url
        self.company_logo_url_on_event_page = company_logo_url_on_event_page
        self.company_logo_match_flag = company_logo_match_flag

    @staticmethod
    def load_data(file_path):
        return pd.read_csv(file_path)
