import google.generativeai as genai


prompt1 = '''1. You are a Business Analyst trying to prepare a Functional Requirement Document.
2. Identify 2-3 key software features from the text and map all their important functionalities to them.
3. Return the result in the form of JSON where the feature name is the key and all functionalities are values, like this:
{
  "FeatureName1": [
    "Functionality1",
    "Functionality2"
  ],
}
4. Don't give any explanations and spaces in naming keys
'''
def extract_features(chunk,API_KEY):
  genai.configure(api_key=API_KEY)
  model = genai.GenerativeModel('gemini-1.5-flash')
  return model.generate_content(prompt1+chunk+'"')

prompt2 = '''
You are a Business Analyst and identified key features along with their functionalities.
Now prepare a Functional Requirement Document (FRD) using the provided data. The document should be concise and include:
Table of Contents with proper indexing:
Use numbers like 3.1, 3.2, and so on for main sections.
For sub-sections within a main section, give a tab sapce and use numbers like 3.2.1, 3.2.2, and so on.
Index the Table of Contents with the actual indexes used for the contents.
Introduction:
Briefly introduce the software and its purpose.
Functional Requirements:
List and describe the key features and their functionalities.
Non-Functional Requirements:
Include and describe non-functional requirements separately.
Format the output in markdown and add <br> at the end of each line except for headings and sub-headings.
'''
def generate_frd(data,API_KEY):
  genai.configure(api_key=API_KEY)
  model = genai.GenerativeModel('gemini-1.5-flash')
  return model.generate_content(prompt2+data+'"')