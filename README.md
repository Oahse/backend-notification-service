# backend-notification-service
A robust, scalable service responsible for managing all user notifications across multiple channels including email, SMS, and real-time socket connections. It handles message queuing, formatting, delivery retries, and ensures reliable, timely communication for alerts, updates, and transactional notifications.

# Start Local Server
Use the command below to start
```bash 
uvicorn main:app --reload
```

# Setting up the Local Database
1. Create Virtual Environment and Install Python Dependencies
   create virtual environment
   ```bash
   python3 -m venv venv
   ```
   active virtual environment (Command for Macos check [here](https://docs.python.org/3/library/venv.html#how-venvs-work) for your os)
   ```bash
   source venv/bin/activate
   ```
   install dependencies
   ```bash
   pip install -r requirements.txt
   ```

2. Start the Servers(redi, celery and fastapi)
   ```bash
   chmod +x ./run_servers.sh && ./run_servers.sh

   ```