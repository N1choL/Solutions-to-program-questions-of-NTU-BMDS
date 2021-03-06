import argparse
import matplotlib.pyplot as plt
import numpy as np


def moving_avg_filter(data_arr, w):
	data_arr_cumsum = np.cumsum(data_arr)
	data_arr_cumsum[w:] = (data_arr_cumsum[w:] - data_arr_cumsum[:-w])
	data_arr_filtered = data_arr_cumsum[w-1:]/w

	return data_arr_filtered


parser = argparse.ArgumentParser(description='Plot the loss vs epoch for given data file')
parser.add_argument('--data_file', help='Data file path', dest='data_file')
parser.add_argument('--step_size', default=1, type=int, help='step size', dest='step_size')
parser.add_argument('--filter_size', default=1, type=int, help='moving average filter size', dest='filter_size')
FLAGS = parser.parse_args()

w = FLAGS.filter_size

data_arr = np.loadtxt(FLAGS.data_file, dtype='float', comments='#', delimiter='\t')

steps = np.arange(data_arr.shape[0]) + 1
train_loss = data_arr[:,1]
val_loss = data_arr[:,2]

if w>1:
	steps = steps[w-1:]
	train_loss = moving_avg_filter(train_loss,w)
	val_loss = moving_avg_filter(val_loss,w)

ind_start = 0
ind_step = FLAGS.step_size
if ind_step>1:
	ind_start = ind_step - 1

ind_end = len(steps) + 1

fig, ax = plt.subplots(figsize=(4,3))
plt.plot(steps[ind_start:ind_end:ind_step], train_loss[ind_start:ind_end:ind_step], 'r', label="train")
plt.plot(steps[ind_start:ind_end:ind_step], val_loss[ind_start:ind_end:ind_step], 'b', label="val")
plt.xlabel('epoch')
plt.ylabel('loss')
plt.grid(linestyle='--')
plt.legend()

fig.subplots_adjust(left=0.18, bottom=0.16, right=0.97, top=0.98, wspace=0.20 ,hspace=0.20 )
fig.savefig('{}.png'.format(FLAGS.data_file[:-4]),dpi=200)

plt.show()
plt.close('all')

	
