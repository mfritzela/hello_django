# Pull base image
FROM python:3.10.8-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2


# Set work directory
WORKDIR /mycode

# Install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Document port to be exposed (does not actually expose port)
EXPOSE 8000

# edit permissions to allow execution of entrypoint script
RUN chmod +x ./docker-entrypoint.sh
# CMD: Command to be run when running a container created from this image
#CMD ["/docker-entrypoint.sh"]
