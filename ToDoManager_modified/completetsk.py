"""This module is designed for the completing process of a task, if a
user completes a task, then  this module  will  be used to update the
data and other housekeeping"""

#Importing modules
import json
import datetime
import ToDoManager_modified.colours as c
import ToDoManager_modified.resetdata as resetdata
import get_path

#Abs. path of files so that they don't get stuck anywhere if we import Main.py out of TDM
data_json = get_path.get_path("ToDoManager_modified", "data.json")


#Func
def complete(*tasks):
    try:
        with open(data_json, "r") as file_in:
            data = json.load(file_in)

            # Will remove the task given
            for task in tasks:
                poihis = data["PoiHis"]

                # Deleting the task for data
                del data[task]

                # Updating points
                data["total_points"] += 8
                print(f"""{c.light_green}8 points has been added for completing the task <3{c.end}""")

                # Updating history
                poihis[f"{datetime.datetime.now()}"] = [+8, "Completed a task :)"]

                #praising
                print(f"{c.Electric_Blue}Congratulation!!! Task Completed{c.end}")

        # Updating the data in data,json
        with open(data_json, "w") as file_out:

            json.dump(data, file_out, indent=4)


    #Exception handling
    # Just to don't raise error during an empty file
    except json.JSONDecodeError:
        msg = f"{c.red}No task in inventory!!!{c.end}"
        print(msg)

    # If no file is there
    except FileNotFoundError:
        msg = f"{c.red}No task in inventory!!!{c.end}"
        print(msg)
        resetdata.reset()

    # If a task does not exist
    except KeyError as er:
        msg = f"{c.red}{er} : Task not found!!! Recheck the name of the task{c.end}"
        print(msg)