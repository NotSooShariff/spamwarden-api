# 📬 Mail/SMS Spam Detection Flask API

This Docker container provides a Mail/SMS Spam Detection Flask API powered by a pre-trained machine learning model. It encapsulates all the necessary components, including the Flask server, pre-trained model, and dependencies, to make it easy for you to run the spam detection API in a containerized environment.


## 📦 Related Repositories
- This API is used in the [SpamWarden Chrome Extension Project](https://github.com/NotSooShariff/Mail-Spam-Classification).

## 📁 Project Structure

The project is organized as follows:

- `model/`: The directory containing the `source-model.ipynb` Jupyter Notebook with the machine learning model development and training process.
- `testcode/`: A folder containing a test script, `test.py`, for using this API.
- `app.py`: The Flask application file that runs the API.
- `requirements.txt`: A file listing the required Python packages.
- `vectorizer.pkl`: A pre-trained TF-IDF vectorizer for text data.
- `Dockerfile`: The Dockerfile used for containerizing this project.

## 🚀 How to Use the Code
To use this Docker container, follow these steps:

### Step 1: Pull the Docker Image

Use the following command to pull the Docker image from Docker Hub:

```bash
docker pull notsooshariff/spamwarden
```

### Step 2: Run the Docker Container

Once the image is downloaded, you can run the Docker container using the following command:

```bash
docker run -p 5000:5000 notsooshariff/spamwarden
```

This command maps port 5000 from the container to port 5000 on your host machine. Adjust the port mapping as needed to match your desired configuration.

### Step 3: Access the API

The SpamWarden API is now running inside the Docker container and accessible at the following URL:

```
http://localhost:5000
```

You can make API requests to this URL to predict whether a given text is likely spam or not.

## 🌐 API Endpoints and Example Usage

The Mail Spam Detection Flask API provides the following endpoint for predicting whether a given text is likely spam or not:

- `/predict` (POST)

This endpoint accepts a JSON request containing the text data to be predicted. 

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

You can use the provided test script in the `testcode/` folder, `test.py`, to make requests to the API. Here's how to use it:

1. Ensure that the Docker Container is running locally, and is set up to expose the API at the desired port.

2. Navigate to the `testcode/` folder in your terminal:

   ```bash
   cd testcode/
   ```

3. Edit the script by replacing the `URL` and `TextToPredict` in the script provided
   ```python
   import requests

    data = {
        'data': 'Your text goes here. Is this a spam message?'
    } 
    
    response = requests.post('http://localhost:5000/predict', json=data)
    
    if response.status_code == 200:
        try:
            result = response.json()
            print('Prediction:', result['prediction'])
        except ValueError:
            print('Response does not contain valid JSON data.')
    else:
        print('Error:', response.status_code)
    
   ```
4. Run the test script, specifying the text you want to predict:

   ```bash
   python test.py 
   ```

   This script sends a POST request to the `/predict` endpoint with the provided text.

5. The script will display the API response, indicating whether the text is likely spam or not.

Example Output:
```
Prediction: 0
```

Please note that you should replace `"Your text goes here. Is this a spam message?"` with the actual text you want to predict. The script will handle the API request and response for you. Feel free to use this example to integrate the API into your own applications or scripts for spam detection.

## 🧠 Machine Learning Model Explanation

The machine learning model used for mail spam detection was developed in the `source-model.ipynb` Jupyter Notebook. Here's a summary of the steps involved in the model development:

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

I have to acknowledge the [CampusX YouTube channel](https://www.youtube.com/@campusx-official) for much of the insights on how to make this ML Model better. And also the [Fireship YouTube Channel](https://www.youtube.com/@Fireship) for the most easy to follow along tutorials and explanations on Docker. Do check them out.

## 🫱🏾‍🫲🏽 Contributions Welcome

Contributions to this project are welcome! If you have ideas for improvements, bug fixes, or new features, please feel free to fork this repository, make your changes, and submit a pull request. Let's collaborate to make this project even better.
