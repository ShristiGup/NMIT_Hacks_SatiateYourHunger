# NMIT_Hacks_SatiateYourHunger

(20th March - 1:45pm)
Project Description - This project aims to build a web application for the users to get to know about the recipes they can make with the ingredients they currently have at their place. This application would be built using Html, Css, Bootstrap4 as frontend tech and django as backend framework.

Current Updates on the project - 
Created 3 apps inside a django project namely main_app, Sat_Hunger and users.

The main_app would contain the basic functionalities of the application like homepage which would contain links to user's profile, find_recipe page of the application, an about page link etc.

The Sat_Hunger app of the project is the app created which contains the admin path of url and includes other urls of the application.

The users app contains the user detail pages like login, logout, register, profile.

*******************************************************************************
(20th March - 2:50pm)
Updates - User authentication system added to the application such as register and login pages in the users app of the project.

*******************************************************************************
(20th March - 5:07pm)
Updates - A form created for filling the ingredients as specified by the user. Some filtering options have also been added to the form for user to make preferences as per his/her choice like veg/non-veg food and the hunger level of the user. This form has been created in find_recipe.html file of the project.
Also a recipes app has been added which would display the video links, steps of preparation of the recipe and other details of the recipe which would come as result of the ingredients inputted by the user.

*******************************************************************************
(20th March - 5:45pm)
Updates - The page for displaying the recipes upon filling the ingredients by the user in the find_recipe form, has been created. This page shows the image and name of the recipe along with some other stats like Category, health score, time taken to prepare the recipe and the number of people who liked this recipe. 

*******************************************************************************
(20th March - 8:51pm)
Updates - The profile page of the user has been made in the application, displaying his/her personal information like name, email, profile picture and an update button for updating any changes if made to the profile.
Also some changes to the UI has been made like navbar has been included in the find_recipe page etc.

********************************************************************************
(20th March - 10:20pm)
Updates (One Add-On Done) - The redirection of user to the www.zomato.com page has been added if the user selects starving radiobutton in the form of find_recipe page of application otherwise the app gives the recipe and it's instructions as a result.
Also half of the functionality has been implemented in the recipe_detail page of the application like image of recipe, it's nutrition information and other basic details of the recipe.

*******************************************************************************
(20th March - 11:50pm)
Update (Another Add-On Done) - The user profile page has been updated with the latest 5 searches of the recipes made by the user as per his/her preferences of ingredients, veg/non-veg food and hunger level. Accordingly the models have been made, saved in the database and shown in the admin page of django project application.

*******************************************************************************
(21st March - 7:30am)
Update - UI has been updated and another html page named sati.html has been made which would appear before register/login page of our application. It would be the first page to be displayed when the user opens up the application.

*******************************************************************************
(21st March - 10:00am)
Update - Instructions for cooking a recipe added on recipe_detail.html file of the application, after fetching from the spoonacular.com api.

*******************************************************************************
(21st March - 11:48am)
Updates - Video links added on the recipe_detail page of the application, along with appropriate messages if no video link is shown up.

*******************************************************************************
(21st March - 1:50am)
Updates - index.html page modified, along with some food jokes and trivia fetched from food trivia api.

*******************************************************************************
