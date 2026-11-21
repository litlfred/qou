/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.Tactic

/-!
# QOU.QBeta.A3OffBlockDerivation — deriving the A=3 super-matrix off-blocks from the Hecke/Wedderburn branching, and the structural bound that EXCLUDES the observed lift

**Scope (read this first).**  This file attacks the wall that ROUTE 2
(`QOU.QBeta.SuperBerezinianA3Magnitude`, PR #4544) relocated: *"derive the q-cubic
off-diagonal blocks `B, C` of the graded super-matrix from first principles."*
Route 2 proved that treating `B` as a **free scalar** makes the even-face correction
`(A − B·D⁻¹·C)/A` surjective, so hitting `r* ≈ 1.585` that way is a **fit**.  Here we
do NOT treat `B` as free: we **derive** the off-blocks from the actual A=3 categorical
data (the `H₃(q)` Wedderburn branching + the super-sector grading) and prove what that
derivation actually yields.

**The categorical input (the A=3 branching data — all established corpus structure).**
* `H₃(q)` is semisimple with three Wedderburn blocks, the partitions of 3:
  `(3)` (trivial rep, `dim 1`), `(2,1)` (standard, `dim 2`), `(1,1,1)` (sign, `dim 1`);
  `1 + 4 + 1 = 6 = 3!`.
* The bar-involution `q ↦ q⁻¹` acts on the blocks as the **transpose** (conjugate
  partition, = the sign-twist / keystone `T₁↔T₂` parity, `option-e.md` 2026-06-16):
  it **fixes** the self-conjugate `(2,1)` and **swaps** `(3) ↔ (1,1,1)`.
* The **super-sector grading** is that transpose involution's `±1` eigendecomposition:
  the bar-EVEN (mass / C1 / cosh) face is the `+1` eigenspace
  (`e_{(2,1)}` and `e₊ = (e_{(3)}+e_{(1,1,1)})/√2`); the bar-ODD (GGM / decay / sinh)
  face is the `−1` eigenspace (`e₋ = (e_{(3)}−e_{(1,1,1)})/√2`).
* The mass endomorphism `𝓜` (`Re 𝔙 = binding`) is **bar-self-adjoint**
  (`BerezinianSelfAdjointCrossTerm`) — diagonal `𝓜 = diag(a, c, b)` in the Wedderburn
  basis, with `a = m_{(3)}`, `c = m_{(2,1)}`, `b = m_{(1,1,1)}` its block contributions.

**The derivation (Part 2).**  Rotating the self-adjoint `𝓜` into the transpose
eigenbasis is a fixed orthogonal change of basis — it does **not** leave `B` free.  On
the `(3)↔(1,1,1)` 2-cycle the symmetric-under-swap rotation `e₊,e₋` gives, with **no**
remaining freedom,

  even `(2,2)`-entry `= (a+b)/2`,  odd block `D = (a+b)/2`,
  off-blocks `B = C = (a−b)/2`   (the `(2,1)` block decouples).

So the even-face Berezinian correction (`(A − B·D⁻¹·C)/A` on the `e₊` mass face) is the
**derived** quantity

  `r(a,b) = 1 − ((a−b)/(a+b))²`   (`magnitudeFactor_eq`).

**The result (Part 3 — scope-(b) structural exclusion, invariant cited).**

> **`magnitudeFactor_le_one` (sorry-free):** for ALL real diagonal blocks `a, b`
> (`a+b ≠ 0`), `r(a,b) = 1 − ((a−b)/(a+b))² ≤ 1`.  The self-adjoint Hecke/Wedderburn
> branching Schur complement is a **REDUCTION**, never a lift.

The observed A=3 factor is a genuine **LIFT** `r* = μ₃/c₃ ≈ 1.585 > 1` (the single
Markov trace `c₃ = 0.297` is bracketed *short* of the AME moment `μ₃ = 0.4708`).  By
`observed_lift_unreachable`, the branching-derived factor **never** equals any `r > 1`
— in particular `r*` and the whole Route-5 acceptance band `[1.50, 1.71]` are
**structurally unreachable**.  The cited invariant is square non-negativity
(`sq_nonneg`): `r > 1` would force a real square to be negative.

**Why (Part 5 — the parity certificate).**  The branching off-blocks are **equal**
(`B = C`, symmetric real rotation) and, since the two 1-dim blocks are bar-conjugate
(`b = σ a`: trivial/sign Markov weights are `q↔q⁻¹` conjugate — the equal Borromean
characters, Part 1), **bar-ODD** (`σB = −B`).  Hence `C = −σ B`: the assembly is
**graded self-adjoint** (`BerezinianSelfAdjointCrossTerm.selfadjoint_crossTerm_bar_even`
⇒ its cross-term is bar-EVEN, the correct parity for the bar-even ratio `r*`, yet
provably bounded `≤ 1`).  A `r* > 1` lift therefore requires **anti-self-adjoint**
(`C ≠ −σ B`, two INDEPENDENT amplitudes) off-blocks — precisely the GGM / Stokes datum
the branching does NOT determine.  This is the honest under-determination: the
categorical branching fixes the bar-even, self-adjoint sector (bounded `≤ 1`); the
bar-odd anti-self-adjoint amplitude that the observed lift needs is left FREE.

**Net verdict — scope-(b) on the self-adjoint branching route; the derivation of `B,C`
from branching does NOT close `r*`.**  It sharpens Route 2: the branching data is not
merely *silent* on `B` (Route 2), it *positively* supplies the wrong-sign
(reduction, `≤ 1`) self-adjoint off-block; the lift is carried entirely by the
anti-self-adjoint off-block (`conj:qdifference-kernel-prolongation-symbol`, bean
`qou-jqof`), recorded as the §3b dependent class `A3LiftFromDerivedOffBlock` with **NO
instance**.  Nothing is fitted, nothing is wired.

**Honesty (STRICT — AGENTS.md §Axiomatization-is-NOT-a-Proof / §3b).**  The four
structural theorems are genuine algebra (a Schur-complement identity, a real-square
bound, a parity certificate), sorry-free.  The single conjecture class carries genuine
content (an equation + a strict inequality on a GEOMETRIC input), has no instance, and
is never self-assuming: `κ_phys` is *checked against* a derived off-block, never solved
from it.

**Base ring (§7c).**  Parts 1–2 and the class: generic `{R : Type*} [Field R]` (scalar
inverses `D⁻¹`, `q⁻¹` genuinely required — the §7c `[Field R]` inverse carve-out).
Part 3's bound adds `[LinearOrder R] [IsStrictOrderedRing R]` (the ordering `≤ 1` is
genuinely archimedean; same generic ordered-field pattern as
`QOU.…DeltaLambdaL1Ceiling`).  Part 5: generic `[CommRing R]` with an abstract bar
`σ : R →+* R`.  No `ℝ`, no `Real.*`; the numerics `r* ≈ 1.585`, `c₃ = 0.297`,
`μ₃ = 0.4708` live only in the Python witness / audit, downstream of the
substrate→archimedean wall.

## References

- [leitner2026] `conj:qdifference-kernel-prolongation-symbol` (the DM q-cubic period
  datum that would pin the anti-self-adjoint off-block); `QOU.QBeta.SuperBerezinianA3Magnitude`
  (Route 2 — the surjectivity/fit result this file sharpens);
  `QOU.QBeta.BerezinianSelfAdjointCrossTerm` (self-adjoint ⇒ bar-even cross-term);
  `QOU.QBeta.OddDecayWeightParity`; `QOU.BraidKnot.A3OperatorCombinerMagnitude`
  (Route 1 — the magnitude is a non-uniform per-partition functional);
  `docs/coordination/option-e.md` (the A=3 magnitude bracket rows); bean `qou-jqof`.
- [wenzl1988] Wenzl, "Hecke algebras of type Aₙ and subfactors", Invent. Math. 92
  (1988) 349-383 (the Markov trace weights on the Wedderburn blocks).
- [donagi-markman1996cubics] https://arxiv.org/abs/alg-geom/9408004 §1 (the cubic
  condition that would pin the off-blocks geometrically).
-/

noncomputable section

namespace QOU.QBeta.A3OffBlockDerivation

/-! ### Part 1 — the branching data: the `H₃(q)` Borromean characters on the transpose
2-cycle `(3) ↔ (1,1,1)` are EQUAL.

The Borromean braid is `β = (σ₁σ₂⁻¹)³ ∈ B₃`.  On the two 1-dim blocks the generators
act by scalars: trivial `σᵢ ↦ q`, sign `σᵢ ↦ −q⁻¹`.  Both characters evaluate to `1`,
so the two diagonal super-matrix entries `m_{(3)}, m_{(1,1,1)}` differ **only** by their
Markov weights `w_{(3)}, w_{(1,1,1)}` — which are `q↔q⁻¹` bar-conjugate (Part 5). -/

/-- Character of the trivial (symmetric) 1-dim rep on the Borromean braid
    `β = (σ₁σ₂⁻¹)³`, `σᵢ ↦ q`: `(q·q⁻¹)³ = 1`. -/
theorem trivChar_borromean {R : Type*} [Field R] (q : R) (hq : q ≠ 0) :
    (q * q⁻¹) ^ 3 = 1 := by
  rw [mul_inv_cancel₀ hq, one_pow]

/-- Character of the sign (antisymmetric) 1-dim rep on the Borromean braid,
    `σᵢ ↦ −q⁻¹`: `((−q⁻¹)·(−q⁻¹)⁻¹)³ = 1`. -/
theorem signChar_borromean {R : Type*} [Field R] (q : R) (hq : q ≠ 0) :
    ((-q⁻¹) * (-q⁻¹)⁻¹) ^ 3 = 1 := by
  rw [mul_inv_cancel₀ (neg_ne_zero.mpr (inv_ne_zero hq)), one_pow]

/-- **The two transpose-paired 1-dim blocks carry the SAME Borromean character.**  So
    `m_{(3)}` and `m_{(1,1,1)}` differ only by their Markov weights: the off-block
    `B = (m_{(3)} − m_{(1,1,1)})/2` is `(w_{(3)} − w_{(1,1,1)})/2`, a pure *weight*
    difference (bar-odd, Part 5). -/
theorem borromean_chars_equal {R : Type*} [Field R] (q : R) (hq : q ≠ 0) :
    (q * q⁻¹) ^ 3 = ((-q⁻¹) * (-q⁻¹)⁻¹) ^ 3 := by
  rw [trivChar_borromean q hq, signChar_borromean q hq]

/-! ### Part 2 — the derived off-blocks (transpose-eigenbasis rotation of the
self-adjoint mass endomorphism). -/

/-- Off-diagonal super-block numerator from the transpose-involution eigenbasis
    rotation of the self-adjoint mass endomorphism `diag(a, c, b)` on the `(3)↔(1,1,1)`
    2-cycle.  The physical off-block is `B = C = (a − b)/2`; the common `/2` (a fixed
    orthogonal-rotation normalization) **cancels** in the even-face magnitude ratio, so
    it is dropped here — `offBlock a b = a − b`.  (The self-conjugate `(2,1)` block is
    transpose-fixed and decouples from the off-block.)  `a = m_{(3)}`, `b = m_{(1,1,1)}`
    are the branching block contributions — the derivation fixes `B`; it is NOT free
    (contrast Route 2). -/
def offBlock {R : Type*} [Field R] (a b : R) : R := a - b

/-- Odd diagonal super-block `D` (physical `D = (a+b)/2`; the `/2` cancels in the ratio,
    so `oddDiag a b = a + b`), coincident with the even `e₊` `(2,2)`-entry `A` under the
    symmetric rotation. -/
def oddDiag {R : Type*} [Field R] (a b : R) : R := a + b

/-- The Berezinian cross-term `t = B·D⁻¹·C` assembled from the derived branching
    off-blocks (`B = C = offBlock`, `D = oddDiag`), in the `/2`-cancelled normalization. -/
def crossTerm {R : Type*} [Field R] (a b : R) : R :=
  offBlock a b * (oddDiag a b)⁻¹ * offBlock a b

/-- The even-face magnitude factor `(A − t)/A` on the bar-even mass/C1 (`e₊`) face,
    where `A = D = oddDiag` is the even `(2,2)`-entry: the factor by which the full
    Berezinian face rescales the naive block-diagonal single-trace value.  The `/2`
    normalization cancels in `(A − t)/A`, so this factor is normalization-independent. -/
def magnitudeFactor {R : Type*} [Field R] (a b : R) : R :=
  (oddDiag a b - crossTerm a b) / oddDiag a b

/-- **The derived even-face factor is `1 − ((a−b)/(a+b))²` (sorry-free).**  Pure
    Schur-complement algebra: `t = (a−b)²/(a+b)`, `A = a+b`, so
    `(A − t)/A = 1 − ((a−b)/(a+b))²` (the physical `/2` normalization cancels).  This is
    the *derivation's* output — the off-block is pinned, the factor is a fixed function
    of the two branching block values. -/
theorem magnitudeFactor_eq {R : Type*} [Field R] (a b : R) (hab : a + b ≠ 0) :
    magnitudeFactor a b = 1 - ((a - b) / (a + b)) ^ 2 := by
  unfold magnitudeFactor crossTerm offBlock oddDiag
  field_simp

/-! ### Part 3 — the structural exclusion (scope-(b), invariant = square
non-negativity). -/

/-- **THE STRUCTURAL EXCLUSION (scope-(b), invariant cited: `sq_nonneg`).**  The
    branching-derived even-face magnitude factor is `≤ 1` for ALL real diagonal blocks
    `a, b` with `a + b ≠ 0`: it is `1` minus a real square.  The self-adjoint
    Hecke/Wedderburn branching Schur complement is a **REDUCTION**, never a lift —
    independent of the sign of `a+b` (the square erases it).  This is the categorical
    content of "every single-Markov-trace ingredient is bracketed *short*": the
    branching correction can only shrink, never enlarge, the naive value. -/
theorem magnitudeFactor_le_one {R : Type*} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] (a b : R) (hab : a + b ≠ 0) :
    magnitudeFactor a b ≤ 1 := by
  rw [magnitudeFactor_eq a b hab]
  have h := sq_nonneg ((a - b) / (a + b))
  linarith

/-- **The observed A=3 lift `r* ≈ 1.585 > 1` is UNREACHABLE by the branching Schur
    complement (sorry-free).**  For any target `r > 1` — the observed `r* = μ₃/c₃`
    and the whole Route-5 acceptance band `[1.50, 1.71]` — the branching-derived
    magnitude factor never equals `r`.  A genuine *enhancement* is structurally outside
    the self-adjoint branching route; the lift must come from the anti-self-adjoint
    (GGM/Stokes) off-block the branching leaves free. -/
theorem observed_lift_unreachable {R : Type*} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] (a b : R) (hab : a + b ≠ 0) (r : R) (hr : 1 < r) :
    magnitudeFactor a b ≠ r := by
  intro h
  have hle := magnitudeFactor_le_one a b hab
  rw [h] at hle
  linarith

/-! ### Part 5 — the parity certificate: WHY the branching assembly is self-adjoint
(hence bar-even cross-term, hence the `≤ 1` bound). -/

/-- **The branching off-block numerator `a − b` is bar-ODD** when the two 1-dim blocks
    are bar-conjugate (`b = σ a`).  The trivial/sign Markov weights ARE `q↔q⁻¹`
    conjugate (transpose-paired blocks with equal Borromean characters, Part 1), so
    `b = σ a` is the branching datum, threaded explicitly.  Result: `σ(a−b) = −(a−b)`,
    matching the bar-ODD odd-face weight of `OddDecayWeightParity`. -/
theorem offBlockNum_bar_odd {R : Type*} [CommRing R] (σ : R →+* R)
    (a b : R) (hinv : ∀ x, σ (σ x) = x) (hconj : b = σ a) :
    σ (a - b) = -(a - b) := by
  subst hconj
  rw [map_sub, hinv a]
  ring

/-- **The branching super-matrix is graded self-adjoint** (`C = −σ B`).  The two
    branching off-blocks are equal (`B = C`, symmetric real rotation) and bar-ODD
    (`σ B = −B`, from `offBlockNum_bar_odd`), so `−σ B = −(−B) = B = C`.  This is
    exactly the hypothesis of `BerezinianSelfAdjointCrossTerm.selfadjoint_crossTerm_bar_even`
    ⇒ the cross-term is bar-EVEN.  Bar-even is the CORRECT parity for the ratio
    `r* = μ₃/c₃` (both moments bar-even), yet the magnitude is provably bounded `≤ 1`
    (Part 3): the branching supplies the right parity but the wrong *sign of
    correction*. -/
theorem branching_graded_selfadjoint {R : Type*} [CommRing R] (σ : R →+* R)
    (B C : R) (hBC : C = B) (hodd : σ B = -B) : C = -σ B := by
  rw [hBC, hodd, neg_neg]

/-! ### Part 6 — the OPEN closure, as an honest §3b dependent conjecture (no instance).

The lift `r* > 1` is structurally excluded from the self-adjoint branching route
(Part 3), so it must be carried by an **anti-self-adjoint** (`C ≠ −σ B`, two independent
amplitudes) off-block **derived from the geometry** (the DM q-cubic / GGM Stokes datum,
`conj:qdifference-kernel-prolongation-symbol`, bean `qou-jqof`) rather than tuned to the
target.  We record that open state as a content-bearing dependent conjecture class with
**NO instance** — the honest "the framework does not yet derive the anti-self-adjoint
off-block" wall. -/

/-- **§3b dependent conjecture — the A=3 lift closes via a DERIVED anti-self-adjoint
    off-block.**

    `@conjecture: dependent` (its content depends on the open geometric derivation of
    the anti-self-adjoint off-block — `conj:qdifference-kernel-prolongation-symbol` /
    the `qou-jqof` wall — supplying `B_geom, C_geom`).

    The claim: geometrically-derived off-blocks `B_geom, C_geom` (INPUTS from the DM
    q-cubic, independent of the physical target) (i) **break** graded self-adjointness
    (`C_geom ≠ −(σ B_geom)`, the anti-self-adjoint amplitude the self-adjoint branching leaves
    free) and (ii) drive the even-face correction to a physical **lift** `κ_phys > 1`
    (unreachable by the self-adjoint branching Schur complement, `magnitudeFactor_le_one`).

    **Why this is content-bearing and NOT a fit.**  In a *fit* `B` is solved from
    `κ_phys` (Route 2's `crossTerm_magnitude_surjective`).  Here `B_geom, C_geom` are
    *given* geometric inputs and the equation is a nontrivial *check* that the geometry
    lands the physics — false for generic off-blocks, and the strict inequality
    `1 < κ_phys` cannot even hold for the *self-adjoint* branching value (Part 3).
    **No instance is supplied**: deriving `B_geom, C_geom` IS the open keystone;
    discharging this by *choosing* them to hit `κ_phys` would be the forbidden fit and
    is explicitly not done. -/
class A3LiftFromDerivedOffBlock {R : Type*} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] (σ : R →+* R) (A B_geom C_geom D_geom κ_phys : R) : Prop where
  /-- The geometrically-derived off-blocks BREAK graded self-adjointness — they are the
      anti-self-adjoint (GGM/Stokes) amplitude the branching leaves free.  The bar
      involution `σ` is quantified as a genuine ring homomorphism applied to `B_geom`;
      the self-adjoint reference value of `C_geom` is `−(σ B_geom)`. -/
  anti_self_adjoint : C_geom ≠ -(σ B_geom)
  /-- The derived (not fitted) off-blocks drive the even-face correction to the physical
      **lift** `κ_phys`, which strictly EXCEEDS `1` — an enhancement provably outside the
      self-adjoint branching route (`magnitudeFactor_le_one`). -/
  geom_gives_lift :
    (A - B_geom * D_geom⁻¹ * C_geom) / A = κ_phys ∧ 1 < κ_phys

end QOU.QBeta.A3OffBlockDerivation
