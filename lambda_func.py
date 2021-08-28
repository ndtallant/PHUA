"""
lambda_func.py
--------------

Author: Nick Tallant 

This file contains a Lambda function that: 
  1. Receives an event of high CPU utilization of an RDS Postgresql instance from an SNS topic.
  2. Queries the RDS Postgresql instance for active queries.
  3. Emails that query information to selected emails.
"""


def event_handler(event, context=None):
    """Receives an event, queries the DB, and emails out revelant information.

    """

    # Maybe get relevant info from event?

    return


def query_information():
    pass


def email_results():
    pass

