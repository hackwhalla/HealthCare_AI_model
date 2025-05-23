import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

df = pd.read_excel("ngo_project.xlsx")

le_desease = LabelEncoder()
le_ay = LabelEncoder()
le_hr = LabelEncoder()
le_ex = LabelEncoder()

df['en_desease'] = le_desease.fit_transform(df['Disease Name'])
df['en_Ayurvedic'] = le_ay.fit_transform(df['Ayurvedic'])
df['en_Home_Remedies'] = le_hr.fit_transform(df['Home Remedies'])
df['en_exerise'] = le_ex.fit_transform(df['Exercise'])

de1 = DecisionTreeClassifier()
de1 = de1.fit(df[['en_desease']],df[['en_Ayurvedic']])

de2 = DecisionTreeClassifier()
de2 = de2.fit(df[['en_desease']],df[['en_Home_Remedies']])

de3 = DecisionTreeClassifier()
de3 = de3.fit(df[['en_desease']],df[['en_exerise']])

def disease_to_number(disease_name):
  # Create a dictionary mapping disease names to their numerical representations
  disease_mapping = {
    "Acne": 0,
    "Allergies": 1,
    "Common Cold": 2,
    "Constipation": 3,
    "Cough": 4,
    "Dizzy": 5,
    "Fever": 6,
    "Headache": 7,
    "Heartburn / Acid Reflux": 8,
    "Indigestion": 9,
    "Itching": 10,
    "Joints pain": 11,
    "Mild Anxiety": 12,
    "Mild Fever": 13,
    "Minor Burn": 14,
    "Mouth ulser": 15,
    "Muscle Pain": 16,
    "Nausea": 17,
    "Sore Throat": 18,
    "Sweeling": 19
  }
  # Check if the disease name is in the mapping
  if disease_name in disease_mapping:
    return disease_mapping[disease_name]
  else:
    return -1  # Return -1 if the disease is not found

def number_to_ayurvedic(ayurvedic_number):

  # Create a dictionary mapping numerical representations to Ayurvedic medicine names
  ayurvedic_mapping = {
      0: "Ajwain Water",
      1: "Aloe vera gel, Jatyadi tailam",
      2: "Avipattikar churna, Amla juice",
      3: "Brahmi Tea",
      4: "Brahmi, Ashwagandha, Shankhpushpi syrup",
      5: "Dashmoolarishta, Nirgundi oil",
      6: "Eucalyptus Oil",
      7: "Giloy Juice",
      8: "Giloy, Tulsi Kadha",
      9: "Ginger powder, Amla juice",
      10: "Khadiradi Vati, Yashtimadhu churna",
      11: "Mulethi (Licorice)",
      12: "Neem Paste",
      13: "Neem oil, Khadirarishta",
      14: "Peppermint Oil",
      15: "Shallaki (Boswellia), Ashwagandha",
      16: "Sitopaladi churna, Yashtimadhu (Mulethi)",
      17: "Triphala Churna",
      18: "Tulsi-Ginger Tea",
      19: "Turmeric + Honey"
  }

  # Check if the Ayurvedic medicine number is in the mapping
  if ayurvedic_number in ayurvedic_mapping:
    return ayurvedic_mapping[ayurvedic_number]
  else:
    return None  # Return None if the number is not found in the mapping

def number_to_home_remedy(remedy_number):
  """Maps numerical representations to Home Remedies."""
  remedy_mapping = {
      0: "Aloe Vera gel",
      1: "Cold compress, Hydration",
      2: "Cold compress, Stay hydrated",
      3: "Cold milk, Fennel seeds, Jeera water, Avoid spicy food",
      4: "Cold water rinse, Honey application, Aloe vera gel",
      5: "Elevate affected area, Cold packs, Epsom salt bath",
      6: "Ginger tea, Fennel seeds",
      7: "Ginger tea, Lemon water, Clove, Stay hydrated",
      8: "Ginger-honey mix, Steam inhalation, Warm fluids",
      9: "Honey on ulcer, Coconut oil swish, Tulsi leaves paste",
      10: "Hot/cold compress",
      11: "Hot/cold compress, Turmeric milk, Epsom salt bath",
      12: "Lemon water, Stay hydrated, Lie down flat, Deep breathing",
      13: "Meditation, Deep breathing",
      14: "Nasal saline rinse",
      15: "Oatmeal bath, Aloe vera gel, Cold compress, Avoid scratching",
      16: "Rest, Hydration",
      17: "Steam inhalation, Honey-lemon",
      18: "Turmeric milk",
      19: "Warm water + Lemon"
  }
  # Check if the remedy number is in the mapping
  if remedy_number in remedy_mapping:
    return remedy_mapping[remedy_number]
  else:
    return None  # Return None if the number is not found in the mapping

def number_to_exercise(exercise_number):
  """Maps numerical representations to Exercise."""
  exercise_mapping = {
      0: "Abdominal massage",
      1: "Avoid movement in affected area",
      2: "Avoid spicy food, Gentle jaw movement",
      3: "Balance exercises, Light walking, Avoid sudden movements",
      4: "Breathing exercises",
      5: "Breathing exercises (Pranayama), Rest",
      6: "Deep breathing, Avoid sudden movements",
      7: "Gentle movement, Avoid overuse of affected area",
      8: "Gentle neck rolls",
      9: "Light stretching, Avoid sweating too much",
      10: "Light stretching, Swimming, Yoga",
      11: "Light walking",
      12: "Light walking after meals, Yoga (e.g., Vajrasana)",
      13: "Neck stretches",
      14: "Rest",
      15: "Rest only",
      16: "Stretching",
      17: "Walking",
      18: "Yoga",
      19: "Yoga (stress relief)"
  }
  # Check if the exercise number is in the mapping
  if exercise_number in exercise_mapping:
    return exercise_mapping[exercise_number]
  else:
    return None  # Return None if the number is not found in the mapping

def user_desease_to_medicin_number(user_desease):
  user_desease = np.array([user_desease])
  user_desease = user_desease.reshape(1, -1)
  pred_ay = de1.predict(user_desease)
  pred_hr = de2.predict(user_desease)
  pred_ex = de3.predict(user_desease)
  return pred_ay,pred_hr,pred_ex

def user_medicine_number_to_medicine(result):
    ayurvedic_number = result[0].item() # Example Ayurvedic medicine number & # Extract the integer value from the NumPy array
    remedy_number = result[1].item()  # Extract integer value
    exercise_number = result[2].item()  # Extract integer value


    ayurvedic_medicine = number_to_ayurvedic(ayurvedic_number)
    home_remedy = number_to_home_remedy(remedy_number)
    exercise_name = number_to_exercise(exercise_number)
    return ayurvedic_medicine,home_remedy,exercise_name


with open('Ayurvedic_model1.pkl', 'wb') as file:
    pickle.dump(de1, file)

with open('Home_Remedies_model2.pkl', 'wb') as file:
    pickle.dump(de2, file)

with open('exerise_model3.pkl', 'wb') as file:
    pickle.dump(de3, file)

"""disease_name =  input("Enter desease name = ") # Example disease name
user_disease_number = disease_to_number(disease_name)

if user_disease_number != -1:
  print(f"The numerical representation of '{disease_name}' is: {user_disease_number}")
  result = user_desease_to_medicin_number(user_disease_number)
  ayurvedic_medicine,home_remedy,exercise_name = user_medicine_number_to_medicine(result)
else:
  print(f"Disease '{disease_name}' not found in the mapping.")


print(f"Ayurvedic Medicine: {ayurvedic_medicine}")
print(f"Home Remedy: {home_remedy}")
print(f"Exercise: {exercise_name}")"""