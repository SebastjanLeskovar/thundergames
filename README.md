# Thunder Games
A website for all your favourite :video_game: video games  :video_game:.

Start of project: 4 February 2019.  
Initial push: 4 February 2019.

Sebastjan Leskovar | [sebastjan.leskovar@gmail.com](mailto:sebastjan.leskovar@gmail.com) | [github.com/SebastjanLeskovar](https://github.com/SebastjanLeskovar)

Link to repository: [https://github.com/SebastjanLeskovar/thundergames](https://github.com/SebastjanLeskovar/thundergames)  
Link to website: [thundergames.pythonanywhere.com](thundergames.pythonanywhere.com)


## Getting Started

### Prerequisites

As of version V4.5, the following prerequisites are necessary to run this website:
- Python 3.7
- Django 2.1.5
- Pillow 5.4.1
- Django Registration 3.0
- Django REST Framework 3.9.1

Previous versions of listed software has not been tested.  
Please check the file *requirements.txt* a full list of prerequisites.

### Installation

1. Open the app repository at [github.com/SebastjanLeskovar/thundergames](https://github.com/SebastjanLeskovar/thundergames).

2. Save the file 'thundergames-master.zip' to your PC by clicking the green button *Clone or download* and then *Download ZIP*.

3. Extract the files.

You can now inspect the source code.

### Start the website on localhost

1. Use the <b>Command Prompt</b> to navigate to the root of the unziped folder (e.g., *cd \thundergames-master*).

2. Install all the required prerequisites from *requirements.txt* with the following command:
```bash
pip install -r requirements.txt
```
Using virtual environment is advised.

3. Start the Django built-in server with:
```bash
python manage.py runserver
```

4. You will receive an error message saying "You have 16 unapplied migration(s)." Do not worry, you can easily apply the migrations with the following command:
```bash
python manage.py migrate
```
You can now safely start the app again with ```python manage.py runserver```.

Please note an internet connection is required to load CSS, JavaScript, jQuery and Popper (CDN). Without a connection, the website will work without any formatting.

### How to use

4. After starting the website, open your web browser.

5. Visit the following address: http://127.0.0.1:8000/.

## App

### Basic functionality

This website lists games, main genres and subgenres. Users are able to add their own items and edit and delete them.

The Main menu contains four buttons:
- **Home** (links to homepage)
- **Games** (opens a list of all games)
- **Main genres** (opens a list of all main genres)
- **Subgenres** (opens a list of all subgenres)

On each of these lists, the items can be opened. All items are also listed on the homepage.

After the visitor creates an account, two more buttons will become visible: **API** and **Contacts**.

### Authentication

Anonymous users can check the site's contents, but cannot add, edit or delete them. To do that, please register and login with your account. User authentication is also mandatory to access API endpoints.

### API

Details how to access API endpoints is listed on link [thundergames.pythonanywhere.com/api/](thundergames.pythonanywhere.com/api/).

## Versioning

### TBD

- Import main genres and subgenres from one of official lists.

### V4.5

- API (GET endpoints).

### V4.0

- User authentication (register and login forms).

### V3.1
- Ability to add images.

### V3.0

- Bootstrap.

### V2.0

- Ability for the user to add, edit and delete his or her own items.

### V1.0

- Working version to be deployed to pythonanywhere.com.
- Database containing main genre, subgenre and game fields.
- Completed draft of README.md.

## Bugs and Issues

<b>Date spoted</b>:  
<b>Level</b>:  
<b>Description</b>:  
<b>Explanation</b>:  

## Author

Sebastjan Leskovar | [sebastjan.leskovar@gmail.com](mailto:sebastjan.leskovar@gmail.com) | [github.com/SebastjanLeskovar](https://github.com/SebastjanLeskovar)

## License

This project is licensed under the MIT License - see the LICENSE file for more details.
