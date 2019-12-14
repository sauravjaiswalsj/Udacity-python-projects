#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../../DataCamp'))
	print(os.getcwd())
except:
	pass

#%%
import matplotlib.pyplot as pyp

#import tkinter as tk


#%%
year=[1960,1980,2000,2020,2040,2060,2080,2100]
pop=[4,6,8,10,10.25,10.45,10.65,10.85]


#%%
print(year[-1])
print(pop[-1])
pyp.plot(year,pop)
pyp.grid()
pyp.show()


#%%
pyp.scatter(year,pop)
pyp.grid()
pyp.show()


#%%
pyp.hist(year,bins=20)
pyp.xlabel('year')
pyp.ylabel('Population')
pyp.title('World Development in 2100')
pyp.show()


#%%
pyp.xscale("log")
pyp.hist(pop,bins=20)
pyp.xlabel('Growth in [M]')
pyp.ylabel('Population')
pyp.title('World Development in 2100')
pyp.show()


#%%



