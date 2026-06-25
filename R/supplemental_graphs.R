# CGT/E Supplement Toy Graph Script
#
# PSH 6/2025

rm(list = ls())

# Graph 1: Possible Interaction Effects ##########################################
currdiff = seq(from = 0, to = 1, by = .1)
prev_easy = 0
prev_diff = 1
prev_extreme_diff = 4

rt_offset = 500
curr_diff_slope = 300
prev_diff_slope = -100
curr_x_prev_diff_intxn = -60


yval_prev_easy = rt_offset + 
  currdiff * curr_diff_slope + 
  prev_easy * prev_diff_slope + + 
  prev_easy * currdiff * curr_x_prev_diff_intxn
yval_prev_diff = rt_offset + 
  currdiff * curr_diff_slope + 
  prev_diff * prev_diff_slope + 
  prev_diff * currdiff * curr_x_prev_diff_intxn
yval_prev_extreme_diff = rt_offset + 
  currdiff * curr_diff_slope + 
  prev_extreme_diff * prev_diff_slope + 
  prev_extreme_diff * currdiff * curr_x_prev_diff_intxn

plot(currdiff, yval_prev_easy, col = 'blue', type = 'l', ylim = c(0,800), lwd = 8,
     xlab = 'Current Difficulty', ylab = 'Decision Time')
lines(currdiff, yval_prev_diff, col = 'red', lwd = 8)
lines(currdiff, yval_prev_extreme_diff, col = 'magenta', lwd = 8)
text(x = 0, y = 550, labels = 'Prev. Easy', srt = 16, col = 'blue', pos = 4)
text(x = 0, y = 445, labels = 'Prev. Diff.', srt = 12, col = 'red', pos = 4)
text(x = 0, y = 140, labels = 'Prev. Extremely Diff.', srt = 3, col = 'magenta', pos = 4)


# Graph 2: Intermediate Difficulty ##########################################
subj_val_diff = seq(from = -6, to = 6, by = .1)

softmax_inv_temp_preveasy = 1
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
polygon(x = c(-100, 100, 100, -100), y = c(.55, .55, .45, .45),col = rgb(0, 0, 0, .2))
polygon(x = c(-100, 100, 100, -100), y = c(.15, .15, 0, 0),col = rgb(0, 0, 0, .2))
polygon(x = c(-100, 100, 100, -100), y = c(.85, .85, 1, 1),col = rgb(0, 0, 0, .2))


plot(prisky_preveasy, abs(prisky_prevdiff - prisky_preveasy), type = 'l')
