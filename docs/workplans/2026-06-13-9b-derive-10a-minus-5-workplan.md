# 9b work-plan — derive or refute `Δ_λ(K) ≈ q₀^(10A−5)` (trace-canonical residual)

**Date:** 2026-06-13 · **Branch:** `claude/9b-derive-10a-minus-5-2026-06-13`
**Owner mandate:** option B of the
[step-9a flip decision package](../audits/2026-06-13-step9a-flip-decision-package.md)
(owner-selected 2026-06-13) makes this item the gate for the per-knot
production flip as well as the standing 9b frontier item.
**Discipline:** formalize-first; Δ_λ-gate (no seventh fit ansatz — the
observation stays near-match tier until *derived*); tiered reporting.

## Inputs (all existing; no recompute needed to start)

- Finding: [`2026-06-09-delta-lambda-canonical-residual.md`](../audits/2026-06-09-delta-lambda-canonical-residual.md)
  — `Δ_λ(K) = B_AME/B_pred ≈ q₀^(10A−5)`; D exact to 0.01 exponent
  units, T −0.07, ⁴He +0.27, ³He −1.40 (Z-dependent).
- Producer + witness: `delta_lambda_canonical_residual.py`,
  `delta-lambda-canonical-residual.witness.json`.
- Canonical trace/binding: `markov/markov_trace_canonical.py::tr_M_element`,
  `binding_canonical.py` (`B_pred = E_0·(tr_M(W_free) − tr_M(W_atom))`).
- Word structure: `mass_at_3A_proper.py::atom_braid_word_3A(Z,N)`
  (chain convention; word lengths 11/23/35/47 = `12A−1` for
  A = 1..4 per the Option-A witness; free variant drops the `A−1`
  inter-nucleon crossings).

## H1 — the structural reading to prove or refute first

The exponent factors as

$$ 10A-5 \;=\; 5\,(2A-1) \;=\; 5\cdot\bigl(\underbrace{A}_{\text{nucleons}} + \underbrace{A-1}_{\text{interfaces}}\bigr), $$

i.e. a constant **weight 5 per chain object** (nucleon or interface).
H1: this weight is the crossing/jet bookkeeping of one chain object in
the `W_free` vs `W_atom` difference under the Jones–Markov trace —
derivable from the canonical word structure, not a coincidence of two
small integers.

**Formalize-first step 1 (before any numerics):** write the one-line
candidate argument — per added nucleon the atom word gains 12 crossings
and the free word 11, per interface the atom word gains 1 — and push the
jet-order accounting of `tr_M(word)` through `z = 1/(√q+1/√q)` to see
whether a 5-units-of-q₀ increment per object is forced, forbidden, or
underdetermined. Each outcome is decisive: forced → continue to Lean;
forbidden → the near-match is numerology, record refutation;
underdetermined → identify the missing structural input before touching
data.

**Constraint any derivation must produce:** the ³He deviation
(≈ −1.4 q₀-units at Z>N, A=3) — i.e. a Z-dependent correction term,
absent for N ≥ Z. A derivation that cannot break p↔n symmetry here is
wrong (cf. `pn_convention="bring_color_weighted"` as the obvious
symmetry-breaking ingredient already in the canonical words).

## Plan (session-ordered)

1. **Structure:** H1 jet-order argument (above). Output: short audit doc
   with the argument or its refutation; no production change.
2. **Lean:** if H1 survives, state the combinatorial lemma (word-length /
   crossing-count of `atom_braid_word_3A` vs free) in Lean — provable
   from the construction — and the conditional bridge to the exponent as
   a §3b-cond class if the analytic step resists.
3. **Numerics (only after 1):** extend `binding_canonical.py` to ⁶Li/⁷Li
   (slope test at A ≥ 5 discriminates `10A−5` from same-small-A
   lookalikes); mirror pairs beyond T/³He for the Z-term.
4. **Reconcile** with the depth-stratified 9b default (different
   decomposition of the same gap; neither wired).

## Explicitly out of scope

Wiring anything to production; any fit of the exponent or the Z-term;
re-litigating the 9a flip (gated on this item per the cheat-sheet note).
