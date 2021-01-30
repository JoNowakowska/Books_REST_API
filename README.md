# Hello and welcome to Books_REST_API

## Summary
This simple RESTful API connects to Google Books API (https://developers.google.com/books) allowing users to 
save book_volumes found by keywords of interest. 
Then, users can search the db in several ways and sort the records.


## Running the app
The app is deployed to Heroku: https://book-restful-api.herokuapp.com/books
To test the app, you can use a platform for API development, e.g. Postman. 
I provide a Postman collection in a file Books_REST_API_GoogleApi.postman_collection.json.  
  
If you want to use the code with your own Google Books API Key, 
you need to create your own API key. 
To do that, go to Google Books API documentation (https://developers.google.com/books/docs/v1/using)
and follow the guidelines. Then, add the API key as an os environment variable named 'GOOGLE_BOOKS_API_KEY'.  
Next, install all the dependencies (see: requirements.txt).  
Finally, you can run the app from the console by entering: 'python app.py' command.


## API's available endpoints
Again, this is the API URL: https://book-restful-api.herokuapp.com/books  
  
The API has the following endpoints: 
  
/books (GET)  
  
/books?published_date=yyyy (GET)  
/books?sort=-published_date (GET)  
/books?sort=published_date (GET)  
/books?author=name1&author=name2 (GET)  
  
/books/<book_id> (GET)  
  
/db (POST - body takes keywords to search for in Google Books API, 
body should look as follows: {"q": "here your keywords"})
  

## API collection
A Postman collection is saved in a file Books_REST_API_GoogleApi.postman_collection.json. Feel free to download it to check the API endpoints easily.


## Database
You can check the database schema by opening the database_design.txt file and pasting the code from there to a code interpreter at the dbdiagram.io website.