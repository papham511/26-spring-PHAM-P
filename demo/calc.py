import pandas as pd
from difflib import SequenceMatcher

# read db
real_df = pd.read_csv('users_cleaned_dataset.csv')
fake_df = pd.read_csv('fusers_cleaned_dataset.csv')
database = pd.concat([real_df, fake_df], ignore_index=True)

def get_similarity(a, b):
	"""Calculates resemblance percentage between two strings."""
	if not a or not b: return 0
	return SequenceMatcher(None, str(a).lower(), str(b).lower()).ratio() * 100

def run_analysis(input_name, input_user, input_bio):
	# Calculate similarity for username
	database['u_sim'] = database['username'].apply(lambda x: get_similarity(input_user, x))

	# Find the best match
	best_match_idx = database['u_sim'].idxmax()
	best_match = database.iloc[best_match_idx]

	if database.loc[best_match_idx, 'u_sim'] < 30:
		return None

	# Feature Engineering: Compare specfic attributes
	name_sim = get_similarity(input_name, best_match.get('name', ''))
	bio_sim = get_similarity(input_bio, best_match.get('description', ''))

	# Follwers-to-following ratio analysis
	followers = max(1, best_match.get('followers', 1))
	following = best_match.get('following', 0)
	ratio = following / followers
	# Flag high ratios as suspivious per your proposal
	ratio_status = "High (Suspicious)" if ratio > 2.0 else "Normal"
	# Overall Calculation using weighted feature analysis
	overall = (best_match['u_sim'] * 0.4) + (name_sim * 0.3) + (bio_sim * 0.3)
	status = "fake Account" if overall > 50 else "Real Account"

	return {
		"username": best_match['username'],
		"u_sim": round(best_match['u_sim'], 2),
		"n_siim": round(name_sim, 2),
		"b_sim": round(bio_sim, 2),
		"ratio_text": ratio_status, 
		"overall": round(overall, 2), 
		"status": status
	}