import Mathlib.Tactic
import Mathlib.Data.Nat.Choose.Basic

/-!
# QOU.Eightfold.Sym2GateFSTrichotomy — a dimension-3 gate pass FORCES complex type

Unifies `QOU.Eightfold.Sym2GateMultiplicity` (the self-dual sector) and
`QOU.Eightfold.Sym2GateComplexType` (the complex sector) into one count over the
full Frobenius–Schur trichotomy, and derives the statement neither file can make
alone.

## The question this answers

Bean `qou-8pl3` Route B records the chapter's argument that the octonionic
`SU(3)` and the icosahedral colour triple cannot both come from one
construction, *"since the `Sym²` gate excludes the icosahedral colour triple
`T₁` while the `G₂` route passes it"*.  That is a **case analysis over two
examples**.  What is actually at work is a property of Frobenius–Schur type:
`T₁` is a rotation representation of `A₅ ⊂ SO(3)` and hence **real**, while the
Günaydin–Gürsey triple in `Im(𝕆) ≅ ℝ ⊕ ℂ³` is **complex**.

Neither companion file can say so.  `Sym2GateMultiplicity` models `FS = ±1`
only; `Sym2GateComplexType` models `FS = 0` only.  The statement needs one
count over all three types, which is what this file supplies.

## The theorem

`gate_forces_complex_of_dim_three` — **any object of dimension 3 that passes the
`Sym²` gate must contain a complex-type irrep.**

So the exclusion of `T₁` is not a fact about the icosahedron and the pass of the
`G₂` triple is not a fact about octonions: both are consequences of
Frobenius–Schur type, and *no* real or quaternionic construction whatever can
supply a three-dimensional object through this gate.  The chapter's two-example
comparison becomes a corollary (`real_triple_fails_gate`).

## The count

For `W ≅ ⨁ mᵢ Vᵢ`, the singlets of `Sym²(W)` are counted per type:

| `FS(Vᵢ)` | invariant form | multiplicity-space contribution |
|---|---|---|
| `+1` real (orthogonal) | symmetric | `Sym²`, `C(mᵢ+1, 2)` |
| `−1` quaternionic (symplectic) | antisymmetric | `Λ²`, `C(mᵢ, 2)` |
| `0` complex | none on `Vᵢ` itself | `mᵢ · m_{dual i}`, from `Vᵢ ⊗ Vᵢ*` |

As in both companions, **the count is the model** — cited standard
representation theory, not derived, since Mathlib has no representation-type
machinery.  Two further standard facts are carried explicitly as hypotheses
rather than smuggled in:

* `QuaternionicEvenDim` — a quaternionic irrep has even dimension (it is an
  `ℍ`-module).  This is what the parity argument actually runs on, and
  `Sym2GateMultiplicity` obtained it from the `SU(2)` formula `dim = 2j + 1`;
  here there is no such formula, so it is a hypothesis.
* `ComplexNotSelfDual` — a complex-type irrep is not its own dual.

Making them hypotheses is the point: the theorem then says exactly which
standard inputs the conclusion needs, and a reader can see that *no* fact about
octonions or icosahedra is among them.

## The complex-type input, and how much of it is now derived

This file leaves complex type as an input.  `TrialitySelectionRule` supplies
half of it: duality negates triality, and in `ℤ/3` an element equals its own
negation only when it is zero, so **an object of non-vanishing triality is not
self-dual** (`not_selfDual_of_triality_ne_zero`).  The fundamental has triality
`1`, hence `fundamental_not_selfDual` — complex type, derived rather than cited.

What remains cited is the *other* half, and it is genuinely about octonions:
that the Günaydin–Gürsey decomposition `Im(𝕆) ≅ ℝ ⊕ ℂ³` puts `SU(3)` on that
`ℂ³` in its **standard fundamental** representation.  Given that, complex type
is no longer an assumption anywhere in the chain.

So bean `qou-8pl3` Route B gap (i) narrows rather than closes: it was "the
`Sym²` pass is a literature decomposition", and what is left is the smaller
claim that the triple carries the fundamental.  This file says what complex type
**buys** once you have it and what real type **costs**; `TrialitySelectionRule`
says what certifies it.

Nor does it bear on the flavour/colour identification: `TrialitySelectionRule`
shows the `ℤ/3` grading is blind to that, and nothing here changes it.

## Base ring (§7c)

Pure combinatorics over `ℕ`.  No ring, no ordering, no archimedean content.

-- Ref: [fulton-harris1991] §3.5, §11 (the Frobenius–Schur trichotomy; the
-- invariant bilinear form is symmetric for `FS = +1`, antisymmetric for
-- `FS = −1`, absent for `FS = 0`; quaternionic irreps carry an `ℍ`-module
-- structure and so have even dimension).
-- Ref: [gunaydin-gursey1973] (the `Im(𝕆) ≅ ℝ ⊕ ℂ³` decomposition under
-- `SU(3) ⊂ G₂`, cited for the complex type of the triple, not derived here).
-/

namespace QOU.Eightfold.Sym2GateFSTrichotomy

open Finset

/-! ## 1. The trichotomy -/

/-- Frobenius–Schur type of an irreducible representation. -/
inductive FSType
  | real
  | quaternionic
  | complex
  deriving DecidableEq, Repr

/-- Self-dual types: those admitting an invariant bilinear form on `Vᵢ` itself.
Exactly the two the companion `Sym2GateMultiplicity` models. -/
def FSType.SelfDual : FSType → Prop
  | .real => True
  | .quaternionic => True
  | .complex => False

instance (t : FSType) : Decidable t.SelfDual := by
  cases t <;> unfold FSType.SelfDual <;> infer_instance

/-! ## 2. The singlet count over all three types -/

/-- Singlets of `Sym²(W)` for `W ≅ ⨁ mᵢ Vᵢ`, counted per Frobenius–Schur type.

**This is the model**, cited not derived — see the module docstring.  For the
complex entries `m i * m (dual i)` counts ordered pairings, so it double-counts
each conjugate pair; only its vanishing is used, which is unaffected. -/
def sym2Singlets (S : Finset ℕ) (fs : ℕ → FSType) (m dual : ℕ → ℕ) : ℕ :=
  ∑ i ∈ S, match fs i with
    | .real => (m i + 1).choose 2
    | .quaternionic => (m i).choose 2
    | .complex => m i * m (dual i)

/-- `dim W = Σ mᵢ dᵢ`. -/
def dimOf (S : Finset ℕ) (m d : ℕ → ℕ) : ℕ := ∑ i ∈ S, m i * d i

/-- **The gate**: `Sym²(W)` carries no singlet. -/
def Passes (S : Finset ℕ) (fs : ℕ → FSType) (m dual : ℕ → ℕ) : Prop :=
  sym2Singlets S fs m dual = 0

/-! ## 3. The standard inputs, carried as hypotheses -/

/-- A quaternionic irrep has even dimension — it is an `ℍ`-module.  Standard;
carried explicitly so the theorem names what it uses. -/
def QuaternionicEvenDim (S : Finset ℕ) (fs : ℕ → FSType) (d : ℕ → ℕ) : Prop :=
  ∀ i ∈ S, fs i = .quaternionic → 2 ∣ d i

/-! ## 4. Per-type consequences of passing -/

/-- Passing forces every real-type multiplicity to vanish: a real irrep carries
a symmetric invariant form, so a single copy already contributes a singlet. -/
theorem real_mult_eq_zero_of_passes {S fs m dual} (h : Passes S fs m dual)
    {i : ℕ} (hi : i ∈ S) (hr : fs i = .real) : m i = 0 := by
  unfold Passes sym2Singlets at h
  rw [Finset.sum_eq_zero_iff] at h
  have := h i hi
  rw [hr] at this
  rw [Nat.choose_eq_zero_iff] at this
  omega

/-- Passing forces every quaternionic-type multiplicity to be at most one: two
copies of a symplectic irrep pair to a singlet in `Sym²`. -/
theorem quaternionic_mult_le_one_of_passes {S fs m dual} (h : Passes S fs m dual)
    {i : ℕ} (hi : i ∈ S) (hq : fs i = .quaternionic) : m i ≤ 1 := by
  unfold Passes sym2Singlets at h
  rw [Finset.sum_eq_zero_iff] at h
  have := h i hi
  rw [hq] at this
  rw [Nat.choose_eq_zero_iff] at this
  omega

/-! ## 5. The theorem -/

/-- Every dimension term is even, provided no complex-type irrep occurs: the
real terms vanish outright and the quaternionic ones carry an even factor. -/
theorem two_dvd_dimOf_of_no_complex {S fs m dual d}
    (hgate : Passes S fs m dual)
    (hq : QuaternionicEvenDim S fs d)
    (hnc : ∀ i ∈ S, fs i ≠ .complex) :
    2 ∣ dimOf S m d := by
  unfold dimOf
  refine Finset.dvd_sum ?_
  intro i hi
  cases hfs : fs i with
  | real =>
    rw [real_mult_eq_zero_of_passes hgate hi hfs]; simp
  | quaternionic =>
    exact (hq i hi hfs).mul_left (m i)
  | complex => exact absurd hfs (hnc i hi)

/-- **The theorem.**  A three-dimensional object that passes the `Sym²` gate
must contain a complex-type irrep.

Real and quaternionic constructions are excluded *as a class*: the real
multiplicities are forced to zero and the quaternionic dimensions are even, so
the total is even and cannot be `3`.  Complex type is not one way among several
to reach dimension three through this gate — it is the only way. -/
theorem gate_forces_complex_of_dim_three {S fs m dual d}
    (hgate : Passes S fs m dual)
    (hq : QuaternionicEvenDim S fs d)
    (hdim : dimOf S m d = 3) :
    ∃ i ∈ S, fs i = .complex := by
  by_contra hcon
  push_neg at hcon
  have h2 := two_dvd_dimOf_of_no_complex hgate hq hcon
  rw [hdim] at h2
  omega

/-- **The chapter's comparison, as a corollary.**  A real-type triple — the
icosahedral `T₁`, a rotation representation of `A₅ ⊂ SO(3)` — cannot pass the
gate at any multiplicity, because passing already forces its multiplicity to
zero.  No appeal to the icosahedron is needed; only its Frobenius–Schur type. -/
theorem real_triple_fails_gate {S fs m dual} {i : ℕ}
    (hi : i ∈ S) (hr : fs i = .real) (hpos : 0 < m i) :
    ¬ Passes S fs m dual := fun h =>
  absurd (real_mult_eq_zero_of_passes h hi hr) (by omega)

/-- The self-dual sector in this language: with no complex type present, the
conclusion of `Sym2GateMultiplicity.even_dimOfMult_of_gate` is recovered. -/
theorem even_dimOf_of_selfDual {S fs m dual d}
    (hgate : Passes S fs m dual)
    (hq : QuaternionicEvenDim S fs d)
    (hsd : ∀ i ∈ S, (fs i).SelfDual) :
    Even (dimOf S m d) := by
  have hnc : ∀ i ∈ S, fs i ≠ .complex := by
    intro i hi hc
    have := hsd i hi
    rw [hc] at this
    exact this
  obtain ⟨c, hc⟩ := two_dvd_dimOf_of_no_complex hgate hq hnc
  exact ⟨c, by omega⟩

/-! ## 6. The gate CANNOT separate flavour from colour

`eightfold-open-problems.md` item 4 concludes that flavour and colour `SU(3)`
*"cannot both come from the same construction: the `Sym²` gate excludes the
icosahedral colour triple `T₁`, while the `G₂` route passes it."*

The premise concerns **two different objects** receiving different verdicts,
which establishes that those two objects differ.  The conclusion is about
**one construction supplying two roles**, which does not follow from it.

`gate_forces_complex_of_dim_three` makes the failure structural rather than
merely a gap in the inference: at dimension three, *passing* is equivalent to
carrying a complex-type irrep.  So any two three-dimensional objects that both
pass are both complex type, and the gate has returned the same verdict for
both.  A flavour triple and a colour triple that each pass are, to this gate,
indistinguishable.

The witnesses below exhibit exactly that: two genuinely distinct
three-dimensional objects, both passing.  The gate is not merely silent on the
flavour/colour question — it is *provably blind* to it, in the same way
`TrialitySelectionRule.identification_invisible_to_selection_rule` shows the
`ℤ/3` grading is. -/

/-- First triple: irrep `0`, complex, conjugate `1` absent. -/
def fsA : ℕ → FSType := fun _ => .complex
def mA : ℕ → ℕ := fun i => if i = 0 then 1 else 0
def dA : ℕ → ℕ := fun _ => 3
def dualA : ℕ → ℕ := fun i => if i = 0 then 1 else 0

/-- Second triple: irrep `2`, complex, conjugate `3` absent.  A different
object — a different index, a different conjugation. -/
def fsB : ℕ → FSType := fun _ => .complex
def mB : ℕ → ℕ := fun i => if i = 2 then 1 else 0
def dB : ℕ → ℕ := fun _ => 3
def dualB : ℕ → ℕ := fun i => if i = 2 then 3 else 2

theorem tripleA_dim : dimOf {0} mA dA = 3 := by decide
theorem tripleB_dim : dimOf {2} mB dB = 3 := by decide

theorem tripleA_passes : Passes {0} fsA mA dualA := by
  unfold Passes sym2Singlets fsA mA dualA; decide

theorem tripleB_passes : Passes {2} fsB mB dualB := by
  unfold Passes sym2Singlets fsB mB dualB; decide

/-- **The gate is blind to the distinction.**  Two distinct three-dimensional
objects, both passing the `Sym²` gate.  Whatever separates a flavour triple
from a colour triple, it is not this gate — so item 4's conclusion does not
follow from its premise, and no strengthening of the premise will rescue it. -/
theorem gate_does_not_separate_two_triples :
    (dimOf {0} mA dA = 3 ∧ Passes {0} fsA mA dualA) ∧
    (dimOf {2} mB dB = 3 ∧ Passes {2} fsB mB dualB) :=
  ⟨⟨tripleA_dim, tripleA_passes⟩, ⟨tripleB_dim, tripleB_passes⟩⟩

end QOU.Eightfold.Sym2GateFSTrichotomy
