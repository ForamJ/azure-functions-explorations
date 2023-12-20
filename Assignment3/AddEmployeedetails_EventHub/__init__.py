from typing import List
import logging
import json
import csv
import azure.functions as func


def main(events: List[func.EventHubEvent]):
    for event in events:
        logging.info(
            "Python EventHub trigger processed an event: %s",
            event.get_body().decode("utf-8"),
        )
        try:
            # Extract employee details from the event body (assuming the event body is a JSON payload)
            employee_data = event.get_body().decode("utf-8")
            employees_details = json.loads(employee_data)

            employee_details = employees_details

            print(f"employee details ................. {employee_details}")

            # Extract individual details
            employeeID = employee_details.get("EmployeeID")
            name = employee_details.get("Name")
            dob = employee_details.get("DOB")
            position = employee_details.get("Position")

            # Append to CSV file
            with open("employee_details.csv", mode="a+", newline="\n") as file:
                writer = csv.writer(file)
                writer.writerow([employeeID, name, dob, position])

            print(
                f"Employee details added: EmployeeID={employeeID}, Name={name}, DOB={dob}, Position={position}"
            )
        except Exception as e:
            print(f"Error processing event: {str(e)}")


# {
#     "EmployeeID" : 3555,
#     "Name" : "John Dave",
#     "DOB" : "12/12/1865",
#     "Position" : "Lead MLE"
# }

# EntityPath=addemployeedetails_eventhub;EntityPath=deleteemployeedetails_eventhub
