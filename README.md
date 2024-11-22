Here is the updated `README.md` file with descriptions in English:

---

# OADF: OpenAI Developer Forum Analysis

This repository contains datasets and scripts for analyzing the OpenAI Developer Forum, aiming to help researchers explore community interaction patterns and trends.

---

## File Structure and Descriptions

### Figures Folder (`Figures/`)

This folder contains all the figures used in the associated research paper, including charts, diagrams, and visualizations.

### GitHub Dataset Folder (`Github_Dataset/`)

- **`github_users.csv`**: Contains a dataset of 722,389 GitHub user profiles crawled as of June 2024.

### OpenAI Dataset Folder (`OpenAI_Dataset/`)

- **`openai_posts.csv`**: Contains data from the OpenAI Developer Forum, including post titles, links, timestamps, and other metadata.

### Scripts Folder (`Scripts/`)

- **`fetch_forum_posts.py`**: Script for crawling basic information about forum posts from the OpenAI Developer Forum.
- **`fetch_user_profiles.py`**: Script for crawling user profile data and activity information.
- **`analyze_popularity.py`**: Script for analyzing the popularity of forum posts.
- **`analyze_difficulty.py`**: Script for assessing the difficulty level of forum posts.

---

## Quick Start

1. **Prepare the Environment**

   Ensure Python 3.8+ is installed along with the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run Crawling Scripts**

   Navigate to the `Scripts/` folder and run the following scripts to collect data:

   ```bash
   python fetch_forum_posts.py
   python fetch_user_profiles.py
   ```

3. **Analyze Data**

   Execute the analysis scripts as needed, for example:

   ```bash
   python analyze_popularity.py
   python analyze_difficulty.py
   ```

---

## Project Goals

- **Popularity Analysis**: Explore trends in the popularity of forum posts over time.
- **Difficulty Analysis**: Assess the difficulty levels of forum post content.

Contributions and feedback are welcome!

---

This README has been updated to reflect the actual structure and content of the repository.
