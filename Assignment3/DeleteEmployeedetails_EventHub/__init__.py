from typing import List
import logging
import csv
import json
import azure.functions as func


def main(events: List[func.EventHubEvent]):
    for event in events:
        logging.info(
            "Python EventHub trigger processed an event: %s",
            event.get_body().decode("utf-8"),
        )
        try:
            # Extract EmployeeID from the event body (assuming the event body is a JSON payload)
            employee_data = event.get_body().decode("utf-8")
            employees_details = json.loads(employee_data)
            employee_details = employees_details

            # print(f"employee details ................. {employee_details}")
            employeeID = employee_details.get("EmployeeID")

            print(f"employee ID ................. {employeeID}")
            fieldnames = ["EmployeeID", "Name", "DOB", "Position"]

            # Read the existing CSV file into a list of dictionaries
            with open("employee_details.csv", mode="r") as file:
                reader = csv.DictReader(file, fieldnames=fieldnames)
                rows = list(reader)

            deleted_entry = None
            new_data = []
            # print(f"rows .......................... {rows}")
            for row in rows:
                if row["EmployeeID"] == employeeID:
                    deleted_entry = row
                    print(f"deleted data ............... {deleted_entry}")
                else:
                    new_data.append(row)

            # Write the updated rows back to the CSV file
            with open("employee_details.csv", mode="w+", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                # writer.writeheader()
                writer.writerows(new_data)

            print(f"Employee details deleted: EmployeeID={employeeID}")
        except Exception as e:
            print(f"Error processing event: {str(e)}")


# "EmployeeID" : "3555"
