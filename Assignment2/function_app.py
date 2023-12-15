import logging
import json
import azure.functions as func

app = func.FunctionApp()


def get_base_salary(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data.get("base_salary", 0.0)
    except (FileNotFoundError, json.JSONDecodeError):
        logging.error(f"Error reading base salary from file: {file_path}")
        return 0.0


def save_updated_salary(file_path, updated_salary):
    try:
        with open(file_path, "w") as file:
            json.dump({"base_salary": updated_salary}, file)
    except FileNotFoundError:
        logging.error(f"Error saving updated salary to file: {file_path}")


def SalaryIncrement(myTimer: func.TimerRequest) -> None:
    file_path = "salary.txt"

    base_salary = get_base_salary(file_path)

    print(f"base salary ............... {base_salary}")

    # Increment base salary by 2.5%
    updated_salary = float(base_salary) * 1.025

    # Save the updated salary back to the file
    save_updated_salary(file_path, updated_salary)

    logging.info(f"Base salary: {base_salary}, Updated salary: {updated_salary}")

    if myTimer.past_due:
        logging.info("The timer is past due!")


@app.schedule(
    schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=True, use_monitor=False
)
def SalayIncrement(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info("The timer is past due!")

    SalaryIncrement(myTimer)
    logging.info("Python timer trigger function executed.")
