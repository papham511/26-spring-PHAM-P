import pandas as pd
from difflib import SequenceMatcher

# Load Datasets & remove duplicates
try:
	real_df = pd.read_csv('users_cleaned_dataset.csv')
	fake_df = pd.read_csv('fusers_cleaned_dataset.csv')
	db = pd.concat([real_df, fake_df], ignore_index=True).drop_duplicates(subset=['username'])
except FileNotFoundError:			# File missing during testing
	db = pd.DataFrame(columns=['username','name', 'bio', 'fake', 'followers_following_ratio'])


def get_similarity(a, b):
	"""Calculates resemblance percentage between two strings."""
	if not a or pd.isna(a) or not b or pd.isna(b): 
		return 0
	return round(SequenceMatcher(None, str(a).lower(), str(b).lower()).ratio() * 100, 2)

def run_analysis(input_name, input_user, input_bio):
	# Calculate field similarity 
	db['u_sim'] = db['username'].apply(lambda x: get_similarity(input_user, x))
	db['n_sim'] = db['name'].apply(lambda x: get_similarity(input_name, x))
	
	#Check bio provided
	hbio = bool(input_bio and str(input_bio).strip())

	if hbio:
		db['b_sim'] = db['bio'].apply(lambda x: get_similarity(input_bio, x))
		matches = db[(db['u_sim'] >= 80) | (db['n_sim'] >= 80) | (db['b_sim'] >= 80)].copy()			# Filter: At least on field must be >= 80%
		matches['overall'] = (matches['u_sim'] + matches['n_sim'] + matches['b_sim']) / 3
	else:
		# If no bio provided
		db['b_sim'] = None
		matches = db[(db['u_sim'] >= 80) | (db['n_sim'] >= 80)].copy()
		matches['overall'] = (matches['u_sim'] + matches['n_sim']) / 2

	
	if matches.empty:
		return None

	# Calculate Overall Score (Average of the three fields)
	
	matches['overall'] = matches['overall'].round(2)

	# Sort and take top 5
	top_matches = matches.sort_values(by='overall', ascending=False).head(5)

	results_list = []
	for _, row in top_matches.iterrows():
		#FF ratio analysis (Suspisious if ratio is 1 or lower - more followering than followers)
		ratio = row.get('followers_following_ratio', 0)
		ratio_status = "High Suspicious Impersionation Account" if ratio <= 1 else "Average"

		# Identity status from dataset
		identity_status = "Impersonation Account" if row['fake'] == 1 else "Real Account"

		results_list.append({
		 	"username": row['username'],
		 	"name": row['name'],
		 	"u_sim": row['u_sim'],
		 	"n_sim": row['n_sim'],
		 	"b_sim": row['b_sim'],
		 	"overall": row['overall'],
		 	"ratio_text": ratio_status,
		 	"status": identity_status
		})

	return results_list