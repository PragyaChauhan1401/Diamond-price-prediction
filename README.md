Diamond Price Prediction with MLOps & DevOps
1. Project Title and Description
Description:
This project builds a complete machine learning pipeline for diamond price prediction. It features an automated, scalable, and containerized workflow with CI/CD integration. Using MLOps best practices, it ensures reproducibility, version control, and seamless deployment with Docker and Jenkins.

2. Tech Stack
Python
Pandas
Scikit-Learn
XGBoost
DVC (Data Version Control)
Jenkins
Docker
Streamlit

3. Key Features
#MLOps Modular Pipeline: Structured into stages — Data Ingestion → Preprocessing → Training → Evaluation → Prediction.

#DVC Integration: Version control for datasets and models, ensuring reproducibility.

#Jenkins CI/CD: Automated testing, building, containerization, and deployment on GitHub push.

#Docker Deployment: Fully containerized app for easy setup and portability.

#Streamlit App: Real-time diamond price prediction with a user-friendly web interface.

4. Architecture Overview / Workflow Diagram
   GitHub Push → Jenkins Build → DVC Pull → Train & Evaluate → Dockerize → Streamlit Deploy

6. Setup Instructions
7. 
Clone the Repository:
bash
Copy
Edit
git clone https://github.com/your-username/diamond-price-prediction-mlops.git
cd diamond-price-prediction-mlops

Set Up Python Environment:
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Run Streamlit App Manually:
bash
Copy
Edit
cd Streamlit-app
streamlit run app.py

Run the Project via Docker:
bash
Copy
Edit
docker build -t diamond-price-prediction .
docker run -p 8501:8501 diamond-price-prediction

6. CI/CD Pipeline Explanation
Jenkins automates testing, building, containerization, and deployment upon every GitHub push.

7. Folder Structure
bash
Copy
Edit
├── data/            # Raw and processed datasets
├── model/           # Trained models and evaluation results
├── src/             # Source code (data ingestion, preprocessing, training, evaluation)
├── Streamlit-app/   # Streamlit application code
├── Dockerfile       # Dockerfile for containerization
├── Jenkinsfile      # Jenkins pipeline configuration
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
8. Deployment
Local Deployment: Use Docker to deploy locally.

Production Deployment: https://diamond-price-prediction-ek10.onrender.com/


10. Contact Information

Maintained by: Pragya Chauhan  
GitHub: [https://github.com/PragyaChauhan1401]


https://github.com/user-attachments/assets/d46182a6-a40d-42e2-bfcc-8709506198f5


