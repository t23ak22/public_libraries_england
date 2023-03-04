App has bees hosted successfully at render at - https://public-libraries-england-render.onrender.com
And the app was successfully uploaded to github and was able to push changes to the repository accordingly(https://github.com/t23ak22/public_libraries_england).
A file named 'requirements.txt' was generated specifying all the dependencies of the application.


This is an app which helps users to find the public library available in their locality.
The home page contains the form element which is a text box where sers can enter the post code.
And on tapping the search button, it will return the available list of libraries by joining the two tables named libraries and post_codes_table.
The result shown to the user will be filtered using the postcode user entered, which is passed as a string to the SQL query.


This app has been developed using 'flask' framework.



Step 1
  The first step was to import the data from csv to a newly created db file in the app directory. For that, I used 'database.py' which will create two tables.
  And in that table postcode was the common attribute among them. So,it was possible to join them using the 'postcode' foreign key.

Step 2
  Once the data got parsed, I created my main python controller file which is 'find_library.py'.
  This file contains all the routing functions required for the functioning of the app.

Step 3 
  Then in parallel with working on the main file, I worked on the html files which can be rendered using render_template() function.

  
In order to run the app in a local machine, use the following commands.
  export FLASK_APP=find_library.py 
  export FLASK_ENV=development
  python3 -m flask run 