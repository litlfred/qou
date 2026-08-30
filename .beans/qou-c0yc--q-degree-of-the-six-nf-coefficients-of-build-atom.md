---
# qou-c0yc
title: q-degree of the six NF coefficients of build_atom_nf_sym, all (Z,N)
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T18:13:33Z
updated_at: 2026-08-30T18:42:08Z
---

MEASURED (PR #6308, producer computations/probes/atom_nf_q_degree_probe.py).

RING. Not Q(q, sqrt q) as the docstring said. The six coefficients are Laurent
polynomials over the DYADIC rationals, Z[1/2][q, q^+-1]: hm_sym only ever gets
c = 1 and d in {0, -h, -h/2}. Denominators reach 2^32 by A = 8, so Z[q^+-1] is
wrong too. Docstring corrected at source in the same PR.

STRUCTURE. Support exactly symmetric (lo = -hi), 540/540 components over 90
nuclei, 0 exceptions. Exponent parity + NF word length is constant per nucleus
(90/90), so each coefficient is a +-1 eigenvector of q -> 1/q with the sign
fixed by word length.

DEGREE. Quadratic in A from the A(A-1)/2 pair steps.
  all-proton  deg(sigma0) = 12A + A(A-1)/2 - 1, exact A = 1..30 (= n_calls - 1)
  pure-neutron deg(gamma) = A(A+1)/2 on 7 <= A <= 26, BREAKS at A = 27

TROPICAL. Max-plus on the effective step matrix is a genuine upper bound (0
violations / 540) but attained in only 197/540; gap always even, zero
proton-rich, 104 at A = 12 and still growing there.

COST. build_atom_nf_sym is exponential (hm_sym never canonicalises): A=1 is
0.13 s, A=2 did not finish in 15 min. sp.expand per call is value-preserving
and gets A=8 to 8.5 s; the Fraction mirror gets A=30 in seconds. So the
symbolic-q path is unnormalised, not intractable -- the corpus had the cause
right (compound_shift_nf.py) and abandoned the path on the cost.

OPEN, not derived: the neutron-rich leading-order cancellation, and the A=27
break. shift_NF = 18Z+21N+1 is a different quantity and matches nothing here.
