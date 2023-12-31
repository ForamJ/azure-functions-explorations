import azure.functions as func
import logging
import json

# import os
import csv

from applicationinsights import TelemetryClient


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Initialize Application Insights with your Instrumentation Key
app_insights_key = "32a1b9e2-dc78-41b2-8f84-750e77d2eaa3"
telemetry_client = TelemetryClient(app_insights_key)


def track_request(request):
    telemetry_client.context.operation.id = request.headers.get("Request-Id")
    telemetry_client.context.user.id = request.headers.get("x-ms-client-principal-id")
    telemetry_client.context.session.id = request.headers.get("x-ms-client-session-id")


@app.route(route="AddEmployeeDetails")
def AddEmployeeDetails(req: func.HttpRequest) -> func.HttpResponse:
    track_request(req)  # Call this at the beginning of your function

    logging.info("Python HTTP trigger function processed a request.")

    try:
        req_body = req.get_json()

        # Validate input parameter
        if not req_body or not isinstance(req_body, list):
            return func.HttpResponse(
                "Invalid input. Please provide a list of employee details.",
                status_code=400,
            )

        filename = "/tmp/" + "employee_details.csv"
        added_entries = []

        # Append each entry to CSV file
        with open(filename, "a+", newline="\n") as file:
            writer = csv.writer(file)
            for entry in req_body:
                employee_id = entry.get("EmployeeID")
                name = entry.get("Name")
                dob = entry.get("DOB")
                position = entry.get("Position")

                # Validate individual entry
                if not employee_id or not name or not dob or not position:
                    return func.HttpResponse(
                        "Invalid employee details. Please provide EmployeeID, Name, DOB, and Position for each entry.",
                        status_code=400,
                    )

                # Append to CSV file
                writer.writerow([employee_id, name, dob, position])

                # Add to the response list
                added_entries.append(
                    {
                        "EmployeeID": employee_id,
                        "Name": name,
                        "DOB": dob,
                        "Position": position,
                    }
                )

        return func.HttpResponse(json.dumps(added_entries), status_code=200)

    except Exception as e:
        # Log the exception and send telemetry
        telemetry_client.track_exception()
        telemetry_client.flush()  # Ensure telemetry is sent
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)


@app.route(route="DisplayEmployeeDetails")
def DisplayEmployeeDetails(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    try:
        req_body = req.get_json()
        employee_id = req_body.get("EmployeeID")
        print(employee_id)
        fieldnames = ["EmployeeID", "Name", "DOB", "Position"]
        if employee_id is None:
            return func.HttpResponse(
                "Please provide an EmployeeID parameter.", status_code=400
            )

        # Define the path to your local CSV file
        csv_file_path = "/tmp/" + "employee_data.csv"
        # csv_file_path = os.path.join(os.getcwd(), "employee_data.csv")

        # Read the data from the CSV file
        employee_data = []
        with open(csv_file_path, mode="r") as file:
            reader = csv.DictReader(file, fieldnames=fieldnames)
            for row in reader:
                print(row)
                if int(employee_id) == 0 or int(row["EmployeeID"]) == int(employee_id):
                    employee_data.append(row)

        if not employee_data:
            return func.HttpResponse("Employee not found.", status_code=404)

        return func.HttpResponse(
            json.dumps(employee_data), mimetype="application/json", status_code=200
        )

    except Exception as e:
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)


@app.route(route="DeleteEmployeeDetails")
def DeleteEmployeeDetails(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    try:
        req_body = req.get_json()
        employee_id = req_body.get("EmployeeID")
        print(employee_id)
        fieldnames = ["EmployeeID", "Name", "DOB", "Position"]
        if employee_id is None:
            return func.HttpResponse(
                "Please provide an EmployeeID parameter.", status_code=400
            )

        # Define the path to your local CSV file
        csv_file_path = "/tmp/" + "employee_data.csv"
        # csv_file_path = os.path.join(os.getcwd(), "employee_data.csv")

        # Read the CSV file and store the data
        with open(csv_file_path, mode="r") as file:
            csv_reader = csv.DictReader(file, fieldnames=fieldnames)
            data = list(csv_reader)

        deleted_entry = None
        new_data = []

        for row in data:
            if row["EmployeeID"] == employee_id:
                deleted_entry = row
            else:
                new_data.append(row)

        if deleted_entry:
            # Write the updated data (without the deleted entry) back to the CSV file
            with open(csv_file_path, mode="w", newline="") as file:
                # fieldnames = ["EmployeeID", "Name", "DOB", "Position"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                # writer.writeheader()
                writer.writerows(new_data)

            return func.HttpResponse(
                json.dumps(deleted_entry), mimetype="application/json", status_code=200
            )
        else:
            return func.HttpResponse(
                f"Employee with ID {employee_id} not found.", status_code=404
            )

    except Exception as e:
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)
