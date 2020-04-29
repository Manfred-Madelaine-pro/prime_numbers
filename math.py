
from matplotlib import pyplot as plt

import csv
import datetime


BORNE_SUP = 10000
GROUP = 200


def main():
	l = prime_numbers(BORNE_SUP)
	print('Primes:\n', l)
	
	map = group_by(l, GROUP)
	nb_prime_by_group = digest(map)
	plot_curve(nb_prime_by_group)
	
	# write_in_csv(res)


def prime_numbers(borne_sup):
	prime_list = []
	for n in range(2, borne_sup):
		for x in range(2, n):
			if n % x == 0:
				break
		else:
			# loop fell through without finding a factor
			prime_list.append(n)

	return prime_list


def group_by(list, group):
	map_group = {}

	i=0
	map_group[i] = []	
	for x in list:
		if x >= (i+1)*group:
			while x >= (i+1)*group:
				i+=1
			map_group[(i)*group] = []
		
		map_group[(i)*group].append(x)

	return map_group


def digest(map):
	print('\nProcess the grouped primes.')
	l = []
	count = 0
	for k, v in map.items():
		count += len(v)

		print('{} : {} (count = {})'.format(k, len(v), count))
		l.append(len(v))

	return l


def plot_curve(list):
	plt.plot(list)
	
	plt.title("count prime numbers")
	plt.ylabel("count")
	plt.xlabel("group")
	plt.show()

def write_in_csv(list):
	f_name = 'output_' + get_date_timestamp() + '.csv'
	f = open(f_name, 'w')

	with f:
		writer = csv.writer(f)
		writer.writerow(['group', 'count']) # column name
		for _, v in enumerate(list):
			writer.writerow([_, v])


def get_date_timestamp():
	dt = str(datetime.datetime.now()) # example : 2020-04-29 23:12:05.033586
	dt = dt.replace(' ', '_')
	dt = dt.replace(':', '')		# remove time token
	dt = dt.split('.')[0] 			# remove nano second
	return dt




# ----------------------------


main()