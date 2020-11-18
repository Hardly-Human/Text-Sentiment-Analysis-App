import streamlit as st



def main():
  
	st.title("Sentiment Analysis App")
	st.text("Built with Python and Streamlit")
	st.markdown("### [![Open Source Love svg1](https://aleen42.github.io/badges/src/github.svg)](https://github.com/Hardly-Human/Image-Captioning-App)\
	`            `[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://lbesson.mit-license.org/)")

	input_text = st.text_area("Enter Your text here", height = 50)

	if input_text is None:
		st.warning("Enter text and Predict Sentiment")



if __name__== "__main__":
	main()