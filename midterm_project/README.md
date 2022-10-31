# Midterm project: Prediction of the value of a car based on its characteristics (ML Zoomcamp)

The proposal here is to extract data from the internet regarding the characteristics of cars and their respective values
and later we make the prediction of how much a certain car should cost.

## Steps of the project

### Step 0: Extract data from the web
The first step of this project was to extract data from the web through the Scrapy Framework. The data were extracted from the website [Creditas Auto](https://auto.creditas.com/), which is a website where you can buy semi-used cars.

### Step 1: Data preparation and data cleaning
In this step, the database was downloaded and some features were treated, such as the choice of how to handle and use the "year" feature.

### Step 2: EDA and Feature Engineering 
In this part of the project I tried to make the target "value" more gaussian and also extract some information from the "car_description" variable.

### Step 3: Model selection process and parameter tuning
This was the stage of training some models, tuning parameters and selecting the best model.
In this case, the model chosen was the Ridge model.

## Instructions on how to run the project
Download this repository with all the files. To run locally run the **app.py** file.

### To run with docker (Reference: https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/chapter-05-deployment)
* Build the image

        docker build -t car-price-prediction .
    
* Run it

        docker run -it -p 9696:9696 car-price-prediction:latest
    
(Do not forget to setup docker.)

### To deploy on aws Elastic Beanstalk (If you get stuck see this [video](https://www.youtube.com/watch?v=HGPJ4ekhcLg&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR))
* Run to access the environment

       pipenv shell
    
 * Verify if Elastic Beanstalk is ok in the environment
 
       eb
    
 * Instance of EB with docker
 
       eb init -p docker -r us-east-1 car-price
    
 * Run locally to check if the application is ok
 
       eb local run --port 9696
    
 * Create the environment on aws
 
       eb create car-price-env
        
See the model working [here](https://www.linkedin.com/feed/update/urn:li:activity:6992590637694881792/) or in the video below:

https://user-images.githubusercontent.com/81170729/198910489-1c213fde-2af3-42b4-b888-01326af9e5c9.mp4

