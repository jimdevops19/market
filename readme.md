# Jim Shaped Coding Django Project

## This Readme file explains two ways to execute this website on your local environment


### Option 1 - Run on your Machine

 - Make sure you have Django installed with `pip install django`
 - **Not must** -  Install pillow by `pip install Pillow`
    - This package is for creating ImageFields and handle images that are
    being uploaded to your database, since in the video I pull all the images from
    a CDN, this is not a necessary step.
 - Within the directory of the project, run `python manage.py runserver`
 


### Option 2 - Run on a docker container
 - **NOTE: there is an issue with Base64 encoding with versions that are <3.1.
 This is going to work ONLY when docker image for django3.1< is released.
 A link for a question raised on StackOverflow: https://stackoverflow.com/questions/63650745/invalid-base64-encoded-string-number-of-data-characters-217-cannot-be-1-more**
 
 - Make sure you have docker installed on your local environment by -  `docker run hello-world`
 - Within the directory of the project run - `docker build . -t market`.
 This will build the project image with docker.
 - Run the Container that is built by: `docker run -p 8000:8000 market`
 


 
    
 
