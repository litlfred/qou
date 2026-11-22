import QOU.Machinery.HeckeH3AlgebraInstance
import QOU.Machinery.HeckeTowerBasicConstruction
import QOU.Machinery.HeckeH2AlgebraInstance
import QOU.Machinery.HeckeH3Semisimple
import QOU.MathlibExt.TraceFormSemisimple
import Mathlib.Tactic.IntervalCases

/-!
# A rank-bounded braided presentation — and the corpus's first content-bearing instance

`HeckeBraidedCategory.HeckeBraidedPresentation` quantifies its three relations
over **all** `i : ℕ`, i.e. it describes `H_∞`. Two facts about that, both proved
in `HeckeTowerBasicConstruction`:

* it is satisfiable **degenerately** — a single element meeting the quadratic
  gives an instance via the constant family, with braid and far-commutation
  `rfl` (`constant_generator_presentation`);
* and no finite `H_n` satisfies it with its true generators
  (`far_commute_zero`; the same obstruction, covering both padding routes, is
  recorded in prose in `HeckeH3AlgebraLaws`'s honesty note, which predates this
  file — the Lean version machine-checks half of what was already known there).

Together those say the class cannot be given a **useful** instance: the reachable
ones carry no Hecke content, and the contentful ones do not exist.

`HeckeBraidedPresentationOfRank` fixes that by bounding the relations to a rank
`n`, which is what a finite Hecke algebra actually satisfies. It is a NEW class
rather than a change to the old one: twelve files bind
`HeckeBraidedPresentation`, and mutating its signature is a refactor whose blast
radius is unrelated to the point being made here.

## What this buys

`heckePresentationOfRank_H3A` is an instance with **real content**: the genuine
`H₃(q)` on the six-element normal-form basis, its two true generators `σ₀` and
`σ₁`, the Hecke quadratic for both, and the braid relation `σ₀σ₁σ₀ = σ₁σ₀σ₁`.
Nothing is padded and nothing is constant — `σ₀` and `σ₁` are distinct and do
not commute.

It is, as far as the corpus goes, the first presentation instance of any kind.
The concrete layer it is built from (`H3A`, `mulNF`, the proved laws) is
pre-existing; what is new is that a presentation class now has somewhere to land.

## What it does NOT do

It does not give `HeckeCosetSpanning` an instance. That class binds the
**unbounded** presentation, so re-pointing it at this one is a further change,
deliberately not made here — and the spanning statement itself would still need
proving for `H₂ ⊂ H₃` afterwards.
-/

namespace QOU.Machinery.HeckeRank

open QOU.Machinery.H3 QOU.Machinery.HeckeTower

variable {R : Type*} [Field R]

/-! ## The instance: genuine H₃(q) at rank 3 -/

/-- `σ₀` as an element of the normal-form algebra — basis index 1. -/
def s0 (h : R) : H3A R h := ⟨![0, 1, 0, 0, 0, 0]⟩

/-- `σ₁` as an element of the normal-form algebra — basis index 2. -/
def s1 (h : R) : H3A R h := ⟨![0, 0, 1, 0, 0, 0]⟩

/-- The generator family. At rank 3 the guards constrain only `σ 0` and `σ 1`;
indices past the rank are unconstrained, so they are sent to `0` rather than
padded with a real generator — padding is exactly what the unbounded class
cannot survive. -/
def gen (h : R) : ℕ → H3A R h := fun i => if i = 0 then s0 h else if i = 1 then s1 h else 0

theorem s0_mul_s0 (h : R) : s0 h * s0 h = h • s0 h + 1 := by
  apply H3A.ext; funext i; fin_cases i <;>
    simp [s0, mulNF, mulσ₀, mulσ₁, unitNF]

theorem s1_mul_s1 (h : R) : s1 h * s1 h = h • s1 h + 1 := by
  apply H3A.ext; funext i; fin_cases i <;>
    simp [s1, mulNF, mulσ₀, mulσ₁, unitNF]

theorem braid_s0_s1 (h : R) : s0 h * s1 h * s0 h = s1 h * s0 h * s1 h := by
  apply H3A.ext; funext i; fin_cases i <;>
    simp [s0, s1, mulNF, mulσ₀, mulσ₁]

/-- **The corpus's first content-bearing presentation instance.** Genuine
`H₃(q)` on the six-element normal-form basis, with its two true generators: the
Hecke quadratic for each and the braid relation between them. Nothing padded,
nothing constant. -/
instance heckePresentationOfRank_H3A (q : R) :
    HeckeBraidedPresentationOfRank q 3 (H3A R (q - q⁻¹)) (gen (q - q⁻¹)) where
  hecke_quadratic i hi := by
    have hlt : i < 2 := by omega
    interval_cases i
    · simpa [gen] using s0_mul_s0 (R := R) (q - q⁻¹)
    · simpa [gen] using s1_mul_s1 (R := R) (q - q⁻¹)
  braid_adjacent i hi := by
    have hlt : i < 1 := by omega
    interval_cases i
    · simpa [gen] using braid_s0_s1 (R := R) (q - q⁻¹)
  far_commute i j hij hj := by omega

/-! ## The instance is not the degenerate one

`constant_generator_presentation` shows the unbounded class is satisfiable by a
constant family, where every relation is `rfl` and nothing fails to commute. An
instance is worth having only if it is not of that shape, so that is checked
rather than assumed. -/

/-- The two generators are distinct. -/
theorem s0_ne_s1 (h : R) [Nontrivial R] : s0 h ≠ s1 h := by
  intro hEq
  have h1 := congrArg (fun x => H3A.v x 1) hEq
  simp [s0, s1] at h1

/-- **The two generators do not commute.** This is what the constant family
cannot reproduce: there, `far_commute` and `braid_adjacent` hold by `rfl`
precisely because everything commutes. Here the braid relation
`σ₀σ₁σ₀ = σ₁σ₀σ₁` is a genuine identity between two *different* products. -/
theorem s0_mul_s1_ne_s1_mul_s0 (h : R) [Nontrivial R] :
    s0 h * s1 h ≠ s1 h * s0 h := by
  intro hEq
  have h3 := congrArg (fun x => H3A.v x 3) hEq
  simp [s0, s1, mulNF, mulσ₀, mulσ₁] at h3

/-! ## H₂ ⊂ H₃: the spanning decomposition, concretely

The four `σ₁`-coset products are exactly the four basis vectors that
`iota23` does not reach, with no correction terms:

| product | basis index |
|---|---|
| `σ₁` | 2 |
| `σ₁ · σ₀` | 3 |
| `σ₀ · σ₁` | 4 |
| `σ₀ · σ₁ · σ₀` | 5 |

and `iota23 a b = ![a, b, 0, 0, 0, 0]` covers 0 and 1. So `H₃ = ι(H₂) + ι(H₂)·σ₁·ι(H₂)`
holds on the nose. -/

/-- `σ₀` inside the rank-2 algebra. -/
def t0 (h : R) : H2A R h := ⟨0, 1⟩

/-- Rank-2 generator family. At rank 2 the only obligation is the quadratic for
`σ 0`; braid and far-commutation are vacuous, so indices past the rank go to `0`. -/
def gen2 (h : R) : ℕ → H2A R h := fun i => if i = 0 then t0 h else 0

theorem t0_mul_t0 (h : R) : t0 h * t0 h = h • t0 h + 1 := by
  apply H2A.ext <;> simp [t0]

/-- Rank-2 presentation instance for `H₂(q)`. -/
instance heckePresentationOfRank_H2A (q : R) :
    HeckeBraidedPresentationOfRank q 2 (H2A R (q - q⁻¹)) (gen2 (q - q⁻¹)) where
  hecke_quadratic i hi := by
    have hlt : i < 1 := by omega
    interval_cases i
    · simpa [gen2] using t0_mul_t0 (R := R) (q - q⁻¹)
  braid_adjacent i hi := by omega
  far_commute i j hij hj := by omega

/-- **`HeckeCosetSpanning`, instantiated.** Every `w : H₃` splits as
`ι a + Σᵢ ι (b i) · σ₁ · ι (c i)` with the four coset terms reading off `w`'s
coordinates 2–5 and `a` reading off 0–1.

This is the class's first instance, and the statement is discharged by an
explicit decomposition rather than by any abstract argument. -/
instance heckeCosetSpanning_H2_H3 (q : R) :
    HeckeCosetSpanning R q 3 (H2A R (q - q⁻¹)) (H3A R (q - q⁻¹))
      (gen (q - q⁻¹)) (H2A.iotaAlg (h := q - q⁻¹)) 1 where
  spanning w := by
    classical
    refine ⟨⟨w.v 0, w.v 1⟩, Finset.range 4,
      fun i => if i = 0 then (w.v 2) • 1 else if i = 1 then (w.v 4) • t0 _
               else if i = 2 then (w.v 3) • 1 else (w.v 5) • t0 _,
      fun i => if i = 0 then 1 else if i = 1 then 1
               else if i = 2 then t0 _ else t0 _, ?_⟩
    apply H3A.ext
    funext i
    fin_cases i <;>
      simp [Finset.sum_range_succ, gen, H2A.iotaAlg, H2A.iotaFun, iota23, t0, s1,
        mulNF, mulσ₀, mulσ₁]

/-! ## The conditional expectation for H₂ ⊂ H₃

`ε` is FORCED on the basis once the Markov property is imposed, given the
coset table above:

  ε γ = γ,  ε σ₀ = σ₀                          (retraction on the image)
  ε σ₁ = z•γ                                   (Markov)
  ε (σ₁σ₀) = z•σ₀,  ε (σ₀σ₁) = z•σ₀            (bimodule, one side trivial)
  ε (σ₀σ₁σ₀) = z•σ₀² = z•(h•σ₀ + 1)            (bimodule, both sides)

so in coordinates

  ε v = ⟨v₀ + z·v₂ + z·v₅ , v₁ + z·v₃ + z·v₄ + z·h·v₅⟩.

Nothing is chosen here: every entry is read off the table. -/

/-- The conditional expectation `H₃ → H₂` at Markov parameter `z`, in
coordinates. -/
def epsFun (h z : R) (w : H3A R h) : H2A R h :=
  ⟨w.v 0 + z * w.v 2 + z * w.v 5,
   w.v 1 + z * w.v 3 + z * w.v 4 + z * h * w.v 5⟩

/-- `epsFun` bundled as an `R`-linear map. -/
def epsLin (h z : R) : H3A R h →ₗ[R] H2A R h where
  toFun := epsFun h z
  map_add' x y := by apply H2A.ext <;> simp [epsFun] <;> ring
  map_smul' c x := by apply H2A.ext <;> simp [epsFun, H2A.smul_a, H2A.smul_b] <;> ring

/-- **`retract` holds for `epsLin`** — the first field of
`HeckeConditionalExpectation`, concretely. -/
theorem epsLin_retract (h z : R) (x : H2A R h) :
    epsLin h z (H2A.iotaAlg x) = x := by
  apply H2A.ext <;> simp [epsLin, epsFun, H2A.iotaAlg, H2A.iotaFun, iota23]

/-- **`bimodule` holds for `epsLin`** — the second field, concretely:
`ε (ι x · w · ι y) = x · ε w · y` for all `x, y : H₂` and `w : H₃`.

This is the one that could have failed. `ε` was written down from the coset
table by imposing the Markov property; whether the resulting map is an
`(H₂, H₂)`-bimodule map is a separate question, settled here by computation
over all six coordinates with `x`, `y`, `w` symbolic. -/
theorem epsLin_bimodule (h z : R) (x y : H2A R h) (w : H3A R h) :
    epsLin h z (H2A.iotaAlg x * w * H2A.iotaAlg y)
      = x * epsLin h z w * y := by
  apply H2A.ext <;>
    simp [epsLin, epsFun, H2A.iotaAlg, H2A.iotaFun, iota23, mulNF, mulσ₀, mulσ₁,
      H2A.mul_a, H2A.mul_b] <;> ring

/-- **The Markov property holds for `epsLin`** — the field of
`HeckeMarkovExpectation`: `ε (ι b · σ₁ · ι c) = z • (b · c)`. -/
theorem epsLin_markov (h z : R) (b c : H2A R h) :
    epsLin h z (H2A.iotaAlg b * s1 h * H2A.iotaAlg c) = z • (b * c) := by
  apply H2A.ext <;>
    simp [epsLin, epsFun, H2A.iotaAlg, H2A.iotaFun, iota23, s1, mulNF, mulσ₀,
      mulσ₁, H2A.mul_a, H2A.mul_b, H2A.smul_a, H2A.smul_b] <;> ring

/-! ### The instances

With `HeckeConditionalExpectation` and `HeckeMarkovExpectation` re-pointed at
`HeckeBraidedPresentationOfRank`, the three theorems above are exactly their
fields, so both classes are now inhabited at this rung. -/

/-- **`HeckeConditionalExpectation`, instantiated** for `H₂ ⊂ H₃`. -/
instance heckeConditionalExpectation_H2_H3 (q z : R) :
    HeckeConditionalExpectation R q 3 (H2A R (q - q⁻¹)) (H3A R (q - q⁻¹))
      (gen (q - q⁻¹)) (H2A.iotaAlg (h := q - q⁻¹)) (epsLin (q - q⁻¹) z) where
  retract := epsLin_retract (q - q⁻¹) z
  bimodule x zz y := epsLin_bimodule (q - q⁻¹) z x zz y

/-- **`HeckeMarkovExpectation`, instantiated** for `H₂ ⊂ H₃` at the coset
generator `σ₁`, with the Ocneanu scalar `z`. -/
instance heckeMarkovExpectation_H2_H3 (q z : R) :
    HeckeMarkovExpectation R q 3 (H2A R (q - q⁻¹)) (H3A R (q - q⁻¹))
      (gen (q - q⁻¹)) (H2A.iotaAlg (h := q - q⁻¹)) (epsLin (q - q⁻¹) z) 1 z where
  markov b c := by simpa [gen] using epsLin_markov (q - q⁻¹) z b c

/-- **All four tower classes are inhabited at `H₂ ⊂ H₃`, and found by instance
search.** Recorded as one statement so the milestone is checkable rather than
asserted across four separate declarations — and so that a later change which
quietly breaks resolution for any one of them fails here.

What this does NOT say: nothing about general `n`. Every component is fixed at
rank 3, and `WenzlTowerStep` is not among them. -/
theorem tower_classes_inhabited_H2_H3 (q z : R) :
    HeckeBraidedPresentationOfRank q 3 (H3A R (q - q⁻¹)) (gen (q - q⁻¹))
      ∧ HeckeCosetSpanning R q 3 (H2A R (q - q⁻¹)) (H3A R (q - q⁻¹))
          (gen (q - q⁻¹)) (H2A.iotaAlg (h := q - q⁻¹)) 1
      ∧ HeckeConditionalExpectation R q 3 (H2A R (q - q⁻¹)) (H3A R (q - q⁻¹))
          (gen (q - q⁻¹)) (H2A.iotaAlg (h := q - q⁻¹)) (epsLin (q - q⁻¹) z)
      ∧ HeckeMarkovExpectation R q 3 (H2A R (q - q⁻¹)) (H3A R (q - q⁻¹))
          (gen (q - q⁻¹)) (H2A.iotaAlg (h := q - q⁻¹)) (epsLin (q - q⁻¹) z) 1 z :=
  ⟨inferInstance, inferInstance, inferInstance, inferInstance⟩

/-! ## `WenzlTowerStep` at this rung is a TRIVIAL discharge — read this before citing it

`WenzlTowerStep`'s field is an implication whose conclusion is
`IsSemisimpleRing Hn1`. At `H₂ → H₃` that conclusion is already a theorem —
`isSemisimpleRing_H3A`, via the explicit Wedderburn decomposition — so the field
can be discharged by **ignoring both hypotheses and citing it**.

That is what `wenzlTowerStep_H2_H3_trivial` below does, and it is why the name
says so. It is a true statement and it is **not Wenzl's ascent**: the induction
step (semisimplicity of `Hₙ` plus trace nondegeneracy *implying* semisimplicity
of `H_{n+1}`) is never exercised. Anything downstream that cites this as evidence
the ascent is formalized would be wrong.

The same shape as `constant_generator_presentation`: an instance can exist while
carrying none of the content its class is named for. Recorded for the same
reason — so the next reader does not mistake inhabitation for content.

**The general-`n` ascent remains open.** It is the actual target, and no part of
this file touches it. -/

/-- **`WenzlTowerStep` holds at `H₂ → H₃`, trivially.** Both hypotheses are
discarded; the conclusion is `isSemisimpleRing_H3A`.

Stated as a theorem taking the genericity conditions explicitly rather than as an
`instance`, for two reasons: `isSemisimpleRing_H3A` needs them, and an instance
would invite instance search to present a trivial discharge as though it were the
ascent. -/
theorem wenzlTowerStep_H2_H3_trivial (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (trn1 : H3A R (q - q⁻¹) → R) :
    WenzlTowerStep R q 3 (H2A R (q - q⁻¹)) (H3A R (q - q⁻¹))
      (gen (q - q⁻¹)) (H2A.iotaAlg (h := q - q⁻¹)) trn1 where
  semisimple_ascend _ _ := isSemisimpleRing_H3A q hq h2 h3

/-! ## `WenzlTowerStep` at GENERAL rank, for the regular trace

`wenzlTowerStep_H2_H3_trivial` above discharges the field by discarding both
hypotheses — it proves nothing about the ascent. This does the opposite, and the
difference is the point.

Read the field again:

    semisimple_ascend :
      IsSemisimpleRing Hn →
      (∀ y : Hn1, y ≠ 0 → ∃ z, trn1 (y * z) ≠ 0) →
      IsSemisimpleRing Hn1

The **second hypothesis is exactly left-nondegeneracy of `trn1`**. So when `trn1`
is the algebra trace, `QOU.MathlibExt.isSemisimpleRing_of_trace_nondegenerate`
discharges the field from that hypothesis alone — at **every** rank, with no
appeal to any particular `H_n`.

**And the first hypothesis is then redundant.** `IsSemisimpleRing Hn` is never
used. That is a fact about the class worth stating plainly: for the algebra trace
the ascent does not need semisimplicity at the level below, only nondegeneracy at
the level above.

## Scope — the one thing this does NOT settle

It holds for `trn1 = algTrace`. Whether QOU's Markov trace **is** the algebra
trace, or a nonzero multiple of it, is a **separate question and is not settled
here**. If the Markov trace is some other functional, this instance does not
apply to it and the general-`n` ascent for *that* trace remains open. Do not cite
this as "the Wenzl ascent is formalized" without first pinning down which trace
is meant. -/

/-- **`WenzlTowerStep` for the regular trace, at any rank.** Discharged from
left-nondegeneracy alone; the `IsSemisimpleRing Hn` hypothesis is discarded
because it is not needed.

The semisimplicity engine is NOT proved here — it is
`QOU.MathlibExt.isSemisimpleRing_of_regTraceForm_nondegenerate`, which the
corpus has carried since brick B3d (epic `qou-hnhg`). What this adds is only
the adapter: `WenzlTowerStep` states nondegeneracy existentially (`∀ y ≠ 0,
∃ z, tr (y * z) ≠ 0`) where that theorem states it as a left-kernel condition
(`∀ x, (∀ y, B x y = 0) → x = 0`). The two are contrapositives once the unary
trace is `w ↦ trace (L_w)`, since then `tr (y * z) = regTraceForm R Hn1 y z`.

Contrast `wenzlTowerStep_H2_H3_trivial`, which discards BOTH hypotheses and
therefore carries no content. Here the nondegeneracy hypothesis does the work. -/
theorem wenzlTowerStep_regTrace {rank : ℕ}
    {Hn Hn1 : Type*} [Ring Hn] [Ring Hn1] [Algebra R Hn] [Algebra R Hn1]
    [FiniteDimensional R Hn1]
    (q : R) (σn1 : ℕ → Hn1) [HeckeBraidedPresentationOfRank q rank Hn1 σn1]
    (ι : Hn →ₐ[R] Hn1) :
    WenzlTowerStep R q rank Hn Hn1 σn1 ι
      (fun w => LinearMap.trace R Hn1 (Algebra.lmul R Hn1 w)) where
  semisimple_ascend _ hnd := by
    refine QOU.MathlibExt.isSemisimpleRing_of_regTraceForm_nondegenerate (K := R) ?_
    intro x hx
    by_contra hne
    obtain ⟨z, hz⟩ := hnd x hne
    exact hz (hx z)

/-! ## The class is FREE wherever its conclusion holds — and NOTHING consumes it

Two instances above discharge `WenzlTowerStep`: one by discarding both hypotheses
(rank 3), one from nondegeneracy alone for the algebra trace (any rank). This
section records the general shape of the first, and a measurement that reframes
what the class is worth.

**Measured on this corpus, 2026-09-27.** `WenzlTowerStep` occurs **27** times in
the Lean tree: **1** class definition, **2** discharge targets (the two above),
and **24** prose mentions. It occurs in **no instance-hypothesis position** —
`grep -rn '\[WenzlTowerStep' content/ --include=*.lean` returns nothing — and
`semisimple_ascend` is never projected outside this file. **No declaration in the
corpus depends on the class.**

That is worth stating because five files name "a `WenzlTowerStep` instance at the
Markov trace" as an outstanding blocker (`HeckeColimitRadicalDescent`,
`TraceNondegeneracyInsufficient`, `TLTowerRadicalDescent`, `MarkovTraceQuotient`,
`HeckeH4Semisimple`). Nothing there is wrong about the class's *content*; but an
instance cannot unblock a consumer that does not exist, so effort spent obtaining
one buys nothing until something is written that actually takes `[WenzlTowerStep
…]` as a hypothesis.

**And at the Hecke carrier the conclusion is now free outright.**
`QOU.SchurWeyl.isSemisimpleRing_hecke_generic` gives `IsSemisimpleRing (Hecke K q
q⁻¹ n)` for every `n` over any `CharZero` field, under `q ≠ 0` and
`NotRootOfUnity q` only — sorry-free, and it routes through `heckeWedderburn`,
**not** through any Gram determinant (both check `[propext, Classical.choice,
Quot.sound]`). So at that carrier the theorem below applies and the class carries
no information at all.

🛑 **This is not a proof of the Wenzl ascent and must never be cited as one.** It
is the opposite: a witness that the class is contentless whenever its conclusion
is independently available. The genuine ascent question — does semisimplicity
ascend along a *nondegenerate Markov trace*, at a carrier where the conclusion is
NOT already known — is untouched here and stays open (bean `qou-s7z2`).

-- Ref: [leitner2026] beans qou-s7z2, qou-0cyu.
-/

/-- **`WenzlTowerStep` is free wherever its conclusion already holds.**

Given `IsSemisimpleRing Hn1` the field is discharged by ignoring both hypotheses,
at any rank and any carrier. `wenzlTowerStep_H2_H3_trivial` is the `rank = 3`
special case of this; `wenzlTowerStep_regTrace` is the contrasting one, where the
nondegeneracy hypothesis genuinely does the work.

🛑 **Do not cite this as the Wenzl ascent.** It proves that the class says nothing
once its conclusion is known, per AGENTS.md §3b-cond rule 5 — the reason no
instance of it was created at the `wtrace` quotient carrier, where
`WtraceRadicalSemisimple.isSemisimpleRing_traceQuot_of_hecke` makes the conclusion
unconditional. -/
theorem wenzlTowerStep_vacuous_of_isSemisimpleRing {rank : ℕ}
    {Hn Hn1 : Type*} [Ring Hn] [Ring Hn1] [Algebra R Hn] [Algebra R Hn1]
    (q : R) (σn1 : ℕ → Hn1) [HeckeBraidedPresentationOfRank q rank Hn1 σn1]
    (ι : Hn →ₐ[R] Hn1) (trn1 : Hn1 → R)
    (hss : IsSemisimpleRing Hn1) :
    WenzlTowerStep R q rank Hn Hn1 σn1 ι trn1 where
  semisimple_ascend _ _ := hss

end QOU.Machinery.HeckeRank
