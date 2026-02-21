from datetime import datetime
import os

def generate_log(log_data):
    """
    Create a log file named log_YYYYMMDD.txt and write each entry on its own line.
    Returns the filename.
    Raises ValueError if log_data is not a list.
    """
    if type(log_data) is not list:
        raise ValueError("log_data must be a list")

    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        for item in log_data:
            f.write(f"{item}\n")

    return filename

if __name__ == "__main__":
    sample = ["User logged in", "User updated profile", "Report exported"]
    file_name = generate_log(sample)
    print(f"Log written to {file_name}")