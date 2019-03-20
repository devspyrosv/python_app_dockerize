## python_app_dockerize
  
  Dockerize a simple python app.
  
  Utilize Docker layer caching to improve build speed.
  
  Build and run with: 
  
  ```bash
  
  docker build -t pydock:0.1 . && docker run \
  -v `pwd`/volume1:/data \
  --env VAR1=env1 --env VAR2=env2 \
  --name pydock \
  -u 1000:1000 \
  pydock:0.1
  ``` 
