# **Expenses Calculator**
  

![Expenses Calculator](documentation/readme/main_image.png)  


This Expenses Calculator is a Python command line interface (CLI) application designed to record work completed at various locations, which logs details such as date, location, work type, work fee, and distance travelled. Based on the user input it will then calculate travel expenses and the total fees due for travel and work completed.

View the live application here: [ExpensesCalculator](https://expenses-calculator-93f67e190108.herokuapp.com/)  

Google Sheets (view only) [here.](https://docs.google.com/spreadsheets/d/1VC_oKD_-P18TzticsIXXsxaBuKRskCvY82OEt0-8TLo/edit?usp=sharing)


## Contents
* [**User Experience/User Interface (UX/UI)**](#user-experienceuser-interface-uxui)
  * [User Goals](#user-goals)
  * [User Stories](#user-stories)
* [**Creation process**](#creation-process)
  * [Project Planning](#project-planning)
  * [Flowchart](#flowchart)
  * [Google API SetUp](#google-api-setup)
  * [Python Logic](#python-logic)
  * [Data Model - Google Sheets](#data-model---google-sheets)
  * [Design Choices](#design-choices)
* [**Features**](#features)
  * [How to Use BakeStock](#how-to-use-bakestock)
  * [Future Features](#future-features)
* [**Technologies Used**](#technologies-used)
* [**Libraries & Packages**](#libraries--packages)
* [**Testing**](#testing)
* [**Creation & Deployment**](#creation--deployment)
* [**Credits**](#credits) 

  
# User Experience/User Interface (UX/UI)  
  
## User Goals
The Expenses Calculator is designed to be an easy-to-use application to help the user keep track of work completed, and to provide an efficient way of calculating expenses and total fees for work completed. 

  - It must be easy for the user to navigate.
  - Clear instructions are available to ensure the user will be prompted to enter the relevant data at the correct time.
  - There is an option to re-enter data at each step in case the user enters incorrect information.
  - Dead ends are avoided by causing each function to re-run in the event of invalid response / input.


## User Stories  
  1. As a user, I want a practical application to store information about work completed. 
  2. As a User, I want an efficient application which will accurately calculate and record my expenses.
  3. As a User, I want the application to automatically update the relevant spreadsheet.
  4. As a User, I want an application which is clear and easy to use.
  5. As a User, I want an application which provides instructions at every step regarding the type of input required.
  6. As a User, I want the option to re-enter data if I am unhappy with what I have already entered.
  
  

# Creation Process    
  
## Project Planning  
The idea for this project came from my current work as an organist. Apart from my usual places of work, my job also takes me to various locations around the country and for different events. I wanted to create an application which would help me to keep track of work completed and which would keep track of fees due for my work. This programme is therefore designed to record information about the date, location, event type, basic fee and distance travelled. Furthermore, based on information provided about distance travelled, it will calculate my travel expenses and then calculate my total expenses by adding my basic fee and travel expenses. It then records this data in a spreadsheet.
 
The Expenses Calculator was created from this idea and fully planned out using [Lucidchart](https://www.lucidchart.com/) to create a flowchart showing the logic and layout of the application. Once I had investigated the terminal that would run this application, I made sure to stay within it's restrictions and referred back to my flowchart frequently. My main goals for the application were:  

- The first main goal was to have functions with inputs which would record user data
- The second important goal was to ensure that the application would accurately transfer the inputted data to the relevant spreadsheet.

Based on the design of the flowchart, I created the various functions in my code, testing them at each stage, particularly ensuring that the user would not meet any dead ends if they did not enter a valid response or if they wished to re-enter a piece of data.

  
I decided to use Google Sheets to store any data that was entered from the terminal. This 

  
## Flowchart   
To help with planning my project, I used Lucidchart to produce a flowchart of my expected functions and their flow.

![Expenses Calculator flowchart](documentation/expenses_calculator.jpeg)  


<br>  

## Google API SetUp   
Before beginning to code, I set up the relevant credentials and API. This process is detailed in the [Creation & Deployment](#creation--deployment) section. For security reasons regarding connecting a Google account for accessing Google Sheets, I ensured that the `CREDS.json` file would not be open to public view.

Google Sheets was used to store any entered user data and called upon when data was manipulated and updated. All data entry and manipulation takes place within the terminal. 

Clear instructions are printed in the terminal instructing the user in how to enter the data, so that it may be displayed correctly on its output, within the scope of this project. 

<br>  

## Python Logic  
As this is my first Python project, I aimed to create a relatively simple application which is practical and relevant to me. Having completed my initial flowchart, I began the process of coding. I created simple functions corresponding to the data I wished to record and transfer to the spreadsheet.

In each function which required user input I made use of if/elif statements to ensure that the user can confirm that they are happy with the data inputted before moving on to the next step. If the user wishes to re-enter data or if they answer anything other than "y/yes" or "n/no" they will likewise be prompted to re-enter the required data.

Throughout the building of the application I tested the functions individually and together to ensure that the flow of the application was correct.


<br>  

## Data Model - Google Sheets
The data provided by the user is inputted into the respective Google Sheets worksheets. The worksheet is accessed by myself as the only Editor but I include here a View only link to show the recorded data. [Google Worksheets](https://docs.google.com/spreadsheets/d/1VC_oKD_-P18TzticsIXXsxaBuKRskCvY82OEt0-8TLo/edit?usp=sharing)  


   

<br>  

## Design Choices      
As this project was focusing on back-end programming, there was no front-end production by myself, a student of the [Code Institute](https://codeinstitute.net/ie/). The CLI code was provided through the use the the CI's [Python Essentials template](https://github.com/Code-Institute-Org/python-essentials-template) and I did not alter the HTML or JavaScript code, choosing to remain with the original view of the interface. The CLI application allowed a display window of 80 characters, and a vertical scrollbar. _(Please refer to the [Creation & Deployment](#creation--deployment) section of this README to learn how to recreate this project yourself.)_
  

  <br>
      
    

# Features

## How to Use Expenses Calculator

### Launch  
Once the application is opened, the user is greeted with a welcome message.
![Main Menu screenshot](documentation)  
  
    
### Date Input   
The user is prompted to enter the date of the work they wish to record. To ensure consistency when the data is transferred to the spreadsheet, they are reminded to enter the date in the format dd/mm/yyyy. Once the date has been inputted, a response will appear to tell the user what data they gave, followed by a y/n option to confirm and continue to the next step.
![Date input screenshot](documentation)
  
  
### Location 
The user is then prompted to enter their work location. As above, they are given the option to confirm or amend the data.
![Location screenshot](documentation)  
  
    
### Event Type 
Since this programme was designed primarily for my work as an organist, the event type is recorded (e.g. funeral, wedding, choir rehearsal, recital). Once the user has inputted the data there is an opportunity to confirm or revise before moving on.
![Event type screenshot](documentation)
  
### Fee 
The user is prompted enter the basic fee for the event being recorded. This step specifies that the amount is to be entered in Euro(€). The input is fed back to the user with the option to confirm or re-enter the amount. The fee will be returned as a float to account for decimals in the amount.
![Fee input screenshot](documentation)

### Distance travelled and travel expenses 
The next step asks the user to input the distance travelled for work in kilometers. Once the user has confirmed the distance, the function calculates the travel expenses by multiplying the distance travelled by the amount per kilometer (in this instance €0.43 per kilometer). This amount is returned as a float.
![Distance and travel expenses](documentation)

### Calculation of total fee due
The next function calculates the total fee due by adding the initial fee entered and the fee for travel expenses. Since the travel expenses may run to several decimal places, this function includes a direction to round the amount to two decimal places.
![Total fee due](documentation)
 
### Add data given to Google Sheets  
 

### Exit  
In the event that the user wishes to record a further event and travel expenses, the option is provided to begin the application again. Otherwise, the user can choose to exit the application.
![Exit](documentation)  
 

-----  

<br>

## Future Features  
There are a few features that I feel could benefit from additions in the future:
...

  
# Technologies Used:
   - Python - Python code written is my own unless referenced in the source code or the below Credits section.
   - [Lucidchart](https://www.lucidchart.com/pages/) - used to create the flowchart needed during project planning.
   - [GitHub](https://github.com/) - used for hosting the program's source code.
   - [Gitpod](https://www.gitpod.io/) - used as a workspace for developing the code and testing the program.
   - Git - used for version control.
   - [Google Sheets](https://docs.google.com/spreadsheets/) - used for storing edited and saved user data.
   - [Google Cloud Platform](https://cloud.google.com/) - used to provide the APIs for connecting the data sheets with the Python code.
   - [Heroku](https://heroku.com/apps) - used for deploying the project.
   - [PEP8 Validator](https://pep8ci.herokuapp.com/#) - used for validating the Python code.
   - [Tiny PNG](https://tinypng.com/) - used to compress images.

<br>  

# Libraries & Packages 
   - **gspread** - gspread was imported and used to add, remove and manipulate data in the connected Google Sheets worksheets.  

   - **google.oauth.service_account** - This library was used for the authentication needed to access the Google APIs for connecting the Service Account with the Credentials function. A `CREDS.json` file was generated from this with the details needed for the API to access my Google account which holds the Google Sheets worksheet containing the applications data. When deploying to Heroku, this information is then stored in the config var section to ensure the application will run.  


  
# Testing  
I have created an additional file for my Manual Testing and Validation this can be found here: [TESTING.md](/TESTING.md)
  
# Creation & Deployment    
  
The below steps to creating and setting up a new Python workspace and API credentials has been guided by and adapted from the [Code Institute's](https://codeinstitute.net/ie/) Python walkthrough project 'Love Sandwiches'. Please check each step is relevant to your project needs and change the data entered to suit it.

### Creating a new repository 
<details open>
<summary>Steps to create a new repository.</summary>  

The [Code Institute's Python Essential Template](https://github.com/Code-Institute-Org/python-essentials-template) was used to create a terminal for my Python file to generate it's output. To use this template, please follow these steps:
1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above Python template repository.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In your new repository space, click the green '**Gitpod**' button to generate a new workspace.   

</details> 
  
-----  

### Activating the Google Drive & Sheets API
<details>
<summary>Steps to activate the APIs</summary>
To access the data in a Google Sheets worksheet using Python code, an API is required. Please follow these steps to set up your APIs:  

1. Navigate to the [Google Cloud Platform](https://cloud.google.com), using an email address/Google account that is registered to you alone.
2. In the Google Cloud Platform Dashboard, create a new project by clicking on the '**Select a Project**' button and choosing the '**New Project**' option. Give your new project a name and click '**Create**'. (Your access credentials are unique to each project, so create a new project for every project that you build.) 
3. Click '**Select Project**' in the blue banner to bring you to your project page.
4. Select '**APIs and Services**' from the left side menu, then select '**Library**'.
5. Use the search bar to search for the two APIs needed for this project, Google Drive API and Google Sheets API. One at time, choose the APIs from the search and click '**Enable**' on their main page. Follow the below steps for the Google Drive API, but only click '**Enable**' for the Google Sheets API. There is no need to download credentials again for it.
6. On the API overview page, click '**Create Credentials**' to generate some credentials which will allow us access to our Google Drive from our Python code.
7. Fill out the forms fields and dropdown menus with the information that is relevant to your project. For mine, I chose **Google Drive API -> Application Data -> No, I'm not using them** (regarding using Kubernetes, App Engine etc)
8. Under Service Account Details, choose a Service Account name and click '**Create**'.
9. In the Role Dropdown box choose **Basic -> Editor** then press '**Continue**'. Click '**Done**' to finish the form if you do not need to grant users access to the service account if it is a personal project.
10. On the next page, click on your new Service Account that has been created, then click on the '**Keys**' tab to '**Add Key**'. Select '**Create New Key**'.
11. Select JSON and '**Create**'. Your json file containing your API credentials will be downloaded to your machine.

</details>

-----  

### Setting up the Gitpod workspace for the APIs
<details>
<summary>Steps for workspace setup</summary>
  
1. In the new Gitpod workspace you've created with the Python Essentials template, click and drag the json file that you created in the above steps, into the Gitpod workspace.  
2. Rename it to `CREDS.json`, if you wish, and open the file. Find the client_email address you previously entered, copy it without the quotes around it.
3. In the Google Sheets file that you have created for this project, click the '**Share**' button and paste the email address into the field, choose '**Editor**', untick '**Notify People**' and click '**Share**'. This allows our project access to the spreadsheet.
4. To ensure the private credentials that you have created do not make their way to the cloud for others to view, add the `creds.json` file to your `gitignore` file before you commit any changes to your repository, and push them to the cloud.
5. Use the command `git status` to check that the `creds.json` file is not staged to be committed.

</details>  
  
-----  

### Initial Code for connecting to our API with Python
<details>
<summary>Steps to including the Python/API connection code</summary>

1. The code needed to ensure your APIs connect correctly can be found at the top of the `run.py` file connected to this project. It is important that you remember to pass the exact same name as your spreadsheet to the `SHEET = GSPREAD_CLIENT.opn('your-filename-here')` code, or else gspread will throw an error.
2. The command `pip3 install gspread google-auth` is needed to install the gspread package for handling the worksheet data and the google-auth package to allow access to the Google Sheets account via the Credentials we downloaded earlier. Use the above command in the Gitbash terminal to install.
3. Please refer to the `run.py` file for the import, SCOPE, CREDS, SCOPED CREDS, GSPREAD CLIENT, SHEET code that is needed to connect the APIs and change any data that is personal to your project.

</details>
  
-----  

### Deploying to Heroku  

Heroku has been used to deploy this project as Python is used as a back-end language. To allow for accurate testing, I deployed the project to Heroku early on using Automatic Deployment to update the program everytime new code was pushed to my GitHub repository. Here are the steps that I followed to set my project up, guidance was provided by the [Code Institute's](https://codeinstitute.net/ie/) 'Love Sandwiches' project.     

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
<details>
<summary>Create new app</summary>
<img src ="documentation/readme/heroku_1.png">
</details>  

3. Enter an app name and choose your region. Click '**Create App**'.
<details>
<summary>Enter app name</summary>
<img src ="documentation/readme/heroku_2.png">
</details>  
  
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. In KEY enter `CREDS`, in VALUE, paste in the text content of your `CREDS.json` file. Select '**Add**'.  
5. Repeat this process with a KEY:VALUE pair of `PORT` and `8000`.
6. In the Settings tab, in the Buildpack section, click '**Add Buildpack**', located near the bottom, right of the refreshed screen. One at a time, choose the '**Python**' pack, save changes, then choose the '**NodeJS**' buildpack and save changes. **NB: the Python buildpack _must_ be above the NodeJS buildpack.**
  
<details>
<summary>Choose Buildpacks</summary>
<img src ="documentation/readme/heroku_bp.png">
</details>  
  
7. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
8. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
9. Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Automatic' deployment method. Click '**Deploy Branch**'.
10. Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site.

  
-----  

### Forking the GitHub Repository

A copy of the original repository can be made through GitHub. Please follow the below steps to fork this repository:  

1. Navigate to GitHub and log in.  
2. Once logged in, navigate to this repository using this link [BakeStock Repository](https://github.com/amylour/BakeStock).
3. Above the repository file section and to the top, right of the page is the '**Fork**' button, click on this to make a fork of this repository.
4. You should now have access to a forked copy of this repository in your Github account.

-----  

### Clone this GitHub Repository

A local clone of this repository can be made on GitHub. Please follow the below steps:

1. Navigate to GitHub and log in.
2. The [BakeStock Repositiory](https://github.com/amylour/BakeStock) can be found at this location.
3. Above the repository file section, locate the '**Code**' button.
4. Click on this button and choose your clone method from HTTPS, SSH or GitHub CLI, copy the URL to your clipboard by clicking the '**Copy**' button.
5. Open your Git Bash Terminal.
6. Change the current working directory to the location you want the cloned directory to be made.
7. Type `git clone` and paste in the copied URL from step 4.
8. Press '**Enter**' for the local clone to be created.
  
<br>

# Credits

## Content References
   - gspread Documentation is used as reference material and guidance throughout the project for the manipulation of data between Python and Google Sheets: [gspread Docs](https://docs.gspread.org/en/latest/index.html)
   - Code Institute's 'Love Sandwiches' project for Google Sheets API and Creds Set-Up: [Code Institute](https://codeinstitute.net/ie/)
   - 101 Computing for the type-text effect, 'screen sleep', and 'clear screen' effects used throughout the project: [Python typing text effect](https://www.101computing.net/python-typing-text-effect/)
   - StackOverflow for providing a solution to display my Sales Data: [Adding tab for data formatting and display](https://stackoverflow.com/questions/4488570/how-do-i-write-a-tab-in-python)
   - Python enumerate tutorial by Tech with Tim for searching through Google Sheet data: [Tech with Tim Youtube](https://www.youtube.com/watch?v=-MZiQaNI0QA)
   - Python enumerate tutorial via Real Python for looping through data items: [Real Python](https://realpython.com/python-enumerate/)
   - Python zip() Function for Parallel Iteration for display of Batch and Inventory items: [Real Python](https://realpython.com/python-zip-function/)
   - Linuxhint for their Colorama tutorial and materials: [Linuxhint Colorama & Python](https://linuxhint.com/colorama-python/)  

Additional reading materials:
   - [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/) for more information about Google Sheets and Python Automation.
   - [GitHub Docs](https://docs.github.com/en) for information on cloning and forking the repository.
   - [Geeks for Geeks](https://www.geeksforgeeks.org/python-programming-language/?ref=ghm) for additional Python learning.

## Literature
I used the below book as extra learning material and reference material during the project:  

- [Python Crash Course](https://www.oreilly.com/library/view/python-crash-course/9781492071266/), Author: Eric Matthes, Publisher: No Starch Press, Year: 2019 Edition.

## Media
ASCII art was used twice in the project and were generated by:
- [ManyTools.org](https://manytools.org/hacker-tools/ascii-banner/), for the opening banner.
- [ASCII Art](https://www.asciiart.eu/), for the hidden easter egg.

## Acknowledgements  
- Many thanks to my family for their continued support when I need to talk through ideas and bugs, and for testing my work.
- Thank you to my mentor Rahul Lakhanpal for his support and guidance.
- Thanks and appreciation to my fellow Code Institute students who have offered great support. 
