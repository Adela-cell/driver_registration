# **Driver Registration API**

This API is built using **FastAPI** and **MongoDB**. It provides endpoints to register a driver and retrieve driver details using their phone number.

## **Features**
- Register a new driver.
- Retrieve a driver's details using their unique phone number.
- Input validation and structured error responses.

---

## **Requirements**
Before running the application, ensure you have the following installed:
1. **Python 3.8+**
2. **MongoDB** (running locally or accessible remotely)
3. **pip** (Python package manager)

---

## **Setup and Installation**

### 1. Clone the Repository
```bash
git clone <repository_url>
cd driver_registration
```

### 2. Create a Virtual Environment
Create and activate a virtual environment to isolate dependencies:
```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install the required libraries using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Configure MongoDB
Ensure MongoDB is running locally or update the connection string in `database.py`:
```python
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")  # Update this if needed
db = client["driver_database"]
```

---

## **Running the API**

Start the server with the following command:
```bash
uvicorn app.main:app --reload
```

### Output:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

---

## **Usage**

### Base URL
- **Local**: `http://127.0.0.1:8000`

### Endpoints
1. **Register a Driver**
   - **URL**: `POST /drivers/register`
   - **Description**: Registers a new driver.
   - **Request Body** (JSON):
     ```json
     {
       "name": "Samuel Brian",
       "phone":"9011262024",
       "email": "sammybrian@gmail.com",
       "license_number": "AB23671",
       "address": "41 ademola Street"
     }
     ```
   - **Response** (Success):
     ```json
     {
       "message": "Driver registered successfully!",
       "driver": {
         "name": "Samuel Brian",
         "phone": "9011262024",
         "email": "sammybrian@gmail.com",
         "license_number": "AB23671",
         "address": "41 ademola Street"
       }
     }
     ```
   - **Error Example** (If driver exists):
     ```json
     {
       "detail": "A driver with this phone number already exists."
     }
     ```

2. **Retrieve a Driver**
   - **URL**: `GET /drivers/{phone}`
   - **Description**: Fetches driver details using their phone number.
   - **Path Parameter**:
     - `phone`: The phone number of the driver to retrieve.
   - **Response** (Success):
     ```json
     {
       "message": "Driver found!",
       "driver": {
         "_id": "648a6c25e9879c3ab00f2032",
         "name": "Samuel Brian",
         "phone": "9011262024",
         "email": "sammybrian@gmail.com",
         "license_number": "AB23671",
         "address": "41 ademolaStreet"
       }
     }
     ```
   - **Error Example** (If driver not found):
     ```json
     {
       "detail": "Driver not found."
     }
     ```

---

## **Testing the API**

### Using Swagger UI
1. Navigate to `http://127.0.0.1:8000/docs`.
2. Test the endpoints interactively.

### Using Postman
1. Import the following endpoints:
   - **POST /drivers/register**
   - **GET /drivers/{phone}**
2. Send requests and view responses.

---

## **File Structure**
```plaintext
driver_registration/
├── app/
│   ├── __init__.py          # Initializes the app package
│   ├── database.py          # MongoDB connection setup
│   ├── models.py            # Pydantic models
│   ├── routes.py            # API endpoints
│   ├── main.py              # FastAPI application setup
├── requirements.txt         # List of dependencies
├── README.md                # Documentation (this file)
```
