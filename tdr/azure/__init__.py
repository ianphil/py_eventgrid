#!/usr/bin/env python
import os
import sys
import time
from azure.common.credentials import ServicePrincipalCredentials

subscription_id = os.getenv("SUBSCRIPTIONID")
client_id = os.getenv("AZURE_CLIENT_ID")
client_secret = os.getenv("AZURE_CLIENT_SECRET")
tenant_id = os.getenv("AZURE_TENANT_ID")

credentials = ServicePrincipalCredentials(
    client_id=client_id, secret=client_secret, tenant=tenant_id
)

def poll_for_complete(result):
    while result.done() is False:
        time.sleep(1)
