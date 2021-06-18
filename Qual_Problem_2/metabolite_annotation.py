# Script to solve Problem 2.Metabolite Annotation
# Stepik Bioinformatics Contest 2021

from decimal import Decimal
from sys import maxsize

def test_splitter(fin_lines):

	"""
	Submodule to parse the input file and split it into
	individual tests
	"""

	def partition_list(superList, num_chunk_el):

		"""
		Submodule that partitions a given list into smaller chunks of given size
		"""

		for i in range(0, len(superList), num_chunk_el):
			yield superList[i:i + num_chunk_el]

	pre_parted_list = partition_list(fin_lines[1:], 4)

	parted_list = []

	for element in list(pre_parted_list):
		parted_list.append(list(map(str.strip, element)))

	return parted_list


def annotate_metabolites(m_masses, k_masses, n_masses):

	"""
	Submodule to annotate metabolite-adduct pairs for a given signal
	# Problem statement
	n = m + k + delta, 
	where,
	n = mass of signal
	m = mass of metabolite
	k = mass of adduct
	# Constraint
	# m + k > 0
	"""

	from collections import OrderedDict

	def create_id_dict(list_el):

		"""
		Submodule to create hash tables to hold original index ids for all masses
		"""

		dict_el = OrderedDict()

		for index, value in enumerate(list_el):
			dict_el.update({index + 1 : value})

		return dict_el


	def closest_metabolite_adduct_pair(array_M, array_K, n_mass):

		"""
		Submodule that takes in sorted arrays: array_M and array_K
		and finds the pair of m and k closest to n_mass

		Returns:
			smallest_delta: tuple comprising of metabolite mass (m), adduct mass (k) and smallest delta
		"""

		# Algorithm - Sorting and walking inwards

		# Start with two pointers, one pointing at the smallest element of A, the other pointing to the largest element of B
		# Calculate the sum of the pointed two elements
		# If it is smaller than k, increment the pointer into A so that it points to the next largest element
		# If it is larger than k, decrement the pointer into B so that it poitns to the next smallest element
		# If it is exactly k, you've found a pair. Move one of the pointers and keep going to find the next pair

		import sys

		length_M = len(array_M)
		length_K = len(array_K)

		# Set initial pointers
		# Start of metabolite masses array
		pointer_M = 0
		# End of adduct masses array
		pointer_K = length_K - 1

		# Initialize delta as a very big number
		delta = sys.maxsize

		# Initialize smallest_delta tuple
		smallest_delta = (array_M[pointer_M], array_K[pointer_K], decimal.Decimal(sys.maxsize))

		while (pointer_M < length_M and pointer_K >= 0):

			m_index = pointer_M
			k_index = pointer_K
			delta = abs(array_M[pointer_M] + array_K[pointer_K] - n_mass)

			# Update smaller delta when found
			# This clause was necessary as there are negative numbers in the array (better solution might exist)
			if delta <= smallest_delta[-1]:
				# Check if the constraint on masses is satisfied
				if array_M[pointer_M] + array_K[pointer_K] > 0:
					smallest_delta = (array_M[m_index], array_K[k_index], delta)

			# Move the pointers based on intermediate sums
			if array_M[pointer_M] + array_K[pointer_K] > n_mass:
				pointer_K = pointer_K - 1
			else:
				pointer_M = pointer_M + 1

		return smallest_delta

	m_masses_ids = create_id_dict(m_masses)
	k_masses_ids = create_id_dict(k_masses)
	n_masses_ids = create_id_dict(n_masses)

	print(f'Length m_masses_ids: {len([*m_masses_ids])}')
	print(f'Length k_masses_ids: {len([*k_masses_ids])}')
	print(f'Length n_masses_ids: {len([*n_masses_ids])}')

	metabolites_by_n = OrderedDict()

	# Sort the arrays using numpy sort
	sorted_m_masses = np.sort(m_masses)
	sorted_k_masses = np.sort(k_masses)

	for n_id in n_masses_ids:

		n_mass = n_masses_ids[n_id]

		m_k_pair = closest_metabolite_adduct_pair(sorted_m_masses,
													sorted_k_masses,
													n_mass)
		
		m_id = next(key for key, value in m_masses_ids.items() if value == m_k_pair[0])
		k_id = next(key for key, value in k_masses_ids.items() if value == m_k_pair[1])

		metabolites_by_n.update({n_id : (m_id, k_id)})

	return metabolites_by_n


if __name__ == "__main__":

	from pathlib import Path
	import decimal
	import time
	import numpy as np

	# Note the start time
	start_time = time.time()

	# Specify input and output files
	fin_lines = open(Path(Path.cwd(), '5.txt'), 'r').readlines()
	fout_file = open(Path(Path.cwd(), '5_np_2.out'), 'w')

	print(f'Number of tests: {fin_lines[0]}')

	tests = test_splitter(fin_lines)
	
	for test_index, test_el in enumerate(tests):
		# Extract the header
		test_param_num = test_el[0].split()
		# Number of masses
		test_M = test_param_num[0]
		# Number of adducts
		test_K = test_param_num[1]
		# Number of series
		test_N = test_param_num[2]

		# Masses of metabolites
		array_M = np.array([decimal.Decimal(m) for m in test_el[1].split()])
		# Masses of adducts
		array_K = np.array([decimal.Decimal(k) for k in test_el[2].split()])
		# Masses of series
		array_N = np.array([decimal.Decimal(n) for n in test_el[3].split()])

		print(f'Index: {test_index}, M: {test_M}, K: {test_K}, N: {test_N}')

		metabolites_by_n = annotate_metabolites(array_M, array_K, array_N)

		for n_id in metabolites_by_n:
			
			fout_file.write(' '.join(map(str, metabolites_by_n[n_id])) + '\n')

	# Note the end time
	end_time = time.time()
	
	# Print the running time for the script
	print(f'Running time: {time.strftime("%H:%M:%S", time.gmtime(end_time - start_time))}')