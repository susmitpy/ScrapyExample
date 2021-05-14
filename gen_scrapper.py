from jinja2 import Environment, FileSystemLoader
import os


init = input("Do you want to create scrapper.py ? Y/N: ").upper()
scrapping_item_name = input("Type Scrapping item name: ") 

scrapping_item_name = scrapping_item_name.capitalize() + "Item"
module_path = f"./{scrapping_item_name.lower()}_scrapper"

if init == "Y":
    if os.path.exists("./scrapper.py"):
        raise Exception("scrapper.py already exists !")

if os.path.exists(module_path):
    raise Exception("Module with name " + scrapping_item_name.lower() + "_scrapper already exists!")

os.mkdir(module_path)


env = Environment(loader=FileSystemLoader('templates'))

template = env.get_template('item.jinja')
item_file = template.render(name=scrapping_item_name)
with open(f"{module_path}/item.py", "w") as fh:
    fh.write(item_file)

template = env.get_template('spider.jinja')
item_file = template.render(name=scrapping_item_name)
with open(f"{module_path}/spider.py", "w") as fh:
    fh.write(item_file)

template = env.get_template('store.jinja')
item_file = template.render(name=scrapping_item_name)
with open(f"{module_path}/store.py", "w") as fh:
    fh.write(item_file)


template = env.get_template('pipeline.jinja')
item_file = template.render(name=scrapping_item_name)
with open(f"{module_path}/pipeline.py", "w") as fh:
    fh.write(item_file)

template = env.get_template('config.jinja')
item_file = template.render(name=scrapping_item_name)
with open(f"{module_path}/config.py", "w") as fh:
    fh.write(item_file)

if init == "Y":
    if os.path.exists("./scrapper.py"):
        raise Exception("scrapper.py already exists !")
    template = env.get_template('scrapper.jinja')
    item_file = template.render(name=scrapping_item_name)
    with open(f"./scrapper.py", "w") as fh:
        fh.write(item_file)

print("Code Generation Complete !")