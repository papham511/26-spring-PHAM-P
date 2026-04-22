# Data Science Capstone Project
## Instagram Impersonation Accounts Detection
### Descriptions
With Instagram's massive user base comes a growing threat. This project tackles the challenge of distinguishing impersonated accounts from real ones by leveraging a targeted set of behavioral and account features, like username, name, bio, post count, followers count, and following counts, alongside derived indicators such as bio length, digit ratio in usernames, and followers to following ratio. Unlike conventional supervised classification, this project employs a similarity analysis framework to identify clusters of accounts that closely mirror a target accounts, a pattern of impersonation behavior. Overall, the central aim is to pinpoint which features most effectively expose these impersonated patterns, delivering a precise, data-driven approach to combating identity fraud on Instagram.

#### Core Components
* Data
	- Combines CSV files containing real and impersonated account data sourced from GitHub.
	- Web Scraping: Utilized BeautifulSoup to gather real-time data from top Instagram influencer accounts for baseline comparison. 
* Analysis & Models (Jupyter & Python) 
	- Visualizations: Plots analyzing follower to following ratios, post frequency, and class balance (Real vs. Fake). Identified and removed redundant features.
	- Model Evaluation: Performacne tesing using Logistic Regession, Support Vector Classifier, and Regression models.
	- Feature Importance: Identified which metadata attributes (e.g., account age, ratio) most significnatly impact detection accuracy.

* Web-Based Detection Tool (Flask)
	- Interactive Dashboard: A UI that flags accounts with a similarity score of 80% or higher. 
	- Similarity Index: An algorithm calculating overlaps in usernames, display names, biographies, and follower ratios.
	- Risk Reporting: Visualizes the top 5 high-risk pairs with specific breakdowns and a final real or impersonated label.
	- User Validation: Includes interactive surveys to incorporate human feedback, refining the tool's accuracy and reliability.


### Organized Files
```text
26-spring-PHAM-P
├── data
│	├── Visualize_Plot.ipynb
│	├──	clean_dataset.ipynb
│	├──	fusers(1).csv
│	├──	fusers(2).csv
│	├──	fusers.csv
│	├──	fusers_cleaned_dataset.csv
│	├──	insta_influencers.csv
│	├──	insta_scrape.ipynb
│	├──	pre-model.ipynb
│	├──	user(2).csv
│	├──	users(1).csv
│	├──	users.csv
│	└──	users_cleaned_dataset.csv
│
├── demo
│	├──	__pycache__
│	│	└──	 calc.cpython-313.pyc
│	│
│	├──	styles
│	│	├──	 estyle.css
│	│	├──	 insta-background.jpg
│	│	├──	 insta-ebackground.jpg
│	│	├──	 rstyle.css
│	│	└──	 style.css
│	│
│	├──	templates
│	│	├──	error.html
│	│	├──	form.html
│	│	└──	result.html
│	│
│	├──	Readme.md
│	├──	app.py
│	└──	calc.py
│
├── poster
│	└──	Readme.md
│
├── presentation
│	├──	EDA.pdf
│	└──	Readme.md
│
├── proposal
│	├──	Capstone Proposal Template.docx
│	└──	Proposal.pdf
│
├── report
└── README.MD

```

### Project Process Workflow
1. Data Integration & Cleaning
	- Collection: Scrape dat from websites and convert to CSV.
	- Consolidation: Merge diverse datasets into two unified groups, impersonated and real accounts.
	- Standardization: Use unique ID to separate account from each other and use NA or NaN to handle missing values and remove duplicates.
2. Visualize Plot & Model
	- EDA: Create plots to compare behaviors between fake and real acccoutns and identify redundant features.
	- Model Selection: Train and test various classificiaotn models on the combined dataset. 
	- Evaluation: Select the model with the highest accuracy. Generate a confusion matrix heatmap and calculate feature importance scores.

3. Analysis
	- Evaluate the high-performing model to determine which features most significnatly impact the accuracy and the project goals.

4. Results
	- Finalize the top features to be used as the primary inputs for the web application.
5. Create web
	1) Start making the template. The form.html for survey template, result.html for answer for data similarity between input user informations and the data. Lastly error.html for any account that is not in the data update in the web.
	2) Create calc.py to calculate the similarity percentage of username, name, bio, and overall score while it identified if it impersonated or not. Also, using machines learning to match top 5 account similarity of the data with the user input. Create app.py which is the route for the template transfer to another template and including the machine learning calculation.

6. Launch & Test the web
	1) Launch: Open the project directory in the terminal and run the Python Script. 
	2) Access: Open the provided local link in an incognito browser window.
	3) Input: Enter the target account's name, username, and bio.
	4) Provessing: app.py calculates similairty percentages for the name, username, and an overall score.
	5) Output: Result displays a list of accounts and their similarity scores (Real vs. Impersonated). Error Page displays if no matching data is found.
	6) Navigation: Use the "Back" Button to return to the input form.
7. Report
	- Conclude the project, and summarize key takeaways.
	- Identify reasearch gaps, lessons learned, and ares for future improvement.