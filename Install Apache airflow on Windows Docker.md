Apache airflow on Windows Docker

Step 1
Download Docker Desktop for Windows:
https://docs.docker.com/desktop
search and run this on command prompt:
wsl --uppdate
next launch the docker app and follow the set up process
also install vs code if you don't have:
Download Visual Studio Code:
https://code.visualstudio.com/download

step 2
create a dedicated airflow folder for airflow work
Name it: workspace
inside the folder, right click on empty space and open terminal
enter:
code .
the command will launch VS Code and open the folder for development
RUN ON COMMAND:
docker build -t sleek-airflow:latest .
Then Start the Airflow Container:
docker run -d -p 8081:8080 --name sleek-airflow sleek-airflow:latest standalone
http://localhost:8081

To view logs to get password:  74ZcwqX3EA7GA5TA
docker logs sleek-airflow

clean sleek-airflow:
docker rm sleek-airflow

Create the folders Airflow needs:
Right now your directory only had a Dockerfile earlier.
You must create the folders that you mapped as volumes.

NEXT:
airflow-docker
│
├── dags
├── logs
├── plugins
├── airflow_home
├── docker-compose.yml
└── dockerfile

Add this in docker-compose.yml file:
version: '3'
services:
  sleek-airflow:
    image: sleek-airflow:latest
    volumes:
      - ./airflow:/opt/airflow
    ports:
      - "8080:8080"
    command: airflow standalone

Run the script below for volume mapping: Your Windows folders will be mounted into the container.

docker run -d ^
-p 8081:8080 ^
-v C:\Users\USER\workspace\airflow-docker\dags:/opt/airflow/dags ^
-v C:\Users\USER\workspace\airflow-docker\logs:/opt/airflow/logs ^
-v C:\Users\USER\workspace\airflow-docker\plugins:/opt/airflow/plugins ^
-v C:\Users\USER\workspace\airflow-docker\airflow_home:/opt/airflow ^
--name sleek-airflow ^
sleek-airflow:latest standalone

Confirm the DAG folder is actually mounted:
docker exec -it sleek-airflow bash

Create DAGS in VS Code

TO START AIRFLOW WITH COMMAND LINE IN WINDOWS:
Open Docker app,
  -  cd workspace
    - cd airflow-docker
      - dir
      - docker ps -a
      - docker start sleek-airflow
TO CHECK RUNNING CONTAINERS:
      - docker ps
TO VIEW LOGS:
      - docker logs sleek-airflow 
try running http://localhost:8081/

TO STOP
docker stop sleek-airflow


Restart Airflow (if something breaks)- Sometimes scheduler issues happen:
Restart container:
docker restart sleek-airflow

How to Change or Maintain the Airflow Password:

Option 1 — Change password from CLI (Recommended)

Run this command:
docker exec -it sleek-airflow airflow users reset-password --username admin
It will prompt:
Password:
Repeat for confirmation:
Enter your new password.


Create a new user:- If you want a different account:

docker exec -it sleek-airflow airflow users create ^
--username gospel ^
--firstname Gospel ^
--lastname Orok ^
--role Admin ^
--email gospel@example.com ^
--password strongpassword
Then login with that user.

Your Daily Execution Flow (Simple Version):
Each day you want to work:
1️⃣ Start Docker Desktop
2️⃣ Open command line
3️⃣ docker start sleek-airflow
4️⃣ Open http://localhost:8081
5️⃣ Write DAGs in VS Code
6️⃣ Run pipelines

