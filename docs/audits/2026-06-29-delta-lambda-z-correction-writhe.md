# Δ_λ Z-correction = the bar-odd writhe `σ−σ⁻¹ = 4Z` (2026-06-29)

**Branch:** `claude/categorical-derivation-10a-5-85e945`.
**Discipline:** formalize-first; Δ_λ gate (no fit); tiered status.
**Status:** the *arithmetic skeleton* of the Z-correction is **derived**; the
*coefficient* (`≈ −1.4` / excess proton) stays **measured, not fitted** (open).

This audit records the bar-parity reading of the `10A−5` Δ_λ residual and its
Z-dependent correction, completing the structural half of the
[2026-06-19 keystone audit](2026-06-19-delta-lambda-exponent-keystone-formalize-first.md)
on the Z side. It answers the standing constraint from the
[2026-06-09 finding](2026-06-09-delta-lambda-canonical-residual.md): *any*
derivation of the residual must produce a Z-dependent correction (³He needs
`≈ −1.4` q₀-units per excess proton, absent for N ≥ Z).

## The bar-parity split — why the correction is forced to be Z-only

The atom braid word `atom_braid_word_3A(Z, N)`
(`computations/mass_at_3A_proper.py`) has closed-form crossing counts
(`delta_lambda_exponent_from_crossings.py`, verified D, T, ³He, ⁴He):

| quantity | closed form | parity under q ↦ q⁻¹ | depends on |
|---|---|---|---|
| positive crossings `σ` | `7Z + 5N − 1` | — | Z, N |
| negative crossings `σ⁻¹` | `3Z + 5N − 1` | — | Z, N |
| **sum** `σ + σ⁻¹` | `10A − 2` | **bar-EVEN** | **A only** (Z, N cancel) |
| **writhe** `σ − σ⁻¹` | `4Z` | **bar-ODD** | **Z only** (A, N cancel) |
| color-averaged `d = −h/2` | `2A + 1` | bar-EVEN | A (0 net q-power) |

The leading exponent `10A−5 = (σ+σ⁻¹) − 3` lives entirely in the **bar-even**
sum, so it is **A-only**: it cannot carry any Z-dependence. The binding data
nonetheless shows a Z-dependent deviation (sharp on proton-rich ³He). By parity
that deviation **must** come from the **bar-odd** part — the writhe `σ−σ⁻¹ = 4Z`.
This is not a modelling choice; a symmetric (bar-even) object is q ↦ q⁻¹
invariant and structurally incapable of producing the ³He/T asymmetry.

**This is a leading-order + first-correction picture.** 0th order: the bar-even
`q₀^{10A−5}` (A-only, exponent 15→35). 1st correction: the bar-odd writhe-driven
Z-term, small relative to the leading exponent (D: `0.01/15 ≈ 0.07 %`;
³He: `1.40/25 ≈ 5.6 %`).

## The writhe decomposition — the p≠n seed and the mirror-pair splitter

The writhe splits exactly into intra-nucleon and interface parts:

    writhe = 4Z = intra (3Z + N) + interface (Z − N)

- **Intra (`3Z + N`).** Per-nucleon intra-𝓑₃ writhe: a **proton** walk is
  `6σ − 3σ⁻¹ = +3`, a **neutron** `5σ − 4σ⁻¹ = +1`. The inequality `3 ≠ 1` is
  the **p≠n seed**: a proton walk is intrinsically more positive-chirality, so a
  proton excess accumulates net writhe faster than a neutron excess. This is the
  structural origin of the asymmetric penalty (³He penalised, mirror T barely).
- **Interface (`Z − N`).** `(Z−1)` `p-p` interfaces are `σ` (+1), `(N−1)` `n-n`
  are `σ⁻¹` (−1), the single `p-n` is bar-symmetric (0): net `(Z−1) − (N−1) =
  Z − N`. This is the **mirror-pair splitter** — the only writhe contribution
  that distinguishes ³He (`Z−N = +1`) from T (`Z−N = −1`), which share
  `σ+σ⁻¹ = 28` and hence an identical leading exponent `25`.

The measured deviation tracks `Z−N` asymmetrically: `D` (0) `−0.01`, `T` (−1)
`−0.07`, ³He (+1) `−1.40`, ⁴He (0) `+0.27`. Proton excess (`Z−N = +1`) is
penalised ≈20× more than the mirror neutron excess (`Z−N = −1`) — exactly the
sign-asymmetry the `3 > 1` intra seed predicts.

## What is derived vs open (tiered)

- **Derived (pure arithmetic; Lean sorry-free):** `σ−σ⁻¹ = 4Z` (Z-only);
  `intra (3Z+N) + interface (Z−N) = 4Z`; interface imbalance `= Z−N`; the p≠n
  seed `protonIntraWrithe (3) ≠ neutronIntraWrithe (1)`; and the *conditional*
  ³He-vs-T consequence given the asymmetry hypothesis.
- **Conjectural / open (NOT asserted — Δ_λ gate):** the bridge from the writhe
  to the binding exponent *coefficient* (`≈ −1.4` per excess proton). It is
  recorded as the predicate `ProtonExcessPenaltyAsymmetry` (truth open), never a
  theorem; the coefficient is measured, never fitted into the closure.

## Lean

`content/quantum-observable-universe/lean/QOU/BraidKnot/DeltaLambdaExponentKeystone.lean`
(namespace `QOU.BraidKnot`), extended this PR with the Z-companion section:

| decl | kind | content |
|---|---|---|
| `writhe`, `writhe_eq_four_Z` | def + **theorem** | `σ − σ⁻¹ = 4Z` (omega) |
| `protonIntraWrithe`/`neutronIntraWrithe` | def | `3` / `1` |
| `proton_neutron_intra_writhe_asymmetry` | **theorem** | `3 ≠ 1` (decide) |
| `intraWrithe`, `interfaceImbalance` | def | `3Z+N`, `(Z−1)−(N−1)` |
| `interfaceImbalance_eq_Z_sub_N` | **theorem** | `= Z − N` (ring) |
| `writhe_intra_interface_decomp` | **theorem** | `(3Z+N) + (Z−N) = 4Z` (ring) |
| `ProtonExcessPenaltyAsymmetry` | def (`Prop`) | conjecture predicate (NOT asserted) |
| `he3_penalised_more_than_triton` | **theorem** | conditional: `δ 1 < δ (-1)` given the asymmetry |

Verified sorry-free via `lean`-direct over the restored `lake-cache/qou-v4-24-0`
oleans (exit 0).

## Not done / next

- **Coefficient.** Whether `≈ −1.4` per excess proton derives from the `3 > 1`
  intra seed (e.g. as a writhe-weighted q₀-power) is the open research step.
  Until it lands the Z-correction stays near-match tier; **no fit** (Δ_λ gate).
- **Slope test.** Extend `binding_canonical.py` to ⁶Li/⁷Li to test `10A−5` at
  A ≥ 5 and the `Z−N` correction on a second mirror pair (per the 9b workplan).
- **Not wired.** Nothing here touches production.
