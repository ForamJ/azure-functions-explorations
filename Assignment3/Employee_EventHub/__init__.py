import logging
import json
import azure.functions as func
from azure.eventhub import EventHubProducerClient, EventData

EVENTHUB_CONNECTION_STRING = "Endpoint=sb://mle-azurefunction-eventhub.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=gcV2MXdryxPx+8T8mup0hQe9khM0jbCy6+AEhMyOxDI="
EVENTHUB_NAME_ADD = "AddEmployeeDetails_EventHub"
EVENTHUB_NAME_DELETE = "DeleteEmployeeDetails_EventHub"


def send_add_employee_message(employee_id, name, dob, position):
    event_data = json.dumps(
        {"EmployeeID": employee_id, "Name": name, "DOB": dob, "Position": position}
    )
    send_message(EVENTHUB_NAME_ADD, event_data)


def send_delete_employee_message(employee_id):
    event_data = json.dumps({"EmployeeID": employee_id})
    send_message(EVENTHUB_NAME_DELETE, event_data)


def send_message(eventhub_name, event_data):
    producer_client = EventHubProducerClient.from_connection_string(
        EVENTHUB_CONNECTION_STRING, eventhub_name=eventhub_name
    )
    try:
        with producer_client:
            event_data_batch = producer_client.create_batch()
            event_data_batch.add(EventData(event_data))
            producer_client.send_batch(event_data_batch)
    except Exception as e:
        logging.error(f"An error occurred while sending message to Event Hub: {str(e)}")
    finally:
        producer_client.close()


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
