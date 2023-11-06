import streamlit as st
import openai
import webbrowser

# Set your OpenAI API key 
api_key =st.secrets["OPENAI_API_KEY"]

openai.api_key = api_key

# Define educational resources
educational_resources = {
    "Algebra": "https://www.khanacademy.org/math/algebra",
    "Calculus": "https://www.khanacademy.org/math/calculus-1",
    "Geometry": "https://www.khanacademy.org/math/geometry",
    "Trigonometry": "https://www.khanacademy.org/math/trigonometry",
    "Statistics": "https://www.khanacademy.org/math/statistics-probability",
    "Linear Algebra": "https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/"
}

# Define the ask_math_question function
def ask_math_question(question):
    conversation = [
        {"role": "system", "content": "You are a math tutor."},
        {"role": "user", "content": question}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    reply = response['choices'][0]['message']['content']
    return reply

def main():
    st.title("MathGPT - Math Assistant")

    # Define a user profile with user-specific settings (language, units, etc.)
    user_profile = {
        "language": "English",
        "preferred_units": "imperial",
        # Add more user-specific settings here
    }

    # Sidebar for User Profile Customization
    with st.sidebar:
        st.header("Raghul Rajkumar.R")
        linkedin_url="https://www.linkedin.com/in/rraghulrajkumar/"
        github_url="https://github.com/RRaghulRajkumar"
        st.image("https://proinfluent.b-cdn.net/wp-content/uploads/2019/05/Logo-LinkedIn-officiel.png",width=100)
        if st.button("LinkedIn"):
            # Open the LinkedIn URL in a web browser
            webbrowser.open_new_tab(linkedin_url)
        
   
        st.image("https://imgs.search.brave.com/_kHkOj0rQGazc6sqY0ZeglYK_a8fA6vv2plHMAelW3Y/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9hc3Nl/dHMuc3RpY2twbmcu/Y29tL2ltYWdlcy81/ODQ3Zjk4ZmNlZjEw/MTRjMGI1ZTQ4YzAu/cG5n",width=70)
        if st.button("Github"):
             # Open the LinkedIn URL in a web browser
            webbrowser.open_new_tab(github_url)
       

    user_profile["language"] = st.selectbox("Language", ["English", "Spanish", "French"])
    user_profile["preferred_units"] = st.selectbox("Preferred Units", ["Imperial", "Metric"])

    # User Input for Math Questions
    st.subheader("Ask a math question:")
    
    # Increase the height of the input field by setting the height parameter
    question = st.text_area("", height=200, key="math_question")
        # Educational Resources Section
    st.header("Educational Resources")
    topic = st.selectbox("Select a topic:", list(educational_resources.keys()))
    if st.button("Explore"):
        if topic in educational_resources:
            st.write(f"Here are some educational resources for {topic}:")
            st.write(f"[{topic} on Khan Academy]({educational_resources[topic]})")
        else:
            st.error("Topic not found. Please select a valid topic.")


    if st.button("Submit"):
        # Send the user question to MathGPT and get the answer
        answer = ask_math_question(question)

        # Display the answer
        st.write(f"**Answer:** {answer}")

if __name__ == "__main__":
    main()
