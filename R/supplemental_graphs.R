# CGT/E Supplement Toy Graph Script
#
# PSH 6/2025

rm(list = ls())

# Graph 1: Possible Interaction Effects ##########################################
currdiff = seq(from = 0, to = 1, by = .1)
prev_easy = 0
prev_diff = 1
prev_very_diff = 2.5
prev_extreme_diff = 4

rt_offset = 400
curr_diff_slope = 400
prev_diff_slope = -100
curr_x_prev_diff_intxn = -80


yval_prev_easy = rt_offset + 
  currdiff * curr_diff_slope + 
  prev_easy * prev_diff_slope 
yval_prev_diff = rt_offset + 
  currdiff * curr_diff_slope + 
  prev_diff * prev_diff_slope
yval_prev_very_diff = rt_offset + 60 + 
  currdiff * curr_diff_slope + 
  prev_very_diff * prev_diff_slope + 
  prev_very_diff * currdiff * curr_x_prev_diff_intxn
yval_prev_extreme_diff = rt_offset + 100 + 
  currdiff * curr_diff_slope + 
  prev_extreme_diff * prev_diff_slope + 
  prev_extreme_diff * currdiff * -90

plot(currdiff, yval_prev_easy, col = 'blue', type = 'l', ylim = c(0,800), lwd = 8,
     xlab = 'Current Difficulty', ylab = 'Decision Time')
lines(currdiff, yval_prev_diff, col = 'red', lwd = 8)
lines(currdiff, yval_prev_very_diff, col = 'red3', lwd = 8, lty = 'dotted')
lines(currdiff, yval_prev_extreme_diff, col = 'red4', lwd = 8, lty = 'dotted')
text(x = 0, y = 455, labels = 'Prev. Easy', srt = 20, col = 'blue', pos = 4)
text(x = 0, y = 350, labels = 'Prev. Diff.', srt = 20, col = 'red', pos = 4)
text(x = 0, y = 255, labels = 'Prev. Very Diff.', srt = 10, col = 'red3', pos = 4)
text(x = 0, y = 140, labels = 'Prev. Extremely Diff.', srt = 2, col = 'red4', pos = 4)


# Graph 2: Intermediate Difficulty ##########################################
subj_val_diff = seq(from = -6, to = 6, by = .1)

softmax_inv_temp_preveasy = .8
softmax_inv_temp_prevdiff = .5

softmax <- function(xvals,mu){
  yvals = 1/(1 + exp(-mu * xvals))
  return(yvals)
}

prisky_preveasy = softmax(xvals = subj_val_diff, mu = softmax_inv_temp_preveasy)
prisky_prevdiff = softmax(xvals = subj_val_diff, mu = softmax_inv_temp_prevdiff)

plot(subj_val_diff, prisky_preveasy, col = 'blue', type = 'l', lwd = 6, 
     xlab = 'Subjective Value Difference (risky - safe)',
     ylab = 'p(choose risky)')
lines(subj_val_diff, prisky_prevdiff, col = 'red', lwd = 6)

# Boxes defined in probability space
# polygon(x = c(-100, 100, 100, -100), y = c(.55, .55, .45, .45),col = rgb(0, 0, 0, .2))
# polygon(x = c(-100, 100, 100, -100), y = c(.15, .15, 0, 0),col = rgb(0, 0, 0, .2))
# polygon(x = c(-100, 100, 100, -100), y = c(.85, .85, 1, 1),col = rgb(0, 0, 0, .2))


# Boxes defined in value-difference space
easy_rej_bound = .15
easy_acc_bound = .85
diff_bounds = c(.45, .55)

xvals_easyrej = log((1/easy_rej_bound-1))/-softmax_inv_temp_preveasy
xvals_easyacc = log((1/easy_acc_bound-1))/-softmax_inv_temp_preveasy
xvals_diff = log((1/diff_bounds-1))/-softmax_inv_temp_preveasy

polygon(x = c(-6, -6, xvals_easyrej, xvals_easyrej), y = c(0, 1, 1, 0),col = rgb(0, 0, 0, .1), border = F)
polygon(x = c(6, 6, xvals_easyacc, xvals_easyacc), y = c(0, 1, 1, 0),col = rgb(0, 0, 0, .1), border = F)
polygon(x = c(xvals_diff[1], xvals_diff[1], xvals_diff[2], xvals_diff[2]), y = c(0, 1, 1, 0),col = rgb(0, 0, 0, .1), border = F)

int_rej_bounds = c(.25, .35)
int_acc_bounds = c(.65, .75)

xvals_intrej = log((1/int_rej_bounds-1))/-softmax_inv_temp_preveasy
xvals_intacc = log((1/int_acc_bounds-1))/-softmax_inv_temp_preveasy

polygon(x = c(xvals_intrej[1], xvals_intrej[1], xvals_intrej[2], xvals_intrej[2]), y = c(0, 1, 1, 0),col = rgb(0, 0, 0, .2))
polygon(x = c(xvals_intacc[1], xvals_intacc[1], xvals_intacc[2], xvals_intacc[2]), y = c(0, 1, 1, 0),col = rgb(0, 0, 0, .2))



# plot(prisky_preveasy, abs(prisky_prevdiff - prisky_preveasy), type = 'l')
