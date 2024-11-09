import sqlalchemy
from sqlalchemy import create_engine, text

import os


db_connection_string = os.getenv('db_connection_string')





engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {"ca": "ca (1).pem"},  # Update to the actual path
    },
    pool_timeout=30 ) # Sets a timeout for connection attempts

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
  # This will show the structure of each job in the console
        return jobs




