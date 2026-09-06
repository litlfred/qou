import sys
from mass_at_3A_proper import atom_braid_word_3A
from chi_general_word import chi_all_lambda_any
from chi_general_word import chi_all_lambda_any

word = atom_braid_word_3A(3, 4, include_inter=False)
res_orig = chi_all_lambda_any(word, 21)
res_red = chi_all_lambda_any(word, 21)

for k in res_orig:
    diff = abs(res_orig[k] - res_red.get(k, 0))
    if diff > 1e-9:
        print(f"{k}: orig={res_orig[k]} red={res_red.get(k, 0)}")
