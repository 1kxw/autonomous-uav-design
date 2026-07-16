import numpy


mass = 2.2
rho = 1.225
cruise_speed = 25
stall_fraction = 0.7
CL_max = 1.3
aspect_ratio = 8

W = mass * 9.81
V_stall = cruise_speed * stall_fraction
S = 2 * W / (rho * V_stall**2 * CL_max)
b = numpy.sqrt(aspect_ratio * S)
c = S / b

print(f"Wing area: {S:.3f} m^2")
print(f"Wingspan: {b:.3f} m")
print(f"Mean chord: {c:.3f} m")