# Import all essential libraries
import pandas as pd
import os
import json
import yaml
import requests
import sqlalchemy as db
import psycopg2
import numpy as np
import logging
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
# from dotenv import load_dotenv

