## Installation

```
pip3 install pipenv
pipenv install
pipenv shell
python manage.py migrate
```

## Startup

```
pipenv shell
python manage.py runserver
```

## Integration with Docker (Linux)

To play with docker you need to install it first :-)

(Of course you can follow the commands [here](https://serverspace.io/support/help/how-to-install-docker-on-ubuntu-20-04/) )

```
sudo apt update
sudo apt install software-properties-common ca-certificates curl gnupg-agent apt-transport-https
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io
```
Now, you have downloaded the docker engine where all the containers will be executed. A useful tool that will help us
orchestrate all the containers (at first we only have database & django app; later we shall also have tomcat/nginx) is docker-compose

To install docker-compose you can visit the link [here](https://docs.docker.com/compose/install/). TLDR:

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version 
```

## Launch the environment
Now that you have installed the necessary tools you can play with our application. Simply change directory so that you are on django-scaffolding/docker and execute the following command. This will keep the terminal blocked and you will see the logs that are spitted
from all the containers. 

```
docker-compose up
```

If you want to ignore the logs and you simply want to start the containers use the option -d:

```
docker-compose up -d
```

In the first time it will try to install the necessary images for every container that we are about to launch (i.e. it will download the image for python for the web container and the postgres image for the database container). Thus, the first time it may take a couple of minutes.

Now the application is up and you can connect via a web-browser to the url: http://localhost:8000

To shut down the containers execute:

```
docker-compose down
```

## Some useful commands with docker and docker-compose

Check the images that you have downloaded: 

```
docker images
```

Check if containers are up: 

```
docker container ps
```

In order to access a container directly (like running ssh on a remote vm) you can execute (on docker directory):

```
docker-compose exec <name of the container e.g. web> /bin/bash
```

## Some commands for demo with db and django containers

```
docker-compose exec web /bin/bash
python manage.py createsuperuser --username=nikos --email=nikos@example.com
<It should then ask you for a password.>
```

Once you have entered the password go ahead and connect to http://localhost:8000 or http://localhost:8000/admin with the credentials that you've just created!

## Debug the database 

```
docker-compose exec postgres /bin/bash
psql -h localhost -U postgres -d postgres
select * from auth_user;
```

With these sequence of commands you verify that indeed you have created a user and it exists in db

## Notes regarding data directory

TL;DR: It is included in .gitignore so no worries :)

You may notice that once you execute the docker-compose a directory "data" is going to be created in project. There we are going to have all the files that are going to be used for postgresql and later for our application server.

Due to the fact that there wasn't any directory there before it has automatically created and it's and it's owned by root. So the first time it appears simply execute the following command (by replacing <user> with your linux username).

```
sudo chown -R <user>:<user> data/ 
```


