import os

# print(os.getcwd())
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.listdir())


# for i in os.listdir():
#     if os.path.isfile(i):
#         print(i)
#     elif os.path.isdir(i):
#         print(f"{i} is a directory")


last_load = "2026-01-10"
for i in os.listdir((os.path.join(os.path.dirname(os.path.abspath(__file__)), "Data"))):
    if i.split(".")[0] > last_load:
        print(f"Processed {i} new file")