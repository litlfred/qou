---
# qou-nxvg
title: 'GAP: derive the Coulomb and asymmetry q-integer assignments lambda_C = (q - 1/q)[6]_q m_e and a_asym = 3[2]_q[7]_q m_e'
status: in-progress
pr: 8185
type: task
priority: normal
tags:
    - 8f-decide
    - no-fitting
created_at: 2026-10-11T06:45:00Z
updated_at: 2026-10-11T07:30:00Z
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

## 2026-10-11 — owner pick 3 (leave both, record); derivation check via the channel product

Owner kept both normalisations recorded. Checked whether `prop:eigenvalue-product-expansion`
(sorry-free) fixes one. It gives ln|Lambda_sym| = l (n_pp - n_nn) + l2 n_pn with n_pn = ZN =
A^2/4 - T^2, T = (Z-N)/2 (re-verified with sympy). This scales as A^2, so it is not an energy
until it is normalised, and no block in the corpus maps ln|Lambda_sym| to a binding energy
(its only consumer is its own proof block). IF it is divided by A (a choice, not derived):
ln|Lambda_sym|/A = l2 A/4 - l2 (N-Z)^2/(4A) + l T (A-1)/A.
That has exactly the seven-term shape (N-Z)^2/(4A), but with asymmetry/volume ratio
l2 / (l2/4) = 4, against the stated a_asym/lambda_V = 3/2, and it carries a term l T odd in
Z - N that the seven-term formula lacks. So: shape suggested under an unjustified normalisation,
coefficient not reproduced. Still open.


---

# 2026-10-11 — Does the channel product map to a binding energy? (owner option 1)

Short answer: **no route in the corpus, and the obvious one is already
excluded.** Recorded as a scope-(a) negative for this construction alone.

1. **The corpus's step-7 functional is not ln|Lambda_sym|.** The map
   trace -> MeV is `S = -alpha * sum_{bonds} log mu_e`, summed over the
   chain's `A-1` interfaces (`binding_functional_extensivity_prune_probe.py`,
   bean `qou-y0mc`). `Lambda_sym` is a product over **all** pairs:
   `ln|Lambda| = l(n_pp - n_nn) + l2*n_pn` with `n_pn = ZN`, which is
   complete-graph coordination.
2. **Taken unnormalised it is the excluded complete-graph law.**
   `QOU.Mass.CoordinationSaturation.complete_graph_no_saturation`
   (sorry-free): `B/A ~ eps*(A-1)/2`, unbounded.
3. **Dividing by A is not forced anywhere.** It is a Kac/mean-field
   rescaling (pair strength ~ 1/A). The corpus already labels the
   `(N-Z)^2/A` power as needing "a well-mixed assignment, which is a
   mean-field model and is labelled as one", with the canonical segregated
   layout giving no symmetry term at all
   (`docs/audits/2026-09-05-binding-law-arc-synthesis.md` section 6a).
4. **Even granting /A, the ratio is fixed by counting and matches neither
   formula.** `ln|Lambda|/A = (l2/4)[A - (N-Z)^2/A] + l*T(A-1)/A`, so
   volume : asymmetry = 1 : 1 per `(N-Z)^2/A`, for every q. The corpus
   coefficients give 3/2 (beta-stability normalisation, `(N-Z)^2/A`) and
   3/8 (seven-term, `(N-Z)^2/(4A)`). The q-dependence also differs:
   `ln([2]_q/2)` against `[2]_q[7]_q`. So the channel product does not
   settle the normalisation conflict.
5. **The one derived 1/A route in the corpus is the Wigner term**,
   `-Delta_W T(T+1)/A` from the (2,2) self-conjugate shadow price
   (`unified-iterative-correction-proof.md`); `qou-a5jk`/`qou-w06d` cap it
   at k = 4 and leave open whether (2,2) alone reproduces it. Note
   `T(T+1)/A ~ (N-Z)^2/(4A)` is the seven-term normalisation's shape. Not
   assessed further here.

Stays todo: lambda_C and a_asym remain stated, not derived.


---

# 2026-10-11 (later) — The Wigner lead does not derive a_asym (owner option 1)

The corpus carries **three inequivalent Wigner coefficients**, at proton q0
(mp.dps 30):

    prop:wigner-np-pairing        Delta_(2,2) = m_e [3]_q [2]_q^2     6.2893 MeV
    prop:wigner-coefficient-deriv [5]_q! m_e                          67.1008 MeV
    prop:wigner-2-coefficient     C_(2,2) = w h/2, w = dim_q^2/[4]_q! 0.017357 (dimensionless)

with `dim_q(2,2) = 2.04371`, `w_(2,2) = 0.166049`. Against
`a_asym = 3[2]_q[7]_q m_e = 23.5066` and `a_asym/4 = 5.8767`, **none
matches**, and the q-forms differ (`[3][2]^2`, `[5]!`, versus `[2][7]`).
Closeness of 6.29 to 5.88 is not evidence (no-fitting rule).

Shape: `T(T+1)/A = (N-Z)^2/(4A) + |N-Z|/(2A)`, so a Wigner term contains the
seven-term asymmetry shape plus a linear cusp. But the seven-term formula keeps
asymmetry (term 4) and Wigner (term 9) as separate terms, so identifying them
would double-count. The lead does not settle the normalisation conflict.

Side finding, not acted on: the `[5]_q!` block puts the Wigner scale at level
k = 5, where (qou-a5jk / qou-w06d, sorry-free) no self-conjugate shape has
l <= 2, so under convention D a level-5 self-conjugate shadow price is zero.
Its proof asserts the k = 5 scale and cites agreement with a fitted 68.9 MeV.

## Progress Update (Round 55 — PR #8185)
- [x] Formalized non-vacuous Lean 4 theorems (`0` `sorry`, `0` vacuity advisories across all 6 static audits) in `folio/quantum-observable-universe/lean/QOU/Eightfold/ColourConjugationGMODeviationAndAsymmetry.lean` and wired into `QOU.lean`.
- [x] Added 50-dps `mpmath` probe `computations/probes/colour_conjugation_gmo_deviation_and_asymmetry_probe.py` and 2-commit stamped witness `computations/probes/colour-conjugation-gmo-deviation-and-asymmetry.witness.json` (`scriptCommitSha: dc490df3193b70802e4608a98cc9402380f4dbcd`, `HEAD: ea791bb906663eb37105b3486abd6e07818699ed`).
- [x] Opened `litlfred/qou#8185` (status kept at `in-progress` per no-unilateral-closure policy).
