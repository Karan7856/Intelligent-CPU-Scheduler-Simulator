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
# FCFS 
def fcfs(processes):
    processes.sort(key=lambda x: x['arrival'])
    time, gantt, total_wt, total_tat = 0, [], 0, 0
    
    for process in processes:
        start_time = max(time, process['arrival'])
        end_time = start_time + process['burst']
        gantt.append((process['id'], start_time, end_time))
        
        total_wt += start_time - process['arrival']
        total_tat += end_time - process['arrival']
        time = end_time
    
    avg_wt = total_wt / len(processes)
    avg_tat = total_tat / len(processes)
    return gantt, avg_wt, avg_tat

# SHORTEST JOB FIRST(SJF)
def sjf(processes):
    processes.sort(key=lambda x: (x['arrival'], x['burst']))
    time, gantt, total_wt, total_tat = 0, [], 0, 0
    ready_queue = []
    
    while processes or ready_queue:
        while processes and processes[0]['arrival'] <= time:
            process = processes.pop(0)
            heapq.heappush(ready_queue, (process['burst'], process['id'], process))
        
        if ready_queue:
            _, pid, process = heapq.heappop(ready_queue)
            start_time = time
            time += process['burst']
            end_time = time
            gantt.append((pid, start_time, end_time))
            total_wt += start_time - process['arrival']
            total_tat += end_time - process['arrival']
        else:
            time += 1
    
    avg_wt = total_wt / len(gantt)
    avg_tat = total_tat / len(gantt)
    return gantt, avg_wt, avg_tat

# ROUND ROBIN SCHEDULING
def round_robin(processes, quantum=2):
    queue = sorted(processes, key=lambda x: x['arrival'])
    time, gantt, total_wt, total_tat = 0, [], 0, 0
    remaining_burst = {p['id']: p['burst'] for p in queue}
    arrival_times = {p['id']: p['arrival'] for p in queue}
    ready_queue = []
    
    while queue or ready_queue:
        while queue and queue[0]['arrival'] <= time:
            ready_queue.append(queue.pop(0))
        
        if ready_queue:
            process = ready_queue.pop(0)
            execute_time = min(quantum, remaining_burst[process['id']])
            start_time = time
            time += execute_time
            gantt.append((process['id'], start_time, time))
            remaining_burst[process['id']] -= execute_time
            
            if remaining_burst[process['id']] > 0:
                while queue and queue[0]['arrival'] <= time:
                    ready_queue.append(queue.pop(0))
                ready_queue.append(process)
            else:
                total_tat += time - arrival_times[process['id']]
                total_wt += total_tat - process['burst']
        else:
            time += 1
    
    avg_wt = total_wt / len(processes)
    avg_tat = total_tat / len(processes)
    return gantt, avg_wt, avg_tat

# PRORITY SCHEDULING
def priority_scheduling(processes):
    if not processes:
        print("No processes to schedule.")
        return [], 0, 0

    processes.sort(key=lambda x: x['arrival'])
    time, gantt = 0, []
    waiting_time, turnaround_time = {}, {}
    remaining_burst = {p['id']: p['burst'] for p in processes}
    original_burst = {p['id']: p['burst'] for p in processes}
    ready_queue, completed = [], set()

    while len(completed) < len(original_burst):  # Run until all processes are completed
        while processes and processes[0]['arrival'] <= time:
            process = processes.pop(0)
            heapq.heappush(ready_queue, (process['priority'], process['arrival'], process['id'], process['burst']))

        if not ready_queue:
            time += 1
            continue

        priority, arrival, pid, burst = heapq.heappop(ready_queue)
        start_time = time
        gantt.append((pid, start_time, start_time + 1))  # Execute for 1 time unit
        remaining_burst[pid] -= 1
        time += 1

        if remaining_burst[pid] == 0:
            turnaround_time[pid] = time - arrival
            completed.add(pid)
        else:
            heapq.heappush(ready_queue, (priority, time, pid, remaining_burst[pid]))

    if len(turnaround_time) == 0:
        return gantt, 0, 0

    avg_wt = sum(turnaround_time[pid] - original_burst[pid] for pid in turnaround_time) / len(turnaround_time)
    avg_tat = sum(turnaround_time.values()) / len(turnaround_time)

    return gantt, avg_wt, avg_tat


# GANTT CHART CODE
def plot_gantt_chart(gantt):
    for process, start, end in gantt:
        plt.barh(process, end - start, left=start, color="lightblue")
    plt.xlabel("Time")
    plt.ylabel("Processes")
    plt.title("Gantt Chart")
    plt.grid(axis="x")
    plt.show()

# GUI CODE
def run_scheduler():
    processes = get_process_data()
    if not processes:
        return
    
    choice = simpledialog.askinteger("Input", "Choose Algorithm:\n1. FCFS\n2. SJF\n3. Round Robin\n4. Priority Scheduling")
    
    if choice == 1:
        gantt, avg_wt, avg_tat = fcfs(processes)
    elif choice == 2:
        gantt, avg_wt, avg_tat = sjf(processes)
    elif choice == 3:
        quantum = simpledialog.askinteger("Input", "Enter Time Quantum:")
        gantt, avg_wt, avg_tat = round_robin(processes, quantum)
    elif choice == 4:
        gantt, avg_wt, avg_tat = priority_scheduling(processes)
    else:
        messagebox.showerror("Error", "Invalid choice")
        return
    
    messagebox.showinfo("Results", f"Average Waiting Time: {avg_wt:.2f}\nAverage Turnaround Time: {avg_tat:.2f}")
    plot_gantt_chart(gantt)

# RUNNING GUICODE
tk.Tk().withdraw()
run_scheduler()

