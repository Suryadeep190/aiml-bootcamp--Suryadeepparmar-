import random
import re

from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter, defaultdict

log_file = Path(__file__).resolve().parent / "application.log"

random.seed(42)

levels = ["INFO", "WARN", "ERROR"]

messages = {
    "INFO": [
        "Application started",
        "User logged in",
        "Request processed successfully",
        "File uploaded successfully",
        "User logged out"
    ],

    "WARN": [
        "Memory usage is high",
        "Disk space is running low",
        "Response time is slow",
        "Too many login attempts"
    ],

    "ERROR": [
        "Database connection failed",
        "Database connection failed",
        "Database connection failed",
        "File not found",
        "Payment processing failed",
        "Authentication failed"
    ]
}

current_time = datetime(2026, 11, 19, 8, 0, 0)

with open(log_file, "w", encoding="utf-8") as file:

    for i in range(240):

        level = random.choices(
            levels,
            weights=[60, 25, 15]
        )[0]

        message = random.choice(messages[level])

        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"{timestamp} {level} {message}\n")

        current_time += timedelta(minutes=random.randint(5, 25))

print("Log file generated successfully!")


log_pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|WARN|ERROR) (.+)$"

parsed_entries = []

with open(log_file, "r", encoding="utf-8") as file:

    for line in file:

        line = line.strip()

        match = re.match(log_pattern, line)

        if match:

            timestamp_string, level, message = match.groups()

            timestamp = datetime.strptime(
                timestamp_string,
                "%Y-%m-%d %H:%M:%S"
            )

            parsed_entries.append({
                "timestamp": timestamp,
                "level": level,
                "message": message
            })

print("Total parsed entries:", len(parsed_entries))




level_count = Counter(
    entry["level"] for entry in parsed_entries
)

print("\n--- Log Level Counts ---")

for level, count in level_count.items():
    print(f"{level}: {count}")




hour_count = Counter(
    entry["timestamp"].hour for entry in parsed_entries
)

busiest_hour, busiest_count = hour_count.most_common(1)[0]

print("\n--- Busiest Hour ---")
print(f"{busiest_hour:02d}:00 - {busiest_hour:02d}:59")
print("Total entries:", busiest_count)




error_messages = Counter(
    entry["message"]
    for entry in parsed_entries
    if entry["level"] == "ERROR"
)

print("\n--- Most Frequent ERROR Message ---")

if error_messages:

    message, count = error_messages.most_common(1)[0]

    print("Message:", message)
    print("Occurrences:", count)

else:
    print("No ERROR entries found.")



grouped_logs = defaultdict(list)

for entry in parsed_entries:

    grouped_logs[entry["level"]].append(entry)

print("\n--- Grouped Log Entries ---")

for level, entries in grouped_logs.items():

    print(f"{level}: {len(entries)} entries")




error_entries = sorted(
    [
        entry for entry in parsed_entries
        if entry["level"] == "ERROR"
    ],
    key=lambda entry: entry["timestamp"]
)

longest_gap = timedelta(0)

if len(error_entries) >= 2:

    for i in range(1, len(error_entries)):

        previous_time = error_entries[i - 1]["timestamp"]
        current_time = error_entries[i]["timestamp"]

        gap = current_time - previous_time

        if gap > longest_gap:

            longest_gap = gap
            gap_start = previous_time
            gap_end = current_time

    print("\n--- Longest Gap Between ERROR Entries ---")
    print("Longest gap:", longest_gap)
    print("Previous ERROR:", gap_start)
    print("Next ERROR:", gap_end)

else:
    print("\nNot enough ERROR entries to calculate a gap.")



print("\n========== FINAL SUMMARY ==========")

print("Total log entries:", len(parsed_entries))
print("INFO entries:", level_count["INFO"])
print("WARN entries:", level_count["WARN"])
print("ERROR entries:", level_count["ERROR"])
print("Unique ERROR messages:", len(error_messages))