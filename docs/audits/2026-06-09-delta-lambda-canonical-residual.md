# Δ_λ(K) on the trace-canonical path: residual ≈ q₀^(10A−5) (2026-06-09)

**Status:** exploratory / **near-match tier** (c_k tiering discipline —
an observation of structure in the canonical residual, NOT a wired
closure, NOT a fit ansatz). Probe:
[`delta_lambda_canonical_residual.py`](../../computations/delta_lambda_canonical_residual.py),
witness
[`delta-lambda-canonical-residual.witness.json`](../../computations/delta-lambda-canonical-residual.witness.json).

## Context — the trace-convention reconciliation (recap)

A corpus-first sweep (full record:
`docs/audits/2026-06-09-binding-trace-convention-split.md`, PR #2082)
found the binding effort scattered across ≥3 trace conventions
(matrix-M parabolic; deprecated Plancherel `markov_trace_3A`; per-block
archimedean #1742) — while the codebase's **canonical** path already
exists and is witnessed:

- **Trace:** `computations/markov/markov_trace_canonical.py::tr_M_element`
  — the Jones–Markov trace (`z = 1/(√q+1/√q)`), forced by the four
  Markov axioms
  ([`markov-axioms-primitive`](../../content/quantum-observable-universe/braids-and-knots/markov-axioms-primitive.md),
  `prop:categorical-mass-markov`).
- **Binding:** [`binding_canonical.py`](../../computations/binding_canonical.py):
  `B_pred(Z,N) = E_0·(tr_M(W_free) − tr_M(W_atom))` — a free−bound
  **difference** of canonical traces.

The off-convention session objects (abs-sum, trace-level bar product,
matrix-M signed tr_M) are recorded as such in the convention-split audit;
the bar product is separately **rejected** (underbinds ~10⁴×).

## The finding — the canonical residual is a near-integer q₀-power

Tabulating `Δ_λ(K) = B_AME / B_pred` on the canonical path:

| atom | Z | N | A | B_AME (MeV) | B_pred (MeV) | Δ_λ | log_{q₀} Δ_λ | 10A−5 | dev |
|------|---|---|---|-------------|--------------|------|--------------|-------|-----|
| D | 1 | 1 | 2 | 2.225 | 0.4656 | 4.778 | **14.99** | 15 | −0.01 |
| T | 1 | 2 | 3 | 8.482 | 0.6290 | 13.486 | **24.93** | 25 | −0.07 |
| ³He | 2 | 1 | 3 | 7.718 | 0.6581 | 11.728 | 23.60 | 25 | −1.40 |
| ⁴He | 2 | 2 | 4 | 28.296 | 0.7135 | 39.660 | **35.27** | 35 | +0.27 |

$$ \Delta_\lambda(K) \;\approx\; q_0^{\,10A-5} \;=\; q_0^{\,5(2A-1)}, $$

with the N≥Z isotopes (D, T, ⁴He) within **0.27 q₀-exponent units** of
the integer law (the deuteron is exact to 0.01), and a Z-dependent
deviation on the proton-rich ³He (−1.40).

Equivalently: **B_AME ≈ E_0·(tr_M(W_free) − tr_M(W_atom))·q₀^(10A−5)** —
the per-nucleon increment is exactly **10** in q₀-exponent units.

## Why this matters / what it is NOT

- It locates the **entire canonical Δ_λ(K)** in a single near-integer
  q₀-power family — the kind of integer-exponent structure the
  framework's jet-order/crossing-count bookkeeping produces.
- **It is NOT wired** and must not be: per the Δ_λ-gate rule, a seventh
  fit ansatz is prohibited. The admissible next step is a **categorical
  derivation of 10A−5** (crossing-count / jet-order / tower-depth
  bookkeeping of `W_free` vs `W_atom`), which — if it exists — IS the
  canonical Δ_λ(K). If no derivation exists, the observation stays at
  near-match tier.
- The ³He deviation says any derivation must produce a Z-dependent
  correction (∼ −1.4 q₀-units per excess proton at A=3).

## Relation to the cheat-sheet 9b default

The cheat-sheet 9b canonical *default* (depth-stratified tower,
[`2026-06-09-binding-canonical-default-depth-stratified.md`](2026-06-09-binding-canonical-default-depth-stratified.md))
is a different decomposition of the same gap (undershoots 67–73%). The
Jones–Markov difference path here is the **trace-canonical** baseline;
reconciling the two decompositions (tower depths ↔ the q₀^(10A−5)
residual) is part of the same open item. Neither is wired as a closure.

## Next steps

1. **Derive or refute `10A−5`** from the canonical chain (W_free vs
   W_atom crossing/jet bookkeeping). Formalize-first: a one-line
   structural argument should fix the per-nucleon increment 10 and the
   offset −5 before any further numerics.
2. Extend `binding_canonical.py` beyond A=4 (⁶Li/⁷Li) to test the law's
   slope at higher A (coordinate with #2080's A≥4 coverage).
3. Characterize the Z-dependence on mirror pairs (T vs ³He is the only
   pair so far).
