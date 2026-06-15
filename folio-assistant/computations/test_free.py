import sys
from mass_at_3A_proper import atom_braid_word_3A
from chi_monotone_transfer import chi_all_lambda
from reduced_block_kernel import chi_all_lambda_reduced_block

word = atom_braid_word_3A(3, 3, include_inter=False)
res_orig = chi_all_lambda(word, 18)
res_red = chi_all_lambda_reduced_block(word, 18)

for k in res_orig:
    diff = abs(res_orig[k] - res_red[k])
    if diff > 1e-9:
        print(f"{k}: orig={res_orig[k]} red={res_red[k]}")
