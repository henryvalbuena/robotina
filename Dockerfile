# set base image (host OS)
FROM python:3.8.3-slim-buster

# set the working directory in the container
WORKDIR /robotina

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "./start.py" ] 