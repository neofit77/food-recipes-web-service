Steps
1. clone repo
2. in project folder (food-recipes-web-service) create two folders for volumes, folder names are mysql_data1 and static_data
3. in file app/app/User/validate_mail enter your API keys for hunter and clearbit
4. in project folder (food-recipes-web-service) create environment file .env, this is example cintext that file

DB_NAME=food_recipes
DB_PASSWORD=test123
DB_USER=aleksandar
SECRET_KEY=tajna7777
ROOT_PASS=ajhsk3452

6. run command "docker-file build" (yes, you must have instaled docker and docker-compose)
7. run command "docker-compose up"
