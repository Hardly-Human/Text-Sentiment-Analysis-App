import streamlit as st



def main():
  
	st.title("Sentiment Analysis App")
	st.text("Built with Python and Streamlit")
	st.markdown("### [![Open Source Love svg1](https://aleen42.github.io/badges/src/github.svg)](https://github.com/Hardly-Human/Image-Captioning-App)\
	`            `[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://lbesson.mit-license.org/)")

	input_text = st.text_area("Enter Your text here", height = 50)

	if input_text is None:
		st.warning("Enter text and Predict Sentiment")

	if st.button("Generate Caption"):
		if input_text is not None:
			r = requests.post(
                "https://api.deepai.org/api/sentiment-analysis",
                data = {
                            'text': input_text,
                        },
                headers = {'api-key': 'aa48ee59-f392-4783-b1ac-ab410534ca61'}
            )
			output = r.json()['output']
			if output[0] == 'Positive' and len(output)== 1:
				st.success('Output : {}'.format(output))
			elif output[0] == 'Negative' and len(output)== 1:
				st.error('Output : {}'.format(output))
			else:
				st.info('Output : {}'.format(output))



if __name__== "__main__":
	main()