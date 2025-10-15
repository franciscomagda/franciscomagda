import matplotlib.pyplot as plt

times = []
voltages = []
currents = []

with open("solar_data.txt") as f:
    next(f)
    for line in f:
        t_str, v_str, i_str = line.split(",")
        t = float(t_str)
        v = float(v_str)
        i = float(i_str)

        times.append(t)
        voltages.append(v)
        currents.append(i)

powers = [v * i for v, i in zip(voltages, currents)]

plt.figure(1)
plt.plot(times, voltages, 'o-', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Volatge vs Time')
plt.grid(True)
plt.show()

plt.figure(2)
plt.plot(voltages, powers, 'o-', color='orange')
plt.xlabel('Voltage (V)')
plt.ylabel('Power (W)')
plt.title('Power vs Voltage')
plt.grid(True)
plt.show()