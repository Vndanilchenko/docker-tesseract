# TESSERACT-DOCKER

example of text extraction from images using tesseract, flask and docker 

description - the service selects a random image from gallery, extracts the text and returns it through the flask endpoint "getResponse"

main script

    main.py
    
    
build image 

    sudo docker build -t tesseract-docker .

![build image](screenshots/build.png)
    
run container

    sudo docker run -it -p 8080:80 tesseract-docker

![run container](screenshots/run.png)

random results 

![res1](screenshots/example%201.png)
![res2](screenshots/example%202.png)



author: Vadim Danilchenko

email: vndanilchenko@gmail.com 