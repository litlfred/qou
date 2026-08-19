import QOU.QBeta.AdjointIndexSetM3

/-!
# QOU.QBeta.GZThirdKnotRankGrading — the third knot's rank grading: a GZ erratum, an object-identity guard, and an S₃ block decomposition

## Why this file exists

Route C M3 (`AdjointIndexSetM3`) left one live question: `H_Ad` claims the
knot-independent core of the DT index set is the multiplicity-free `𝔰𝔩₂` adjoint
weight set, `s(x) = x + 1 + x⁻¹`. The stated way to break it was a **rank-6 knot**
whose grading is *not* multiplicity-free.

Garoufalidis–Zagier, *Knots and Their Related q-Series* (SIGMA 19 (2023) 082,
`uploads/2304.09377v2.pdf`) — the sequel `[44]` that
`uploads/2111.06645v3.pdf` announces — supplies exactly such a knot: the
`(−2,3,7)` pretzel, where §3.5 reports **"a new phenomenon… the weight spaces
have higher multiplicity."**

That looks like the refutation. **It is not**, and Part B below is the guard that
says why. Recording the near-miss is the point: the two gradings agree on `4₁`'s
*total* only by coincidence, and conflating them would have retired a hypothesis
on the strength of a different object.

-- Ref: [manuscript] uploads/2304.09377v2.pdf §3.4, §3.5 (Garoufalidis–Zagier)
-- Ref: [manuscript] uploads/2111.06645v3.pdf §2.1 (Garoufalidis–Zagier)
-- Ref: [manuscript] docs/audits/2026-08-11-route-c-bps-cohomology-scoping.md §6
-/

namespace QOU.QBeta.GZThirdKnotRankGrading

open QOU.QBeta.AdjointIndexSetM3

/-! ## Part A — the `(−2,3,7)` weight data, and an internal contradiction in the source

Three statements in §3.5, quoted:

1. **Prose**: *"there are weights 0, 1 and 2 with dimensions **1, 4 and 1**,
   respectively."*
2. **Explicit decomposition**: `⟨h⟩ = W₀ ⊕ W₁ ⊕ W₂` with
   `W₀ = ⟨H₀, H₃, H₄, H₅⟩`, `W₁ = ⟨H₁⟩`, `W₂ = ⟨H₂⟩`.
3. **ε-deformation degrees**: `(δ₀,…,δ₅) = (0,1,2,0,0,0)`; and the companion
   weight vector `(−1, 0, 1, −1, −1, −1)` on `h = (h_j)`.

Statements 2 and 3 agree with each other and give `(4, 1, 1)`. Statement 1 gives
`(1, 4, 1)`. Two independent internal statements against one: **the prose has its
first two dimensions transposed.** Adjudicated below rather than guessed. -/

/-- The ε-deformation degree `δ_j` of each of the six `(−2,3,7)` q-series
(GZ §3.5, eq. (3.17) preamble). -/
def deltaDegrees : List Int := [0, 1, 2, 0, 0, 0]

/-- The companion weight vector on `h = (h_j)_{j=0}^{5}` (GZ §3.5), the same
grading centred so the weights are `{−1, 0, +1}`. -/
def hWeights : List Int := [-1, 0, 1, -1, -1, -1]

/-- Multiplicity of a weight in a grading vector. -/
def mult (ws : List Int) (w : Int) : Nat := (ws.filter (fun v => decide (v = w))).length

/-- Dimensions of `W₀, W₁, W₂` as the explicit decomposition gives them:
`W₀ = ⟨H₀,H₃,H₄,H₅⟩`, `W₁ = ⟨H₁⟩`, `W₂ = ⟨H₂⟩`. -/
def decompositionDims : List Nat := [4, 1, 1]

/-- The dimensions the **prose** sentence states. -/
def proseDims : List Nat := [1, 4, 1]

/-- **The `δ` degrees reproduce the explicit decomposition.** -/
theorem delta_matches_decomposition :
    [mult deltaDegrees 0, mult deltaDegrees 1, mult deltaDegrees 2] = decompositionDims := by
  decide

/-- **The centred weight vector reproduces it too**, weight `−1` playing the role
of degree `0`. Two independent encodings of the same grading. -/
theorem hweights_match_decomposition :
    [mult hWeights (-1), mult hWeights 0, mult hWeights 1] = decompositionDims := by
  decide

/-- **The erratum, as a theorem.** The prose dimensions differ from what the
paper's own decomposition and `δ`-degrees give — and differ precisely by
transposing the first two entries. -/
theorem prose_contradicts_decomposition :
    proseDims ≠ decompositionDims ∧
    proseDims = [decompositionDims[1]!, decompositionDims[0]!, decompositionDims[2]!] := by
  decide

/-- Both readings agree on the **total**, which is why the slip is easy to miss:
it is a transposition, not a miscount. -/
theorem totals_agree : proseDims.sum = decompositionDims.sum ∧ proseDims.sum = 6 := by
  decide

/-! ## Part B — the object-identity guard: this grading is **not** `s(x)`

`H_Ad` would be refuted if the object GZ grades were the one whose character is
`s(x) = x + 1 + x⁻¹`. It is not, and two independent checks say so. -/

/-- The rank `r` of each knot: GZ §3.4 gives `2r` q-series in total, and reports
`4`, `6`, `12` for `4₁`, `5₂`, `(−2,3,7)`. (GZ 2111.06645 §2.1 states the same
ranks `2, 3, 6` directly.) -/
def rank : PKnot → Int
  | PKnot.fourOne => 2
  | PKnot.fiveTwo => 3
  | PKnot.pretzel237 => 6

/-- **Check 1 — the totals disagree already at `4₁`.** The grading's total is
`r = 2` there, while `s(1) = 3`. A grading of a 2-dimensional space cannot be the
3-term polynomial `s`. -/
theorem rank_total_differs_from_s_at_one :
    rank PKnot.fourOne = 2 ∧ sAtOne = 3 ∧ rank PKnot.fourOne ≠ sAtOne := by
  refine ⟨by decide, s_at_one_eq_three, ?_⟩
  rw [s_at_one_eq_three]; decide

/-- The `4₁` weight set: GZ §3.4 declares `g₀, g₁` to have weights `∓1/2`
(recorded doubled, as `∓1`, to stay in `Int`). -/
def fourOneWeightsDoubled : List Int := [-1, 1]

/-- **Check 2 — even the weight *set* is knot-dependent.** `4₁` grades a
**2**-element set, `(−2,3,7)` a **3**-element one; and `4₁`'s weights are
half-integers while `(−2,3,7)`'s are integers (GZ's "level" phenomenon). A
knot-independent core cannot be read off a grading that changes shape per knot. -/
theorem weight_set_is_knot_dependent :
    fourOneWeightsDoubled.length = 2 ∧
    [mult hWeights (-1), mult hWeights 0, mult hWeights 1].length = 3 ∧
    fourOneWeightsDoubled.length ≠ adjointExponents.length := by
  refine ⟨by decide, by decide, by decide⟩

/-- **The guard, stated so it cannot be lost.** The `(−2,3,7)` grading *is*
non-multiplicity-free — a weight of dimension `4` — yet this does **not** refute
`H_Ad`, because the graded object is not the one `s(x)` describes. Recording both
halves together is the point. -/
theorem higher_multiplicity_does_not_refute_h_ad :
    (∃ w ∈ hWeights, mult hWeights w > 1) ∧
    rank PKnot.fourOne ≠ sAtOne := by
  refine ⟨⟨-1, by decide, by decide⟩, ?_⟩
  rw [s_at_one_eq_three]; decide

/-! ## Part C — the rank corroborates Part 4's arithmetic, on a third knot

`AdjointIndexSetM3` derived `|P_K| = 3, 4, 7` from the trace-field signatures.
GZ's ranks are `r = 2, 3, 6` — i.e. `|P_K| − 1`, the non-trivial representations.
This is a **second, independent** confirmation: `2111.06645` §2.1 states the
ranks outright, and `2304.09377` §3.4 recovers them from q-series counts. -/

/-- **`r = |P_K| − 1` on all three knots.** The grading counts exactly the
non-trivial boundary-parabolic representations. -/
theorem rank_eq_pk_minus_one : ∀ K : PKnot, rank K = pkSize K - 1 := by
  intro K; cases K <;> decide

/-- **The signature formula predicts the rank directly**: real embeddings plus
twice the complex-conjugate pairs. -/
theorem rank_from_signature :
    ∀ K : PKnot, rank K = realEmbeddings K + 2 * complexPairs K := by
  intro K; cases K <;> decide

/-- The three ranks are distinct, so the agreement is not a two-point fit. -/
theorem ranks_are_three_distinct_values :
    rank PKnot.fourOne = 2 ∧ rank PKnot.fiveTwo = 3 ∧ rank PKnot.pretzel237 = 6 ∧
    rank PKnot.fourOne ≠ rank PKnot.fiveTwo ∧
    rank PKnot.fiveTwo ≠ rank PKnot.pretzel237 := by
  refine ⟨by decide, by decide, by decide, by decide, by decide⟩

/-! ## Part D — `W₀` is an `S₃` representation, and its blocks are partitions of 3

GZ §3.5, quoted: the `SL₂(ℤ)` action *"is the identity on `W₁` and `W₂` and has
kernel `Γ(2)` on `W₀`. Thus, the action of `ρ` on `W₀` comes from a
representation `ρ′` of the quotient group `S₃ = Γ/Γ(2)`. The latter decomposes as
the direct sum of the 2-dimensional irreducible representation of `S₃` and two
copies of the trivial representation."*

`S₃`-irreps are indexed by partitions of `3` — the same Wedderburn indexing the
QOU Hecke programme uses at `q = 1`. So the third knot's modular structure lands
directly in the corpus's own language, and one block is conspicuously **absent**. -/

/-- The irreducible representations of `S₃`, as partitions of `3`, with their
dimensions: `(3)` trivial, `(2,1)` standard, `(1,1,1)` sign. -/
def s3IrrepDims : List Nat := [1, 2, 1]

/-- The multiplicity of each `S₃`-irrep in `W₀`, in the same `(3) / (2,1) /
(1,1,1)` order: two trivials, one standard, **no sign**. -/
def w0Multiplicities : List Nat := [2, 1, 0]

/-- **The decomposition is dimensionally consistent**: `2·1 + 1·2 + 0·1 = 4 =
dim W₀`. -/
theorem w0_decomposition_consistent :
    w0Multiplicities[0]! * s3IrrepDims[0]!
      + w0Multiplicities[1]! * s3IrrepDims[1]!
      + w0Multiplicities[2]! * s3IrrepDims[2]! = decompositionDims[0]! := by
  decide

/-- **The sign representation is absent from `W₀`.** Under the standard
identification the sign block is the bar-odd one, so the `Γ/Γ(2)` action on the
level-2 part of the third knot's grading carries **no** sign component — a
chirality-flavoured statement, and the one asymmetry in the decomposition. -/
theorem w0_has_no_sign_representation : w0Multiplicities[2]! = 0 := by decide

/-- **The level-2 behaviour is confined to `W₀`.** `ρ` is the identity on `W₁`
and `W₂`, so the entire `Γ(2)` phenomenon lives in the 4-dimensional weight space
— exactly the one whose multiplicity the prose misreported. -/
theorem level_two_confined_to_w0 :
    decompositionDims[1]! = 1 ∧ decompositionDims[2]! = 1 ∧
    decompositionDims[0]! = 4 := by
  decide

/-! ## Part E — the absent sign block is FORCED, not observed

Part D recorded the missing sign representation as an observation. It is more
than that: given GZ's own decomposition it is a **theorem**, and the reason is a
general fact about permutation modules.

**Step 1 — the level restricts where the question can even be asked.** GZ
introduces the level as *"a new phenomenon"* arising at `(−2,3,7)`, which has
`N = 2`. The other two knots have `N = 1`, so `ρ` factors through the *trivial*
quotient: **there is no finite group acting at `4₁` or `5₂`, hence no sign block
to be absent.** The observation is single-instance among these three knots by
construction, and Part D's phrasing understated that.

**Step 2 — but at `(−2,3,7)` the absence is forced.** `S₃`-characters are
determined on the three classes `e`, transpositions, 3-cycles (sizes `1, 3, 2`).
GZ gives `W₀ = ` standard `⊕` trivial`²`, whose character is `[4, 2, 1]`. That is
exactly `[3, 1, 0] + [1, 1, 1]` — the character of the **permutation module on 3
points**, plus one trivial. Characters determine complex representations up to
isomorphism, so

  `W₀ ≅ ℂ[X] ⊕ ℂ`,  `X` a 3-element `S₃`-set.

And a permutation module on 3 points **never** contains the sign representation:
`⟨χ_perm, χ_sign⟩ = (1·3·1 + 3·1·(−1) + 2·0·1)/6 = 0`. Adding trivial summands
cannot introduce one. So the sign block's absence is a consequence of `W₀` being
permutation-type, not a coincidence to be explained.

**What stays interpretive.** That the 3-element set is *geometrically* the three
cusps of `Γ(2)` (equivalently the three non-zero 2-torsion classes, the three
index-2 subgroups) is the standard `Γ/Γ(2) ≅ S₃` picture, but GZ does not say
`W₀` realizes it, and this file does not claim so. The character identity is
proved; the geometric identification is a reading.

Inner products are carried as `6⟨·,·⟩` to stay in `Int`. -/

/-- Class sizes of `S₃`: identity, transpositions, 3-cycles. -/
def s3ClassSizes : List Int := [1, 3, 2]

/-- Character of the trivial representation. -/
def chiTrivial : List Int := [1, 1, 1]

/-- Character of the sign representation. -/
def chiSign : List Int := [1, -1, 1]

/-- Character of the 2-dimensional standard representation. -/
def chiStandard : List Int := [2, 0, -1]

/-- Character of the permutation module on 3 points (`χ(g) = #` fixed points). -/
def chiPerm : List Int := [3, 1, 0]

/-- Six times the character inner product, kept integral. -/
def ip6 (a b : List Int) : Int :=
  (List.zipWith (fun s ab => s * ab) s3ClassSizes (List.zipWith (· * ·) a b)).sum

/-- Pointwise sum of characters (direct sum of representations). -/
def addChar (a b : List Int) : List Int := List.zipWith (· + ·) a b

/-- **The permutation module on 3 points is `trivial ⊕ standard`.** Multiplicity
one each (`6⟨·,·⟩ = 6`). -/
theorem perm_is_trivial_plus_standard :
    ip6 chiPerm chiTrivial = 6 ∧ ip6 chiPerm chiStandard = 6 := by decide

/-- **A permutation module on 3 points contains no sign component.** This is the
general fact the absence rests on — nothing about knots enters. -/
theorem perm_has_no_sign : ip6 chiPerm chiSign = 0 := by decide

/-- The character of `W₀` as GZ decomposes it: standard `⊕` trivial`²`. -/
def chiW0 : List Int := addChar chiStandard (addChar chiTrivial chiTrivial)

/-- **`W₀` is a permutation module plus a trivial**, at the level of characters —
and characters determine complex representations up to isomorphism. -/
theorem w0_is_perm_plus_trivial : chiW0 = addChar chiPerm chiTrivial := by decide

/-- `W₀` has the dimension Part A extracted: `χ(e) = 4`. -/
theorem w0_dimension_four : chiW0.head! = 4 := by decide

/-- Six times the **sign multiplicity** of a character given by its three class
values `(a₀, a₁, a₂)`: `1·a₀·1 + 3·a₁·(−1) + 2·a₂·1`. -/
def signMult6 (a0 a1 a2 : Int) : Int := a0 - 3 * a1 + 2 * a2

/-- `signMult6` agrees with `ip6 · chiSign` on the permutation character. -/
theorem signMult6_matches_ip6 : signMult6 3 1 0 = ip6 chiPerm chiSign := by decide

/-- **Adding a trivial summand does not change the sign multiplicity.** This is
the whole mechanism: `χ_triv = (1,1,1)` contributes `1 − 3 + 2 = 0`. -/
theorem addTrivial_preserves_signMult (a0 a1 a2 : Int) :
    signMult6 (a0 + 1) (a1 + 1) (a2 + 1) = signMult6 a0 a1 a2 := by
  unfold signMult6; omega

/-- **The sign block's absence is FORCED, for the whole family.** Starting from
the permutation character (sign multiplicity `0`) and adding *any* number of
trivial summands leaves it `0`. So no representation of the form
`ℂ[3 points] ⊕ ℂ^{⊕n}` — which is what `W₀` is — can contain the sign
representation. Not "observed to be zero": zero by shape. -/
theorem sign_absence_is_forced :
    ∀ n : Nat, signMult6 (3 + n) (1 + n) (0 + n) = 0 := by
  intro n; unfold signMult6; omega

/-- **The instance follows.** `W₀` itself has zero sign multiplicity. -/
theorem w0_sign_multiplicity_zero : ip6 chiW0 chiSign = 0 := by decide

/-! ### The level restriction, recorded so the scope is not overstated -/

/-- The level `N` of each knot (GZ §3.5: the level is *introduced* at `(−2,3,7)`,
which has `N = 2`; the other two are `N = 1`). -/
def level : PKnot → Nat
  | PKnot.fourOne => 1
  | PKnot.fiveTwo => 1
  | PKnot.pretzel237 => 2

/-- **At level 1 there is no group, hence no sign block to be absent.** The
`Γ/Γ(N)` quotient is trivial exactly when `N = 1`, so `4₁` and `5₂` supply no
comparandum — the sign-absence is a one-knot statement among these three, and
saying otherwise would overstate it. -/
theorem sign_question_only_arises_at_level_two :
    level PKnot.fourOne = 1 ∧ level PKnot.fiveTwo = 1 ∧ level PKnot.pretzel237 = 2 ∧
    level PKnot.pretzel237 ≠ level PKnot.fourOne := by
  refine ⟨by decide, by decide, by decide, by decide⟩

/-! ## Part F — Dimofte–Garoufalidis §6: the signature inputs confirmed, the hypothesis named, and two conditional predictions

`uploads/1511.05628v1.pdf` (Dimofte–Garoufalidis, *Quantum Modularity and Complex
Chern–Simons Theory*) §6 states trace fields in the **signature notation
`[r₁, r₂]`** — exactly the input Part 4's rule consumes — for five knots,
glyph-verified:

| knot | minimal polynomial | type `[r₁,r₂]` | disc |
|---|---|---|---|
| `4₁` | `x² − x + 1` | `[0, 1]` | `−3` |
| `5₂` | `x³ − x² + 1` | `[1, 1]` | `−23` |
| `6₁` | `x⁴ − 2x³ + x² + 3x + 1` | `[0, 2]` | `257` |
| `(−2,3,−3) = (−2,3,9)` | `x⁵ − x⁴ + x³ + 2x² − 2x + 1` | `[1, 2]` | `23·733` |
| `(−2,3,7)` | *same trace field as* `5₂` | `[1, 1]` | `−23` |

**Confirmation.** Part 4 derived `4₁ ↦ (0 real, 1 pair)` and `5₂ ↦ (1 real, 1
pair)` by reading GZ's prose. DG states the same two as `[0,1]` and `[1,1]` in
type notation. Independent sources, identical inputs.

**The hypothesis Part 4 was silently making, now named.** The rule is
`r = #embeddings of A_K^red`, and `A_K^red ⊇ F_K` (the trace field) with equality
**iff** `K` has no boundary-parabolic representations outside its trace field.
Part 4 used `A_K^red`; DG tabulates `F_K`. They coincide for `4₁` and `5₂` — and
**`(−2,3,7)` is a worked counterexample where they do not**: its trace field is
`5₂`'s (3 embeddings) while `r = 6`, because `P_K` picks up a second Galois orbit
over the totally real `ℚ(η)`. So "signature of the trace field" is *not*
interchangeable with "signature of `A_K^red`", and Part 4's agreement on two
knots did not establish which one the rule needs.

**Two conditional predictions.** Under the named hypothesis `A_K^red = F_K`:

* `6₁`  — `[0,2]` ⇒ `r = 0 + 2·2 = 4`, `|P_K| = 5`;
* `(−2,3,9)` — `[1,2]` ⇒ `r = 1 + 2·2 = 5`, `|P_K| = 6`.

Falsifiable, and stated *with* their hypothesis rather than as bare numbers —
`(−2,3,7)` is exactly the knot where an unstated version of this would have been
wrong.

**A non-inference, recorded deliberately.** DG's Table 2 has a column headed
"Level" (`4₁ ≤7`, `5₂ ≤5`, `6₁ ≤3`, …). That is the **Chern–Simons level**
`k` with `ζ^k = 1` — the order of the root of unity at which the numerics were
run — **not** GZ's level `N` (the period of the colored-Jones degree
quasi-polynomial) from Part E. Reading `6₁ ≤ 3` as "`6₁` has level 3" would
manufacture the fourth level-`> 1` knot that Part E's open question asks for, out
of a different quantity. Third instance of this same conflation trap in this arc;
recorded so it is not walked into a fourth time. -/

/-- The knots for which Dimofte–Garoufalidis §6 gives a trace-field signature. -/
inductive DGKnot where
  | fourOne : DGKnot
  | fiveTwo : DGKnot
  | sixOne : DGKnot
  | pretzel239 : DGKnot
  deriving DecidableEq

/-- `r₁`, the number of **real** embeddings of the trace field (DG type `[r₁,r₂]`). -/
def traceFieldReal : DGKnot → Int
  | DGKnot.fourOne => 0        -- ℚ(√−3),  type [0,1]
  | DGKnot.fiveTwo => 1        -- x³−x²+1, type [1,1]
  | DGKnot.sixOne => 0         -- x⁴−2x³+x²+3x+1, type [0,2]
  | DGKnot.pretzel239 => 1     -- x⁵−x⁴+x³+2x²−2x+1, type [1,2]

/-- `r₂`, the number of **complex-conjugate pairs** of embeddings. -/
def traceFieldPairs : DGKnot → Int
  | DGKnot.fourOne => 1
  | DGKnot.fiveTwo => 1
  | DGKnot.sixOne => 2
  | DGKnot.pretzel239 => 2

/-- Degree of the trace field, `r₁ + 2r₂` — checkable against the stated minimal
polynomials (degrees `2, 3, 4, 5`). -/
def traceFieldDegree (K : DGKnot) : Int := traceFieldReal K + 2 * traceFieldPairs K

/-- **The signatures reproduce the stated minimal-polynomial degrees.** A
consistency check on the transcription: `[0,1] → 2`, `[1,1] → 3`, `[0,2] → 4`,
`[1,2] → 5`. -/
theorem signatures_match_polynomial_degrees :
    traceFieldDegree DGKnot.fourOne = 2 ∧
    traceFieldDegree DGKnot.fiveTwo = 3 ∧
    traceFieldDegree DGKnot.sixOne = 4 ∧
    traceFieldDegree DGKnot.pretzel239 = 5 := by decide

/-- **DG's types confirm Part 4's inputs on the two shared knots.** Part 4 read
its signatures off GZ's prose; DG states them independently in `[r₁,r₂]`
notation, and they agree. -/
theorem dg_confirms_part4_inputs :
    traceFieldReal DGKnot.fourOne = realEmbeddings PKnot.fourOne ∧
    traceFieldPairs DGKnot.fourOne = complexPairs PKnot.fourOne ∧
    traceFieldReal DGKnot.fiveTwo = realEmbeddings PKnot.fiveTwo ∧
    traceFieldPairs DGKnot.fiveTwo = complexPairs PKnot.fiveTwo := by decide

/-- The rank predicted **under the hypothesis** `A_K^red = F_K`. -/
def predictedRankFromTraceField (K : DGKnot) : Int := traceFieldDegree K

/-- **The hypothesis holds for `4₁` and `5₂`** — the prediction reproduces GZ's
measured ranks `2` and `3`. -/
theorem prediction_correct_where_hypothesis_holds :
    predictedRankFromTraceField DGKnot.fourOne = rank PKnot.fourOne ∧
    predictedRankFromTraceField DGKnot.fiveTwo = rank PKnot.fiveTwo := by decide

/-- **And it FAILS for `(−2,3,7)`** — the worked counterexample. Its trace field
is `5₂`'s, so the trace-field-only rule predicts `3`; the measured rank is `6`,
because `P_K` acquires a second Galois orbit over `ℚ(η)`. This is why the
hypothesis has to be stated, not assumed. -/
theorem trace_field_alone_fails_on_pretzel237 :
    traceFieldDegree DGKnot.fiveTwo = 3 ∧ rank PKnot.pretzel237 = 6 ∧
    traceFieldDegree DGKnot.fiveTwo ≠ rank PKnot.pretzel237 := by decide

/-- **The two conditional predictions.** Under `A_K^red = F_K`: `6₁` has rank `4`
and `|P_K| = 5`; `(−2,3,9)` has rank `5` and `|P_K| = 6`. Not verified here — no
source in the corpus gives these ranks — and false if either knot has
representations outside its trace field, exactly as `(−2,3,7)` does. -/
theorem conditional_predictions :
    predictedRankFromTraceField DGKnot.sixOne = 4 ∧
    predictedRankFromTraceField DGKnot.sixOne + 1 = 5 ∧
    predictedRankFromTraceField DGKnot.pretzel239 = 5 ∧
    predictedRankFromTraceField DGKnot.pretzel239 + 1 = 6 := by decide

/-! ## Part G — the `6₁` prediction is CONFIRMED, from a second, unrelated object

Part F predicted, *under* the named hypothesis `A_K^red = F_K`, that `6₁` has
`r = 4` and `|P_K| = 5`, derived from Dimofte–Garoufalidis's trace-field type
`[0, 2]`.

**A sibling session independently certified it** (`main`, `96d65d02e`, bean
`qou-btvl`, probe `apoly_census_ldegree_certification_probe.py`, 3/3) from the
Culler A-polynomial census (`uploads/A_census.tgz`, owner-supplied):

| knot | census name | geometric `L`-degree | full `L`-degree |
|---|---|---|---|
| `4₁` | `K2_1` | 2 | 3 |
| `5₂` | `K3_2` | 3 | 4 |
| `6₁` | `K4_1` | **4** | **5** |

**Why this is a test and not a restatement.** The two sides come from unrelated
objects in unrelated sources:

* the prediction is the **degree of an algebraic number field** — DG §6's
  `x⁴ − 2x³ + x² + 3x + 1`, signature `[0,2]`, discriminant `257`;
* the certification is the **`L`-degree of a Newton polygon** — the census
  A-polynomial of `K4_1`.

Nothing forces a number field's degree to equal a knot polynomial's `L`-degree.
They agree on **three** knots (`2, 3, 4`), and `6₁` was predicted *before* its
census value was in hand.

**One half is NOT a test, and the sibling flagged it first.** `full = geom + 1`
holds by construction — the `+1` is the abelian/trivial representation — so the
`|P_K| = r + 1` leg confirms nothing. The content is entirely in
`deg F_K = geometric L-degree = r`.

**And the control fires.** At `(−2,3,7)` the identity **fails**: its trace field
is `5₂`'s (degree `3`) while `r = 6`. That is not a counterexample to the rule —
it is the rule's hypothesis doing its job, since `(−2,3,7)` is exactly the knot
with `A_K^red ⊋ F_K`. A rule that fitted everything would be the worrying
outcome; this one fits where its stated hypothesis holds and breaks where it
does not.

Credit: the census certification is the sibling's work, not this file's. What is
this file's is the prediction it confirms. -/

/-- Geometric `A`-polynomial `L`-degree, certified from the Culler census
(sibling probe `apoly_census_ldegree_certification_probe.py`). -/
def geomLDegree : DGKnot → Int
  | DGKnot.fourOne => 2      -- census K2_1
  | DGKnot.fiveTwo => 3      -- census K3_2
  | DGKnot.sixOne => 4       -- census K4_1
  | DGKnot.pretzel239 => 0   -- not in the certified census data

/-- Full `A`-polynomial `L`-degree = geometric `+ 1` (the abelian factor). -/
def fullLDegree (K : DGKnot) : Int := geomLDegree K + 1

/-- **The `6₁` prediction is confirmed.** The trace-field degree from DG's
signature `[0,2]` equals the certified geometric `L`-degree from the census. -/
theorem sixOne_prediction_confirmed :
    predictedRankFromTraceField DGKnot.sixOne = geomLDegree DGKnot.sixOne ∧
    geomLDegree DGKnot.sixOne = 4 ∧
    fullLDegree DGKnot.sixOne = 5 := by decide

/-- **Trace-field degree = geometric `L`-degree on all three certified knots.**
A number field's degree and a Newton polygon's `L`-degree are unrelated a priori;
they agree at `2, 3, 4`. -/
theorem degree_equals_geom_ldegree_on_all_three :
    predictedRankFromTraceField DGKnot.fourOne = geomLDegree DGKnot.fourOne ∧
    predictedRankFromTraceField DGKnot.fiveTwo = geomLDegree DGKnot.fiveTwo ∧
    predictedRankFromTraceField DGKnot.sixOne = geomLDegree DGKnot.sixOne := by decide

/-- **The three values are distinct**, so the agreement is not a constant. -/
theorem the_three_degrees_are_distinct :
    geomLDegree DGKnot.fourOne = 2 ∧ geomLDegree DGKnot.fiveTwo = 3 ∧
    geomLDegree DGKnot.sixOne = 4 ∧
    geomLDegree DGKnot.fourOne ≠ geomLDegree DGKnot.sixOne := by decide

/-- **The `+1` leg is not a test.** `full = geom + 1` holds definitionally here
(the abelian representation), so it cannot corroborate anything — recorded so the
`|P_K| = r + 1` agreement is never cited as evidence. -/
theorem plus_one_leg_is_definitional (K : DGKnot) :
    fullLDegree K = geomLDegree K + 1 := rfl

/-- **The control fires at `(−2,3,7)`.** Its trace field is `5₂`'s, degree `3`,
while its rank is `6` — the identity fails exactly where the hypothesis
`A_K^red = F_K` fails. A rule that matched here too would be the worrying
outcome. -/
theorem control_fires_where_hypothesis_fails :
    predictedRankFromTraceField DGKnot.fiveTwo = 3 ∧
    rank PKnot.pretzel237 = 6 ∧
    predictedRankFromTraceField DGKnot.fiveTwo ≠ rank PKnot.pretzel237 := by decide

end QOU.QBeta.GZThirdKnotRankGrading
