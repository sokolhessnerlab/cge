// CGT Grid Search Javascript Code
// 
// Code to implement a grid search algorithm to identify the best
// choice set to use in phase 2 of the CGT experiment
//
// written by Peter Sokol-Hessner, July 2022

// Execute in a UNIX terminal with "node cgt_gridsearch_script.js" (no
// quotes).


// Placeholders for the data assumed to be present from Phase 1.
// Used for testing effectiveness of the below script across python, R, & javascript
riskygain_values = [5, 8, 10, 12, 18, 4, 9];
riskyloss_values = [0, 0,  0,  0,  0, 0, 0];
certain_values =   [1, 5,  3,  8, 10, 2, 4];
choices =          [1, 0,  1,  1,  0, 0, 1];

console.log("Risky Gain Values: ", riskygain_values) // check definitions worked

// Function Definitions

function choice_probability(parameters, riskyGv, riskyLv, certv) {
  rho = parameters[0];
  mu = parameters[1];

  nTrials = riskyGv.length;

  div = Math.max.apply(Math,riskyGv) ** rho;

  utility_risky_option = [];
  utility_safe_option = [];
  p = [];
  for (let i = 0; i < nTrials; i++){
    utility_risky_option = 0.5 * Math.pow(riskyGv[i],rho) + 0.5 * Math.pow(riskyLv[i],rho);
    utility_safe_option = Math.pow(certv[i],rho);

    p[i] = 1/(1 + Math.exp(-mu/div*(utility_risky_option - utility_safe_option)))
  }

  return p
}

function negLLprospect_cgt(parameters, riskyGv, riskyLv, certv, choices) {
  choiceP = choice_probability(parameters, riskyGv, riskyLv, certv);

  nTrials = riskyGv.length;

  likelihood = [];
  negloglikelihood = [];
  for (let t = 0; t < nTrials; t++){
    likelihood[t] = choices[t]*choiceP[t] + (1-choices[t])*(1-choiceP[t]);
    if (likelihood[t] == 0){
      likelihood[t] = 0.000000000000001;
    }
    negloglikelihood[t] = -Math.log(likelihood[t]);
  }

  nll = negloglikelihood.reduce((partialSum, a) => partialSum + a, 0);

  return nll
}

// Checking that it works
temp_val = choice_probability([.8, 3], riskygain_values, riskyloss_values, certain_values)
console.log("choiceP:", temp_val)

temp_val = negLLprospect_cgt([.8, 3], riskygain_values, riskyloss_values, certain_values, choices)
console.log("NLL:", temp_val)

// Grid Search Code

// WILL NEED TO MAKE SURE DATA IS ONLY FROM TRIALS WHERE PARTICIPANT RESPONDED
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

for (let r = 0; r < n_rho_values; r++){
  rho_values[r] = [rmin + r*rstep]; // creates the rho values
}

for (let m = 0; m < n_mu_values; m++){
  mu_values[m] = [mmin + m*mstep]; // creates the mu values
}

best_nll_value = 1e10; // a preposterously bad first nll

for (let r = 0; r < n_rho_values; r++){
  for (let m = 0; m < n_mu_values; m++){
    nll_new = negLLprospect_cgt([rho_values[r], mu_values[m]], riskygain_values, riskyloss_values, certain_values, choices);
    if (nll_new < best_nll_value) {
      best_nll_value = nll_new;
      bestR = r + 1; // +1 corrects for diff. in javascript vs. R indexing
      bestM = m + 1; // +1 corrects for diff. in javascript vs. R indexing
    }
  }
}

// print indices of best-fitting parameter values + NLL
console.log("The best R index is",bestR,"while the best M index is",bestM,", with an NLL of",best_nll_value)

// Format the indices for good printing to filename
str_bestR = String(bestR);
if(str_bestR.length == 1){
  str_bestR = "00" + str_bestR;
} else if (str_bestR.length == 2) {
  str_bestR = "0" + str_bestR;
}

str_bestM = String(bestM);
if(str_bestM.length == 1){
  str_bestM = "00" + str_bestM;
} else if (str_bestM.length == 2) {
  str_bestM = "0" + str_bestM;
}

// The file name to use in part 2
fname = "bespoke_choiceset_rhoInd" + str_bestR + "_muInd" + str_bestM + ".csv";
console.log(fname)
