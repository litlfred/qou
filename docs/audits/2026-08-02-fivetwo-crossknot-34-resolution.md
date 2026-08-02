# 5₂ cross-knot {3,4} distinguisher — the scalar-vs-spectrum resolution lever

**Date:** 2026-08-02
**Branch/PR:** `claude/fivetwo-crossknot-34-resolution-2026-08-02` / #4567
**Arc ledger:** [`docs/coordination/2026-08-02-c3-odd-aomega-unification.md`](../coordination/2026-08-02-c3-odd-aomega-unification.md)
**Keystone siblings:** #4554 (A_ω internal derivation), #4553 (DT/3d-index unification)

## The question

The c₃-odd leg of the Δ_λ chain reduces to the fibre→observable normalization
of the bar-odd channel `S = Q_β/E₀`. The keystone (#4554) established that the
integer target is the **q-exact GGM symmetry constant** `S₁₂+S₂₁ = 3·S₁₁` for
4₁ (`StokesSymmetryConstant.symmetryConstant_const`, sorry-free), and that the
DT *spectrum* is the pair `{3,4}`. For 4₁'s **2×2** Stokes block the *scalar*
reading (a single 3) and the *spectrum* reading ({3,4}) cannot be numerically
separated — the `σ_A ≈ 40%` ppb-q₀ ceiling (#4541) blocks it.

**5₂ has a 3×3 Stokes block and is chiral** (4₁ is amphichiral). Whether `S`
carries the scalar constant or the full spectrum is therefore a **structural**
distinction, decidable from the 5₂ analogue and *not* blocked by the precision
ceiling. This is the arc ledger's route 1 ("cross-knot {3,4} test on 5₂").

## Method — reuse of certified corpus, no recompute

The certified 5₂ Stokes pair `S±(q)` is assembled by
[`computations/probes/qbeta_g3_5two_stokes_sandwich.py`](../../computations/probes/qbeta_g3_5two_stokes_sandwich.py)
(K1/K2/K3 ✓, unflipped W-convention), whose q→0 limits are the glyph-decoded
(96/97) factorizations. The same integer matrices are Lean-promoted in
[`FiveTwoStokesMatrixIdentities.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/FiveTwoStokesMatrixIdentities.lean).
The distinguisher probe
[`fivetwo_crossknot_34_distinguisher.py`](../../computations/probes/fivetwo_crossknot_34_distinguisher.py)
imports that machinery unchanged and computes three things.

### Certified leading matrices

```
S⁺(0) = [[1, 4, 0], [0, 1, 0], [-3, -9, 1]]    (the (96) factorization, constant 4)
S⁻(0) = [[1, 0, 3], [-4, 1, -3], [0,  0, 1]]    (the (97) factorization, constant 3)
```

## Findings

### 1. The literal 4₁ symmetry constant does not clone to 5₂

For 4₁, `(S₁₂+S₂₁)/S₁₁ = 3` q-exactly. For 5₂, the direct (1,2)-pair analogue
`(S₁₂+S₂₁)/S₁₁` is **NOT a q-exact constant** for either `S⁺(q)` or `S⁻(q)`
(tested to O(q¹²) by exact q-series long division). A battery of `(Sᵢⱼ+Sⱼᵢ)/Sₖₖ`
combinations and the trace likewise fail to be q-constant. The scalar symmetry
relation is a 2×2 / amphichiral feature, not a knot-universal one.

*(Scope note: this battery is the natural set of generalizations, not a proof
that GGM's eq-65 3×3 symmetry — whatever its exact form — has no q-exact
constant. The load-bearing argument is §3, which is independent of it.)*

### 2. The DT spectrum {3,4} is split across chirality

`S⁺(0)` carries the **4** (its (1,2) entry, the (96) constant); `S⁻(0)` carries
the **3** (its (1,3) entry, the (97) constant). The spectrum genuinely has two
distinct members — unlike amphichiral 4₁, whose single `S⁺(0)=[[1,3],[0,1]]`
carries only 3 (the two chiralities coincide, collapsing the spectrum).

### 3. The distinguisher — the bar-odd observable is ι-odd, the scalar is ι-even

The bar-odd observable `ω = β·p − β⁻¹·q` is **ι-odd**
(`BarOddAntisymOffDiagonal.omega_iota_odd`) under the amphichiral involution
`ι : (β,p,q) ↦ (β⁻¹,q,p)`, and **vanishes on the amphichiral ι-fixed locus**
(`omega_zero_on_iotaFixed` — the corpus fact `V(4₁)_odd = 0`). The symmetry
constant `(S₁₂+S₂₁)/S₁₁` is a **SUM** — an ι-**even** object. An ι-odd observable
cannot be carried by an ι-even scalar. At the level of the two chirality
constants, the ι-odd datum is the antisymmetric combination
`chiralityOdd(a,b) = a − b`: for 5₂ it is `chiralityOdd(4,3) = 1 ≠ 0` (a genuine,
chirality-sourced datum), and it vanishes on the amphichiral degeneracy
`chiralityOdd(a,a) = 0`.

A subtle but decisive consequence: **4₁'s A_ω = 3 lives in the ι-even sector,
but the bar-odd observable lives in the ι-odd sector and vanishes at 4₁.** Using
4₁'s symmetric constant 3 to normalize the bar-odd channel is therefore a
category mismatch — amphichiral 4₁ supplies *no* bar-odd information. Only a
chiral knot (5₂) sources the channel, and there the relevant datum is the
chirality split, not a symmetric scalar.

## Verdict (scope-labelled, honest)

**5₂ REFUTES the single-scalar-symmetry-constant reading of the bar-odd
normalization — scope-(a), structural.** It does **not** confirm either A=2
(κ_shape) or A=3 (A_ω·κ_pot) as a *knot-independent scalar*: the correct object
is per-chirality (the {3,4} split), degenerating to the single 3 at amphichiral
4₁ only because the two chiralities coincide there.

This does **not** exclude the integer 3 (or 4) as an *ingredient* — 3 is the S⁻
member of the spectrum, 4 the S⁺ member — and per the anti-over-claim discipline
it is a scope-(a) constraint on the *reading/combination*, not a scope-(b)
structural exclusion of any ingredient. What is sharpened: the residual
normalization fork (`qou-yh67`, `qou-pzzl`) moves from "**scalar vs spectrum**"
to "**which member/combination of the {3,4} chirality split**". The ι-odd grade
of the observable is a genuine constraint on that choice (it must be an ι-odd
combination — the difference-type datum — not the ι-even sum).

## Formalization (formalize-first, sorry-free)

[`FiveTwoDTSpectrumSplit.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/FiveTwoDTSpectrumSplit.lean)
— core-Lean-only (verifies with the toolchain alone, no Mathlib olean set;
§7c integer data, no `ℝ`). Decidable facts:

| Theorem | Content |
|---|---|
| `splus0_carries_four` / `sminus0_carries_three` | the {3,4} split across chirality |
| `dt_spectrum_two_element` | `4 ≠ 3` — genuine 2-element spectrum |
| `chirality_odd_datum_ne_zero` | `chiralityOdd 4 3 = 1 ≠ 0` — nonzero ι-odd datum |
| `chiralityOdd_degenerate` | `chiralityOdd a a = 0` — vanishes at amphichiral degeneracy |
| `chiralityOdd_antisym` | the datum is genuinely antisymmetric (ι-odd) |
| `readings_all_distinct` | sum(7)/members(4,3)/diff(1) pairwise distinct |

## Anti-numerology guards respected

- No new fit; no `c_k` wired; no axiomatization; the answer was **not** picked
  to match 4₁ (the probe's expected assertion is *FALSE* for the scalar reading).
- q₀-independent — the σ_A≈40% ceiling (#4541) is irrelevant to a structural
  matrix-entry comparison.
- The refutation is scoped (a) and does not exclude the integers 3/4 as
  ingredients (per the "refuted/ruled out" STRICT rule).

## Next / open

- **`qou-yh67` / `qou-pzzl`** — the normalization fork, now sharpened to "which
  {3,4} member/combination, constrained to be ι-odd." Still structurally open;
  this PR narrows but does not close it.
- Converge with #4554 / #4553: whichever lands the DT-count→observable bridge
  first should cite this cross-knot result as the structural evidence that the
  bridge output is per-chirality, not a universal scalar.
