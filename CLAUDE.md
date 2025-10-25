# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Python-based Atlassian Goals data collection tool that extracts project information, goals, teams, contributors, and Jira issues from Atlassian's API endpoints. The main script `altassiangoals_collector.py` provides functions to interact with Atlassian Goals API and scrape data using Playwright for authentication.

## Development Setup

### Environment Setup
1. Python 3.13+ required
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file with required credentials:
   ```
   ATLASSIAN_API_TOKEN=your_token_here
   ATLASSIAN_EMAIL=your_email@domain.com
   ATLASSIAN_PASSWORD=your_password_here
   ```

### Running the Script
- Main execution: `python altassiangoals_collector.py`
- The script prompts for project key or URL input
- Uses hardcoded org_id and site_id for the specific Atlassian instance

## Architecture

### Core Components

**altassiangoals_collector.py** - Main module containing:
- `get_atlassian_goal_data()` - Fetches goal details, teams, contributors, and Jira issues via REST API
- `get_atlassian_project_info()` - Retrieves project information from Atlassian Goals API
- `get_goals_for_project()` - Gets all goals associated with a project
- `extract_goals_from_sidebar()` - Web scraping function using Playwright for authentication and data extraction

### API Integration
- Uses Atlassian Goals API v1.0 endpoints
- HTTPBasicAuth authentication with email and API token
- Hardcoded organization and site IDs for specific instance
- Error handling for 404s and HTTP errors

### Dependencies
- `requests` - HTTP client for API calls
- `python-dotenv` - Environment variable management (optional)
- `playwright` - Web automation for authentication and scraping
- Standard library: `json`, `os`, `datetime`, `re`

### Data Structure
The tool extracts and organizes data into structured dictionaries containing:
- Goal details (name, dates, description)
- Associated teams
- Contributors
- Linked Jira issues

## Configuration

### Hardcoded Values
- Organization ID: `b9427kk9-4caa-1ka6-7jj5-c777aa87a1aa`
- Site ID: `66dac687-c07e-4919-9fec-8ed98e6c14ec`
- Base API URL: `https://api.atlassian.com`

These values are specific to the target Atlassian instance and may need updating for different organizations.