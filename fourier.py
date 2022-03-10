import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

plt.rcParams['figure.figsize'] = [8,8]
plt.rcParams.update({'font.size' : 20})

# Define Changeable Values
var_num = 69 # Number of cos and sin terms
round_to_digit = 4 # Number of digits to round to
L = np.pi # Range of function, [-L,L]

# Define domain
dx = 1e-5
x = L * np.arange(-1+dx,1+dx,dx)
n = len(x)
nquart = int(np.floor(n/4))

# Define Function

# f = np.sin(x)**2

# Hat function
# f = np.zeros_like(x)
# f[nquart:2*nquart] = (4/n)*np.arange(1,nquart+1)
# f[2*nquart:3*nquart] = np.ones(nquart) - (4/n)*np.arange(0,nquart)

# Signum (sign) function
f = np.ones_like(x)
f[0:2*nquart] = -1*f[0:2*nquart]
f[2*nquart:4*nquart] = f[2*nquart:4*nquart]


# Configure plot
fig,ax = plt.subplots()
ax.plot(x,f,'-',color='k',linewidth = 2)
var_num_print = str(var_num)
if var_num in [69, 34, 420]:
    var_num_print += ' (nice)'
plt.title(f'Fourier Series for {var_num_print} Terms')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x[0],f[0],'bo')
plt.plot(x[-1],f[-1],'bo')

# name = 'Accent'
# cmap = get_cmap('tab10')
# colors = cmap.colors
# ax.set_prop_cycle(color = colors)

# Compute Fourier Series
A0 = np.sum(f * np.ones_like(x)) * dx
frs = A0/2
A0 = round(A0,round_to_digit)
A = np.zeros(var_num)
B = np.zeros(var_num)
for k in range(var_num):
    A[k] = round(np.sum(f * np.cos(np.pi*(k+1)*x/L)) * dx, round_to_digit)
    B[k] = round(np.sum(f * np.sin(np.pi*(k+1)*x/L)) * dx, round_to_digit)
    frs += A[k] * np.cos(np.pi*(k+1)*x/L) + B[k] * np.sin(np.pi*(k+1)*x/L)
ax.plot(x,frs,'-',color='r',linewidth = 2,label = 'Fourier Series')

plt.show()

# Print values
print('A_0 =', A0/2) if A0 != 0 else print('A_0 = N/A')
tab = '\t'
if round_to_digit > 5: tab += '\t'
for k in range(var_num):
    if A[k] != 0 and B[k] != 0:
        print(f'A_{k+1} =', A[k], tab, f'B_{k+1} =', B[k])
    elif A[k] != 0:
        print(f'A_{k+1} =', A[k])
    elif B[k] != 0:
        print(f'B_{k+1} =', B[k])
