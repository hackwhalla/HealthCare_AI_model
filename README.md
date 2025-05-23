#HealthCare_AI_model

🏥 HealthCare AI Model for Low-Cost Home Treatment
This project aims to empower underserved communities by providing accessible, low-cost, and time-saving healthcare recommendations using machine learning. It suggests Ayurvedic remedies, home treatments, and suitable exercises for common diseases based on user input.

✨ Key Features
Predicts Ayurvedic medicine, home remedies, and simple exercises for 20 common health conditions.

Trained using Decision Tree classifiers to ensure transparency and interpretability.

Utilizes label encoding and scikit-learn for streamlined data preprocessing and model training.

Outputs are mapped back to human-readable treatments to guide non-expert users.

Can be extended or integrated into mobile apps for on-the-go use in rural areas.

🎯 Use Case
This project is designed for NGOs, rural health initiatives, or community clinics where people may lack access to costly or distant healthcare facilities. It helps them:

Save time by avoiding travel to clinics for minor illnesses.

Save money on initial consultations and over-the-counter drugs.

Save energy by offering immediate, home-based care options.

📁 Files Included
Health_care_AI_main_file.py: Core script to preprocess data, train models, and make predictions.

Pretrained models:

Ayurvedic_model1.pkl

Home_Remedies_model2.pkl

exerise_model3.pkl

Dataset: ngo_project.xlsx (not included here for privacy)

🛠️ Requirements
Python 3.x

pandas

numpy

scikit-learn

✅ How It Works
Input a disease name (e.g., “Fever”).

The model encodes it and predicts the best:

Ayurvedic treatment

Home remedy

Physical exercise

Results are displayed in user-friendly language.
