import random
import time
import tkinter as tk
import matplotlib.pyplot as plt

class SQLTableGenerator:
    def __init__(self, low_set_point, high_set_point):
        self.values = []
        self.timestamps = []
        self.low_set_point = low_set_point
        self.high_set_point = high_set_point
        self.is_running = False
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="")
        self.start_button = tk.Button(self.root, text="START", command=self.start)
        self.stop_button = tk.Button(self.root, text="STOP", command=self.stop)
        self.line_graph_button = tk.Button(self.root, text="Generate Line Graph", command=self.generate_line_graph)

    def generate_value(self):
        while self.is_running:
            value = random.randint(self.low_set_point, self.high_set_point)
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            self.values.append(value)
            self.timestamps.append(timestamp)
            self.check_set_points(value)
            self.label.config(text=f"Value: {value}")
            self.root.update()
            time.sleep(1)

    def check_set_points(self, value):
        if value < self.low_set_point or value > self.high_set_point:
            self.label.config(fg="red")

    def start(self):
        self.is_running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.generate_value()

    def stop(self):
        self.is_running = False
        last_value = self.values[-1] if self.values else None
        self.label.config(text=f"Last Value: {last_value}", fg="black")
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def generate_line_graph(self):
        num_values = len(self.values)
        if num_values < 10:
            x = range(num_values)
            y = self.values
        else:
            x = range(num_values - 10, num_values)
            y = self.values[-10:]

        plt.plot(x, y)
        plt.xticks(x, self.timestamps[-10:], rotation='vertical')
        plt.xlabel('Timestamp')
        plt.ylabel('Value')
        plt.title('Line Graph')
        plt.axhline(self.low_set_point, color='r', linestyle='--')
        plt.axhline(self.high_set_point, color='r', linestyle='--')
        plt.show()

    def run(self):
        self.label.pack()
        self.start_button.pack()
        self.stop_button.pack()
        self.line_graph_button.pack()
        self.root.mainloop()

# Usage example
low_set_point = 50
high_set_point = 100

table_generator = SQLTableGenerator(low_set_point, high_set_point)
table_generator.run()


