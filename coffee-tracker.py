import csv
with open("data.csv", "a") as csvfile:
    fieldnames = ("Name", "Time", "Date", "Level", "Coffee", "Brew")
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
    writer.writerow({"Name" : input("Name: "), "Time" : input("Time: "), "Date" : input("Date (mm/dd/yyyy): "), "Level" : input("Level (Empty or Not Empty): "), "Coffee" : input("Did they leave with coffee?: "), "Brew" : input("Brew (Yes, No, or N/A): ")})
