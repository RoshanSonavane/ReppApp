# Real Estate Price Prediction

## Project Overview
The Real Estate Price Prediction project is a live web application designed to predict property prices based on various factors such as location, size, and amenities. This project leverages machine learning algorithms to provide accurate price estimations, helping users make informed decisions in the real estate market.

## Features
- **Machine Learning Integration**: Utilizes advanced machine learning models to predict real estate prices.
- **User-Friendly Interface**: Simple and intuitive front-end design, making it easy for users to input property details and obtain price predictions.
- **Real-Time Predictions**: Provides instant predictions based on the data provided by the user.
- **Scalable Database**: Uses SQLite3 for managing property data efficiently.

## Technologies Used
- **Front-End**: HTML, CSS
- **Back-End**: Python, Django Framework
- **Database**: SQLite3
- **Machine Learning**: Scikit-learn for model development and deployment

## How It Works
1. **Data Collection**: User inputs property details such as location, area, and other relevant features.
2. **Model Processing**: The application processes this data through a trained machine learning model.
3. **Price Prediction**: The model predicts the property's price based on the input data, which is then displayed to the user.

## Installation and Setup
To run this project locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/real-estate-price-prediction.git
    ```
2. Navigate to the project directory:
    ```bash
    cd real-estate-price-prediction
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Django development server:
    ```bash
    python manage.py runserver
    ```
5. Open your browser and go to `http://127.0.0.1:8000/` to access the application.

## Project Structure
- `real_estate_price_prediction/`: Main Django project directory
- `templates/`: Contains HTML templates for the web pages
- `static/`: Stores static files like CSS and JavaScript
- `model/`: Contains the machine learning model used for prediction
- `db.sqlite3`: SQLite database file

## Contributing
Contributions are welcome! If you have any ideas or improvements, feel free to submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any queries or support, please reach out to me at [roshan742446@gmail.com](mailto:roshan742446@gmail.com).
