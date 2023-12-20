import logging
import csv
import os
import azure.functions as func


def main(msg: func.ServiceBusMessage):
    logging.info(
        "Python ServiceBus queue trigger processed message: %s",
        msg.get_body().decode("utf-8"),
    )
    try:
        # Decode the message content and get EmployeeID
        employee_id = msg.get_body().decode("utf-8")

        print("logging from Delete service bus trigger ......................")
        logging.info(f"EmployeeID: {employee_id}")

        # Delete the employee with the specified EmployeeID from the local CSV file
        delete_employee(employee_id)

        logging.info(
            f"Python ServiceBus queue trigger processed message for EmployeeID: {employee_id}"
        )
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


def delete_employee(employee_id):
    # Path to the local CSV file
    file_path = "employee_details.csv"

    # Check if the file exists
    if os.path.exists(file_path):
        # Read existing data from the CSV file
        with open(file_path, "r") as csvfile:
            fieldnames = ["EmployeeID", "Name", "DOB", "Position"]
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            rows = list(reader)

        deleted_entry = None
        new_data = []

        for row in rows:
            if row["EmployeeID"] == employee_id:
                deleted_entry = row
                print(f"deleted data ..................... {deleted_entry}")
            else:
                new_data.append(row)

        # Write the updated data back to the CSV file
        with open(file_path, "w+", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            writer.writerows(new_data)
    else:
        logging.warning(f"CSV file not found at path: {file_path}")
