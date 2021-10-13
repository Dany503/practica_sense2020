import numpy as np
import matplotlib.pyplot as plt


datos = np.loadtxt('datos.csv', delimiter=',')
t = datos[0,:]
accel_x = datos[1,:]
accel_y = datos[2,:]
accel_z = datos[3,:]
gyros_x = datos[4,:]
gyros_y = datos[5,:]
gyros_z = datos[6,:]

plt.figure()
plt.subplot(211)
plt.plot(t,accel_x,'b')
plt.plot(t,accel_y,'r')
plt.plot(t,accel_z,'y')
plt.legend(['x','y','z'])
plt.grid()
plt.xlabel('t (s)')
plt.ylabel('A (Gs)')
plt.title('Muestras de la IMU')

plt.subplot(212)
plt.plot(t,gyros_x,'b')
plt.plot(t,gyros_y,'r')
plt.plot(t,gyros_z,'y')
plt.legend(['x','y','z'])
plt.grid()
plt.xlabel('t (s)')
plt.ylabel('V (rad/s)')
plt.show()
