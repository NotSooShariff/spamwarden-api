from flask import Flask, request, jsonify
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)

# Load the TF-IDF vectorizer and the machine learning model
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

nltk.download('punkt')
nltk.download('stopwords')
ps = PorterStemmer()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the text data from the request
        data = request.json['data']

        # Preprocess the input text data
        preprocessed_data = transform_text(data)

        # Vectorize the preprocessed data
        vectorized_data = vectorizer.transform([preprocessed_data])

        # Make a prediction
        prediction = model.predict(vectorized_data)

        # Return the prediction as JSON
        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)})

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

if __name__ == '__main__':
    app.run(debug=False)
