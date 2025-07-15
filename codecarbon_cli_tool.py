# CodeCarbon CLI Tool
# Description: A simple command-line interface to run a Python script and log its carbon emissions using CodeCarbon

import argparse
import subprocess
from codecarbon import EmissionsTracker
import os
import datetime

def run_script_with_tracker(script_path):
    # Prepare logging directory
    log_dir = "codecarbon_logs"
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"emissions_{timestamp}.csv")

    # Initialize emissions tracker
    tracker = EmissionsTracker(output_dir=log_dir, output_file=f"emissions_{timestamp}.csv")
    tracker.start()

    # Run the script
    try:
        print(f"Running script: {script_path}")
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")
    finally:
        emissions = tracker.stop()
        print(f"Estimated CO2 emissions: {emissions:.6f} kg")
        print(f"Log saved to: {log_file}")

def main():
    parser = argparse.ArgumentParser(description="Run a Python script and measure its CO2 emissions with CodeCarbon.")
    parser.add_argument("script", help="Path to the Python script to run")
    args = parser.parse_args()

    if not os.path.isfile(args.script):
        print(f"Script not found: {args.script}")
        return

    run_script_with_tracker(args.script)

if __name__ == "__main__":
    main()
