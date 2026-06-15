import sys
from mass_at_3A_proper import atom_braid_word_3A
from chi_monotone_transfer import chi_all_lambda
from chi_free_via_lr import chi_free_lr

Z, N = 3, 4
n = 21
chf_lr = chi_free_lr(Z, N)
chf = chi_all_lambda(atom_braid_word_3A(Z, N, include_inter=False), n)

diff = max(abs(chf[l] - chf_lr.get(l, 0)) for l in chf)
print(f"Max diff: {diff}")
