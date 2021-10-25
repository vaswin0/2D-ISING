#!/usr/bin/env python
# coding: utf-8

'''
Python script to simulate 2d ising model
using metropolis-hasting algorithm


'''




import matplotlib.pyplot as plt
import random
import numpy as np
from PIL import Image





def spin_matrix(N,M):
    return np.random.choice([-1,1],size=(N,M))






def visualize(ising):
    return Image.fromarray(np.uint8((ising+1)*0.5+255))





def deltaE(present,i,j,N,J):
    return 2*J*present[i%N][j%N]*( present[i%N][(j+1)%N]+present[i%N][(j-1)%N]+present[(i+1)%N][j%N]+present[(i-1)%N][j%N] )





def ENERGY(lattice, N, J):
    '''Fn to compute energy''' 
    energy = 0
    
    for i in range(N):
        for j in range(N):
            
            energy += -J * lattice[i%N][j%N] * (lattice[i%N][(j + 1)%N] + lattice[i%N][(j-1)%N] + lattice[(i+1)%N][j%N] + lattice[(i-1)%N][j%N] )
            
            
    return energy/2
                





def spec_heat(ene_list):
    '''fn to compute specific heat
      args: energy of the system after each flip'''
    
    ene_ = np.array(ene_list)
    
    avg_ene = np.sum(ene_)/len(ene_)
    
    sigma_sq = np.sum((ene_ - avg_ene)**2)/len(ene_)
    
    
    return sigma_sq
    
    
    
    
    


# In[29]:


def CHI(mag_list):
    
    mag_ = np.array(mag_list)
    avg_mag = np.sum(mag_)/len(mag_)
    
    sigma_sq_mag = np.sum((mag_ - avg_mag)**2)/len(mag_)
    
    
    return sigma_sq_mag
    





def evolve(N,steps,T,J):
    
    '''FN to to flip spins 
    using the MC
    args: N - lattice sites
          steps - number of MC sweeps
          T - temperature
          J - coupling constant/ exchange energy'''
    
    ene_list = []
    mag_list = []
    
    
    

     #=np.zeros(steps)
    #lattice = spin_matrix(N,N)
    lattice = np.ones((N,N))

    #visualize(lattice)



    for ii in range(steps):
        random.seed(a=None, version=2)
        i=random.randint(0,N-1)
        j=random.randint(0,N-1)
        
    
        ediff = deltaE(lattice,i,j,N,J)
    
        if ediff < 0 or random.random() < np.exp(-ediff/T):
            lattice[i][j] =- lattice[i][j]
            
        ene_list.append(ENERGY(lattice, N, J))
        mag_list.append(np.sum(lattice)/(N**2))
        
            
     
    m = np.sum(lattice)/(N*N)
    en = ENERGY(lattice, N, J)
    cv = spec_heat(ene_list) /T**2  
    chi = CHI(mag_list)/T
        
      
    return m ,lattice, en, cv, chi





TEMP = np.arange(5, 0.5, -0.5)
M = []
En = []

CV = []

KAI = []

LATTICE = []

for temp in TEMP:
    
    mag, lattice, ene, Cv, kai = evolve(20,30000,temp, 1)
    
    M.append(mag)
    
    En.append(ene)
    
    CV.append(Cv)
    
    KAI.append(kai)
    
    LATTICE.append(lattice)
    
    
    
    
    
    
    
    





plt.figure(dpi = 100)
plt.plot(TEMP, M, 'b')
plt.xlabel('Temperature(K)')
plt.ylabel('Net Magnetization')
plt.savefig('mag.jpg', dpi = 100)






plt.figure(dpi = 100)
plt.plot(TEMP, KAI, 'b')
plt.xlabel('Temperature(K)')
plt.ylabel('Magnetic Susceptibility ')
plt.savefig('chi.jpg', dpi = 100)





plt.figure(dpi = 100)
plt.plot(TEMP, En, 'b')
plt.xlabel('Temperature(T)')
plt.ylabel('Energy')
plt.savefig('energy.jpg', dpi = 100)





plt.figure(dpi = 100)
plt.plot(TEMP, CV, 'b')
plt.xlabel('Temperature(K)')
plt.ylabel('Specififc Heat(Cv)')
plt.savefig('Cv.jpg', dpi = 100)

#animation
mport matplotlib.animation as animation
fig, ax = plt.subplots()
ims = []

for i in range(len(LATTICE)):
    
    
    img = plt.imshow(LATTICE[i] ,cmap='Greys')
    ims.append([img])

ani = animation.ArtistAnimation(fig, ims,interval=100) #, blit=True,repeat_delay=1000)
    
plt.show()
ani.save('ising1.mp4')




