# TODO: Assign specific version
FROM ubuntu:20.04

# Setting to direct python logs to terminal output
ENV PYTHONUNBUFFERED 1

RUN set -xe \
        && apt-get update \
        && apt-get -y install python3-pip
RUN pip install --upgrade pip

# Copy requirements and install dependencies

# RUN apt-get install -y postgresql-client jpeg-dev
# RUN apt-get install -y .tmp-build-deps \
 #        gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

COPY ./requirements.txt /requirements.txt
RUN pip install -r ./requirements.txt
# RUN apk del .tmp-build-deps

# Setup project directory from the local data
RUN mkdir /aqua_track
WORKDIR /aqua_track
COPY ./aqua_track /aqua_track/

# Setup directories for media/static
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
# Setup user access
# RUN adduser -D user
RUN adduser user

RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web

USER user


