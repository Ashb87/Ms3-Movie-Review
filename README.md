# Milestone Project Three | Movie Review

[View the live project here]() <br>

## About

This website has been created for my Milestone 3 Datacentric Development project. 
As a movie fan myself and after speaking with my mentor, I decided I would like to create a site where users can add and browse movie reviews of all genres. Using the CRUD functionality they will be able to create their own account. From here they can add, edit and delete their own reviews. As well as read the reviews from other users. 

## Contents

## User Experience-(UX)

### Site Goals

  1. I want the site to be attractive, responsive and easy to navigate for the user.
  2. I want the purpose of the site to be clear to the user
  3. I want the user to be able to create, edit and delete their own reviews.
  4. I want their to be an admin account where they can edit, delete and add new genres.
  5. I want the user to be able to register an account, login, logout and delete it if they wish. 

### User Stories
  
  * #### First Time Visitor Goals
    1. I want the site to be attractive and and easy to navigate.
    2. I want the site to be responsive to whichever device I am viewing it on.
    3. I want to understand clearly what the site is for.
    4. I want to be able to register an account easily
    5. I want to be able to view other peoples reviews
    6. I want to be able to search for existing reviews.

  * #### Returning Visitor Goals
    1. I want to be able to login to my account easily for full access of the site.
    2. I want to be able to add my own reviews.
    3. I want to view all my existing reviews through my own profile page.
    4. I want to be able to edit and delete my existing reviews.
    5. I want to follow the site through their social links. 

  * #### Admin Goals
    1. As an admin of the site I Wwould like full access to all pages
    2. I would like to be able to add, edit or delete any genre categories 

### Design

* When considering the design for this project it was important to take in to account the target audience. But very quickly I realised that a site like this doesn't really have any particulart target. Movies appeal to all people from all backgrounds of all ages. So with this in mind I wanted to create a look that just used visually appealing colors that contrast each other nicely and let all the main features of the site stand out and be clear to see for the user. 
* By giving the option to add an image to the users reviews it really helps to make the page stand out and be clear for the user which film they are reading about. 
* For the home page I wanted it to feel like an up to date movie review site so decided to add a video trailer of the biggest film out right now. I feel this instantly draws the user in and gives them the cinematic feeling all us movie fans enjoy.

  * #### Wireframes

  To create my wireframes I used balsamiq. I have done a design for both large and smaller screens to show how the layout of the site will change accordingly with different screen sizes. The links to the wireframes are below. <br>
  * [Large screens](https://github.com/Ashb87/Ms3-Movie-Review/blob/main/assets/wireframes/Movie-review-large.png)
  * [Smaller screens]() 

  The majority of the site has been kept very similar to the design of my wireframes. The main difference is on the *movie review page.* After speaking with my mentor he advised it would be better to have all the movie cards on one page with minimal information, and then open the full review for each individual review on a separate page. By doing this it has reduced the amount of scrolling needed on the movie review page as it is more condensed and much more user friendly. I also like the way the full review opens up on a separate page and think it gives a more professional feel to the site.

  * #### Imagery

  For the design of the site I have only used two images. Both quite small and only used as background images. One for the home page and one on the movie review page. For the home page it is used as the hero image and is a picture of red theatre/movie curtains. Set as a backdrop for some text. For the review page the image is used as the background for the search bar where the user can search for a movie title or genre. It has a backdrop filter over the picture to make the text stand out more making it easier for the user to read. <br>
  As well as these two images the user also has the option to add an image url so they can add a picture to their review. These are all set to a matching size with the same border radius, so that with every review added they all look the same and sit uniformly on the page. If the user doesn't add their own image then I have a default image set to be inserted instead, again with a matching size and border radius. 

  * #### Color scheme

  For the colors on my project I first went to [coolors.co](https://coolors.co/) to use their palette generator. I had an idea of wanting to use a dark blue for the majority of my site and so used the generator to find colors that would match up well. From this I found a palette that hard a dark blue, a shade of red and a yellow. From here I then used the google color picker to fine tune the exact shades of each color I wanted. I thinkthe colors all work really well together and give the look I was going for to suit the movie feel of the site.<br>
  For a contrast I used a grey for the footer of the site and also for some of the headings across the different pages. This gives the footer more of a distinctive look and differentiates it from the rest of the site. Whilst also sitting nicely against the dark blue.

  <img src="static/images/colors.png" width="450" height="200"> 

  * #### Typography

  I have used two fonts across the site both imported from google fonts. They are **bebas neue** and **ubuntu**. The Ubuntu font has been usded for the majority of the text across the site while the Bebas neue font has been used for the headings across the pages. The bebas neue font is displayed in all capitals so works well for the headings. I then wanted another font to sit nicely with the bebas neue and be easy and pleasing to read for the user. I found the ubuntu font and after trying a couple of others felt this font worked well with the look of the site. 

## Features

  * ### Across All Pages
    * Responsive Fixed Nav bar at the top that collapses to burger icon for smaller screens and has blurred effect when page is scrolled behind it. If the user is logged in they will have the options of *home* *movies* *profile* and *logout* If they are not signed in they will have the options of *home* *movies* *login* and *register*
    * Footer with social links opening each one in a new browser.

  * ### Home Page
    * Embedded video from youtube displaying a recent movie trailer to give the effect of an upto date site. Video is responsive to all screen sizes.
    * If user is logged out there is a button under the video that links the user to the login page or if not yet registered then they can link to the register page. If logged in they will instead have the option to add a movie review.
    

  * ### Login/Register Page
    * For the register page the user will be required to create a username with a minimum of 5 characters. And then a password, again minimum of 5 characters. They will need to add the password twice for extra security with the register button being disabled until they match.
    * For the login page they will be required to input their username and password.
    * For both the login and registered pages a flash message will be displayed when user is successful in loggin in or registering.

  * ### Movie Page
    * At the top of the page there is a search bar where the user can look for a movie either by its name or genre.
    * For users not logged in there is a button giving them the option to log in allowing them to add a review.
    * For logged in users this buttin becomes an *add movie button* linking them to the add movie form.
    * Each review already added is then displayd underneath. showing the name of the movie, an image, if provided and who created the review. Within each movie card is a button linking the user to the full review of that specific movie. If they are not logged in they will be prompted to do so before viewing the full review.

  * ### Full Review Page 
    * On this page the user can see the film title with an image card if provided. Then they will be able to see the genre, a movie synopsis, the users review, a rating out of 5 and who the review was added by.
    * A link back to the movie page.

  * ### Profile Page
    * A card panel at the top with the users username displayed and a button that links to the add movie review form.
    * If the user has no reviews there will be a heading saying no reviews yet. Otherwise their reviews will be displayed below, showing the movie title, the image provided or default image and then two buttons. One linking them to the edit review page. The other is delete review button. If they click this they will be prompted my a modal to either confirm or canel their choice to delete the review.
    * At the bottom below their reviews they will have the option to delete their account. Again prompted by a modal to confirm oor cancel their decision.

  * ### Add/Edit Movie Page
    * For the add movie page a form is displayed for the use to fill out. There is a dropdown option for the user to pick a genre. They will then need to fill in the movie name, movie synopsis, and their review of the movie. They will then have the option to add an image url and finally pick a star rating out of 5. Once all filled in they can then click the add movie buton and their review will appear on the movie page.
    * For the edit movie page it will be the same as above with the input fields already filled with previously given information. They can then change what they like on the review and click *confirm edit* or cancel their changes by clicking on the *cancel changes* button. 

## Features to implement in the future
To take this site further, with more knowledge and time there would be a few elements I would like to add to the project.
  * Allow user to add a profile image to their account.
  * Allow the user to edit their username or password
  * Allow more than one Admin by not just using the Admin username.
  * Using emailJS give the user the option to signup to a news letter and recieve emails relevant to the site.
  * Allow any user to add a further review to any review already added on the site.
  * limit how many reviews are displayed on a page before user can click to go to a next page rather than keep scrolling. 

## Technologies used

### Languages used

  * [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) <br>
  * [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) <br>
  * [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) <br>
  * [Python](https://www.python.org/)

### Frameworks, Libraries and Programs Used

  * [Materialize](https://materializecss.com/)<br>
    Materialize was used to help build the structure of the website and add responsiveness across different screen sizes.
    It also supplied some styling and built in components such as the modal.
  * [Balsamiq](https://balsamiq.com/) <br>
     I used balsamiq to design and draw up my wireframes before starting the project.
  * [Google Fonts](https://fonts.google.com/) <br>
     Google fonts was used throughout the project to import my selected fonts.
  * [Font Awesome](https://fontawesome.com/) <br>
      Font awesome was used to add all icons used on the site.
  * [Gitpod](https://www.gitpod.io/) <br>
     Gitpod was the text editor I used for this project.
  * [Git](https://git-scm.com/) <br>
     Git is used as version control software to add, commit and push code to my GitHub repository where the code is then stored.
  * [GitHub](https://github.com/) <br>
     I have used GitHub as a remote repository to push and store the committed changes to my project from Git.
  * [jQuery](https://jquery.com/) <br>
     jQuery was used to initialize Materialize and for some of the sites functionality.
  * [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) <br>
     I have used Google chromes built in developer tools to help with the styling of the site, selecting colors and to help fix any bugs I found.
  * [Heroku](https://id.heroku.com) <br>
     Heroku has been used to deploy my live site.
  * [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) <br>
     Flask was used as the web framework for the application.
  * [MongoDB](https://www.mongodb.com/)
     MongoDB was used to hold the database for my project.
  * [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) <br>
     Werkzeug was used for password hashing and authentication.
  * [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) <br>
     Jinja templating language was used to simplify and display backend data in HTML.
  * [coolors.co](https://coolors.co/) <br>
     Coolors was used. to help find the color palette I wanted for my project.