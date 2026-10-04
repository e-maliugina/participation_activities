import importlib

while True:
    module_name = input("\nEnter the name of the module you want to import: ")
    try:
        imported_module = importlib.import_module(module_name)
        print(f"\nModule '{module_name}' was imported successfully!")
        break
    except ModuleNotFoundError:
        print(f"\nModule '{module_name}' can't be found, try again.")