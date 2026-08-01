# The color-pair space `T₁ ⊗ T₁` — a derived narrowing of the color-tube weight tensor

**Date:** 2026-08-01
**Bean:** `qou-ctkw` (and open question 1 of `conj:inter-nucleon-channel-color-tube`)
**Verdict:** **scope-(a) NARROWING — not a closure.** **0 *tuned* parameters** —
nothing is fitted and no target is consulted; the decomposition is forced by the
character theory. (Distinct from the *result*, which is that `W` still lives in a
2-parameter convex family — see §"The three findings". The probe introduces no
parameters; it *reduces* the ones `W` already had, from 8 to 2.) Nothing wired.

## Why this was the lead

Two independent open items want the same missing object:

* `conj:inter-nucleon-channel-color-tube` **open question 1** — the closed form of
  the 9-element color-pair weight tensor `W_{c₁c₂}(F₁,F₂)` "from the SO(3)-fiber
  tensor over Bring".
* The ν_SDP arc
  ([2026-06-21](2026-06-21-nu-sdp-saturation-obstruction-and-critical-distance.md))
  names its blocker as *"a **derived** color-flavor constraint, not the un-vetted
  9-pair ansatz"* — a positivity restoration that is not an encoding choice.

A derived `W` is exactly that constraint. And the prerequisites are now in place
and Lean-proved rather than assumed: `BringFiberAction` is **discharged** by the
icosahedral Reeb instance, and `color_sheets_carry_T1` proves the three color
sheets **are** the `T₁` irrep (3 sheets = `dim T₁`; `T₁` is the ℓ=1 Hopf
generation selection). So ordered color-sheet pairs carry `T₁ ⊗ T₁` — a
9-dimensional representation of the icosahedral group, and the color-pair index
set of `W` is a representation, not a bare index set.

## What was computed

[`computations/color_tube_t1_tensor_decomposition.py`](../../computations/color_tube_t1_tensor_decomposition.py)
· witness `color-tube-t1-tensor-decomposition.witness.json`. Exact character
arithmetic over `ℚ(√5)` on the five conjugacy classes of `A₅`, with table
**orthonormality asserted first** so the decomposition is not read off an
unvalidated table:

```
T₁ ⊗ T₁ = A ⊕ T₁ ⊕ H          (dims 1 + 3 + 5 = 9)
Sym² T₁ = A ⊕ H  (dim 6)       Alt² T₁ = T₁  (dim 3)
```

(The `Sym²/Alt²` characters use the class-squaring map, where the two 5-cycle
classes **swap** — the same index-2 fusion that carries the `T₁/T₂` chirality.)

Isotypic projector diagonals on the 9 ordered pairs, split by same-color
(`rr, gg, bb`) vs different-color, with each row's trace recovering its dimension:

| summand | diag(same) | diag(diff) | trace = dim | normalised weights |
|---|---|---|---|---|
| `A` | `1/3` | `0` | 1 | same `1/3`, diff `0` |
| `T₁` | `0` | `1/2` | 3 | same `0`, diff `1/6` |
| `H` | `2/3` | `1/2` | 5 | same `2/15`, diff `1/10` |

## The three findings

1. **A canonical 3-summand decomposition of the color-pair space, parameter-free.**
   `W` is no longer an arbitrary nonnegative normalised 9-vector per flavor pair
   (8 free parameters); it is a convex combination of three *canonical* weight
   systems (2 free parameters). That is a genuine narrowing, obtained from the
   discharged fiber action rather than posited.

2. **The `Z/2` grading the `ε` rule needs is FORCED, not chosen.** The block's
   §"Representation-theoretic constraint on ε" requires `ε` to be a section of a
   `Z/2` grading. `Sym²/Alt²` supplies one — and the assignment is forced by
   dimension alone: of the sub-collections of the summand dims `{1,3,5}`, exactly
   one sums to `dim Sym² = 6`, namely `{1,5} = {A,H}`, leaving `{3} = {T₁}` for
   `Alt²`. Machine-checked (`sym_alt_assignment_forced`).

3. **The uniform projection `W = 1/9` is the isotypy-blind barycentre.** The three
   projectors sum to the identity, whose diagonal is `1` on every pair; dividing
   by 9 returns exactly `1/9`. So the "flavor-only projection" the conjecture
   identifies as *lossy* is precisely the average that **forgets which isotypic
   summand a pair sits in**. This gives the projection a structural reading it
   did not have — the missing per-arc detail (the sign-flip diagnostic's
   `R² = 0.83` arc-count correlation) is isotypic information the average
   discards.

## What is NOT claimed

* **Open question 1 is narrowed, not closed.** The color side supplies the
  admissible *basis*; it does **not** supply the flavor dependence `(F₁,F₂)`.
  Choosing a point in the 2-parameter convex family still requires a derivation
  from the flavor structure — and picking one to match a target would be a fit.
* **No instance** of `InterNucleonChannelColorTube` is provided, so every
  downstream conditional result stays conditional.
* **No claim about ν_SDP.** Whether this constraint regularises the indefinite
  Gram is untested here. Note the standing skeptical read of that arc: six
  principled ν_SDP definitions have been refuted, and `ρ_F = ν_SDP` is flagged as
  *"a naming of an underived value"*. If a derived `W` lands and ν_SDP still does
  not follow, that is evidence against the identification — a valuable outcome,
  not a failure.
* **Nothing wired**; no dashboard or mass/binding path consumes this.

## Lean

[`QOU/BraidsAndKnots/ColorPairIsotypicDecomposition.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/ColorPairIsotypicDecomposition.lean),
sorry-free. Deliberately **not** a re-encoding of the probe's output: the file
states the *forced consequences*, which can fail — dimension consistency
(`A ⊕ T₁ ⊕ G` would give `8 ≠ 9`), the forced `Sym²/Alt²` assignment, projector
traces recovering the dimensions, the barycentre identity, and the distinctness
of the three normalised weight systems (so the narrowing is real, not three names
for one weighting).

## Cross-references

- [`conj:inter-nucleon-channel-color-tube`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md) — open questions 1 and 2.
- [`2026-06-20-he4-nu-sdp-not-computed-definition-gate.md`](2026-06-20-he4-nu-sdp-not-computed-definition-gate.md), [`2026-06-21-nu-sdp-saturation-obstruction-and-critical-distance.md`](2026-06-21-nu-sdp-saturation-obstruction-and-critical-distance.md) — the ν_SDP arc this would feed.
- `QOU/BraidsAndKnots/S5SO3FiberAction.lean`, `BringFiberActionInstance.lean` — the discharged fiber action and the A₅ branching anchors.
