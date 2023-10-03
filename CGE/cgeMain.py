#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:20:06 2022

@author: hayley # Modified by Von
"""

"""
Primary script for HRB's dissertation project RCS
This script does some set up for the experiment and calls all required scripts to run the risky decision-making and cognitive control tasks
"""

    

def cgeMain(subID, isReal, computerNumber, taskSet): # define the function and specify the argument(s)

    # subID
            # Must be three digits (e.g., 001, 093, 458, etc.)
    # isReal
            # 0 - for testing
            # 1 - for real
    # computer numbers:
            # 1 - VM Laptop
            # 2 - Chicharron
            # 3 - tofu 
    #taskSet:
        # 1: do all
        # 2: do ospan and symspan only
        # 1: do symspan only
    
    # let us know things are starting...
    print('starting study for participant', subID)    

    # IMPORT MODULES
    import os
    import pandas as pd
    import sys

    # SET WORKING DIRECTORY #
    if computerNumber ==1:
        dirName = ("C:\\Users\\jvonm\\Documents\\GitHub\\cge\\CGE")
        dataDirName = ("C:\\Users\\jvonm\\Documents\\GitHub\\cge\\CGE\\data")
    elif computerNumber ==2:
        dirName = ("/Users/shlab/Documents/Github/cge/CGE/")
        dataDirName = ("/Users/shlab/Documents/Github/cge/CGE/data")
    elif computerNumber ==3:
        dirName = ("/Users/Display/Desktop/Github/cge/CGE/")
        dataDirName = ("/Users/Display/Desktop/Github/cge/CGE/data")
    
    os.chdir(dirName)

    # IMPORT TASK SCRIPTS #
    # cgeRDM
    import cgeRDMdraftET_test 
    # OSpan
    from ospan.ospanTaskModule import ospanTask
    # SymSpan
    from symspan.symSpanTaskModule import symSpanTask
    
    # SETTING TASK VARIABLES & PRESENTATION ORDER
    if taskSet ==1:
        
        # risky decision-making task (input arguments determined above) 
        cgeRDMdraftET_test 
        
        # ospan instructions + instructions quiz + practice + task
        ospanTask(subID, isReal,dirName, dataDirName)
        
        # symspan instructions + instructions quiz + practice + task
        symSpanTask(subID, isReal,dirName, dataDirName)
        
    elif taskSet==2:
        
        ospanTask(subID, isReal,dirName, dataDirName)

        symSpanTask(subID, isReal,dirName, dataDirName)
        
    elif taskSet==3:
        
        symSpanTask(subID, isReal,dirName, dataDirName)
    
    
    # simple analysis script (checks for missing trials, runs simple glm, scores span tasks, notes whether we keep the data and then adjusts the condition file)


    
    
    
    
    
    
