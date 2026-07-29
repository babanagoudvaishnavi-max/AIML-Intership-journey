# Day 6: Data Visualization Tasks

This project contains Python scripts to demonstrate basic data visualization using `matplotlib`. The tasks include creating scatter plots, bar charts, and line charts.

## Folder Structure
```text
Day-6/
│
├── data_visualization.py   # Main Python script containing all chart code
├── requirements.txt        # Required Python libraries
└── README.md               # This setup and instruction file
```

## Setup Instructions

1.  **Open in VS Code:** Open the `Day-6` folder directly in VS Code.
2.  **Create a Virtual Environment (Optional but recommended):**
    Open your terminal in VS Code (`Ctrl + \``) and run:
    ```bash
    python -m venv venv
    ```
    Activate the environment:
    - Windows: `venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
3.  **Install Dependencies:**
    Install `matplotlib` using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Code

Run the Python script to see the visualizations:
```bash
python data_visualization.py
```

Each function inside the script will open a window with the chart and also save an image file (`line_chart.png`, `bar_chart.png`, `scatter_plot.png`) in the same directory.
