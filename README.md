# Project 1
Code for Info3180 Project 1
Author: Jonathan Astwood

Remember to always create a virtual environment and install the packages in your requirements file.
In order for the application to run correctly, the following must be included in a .env file:

```bash
FLASK_DEBUG=True
FLASK_RUN_PORT= *SELECT AN APPROPRIATE PORT*
FLASK_RUN_HOST=0.0.0.0
SECRET_KEY= *SELECT AN APPROPRIATE SECRET KEY*
UPLOAD_FOLDER= *SELECT AN APPROPRIATE FOLDER, I USED ./UPLOADS*
DATABASE_URL=postgresql://*USERNAME*:*PASSWORD*@localhost/*DATABASE NAME*
DATABASE_USERNAME= *DATABASE USERNAME*
DATABASE_PASSWORD= *DATABASE PASSWORD*
```

Note that the database username and database password are the same as those in the DATABASE_URL.