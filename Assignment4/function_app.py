import azure.functions as func
import logging
import json

# import os
import csv

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="AddEmployeeDetails")
def AddEmployeeDetails(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    try:
        req_body = req.get_json()

        if not req_body:
            return func.HttpResponse(
                "Please provide a request body with"
                + " EmployeeID, Name, DOB, and Position.",
                status_code=400,
            )
        employee_id = req_body.get("EmployeeID")
        name = req_body.get("Name")
        dob = req_body.get("DOB")
        position = req_body.get("Position")

        print(employee_id, name, dob, position)

        if not (employee_id and name and dob and position):
            return func.HttpResponse(
                "Please provide all required parameters:"
                + " EmployeeID, Name, DOB, and Position.",
                status_code=400,
            )

        if employee_id and name and dob and position:
            # Define the path to your local CSV file
            csv_file_path = "/tmp/" + "employee_data.csv"
            # os.path.join(os.getcwd(), "employee_data.csv")

            # Append the data to the CSV file
            with open(csv_file_path, mode="a+", newline="\n") as file:
                writer = csv.writer(file)
                # if os.path.getsize(csv_file_path) == 0:
                #     # If the file is empty, add a header row
                #     writer.writerow(["EmployeeID", "Name", "DOB", "Position"])
                writer.writerow([employee_id, name, dob, position])

            # Create a response JSON
            response_data = {
                "EmployeeID": employee_id,
                "Name": name,
                "DOB": dob,
                "Position": position,
            }

            return func.HttpResponse(
                json.dumps(response_data), mimetype="application/json", status_code=200
            )
        else:
            return func.HttpResponse(
                (
                    "This HTTP triggered function executed successfully."
                    + "Pass a name in the query string or in the request"
                    + " body for a personalized response."
                ),
                status_code=200,
            )

    except Exception as e:
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
