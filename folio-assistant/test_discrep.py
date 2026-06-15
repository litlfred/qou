import sys
from pathlib import Path
import mpmath as mp
sys.path.insert(0, 'computations')
from mass_at_3A_proper import atom_braid_word_3A
from chi_monotone_transfer import chi_all_lambda
from reduced_block_kernel import chi_all_lambda_reduced_block
from chi_free_via_lr import chi_free_lr

mp.mp.dps = 50
Z, N = 1, 1
n = 6
word = atom_braid_word_3A(Z, N, include_inter=False)

chf = chi_all_lambda(word, n)
chf_reduced = chi_all_lambda_reduced_block(word, n)
chf_lr = chi_free_lr(Z, N)

print("chi_all_lambda len:", len(chf))
print("chi_reduced len:", len(chf_reduced))
print("chi_free_lr len:", len(chf_lr))

max_diff = max(abs(chf[l] - chf_reduced[l]) for l in chf)
print("max_diff(chi_all, chi_reduced):", max_diff)

max_diff_lr = max(abs(chf[l] - chf_lr.get(l, 0)) for l in chf)
print("max_diff(chi_all, chf_lr):", max_diff_lr)

