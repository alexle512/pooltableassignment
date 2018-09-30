import datetime
import json



class PoolTable:
    def __init__(self, table_number):
        self.status = "Available"
        self.table_number = table_number
        


    def __repr__(self):
        return ("{self.table_number}=>  Status: {self.status}")

class TableInterface:

    def __init__(self):
        self.table_data = []
        self.run = True
        self.pool_tables = []
        self.create_tables()
        self.options()


    def create_tables(self):
        for table_number in range(1, 13):
            pool_table = PoolTable(table_number)
            self.pool_tables.append(pool_table)


    def options(self):
        while self.run == True:

            user_selection = int(input("Press: 1 to view tables...2 to reserve a table...3 to terminate a reservation... 4 to exit:  "))

            if user_selection == 1:
                self.view_all()
            if user_selection == 2:
                self.reserve_table()
            if user_selection == 3:
                self.terminate_reservation()
            if user_selection == 4:
                self.exit()


    def view_all(self):
        print('****__POOL TABLES__***')
        for pool_table in self.pool_tables:
            print(pool_table.table_number)
            print(pool_table.status)
            if pool_table.status == "Occupied":
                print(f"Start time: {pool_table.start_time}")
                pool_table.time_now = datetime.datetime.now()
                pool_table.time_elapsed = pool_table.time_now - pool_table.start_time
                print(f"Play Duration: {pool_table.time_elapsed}")


    def reserve_table(self):
        start_choice = int(input("Enter the number of desired pool table: "))
        pool_table = self.pool_tables[start_choice - 1]
        if pool_table.status == "Occupied":
            print(f"Pool Table {pool_table.table_number} is currently occupied.")
        else:
            pool_table.status = "Occupied"
            pool_table.start_time = datetime.datetime.now()
            print(f"Your table is now ready. Table: {pool_table.table_number}.")
            print("Thank You!")


    def terminate_reservation(self):
        terminate_choice = int(input("Enter the pool table number to terminate session: "))
        pool_table = self.pool_tables[terminate_choice - 1]
        if pool_table.status == "Available":
            print(f"Pool Table {pool_table.table_number} is still open.")
        else:
            pool_table.status = "Available"
            pool_table.end_time = datetime.datetime.now()
            pool_table.total_time = (pool_table.end_time.timestamp() - pool_table.start_time.timestamp())


            dictionary = {
                "Table" : str(pool_table.table_number),
                "Start time": str(pool_table.start_time),
                "End time": str(pool_table.end_time),
                "Total time": str(pool_table.total_time),
            }

            self.table_data.append(dictionary)

            for dictionary in self.table_data:
                for b, c in dictionary.items():
                    print(b + ": " + c)

            date_today = datetime.date.today().strftime("%m-%d-%Y")
            with open(f"{date_today}.json", "w") as write_file:
                json.dump(self.table_data, write_file)


    def exit(self):
        print("Thank you for using the pool table manager")
        self.run = False

pool_hall = TableInterface()


