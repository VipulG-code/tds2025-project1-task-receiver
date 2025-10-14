import requests

data = {
  "email": "23f1002090@ds.study.iitm.ac.in",
  "secret": "ProjectSecret123!",
  "task": "example-task-id",
  "round": 1,
  "nonce": "unique-nonce-value",
  "brief": "Write the project brief here.",
  "checks": [],
  "evaluation_url": "http://example.com/notify",
  "attachments": []
}

r = requests.post("http://127.0.0.1:7860/ready", json=data)
print(r.status_code, r.text)
