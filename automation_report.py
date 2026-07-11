# File: automation_report.py
# Description: Scans a directory and generates a detailed analysis report of files by type, age, and metadata
# Assignment Number: 9
# Name: <YOUR NAME>
# SID: <YOUR SID>
# Email: <YOUR EMAIL>
# Grader: <YOUR GRADER'S NAME Carolyn OR Emma or Ahmadi>
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

import os
import datetime


def count_file_types(directory_path):
    """
    Counts files by type in the directory.
    Returns tuple: (total_files, txt_count, py_count, csv_count, other_count)
    """
    try:
        files = os.listdir(directory_path)
        total = 0
        txt_count = 0
        py_count = 0
        csv_count = 0
        other_count = 0

        for filename in files:
            filepath = os.path.join(directory_path, filename)
            if os.path.isfile(filepath):
                total += 1
                if filename.endswith('.txt'):
                    txt_count += 1
                elif filename.endswith('.py'):
                    py_count += 1
                elif filename.endswith('.csv'):
                    csv_count += 1
                else:
                    other_count += 1

        return total, txt_count, py_count, csv_count, other_count

    except PermissionError:
        raise PermissionError("Unable to access directory.")


def find_file_dates(directory_path):
    """
    Finds oldest and newest files in directory.
    Returns tuple: (oldest_filename, newest_filename)
    """
    try:
        files = os.listdir(directory_path)
        oldest_file = None
        newest_file = None
        oldest_time = float('inf')
        newest_time = float('-inf')

        for filename in files:
            filepath = os.path.join(directory_path, filename)
            if os.path.isfile(filepath):
                mod_time = os.path.getmtime(filepath)

                if mod_time < oldest_time:
                    oldest_time = mod_time
                    oldest_file = filename

                if mod_time > newest_time:
                    newest_time = mod_time
                    newest_file = filename

        return oldest_file, newest_file

    except PermissionError:
        raise PermissionError("Unable to access directory.")


def find_old_files(directory_path, days_threshold):
    """
    Finds files older than specified days (BONUS feature).
    Returns count of old files.
    """
    try:
        files = os.listdir(directory_path)
        old_file_count = 0
        current_time = datetime.datetime.now()

        for filename in files:
            filepath = os.path.join(directory_path, filename)
            if os.path.isfile(filepath):
                mod_time = os.path.getmtime(filepath)
                file_datetime = datetime.datetime.fromtimestamp(mod_time)
                age_days = (current_time - file_datetime).days

                if age_days > days_threshold:
                    old_file_count += 1

        return old_file_count

    except PermissionError:
        raise PermissionError("Unable to access directory.")


def generate_report(directory_path, total_files, txt_count, py_count, csv_count, other_count, oldest_file, newest_file,
                    old_files_count):
    """
    Generates and writes the automation report to a text file.
    """
    try:
        current_time = datetime.datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open('automation_report.txt', 'w') as report_file:
            report_file.write("AUTOMATION REPORT\n")
            report_file.write("=================\n\n")
            report_file.write(f"Directory: {directory_path}\n\n")
            report_file.write(f"Total Files: {total_files}\n\n")
            report_file.write(f"Text Files: {txt_count}\n")
            report_file.write(f"Python Files: {py_count}\n")
            report_file.write(f"CSV Files: {csv_count}\n")
            report_file.write(f"Other Files: {other_count}\n\n")
            report_file.write(f"Oldest File: {oldest_file}\n")
            report_file.write(f"Newest File: {newest_file}\n\n")
            report_file.write(f"Files Older Than 30 Days: {old_files_count}\n\n")
            report_file.write(f"Generated: {timestamp}\n")

    except IOError:
        print("An unexpected error occurred.")


def display_summary(total_files, txt_count, py_count, csv_count, other_count, oldest_file, newest_file):
    """
    Displays the analysis summary to the console.
    """
    print("\nDirectory Analysis Complete\n")
    print(f"Total Files: {total_files}")
    print(f"Text Files: {txt_count}")
    print(f"Python Files: {py_count}")
    print(f"CSV Files: {csv_count}")
    print(f"Other Files: {other_count}\n")
    print(f"Oldest File: {oldest_file}")
    print(f"Newest File: {newest_file}\n")
    print("Report written to automation_report.txt")


def main():
    """
    Main program: orchestrates directory scanning and report generation.
    """
    print("Python Automation Report Generator")
    print("==================================\n")
    directory_name = input("Enter directory name: ")

    try:
        if not os.path.isdir(directory_name):
            print("Directory does not exist. Ending program.")
            return

        total_files, txt_count, py_count, csv_count, other_count = count_file_types(directory_name)
        oldest_file, newest_file = find_file_dates(directory_name)
        old_files_count = find_old_files(directory_name, 30)

        generate_report(directory_name, total_files, txt_count, py_count, csv_count, other_count, oldest_file,
                        newest_file, old_files_count)
        display_summary(total_files, txt_count, py_count, csv_count, other_count, oldest_file, newest_file)

    except PermissionError:
        print("Unable to access directory.")
    except Exception:
        print("An unexpected error occurred.")


if __name__ == "__main__":
    main()