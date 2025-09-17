# Lost and Found Web App

A simple **Flask + SQLite** based web application to report, search, and
manage lost & found items.\
This project is designed for students or small communities to track
their belongings easily.

------------------------------------------------------------------------

## 🚀 Features

-   Add lost items with name, description, and contact info.
-   Search items by name, description, or contact.
-   Mark lost items as **Found** (automatically records found date).
-   View lost items (active reports) and found items (past records)
    separately.
-   Clear all items (with confirmation).
-   Responsive UI styled with custom CSS.

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Backend:** Python, Flask
-   **Database:** SQLite
-   **Frontend:** HTML, CSS (Jinja2 templating)

------------------------------------------------------------------------

## 📂 Project Structure

    .
    ├── app.py                # Main Flask application
    ├── lostfound.db          # SQLite database file (created automatically)
    ├── templates/            # HTML templates
    │   ├── index.html        # Homepage: list & search items
    │   └── add_item.html     # Form to report lost items
    ├── static/               # Static files (CSS, images, JS)
    │   └── style.css         # Styling for the app
    └── README.md             # Project documentation

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1. Clone the Repository

``` bash
git clone https://github.com/your-username/lost-found-app.git
cd lost-found-app
```

### 2. Create a Virtual Environment (Optional but recommended)

``` bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies

``` bash
pip install flask
```

### 4. Run the Application

``` bash
python app.py
```

The app will start at: **http://127.0.0.1:5000/**

------------------------------------------------------------------------

## 📖 Usage Guide

### Adding a Lost Item

-   Go to `Add New Item`
-   Fill in **name**, **description**, and **contact info**
-   Submit → item appears in the Lost Items list

### Marking an Item as Found

-   Click **Mark as Found** on a lost item
-   Item will move to the Found Items list with a timestamp

### Searching Items

-   Use the search bar to filter by **name, description, or contact**

### Clearing All Items

-   Click **Clear All** (you'll be asked for confirmation)
-   Removes all entries from the database

------------------------------------------------------------------------

## 🖼️ Screenshots
![Screenshot_17-9-2025_125735_127 0 0 1](https://github.com/user-attachments/assets/3066eb5b-0612-4429-b441-1c1b467f569c)
![Screenshot_17-9-2025_125728_127 0 0 1](https://github.com/user-attachments/assets/da1fe288-52b6-4630-b786-590a5cbba2bd)



------------------------------------------------------------------------

## 🤝 Contributing

Pull requests are welcome! If you'd like to add features or fix issues,
feel free to fork the repo and submit a PR.

------------------------------------------------------------------------

## 📜 License

This project is open-source and available under the [MIT
License](LICENSE).
