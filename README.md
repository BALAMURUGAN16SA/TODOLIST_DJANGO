The project focuses on using Django as a backend framework to build a webapp.

# Flow of use:
  ->Display home page
  ->Access pages using Sidebar and Navbar :
   a) Sidebar:
      .Asks user to signin/signup before accessing
      .Returning to signin/signup page
        If has an account -> signin
        If doesn't have an account -> signup -> signin
      .Return to Home page
      .Accessing content:
        .Overview : Displays total Lists and total Tasks
        .View     : Displays Lists and no.of tasks, no.of.completed and no.of.pending
                    Clicking on lists returns to Tasks page, where user can add new tasks and edit previous tasks and save
        .Create   : Create new List, and return to Tasks page, where user can add new tasks and edit previous tasks and save

   b) NavBar:
      .View User profile
      .SignOut

# Requirements:
  ->django
  ->crispy-forms
  ->crispy-bootstrap

# Project name:
  ->todolist
  
# App names:
  ->content (to display user pages)
  ->user  (to display signin/signup pages)
  ->todolist (default app)

