import os
import pandas as pd


def list_content(directory):
    items = [{"Name": os.path.basename(directory), "Type": "Directory", "Size": None}]
    item_type = ''
    item_size = 0
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            item_type = "File"
            item_size = os.path.getsize(item_path)
        elif os.path.isdir(item_path):
            item_type = "Directory"
            item_size = None
        item_dict = {"Name": item, "Type": item_type, "Size": item_size}
        items.append(item_dict)

    df = pd.DataFrame(items)
    return df


# Example usage:
directory_path = "images/fprofiles"
directory_df = list_content(directory_path)
print(directory_df)
