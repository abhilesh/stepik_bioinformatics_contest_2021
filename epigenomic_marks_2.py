# Script to solve Problem 1.Epigenomic Marks 2
# Stepik Bioinformatics Contest 2021

def test_splitter(fin_lines):

	"""
	Submodule to find all instances of test headers in the input file
	"""

	import re
	from itertools import chain

	def partition_list(superList, indexList):

		"""
		Submodule that partitions a given list based on indices specified in another list
		"""

		pairs = zip(chain([0], indexList), chain(indexList, [None]))

		return list(superList[i:j] for i, j in pairs)

	# Regular expression for the header lines 
	# (number of sequences <space> length of sequences)
	r = re.compile(r'\d+\s\d+')

	# Get a list of all headers
	headers = list(filter(r.match, fin_lines))
	# Container to hold indices for splitting the input file into individual tests
	split_indices = []
	# Get split indices for all headers
	for header_el in headers:
		for i, j in enumerate(fin_lines):
			if j == header_el:
				if i not in split_indices:
					split_indices.append(i)
	# Sort the split indices
	split_indices.sort()

	# Split the input list into individual tests
	pre_parted_list = partition_list(fin_lines, split_indices)
	# Container to hold the processed individual tests
	parted_list = []
	# Strip unnecessary elements from the sublist
	for element in pre_parted_list[1:]:
		parted_list.append(map(str.strip, element[1:]))

	return parted_list


if __name__ == "__main__":
	
	import sys
	import re
	import pandas as pd
	import numpy as np
	from pathlib import Path

	# Specify input and output files
	fin_lines = open(Path(Path.cwd(), '2.txt'), 'r').readlines()
	fout_file = open(Path(Path.cwd(), '2.out'), 'w')

	print(f'Number of tests: {fin_lines[0]}')

	# Split the input file into individual tests
	tests = test_splitter(fin_lines)
	# Container to hold individual tests converted to dataframes
	test_df_list = []

	# Convert each test element to Pandas DataFrame
	for test_el in tests:
		test_el_df_rows = [list(test_el_seq) for test_el_seq in test_el]
		test_df_list.append(pd.DataFrame(test_el_df_rows))
	
	# Get number of unique states through the alignment
	for test_df in test_df_list:
		# Container to hold all the test_states
		test_states_list = []
		for df_column in test_df:
			test_states_list.append(''.join(test_df[df_column].values))

		test_unique_states = list(dict.fromkeys(test_states_list))
		# Write the first line of output for each test
		fout_file.write(str(len(test_unique_states)) + '\n')
		# Container to assign unique id to each state based on order of appearance
		state_index_dict = {}
		# Container to hold state ids for each position in the sequence
		location_state_list = []		
		
		# Assign unique ids to each state
		for i, s in enumerate(test_unique_states):
			state_index_dict.update({s : i + 1})
		# Map the states to unique ids
		for test_state in test_states_list:
			location_state_list.append(state_index_dict[test_state])

		# Write the second line of output for each test
		fout_file.write(' '.join(map(str, location_state_list)) + '\n')		
