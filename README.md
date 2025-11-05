A simple Flask-based Student Handwritten Assignment Submission Portal (demo project) with features:

Upload handwritten assignments

View uploaded assignments (for teacher)

Delete submissions (simple POST action)

Data stored in assignment_data.json (flat-file for demo)

🔧 Run locally

Create virtualenv:
python -m venv venv && source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate                             # (Windows)

Install requirements:
pip install -r requirements.txt

Run:
python app.py

Open:
http://127.0.0.1:5000

🗒️ Notes

This is a simple educational demo project.

For production, use a database (e.g., SQLite/MySQL), add authentication (login system), and handle secure file uploads.
