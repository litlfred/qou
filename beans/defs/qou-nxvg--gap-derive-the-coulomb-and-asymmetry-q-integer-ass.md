---
# qou-nxvg
title: 'GAP: derive the Coulomb and asymmetry q-integer assignments lambda_C = (q - 1/q)[6]_q m_e and a_asym = 3[2]_q[7]_q m_e'
status: todo
type: task
priority: normal
tags:
    - 8f-decide
    - no-fitting
created_at: 2026-10-11T06:45:00Z
updated_at: 2026-10-11T06:45:00Z
parent: qou-8lxd
---

Successor of `qou-opjb` (closed 2026-10-11 on owner pick 1: its two defects, the
p*(A) / n_pred(p) display and the SEMF-fitted c = 0.01497, are fixed). What
remains is the derivation of the two coefficients that now fix
c = lambda_C / (2 a_asym) ~= 0.0145158337 in `prop:neutron-prediction-comparison`
and `prop:beta-stability`.

The assignments are stated in `conj:q-integer-mass-formula` (Ch 11 §8) and in
`mass-formula-regime-switching-table1-data`; the Lean (`QOU/Interactions/QIntegerMassFormula.lean`)
only defines them (`def lambda_C`, `def a_asym`) and proves `a_asym = (3/2) lambda_V`
by `ring`. `qou-orjl` (completed) showed neither is a q-hook product.

## Corpus search, 2026-10-11 (what exists)

1. `computations/DERIVATION-STATUS.md` rows 3-4 label Coulomb `[2,1] pp excess`
   and Asymmetry `[2,1] h^1 Casimir` as **DERIVED**. No artifact in docs/, folio/,
   computations/ or beans/ carries a derivation under either label: the string
   "h¹ Casimir" occurs only in that table row. The label disagrees with the block
   (which calls the assignments stated) and with `qou-orjl`.
2. `prop:eigenvalue-product-expansion` (Lean `QOU.BraidKnot.eigenvalue_product_expansion`, no `sorry` in the file) gives the
   only derived isospin-quadratic term in the corpus:
   ln|Lambda_sym| = l2 A^2/4 + l T A - l T - l2 T^2, with l = ln q, l2 = ln([2]_q/2),
   T = |Z-N|/2. Its T^2 term is -l2 (Z-N)^2/4: no 1/A, and l2 = 0.0054336 at the
   proton q0. It is not of the SEMF asymmetry form a_A (N-Z)^2/A and does not
   produce 3[2]_q[7]_q.
3. The same proof derives a [c+1]_q factor (the middle Markov-trace term
   sum_{j=0}^{c} q^{c-2j}/2 = [c+1]_q/2) and identifies [7]_q for the Borromean
   braid (c = 6). That supports the [7]_q in lambda_V and a_asym, if accepted. It
   does not explain the prefactor 3 (vs 2 in lambda_V), and the same mechanism
   would give [7]_q, not [6]_q, for a Coulomb term on the same 6-crossing braid.

Values at the proton q0 (mp.dps 30): [2] = 2.0108969, [6] = 6.3880866,
[7] = 7.6253420; lambda_C = 0.68244 MeV, a_asym = 23.50663 MeV, lambda_V = 15.67109 MeV.

## Open

- A derivation of the prefactor 3 in a_asym, and of [6]_q (rather than [7]_q) with
  the factor (q - 1/q) in lambda_C, from the corpus's own constructions.
- Whether `DERIVATION-STATUS.md` rows 3-4 should say "stated" instead of "DERIVED"
  (owner decision; not edited).

## 2026-10-11 — derivation attempt (owner: "can we derive?") and a normalisation conflict

No derivation of the prefactor 3 or of (q - 1/q)[6]_q was found beyond the search above.
`DERIVATION-STATUS.md` rows 3-4 now say STATED (owner pick 1).

Found while trying: the corpus uses TWO normalisations of the asymmetry term with the same
a_asym = 3[2]_q[7]_q m_e.
- Seven-term formula: `binding_energy_bw` in `QOU/Interactions/QIntegerMassFormula.lean`
  (line 108), `bw_chirality_isotopes.py` (line 108), `unified_low_isotope_predictor.py`
  (line 242) and DERIVATION-STATUS row 4 all use - a_asym (N-Z)^2/(4A).
- `prop:beta-stability` and the blocks reconciled to it on 2026-10-11 use a_A (A-2p)^2/A
  = a_A (N-Z)^2/A, which gives c = lambda_C/(2 a_asym) = 0.0145158.
Minimising lambda_C Z^2/A^{1/3} + a_asym (A-2Z)^2/(4A) instead gives Z* = A/(2 + c' A^{2/3})
with c' = lambda_C/a_asym = 0.0290317, i.e. twice c. Diagnostic only (accuracy does not decide
this): Z* at A = 56, 120, 208, 238 is 25.3, 51.0, 82.9, 93.1 with c and 23.1, 44.3, 68.9, 76.4
with c', against 26, 50, 82, 92. Owner decision on which normalisation is canonical.
