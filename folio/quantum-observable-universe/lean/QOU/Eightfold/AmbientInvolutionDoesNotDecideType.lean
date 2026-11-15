import QOU.Eightfold.Sym2GateFSTrichotomy

/-!
# QOU.Eightfold.AmbientInvolutionDoesNotDecideType — screening route E

The `N = 3` problem (`eightfold-open-problems.md` item 1) is now sharply
characterised: `Sym2GateFSTrichotomy.gate_forces_complex_of_dim_three` proves
that a three-dimensional object passing the `Sym²` gate **must contain a
complex-type irrep**.  Real and quaternionic constructions are excluded as a
class.  So any candidate route to the flavour triple owes exactly one thing:
a three-dimensional object of **complex** Frobenius–Schur type.

`docs/audits/2026-08-04-pgl3-higher-teichmuller-assessment.md` §2c proposes the
higher-Teichmüller route — a `PGL(3,ℂ)` decoration of the knot complement,
`ρ₃ : π₁(M) → PGL(3,ℂ)` — and offers this reason for believing it clears that
bar:

> The resulting 3-dim fundamental would be non-self-dual (`PGL(3)` is rank 2
> with non-trivial outer automorphism).

That assessment predates the trichotomy theorem (2026-08-26), so it was never
run through the screen.  Running it: **the reason does not support the claim.**
The premise is a property of the *ambient group* — that it admits a non-trivial
duality involution — and the conclusion is a property of *one representation*.
Those are different statements, and this file proves they come apart.

## What is proved

* `fsType_not_determined_by_dual` — over **one and the same** duality datum
  (a fixed-point-free involution on the index set, the model's stand-in for a
  non-trivial outer automorphism), two three-dimensional candidates: one
  passes the gate, one fails it.  So the ambient involution does not decide
  gate passage, at dimension three or any other.
* `selfDual_candidate_not_three` — the screen itself, in the form a route can
  be held to: a candidate whose occurring irreps are all self-dual cannot have
  dimension three, *whatever* the ambient group's outer automorphism does.

## What this does NOT do

It does not refute the higher-Teichmüller route, and it is not evidence against
it.  It removes one stated reason for confidence in it and replaces that reason
with a checkable obligation: exhibit `ρ₃` with `ρ₃ ≇ ρ̄₃`, i.e. an image not
conjugate into a real form.  A `PGL(3,ℝ)` Hitchin representation — the classical
higher-Teichmüller object for surface groups — lands in the self-dual sector and
is excluded by `selfDual_candidate_not_three`; the `PGL(3,ℂ)` gluing-equation
branch (Garoufalidis–Thurston–Zickert, held as `library/arxiv-1207.6711v1`) is
the branch that can survive, and it survives *conditionally on that check*,
which nobody has run for the trefoil, figure-eight or Borromean links.

This is the scope-(a) / scope-(b) distinction of `AGENTS.md` applied to a
positive claim rather than a negative one: §2c's assertion was scoped to the
ambient group and used at the level of the representation.

## Base ring (§7c)

Pure combinatorics over `ℕ`, inherited from the companion.  No ring, no
ordering, no archimedean content.

-- Ref: [fulton-harris1991] §11 (Frobenius–Schur indicator; the real /
-- complex / quaternionic trichotomy).
-- Ref: [leitner2026] `docs/audits/2026-08-04-pgl3-higher-teichmuller-assessment.md`
-- §2c (the claim screened here); `eightfold-open-problems.md` item 1.
-/

namespace QOU.Eightfold.AmbientInvolutionDoesNotDecideType

open QOU.Eightfold.Sym2GateFSTrichotomy

/-! ## 1. The screen, stated generally

The obligation a route to the flavour triple must discharge.  It is the
contrapositive of `even_dimOf_of_selfDual`, and it is what makes "non-self-dual"
the single checkable condition rather than one desideratum among several. -/

/-- **The screen.**  A candidate all of whose occurring irreps are self-dual
cannot be three-dimensional and pass the `Sym²` gate — no matter what duality
involution the ambient group carries.

The ambient group appears nowhere in the hypotheses: the only inputs are the
Frobenius–Schur types of the irreps actually occurring in the object. -/
theorem selfDual_candidate_not_three {S : Finset ℕ} {fs : ℕ → FSType}
    {m dual d : ℕ → ℕ}
    (hgate : Passes S fs m dual)
    (hq : QuaternionicEvenDim S fs d)
    (hsd : ∀ i ∈ S, (fs i).SelfDual) :
    dimOf S m d ≠ 3 := by
  intro hdim
  obtain ⟨c, hc⟩ := even_dimOf_of_selfDual hgate hq hsd
  omega

/-! ## 2. The ambient duality datum

`dualInv` swaps the two indices `0` and `1`: a fixed-point-free involution, the
model's stand-in for "the ambient group has a non-trivial outer automorphism
exchanging a representation with its conjugate".  Both candidates below carry
*this same* datum, which is the point — they differ only in Frobenius–Schur
type, which is a property of the representation, not of the group. -/

/-- The duality involution: `0 ↔ 1`. -/
def dualInv : ℕ → ℕ := fun i => if i = 0 then 1 else 0

theorem dualInv_involutive : ∀ i < 2, dualInv (dualInv i) = i := by decide

/-- Non-trivial: it has no fixed point on `{0, 1}`. -/
theorem dualInv_no_fixed_point : ∀ i < 2, dualInv i ≠ i := by decide

/-! ## 3. Two candidates over that one datum -/

/-- One irrep, occurring once. -/
def mOne : ℕ → ℕ := fun i => if i = 0 then 1 else 0

/-- Three-dimensional. -/
def dThree : ℕ → ℕ := fun _ => 3

/-- The candidate read as **complex** type. -/
def fsComplex : ℕ → FSType := fun _ => .complex

/-- The candidate read as **real** type — same index set, same multiplicities,
same dimensions, same duality involution. -/
def fsReal : ℕ → FSType := fun _ => .real

theorem candidate_dim : dimOf {0} mOne dThree = 3 := by decide

theorem complex_candidate_passes : Passes {0} fsComplex mOne dualInv := by
  unfold Passes sym2Singlets fsComplex mOne dualInv
  decide

theorem real_candidate_fails : ¬ Passes {0} fsReal mOne dualInv :=
  real_triple_fails_gate (Finset.mem_singleton_self 0) rfl (by decide)

/-! ## 4. The conclusion -/

/-- **The ambient involution does not decide the gate.**  Over one fixed
duality datum there are three-dimensional candidates on both sides: one passes
the `Sym²` gate, one fails it.

So an argument of the form *"the ambient group has a non-trivial outer
automorphism, therefore the three-dimensional object it carries is
non-self-dual"* has no force — the conclusion is independent of the premise.
Frobenius–Schur type is a property of the representation. -/
theorem fsType_not_determined_by_dual :
    ∃ (S : Finset ℕ) (m dual d : ℕ → ℕ) (fs₁ fs₂ : ℕ → FSType),
      (∀ i < 2, dual (dual i) = i) ∧ (∀ i < 2, dual i ≠ i) ∧
      dimOf S m d = 3 ∧ Passes S fs₁ m dual ∧ ¬ Passes S fs₂ m dual :=
  ⟨{0}, mOne, dualInv, dThree, fsComplex, fsReal,
    dualInv_involutive, dualInv_no_fixed_point,
    candidate_dim, complex_candidate_passes, real_candidate_fails⟩

end QOU.Eightfold.AmbientInvolutionDoesNotDecideType
