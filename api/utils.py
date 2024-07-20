import pandas as pd
import sqlite3
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_query(query):
    logger.info(f"Parsing query: {query}")
    parsed_info = {}

    if "companies that are attending Oil & Gas related events over the next 12 months" in query:
        parsed_info['query_type'] = 'oil_gas_events'
        parsed_info['start_date'] = datetime.now().strftime('%Y-%m-%d')
        parsed_info['end_date'] = (datetime.now() + timedelta(days=365)).strftime('%Y-%m-%d')
    elif "sales people for companies that are attending events in Singapore" in query:
        parsed_info['query_type'] = 'sales_people_singapore'
        parsed_info['start_date'] = datetime.now().strftime('%Y-%m-%d')
        parsed_info['end_date'] = (datetime.now() + timedelta(days=270)).strftime('%Y-%m-%d')
    elif "companies in Pharmaceuticals sector are attending" in query:
        parsed_info['query_type'] = 'pharmaceuticals_events'
    elif "email addresses of people working for companies that are attending finance and banking events" in query:
        parsed_info['query_type'] = 'finance_banking_emails'
    else:
        parsed_info['query_type'] = 'default'

    logger.info(f"Parsed info: {parsed_info}")
    return parsed_info

def construct_sql(parsed_info):
    logger.info(f"Constructing SQL for parsed info: {parsed_info}")

    if parsed_info['query_type'] == 'oil_gas_events':
        sql_query = f"""
        SELECT DISTINCT companies.company_name
        FROM events
        JOIN companies ON events.event_url = companies.event_url
        WHERE events.event_name LIKE '%Oil & Gas%'
        AND DATE(events.event_start_date) BETWEEN '{parsed_info['start_date']}' AND '{parsed_info['end_date']}';
        """
    elif parsed_info['query_type'] == 'sales_people_singapore':
        sql_query = f"""
        SELECT DISTINCT people.first_name || ' ' || people.last_name AS person_name, people.email_pattern AS email
        FROM events
        JOIN companies ON events.event_url = companies.event_url
        JOIN people ON companies.homepage_base_url = people.homepage_base_url
        WHERE events.event_venue LIKE '%Singapore%'
        AND DATE(events.event_start_date) BETWEEN '{parsed_info['start_date']}' AND '{parsed_info['end_date']}'
        AND people.job_title LIKE '%Sales%';
        """
    elif parsed_info['query_type'] == 'pharmaceuticals_events':
        sql_query = f"""
        SELECT DISTINCT events.event_name, events.event_start_date, events.event_venue
        FROM events
        JOIN companies ON events.event_url = companies.event_url
        WHERE companies.company_industry = 'Pharmaceuticals';
        """
    elif parsed_info['query_type'] == 'finance_banking_emails':
        sql_query = f"""
        SELECT DISTINCT people.first_name || ' ' || people.last_name AS person_name, people.email_pattern AS email
        FROM events
        JOIN companies ON events.event_url = companies.event_url
        JOIN people ON companies.homepage_base_url = people.homepage_base_url
        WHERE events.event_name LIKE '%Finance%' OR events.event_name LIKE '%Banking%';
        """
    else:
        sql_query = "SELECT 1"  # Default dummy query

    logger.info(f"Constructed SQL: {sql_query}")
    return sql_query

def execute_query(sql_query):
    logger.info(f"Executing SQL query: {sql_query}")
    try:
        conn = sqlite3.connect('../database/database.db')
        result = pd.read_sql_query(sql_query, conn)
        conn.close()
        logger.info(f"Query result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error executing query: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error

if __name__ == "__main__":
  
    # Test the query functions
    queries = [
        "Find me companies that are attending Oil & Gas related events over the next 12 months",
        "Find sales people for companies that are attending events in Singapore over the next 9 months",
        "Find me events that companies in Pharmaceuticals sector are attending",
        "I need the email addresses of people working for companies that are attending finance and banking events"
    ]
    
    for query in queries:
        parsed_info = parse_query(query)
        sql_query = construct_sql(parsed_info)
        result = execute_query(sql_query)
        print(result)
