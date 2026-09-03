---
# qou-pdg9
title: 'DERIVE c1(A): the hbar_q^1 coefficient of tr_M(W_free) - tr_M(W_atom), exactly, from the Laurent trace'
status: in-progress
type: task
priority: high
created_at: 2026-09-03T08:32:06Z
updated_at: 2026-09-03T08:57:43Z
---

Successor to qou-zrx2. c0(A) = 2^-A - 2^(1-2A) is DERIVED (Schur-Weyl + cycle count, ClassicalTraceFloor.lean). c1 = lim (Dtr - c0)/hbar_q is currently six MEASURED dyadic rationals (pp 19/8, pn 37/16, nn 9/4, T 163/64, 3He 85/32, 4He 259/128), entered into PairwiseChainLeadingOrder.lean as defs. Goal: (1) obtain them EXACTLY via laurent_q_trace.tr_M_atomic_lq (formal (z,h)-polynomial with LaurentQ coefficients) expanded at q = e^eta to first order -- no Richardson; (2) find and prove the closed form in A, by the same route as c0 (first-order term of a permutation-character sum). Branch claude/logz-hbarq-rung-operator-class-2026-09-03 (branch name predates the corpus-grep that found qou-ap3d/qou-ssz6 had already closed the log Z rung question).


## 2026-09-03 — DERIVED, both ways, and the six defs are now conditional theorems

Probe: `computations/probes/c1_leading_coefficient_derived_probe.py`.
Lean: `QOU/MassTheory/LeadingOrderTraceCoefficient.lean` (lean-direct exit 0; axioms
`[propext, Classical.choice, Quot.sound]` on every declaration, no `sorryAx`).

### Part A — exact, no extrapolation

The validated exact-`Fraction` seminormal pipeline (`exact_rational_chi_gauge_probe`,
11/11 vs the cached deuteron characters) is duck-typed on `+ − × ÷ **`; run over
truncated power series in `ε = q − 1` with valuation tracking (the `h/(1−q^{−2ρ})`
entries are 0/0 at ε = 0), it returns `Δtr(1+ε)` as exact rationals order by order.

    case   a0 (=c0 derived)   c1 exact   recorded   c2 exact
    pp     1/8               19/8       19/8       357/32
    pn     1/8               37/16      37/16      403/32
    nn     1/8               9/4        9/4        217/16
    T      3/32              163/64     163/64     3285/128
    3He    3/32              85/32      85/32      3451/128
    4He    7/128             259/128    259/128    (P=3, not computed)

`a0` reproduces the DERIVED floor by a completely different computation than the
cycle count (an independent check of `ClassicalTraceFloor`). `c1` equals the six
Richardson-measured rationals EXACTLY. `c2` is new and exact — recorded, not
claimed closed-form.

### Part B — derived: a permutation count, like c0

Expanding the quantum trace `Tr(K ρ(word))/(1+q²)^n` at `q = 1+ε`:
(1) the Hecke relation forces `σ = s + ε(1 + Y)` with `sY = −Ys`
(`hecke_first_order_anticommutes`, `hecke_relation_snd` in the dual numbers);
(2) `Tr(Y·P) = 0` for every permutation `P` by the spin-flip symmetry (NOT
formalised — needs Schur–Weyl); (3) the `K′` term `n·2^c` cancels the
normaliser's `−n·2^c`; (4) each letter's own first-order term is the scalar
`1 + d′(0) ∈ {+1, −1, 0, 0}` for σ/σ⁻¹/averaged/colour-weighted — δ = O(ε³) is
invisible at this order (measured: weighted vs blind agree to ε³, differ at ε⁴).

    d tr_M/dε|₀ = 2^{−n} Σ_ℓ w_ℓ 2^{c(σ with letter ℓ deleted)}      [★]

`c1 = [★](free) − [★](atom)` equals Part A's exact `c1` in all six cases
(Fraction equality). Per-letter data: every intra σ deletion raises the cycle
count by 1, every σ⁻¹ deletion lowers it → proton `4·6−3 = 21`, neutron
`4·5−4 = 16`, interface pp `+4`, nn `−4`, pn `0`, all times `2^{c−1}`:

    c1(Z,N) = (21Z + 16N)·(2^{−A−1} − 2^{−2A}) − 4·(I_pp − I_nn)·2^{−2A}

verified against [★] for every (Z,N) with A = 2..20 (asserted in the probe) and
in Lean (`c1Closed_*`, `c1_defs_eq_closed`, `c1_from_letters` from the explicit
12 letter lists). Also `c1(pp) + c1(nn) = 2·c1(pn)` exactly
(`c1Closed_bond_symmetry`), and the affine step in Z at fixed A (`c1Closed_step`).

### Honest split (same as ClassicalTraceFloor)

Proved: the ring/dual-number identity of step 1; dyadicity of any [★]-sum; the
closed form's values; [★] from the letter data. Assumed: quantum Schur–Weyl
(tr_M = Tr(K ρ)/Z with K = diag(1,q²)^⊗n) and the trace-invisibility of Y.
The six `def c1_*` in `PairwiseChainLeadingOrder.lean` are therefore derived
CONDITIONAL on those two, not unconditionally.

### What this does NOT change

Nothing about the scale (`qou-59j5`) or the log channel. It removes one
"measured" from the pairwise-chain leading-order story: `c0` and `c1` are both
derived now, so `24/7` at 4He etc. are derived ratios.
