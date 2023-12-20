import logging
import csv
import json
import azure.functions as func


def main(msg: func.ServiceBusMessage):
    logging.info(
        "Python ServiceBus queue trigger processed message: %s",
        msg.get_body().decode("utf-8"),
    )

    employee_details_str = msg.get_body().decode("utf-8")
    employee_details = json.loads(employee_details_str)

    print("logging into Add employee service bus trigger function ...............")
    logging.info(employee_details)

    # import pdb

    # pdb.set_trace()

    # Parse the message and append to a local CSV file
    with open("employee_details.csv", "a+", newline="\n") as csvfile:
        fieldnames = ["EmployeeID", "Name", "DOB", "Position"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(employee_details)

    logging.info("Python ServiceBus queue trigger processed message.")


# {
#     "EmployeeID" : 3450,
#     "Name" : "Foram Jivani",
#     "DOB" : "09/12/1991",
#     "Position" : "MLE"
# }
