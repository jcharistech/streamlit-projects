import streamlit as st  
import string
import random


## characters to generate password from
all_characters_pattern = list(string.ascii_letters + string.digits + "!@#$%^&*()")
alphanumeric_pattern = list(string.ascii_letters + string.digits)
common_passwd_pattern = ["password","computer","1234"]

def generate_random_password(characters,password_length=6):
	# shuffling the characters
	random.shuffle(characters)
	# picking random characters from the list
	password = []
	for i in range(password_length):
		password.append(random.choice(characters))
	# shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	return ("".join(password))

def generate_random_password2(characters: list,password_length=6) -> str:
	random.shuffle(characters)
	password = [random.choice(characters) for i in range(password_length)]
	result = "".join(password)
	return result

natophonetics = {"A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-Ray","Y":"Yankee","Z":"Zulu"}
leet_dict = {'a': '4','b': 'l3', 'c': '(', 'd': '[)', 'e': '3', 'l': '1', 's': '5', 't': '+', 'w': '\\/\\/', 'o': '0'}


def get_value(val,my_dict):
		for key ,value in my_dict.items():
			if val == key:
				return value

def get_natophonetics(term):
	result = ' '.join([natophonetics.get(i, i) for i in list(term.upper())])
	return result

def leet_converter(term):
	result = ' '.join([leet_dict.get(i, i) for i in list(term.lower())])
	return result



def main():
	st.title("Ultimate Password Generator App")
	

	menu = ["Home","Advanced","LeetConverter","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		passwd_pattern_list = ['alphanumeric','all','words']
		password_length = st.number_input("Password Length",min_value=5,max_value=25,value=8)
		password_pattern_choice = st.multiselect("Pattern",passwd_pattern_list,default='all')
		
		if st.button("Generate"):
			st.info("Generated Results")
			if 'alphanumeric' in password_pattern_choice:
				passwd_result = generate_random_password2(alphanumeric_pattern,password_length)
				# st.write(passwd_result)
				st.code(passwd_result)
				st.info("Nato Phonetics")
				st.write("Remember:: {}".format(get_natophonetics(passwd_result)))

			elif 'alphanumeric' and 'words' in password_pattern_choice:
				first_result = generate_random_password2(alphanumeric_pattern,password_length)
				# st.write(first_result)
				passwd_result = str(first_result) + random.choice(common_passwd_pattern)
				# st.write(passwd_result)
				st.code(passwd_result)
				st.info("NatoPhonetics")
				st.write("Remember:: {}".format(get_natophonetics(passwd_result)))

			else:
				passwd_result = generate_random_password2(all_characters_pattern,password_length)
				st.code(passwd_result)
				st.info("Nato Phonetics")
				st.write("Remember:: {}".format(get_natophonetics(passwd_result)))

	elif choice == "Advanced":
		st.subheader("Advanced")
		passwd_pattern_list = ['alphanumeric','all']
		password_length = st.number_input("Password Length",min_value=5,max_value=25,value=8)
		custom_word = st.text_input("Add Your Custom Word")
		password_pattern_choice = st.multiselect("Pattern",passwd_pattern_list,default='all')
		
		if st.button("Generate"):
			st.info("Generated Results")
			first_result = generate_random_password2(all_characters_pattern,password_length)
			# st.write(first_result)
			passwd_result = random.choice([custom_word]) + str(first_result) 
			# st.write(passwd_result)
			st.code(passwd_result)
			st.info("NatoPhonetics")
			st.write("Remember:: {}".format(get_natophonetics(passwd_result)))


	elif choice == "LeetConverter":
		st.subheader("LeetConverter")
		col1,col2 = st.columns(2)

		with col1:
			term = st.text_area("Your Text")
			if st.button("Convert"):
				st.success("Results")
				st.write(leet_converter(term))


	else:
		st.subheader("About")


if __name__ == '__main__':
	main()


