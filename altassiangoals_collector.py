import requests
import json
from requests.auth import HTTPBasicAuth
import os
from datetime import datetime
import re
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
        if goal_response.status_code == 404:
            print(f"[ERROR] Goal ID '{goal_id}' not found at {goal_url}")
            return None
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
        print(f"HTTP error occurred for goal '{goal_id}': {http_err}")
        if hasattr(http_err, 'response') and http_err.response is not None:
            print(f"Response content: {http_err.response.content}")
        return None
    except Exception as err:
        print(f"Other error occurred for goal '{goal_id}': {err}")
        return None

def get_multiple_goals_data(goal_ids, api_token=None, email=None):
    results = []
    for goal_id in goal_ids:
        data = get_atlassian_goal_data(goal_id.strip(), api_token, email)
        results.append(data)
    return results

def extract_goal_id_from_url(url):
    match = re.search(r'/project/([A-Z0-9-]+)/about', url)
    if match:
        return match.group(1)
    return url  # fallback: return as-is if not a URL

def get_project_info(project_key, api_token=None, email=None):
    """Fetch Jira project info using the Jira Cloud REST API."""
    if not api_token:
        api_token = os.environ.get('ATLASSIAN_API_TOKEN')
    if not email:
        email = os.environ.get('ATLASSIAN_EMAIL')
    if not api_token or not email:
        raise ValueError("API token and email are required. Provide them as parameters or set as environment variables.")
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    url = f"https://natwest.atlassian.net/rest/api/3/project/{project_key}"
    response = requests.get(url, auth=HTTPBasicAuth(email, api_token), headers=headers)
    if response.status_code == 404:
        print(f"[ERROR] Project '{project_key}' not found at {url}")
        return None
    response.raise_for_status()
    return response.json()

def get_goals_for_project(project_key, org_id, site_id, api_token=None, email=None):
    """Fetch all goals associated with a project (if supported by your Atlassian instance)."""
    if not api_token:
        api_token = os.environ.get('ATLASSIAN_API_TOKEN')
    if not email:
        email = os.environ.get('ATLASSIAN_EMAIL')
    if not api_token or not email:
        raise ValueError("API token and email are required. Provide them as parameters or set as environment variables.")
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    # This endpoint may need to be adjusted for your instance
    url = f"https://api.atlassian.com/goals/1.0/organizations/{org_id}/sites/{site_id}/projects/{project_key}/goals"
    response = requests.get(url, auth=HTTPBasicAuth(email, api_token), headers=headers)
    if response.status_code == 404:
        print(f"[ERROR] No goals found for project '{project_key}' at {url}")
        return []
    response.raise_for_status()
    return response.json().get('values', [])

if __name__ == "__main__":
    # Accept a project key or project URL from user input
    project_input = input("Enter a Jira project key or project URL: ")
    # Extract project key from URL if needed
    match = re.search(r'/project/([A-Z0-9-]+)/about', project_input)
    if match:
        project_key = match.group(1)
    else:
        project_key = project_input.strip()

    # Fetch project info
    project_info = get_project_info(project_key)
    if not project_info:
        exit(1)
    print(f"\nProject: {project_info.get('name', 'N/A')}")
    print(f"Project Key: {project_info.get('key', 'N/A')}")
    print(f"Project Description: {project_info.get('description', {}).get('plain', {}).get('value', 'N/A') if isinstance(project_info.get('description'), dict) else project_info.get('description', 'N/A')}")

    # Set org_id and site_id (hardcoded as before)
    org_id = "b9427kk9-4caa-1ka6-7jj5-c777aa87a1aa"
    site_id = "66dac687-c07e-4919-9fec-8ed98e6c14ec"

    # Fetch all goals for the project
    goals = get_goals_for_project(project_key, org_id, site_id)
    if not goals:
        print("No goals found for this project.")
        exit(0)

    for goal in goals:
        goal_id = goal.get('id')
        if not goal_id:
            continue
        goal_data = get_atlassian_goal_data(goal_id)
        if not goal_data:
            continue
        details = goal_data['goal_details']
        print(f"\nGoal: {details.get('name', 'N/A')}")
        print(f"Start Date: {details.get('startDate', 'N/A')}")
        print(f"End Date: {details.get('endDate', 'N/A')}")
        print("Teams:")
        for team in goal_data["teams"]:
            print(f"- {team.get('name', 'N/A')}")