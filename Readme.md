# Project Name: Django HOS Scheduler

## Description

This Django project is designed to manage driving schedules and ensure compliance with the FMCSA Hours of Service (HOS) regulations. It includes functionalities for optimizing driving schedules and detecting potential HOS violations.

## Module 1 Features

- **Schedule Optimization**: Validates driving schedules against HOS regulations, ensuring they do not exceed the 14-hour daily limit and the 11-hour driving limit.
- **HOS Violation Detection**: Detects potential HOS violations based on given driving and rest times, and provides recommendations to remain compliant.
- **API Endpoints**: Provides RESTful endpoints for clients to interact with the schedule optimization and violation detection functionalities.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Django 3.2.23
- Requests library

### Installation

1. **Extract the ZIP file:**

   - Unzip the project files into a directory of your choice.

2. **Set up a virtual environment (optional but recommended):**

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install required packages:**

   ```
   pip install -r requirements.txt
   ```

### Setting up the environment

1. **Create a `.env` file in the project root directory and update it with necessary configurations:**

   ```
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   PROLOGS_TOKEN_URL=https://identity.prologs.us/connect/token
   ```

2. **Database Setup:**

   - This project uses SQLite by default for development. If you need to configure another database, update your `settings.py` accordingly.

### Running the Project

1. **Run database migrations:**

   ```
   python manage.py migrate
   ```

2. **Start the development server:**

   ```
   python manage.py runserver
   ```

3. **Access the application through your web browser:**

   - Open `http://127.0.0.1:8000/` to interact with the application.

   4. Access GUI

      [Schedule Optimization](http://127.0.0.1:8000/scheduler/form/)

   5. `http://127.0.0.1:8000/scheduler/form/`

### Manual Testing

#### Typical Scenarios

- **Schedule Optimization - Valid Schedule:**
  `curl "http://127.0.0.1:8000/scheduler/optimize/?pickup_time=2023-07-10T09:00:00&dropoff_time=2023-07-10T19:00:00&last_rest_time=2023-07-10T01:00:00" `
- **Schedule Optimization - Exceeds Daily Driving Limit** Test a schedule that exceeds the daily driving limit of 11 hours.

`    curl "http://127.0.0.1:8000/scheduler/optimize/?pickup_time=2023-07-10T05:00:00&dropoff_time=2023-07-10T17:30:00&last_rest_time=2023-07-10T01:00:00"`

- **Schedule Optimization - Exceeds 14-Hour Window** Test a schedule that exceeds the 14-hour window from the start of the day.

  `curl "http://127.0.0.1:8000/scheduler/optimize/?pickup_time=2023-07-10T06:00:00&dropoff_time=2023-07-10T21:00:00&last_rest_time=2023-07-10T06:00:00"`

- **HOS Violation Detection - No Violation**

`    curl "http://127.0.0.1:8000/scheduler/hos_violation/?driving_time=9&hours_since_last_rest=3"`

- **HOS Violation Detection - Violation Detected**

  `curl "http://127.0.0.1:8000/scheduler/hos_violation/?driving_time=12&hours_since_last_rest=4" `

- Use these commands to manually test the API endpoints via `curl` or a similar tool to verify their functionality.

## Contributing

While contributions are welcome, please manually test any changes using the above commands to ensure functionality remains consistent.
