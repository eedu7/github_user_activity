import urllib.request
import json
from collections import Counter

def get_user_activity(username):
    url= f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            status= response.status
            data = response.read()
        return (status, json.loads(data.decode()))
    except Exception as e:
        print(f"Error occured on getting user data: {e}")
        
def get_recent_activities(user_activities):
    activities = []

    for activity in user_activities:
        event = {"type": activity["type"], "repo": activity["repo"]["name"]}

        activities.append(event)

    return activities

def summarize_activites(activities):
    summary = []
    
    for activity in activities:
        event_type = activity["type"]
        repo = activity["repo"]

        match event_type:
            case "PushEvent":
                event = f"Pushed commit to {repo}"
            case "CreateEvent":
                event = f"Created a new branch/tag of {repo}"
            case "IssueEvent":
                event = f"Opened a new issue in {repo}"
            case "DeleteEvent":
                event = f"Deleted a branch or tag in {repo}"
            case "PullRequestEvent":
                event = f"Pull from the {repo}"
            case "IssuesEvent":
                event = f"Opened a issue in {repo}"
            case "IssueCommentEvent":
                event = f"Pushed commit to the issue in {repo}"
            case "ForkEvent":
                event = f"Forked the {repo}"
            case "WatchEvent":
                event = f"Starred the {repo}"
            case "ReleaseEvent":
                event = f"Published/updated/delete the {repo}"
            case "CommitCommentEvent":
                event = f"Commited on the commit in {repo}"
            case "PublicEvent":
                event = f"Made the {repo} public"
            case "MemberEvent":
                event = f"User is added/removed from {repo}"
            case "TeamAddEvent":
                event = f"Team is added to {repo}"
            case "GollumEvent":
                event = f"Wiki Page is updated or deleted of {repo}"
            case "StatusEvent":
                event = f"Commit status created/updated of {repo}"
            case "DeploymentEvent":
                event = f"Deployment is created/updated of {repo}"
            case "DeploymentStatusEvent":
                event = f"Deployment status is created/updated of {repo}"
                
            case _:
                print(event_type)
                continue
        summary.append(event)
    return summary

def print_user_activity(activites):
    activites = Counter(activites)
    for activity in activites:
        count = activites[activity] 
        if count > 1:
            print(activity + f" (Count: {count})")
            continue
        print(activity)

def main():
    username= input("github-activity ")
    status, user_activities = get_user_activity(username)
    
    if status != 200:
        print("User not found")

    recent_activities = get_recent_activities(user_activities)

    summary = summarize_activites(recent_activities)

    print_user_activity(summary)
    


if __name__ == "__main__":
    main()
