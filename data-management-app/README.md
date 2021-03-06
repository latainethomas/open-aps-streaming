# Downloader Web App

## Purpose
Prior to this application, OpenAPS staff relied on manual processes to extract and distribute the data held within the OpenAPS Data Commons to researchers. The purpose of this application therefore was to provide a portal which could automate this process, with the intention of reducing waste and improving accessibility for researchers.

## Pages

-   **Download page**: This page contains a form that researchers can use to download data sourced from the Data Commons. This form includes options which allow researchers to specify the filetype and records they wish to source, and filter by date-range.

<p align="center">
  <img src="https://github.com/Mudano/open-aps-streaming/blob/downloader-app/data-management-app/downloader/static/images/git_images/downloader.JPG" width="60%">
</p>

-   **Analytics Page**: Through a series of dashboards, this page provides information relating to the demographics and metadata of our donatees, and also an analytical breakdown of key metrics related to our donatees **APS** data, such as trends in blood-glocose level throughout the day.

<p align="center">
  <img src="https://github.com/Mudano/open-aps-streaming/blob/downloader-app/data-management-app/downloader/static/images/git_images/analytics.JPG" width="60%">
</p>

-   **Admin Page**: This page contains the core admin functioning of the app, namely where users can be added/removed, and have their applications responded to. There is also a user metrics table on this page that shows how much users have downloaded, number of downloads, login count and last signin.

<p align="center">
  <img src="https://github.com/Mudano/open-aps-streaming/blob/downloader-app/data-management-app/downloader/static/images/git_images/admin.JPG" width="60%">
</p>

-   **Register Page**: This page contains the registration form, which records the following items from the user: name, email, phone, organisation, whether IRB approval is needed, and the justification for requesting access.

<p align="center">
  <img src="https://github.com/Mudano/open-aps-streaming/blob/downloader-app/data-management-app/downloader/static/images/git_images/register.JPG" width="60%">
</p>



## Deployment


## Dependencies/Requirements

The application is ran with **Python 3.6**, with the <a href="https://github.com/Mudano/open-aps-streaming/blob/master/data-management-app/setup/requirements.txt">requirements.txt</a> file in the setup folder specifying all the required packages. The application is based on a PostgreSQL database and uses SQLAlchemy as an interaction layer.

The dependencies required for the frontend of the application are specified in the `<head>` tag of the apps <a href="">layout.html</a> template.


## App Functioning

### Downloading

The process used for generating files for users to download is as follows:

1. User specifies the following parameters on the download page:

    - Filetype - Either **json** or **csv**
    - Date-range - Date-picker allowing users to limit the time-period
    - Entity - Can be **All**, **Entries**, **Treatments**, **Device**, or **Profiles** (see <a href="https://github.com/danamlewis/OpenHumansDataTools/blob/master/NS-data-types.md">here</a>)

2. Records are extracted from the database according to user parameters

3. Pandas is used to convert the records into a **json** or **csv** file, with 4 files rather than 1 being produced if **all** is selected

4. The generated file/s is then moved to a **.zip** folder, which is sent to be downloaded by the user

### Registration

Excluding the admin account which is created during the applications initialisation, users are added via the following process:

1. User applies for access to the site via  the 'Register' link on the login page, and is required to fill out a form containing information such as why they require access

2. An admin receives an email with the information specified in the form, and can then proceed to approve/reject this application using the 'Applications' button on the admin page

3. Upon accepting the application, the applicant will receive an email containing a link to the site's verification page, as well as a verification code

4. After entering the verification code and assigning a password, the user will be able to login and access the rest of the sites content

**Alternatively**: An admin can add a user directly via the 'Add User' button on the admin page. This skips the first two steps in the above process, and proceeds directly to sending the specified user an email with a verification code and link.

### Password Reset

Users can reset their password's by clicking on the 'Reset Password' link on the home page. This will ask them to enter their email, and a reset link will be sent containing a verification code and a link to the verification page.


### Removing User

Admin's can remove users by proceeding to the admin page, selecting the users email from the list next to the 'Remove User' button, and then pressing this button. This will not delete the user, instead it will deactivate their account, and they will have to re-register before they can can access the site again.


## Security

The passwords and tokens required to run the app are sourced from the following environment variables:

- **DOWNLOADER_SECRET_KEY** - The secret key which is used when initialising the app
- **POSTGRES_ (USER, PASSWORD, HOST, PORT, DB)** - Credentials for connecting to the database
- **DOWNLOADER_APP_EMAIL** - The email address used by the app for messaging users/admins
- **DOWNLOADER_EMAIL_PASSWORD** - The password for above email
- **DOWNLOADER_PUBLIC_URL** - The public URL used by the app
- **DOWNLOADER_ADMIN_EMAIL** - The email to notify when a new user registers
- **METABASE_SECRET_KEY** - The secret key used for embedding our Metabase dashboards
- **METABASE_URL** - The URL of a hosted metabase instance
- **DOWNLOADER_SLACK_KEY** - A Slack App API key used for sending error notifications to Slack
