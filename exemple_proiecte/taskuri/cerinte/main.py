from task_manager import add_task, view_tasks, delete_task

def main():
    while True:
        print("\nAplicație de Gestionare a Sarcinilor")
        print("1. Adaugă o sarcină")
        print("2. Afișează toate sarcinile")
        print("3. Șterge o sarcină")
        print("4. Ieșire")

        choice = input("Alege o opțiune: ")

        if choice == '1':
            title = input("Introduce titlul sarcinii: ")
            description = input("Introduce descrierea sarcinii: ")
            add_task(title, description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                index = int(input("Introduce indexul sarcinii de șters: ")) - 1
                delete_task(index)
            except ValueError:
                print("Introduceți un număr valid.")
        elif choice == '4':
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă, te rog încearcă din nou.")

if __name__ == "__main__":
    main()
