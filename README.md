![Screenshot (1)](https://github.com/user-attachments/assets/e215f411-94be-4747-894f-56c17d96ed59)

Follow these steps to set up the project locally:
1. **Clone the repository:**

    git clone https://github.com/praveensolanki1/task_manager.git
    cd task_manager
    
2. **Create a virtual environment and activate it:**
    python3 -m venv venv
    venv\Scripts\activate
    
3. **Install the required dependencies:**

    pip install -r requirements.txt

4. **Apply the migrations:**
   
    python manage.py migrate
   
5. **Run the development server:**

    python manage.py runserver

    The server will start on http://127.0.0.1:8000/

## Running the Tests

To run tests, use:

python manage.py test
