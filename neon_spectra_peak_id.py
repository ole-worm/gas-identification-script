#part 1
#cleaning up raw SGM data for plotting 
import pandas as pd
import csv
import numpy
import sys
import math
pd.set_option('display.max_rows', 500) #set max rows so that they don't get truncated
#1
#open selected raw data file from SGM
fname = input('Enter the file name: ')#choose file in same directory
try:
    fnamefile= open(fname+('.csv'))
    print('cleaning up raw data')
    print('writing spectral data to: "spectra_'+fname+'.txt"')
except:
    print('Make sure the file directory is the same as this script')
    exit()
#save output to new file
spectra = 'spectra_'+fname+'.csv' #name new cleaned up file 'spectra+file name'
sys.stdout = open(spectra, "w") #create new file to write the following data
print('Wavelength,Intensity')
#create dataframe (df) using the file with just the wavelengths
df = pd.read_csv(fname+'.csv', header = [0,1], sep='\t') #only works if i separate
#print(df.iloc[46:446, 0:1].values) #rows containing the wavelengths. You can do df.iloc[2:4] or just df[2:4]. make sure you have the.values or else the indexes will be listed next to the wavelengths.
print(df.iloc[45:446, 0:1].values) #for single string, uncomment to use if needed

##clean up tuples
import fileinput
with fileinput.FileInput(spectra, inplace=True) as file:
    for line in file:
        print(line.replace(" ['", ""), end='')
with fileinput.FileInput(spectra, inplace=True) as file:
    for line in file:
        print(line.replace("']", ""), end='') #replaces brackets with parentheses and removes apostrophes
with fileinput.FileInput(spectra, inplace=True) as file:
    for line in file:
        print(line.replace("(", ""), end='')
with fileinput.FileInput(spectra, inplace=True) as file:
    for line in file:
        print(line.replace("[['", ""), end='')
with fileinput.FileInput(spectra, inplace=True) as file:
    for line in file:
        print(line.replace("]", ""), end='')
        
sys.stdout.close()

#end of code for part 1

#part 2
#run 'plot_spectra.py' to get the graph and peak positions
#plotting points from csvs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import sys
#entering file 
##fname = input('Enter the file name: ')#choose file in same directory
##try:
##    fnamefile= open('spectra_'+fname+('.csv'))
##    print('Opening spectral power distribution!')
##    print('writing peaks positions to "'+fname+'.txt"')
##except:
##    print('Make sure the file directory is the same as this script')
##    exit()

neon_data = pd.read_csv(spectra)
x = neon_data.Wavelength
z = neon_data.Intensity
y = z/max(z) #dividing by max of intensity normalizes the y axis


peaks = find_peaks(y, height = .055)
height = peaks[1]['peak_heights'] #lists only the intensities of the peaks
peak_pos = x[peaks[0]] #list of the peaks x indexes and wavelengths, not the corresponding
#peak_height = y[peaks[0]]
peak_output = peaks[0]+380 #gives arrays of wavelength indexes (wavelength-380) and wavelength values. adding 380 to each element in the array
#append output peak positions to txt file.
#print('Peaks (intensity, wavelength)\n', peak_output, height, file=open('peaks_'+fname+'.txt', 'w')) #writes 2 arrays to text file
#print(peaks, height, file=open('peaks_'+fname+'.txt', 'w',)) #writes 2 arrays to text file
#print('x =', peak_output, 'y =', height, file=open('peaks_'+fname+'.txt', 'w',)) #writes wavelengths and intensity as arrays to text file
print(fname, peak_output, file=open('peaks_'+fname+'.txt', 'w',)) #writes wavelengths to text file

##import pandas as pd
##pd.read_csv('/Users/taylorhealy/Documents/peaks_neon_sample.txt',  header=[0,1], sep='\t')


##from numpy import array, savetxt
##np.savetxt('peaks_'+fname+'.csv', zip(peak_output,height), delimiter=' ')
##data = numpy.array(peak_output, height)
##np.savetxt('peaks_'+fname+'.csv', data, delimiter=' ')

#plot data and highlight peaks in red
#adapted from https://blog.finxter.com/python-scipy-signal-find_peaks/
fig = plt.figure(fname) #adds title to plotfile
#labelling these messes up the graph, use above line to title
#plt.title(fname) 
ax = fig.subplots()
ax.set_xlabel('Wavelength(nm)') #can't add axis because it messes up the graph
ax.set_ylabel('Intensity')
ax.plot(x,y)
ax.scatter(peak_pos, height, color = 'r', s = 15, marker = 'D', label = fname)
ax.legend()
ax.grid()
plt.show()

#plt.savefig(fname+'.png', dpi=200, bbox_inches='tight')

###save text file to excel
##from openpyxl import load_workbook
##
##wb = load_workbook('neon_peaks.xlsx')
##ws = wb['neon_peaks']
##ws["A1"] = "values" #just a header
##row = 2 #represent the 2 row of the sheet
##column = 1 #represent the column "A" of the sheet
##
##for i in list1:
##    ws.cell(row=row, column=column).value = i #getting the current cell, and writing the value of the list
##    row += 1 #just setting the current to the next
##
##wb.save()

#create another script that compares the text files
