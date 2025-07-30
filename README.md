# CodeCarbon CLI Tool

This is a simple command-line interface (CLI) tool to estimate the **CO₂ emissions** of any Python script using the [CodeCarbon](https://mlco2.github.io/codecarbon/) library. It is ideal for developers and researchers who want to understand and reduce the environmental impact of their code.

## Features

- Tracks the energy consumption and estimated CO₂ emissions of a Python script.
- Saves a CSV log file with detailed emissions data.
- Automatically creates a timestamped log for every run.
- Lightweight and easy to use—just one command to get started.

## Requirements

- Python **3.6+**
- `codecarbon` library
- `numpy` (for sample script testing)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/CodeCarbon-CLI-Tool.git
cd CodeCarbon-CLI-Tool
````

2. Install required packages:

```bash
pip install codecarbon numpy
```

## Usage

### Step 1: Prepare your script

Make sure you have a Python script (e.g., `your_script.py`) you want to measure.

### Step 2: Run the CLI tool

```bash
python codecarbon_cli.py your_script.py
```
* This will run your script and output a CSV file inside the `codecarbon_logs/` folder.

## Output

The tool creates a directory called `codecarbon_logs` and saves a CSV file like:

```
emissions_20240715_154210.csv
```

The file includes:

* Duration
* Energy consumed (kWh)
* Estimated emissions (kg CO₂)
* CPU/GPU usage info
* Geographic location (based on IP)

## Sample Script

We’ve included a test script `sample_task.py` that performs basic matrix multiplication to simulate workload.

## License

MIT License

## Contributing

Pull requests are welcome! If you have ideas to extend this tool (e.g., visual summaries, GitHub Actions integration), feel free to fork and contribute.

**Created by [Maliha Nawshin Rahman](https://www.linkedin.com/in/your-profile)**
