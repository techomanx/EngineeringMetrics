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

from playwright.sync_api import sync_playwright

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

def get_atlassian_project_info(project_id, org_id, site_id, api_token=None, email=None):
    base_url = "https://api.atlassian.com"
    url = f"{base_url}/goals/1.0/organizations/{org_id}/sites/{site_id}/projects/{project_id}"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    if not api_token:
        api_token = os.environ.get('ATLASSIAN_API_TOKEN')
    if not email:
        email = os.environ.get('ATLASSIAN_EMAIL')
    auth = HTTPBasicAuth(email, api_token)
    response = requests.get(url, auth=auth, headers=headers)
    if response.status_code == 404:
        print(f"[ERROR] Project '{project_id}' not found at {url}")
        return None
    response.raise_for_status()
    return response.json()

def get_goals_for_project(project_id, org_id, site_id, api_token=None, email=None):
    base_url = "https://api.atlassian.com"
    url = f"{base_url}/goals/1.0/organizations/{org_id}/sites/{site_id}/projects/{project_id}/goals"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    if not api_token:
        api_token = os.environ.get('ATLASSIAN_API_TOKEN')
    if not email:
        email = os.environ.get('ATLASSIAN_EMAIL')
    auth = HTTPBasicAuth(email, api_token)
    response = requests.get(url, auth=auth, headers=headers)
    if response.status_code == 404:
        print(f"[ERROR] No goals found for project '{project_id}' at {url}")
        return []
    response.raise_for_status()
    return response.json().get('values', [])

def extract_goals_from_sidebar(url, email=None, password=None):
    if not email:
        email = os.environ.get('ATLASSIAN_EMAIL')
    if not password:
        password = os.environ.get('ATLASSIAN_PASSWORD')
    if not email or not password:
        raise ValueError("Email and password are required. Provide them as parameters or set as environment variables in .env (ATLASSIAN_EMAIL, ATLASSIAN_PASSWORD).")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        # --- Login if needed ---
        if "id.atlassian.com/login" in page.url:
            print("Logging in to Atlassian...")
            page.fill('input[type="email"]', email)
            page.click('button[type="submit"]')
            page.wait_for_timeout(2000)
            page.wait_for_selector('input[type="password"]', timeout=15000)
            page.fill('input[type="password"]', password)
            page.click('button[type="submit"]')
            page.wait_for_url(lambda url: "project" in url, timeout=60000)

        # Now wait for the sidebar to load
        page.wait_for_selector('aside.sc-EHOje.iBaHwQ', timeout=30000)

        # Extract all text from the sidebar
        sidebar = page.query_selector('aside.sc-EHOje.iBaHwQ')
        sidebar_text = sidebar.inner_text()
        print("Sidebar text:\n", sidebar_text)

        browser.close()

# Usage
extract_goals_from_sidebar(
    url="https://home.atlassian.com/o/b9427kk9-4caa-1ka6-7jj5-c777aa87a1aa/s/66dac687-c07e-4919-9fec-8ed98e6c14ec/project/NATWE-129/about"
)

if __name__ == "__main__":
    # Accept a project key or project URL from user input
    project_input = input("Enter an Atlassian project key or project URL: ")
    # Extract project_id from URL if needed
    match = re.search(r'/project/([A-Z0-9-]+)/about', project_input)
    if match:
        project_id = match.group(1)
    else:
        project_id = project_input.strip()

    # Set org_id and site_id (hardcoded as before)
    org_id = "b9427kk9-4caa-1ka6-7jj5-c777aa87a1aa"
    site_id = "66dac687-c07e-4919-9fec-8ed98e6c14ec"

    # Fetch project info from Atlassian Goals API
    project_info = get_atlassian_project_info(project_id, org_id, site_id)
    if not project_info:
        exit(1)
    print(f"\nProject: {project_info.get('name', 'N/A')}")
    print(f"Project ID: {project_info.get('id', 'N/A')}")
    print(f"Project Description: {project_info.get('description', 'N/A')}")

    # Fetch all goals for the project
    goals = get_goals_for_project(project_id, org_id, site_id)
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