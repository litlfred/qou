# What the α_EM conditionals assert, and which can be discharged (2026-11-27)

Compute-accuracy brief C4 (epic bean `qou-myts`; beans `qou-l4t2`, `qou-3l2l`,
`qou-gg4e`, `qou-rgiz`, `qou-6ufi`). Mathematics only: no measured value enters
any statement below.

The brief names three conditionals behind the α_EM forms: the Form C two-loop
Bloch-`B₃` class, the Bring zero-mode Bloch class, and the Witten/Chern–Simons
`κ`. None of them can be honestly *discharged* by a proof today. Two can be made
precise, and one carries an empirical value inside a formal class.

## 1. Form C (`AlphaEmTwoLoopBlochSchwingerClass`): a formula for `δ`, not a claim

Audit `2026-11-24-alpha-em-two-loop-bloch-schwinger-l4t2-9y43.md` describes the
candidate `C1` with `δ = Δ_{B₃}(q) = ζ(3) − Li₃(q⁻²)`. The class
(`QOU/MassTheory/AlphaEmTwoLoopBlochSchwinger.lean:194`) takes `delta_B3` as a
**free real**, constrained only by `0 ≤ delta_B3`.

Proved in `QOU/MassTheory/AlphaEmFormCConditionalContent.lean` (lean-direct exit 0,
no `sorry`):

- `class_iff`: `AlphaEmTwoLoopBlochSchwingerClass q δ α ↔ 1 < q ∧ 0 ≤ δ ∧ 0 < α ∧ δ = deltaReq q α`,
  with `deltaReq q α = (π·b₁/H(q))·((1/α − rest(q, α))/α²)` read off the
  fixed-point equation.
- `class_of_deltaReq_nonneg`: **every** `α > 0` with `deltaReq q α ≥ 0` satisfies the
  class (take `δ := deltaReq q α`). `delta_unique`: `δ` is determined by `(q, α)`.

So the class is a one-parameter envelope; it does not contain the Form C claim.
The `−0.16σ` figure is not encoded anywhere in Lean.

- `deltaB3 q := Σ_{n≥1} (1 − q^{−2n})/n³` (= `ζ(3) − Li₃(q⁻²)` as one series);
  `deltaB3_summable`, `deltaB3_nonneg` (for `q ≥ 1`, termwise), `deltaB3_one = 0`.
- `FormCPinned q α := AlphaEmTwoLoopBlochSchwingerClass q (deltaB3 q) α`, and
  `formCPinned_iff`: for `q > 1, α > 0` it is **exactly** the one equation
  `deltaB3 q = deltaReq q α`.

That single equation is the Form C content. It is open. What would discharge it is
a derivation of the two-loop coefficient `H(q)·Δ_{B₃}(q)/(8π)` from the model; the
corpus has none. Note also that `C1` is one of six pre-registered candidates, and
`qou-aemx` forbids choosing among them by residual.

Pre-Archimedean remark (from PR #9447): `Δ_{B₃}` at real `q` is a value of the real
trilogarithm, not yet the regulator of an element of a Bloch group `B₃(F)`. Calling
it a "Bloch-`B₃` class" is a label until such an element is exhibited.

## 2. An empirical value inside a formal class (owner rule: no empirical predictions in proofs)

`predicted-spectra/em-coupling-fixed-point.lean:158`:

    codata_consistent : |1 / α - codataInvAlpha| < 1e-3

is a field of `AlphaEmFixedPointNormalization`, and `alpha_em_is_fixed_point_root`
returns it as part of its conclusion. That is a measured value inside a formal
statement. Same pattern, outside C4: `mass-theory/borromean-baryon-mass-formula.lean:145,149`
(`proton_matches_codata`, `neutron_matches_codata`). No other Lean file references
`AlphaEmFixedPointNormalization` (grep of `folio/`).

Not changed here (owner decision; see the PR's options).

## 3. Witten / Chern–Simons `κ`

`predicted-spectra/em-coupling-chern-simons.lean`: `κ` is the Gram-determinant
ratio; the resummation `Σ δ^j κ^{j−1} = δ/(1 − δκ)` is proved (`csTower_resums`);
the identity for `κ` is a content-bearing class with no instance. Not dischargeable
here: it needs the Chern–Simons Gram matrices. Even if proved, audit
`2026-08-22-alpha-em-derivation-redteam.md` records the resulting value at
−467.6 ppb, so it would not move the Form B/C comparison.

## 4. Bring zero mode (`BringZeroModeBlochClass`)

`QOU/MassTheory/EmCouplingBringZeroMode.lean:305`. The class already records itself
as **expected false** (it would make `1/π` a rational combination of periods), and
notes that torus-knot carriers have Bloch–Wigner value 0. The term `2/(3π)` is
itself proved sorry-free as a Gauss–Bonnet ratio (`2g/Area`, `g = 4`); only its
reading as a Bloch class is conditional. The new `BlochGroup F` of PR #9447 would
let the class impose the cocycle condition it currently omits; that would make a
refutation sharper, not discharge it.

## Summary for the owner

| conditional | status after this note |
|---|---|
| Form C class | proved equivalent to `δ := deltaReq(q, α)`; content isolated as `deltaB3 q = deltaReq q α` (open) |
| `codata_consistent` field | empirical value inside a formal class; owner decision |
| Witten/CS `κ` | unchanged; needs CS Gram matrices |
| Bring zero mode | unchanged; expected false by its own record |
