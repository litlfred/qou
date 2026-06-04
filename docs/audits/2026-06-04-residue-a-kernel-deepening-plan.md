# residue-A kernel deepening — Lean engine + cleaner `c_k` re-run + SDP-zero probe

**Date:** 2026-06-04
**Status:** PLAN (in progress)
**Predecessor:** [residue-A unblock kernel scope (#1823, merged)](2026-06-04-residue-a-unblock-kernel-scope.md)

Three author-chosen follow-ups after the kernel scope + recurrence first-cut +
verified `pole_reciprocal_is_char_root` landed. The section numbers below are the
**original option numbers** from #1823's "what next" menu; they are executed in
the author's priority order **3 → 1 → 2**.

## 3. Extend the Lean grounding (env now works)

Now that the toolchain is bootstrapped, extend
[`RationalCoeffRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/RationalCoeffRecurrence.lean):

- **`CFinite d q c`** — the order-`d` constant-coefficient linear recurrence
  (the coefficients of a proper rational `P/Q`).
- **`CFinite.recurrence_step`** — the recurrence *solves for the leading term*:
  for `n ≥ d`, `c n = -(q 0)⁻¹ · ∑_{j<d} q (j+1)·c (n-(j+1))`. This is the
  "kernel produces `c_k` from the seed" engine in math form — it makes the
  Step-2 statement ("the kernel determines `c_{k+1}` from the last `d`")
  rigorous. Verified sorry-free.

## 1. Re-run the recurrence first-cut on consistent-precision c_k

The recurrence first-cut (Step 2 of #1823) left the subleading kernel buried
under the **`c_k` extraction-noise floor** (~1e-5). Sibling **#1824** is
re-extracting `c_4…c_10` at consistent precision —
exactly the input needed. Pick up its witness and **re-run** the Hankel-rank /
over-determined recurrence fit (`qbeta_ck_recurrence_first_cut.py`) on the
cleaner sequence: does a higher-order constant-coefficient recurrence now
appear (⇒ `F` rational, kernel pinned), or does the no-low-order-kernel result
survive at the tighter floor? Gated on #1824's output; coordinate to compose.

## 2. Probe the SDP-normalization zero (the near-real pole)

The interpretive synthesis (#1823 scope): the residue-A pole is a **zero of
`Q_A·cos α_eff`** (the confinement-SDP normalization) near `q₀`, not a
root-of-unity. First concrete cut: from the existing operator-valued witnesses,
evaluate `Q_A·cos α_eff(q)` near `q₀`, locate its zero in `q`-space, and check
it coincides with the residue-A pole at `u_substrate` (imaginary distance
`ε ≈ 4.4e-7`, #1821). If they coincide, the SDP-zero ⇒ pole hypothesis gains a
quantitative anchor; if not, the synthesis is refined/refuted. Diagnostic-only.

## Guards

- TIERED reporting; no fitting.
- `ℏ_q` / `q₀` from canonical witnesses, never hard-coded.
- Lean verified sorry-free against the bootstrapped toolchain.
- Diagnostic-only; no production wiring.
- Tiers governed by the [c_k/d_k registry](../coordination/ck-dk-canonical-registry.md).
