# How to Get Airflow UI Password on Docker:
First Get your container Name: <your_airflow_container_name>
First, get your container name:
docker ps
My container name is:
airflow-docker-sleek-airflow-1
Run this exact command in PowerShell:
docker exec -it airflow-docker-sleek-airflow-1 bash -c "cat /opt/airflow/simple_auth_manager_passwords.json.generated"

If file is missing or If file does NOT exist
Search for it: 
docker exec -it airflow-docker-sleek-airflow-1 bash
Then inside container:
find / -name "*password*"


# Reset password manually (this works 100%)
Open container:
docker exec -it airflow-docker-sleek-airflow-1 bash
Overwrite password file:
echo '{"admin": "Admin123!"}' > /opt/airflow/simple_auth_manager_passwords.json.generated
Restart container:
Exit, then:
docker restart airflow-docker-sleek-airflow-1

# Make password permanent
If you keep restarting containers, this will keep happening.
Fix it properly via environment variables.
In your Docker setup YAML:
environment:
  AIRFLOW__CORE__AUTH_MANAGER: airflow.auth.managers.simple.SimpleAuthManager
  AIRFLOW__SIMPLE_AUTH_MANAGER__USERS: admin:Admin123!

Then restart:
docker compose down
docker compose up -d
