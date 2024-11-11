# base image
FROM python:3.12-slim

# setup working directory in container
WORKDIR /Inventory_management_system

# copy all files to inventory_management_system directory
COPY . /Inventory_management_system/

RUN pip install poetry

RUN poetry install



# command to run on container start
CMD ["poetry", "run", "python", "app/main.py"]