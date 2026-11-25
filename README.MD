# Hotel Management System

A complete web-based Hotel Management System developed using **Python**, **Django**, and **SQLite** to streamline hotel operations including room inventory, room categories, customer records, room availability tracking, and reservations (check-in and check-out).

## Project Features
- **Register Hotel Rooms:** Add, view, edit, delete, search, and filter hotel rooms by number and availability status.
- **Manage Room Categories:** Create and manage room classifications (e.g., Standard, Deluxe, Suite).
- **Register Customers:** Store and manage guest details with search functionality by name or phone number.
- **Make Room Reservations:** Book available rooms for registered customers with check-in and check-out dates.
- **Check Room Availability:** Real-time dashboard overview and automatic room status updates (`Available` / `Occupied`).
- **Manage Check-In & Check-Out Records:** Track booking statuses (`Booked`, `Checked-In`, `Checked-Out`) and automatically release rooms upon check-out.
- **Staff Authentication:** Secure Login and Logout system protecting all management pages.

## Technologies Used
- **Backend:** Python 3, Django Framework
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3

## How to Run the Project Locally
1. **Clone the repository:**
   ```bash
   git clone <your-github-repository-url>
   cd HotelManagementSystem
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install Django:**
   ```bash
   pip install django
   ```
4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a staff/admin account (optional):**
   ```bash
   python manage.py createsuperuser
   ```
6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
7. **Access the application:** Open your browser and go to `http://127.0.0.1:8000/`.