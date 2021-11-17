"""
lambda_func.py
--------------

Author: Nick Tallant 

This file contains a Lambda function that: 
  1. Receives an event of high CPU utilization of an RDS Postgresql instance from an SNS topic.
  2. Queries the RDS Postgresql instance for active queries.
  3. Logs that query information for analysis. 
"""
import os
import json
import psycopg2

psql_args = {
    k: os.environ[k] for k in ["dbname", "user", "password", "host", "port"]
}

def event_handler(event=None, context=None):
    """Sends out activity stats from PG catalog when receiving an event."""

    data = None
    with psycopg2.connect(**psql_args) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT sa.* FROM pg_catalog.pg_stat_activity sa;")
            data = cur.fetchall()
            names = [d[0] for d in cur.description]
    assert data, "No data returned from high utilization query"

    db_stats = [dict(zip(names, row)) for row in data]

    # stdout goes to Lambda logs.
    print(db_stats)

    return {"status": 200, "body": json.dumps(db_stats, default=str)}

