This repository contains datasets and scripts for analyzing the OpenAI Developer Forum and GitHub issues data from major vendors (Gemini, Llama, and OpenAI). The goal is to explore community interaction patterns, identify challenges, and analyze trends.

---

## File Structure and Descriptions

### Figures Folder (`Figures/`)

- This folder contains all the figures used in the associated research paper, including charts, diagrams, and visualizations.

### GitHub Dataset Folder (`Github_Dataset/`)

This folder contains GitHub issues data collected from three vendors:
- **`Gemini/`**: GitHub issues data related to the Gemini project.
- **`Llama/`**: GitHub issues data related to the Llama project.
- **`OpenAI/OpenAI/`**:
  - **`github.xlsx`**: Complete GitHub issues data for OpenAI.
  - **`github_issues.xlsx`**: Filtered GitHub issues dataset.
  - **`sampled_github_issues.xlsx`**: A sampled subset of the GitHub issues dataset, used for constructing the taxonomy.

### OpenAI Dataset Folder (`OpenAI_Dataset/`)

This folder contains data collected from the OpenAI Developer Forum:
- **`annotated_dataset.xlsx`**: Annotated forum posts dataset, used for constructing the taxonomy.
- **`posts.csv`**: Complete dataset of forum posts, including metadata (e.g., titles, links, times).
- **`users.xlsx`**: User profile data, including user activities and registration details.

### Scripts Folder (`Scripts/`) 

1. **Crawling Scripts**: Python scripts for extracting posts (`chatgpt.py`, `other.py`) and user information (`code.py`, `desc+data.py`).  
2. **Data Organization**: Includes text files (`page.txt`, `url_to_title.py`) for organizing and parsing data.  
3. **RQ Analysis and Visualization**: Original chart data and analysis scripts for RQ1 and RQ2 are stored in corresponding subfolders, with Excel files (`data.xlsx`) supporting the analysis.  
---

## Quick Start


1. **Prepare the Environment**

   Ensure Python 3.8+ is installed along with the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run Crawling Scripts**

   Navigate to the `Scripts/` folder and run the scripts to collect data:

   ```bash
   python chatgpt.py
   python other.py
   ```

3. **Analyze Data**

    For popularity and difficulty analysis, refer to the scripts and data located in the RQ1 and RQ2 folders.
For analyzing the challenge taxonomy, use the datasets annotated_dataset.xlsx and sampled_issues.xlsx. These files provide the necessary data for exploring and refining the categorization of challenges.
---

## Project Goals

- **Vendor Comparison**: Analyze GitHub issues across Gemini, Llama, and OpenAI to identify common challenges and trends.
- **Popularity Analysis**: Explore trends in the popularity of forum posts over time.
- **Difficulty Analysis**: Assess the difficulty levels of forum post content.

Contributions and feedback are welcome!

---
