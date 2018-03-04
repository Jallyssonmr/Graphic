# coding=UTF-8
import os
import matplotlib.pyplot as plt

class Graph2D(object):

	def Run(self, x, y, name):
		try:
			plt.plot(x, y, ls = '', marker='o', c = '#363333', alpha = 0.5)
			plt.xlabel('x', fontsize = 12)
			plt.ylabel('y', fontsize = 12)
			plt.savefig('Output/' + name + '.eps')
			plt.savefig('Output/' + name + '.png')
			plt.close('all')
			if not os.path.exists('Output/'):
				os.makedirs('Output/')
		except IOError as (errno, strerror):
			print 'I/O error({0}): {1}'.format(errno, strerror)