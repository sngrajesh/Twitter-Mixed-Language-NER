# 🌍 Predominant Language Detection and NER for Code-Mixed Twitter Data 📝

## 🚀 Overview
This project focuses on processing code-mixed Twitter data using state-of-the-art NLP techniques. The pipeline consists of:
1. **🔍 Fine-tuned mBERT**: Detecting the predominant language in a given code-mixed tweet.
2. **🌐 NLLB (No Language Left Behind)**: Translating the detected language into a monolingual tweet.
3. **📌 Fine-tuned IndicBERT**: Performing Named Entity Recognition (NER) on the translated tweet using a dataset comprising Hindi, Marathi, Telugu, and Gujarati.

## ⚙️ Workflow
### 1. **🧠 Predominant Language Detection**
- Used a fine-tuned **mBERT (Multilingual BERT)** model.
- Trained on **code-mixed Twitter data** from the **Samanantar dataset** to identify the dominant language.

### 2. **🗣️ Translation to Predominant Language**
- Implemented **NLLB (No Language Left Behind)** to translate tweets into the identified predominant language.
- Ensures high-quality translations while maintaining the original context.

### 3. **📝 Named Entity Recognition (NER)**
- Employed a **fine-tuned IndicBERT** model.
- Trained on a multilingual dataset covering **Hindi, Marathi, Telugu, and Gujarati**.
- Identifies named entities such as **👤 Persons, 🏢 Organizations, 📍 Locations, and more**.

## 📊 Dataset
- The dataset consists of code-mixed tweets with annotations for language detection and named entity recognition.
- **📚 Samanantar dataset** was used for training the models, ensuring a robust multilingual representation.
- NER dataset includes labeled data in **Hindi, Marathi, Telugu, and Gujarati**.

## 🎯 Model Training
- **🧩 mBERT** fine-tuned for language detection.
- **🌍 NLLB** used for high-quality translations.
- **🔠 IndicBERT** fine-tuned for NER tasks using the annotated dataset.

## 🛠️ Installation & Usage
### 📌 Prerequisites
Ensure you have the following installed:
- 🐍 Python 3.8+
- 🔥 PyTorch / TensorFlow
- 🤗 Hugging Face Transformers
- 📜 SentencePiece
- 🎭 Fairseq (for NLLB)

## 🛠️ Implementation & Tools
- **Languages & Frameworks: Python 3.8+, PyTorch/TensorFlow, Hugging Face Transformers, SentencePiece, and Fairseq.**
- **Web Deployment: The project is deployed as a Flask web application, which serves as the user interface for real-time processing of code-mixed tweets. The Flask app loads the fine-tuned mBERT, NLLB, and 
     IndicBERT models and exposes a RESTful API for users to submit tweets and retrieve predictions.**
- **Development Platforms: Developed using Python, Jupyter Notebook, and Google Colab.**
- **Hardware Configuration: Tested on systems with NVIDIA RTX 3050Ti GPU, 16 GB RAM, and a Quad-core CPU.**

## 🚀 API Deployment with Flask
Our integrated Flask application enables seamless real-time analysis:

- **User Interface: Provides a web-based form for users to input tweets.**
- **Model Serving: Upon receiving an input, the Flask API sequentially applies language detection, translation, and NER to return structured results.**

## 📈 Results
- **✅ Predominant language detection on Code-Mixed texts**.
- **🌟 Improved translation quality** using NLLB.
- **🚀 High performance in NER** for Indic languages.

## 🔮 Future Improvements
- 🌏 Extend NER to cover more Indic languages.
- 📢 Enhance domain adaptation for informal Twitter data.
- 🔄 Improve translation post-processing to preserve code-mixed nuances.

## 👥 Contributors
- **Dhruv Kurliye** - [🔗 Dhruv-Kurliye](https://github.com/Dhruv-Kurliye)
- **Rajesh Singh** - [🔗 sngrajesh](https://github.com/sngrajesh)
- **Hemanshi Ukani** - [🔗 hemanshiukani2908](https://github.com/hemanshiukani2908)
- **Abhinav Seggyam** - [🔗]()

