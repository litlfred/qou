# Correction: P-C15's `a₁` transcription error — c4qz/T1 verdicts corrected, T1 flips to SURVIVOR

**Date:** 2026-07-07 · **Branch:** `claude/z-c-k-f-map-keystone-ub5yix` (PR #3449)
· **Found during:** I-B step B1 (the transcription gate B1-K1 failed, which it
could not have with correct inputs — the gate did its job).

## 1. The error

[`qbeta_pc15_casoratian_bar_parity_probe.py`](../../computations/qbeta/qbeta_pc15_casoratian_bar_parity_probe.py)
(P-C15, 2026-07-03, on `main`) hardcoded the 4₁ operator's middle coefficient
claiming it was "verbatim from `aj_figure_eight_certificate.py`". It was not:

| | quartic factor | denominator |
|---|---|---|
| **certificate (verified)** | `x⁴q⁴ − x³q³ − x²q³ − x²q − xq + 1` | `x⁸q²` |
| **P-C15 probe (wrong)** | `x²q² − x²q + x² − xq² − xq − x + q² + q + 1` | `x⁶` |

Not algebraically equal. The certificate's coefficients are machine-verified
(telescoping identity (*) + boundary `b = −Cert(x,1)` exact; and B1-K1 now
confirms them independently against the Habiro cyclotomic sum, exact symbolic
N=1..8, [B1 witness](../../computations/qbeta/qbeta-b1-fourone-cyclotomic-rebasing.witness.json)).

## 2. Blast radius

- **P-C15's asserted gates: UNAFFECTED.** Its two assertions used only the
  `a₀/a₂` Casoratian ratio, which both scripts agree on. Its recorded
  `coeff_bar_ratios.a1` and the docstring note "[a₁ bar-odd, upstream-proved]"
  were wrong; probe fixed, witness re-emitted (gates still PASS; the correct
  `a₁` bar-ratio is the **monomial** `x⁷/q⁵` — bar-even up to twist).
  The 2026-07-03 P-C15 audit doc on `main` quotes an abbreviated `a₁ = …(...)…`
  which concealed the mismatch — left as historical record, superseded here.
- **c4qz (I-A gate): mechanism corrected, conclusion unchanged.** With the
  correct `a₁`: K1a (`α₂(1,x) ≡ −1`) and K1b (golden locus `x* = φ^{±2}`)
  still pass — remarkably, the same locus. K2 still fails but for the
  **opposite mechanism**: `bar(α₁)/α₁ = 1` **exactly** — all slot ratios are
  exactly bar-invariant; α₁ is bar-EVEN with zero odd part. The earlier
  "non-monomial covariance" claim is **retracted** (it was the wrong-`a₁`
  artifact). Scope-(a) conclusion stands: a raw pointwise slot cannot source
  the bar-ODD channel.
- **T1 (pair-symmetrization): KILL RETRACTED → SURVIVOR.** With exact slot
  invariance, the pair-difference
  `D(q) = α₁(q, φ²) − α₁(q, φ⁻²)` is **exactly bar-ODD** (invariance + the
  bar swap permuting the pair), `D(1) = 0`, and `S(q)` is exactly bar-even —
  4/4 assertions ([T1 witness](../../computations/qbeta/qbeta-t1-barpair-symmetrization.witness.json)).
  `D(q)` is a **canonical bar-odd scalar built from the 4₁ operator on its
  own c₃-shadow locus** — the first surviving odd-channel candidate of the
  tranche. Not a c_k value; nothing wired.
- **B1+B2 (cyclotomic re-basing): 4/4 PASS.** The Habiro basis
  `ω_k = ∏(x + x⁻¹ − q^j − q^{−j})` is exactly bar-invariant
  (Lean `QOU.QBeta.cycFactor_bar_invariant`, hypothesis-free `ring`); the 4₁
  element (`C_k ≡ 1`) is bar-even in this basis; q=1 shadows have even orders
  `2k`. The odd channel must enter via the ladder evaluation map — the
  quantum-modular S-shadow picture.
- **KC11 (constraint registry): corrected** — the "non-monomial covariance"
  row replaced by the exact-invariance statement + the D(q) survivor (KC15).
- **Investigation audit (2026-07-07 §4.3): superseded on the mechanism** —
  its "non-monomial covariance still obstructs" clause is retracted; its
  verdict items 1–2 (odd-part reading; shadow gates test the even part) are
  unaffected and in fact **strengthened**: the operator side is now cleanly
  all-even, and the odd part demonstrably lives in pair-differences /
  evaluation, not in the coefficients.

## 3. Why the prevention tranche matters here

This error propagated for 4 days through an "(...)"-abbreviated formula quote
and a "verbatim" claim — the same shorthand-drift disease as the a₁ parity
incident. The fix surfaced *because* B1-K1 was a pre-stated transcription
gate. Going forward the corrected coefficient is pinned by: the certificate's
internal verification, the independent Habiro-sum check (B1-K1), and the
KC11/KC15 registry rows.

## 4. Corrected structural picture (state of the keystone after this session)

- Even skeleton, from the 4₁ operator raw slots: `α₂ ≡ −1` (the `c₂`
  constraint, identically), `α₁` bar-even with q=1 value 2 exactly on the
  golden bar-pair `x + x⁻¹ = 3`.
- Odd channel candidates: the pair-difference `D(q)` (exactly odd, vanishes
  at q=1 as it must); the ladder evaluation map (√u prefactor, `u`-twist).
- Cyclotomic basis: diagonalizes bar; `C_k ≡ 1`; the complexity lives
  entirely in the bar-even basis elements.
- Open (B3): the `(u;u)_m → u^k` composition connecting this to the c_k
  rungs, and the z-side convolution — the f-map identification proper.
