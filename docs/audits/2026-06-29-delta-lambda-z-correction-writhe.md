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

## Slope test + Z-coefficient — RAN (2026-06-29, `delta_lambda_z_coefficient_and_slope.py`)

⁶Li, ⁷Li, ⁷Be were added to `binding_canonical.py` (fast path; A=7 sub-second)
and the residual recomputed. Two decisive outcomes:

### (1) The `10A−5` leading law is REFUTED at A≥5 — scope-(a)

| atom | A | log_{q₀}Δ_λ | 10A−5 | dev | marginal slope |
|---|---|---|---|---|---|
| D | 2 | 14.99 | 15 | −0.01 | — |
| T | 3 | 24.93 | 25 | −0.07 | ≈10 |
| ⁴He | 4 | 35.27 | 35 | +0.27 | ≈11.7 |
| ⁶Li | 6 | **36.12** | 55 | **−18.88** | **0.43** |
| ⁷Li | 7 | 38.79 | 65 | −26.21 | 2.67 |
| ⁷Be | 7 | 37.02 | 65 | −27.98 | — |

The producer's earlier extrapolation (⁶Li→55, ⁸Be→75) is **falsified by direct
compute** (⁶Li = 36.1). The slope is ≈10/nucleon only for A≤4 and collapses to
≈0.4 at the ⁴He shell. **Scope-limited negative (a)**, not a structural
exclusion: `B_pred` SATURATES (≈0.7–0.8 across A) while `B_AME` grows ~linearly,
so `log Δ_λ = log B_AME − log B_pred` is logarithmic — the slope-10 was a
coincidence of two light-nucleus trends. The crossing-sum arithmetic
(`σ+σ⁻¹=10A−2`) stands; only its reading as a *global* binding-exponent law
does not. (The earlier producer's ⁶Li/⁸Be "prediction" is re-scoped in place,
not deleted, per the refuted-discipline.)

### (2) The bar-odd Z-correction SURVIVES — confirmed at a second mirror pair

The mirror-pair split (proton-rich − neutron-rich, fixed A) isolates the bar-odd
Z-term independently of the collapsing even baseline:

| pair (A) | proton-rich | mirror | proton-excess penalty |
|---|---|---|---|
| T / ³He (3) | ³He −1.40 | T −0.07 | **−1.34** |
| ⁷Li / ⁷Be (7) | ⁷Be −27.98 | ⁷Li −26.21 | **−1.77** |

Both ≈ −1.3…−1.8 per excess proton, **same sign** — the Z-correction holds at
A=7 even though the leading law has collapsed, confirming the two channels are
independent (as the writhe split predicts).

- **SIGN derived** from the `3 > 1` seed: proton intra-writhe (+3) > neutron
  (+1) ⇒ proton excess is net-positive-chirality ⇒ penalised. Both proton-rich
  members sit below their mirrors. ✓
- **MAGNITUDE not a single derivable number.** −1.34 (A=3) vs −1.77 (A=7) drift
  ~33%; with two pairs, claiming a parameter-free constant would be numerology —
  **not attempted** (Δ_λ gate). Honest statement: O(−1.5)/excess-proton,
  sign-fixed, magnitude open.

## Net picture (updated)

- **bar-even leading (`10A−5`)**: downgraded — a **light-nucleus (A≤4)
  artifact**, refuted as a global law by the ⁶Li/⁷Li/⁷Be slope test.
- **bar-odd Z-correction (proton-excess penalty)**: upgraded — **confirmed**
  across two independent mirror pairs (sign derived; magnitude O(−1.5), open).
- **Not wired.** Nothing here touches production. Witness:
  `delta-lambda-z-coefficient-and-slope.witness.json`.
