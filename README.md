# 📬 Mail/SMS Spam Detection Flask API

This repository contains a Flask API for mail or SMS spam detection using a machine-learning model. The project includes pre-trained models, data preprocessing, and an API for making predictions. Below, you'll find information on how to use this code for local development, the project structure, and an explanation of the machine learning model. 


## 📦 Related Repositories
- This API is used in the [SpamWarden Chrome Extension Project](https://github.com/NotSooShariff/Mail-Spam-Classification).

## 📁 Project Structure

The project is organized as follows:

- `app.py`: The Flask application file that runs the API.
- `Mail_Spam_Detection.ipynb`: The Jupyter Notebook containing the machine learning model development and training process.
- `model.pkl`: A pre-trained machine learning model for spam detection.
- `README.md`: This readme file.
- `requirements.txt`: A file listing the required Python packages.
- `vectorizer.pkl`: A pre-trained TF-IDF vectorizer for text data.
- `API Test/`: A folder containing a test script, `test.py`, for checking if the API works or not after you have followed the steps on how to run below.

## 🚀 How to Use the Code

Follow these steps to set up and run the Mail Spam Detection Flask API locally:

1. Clone this repository:

   ```bash
   git clone https://github.com/NotSooShariff/SpamWardenAPI.git
   ```

2. Navigate to the project directory:

   ```bash
   cd mail-spam-detection
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask server by running:

   ```bash
   python app.py
   ```

   This will start the server on `http://127.0.0.1:5000`.

5. To expose the API to the web, you can use [ngrok](https://ngrok.com/). After registering for Ngrok, go to the [Setup Page](https://dashboard.ngrok.com/get-started/setup) and download and unzip the executable.
6. Launch the executable. Once the terminal pops, Configure the auth token by using the `ngrok config add-authtoken` command. Your auth token will be displayed in the same dashboard.
7. You can now expose your running Flask server to the internet using the command:

   ```bash
   ngrok http 5000
   ```

   Use the URL under "Forwarding" in ngrok to make API calls. This should look something like `https://{your-ngrok-code}.ngrok-free.app/`
8. You can test if the server is running by executing the `test.py` code I have added under the `API Test/` directory from anywhere.

Certainly! Here's an added section on the API's endpoints and example usage:

## 🌐 API Endpoints and Example Usage

The Mail Spam Detection Flask API provides the following endpoint for predicting whether a given text is likely spam or not:

- `/predict` (POST)

This endpoint accepts a JSON request containing the text data to be predicted. To use this endpoint, you should also set a request header to skip the ngrok browser warning, as ngrok may display a warning page otherwise.

**Request Header:**
```
ngrok-skip-browser-warning: true
```

**Request Body:**
```json
{
    "data": "Your text goes here. Is this a spam message?"
}
```

**Response:**
- If the response is `1`, it indicates that the text is likely spam.
- If the response is `0`, it indicates that the text is not spam.
- If there is an error, the API may respond with an appropriate HTTP status code and an error message.

### Example Usage

You can use the provided test script in the `API Test/` folder, `test.py`, to make requests to the API. Here's how to use it:

1. Ensure that the Flask API is running locally, and ngrok is set up to expose the API.

2. Navigate to the `API Test/` folder in your terminal:

   ```bash
   cd API Test/
   ```

3. Edit the script by replacing the `YourNgrokURL` and `TextTopredict`
4. Run the test script, specifying the text you want to predict:

   ```bash
   python test.py 
   ```

   This script sends a POST request to the `/predict` endpoint with the provided text and the `ngrok-skip-browser-warning` header set to `true`.

5. The script will display the API response, indicating whether the text is likely spam or not.

Example Output:
```
Prediction: 0
```

Please note that you should replace `"Your text goes here. Is this a spam message?"` with the actual text you want to predict. The script will handle the API request and response for you. Feel free to use this example to integrate the API into your own applications or scripts for spam detection.

## 🧠 Machine Learning Model Explanation

The machine learning model used for mail spam detection was developed in the `Mail_Spam_Detection.ipynb` Jupyter Notebook. Here's a summary of the steps involved in the model development:

1. **Data Cleaning**: The dataset used for training the model was loaded and cleaned. Unnecessary columns were removed, and missing values and duplicate records were handled.

2. **Exploratory Data Analysis (EDA)**: Some exploratory data analysis was performed to gain insights into the dataset. This included visualizations to understand the distribution of spam and non-spam emails.

3. **Text Preprocessing**: Text data was preprocessed by performing the following steps:
   - Converting text to lowercase.
   - Tokenizing the text into words.
   - Removing special characters, stopwords, and punctuation.
   - Stemming words to their root forms.

4. **Text Vectorization**: The preprocessed text data was transformed into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization. This step converted text data into a format suitable for machine learning.

5. **Model Building**: Several machine learning algorithms were trained and evaluated for spam detection. These algorithms included:
   - Gaussian Naive Bayes
   - Multinomial Naive Bayes
   - Bernoulli Naive Bayes
   - Support Vector Classifier (SVC)
   - Decision Tree Classifier
   - Logistic Regression
   - Random Forest Classifier
   - AdaBoost Classifier
   - Bagging Classifier
   - Extra Trees Classifier
   - Gradient Boosting Classifier
   - XGBoost Classifier

   Model performance metrics such as accuracy and precision were computed for each algorithm.

6. **Model Improvement**: The model was further fine-tuned by changing the `max_features` parameter of the TF-IDF vectorizer, scaling features, and adding the number of characters as a feature.

7. **Ensemble Models**: Ensemble models like the Voting Classifier and Stacking Classifier were explored to combine the strengths of multiple models for better performance.

8. **Model Export**: The final model, along with the TF-IDF vectorizer, was serialized and saved as `model.pkl` and `vectorizer.pkl`, respectively, for use in the Flask API.

The `app.py` file in the root directory serves as the API for making predictions with the pre-trained model. You can send POST requests to the `/predict` endpoint with text data, and the API will return a prediction of whether the text is spam or not.

## 🙏🏽 Acknowledgments

Much of the knowledge and techniques used in this project were acquired from the CampusX YouTube channel. Their educational content played a significant role in the development of this project, and we acknowledge their valuable contributions.

## 🫱🏾‍🫲🏽 Contributions Welcome

Contributions to this project are welcome! If you have ideas for improvements, bug fixes, or new features, please feel free to fork this repository, make your changes, and submit a pull request. Let's collaborate to make this project even better.
