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

### __Unfixed Bugs__

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, the paucity of time and difficulty understanding the implementation is not a valid reason to leave bugs unfixed.

## __Deployment__

This section should describe the process you went through to deploy the project to a hosting platform (e.g., GitHub).

- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab.
  - From the source section drop-down menu, select the Master Branch.
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - insert_live_link_here

## __Credits__

- Bootstrap CSS Framework: [https://getbootstrap.com/](https://getbootstrap.com/)
- Font Awesome Icons: [https://fontawesome.com/](https://fontawesome.com/)
- Google Fonts: [https://fonts.google.com/](https://fonts.google.com/)

### __Media__

- Photos and images on page are from [Pexels](https://www.pexels.com/)
- Favicon from [iconarchive](https://www.iconarchive.com/)

Website created by [Pierre Slagbrand](https://github.com/Pierreslag).