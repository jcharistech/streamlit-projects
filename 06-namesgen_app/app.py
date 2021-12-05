# Core Pkgs
import streamlit as st 
import names
from ultimate_wordlist import animals_list,adjectives_list,adverbs_list,positive_wordlist,negative_wordlist
import random 
import string

# Fxn
def generate_random(mylist:list,number_of_words:int=7)->list:
	results = [random.choice(mylist) for i in range(number_of_words)]
	return results

def custom_filter(mylist,start_char):
	results = [i for i in mylist if i.startswith(start_char)]
	# results = list(filter(lambda x: x.startswith(start_char),mylist))# method 2
	return results


def randomize(category,number_of_words):
	return {
	'First Names':lambda: [names.get_first_name() for i in range(number_of_words)],
	'Last Names':lambda: [names.get_last_name() for i in range(number_of_words)],
	'Positive Words':lambda: generate_random(positive_wordlist,number_of_words),
	'Negative Words':lambda: generate_random(negative_wordlist,number_of_words),
	'Adverb':lambda: generate_random(adverbs_list,number_of_words),
	'Adjectives':lambda: generate_random(adjective_list,number_of_words),
	'PetNames':lambda: generate_random(animals_list,number_of_words),
	}.get(category,lambda:'None Found')()



def main():
	st.title("Names Generator App")
	st.subheader("Streamlit Project")
	menu = ["Home","NamesList","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("HomePage")
		number_of_names = st.number_input("Number of Names",value=7)
		gender = st.radio('Gender',('Both','Male','Female'))
		if st.button("Generate"):
			if gender == "Both":
				results = [names.get_full_name() for i in range(number_of_names)]
			else:
				results = [names.get_full_name(gender=gender) for i in range(number_of_names)]
		
			st.write(results)
			# Copy
			st.code(results)
			# Download
			st.download_button('Download',str(results))	


	elif choice == "NamesList":
		st.subheader("NamesList Page")

		# Layout
		col1,col2 = st.columns(2)
		with col1:
			st.info("Random List")
			number_of_words = st.number_input("Number of Words",min_value=1,max_value=100,value=7)
			category = st.selectbox("Category",["First Names","Last Names","Animals","Positive Words","Negative Words","Adverbs","Adjectives"])
			if st.button("Generate"):
				# # Method 1
				# if category == "First Names":
				# 	results = [names.get_first_name() for i in range(number_of_words)]
				# elif category == "Last Names":
				# 	results = [names.get_last_name() for i in range(number_of_words)]
				# elif category == "Animals":
				# 	results = generate_random(animals_list,number_of_words)
				# elif category == "Positive Words":
				# 	results = generate_random(positive_wordlist,number_of_words)
				# elif category == "Negative Words":
				# 	results = generate_random(negative_wordlist,number_of_words)
				# elif category == "Adverbs":
				# 	results = generate_random(adverbs_list,number_of_words)
				# elif category == "Adjectives":
				# 	results = generate_random(adjectives_list,number_of_words)
				# Method 2
				results = randomize(category,number_of_words)

				st.write(results)	

				# Copy
				st.code(results)
				# Download
				st.download_button('Download',str(results))		



		with col2:
			st.success("PetNames List")
			# alphabet_list = list(string.ascii_uppercase)
			# st.code(alphabet_list)
			alphabet_list_with_any = ['Any','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
			number_of_words = st.number_input("Number of Words",min_value=1,max_value=100,value=7,key='2')
			alphabeth_type =st.selectbox("Startwith Character",alphabet_list_with_any)
			if st.button("Generate Petnames"):
				if alphabeth_type == "Any":
					results = [(random.choice(positive_wordlist)+ ' ' + random.choice(animals_list)) for i in range(number_of_words)]
				else:
					custom_positive_wordlist = custom_filter(positive_wordlist,str(alphabeth_type).lower())
					custom_animals_wordlist = custom_filter(animals_list,str(alphabeth_type).lower())
					results = [(random.choice(custom_positive_wordlist)+ ' ' + random.choice(custom_animals_wordlist)) for i in range(number_of_words)]
				st.write(results)

				# Copy
				st.code(results)
				# Download
				st.download_button('Download',str(results))	


	else:
		st.subheader("About")




if __name__ == '__main__':
	main()