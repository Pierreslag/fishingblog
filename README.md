# __Swedish Angler's Diary__

The idea for "Swedish Angler's Dairy" is to document the owner's journey of discoveries and adventures here in Sweden. And for members to be able to leave feedback and keep track of their own fishing trips.

![Responsive Mockup](/static/images/readmeimages/responsive.jpg)

## __Features__

### __Existing Features__

- __Blogposts__
  - For the owner to share his journey and for fishing enthusiasts to read.
  - Eduacantion and fun reading wile also getting some tips.

![Feature Image](/static/images/readmeimages/posts.jpg)

- __Blogposts edit/delete__
  - For the owner to edit and delete his posts.
  - To keep relative information up to date.

![Feature Image](/static/images/readmeimages/editpostsadmin.jpg)

- __Fishing Journal__
  - For members to keep a private fishing journal of their fishing information.
  - Easy way to keep track of all fishing trips.

![Feature Image](/static/images/readmeimages/journal.jpg)

- __Contact__
  - For visitors and members to be able to contact owner.
  - Leave feedback or ask questions

![Feature Image](/static/images/readmeimages/contact.jpg)

- __Sign in/up/out__ (similar layout)
  - For visitors and members to be able to login, logout and signup.
  - To become a member of the blog

![Feature Image](/static/images/readmeimages/register.jpg)

### __Features Left to Implement__

- User profile to personalize the page abit.

## __Agile Development__
Started the agile aproach with thinking about what this website / blog is going to need. Put it down on my notes as a small draft and then got to work with adding the diffrent user stories. Was aiming to get 12 of them.
Links to the user stories below!
### __Complete User Stories__
- [USER STORY: Intuitive and Accessible Front-End Design](https://github.com/Pierreslag/fishingblog/issues/1)
- [USER STORY: User Account Sign-Up](https://github.com/Pierreslag/fishingblog/issues/2)
- [USER STORY: Social Media Integration](https://github.com/Pierreslag/fishingblog/issues/3)
- [USER STORY: Contact Administrator/Author](https://github.com/Pierreslag/fishingblog/issues/4)
- [USER STORY: View List of Posts](https://github.com/Pierreslag/fishingblog/issues/5)
- [USER STORY: Like a Post](https://github.com/Pierreslag/fishingblog/issues/6)
- [USER STORY: Log Out](https://github.com/Pierreslag/fishingblog/issues/7)
- [USER STORY: Comment on a Post](https://github.com/Pierreslag/fishingblog/issues/9)
- [USER STORY: Manage Fishing Journal Entries (CRUD)](https://github.com/Pierreslag/fishingblog/issues/12)
- [USER STORY: Create and Publish New Posts](https://github.com/Pierreslag/fishingblog/issues/13)
- [USER STORY: Edit or Update Existing Posts](https://github.com/Pierreslag/fishingblog/issues/14)

### __In Progress User Stories__
- [USER STORY: TESTING](https://github.com/Pierreslag/fishingblog/issues/16)

### __Incomplete User Stories__
- [USER STORY: Sort Posts](https://github.com/Pierreslag/fishingblog/issues/8)

## __Custom Model__
### __FishingJournalEntry__

| Field         | Type              |
|---------------|-------------------|
| id            | AutoField (PK)    |
| user          | ForeignKey (FK)   |
| title         | CharField         |
| location      | CharField         |
| date          | DateField         |
| catch_details | TextField         |
| notes         | TextField (optional) |

### __ContactMessage__

| Field          | Type              |
|----------------|-------------------|
| id             | AutoField (PK)    |
| name           | CharField         |
| email          | EmailField        |
| subject        | CharField         |
| message        | TextField         |
| created_on     | DateTimeField     |

## __Testing__

### Manual Testing Summary

| Functionality                  | Test Result       |
|--------------------------------|-------------------|
| Sign In                        | Passed            |
| Sign Out                       | Passed            |
| Sign Up                        | Passed            |
| Register                       | Passed            |
| Contact Us                     | Passed            |
| Comment                        | Passed            |
| Like                           | Passed            |
| Dislike                        | Passed            |
| Add Entry                      | Passed            |
| Edit Entry                     | Passed            |
| Delete Entry                   | Passed            |
| Pagination                     | Passed            |
| Social Links                   | Passed            |
| Navigation Bar                 | Passed            |
| Post a Post                    | Passed            |
| Edit a Post                    | Passed            |
| Delete a Post                  | Passed            |
| Responsiveness for Devices     | Passed            |
| Alert Messages                 | Passed            |

### __Validator Testing__

- HTML
  - No errors were returned when passing through the official [W3C validator](insert_html_validator_url_here)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](insert_css_validator_url_here)

### __Lighthouse Testing__

- base.html ![base.html](/static/images/readmeimages/lighthousefirst.jpg)

- entry_base.html ![base.html](/static/images/readmeimages/lighthouseentrypage.jpg)

## __Deployment__

Step 1: Set up your local project
1. Create a new project or use an existing one on your local machine. Make sure it has all the necessary code.

Step 2: Set up a GitHub repository
1. If you don't have a GitHub account, sign up for one.
2. Create a new repository on GitHub to host your project.
3. Push your local project to the newly created GitHub repository.

Step 3: Configure environment variables on Heroku
1. Sign in to your Heroku account or create one if you don't have it.
2. Create a new Heroku app by clicking the "New" button and selecting "Create new app."
3. Under the "Settings" tab, click on "Reveal Config Vars."
4. Add the necessary environment variables, such as CLOUDINARY_URL, DATABASE_URL, PORT etc.

Step 4: Deploy your app to Heroku
1. Connect your Heroku app to your GitHub repository. Under the "Deploy" tab, choose "GitHub" as your deployment method and link it to the appropriate repository.
2. Choose the branch you want to deploy (usually the main/master branch).
3. Enable automatic deployments if you want your app to be automatically updated whenever you push changes to the selected branch on GitHub.
4. Click "Deploy Branch" to initiate the deployment process.

Step 5: Verify your deployment
1. Once the deployment is complete, Heroku will provide you with the URL of your deployed app.
2. Open the provided URL in your web browser to ensure that your app is working correctly.

That's it! Your app should now be deployed. Any changes you push to the linked GitHub repository will trigger automatic updates to your deployed app.

## __Credits__

- Bootstrap CSS Framework: [https://getbootstrap.com/](https://getbootstrap.com/)
- Font Awesome Icons: [https://fontawesome.com/](https://fontawesome.com/)
- Google Fonts: [https://fonts.google.com/](https://fonts.google.com/)

### __Media__

- Photos and images on page are from [Pexels](https://www.pexels.com/)
- Favicon from [iconarchive](https://www.iconarchive.com/)

Website created by [Pierre Slagbrand](https://github.com/Pierreslag).