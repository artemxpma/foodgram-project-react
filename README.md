# Foodgram  
Simple web-app to exchange cooking recipes with your friends. Find, like and create shopping list for your lunch just in few clicks.  
  
  
### Stack:  
Backend based mostly on next technologies:  
- Python  
- Django  
- DRF  
- Djoser  
- Docker  
- PostgreSQL  
- nginx  
- gunicorn  

Front-end based on React and made by Ya.Practicum team.  



### How-to:  
Download ```infra``` folder from repo and run ```$ docker-compose up``` in ```infra``` folder.   
Don't forget to create ```.env``` file and populate it with Django Database settings.  
Run ```docker-compose exec backend bash``` and then   
```
python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py collectstatic && python3 manage.py load_json ingredients.json && python3 manage.py createsuperuser  
```  

### API
Documentations with example requests and responses availiable at   
51.250.4.136/api/docs/redoc  
  
### Author:
Artem Sinitsyn, Ya.Practicum.   
v1.2  

### Check it out at...  
51.250.4.136/
