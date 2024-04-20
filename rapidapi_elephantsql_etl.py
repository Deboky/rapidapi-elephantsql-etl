from common.utils import *


# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# load_dotenv()  # Load environment variables from a .env file
database_url = 'postgresql://url'

def fetch_data(url, query_params, headers):
    try:
        response = requests.get(url, headers=headers, params=query_params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        logging.info("Data fetched successfully from API.")
        return response.json()
    except requests.HTTPError as e:
        logging.error(f"HTTP error occurred: {e}")
        return None
    except requests.ConnectionError as e:
        logging.error(f"Connection error occurred: {e}")
        return None
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

def process_data(data):
    try:
        df = pd.DataFrame(data["data"])
        df.drop(columns=["working_hours", "photos", "description"], inplace=True)
        logging.info("Data processed successfully.")
        return df
    except Exception as e:
        logging.error(f"Error processing data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

def load_data(df, database_url):
    if df.empty:
        logging.warning("Empty DataFrame cannot be loaded into database.")
        return
    try:
        engine = db.create_engine(database_url)
        df.to_sql('searchmaps_data', engine, if_exists="replace", index=False)
        logging.info("Data loaded successfully into database.")
    except Exception as e:
        logging.error(f"Error loading data into database: {e}")

def rapidapi_elephantsql_etl():
    api_url = "https://maps-data.p.rapidapi.com/searchmaps.php"
    params = {
        "query": "restaurant", "limit": "20", "country": "uk",
        "lang": "en", "lat": "51.5072", "lng": "0.12",
        "offset": "0", "zoom": "13"
    }
    headers = {
        "X-RapidAPI-Key": "apy-key",
        "X-RapidAPI-Host": "maps-data.p.rapidapi.com"
    }
    raw_data = fetch_data(api_url, params, headers)
    if raw_data:
        processed_data = process_data(raw_data)
        load_data(processed_data, database_url=database_url)

if __name__ == "__main__":
    rapidapi_elephantsql_etl()
