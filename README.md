# Bitbucket-bot - clone of telegram bot @Vsratoslav
Bot gets picture from user, choose random phrase from file and draw this one on the picture. After that bot send modified picture to the user and offer to share it to some telegram-channel.

# Usage
Clone the repository
```
git clone https://github.com/fomin2601/Bitbucket.git
```
Choose working directory
```
cd bitbucket
```
Set virtual environment
```
python3 -m venv venv
```
Activate venv
```
source venc/bin/activate
```
Set dependencies
```
pip install -r requirements.txt
```
Bitbucket-bot requires environment variables:
- **BOT_TOKEN** - bot-token
- **IMAGES_PATH** - path to folder with user images
- **PHRASES** - path to phrases-file
- **CHANNEL_TO_REPOST** - channel-id to repost modified image
To start bot use in working directory
```
python3 main.py
```

# Docker
There is Dockerfile in project folder. To build docker container use
```
docker build -t bitbucket:<tag>
```
Nextly to start docker container use
```
docker run bitbucket:<tag>
```
