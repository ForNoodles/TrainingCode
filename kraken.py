# -*- coding: utf-8 -*-
"""
Kraken, a simple data-pulling script to be used on WEPP-PEP output files
Last edit: 04/12/2020

author: Lilian Hart
"""
import numpy as np
import pandas as pd

#Define a new function called 'winnow'
def winnow():
    #Query the directory  name
    dir1 = input('Enter your working directory name (no quotations): ')
    #Query the Unburnt simulation folder
    unburnt = dir1+'\\'+input('Enter the name of your UNBURNT simulation folder: ')
    #Query the Burnt simulation folder
    burnt = dir1+'\\'+input('Enter the name of your BURNT simulation folder: ')
    #Query the name for the final CSV output file
    outname = input('Enter a name for this pair of simulations: ')

    #SECTION 1: Climate and Avg. Ann. Delivery From Channel Outlet
    
    #Read in the files as text files, because columns don't match up here
    un_loss = (unburnt+r'\wepp\output\loss_pw0.txt')
    abre1 = open(un_loss)
    b_loss = (burnt+r'\wepp\output\loss_pw0.txt')
    abre2 = open(b_loss)
    #Read the number of lines
    un_lines = abre1.readlines()
    b_lines = abre2.readlines()
    #Get the number marking the end of the document
    #because the length is variable, and we just want the end summary
    #This value will be the length minus 2
    endline1 = (len(un_lines)-2)
    endline2 = (len(b_lines)-2)

    #The data begins 49 lines earlier
    beginline1 = (endline1-49)
    beginline2 = (endline2-49)
    #The end of Section 1
    deliveryline1 = (beginline1+20)
    deliveryline2 = (beginline2+20)

    #Create an empty list to hold numeric values from the text file
    holdList1 = []
    holdList2 = []

    #For loop that goes over every line from the section of interest
    #and checks each line for numeric values
    for line in un_lines[beginline1:deliveryline1]:
        #Create an empty string to hold digits
        val = str()
        for i in line:
            #If there is a numeric value
            if i.isdigit() == True or i == '.':
                #Add the string digit to val 
                val = (val+str(i))
            else:
            #Otherwise, if there are digits in val, send to the list
                if len(val) > 0:    
                    holdList1.append(val)
                #If there are no digits, do not send to list
                else:
                    pass
                #And reset val to be empty
                val = str()
                        
    #Remove the empty periods from the holdList
    holdList1 = [float(y) for y in holdList1 if y != '.']
    #Create a better list, without the digits from the units or empty sections like irrigation
    shortList1 = holdList1[0:6]
    shortList1.append(holdList1[9]) 
    shortList1.extend(holdList1[11:16])

    #Now repeating, for the burnt data
    for line in b_lines[beginline2:deliveryline2]:
        #Create an empty string to hold digits
        val = str()
        for i in line:
            #If there is a numeric value
            if i.isdigit() == True or i == '.':
                #Add the string digit to val 
                val = (val+str(i))
            else:
                #Otherwise, if there are digits in val, send to the list
                if len(val) > 0:    
                    holdList2.append(val)
                #If there are no digits, do not send to list
                else:
                    pass
                #And reset val to be empty
                val = str()
    holdList2 = [float(y) for y in holdList2 if y != '.']   
    shortList2 = holdList2[0:6]
    shortList2.append(holdList2[9]) 
    shortList2.extend(holdList2[11:16]) 

    #Rename the lists for later use
    sec1_unburnt = pd.Series(shortList1)
    sec1_burnt = pd.Series(shortList2)

    #Delete the variables no longer needed
    del holdList1, holdList2, val, shortList1, shortList2 

    #SECTION 2: Sediment Particle Info Leaving Channel
    #Create a reference integer to the beginning of this section 2
    classline1_start = (deliveryline1 + 8)
    classline2_start = (deliveryline2+8)
    i = classline1_start
    i2 = classline2_start
    #Create a columns list to use when importing data from the text file
    columns= list(range(0,8))
    #Read in the text file, skipping to the section and reading only the rows in this section
    sec2_unburnt = pd.read_table(un_loss,header=None, names=columns, skiprows=(i), nrows=5, delim_whitespace=True, comment='-', usecols=[7])
    sec2_burnt = pd.read_table(b_loss,header=None, names=columns, skiprows=(i2), nrows=5, delim_whitespace=True, comment='-', usecols=[7])

    #SECTION 3: Primary Particles and Specific Surface

    #Set up integer variables to reference the lines in this section
    particleline1 = (endline1-7)
    particleline2 = (endline2-7)

    #For loop that extracts numbers from Section 3 of unburnt
    holdList1 = []
    holdList2 = []

    for line in un_lines[particleline1:(endline1+1)]:
    #Create an empty string to hold digits
        val = str()
        for i in line:
            #If there is a numeric value
            if i.isdigit() == True or i == '.':
                #Add the string digit to val 
                val = (val+str(i))
            else:
                #Otherwise, if there are digits in val, send to the list
                if len(val) > 0:    
                    holdList1.append(val)
                    #If there are no digits, do not send to list
                else:
                    pass
            #And reset val to be empty
                val = str()
    shortList1 = holdList1[0:5]
    shortList1.append(holdList1[6])
    shortList1 = holdList1[0:5]
    shortList1.append(holdList1[6])

    #For Loop extracting the same from Section 3 of burnt data
    for line in b_lines[particleline2:(endline2+1)]:
        #Create an empty string to hold digits
        val = str()
        for i in line:
            #If there is a numeric value
            if i.isdigit() == True or i == '.':
                #Add the string digit to val 
                val = (val+str(i))
            else:
                #Otherwise, if there are digits in val, send to the list
                if len(val) > 0:    
                    holdList2.append(val)
                    #If there are no digits, do not send to list
                else:
                    pass
            #And reset val to be empty
                val = str()
            
    #Remove the '2' value collected from the m^2 unit in the text file
    shortList2 = holdList2[0:5]
    shortList2.append(holdList2[6])
    shortList2 = holdList2[0:5]
    shortList2.append(holdList2[6])

    sec3_unburnt = pd.Series(shortList1)
    sec3_burnt = pd.Series(shortList2)

    #Delete the variables no longer needed
    del holdList1, holdList2, val, shortList1, shortList2, beginline1, beginline2
    del classline1_start, classline2_start, deliveryline1, deliveryline2, endline1, endline2
    del particleline1, particleline2, un_lines
    #Close the open text files
    abre1.close()
    abre2.close() 

    #Consolidate all unburnt data into a single columned dataframe
    index = ['storms','rainfall','events','runoff','total_contrib','precip','water_disch_outlet','hill_soil_loss','channel_soil_loss','sed_disch_outlet','deliv_wshed','sed_ratio','Class1','Class2','Class3','Class4','Class5','PP_clay','PP_silt','PP_sand','PP_OM','ISS','enrichment']
    sec2_unburnt = sec2_unburnt.rename(columns={7:0})
    frames1 = [sec1_unburnt,sec2_unburnt,sec3_unburnt]
    result_unburnt = pd.concat(frames1)
    result_unburnt = result_unburnt.rename(columns={0:'Unburnt'})
    result_unburnt.index = index

    #Consolidate all burnt data the same way
    sec2_burnt = sec2_burnt.rename(columns={7:0})
    frames2 = [sec1_burnt,sec2_burnt,sec3_burnt]
    result_burnt = pd.concat(frames2)
    result_burnt = result_burnt.rename(columns={0:'Burnt'})
    result_burnt.index = index

    #Create a DataFrame to hold the extracted data
    moreinfo = ['integer','avg.ann. in mm','integer','in mm','area in ha','avg.ann. in m^3/yr','avg.ann. in m^3/yr','avg.ann. in tonnes/yr','avg.ann in tonnes/yr','avg.ann. in tonnes/yr','in T/ha/yr','ratio','fraction clay','fraction silt', 'fraction small agg.', 'fraction large agg.', 'fraction sand','fraction','fraction','fraction','fraction','in m^2/g of total sediment','ratio']
    columns = ['Unburnt','Burnt']
    bowels = pd.DataFrame(index = index)
    bowels['more info'] = moreinfo
    bowels['Unburnt'] = result_unburnt
    bowels['Unburnt'] = bowels.Unburnt.astype(float)
    bowels['Burnt'] = result_burnt
    bowels['Burnt'] = bowels.Burnt.astype(float)

    #Create a final column to record the change, handling ZeroDivisionError
    bowels['%change'] = bowels['Burnt']-bowels['Unburnt']
    try:
        bowels['%change'] = bowels['%change'].div(bowels['Unburnt'])   
    except ZeroDivisionError:
        bowels['% change'] = bowels['%change'].div(1)
    finally:
        bowels['%change'] = bowels['%change']*100
   
    bowels.to_csv(dir1+'\\'+ outname +'.csv')
   
   