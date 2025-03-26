import heapq
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, simpledialog

#FUNCTION TO GET PROCESS DATA
def get_process_data():
    processes = []
    num_processes = simpledialog.askinteger("Input", "Enter the number of processes:")
    if not num_processes:
        return []
    
    for i in range(num_processes):
        arrival = simpledialog.askinteger("Input", f"Enter arrival time for P{i + 1}:")
        burst = simpledialog.askinteger("Input", f"Enter burst time for P{i + 1}:")
        priority = simpledialog.askinteger("Input", f"Enter priority for P{i + 1} (lower = higher priority):", initialvalue=1)
        processes.append({"id": f"P{i+1}", "arrival": arrival, "burst": burst, "priority": priority})
    return processes

