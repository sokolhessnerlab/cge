#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 21:29:05 2022
@title: CGT Grid Search Python Code

@description: Code to implement a grid search algorithm to identify the best 
choice set to use in phase 2 of the CGT Experiment.

@author: sokolhessner
"""

# Placeholders for the data assumed to be present from Phase 1
# Used for testing effectiveness of the below script across python & R
riskygain_values = list((5, 8, 10, 12, 18, 4, 9));
riskyloss_values = list((0, 0,  0,  0,  0, 0, 0));
certain_values =   list((1, 5,  3,  8, 10, 2, 4));
choices =          list((1, 1,  1,  1,  0, 0, 1));

import math

### Function Definitions

def choice_probability(parameters, riskyGv, riskyLv, certv):
    # Pull out parameters
    rho = parameters[0];
    mu = parameters[1];
    
    nTrials = len(riskyGv);
    
    # Calculate utility of the two options
    utility_riskygain_value = [math.pow(value, rho) for value in riskyGv];
    utility_riskyloss_value = [math.pow(value, rho) for value in riskyLv];
    utility_risky_option = [.5 * utility_riskygain_value[t] + .5 * utility_riskyloss_value[t] for t in range(nTrials)];
    utility_safe_option = [math.pow(value, rho) for value in certv]
    
    # Normalize values with div
    div = max(riskyGv)**rho;
    
    # Softmax
    p = [1/(1 + math.exp(-mu/div*(utility_risky_option[t] - utility_safe_option[t]))) for t in range(nTrials)];
    return p

def negLLprospect_cgt(parameters, riskyGv, riskyLv, certv, choices):
    choiceP = choice_probability(parameters, riskyGv, riskyLv, certv);
    
    nTrials = len(choiceP);
    
    likelihood = [choices[t]*choiceP[t] + (1-choices[t])*(1-choiceP[t]) for t in range(nTrials)];
    zeroindex = [likelihood[t] == 0 for t in range(nTrials)];
    for ind in range(nTrials):
        if zeroindex[ind]:
            likelihood[ind] = 0.000000000000001;
    
    loglikelihood = [math.log(likelihood[t]) for t in range(nTrials)];
    
    nll = -sum(loglikelihood);
    return nll


### Grid Search Code

# Prepare rho & mu values
n_rho_values = 200;
n_mu_values = 201;

rmin = 0.3
rmax = 2.2
rstep = (rmax - rmin)/(n_rho_values-1)

mmin = 7
mmax = 80
mstep = (mmax - mmin)/(n_mu_values-1)

rho_values = [];
mu_values = [];

for r in range(n_rho_values):
    rho_values += [rmin + r*rstep];

for m in range(n_mu_values):
    mu_values += [mmin + m*mstep];

# Execute the grid search
best_nll_value = 1e10; # a preposterously bad first NLL

for r in range(n_rho_values):
    for m in range(n_mu_values):
        nll_new = negLLprospect_cgt([rho_values[r], mu_values[m]], riskygain_values, riskyloss_values, certain_values, choices);
        if nll_new < best_nll_value:
            best_nll_value = nll_new;
            bestR = r + 1; # "+1" corrects for diff. in python vs. R indexing
            bestM = m + 1; # "+1" corrects for diff. in python vs. R indexing

print('The best R index is', bestR, 'while the best M index is', bestM, ', with an NLL of', best_nll_value);

fname = "bespoke_choiceset_rhoInd%03i_muInd%03i.csv" % (bestR, bestM)

