import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

# Set up Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('happimynd-3460553cc66f.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheets document by its title
spreadsheet = client.open_by_key("1YpIAgkk9nkpczG6U9k-f2aafMy0Tn3Fmu-JJ-O278TY")
worksheet = spreadsheet.get_worksheet(1)  # Assuming the data is in the first worksheet

def categorize_stress_level(total_score):
    if total_score <= 4:
        return st.title("आपका चिंता स्तर न्यूनतम है।")
    elif 5 <= total_score <= 9:
        return "आपका चिंता स्तर हल्का है।"
    elif 10 <= total_score <= 14:
        return "आपका चिंता स्तर मध्यम है।"
    else:
        return "आपका चिंता स्तर गंभीर है।"


def submit_survey_data(name, email, mobile_number, company_name, total_score, stress_level):
    data = [name, email, mobile_number, company_name, total_score, stress_level]
    worksheet.append_row(data)
    st.success("Data submitted successfully!")
    
def survey_question_1():
    st.markdown("Q1. पिछले 2 सप्ताहों में, आपने कितनी बार  चिंता या घबराहट महसूस की है?")
    st.markdown("(Over the last 2 weeks, how often have you felt nervous, anxious or on edge?)")
    options = ["बिल्कुल नहीं (Not at all)", "कई दिन (Several days)", "आधे से ज्यादा दिन (More than half the days)", "लगभग हर दिन (Nearly every day)"]
    selected_option = st.radio("", options, index=None, key="question1")

    # Assign scores based on the selected option
    scores = {"बिल्कुल नहीं (Not at all)": 0, "कई दिन (Several days)": 1, "आधे से ज्यादा दिन (More than half the days)": 2, "लगभग हर दिन (Nearly every day)": 3}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_2():
    st.markdown("Q2. पिछले 2 सप्ताहों में, आप कितनी बार चिंता को रोकने या नियंत्रित करने में असमर्थ हुए हैं?")
    st.markdown("(Over the last 2 weeks, how often have you not been able to stop or control worrying?)")
    options = ["बिल्कुल नहीं (Not at all)", "कई दिन (Several days)", "आधे से ज्यादा दिन (More than half the days)", "लगभग हर दिन (Nearly every day)"]
    selected_option = st.radio("", options, index=None, key="question2")

    # Assign scores based on the selected option
    scores = {"बिल्कुल नहीं (Not at all)": 0, "कई दिन (Several days)": 1, "आधे से ज्यादा दिन (More than half the days)": 2, "लगभग हर दिन (Nearly every day)": 3}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_3():
    st.markdown("Q3. पिछले 2 सप्ताहों में, आप कितनी बार अलग-अलग चीज़ों को लेकर बहुत अधिक चिंतित रहे हैं?")
    st.markdown("(Over the last 2 weeks, how often have you worried too much about different things?)")
    options = ["बिल्कुल नहीं (Not at all)", "कई दिन (Several days)", "आधे से ज्यादा दिन (More than half the days)", "लगभग हर दिन (Nearly every day)"]
    selected_option = st.radio("", options, index=None, key="question3")

    # Assign scores based on the selected option
    scores = {"बिल्कुल नहीं (Not at all)": 0, "कई दिन (Several days)": 1, "आधे से ज्यादा दिन (More than half the days)": 2, "लगभग हर दिन (Nearly every day)": 3}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_4():
    st.markdown("Q4. पिछले 2 सप्ताहों में, आपको कितनी बार आराम करने में परेशानी हुई है?")
    st.markdown("(Over the last 2 weeks, how often have you had trouble relaxing?)")
    options = ["बिल्कुल नहीं (Not at all)", "कई दिन (Several days)", "आधे से ज्यादा दिन (More than half the days)", "लगभग हर दिन (Nearly every day)"]
    selected_option = st.radio("", options, index=None, key="question4")

    # Assign scores based on the selected option
    scores = {"बिल्कुल नहीं (Not at all)": 0, "कई दिन (Several days)": 1, "आधे से ज्यादा दिन (More than half the days)": 2, "लगभग हर दिन (Nearly every day)": 3}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_5():
    st.markdown("Q5. पिछले 2 सप्ताहों में, आप कितनी बार इतने बेचैन हुए कि शांत बैठने में परेशानी हुई ?")
    st.markdown("(Over the last 2 weeks, how often have you been so restless that it is hard to sit still?)")
    options = ["बिल्कुल नहीं (Not at all)", "कई दिन (Several days)", "आधे से ज्यादा दिन (More than half the days)", "लगभग हर दिन (Nearly every day)"]
    selected_option = st.radio("", options, index=None, key="question5")

    # Assign scores based on the selected option
    scores = {"बिल्कुल नहीं (Not at all)": 0, "कई दिन (Several days)": 1, "आधे से ज्यादा दिन (More than half the days)": 2, "लगभग हर दिन (Nearly every day)": 3}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_6():
    st.markdown("Q6. पिछले 2 सप्ताहों में, आप कितनी बार आसानी से परेशान या चिड़चिड़े हो गए हैं?")
    st.markdown("(Over the last 2 weeks, how often have you become easily annoyed or irritable?)")
    options = ["बिल्कुल नहीं (Not at all)", "कई दिन (Several days)", "आधे से ज्यादा दिन (More than half the days)", "लगभग हर दिन (Nearly every day)"]
    selected_option = st.radio("", options, index=None, key="question6")

    # Assign scores based on the selected option
    scores = {"बिल्कुल नहीं (Not at all)": 0, "कई दिन (Several days)": 1, "आधे से ज्यादा दिन (More than half the days)": 2, "लगभग हर दिन (Nearly every day)": 3}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score

def survey_question_7():
    st.markdown("Q7. पिछले 2 सप्ताहों में, आपको कितनी बार डर महसूस हुआ कि कुछ भयानक घटित हो सकता है?")
    st.markdown("(Over the last 2 weeks, how often have you felt afraid as if something awful might happen?)")
    options = ["बिल्कुल नहीं (Not at all)", "कई दिन (Several days)", "आधे से ज्यादा दिन (More than half the days)", "लगभग हर दिन (Nearly every day)"]
    selected_option = st.radio("", options, index=None, key="question7")

    # Assign scores based on the selected option
    scores = {"बिल्कुल नहीं (Not at all)": 0, "कई दिन (Several days)": 1, "आधे से ज्यादा दिन (More than half the days)": 2, "लगभग हर दिन (Nearly every day)": 3}
    
    # Handle the case where no option is selected
    score = scores.get(selected_option, None)
    
    return score



def get_user_info():
    name = st.text_input("नाम (Name):")
    email = st.text_input("ईमेल आईडी (Email ID):")
    mobile_number = st.text_input("मोबाइल नंबर (Mobile Number):")
    company_name = st.text_input("कंपनी/इंस्टीट्यूट का नाम (Company/Institute Name):")
    
    # Validate that name, email, mobile_number, and company_name are not empty
    if not name.strip() or not email.strip() or not mobile_number.strip() or not company_name.strip():
        st.warning("कृपया सभी विवरण भरें।")
        return None, None, None, None

    return name, email, mobile_number, company_name    
  
def main():
    st.image("HLS-removebg-preview.png", width = 150)
    st.header("HappiLIFE Screening")
    st.header("चिंता मापनी (Anxiety Test)")
    
    st.subheader("पहला कदम जो आपकी भावनात्मक और मानसिक स्वास्थ्य का  मूल्यांकन करने में आपकी मदद करता है।")
    st.divider()
    
    # First question
    score1 = survey_question_1()
    st.divider()
    
    # Second question
    score2 = survey_question_2()
    st.divider()
    
    # Third question
    score3 = survey_question_3()
    st.divider()
    
    # Fourth question
    score4 = survey_question_4()
    st.divider()
    
    # Fifth question
    score5 = survey_question_5()
    st.divider()
    
    # Sixth question
    score6 = survey_question_6()
    st.divider()
    
    # Seventh question
    score7 = survey_question_7()
    st.divider()
    
    # Collect user information
    name, email, mobile_number, company_name = get_user_info()
    
    # Handle the case where no option is selected for any question
    if any(score is None for score in [score1, score2, score3, score4, score5, score6, score7, name, email, mobile_number, company_name]):
        st.warning("Please select an option for all questions")
        return

    # Calculate total score
    total_score = score1 + score2 + score3 + score4 + score5 + score6 + score7
    
    # Display total score
    st.subheader(f"आपका तनाव स्कोर 21 में से {total_score} है")

    # Categorize stress level and display result
    stress_level = categorize_stress_level(total_score)
    st.subheader(f"{stress_level}")

# Submit data to Google Sheets
    if st.button("Submit"):
        submit_survey_data(name, email, mobile_number, company_name, total_score, stress_level)
 
if __name__ == "__main__":
    main()
