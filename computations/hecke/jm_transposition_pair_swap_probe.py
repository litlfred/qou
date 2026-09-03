"""The PAIR-SWAP mechanism behind Mathas 3.24(i) -- measured before it was proved.

With the expansion A_k = d . SUM_{l<k} T_(l,k) in hand, the question "does sigma_j commute
with A_k?" becomes "does sigma_j fix that sum?". For i > j+1 exactly TWO terms can be
disturbed -- l = j and l = j+1 -- since i itself is out of reach of sigma_j.

This measures whether sigma_j preserves THAT PAIR. Regular representation of H_6 (faithful),
exact fractions.Fraction, q in {2, 3}.

RESULT: the pair commutes in EVERY case; each term ALONE never does. So it is a genuine
pair phenomenon, not term-by-term commutation -- which is why a naive "sigma_j commutes with
each transposition" approach fails and the sum is essential.

Now PROVED as `sigma_comm_transp_pair` in HeckeTranspositionExpansion.lean. The proof needs
BOTH relations: the base case i = j+2 reduces via one braid move to
vuv^2 + uv = v^2uv + vu, and only the HECKE relation v^2 = hv + 1 makes both sides
h.vuv + uv + vu. Braid alone does not close it. The step i -> i+1 is pure far-commutation.

Kept as the record of the measurement that pointed at the lemma.
Emits no witness.
"""
from fractions import Fraction as F
exec(open(__file__.replace('jm_transposition_pair_swap_probe','jm_adjacent_widen_q_and_n')).read().split('print("jm words')[0])
def add(a,b):
    r=dict(a)
    for k,v in b.items():
        r[k]=r.get(k,F(0))+v
        if r[k]==0: del r[k]
    return r
def transp(i,k):
    if k==i+1: return [i]
    return [k-1]+transp(i,k-1)+[k-1]
print("sigma_j vs the PAIR T_(j,i)+T_(j+1,i), and vs each term alone")
for (n,q) in [(6,F(2)),(6,F(3))]:
    word=build(n,q); print(f"n={n} q={q}")
    for j in range(0,3):
        for i in range(j+2,n):
            L=add(word([j]+transp(j,i)), word([j]+transp(j+1,i)))
            R=add(word(transp(j,i)+[j]), word(transp(j+1,i)+[j]))
            solo = word([j]+transp(j,i))==word(transp(j,i)+[j])
            print(f"   j={j} i={i}: pair={L==R}  single={solo}")
