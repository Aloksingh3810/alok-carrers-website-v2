from dataclasses import asdict


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
def load_job_from_db(id):
    with engine.connect()as conn:

        result = conn.execute(
         text(f"SELECT * FROM jobs WHERE id = {id}")
        )


        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return (rows[0]._asdict())


from sqlalchemy.sql import text

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        # Remove the space between the colon and placeholder
        query = text(
            "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, experience, resume_url) "
            "VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :experience, :resume_url)"
        )

        # Define the parameters as a dictionary
        parameters = {
            "job_id":job_id,
            "full_name": data['full_name'],
            "email": data['email'],
            "linkedin_url": data['linkedin_url'],
            "education": data['education'],
            "experience": data['experience'],
            "resume_url": data['resume_url']
        }

        # Execute the query with the parameters
        conn.execute(query, parameters)

        conn.commit()


