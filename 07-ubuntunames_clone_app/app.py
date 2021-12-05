
import streamlit as st 
import string 
import random 
from ultimate_wordlist import animals_list,adjectives_list,negative_wordlist,positive_wordlist

# Fxn
def custom_filter(mylist,start_char):
	results = [i for i in mylist if i.startswith(start_char)]
	return results


# # Fxn with typing
# def custom_filter(mylist: list,start_char:str) -> list:
# 	results = [i for i in mylist if i.startswith(start_char)]
# 	return results





def main():
	st.title("Ambivalent & Ubuntu Names Generator App")
	st.subheader("Streamlit Projects")

	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		# layout
		col1,col2 = st.columns(2)

		with col1:
			st.info("Ubuntu Names Generator")
			alphabeth_type = st.selectbox("Startwith",list(string.ascii_uppercase))
			if st.button("Generate Ubuntu Name"):
				custom_animals_list = custom_filter(animals_list,alphabeth_type.lower())
				custom_adjectives_list = custom_filter(adjectives_list,alphabeth_type.lower())
				results =  random.choice(custom_adjectives_list) + ' ' + random.choice(custom_animals_list)
				st.write(results)

				# Copy
				st.code(results)

		with col2:
			st.success("Ambivalent Words Generator")
			alphabet_list_with_any = ['Any','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
			alphabeth_type = st.selectbox("Startwith Alphabet",alphabet_list_with_any)
			
			if st.button("Ambivalentize"):
				if alphabeth_type == "Any":
					results =  random.choice(positive_wordlist) + ' ' + random.choice(negative_wordlist)
				else:
					custom_positive_wordlist = custom_filter(positive_wordlist,alphabeth_type.lower())
					custom_negative_wordlist = custom_filter(negative_wordlist,alphabeth_type.lower())
					results =  random.choice(custom_positive_wordlist) + ' ' + random.choice(custom_negative_wordlist)
				
				st.write(results)

				# Copy
				st.code(results)



	else:
		st.subheader("About")


if __name__ == '__main__':
	main()


