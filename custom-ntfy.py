import json
import os
import sys
import requests

def main(args):
  if len(args) < 3:
    print("ERROR: Wrong arguments")
    sys.exit(2)

  alert_file_location = args[1]
  hook_url = args[2]

  try:
    with open(alert_file_location) as alert_file:
      alert_json = json.load(alert_file)

      alert_level = alert_json['rule']['level']
      description = alert_json['rule'].get('description', 'N/A')
      agentname = alert_json['agent'].get('name')
      timestamp = alert_json['timestamp']
      
      ntfy_level = 1
      
      if 2 <= alert_level <= 7:
        ntfy_level = 1
      elif 8 <= alert_level <= 9:
        ntfy_level = 2
      elif 10 <= alert_level <= 11:
        ntfy_level = 3
      elif 12 <= alert_level <= 13:
        ntfy_level = 4
      elif 14 <= alert_level <= 15:
        ntfy_level = 5

      headers = {
        'X-Title': f'{agentname}: {description}',
        'X-Priority': str(ntfy_level),
      }
      
      # Convert the date to a more readable format
      timestamp = timestamp.replace('T', ' ').replace('+0000', '')

      data = f'Date: {timestamp}\nAgent: {agentname}\nDescription:{description}'

      response = requests.post(url=hook_url, headers=headers, data=data)
      response.raise_for_status()

  except FileNotFoundError:
    print(f"ERROR: Alert file {alert_file_location} not found")
    sys.exit(6)

  except json.JSONDecodeError:
    print(f"ERROR: Invalid JSON in {alert_file_location}")
    sys.exit(7)

  except requests.RequestException as e:
    print(f"ERROR: Failed to send request to {hook_url}: {e}")
    sys.exit(1)

if __name__ == "__main__":
  main(sys.argv)
