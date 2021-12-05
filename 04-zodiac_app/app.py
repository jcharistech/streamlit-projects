
import streamlit as st 
import pandas as pd 
month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]


# Get the Zodia using the month and the day
def find_zodiac(month,day):
	if month == 'december':
		astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
	elif month == 'january':
		astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
	elif month == 'february':
		astro_sign = 'Aquarius' if (day < 19) else 'pisces'
	elif month == 'march':
		astro_sign = 'Pisces' if (day < 21) else 'aries'
	elif month == 'april':
		astro_sign = 'Aries' if (day < 20) else 'taurus'
	elif month == 'may':
		astro_sign = 'Taurus' if (day < 21) else 'gemini'
	elif month == 'june':
		astro_sign = 'Gemini' if (day < 21) else 'cancer'
	elif month == 'july':
		astro_sign = 'Cancer' if (day < 23) else 'leo'
	elif month == 'august':
		astro_sign = 'Leo' if (day < 23) else 'virgo'
	elif month == 'september':
		astro_sign = 'Virgo' if (day < 23) else 'libra'
	elif month == 'october':
		astro_sign = 'Libra' if (day < 23) else 'scorpio'
	elif month == 'november':
		astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
	return astro_sign


@st.cache
def load_data(data):
	return pd.read_csv(data)

def main():
	st.title("Zodiac App")
	st.subheader("Streamlit Projects")

	menu = ["Home","ZodiacBoard","About"]
	choice = st.sidebar.selectbox("Menu",menu)
	df = load_data('data/zodiac_data.csv')

	if choice == "Home":
		st.subheader("Home")
		dob = st.date_input("Date of Birth")
		month_of_birth = st.selectbox("Month",month_list)
		day_of_birth =  st.number_input("Date",min_value=1,max_value=31)
		if st.button("Predict"):
			# st.write(dob)
			results = find_zodiac(month_of_birth.lower(),day_of_birth)
			st.success("Results")
			st.write("You are ::{}".format(results))

			zdf = df[df['horoscope'] == results.title()]
			# st.dataframe(zdf)
			st.write('Alias:: {}'.format(zdf.iloc[0].aliasname))

			rcol1,rcol2,rcol3 = st.columns([2,1,1])

			with rcol1:
				st.info("Description")
				st.write(zdf.iloc[0].description)

			with rcol2:
				with st.expander("Positives "):
					st.write(zdf.iloc[0].positives.split(','))

			with rcol3:
				with st.expander("Negatives "):
					st.write(zdf.iloc[0].negatives.split(','))





	elif choice == "ZodiacBoard":
		st.subheader("ZodiacBoard")
		st.dataframe(df)


	else:
		st.subheader("About")


if __name__ == '__main__':
	main()


