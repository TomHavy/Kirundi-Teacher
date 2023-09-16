# Kirundi-Teacher: Fine-tuning an LLM on the Kirundi Language

## 📜 Introduction 

Kirundi is a low-referenced Bantu language primarily spoken in Burundi, Tanzania, Uganda, and the Democratic Republic of Congo. Despite its significance, Kirundi has limited online resources available, which presents a considerable challenge for Language Model Models (LLMs), particularly open-source ones, to effectively communicate in Kirundi.

In response to this issue, this project aims to address the scarcity of Kirundi language resources by fine-tuning a Language Model into an expert capable of answering questions about the Kirundi language.

## 📊 Dataset Creation

### The Challenge

The first significant challenge encountered in this project was the unavailability of an appropriate dataset for this specific use case. It was unsurprising that existing datasets did not align with the project's requirements, which necessitated the creation of a new dataset.

### Dataset Creation Protocol

To overcome this challenge, the project creator utilized ChatGPT, a powerful language model, to generate a custom dataset in JSON format with the structure ['question', 'answer']. Several iterations were performed to determine the most effective prompt, which turned out to be: "You are a Kirundi expert. Your goal is to generate a JSONL file of questions and answers about the Kirundi language. Generate 100 unique samples." This protocol was instrumental in generating approximately 2000 unique rows of Kirundi language-related content.

## 🤖 LLM Choice

Due to resource constraints, the project was conducted using Google Colab, which limited the choice of Language Model to those with around 7 billion parameters. At the time of this project, the best open-source model of this size available was Llama 2 (insert leaderboard link), which was selected for fine-tuning.

## 🧹 Data Pre-processing

The next critical step involved processing the initial dataset to create a dataset specifically tailored for Kirundi content. This data pre-processing stage resulted in a structured dataset with entries in the format ['question', 'answer'].

## 🚀 Training

### Training Results

The training phase involved multiple iterations to fine-tune the chosen LLM. The following results were achieved after training the model over 4 epochs with a total of 2500 steps:

![Training loss (Epochs: 4; Steps: 2500)](images/image-1.png)

After 4 epochs and 2500 step, the training loss 
## 💬 Inference

To make the Kirundi language more accessible and promote its use, a user-friendly web interface (UI) was developed using Streamlit. This UI allows users to ask questions about Kirundi and receive informative responses effortlessly.

### 🖥️ Web Interface (UI)

### 📝 How to Use

To interact with Kirundi Teacher, follow these simple steps:

1. Clone this repository.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Launch the Streamlit web app by running `streamlit run app.py`.

Now, you can start asking questions and exploring the Kirundi language with ease.

## 📣 Contribution and Feedback

This project is open to contributions, suggestions for improvements, and reports of any issues. Your input is invaluable in enhancing the capabilities of Kirundi Teacher and making it a more powerful tool for promoting the Kirundi language.

---

