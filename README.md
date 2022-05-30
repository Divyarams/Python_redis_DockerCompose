# Python_redis_DockerCompose
A python code to update/get data from Redis by provisioning both environments in custom-defined network for connectivity.

# Overview
Using Docker-compose, it is easier to run containers than specifying flags for each docker run command. In addition, it is easy to set up environments with just few lines of code.

1. The build for python is in the Docker file. Redis image in itself is mentioned in Dockerfile.
2. A requirements.txt file specified requirement to import redis in python
3. The logic to update/get/set data in Redis is mentioned in app. 
4. Once all the files are in place, execute 
        ``docker compose up -d``
5. Both the containers are running and can connect to network using the custom defined network in bridge mode. Additional commands t inspect the custom network,

          docker network inspect <networkname>
        
          docker network connect <containerid> <networkname>
          
          docker network create <networkname>
          
          docker network prune


