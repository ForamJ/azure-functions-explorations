import logging
import json
import azure.functions as func

from azure.servicebus import ServiceBusClient, ServiceBusMessage

CONNECTION_STR = "Endpoint=sb://mle-azurefunction-servicebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=5MbB61A9agnAPNmbOH6cTX1y90mAU5ftE+ASbPKem2Y="
TOPIC_NAME = "fj-assignment3-topic"


def send_single_message(sender, message_content):
    message = ServiceBusMessage(message_content)
    sender.send_messages(message)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    try:
        # Get operation from the query parameters
        operation = req.params.get("Operation")
        logging.info(f"operation ........................{operation}")

        if operation == "AddEmployee":
            # Read parameters from the request payload
            data = req.get_json()
            employee_id = data.get("EmployeeID")
            name = data.get("Name")
            dob = data.get("DOB")
            position = data.get("Position")

            print(f"employee id ................... {employee_id}")
            print(f"employee name ................... {name}")
            print(f"dob ................... {dob}")
            print(f"position ................... {position}")

            # Send message to AddEmployeeDetails_ServiceBus topic subscription
            send_add_employee_message(employee_id, name, dob, position)

            return func.HttpResponse(
                f"Employee added with ID: {employee_id}", status_code=200
            )
        elif operation == "DeleteEmployee":
            # Read EmployeeID from the request payload
            data = req.get_json()
            employee_id = data.get("EmployeeID")

            # Send message to DeleteEmployeeDetails_ServiceBus queue
            send_delete_employee_message(employee_id)

            return func.HttpResponse(
                f"Employee deleted with ID: {employee_id}", status_code=200
            )
        else:
            return func.HttpResponse("Invalid operation specified", status_code=400)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return func.HttpResponse("Internal Server Error", status_code=500)


def send_add_employee_message(employee_id, name, dob, position):
    payload = {
        "EmployeeID": employee_id,
        "Name": name,
        "DOB": dob,
        "Position": position,
    }
    # Convert the dictionary to a JSON string
    json_message = json.dumps(payload)

    servicebus_client = ServiceBusClient.from_connection_string(
        conn_str=CONNECTION_STR, logging_enable=True
    )
    with servicebus_client:
        sender = servicebus_client.get_topic_sender(topic_name=TOPIC_NAME)
        with sender:
            send_single_message(sender, json_message)

    print("Add Employee Send message is done.")


def send_delete_employee_message(employee_id):
    # Replace with the URL of your Azure Function that handles deleting employees
    # function_url = "http://localhost:7071/api/DeleteEmployeeDetails_ServiceBus"
    payload = {"EmployeeID": employee_id}
    # headers = {"Content-Type": "application/json"}
    # Convert the dictionary to a JSON string
    json_message = json.dumps(payload)

    servicebus_client = ServiceBusClient.from_connection_string(
        conn_str=CONNECTION_STR, logging_enable=True
    )
    with servicebus_client:
        sender = servicebus_client.get_topic_sender(topic_name=TOPIC_NAME)
        with sender:
            send_single_message(sender, employee_id)

    print("Delete Employee Send message is done.")
    # # Send HTTP POST request to the target function
    # response = requests.post(function_url, json=payload, headers=headers)
    # response.raise_for_status()


# {
#     "Operation": "AddEmployee",
#     "EmployeeID": 5555,
#     "Name": "Dimple Jain",
#     "DOB": "15/08/1996",
#     "Position": "Analyst"
# }
