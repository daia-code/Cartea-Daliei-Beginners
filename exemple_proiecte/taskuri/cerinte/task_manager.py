tasks = []

def add_task(title, description):
    task = {"title": title, "description": description}
    tasks.append(task)
    print("Sarcina a fost adăugată cu succes.")

def view_tasks():
    if not tasks:
        print("Nu există sarcini.")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']}: {task['description']}")

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Sarcina a fost ștearsă cu succes.")
    else:
        print("Index invalid.")
