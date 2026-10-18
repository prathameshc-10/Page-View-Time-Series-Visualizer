# Page View Time Series Visualizer

Analyze daily freeCodeCamp forum page views from 2016 to 2019 with Pandas, Matplotlib, and Seaborn.

## Included files

- `time_series_visualizer.py` — data cleaning and three chart functions.
- `main.py` — generates and displays all three charts.
- `test_module.py` — basic smoke tests for generated plots.
- `download_dataset.py` — downloads `fcc-forum-pageviews.csv`.
- `requirements.txt` — Python dependencies.

## Setup

Use Python 3.9 or newer. Open a terminal in this folder.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt**
```bat
.venv\Scripts\activate.bat
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install dependencies and download the dataset:

```bash
python -m pip install -r requirements.txt
python download_dataset.py
```

## Run

```bash
python main.py
```

The charts are saved as `line_plot.png`, `bar_plot.png`, and `box_plot.png`.

## Test

```bash
python -m unittest test_module.py
```

