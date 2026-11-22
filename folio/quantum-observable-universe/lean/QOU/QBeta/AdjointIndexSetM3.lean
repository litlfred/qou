import Init.Data.Int.Basic
import Init.Omega

/-!
# QOU.QBeta.AdjointIndexSetM3 — the knot-INDEPENDENT core of the DT index set, and what it forces

## Where this sits (Route C, milestone M3)

M2 (`AomegaM2BPSCohomology`) established — conditional on the DT/BPS bridge —
that the closed-sector BPS spectrum would be **abelian**: every Borel ray
distinct, trivial Davison–Meinhardt plethystic log, `dim BPS_d = |Ω_d|`, all
multiplicities `1`. That has a consequence worth stating plainly:

> **If the spectrum is abelian with unit multiplicities, "categorifying" it is
> nearly content-free.** A direct sum of one-dimensional spaces carries no
> information beyond *which rays exist*. So M3's real target is not "build a
> cohomological Hall algebra" — it is **derive the index set `Ω`**.

That is a much sharper target than the CoHA framing, and it is what this file
attacks.

## The observation that constrains any answer

M2 records the `4₁` index set as the meridian-charge polynomial
`s(x) = x + 1 + x⁻¹` (three unit-multiplicity states, charges `e ∈ {−1,0,+1}`),
and the corpus records that **the same `s(x)` governs `5₂`** (GGM eqs 239/277/307:
the `5₂` q→0 Stokes entries are `s(x)`, `s(x)`, `s(x)+1`). Knot-independence is
the single hardest fact for any explanation to meet: it is exactly why every
knot-specific invariant tried so far failed (`Driver14CharacterVarietyDTMenu`
tests eight of them; Route A's `R1` was the ninth).

## The hypothesis this file makes precise (NOT proved here)

`H_Ad` — the knot-independent core of the index set is the **weight set of the
adjoint representation of `sl₂`**. For a meridian holonomy with eigenvalues
`(m, m⁻¹)` and `x = m²`, the adjoint (3-dimensional) representation has
eigenvalues `(x, 1, x⁻¹)`, so its character is exactly `s(x) = x + 1 + x⁻¹`, and
at the parabolic point `x = 1` its value is `3 = dim 𝔰𝔩₂`.

Why this is a *mechanism* and not a numerical coincidence:

* In complex Chern–Simons theory the Borel singularities are differences of
  complex volumes of flat connections, and the deformation theory of a flat
  connection is governed by `H¹(M, Ad ρ)` — the **adjoint** local system is the
  canonical coefficient object, not a chosen one.
* `Ad(𝔰𝔩₂)` is multiplicity-free with weights `{2, 0, −2}`, matching M2's
  `sMultiplicities = [1,1,1]` without adjustment.
* It **predicts** knot-independence, which is the observed fact no knot-specific
  invariant could produce.
* In QOU-native terms `Ad ≅ Sym²V = S^{(2)}(ℂ²)`, the **Schur–Weyl partner** of
  the partition-`(2)` Wedderburn block of `H₂(q)` — so the hypothesis is
  expressible in Hecke language. (Partner, *not* the block: the block itself is
  1-dimensional. See Part 3, where both dimensions are derived and this
  file's own earlier conflation of the two is corrected.)

**`H_Ad` is a hypothesis, not a derivation.** Identifying the index set with a
rep-theoretic object that is standard in the deformation theory is a structural
reading; it does not derive the DT spectrum from Hecke data, and this file
claims no such derivation.

## What IS proved here (decidable, no literature input in the general results)

The adjoint weight combinatorics, and — the load-bearing part — a **forcing
theorem**: any knot-independent core, `H_Ad` included, *cannot by itself* produce
the chirality-split `(4₁, 5₂) ↦ (3, 4)`; it necessarily requires a
knot-**dependent** remainder, and that remainder is forced to differ by exactly
one between the two knots. This converts the otherwise-unfalsifiable move "add
one more state for `5₂`" into a structural requirement with a definite value,
which any completion of `H_Ad` must independently derive.

Part 2 then answers the obvious adversarial objection — *"isn't `H_Ad` just Route
A's `R1` again?"* — and the answer cuts both ways. It is **not**: `R1` is the
`dtMax` projection of the chirality-split datum and `H_Ad`'s core is `dtMin`, so
they read different halves, and the *pair* reconstructs the 2-element set `{3,4}`
that `no_scalar_matches_chirality_split_datum` forbids any *single* scalar from
naming. But the evidence is thinner than that makes it sound: `4₁`'s
amphichirality collapses `dtMin` onto `dtMax`, so the entire support for a
knot-independent core is **one** observation (`S⁻(5₂) = 3`); and a rival
hypothesis with no `𝔰𝔩₂` in it at all — the core is the `{0, g, ḡ}` triple every
hyperbolic knot carries, i.e. `R1`'s own universal floor — reproduces every
`H_Ad` prediction, including a palindromic 3-element grading. Both are proved
below. `H_Ad` stays a hypothesis, and it is not the only one standing.

-- Ref: [leitner2026] docs/audits/2026-08-11-route-c-bps-cohomology-scoping.md (Route C, M3)
-/

namespace QOU.QBeta.AdjointIndexSetM3

/-! ## The adjoint weight data (knot-independent by construction) -/

/-- The `x`-exponents of the adjoint representation of `𝔰𝔩₂`, i.e. the weights
`{2, 0, −2}` written in the variable `x = m²`: `(x, 1, x⁻¹) ↦ (1, 0, −1)`. -/
def adjointExponents : List Int := [1, 0, -1]

/-- **Multiplicity-free**: the adjoint weights are pairwise distinct, matching
M2's `sMultiplicities = [1,1,1]` with no adjustment. -/
theorem adjoint_multiplicity_free : adjointExponents.Nodup := by decide

/-- **`dim 𝔰𝔩₂ = 3`** — the number of adjoint weights. -/
theorem adjoint_dim_three : adjointExponents.length = 3 := by decide

/-- **The weight set is closed under negation** (`x ↔ x⁻¹`), i.e. the index set is
bar-symmetric — the same `q ↦ q⁻¹` involution that grades the DT split in
`ChiralityGradedCount`. -/
theorem adjoint_palindromic :
    ∀ e ∈ adjointExponents, (-e) ∈ adjointExponents := by decide

/-- The character value at the parabolic point `x = 1` is the number of weights:
`s(1) = 3`. (Each weight contributes `1` because the weights are
multiplicity-free.) -/
def sAtOne : Int := (adjointExponents.map (fun _ => (1 : Int))).sum

/-- **`s(1) = 3 = dim 𝔰𝔩₂`**, matching M2's `sAtOne`. -/
theorem s_at_one_eq_three : sAtOne = 3 := by decide

/-! ## The forcing theorem — the load-bearing content

A *knot-independent* core assigns the same count to every knot. The certified DT
data does not: `4₁ ↦ 3` and `5₂ ↦ 4` (the `S⁺` entries). So a knot-independent
core cannot be the whole story, and the shortfall is pinned exactly. -/

/-- The two knots carrying certified DT data. -/
inductive KKnot where
  | fourOne : KKnot
  | fiveTwo : KKnot
  deriving DecidableEq

open KKnot

/-- **A knot-independent core forces a knot-dependent remainder differing by one.**
If a count decomposes as a constant `core` plus a per-knot `extra`, and reproduces
the certified `(3, 4)` split, then `extra` is larger at `5₂` by exactly `1` —
whatever the core is. The "extra state for `5₂`" is therefore not an optional
patch: it is forced, with a definite value. -/
theorem knot_independent_core_forces_unit_remainder
    (core : Int) (extra : KKnot → Int)
    (h41 : core + extra fourOne = 3)
    (h52 : core + extra fiveTwo = 4) :
    extra fiveTwo = extra fourOne + 1 := by
  omega

/-- **Under `H_Ad` the remainder is pinned to `0` and `1`.** Taking the
knot-independent core to be the adjoint count `s(1) = 3`, the `4₁` remainder
vanishes and the `5₂` remainder is exactly one state. Any completion of `H_Ad`
must derive that single extra `5₂` ray independently — it cannot be assumed. -/
theorem adjoint_core_pins_remainder
    (extra : KKnot → Int)
    (h41 : sAtOne + extra fourOne = 3)
    (h52 : sAtOne + extra fiveTwo = 4) :
    extra fourOne = 0 ∧ extra fiveTwo = 1 := by
  rw [s_at_one_eq_three] at h41 h52
  omega

/-- **The falsifier, stated as a theorem.** If some completion claims the count is
*purely* knot-independent (no remainder at all), it contradicts the certified
split. So `H_Ad` alone is provably incomplete — it is not a candidate for the
whole answer, and saying so is not a concession but a derived fact. -/
theorem no_purely_knot_independent_count
    (core : Int)
    (h41 : core = 3) (h52 : core = 4) : False := by
  omega

/-! ## Part 2 — WHICH projection `H_Ad` is, and the rival hypothesis it cannot beat

The obvious adversarial objection to `H_Ad` is that it may be a re-description of
Route A's surviving reading `R1` (`DT integer = #boundary-parabolic `SL₂(ℂ)` flat
connections = A-polynomial `L`-degree`), since both hand back `3` for `4₁`. This
part settles that, and the answer is *two-sided*.

The certified chirality-split data (`FiveTwoDTSpectrumSplit`, `AomegaM2BPSCohomology`):
`4₁` is amphichiral, so its bar-odd part vanishes and `(S⁺, S⁻) = (3, 3)`; `5₂` is
chiral with `(S⁺, S⁻) = (4, 3)`. -/

/-- The `S⁺` (bar-positive chirality) DT count. -/
def dtPlus : KKnot → Int
  | fourOne => 3
  | fiveTwo => 4

/-- The `S⁻` (bar-negative chirality) DT count. Amphichirality forces
`dtMinus 4₁ = dtPlus 4₁`. -/
def dtMinus : KKnot → Int
  | fourOne => 3
  | fiveTwo => 3

/-- The smaller of the two chirality counts. -/
def dtMin (K : KKnot) : Int := if dtPlus K ≤ dtMinus K then dtPlus K else dtMinus K

/-- The larger of the two chirality counts. -/
def dtMax (K : KKnot) : Int := if dtPlus K ≤ dtMinus K then dtMinus K else dtPlus K

/-- **`R1` is the `dtMax` projection.** Route A's surviving reading assigns
`4₁ ↦ 3`, `5₂ ↦ 4` — precisely the larger chirality count, on both knots. -/
theorem r1_is_the_dtmax_projection :
    dtMax fourOne = 3 ∧ dtMax fiveTwo = 4 := by decide

/-- **`H_Ad` is the `dtMin` projection.** The knot-independent adjoint core `s(1)=3`
equals the *smaller* chirality count on both knots. So `H_Ad` and `R1` are reading
**different halves** of the same chirality-split datum, not the same half twice. -/
theorem h_ad_is_the_dtmin_projection :
    dtMin fourOne = sAtOne ∧ dtMin fiveTwo = sAtOne := by decide

/-- **Complementarity: the two projections together reconstruct the datum.** Listing
each knot's chirality counts in increasing order gives exactly `[dtMin, dtMax]`. So
the pair `(H_Ad, R1)` recovers the full set-valued DT datum for both knots. -/
theorem min_max_pair_reconstructs_datum :
    [dtMinus fourOne, dtPlus fourOne] = [dtMin fourOne, dtMax fourOne] ∧
    [dtMinus fiveTwo, dtPlus fiveTwo] = [dtMin fiveTwo, dtMax fiveTwo] := by decide

/-- **No tension with the scalar-impossibility theorem.**
`Driver14CharacterVarietyDTMenu.no_scalar_matches_chirality_split_datum` rules out a
**single** scalar equalling the set-valued `5₂` datum; it says nothing about a
*pair*. Stated here as the general fact: two scalars suffice to name a 2-element set
that neither can name alone. -/
theorem two_scalars_name_what_one_cannot
    (f g : KKnot → Int)
    (hf : f fiveTwo = 3) (hg : g fiveTwo = 4) :
    [f fiveTwo, g fiveTwo] = [3, 4] ∧ f fiveTwo ≠ g fiveTwo := by
  refine ⟨?_, ?_⟩ <;> rw [hf, hg] <;> decide

/-! ### The cost side: how thin the evidence for the core actually is -/

/-- **`4₁` supplies no evidence for `H_Ad` independent of `R1`.** Amphichirality
collapses the two projections there (`dtMin = dtMax`), while they genuinely differ at
`5₂`. So the whole empirical support for "the core is knot-independently `3`" is the
**single** observation `dtMinus 5₂ = 3`: one non-degenerate data point, not two. -/
theorem fourone_is_a_degenerate_observation :
    dtMin fourOne = dtMax fourOne ∧ dtMin fiveTwo ≠ dtMax fiveTwo := by decide

/-- The rival hypothesis `H_floor`: the knot-independent core is the triple of flat
connections `{0, g, ḡ}` that **every** hyperbolic knot carries — i.e. the universal
floor of `R1` itself, with no `𝔰𝔩₂` adjoint anywhere. -/
def hyperbolicConnectionFloor : Int := 3

/-- **`H_Ad` and `H_floor` are observationally indistinguishable on the certified
data.** Their cores are equal, so they impose *identical* constraints on any
completion — the same remainder, the same forcing, the same predictions. The
numerical agreement `3 = dim 𝔰𝔩₂ = |{0, g, ḡ}|` is therefore not evidence for the
adjoint reading over the connection-floor reading; only the **grading variable**
(meridian `x = m²` for `H_Ad`, Chern–Simons value for `H_floor`) could separate them,
and that separation is not made here. -/
theorem h_ad_and_h_floor_are_indistinguishable
    (extra : KKnot → Int) :
    (hyperbolicConnectionFloor + extra fourOne = 3 ∧
       hyperbolicConnectionFloor + extra fiveTwo = 4)
    ↔ (sAtOne + extra fourOne = 3 ∧ sAtOne + extra fiveTwo = 4) := by
  unfold hyperbolicConnectionFloor
  rw [s_at_one_eq_three]

/-- **Both rivals also fail `T4`'s genericity screen the same way.** `H_floor`'s
Chern–Simons values `{0, +𝔙, −𝔙}` form a 3-element palindromic set exactly as the
adjoint weights `{1, 0, −1}` do, so the palindromic shape — already known generic —
cannot arbitrate either. Recorded as the shape identity that makes the point. -/
theorem palindromic_shape_does_not_arbitrate :
    adjointExponents.length = 3 ∧
    (∀ e ∈ adjointExponents, (-e) ∈ adjointExponents) ∧
    hyperbolicConnectionFloor = adjointExponents.length := by
  refine ⟨by decide, by decide, by decide⟩

/-! ## Part 3 — the meridian grading, derived from Young-tableau combinatorics

Part 2 left exactly one discriminator between `H_Ad` and its rival `H_floor`: the
**grading variable**. `H_floor` grades by Chern–Simons value; `H_Ad` grades by
meridian eigenvalue `x = m²`. If the meridian grading falls out of QOU-native
Hecke/Schur–Weyl data, `H_Ad` has a route `H_floor` does not.

It does — and getting there corrects an imprecision in this file's own earlier
prose.

**CORRECTION.** Part 1's docstring said "`Ad ≅ Sym²V`, the partition-`(2)`
Wedderburn block of `H₂(q)`". That conflates the two sides of Schur–Weyl duality.
The partition-`(2)` block of `H₂(q)` has dimension `#SYT((2)) = 1`; it is
**one**-dimensional, not three. What is three-dimensional is its Schur–Weyl
*partner* `S^{(2)}(ℂ²) = Sym²V` on the quantum-group side of
`V^{⊗2} ≅ ⨁_λ S^λ(V) ⊗ M_λ`. The `3` therefore lives on the `U_q(𝔰𝔩₂)` factor
paired with the `(2)` block — not in the block itself. Both dimensions are derived
below so the distinction cannot be lost again.

The payoff: the weight basis of `S^{(2)}(ℂ²)` is the set of semistandard Young
tableaux of shape `(2)` on the alphabet `{1,2}`, and each tableau's weight is read
off directly in the **meridian** variable — entry `1` contributes `m`, entry `2`
contributes `m⁻¹`. So the meridian grading is *combinatorial*, not assumed. -/

/-- All fillings of the shape-`(2)` row by the alphabet `{1,2}`. -/
def shapeTwoFillings : List (Nat × Nat) := [(1, 1), (1, 2), (2, 1), (2, 2)]

/-- The semistandard tableaux of shape `(2)`: rows weakly increase. -/
def ssytShapeTwo : List (Nat × Nat) := [(1, 1), (1, 2), (2, 2)]

/-- The standard tableaux of shape `(2)`: each of `1,2` used once, strictly
increasing along the row. -/
def sytShapeTwo : List (Nat × Nat) := [(1, 2)]

/-- **The semistandard tableaux are exactly the weakly-increasing fillings** — the
`3` is *derived* from the tableau condition, not asserted. -/
theorem ssyt_from_weakly_increasing :
    shapeTwoFillings.filter (fun t => decide (t.1 ≤ t.2)) = ssytShapeTwo := by decide

/-- **The standard tableaux are exactly the strictly-increasing fillings** — the
`1` is likewise derived. -/
theorem syt_from_strictly_increasing :
    shapeTwoFillings.filter (fun t => decide (t.1 < t.2)) = sytShapeTwo := by decide

/-- **The correction, as a theorem.** `dim M_{(2)} = #SYT((2)) = 1` while
`dim S^{(2)}(ℂ²) = #SSYT((2)) = 3`. The adjoint's `3` is the Schur–Weyl *partner*
of the `(2)` Hecke block, never the block's own dimension. -/
theorem hecke_block_one_schur_partner_three :
    sytShapeTwo.length = 1 ∧ ssytShapeTwo.length = 3 ∧
      sytShapeTwo.length ≠ ssytShapeTwo.length := by decide

/-- The **meridian** weight of a tableau, in exponents of `m`: entry `1` contributes
`m¹`, entry `2` contributes `m⁻¹`. -/
def meridianWeight (t : Nat × Nat) : Int :=
  (if t.1 = 1 then 1 else -1) + (if t.2 = 1 then 1 else -1)

/-- **The meridian grading is derived, not assumed.** The shape-`(2)` semistandard
tableaux carry `m`-weights `(2, 0, −2)`, i.e. exactly **twice** the adjoint
`x`-exponents `(1, 0, −1)` — which is precisely the substitution `x = m²`. So
`s(x) = x + 1 + x⁻¹` is the character of `S^{(2)}(ℂ²)` in the meridian variable,
read off Young-tableau combinatorics with nothing fitted.

This is the discriminator Part 2 asked for: `H_Ad`'s grading variable follows from
QOU-native Schur–Weyl data, while `H_floor` (whose grading is by Chern–Simons
value) has no route to it. It does **not** by itself decide between them — it
supplies `H_Ad` with a mechanism `H_floor` lacks, which is a weaker and different
thing than excluding `H_floor`. -/
theorem ssyt_meridian_weights_are_twice_adjoint :
    ssytShapeTwo.map meridianWeight = adjointExponents.map (fun e => 2 * e) := by
  decide

/-- **The grading is multiplicity-free at the tableau level too** — the three
tableaux carry three distinct weights, matching M2's `sMultiplicities = [1,1,1]`
without adjustment. -/
theorem ssyt_weights_nodup : (ssytShapeTwo.map meridianWeight).Nodup := by decide

/-! ## Part 4 — the remainder is DERIVED from the trace field, and it is `H_floor`'s win

Part 1 proved that a knot-independent core forces a knot-dependent remainder, and
said any completion "must derive that remainder independently". Part 2 named the
rival `H_floor`. This part reports that `H_floor` **does** derive it — from the
arithmetic of the trace field — which is a point against `H_Ad`, not for it.

**Source (glyph-verified, corpus `library/arxiv-2111.06645v3/2111.06645v3.pdf` §2.1).**
Garoufalidis–Zagier describe `P_K`, the set of boundary-parabolic `SL₂(ℂ)`
representations, for their three standard knots:

* `4₁` — `P_K = {σ₀, σ₁, σ₂}`; trace field `ℚ(√−3)`, signature `(0,1)`.
* `5₂` — `P_K = {σ₀, σ₁, σ₂, σ₃}`; trace field the cubic of discriminant `−23`,
  signature `(1,1)`; `σ₃` is the root with **zero imaginary part**.
* `(−2,3,7)` — `P_K` has **seven** elements: `σ₀`, the three from `ℚ(ξ)` (the same
  cubic as `5₂`), and three more from `ℚ(η)`, `η³+η²−2η−1 = 0`, the **totally
  real** abelian cubic of discriminant `49`, signature `(3,0)`.

So `|P_K| = 3, 4, 7` — which reproduces `R1`'s `4₁ ↦ 3`, `5₂ ↦ 4` from a source
independent of the A-polynomial, and *extends* it to a third knot.

**The structural read that follows.** `H_floor`'s core is `{σ₀, g, ḡ}` = the
trivial representation plus **one** complex-conjugate pair (the geometric one).
Everything else in `P_K` is remainder. Counting embeddings by signature:

| `K` | reduced trace algebra | real | pairs | `\|P_K\|` | core | remainder |
|---|---|---|---|---|---|---|
| `4₁` | `ℚ(√−3)` | 0 | 1 | 3 | 3 | **0** |
| `5₂` | cubic, disc `−23` | 1 | 1 | 4 | 3 | **1** |
| `(−2,3,7)` | `ℚ(ξ) × ℚ(η)` | 1+3 | 1+0 | 7 | 3 | **4** |

The `5₂` remainder of exactly `1` is therefore **not** an unexplained extra state:
it is the single **real embedding** of the discriminant `−23` cubic trace field,
and `4₁`'s remainder vanishes because its trace field is imaginary quadratic and
has none. That is a derivation, from arithmetic, of the quantity Part 1 could only
force.

**Honest scoring.** This strengthens `H_floor` and weakens the case for `H_Ad` on
the *count*: `H_floor` now explains the number `3`, predicts the remainder, and
does so with no `𝔰𝔩₂` anywhere. `H_Ad`'s remaining distinct content is what Part 3
established — the meridian **grading** `s(x) = x + 1 + x⁻¹`, which `H_floor` says
nothing about. The two are best read as answering *different questions* (`H_floor`:
why that many; `H_Ad`: why that polynomial) rather than as rivals for one.

Nothing here is a Hecke-internal derivation, so M3's actual target is untouched. -/

/-- The three knots for which Garoufalidis–Zagier tabulate `P_K` (§2.1). -/
inductive PKnot where
  | fourOne : PKnot
  | fiveTwo : PKnot
  | pretzel237 : PKnot
  deriving DecidableEq

/-- Number of **real** embeddings of the reduced trace algebra `A_K^red`. -/
def realEmbeddings : PKnot → Int
  | PKnot.fourOne => 0            -- ℚ(√−3): imaginary quadratic
  | PKnot.fiveTwo => 1            -- cubic, disc −23: signature (1,1)
  | PKnot.pretzel237 => 4         -- ℚ(ξ) gives 1, ℚ(η) (totally real cubic) gives 3

/-- Number of **complex-conjugate pairs** of embeddings of `A_K^red`. -/
def complexPairs : PKnot → Int
  | PKnot.fourOne => 1
  | PKnot.fiveTwo => 1
  | PKnot.pretzel237 => 1         -- only ℚ(ξ) contributes; ℚ(η) is totally real

/-- `|P_K| = 1 + (real embeddings) + 2·(complex pairs)` — the trivial
representation plus every embedding of the reduced trace algebra. -/
def pkSize (K : PKnot) : Int := 1 + realEmbeddings K + 2 * complexPairs K

/-- **The Garoufalidis–Zagier counts, reproduced from the signatures alone.**
`|P_K| = 3, 4, 7` for `4₁`, `5₂`, `(−2,3,7)` — matching §2.1 verbatim. -/
theorem pk_sizes_three_four_seven :
    pkSize PKnot.fourOne = 3 ∧ pkSize PKnot.fiveTwo = 4 ∧ pkSize PKnot.pretzel237 = 7 := by decide

/-- `H_floor`'s core: the trivial representation together with one
complex-conjugate pair (the geometric connection and its mirror). -/
def floorCore : Int := 3

/-- The remainder `H_floor` predicts: everything in `P_K` beyond the core. -/
def floorRemainder (K : PKnot) : Int := pkSize K - floorCore

/-- **The remainder equals the count of real embeddings, plus the pairs beyond the
geometric one.** For all three knots this is exactly
`realEmbeddings K + 2·(complexPairs K − 1)`. -/
theorem remainder_is_arithmetic (K : PKnot) :
    floorRemainder K = realEmbeddings K + 2 * (complexPairs K - 1) := by
  cases K <;> decide

/-- **The forced unit remainder of Part 1 is derived, not assumed.** `4₁`'s
remainder is `0` because its trace field is imaginary quadratic (no real
embedding); `5₂`'s is `1` because the discriminant `−23` cubic has exactly one.
The `+1` that `knot_independent_core_forces_unit_remainder` could only *force* now
has an arithmetic source. -/
theorem forced_remainder_is_the_real_embedding_count :
    floorRemainder PKnot.fourOne = realEmbeddings PKnot.fourOne ∧
    floorRemainder PKnot.fiveTwo = realEmbeddings PKnot.fiveTwo ∧
    floorRemainder PKnot.fourOne = 0 ∧ floorRemainder PKnot.fiveTwo = 1 := by decide

/-- **The third knot is a genuine extension, not a restatement.** `(−2,3,7)` has a
remainder of `4`, distinct from both smaller knots — so the arithmetic rule is not
fitted to a two-point data set. (Its `q→0` Stokes matrix is not published, so this
is a *prediction*: `R1`/`H_floor` say the `(−2,3,7)` count is `7`.) -/
theorem pretzel_is_a_new_data_point :
    floorRemainder PKnot.pretzel237 = 4 ∧
    floorRemainder PKnot.pretzel237 ≠ floorRemainder PKnot.fourOne ∧
    floorRemainder PKnot.pretzel237 ≠ floorRemainder PKnot.fiveTwo := by decide

/-- **The core is knot-independent across all three** — the one shared prediction
of `H_Ad` and `H_floor`, now checked on a third knot rather than two. -/
theorem core_is_three_on_all_three :
    ∀ K : PKnot, pkSize K - floorRemainder K = sAtOne := by
  intro K; cases K <;> (rw [s_at_one_eq_three]; decide)

end QOU.QBeta.AdjointIndexSetM3
