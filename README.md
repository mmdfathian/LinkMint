# LinkMint 🚀

A fast, scalable, and production-ready URL shortener built with FastAPI and SQLite. Mint your links into short, trackable URLs.

## ✨ Features

*   **Shorten URLs:** Create short, unique links from long URLs.
*   **Redirect Tracking:** Automatically redirects short URLs to their original destination.
*   **Click Analytics:** Tracks the number of clicks for each short URL.
*   **Clean API:** A well-documented RESTful API for easy integration.
*   **Extensible:** Designed for easy integration of advanced features like authentication, caching, and custom domains.

## 🛠️ Tech Stack

*   **Backend:** Python, FastAPI
*   **Database:** SQLite (for MVP), easily switchable to PostgreSQL
*   **ORM:** SQLAlchemy
*   **Deployment:** Uvicorn

## 📂 Project Structure
linkmint/

├── app/

│ ├── init.py

│ ├── main.py # FastAPI application instance

│ ├── database.py # Database connection and session management

│ ├── models.py # SQLAlchemy database models

│ ├── schemas.py # Pydantic schemas for request/response validation

│ └── utils.py # Utility functions (e.g., short code generation)

├── requirements.txt # Project dependencies

├── .gitignore # Files/directories to ignore in Git

└── README.md # This README file


## 🚀 Getting Started

### Prerequisites

*   Python 3.7+
*   pip
 
