import requests
import json
from requests.auth import HTTPBasicAuth
import os
from datetime import datetime
# Add dotenv support
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # If dotenv is not installed, print a helpful message
    print("[INFO] python-dotenv not installed. Install it with: pip install python-dotenv if you want to load .env files.")

def get_atlassian_goal_data(goal_id, api_token=None, email=None):
    """
    Retrieve goal data from Atlassian, including goals, teams, contributors, and Jira issues.
    
    Args:
        goal_id (str): The goal ID (e.g., 'NATWE-305')
        api_token (str, optional): Your Atlassian API token. If None, will look for ATLASSIAN_API_TOKEN env var
        email (str, optional): Your Atlassian email. If None, will look for ATLASSIAN_EMAIL env var
        
    Returns:
        dict: A dictionary containing the goal data with sections for:
            - goal_details
            - teams
            - contributors
            - jira_issues
    """
    # Use provided credentials or get from environment
    if not api_token:
        api_token = os.environ.get('ATLASSIAN_API_TOKEN')
    if not email:
        email = os.environ.get('ATLASSIAN_EMAIL')
        
    if not api_token or not email:
        raise ValueError("API token and email are required. Provide them as parameters or set as environment variables.")
    
    # Base URL for Atlassian API
    base_url = "https://api.atlassian.com"
    
    # Authenticate
    auth = HTTPBasicAuth(email, api_token)
    
    # Headers for API requests
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    # Extract organization ID and site ID from the URL format you provided
    # This is a simplification - you may need to adjust based on your actual URL structure
    org_id = "b9427kk9-4caa-1ka6-7jj5-c777aa87a1aa"
    site_id = "66dac687-c07e-4919-9fec-8ed98e6c14ec"
    
    # Initialize results dictionary
    results = {
        "goal_details": {},
        "teams": [],
        "contributors": [],
        "jira_issues": []
    }
    
    try:
        # 1. Get goal details
        goal_url = f"{base_url}/goals/1.0/organizations/{org_id}/sites/{site_id}/goals/{goal_id}"
        goal_response = requests.get(goal_url, auth=auth, headers=headers)
        goal_response.raise_for_status()
        results["goal_details"] = goal_response.json()
        
        # 2. Get teams associated with the goal
        teams_url = f"{base_url}/goals/1.0/organizations/{org_id}/sites/{site_id}/goals/{goal_id}/teams"
        teams_response = requests.get(teams_url, auth=auth, headers=headers)
        teams_response.raise_for_status()
        results["teams"] = teams_response.json().get("values", [])
        
        # 3. Get contributors for the goal
        contributors_url = f"{base_url}/goals/1.0/organizations/{org_id}/sites/{site_id}/goals/{goal_id}/contributors"
        contributors_response = requests.get(contributors_url, auth=auth, headers=headers)
        contributors_response.raise_for_status()
        results["contributors"] = contributors_response.json().get("values", [])
        
        # 4. Get Jira issues linked to the goal
        jira_issues_url = f"{base_url}/goals/1.0/organizations/{org_id}/sites/{site_id}/goals/{goal_id}/jira-issues"
        jira_response = requests.get(jira_issues_url, auth=auth, headers=headers)
        jira_response.raise_for_status()
        results["jira_issues"] = jira_response.json().get("values", [])
        
        return results
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response content: {http_err.response.content}")
        raise
    except Exception as err:
        print(f"Other error occurred: {err}")
        raise

# Example usage
if __name__ == "__main__":
    goal_id = "NATWE-305"
    
    # Option 1: Using environment variables
    # export ATLASSIAN_API_TOKEN="your_api_token"
    # export ATLASSIAN_EMAIL="your_email@example.com"
    
    # Option 2: Passing credentials directly
    # api_token = "your_api_token"
    # email = "your_email@example.com"
    
    goal_data = get_atlassian_goal_data(goal_id)
    
    # Print the results in a readable format
    print(f"Goal: {goal_data['goal_details'].get('name', 'N/A')}")
    print(f"Description: {goal_data['goal_details'].get('description', 'N/A')}")
    print(f"Status: {goal_data['goal_details'].get('status', 'N/A')}")
    
    print("\nTeams:")
    for team in goal_data["teams"]:
        print(f"- {team.get('name', 'N/A')}")
    
    print("\nContributors:")
    for contributor in goal_data["contributors"]:
        print(f"- {contributor.get('displayName', 'N/A')} ({contributor.get('email', 'N/A')})")
    
    print("\nJira Issues:")
    for issue in goal_data["jira_issues"]:
        print(f"- {issue.get('key', 'N/A')}: {issue.get('summary', 'N/A')}")