# **Elimination Diet Capstone**
Track diet, gut health, and mood.

------

## Project Overview

An elimination diet capstone is a Django application for the purpose of allowing it's users to track their diet and gut health on a calendar as well as provide helpful information regarding food allergies.

**Libraries Used**
- [Django](https://www.djangoproject.com)
- [Vue](https://vuejs.org/)
- [Materialize](https://materializecss.com/)

------

## Functionality

- User System
    - Register new user
    - Log in
    - Log out
    - Edit profile
- Journal
    - Calendar
        - Select date
    - Create Entry
        - Hours slept
            - Quality of sleep
        - User weight
        - Eliminated food
            - Duration
        - Food consumed
            - Time of day
        - User mood
    - Edit Entry
- Allergen guide
    - Sidebar

------

## Data Models

**User**
- user_name (CharField)

**Journal Model**
- date_time (DateTimeField)
- food avoided (CharField)
- food consumed (Charfield)
- user_weight (IntegerField)
- mood (CharField)

------

## Schedule

- Week 1
  - [ ] create Models
  - [ ] create user system - register, login, logout, Edit Profile
- Week 2
  - [ ] Display Calendar
  - [ ] Create Journal Entry 
  - [ ] Edit Entry - Update, delete
- Week 3
  - [ ] Styling