#Intelligent CPU Scheduler Simulator
Overview
The intelligent CPU Scheduler Simulator is an intelligent tool designed to simulate and visualize various CPU Scheduling Algorithm like
1) FCFS(First Come First Serve): In FCFS the Process is executed first which arrives first
2) SJF(Shortest Job First): In SJF the Process having the lowest burst time is executed First
3) PRIORITY SCHEDULING: In Priority Scheduling the Process which has the highest priority is executed
4) ROUND ROBIN: In round robin there is a specific time Quantum in which each process is executed
This project provides real-time visualizations, Gantt charts, and performance metrics for better understanding and analysis of CPU scheduling techniques.

FEATURES
1)Supports multiple scheduling algorithms
2)Interactive Gantt Chart visualization
3)Real-time performance metrics (Turnaround Time, Waiting Time, etc.)
4)User-friendly interface
5) Simulates preemptive and non-preemptive scheduling
6)Customizable process input (arrival time, burst time, priority, etc.)

HOW CAN WE USE THIS 
1. USER INPUT: Give the user input of the process details like the number of processes, arrival time of each process, burst time of each process and time quantum if applicable and the priority of the process
2. ALGORITHM EXECUTION: The CPU analyses the user input and process the input
3. VISUALIZATION: A Gantt chart is used to generate to show the execution order

Installation
Prerequisites
Ensure you have the following installed:

Python (if implemented in Python)
Required libraries (e.g., matplotlib for Python visualization)

Usage Guide
Select an algorithm from the menu.

Input process details (arrival time, burst time, priority).

Click Run Simulation to visualize execution order and performance metrics.

Performance Metrics
Turnaround Time (TAT) = Completion Time - Arrival Time

Waiting Time (WT) = Turnaround Time - Burst Time

Response Time (RT) = Time when process first starts execution - Arrival Time


Future Improvements
🔹 Add ML-based intelligent scheduling
🔹 Implement additional scheduling algorithms (Multilevel Queue, Multilevel Feedback Queue)
🔹 Web-based interface for accessibility

CONTRIBUTORS
1)KARAN RAJ
2) ABHINAV
   GITHUB ID: Abhinavkumar550
3) SAURABH SANGWAN
   GITHUB ID:
