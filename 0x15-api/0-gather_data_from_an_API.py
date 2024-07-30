import requests
import sys


def fetch_employee_todo_progress(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print(f"Error: Could not retrieve employee data for ID {employee_id}")
        return

    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    # Fetch employee's TODO list
    todos_url = f"""https://jsonplaceholder.typicode.com/todos?userId
={employee_id}"""
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error: Could not retrieve TODO list for employee ID {employee_id}")
        return
    
    todos = todos_response.json()
    
    # Calculate task progress
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Print TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
    
    fetch_employee_todo_progress(employee_id)

