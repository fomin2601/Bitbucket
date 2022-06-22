FROM python:3.9-alpine
LABEL maintainer="fomin260145@gmail.com"
LABEL projectname="It's pet-project called Bitbucket"

#Set constants
ENV BOT_TOKEN="5254572269:AAGFxJTwEVIlSFxB1MaddjR8QUEnWBvsw8o"
ENV IMAGES_PATH="./images/"
ENV PHRASES="./phrases.txt"
ENV CHANNEL_TO_REPOST="473651829"

RUN apk update && apk upgrade && apk add bash

#Copy application files
COPY images ./Bitbucket/images
COPY Lobster-Regular.ttf ./Bitbucket
COPY main.py ./Bitbucket
COPY phrases.txt ./Bitbucket
COPY requirements.txt ./Bitbucket

#Choose workdir
WORKDIR ./Bitbucket

#Install dependencies
RUN apk add -u zlib-dev jpeg-dev gcc \
    freetype-dev \
    fribidi-dev \
    harfbuzz-dev \
    lcms2-dev \
    libimagequant-dev \
    openjpeg-dev \
    tcl-dev \
    tiff-dev \
    tk-dev \
    musl-dev

RUN python3 -m pip install --no-cache-dir -r requirements.txt


#Command to run bitbucket-bot
ENTRYPOINT ["python3", "main.py"]