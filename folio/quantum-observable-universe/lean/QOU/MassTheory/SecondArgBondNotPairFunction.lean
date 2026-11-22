import QOU.MassTheory.ChainBondOrderDependence

/-!
# A bond that reads only the second nucleon is not a pair function at all

Bean `qou-ix0x`, PR #7287.  This is the Lean form of one measurement from
`computations/probes/gamma_gamma_bond_is_pair_independent_probe.py`, and it
upgrades that measurement from a *number* to a *shape* statement.

## What was measured

Under the owner's γγ ruling (bean `qou-ales`) the selected interface bond is
`G³ = (σ₂σ₃⁻¹)³`.  Its bond factor `μ` was measured on all four ORDERED
nucleon pairs at the proton anchor, 60 dps:

    μ(p,p) = 1.00105775254515984      μ(n,p) = 1.00105775254515984
    μ(p,n) = 1.00061119140688078      μ(n,n) = 1.00061119140688078

so `μ a b` depends only on `b` — the SECOND nucleon — to `1.6e-61`, while
`μ(p,n) ≠ μ(n,p)` by `4.47e-4`.

## What is proved here, and why it is stronger than "order-dependent"

`ChainBondOrderDependence.bondOf` is the corpus's bond scalar,

    bondOf Lpp Lpn Lnn a b = if a = b then (if a then Lpp else Lnn) else Lpn

and it is **symmetric in `a` and `b` by construction** (`bondOf_comm` below):
`a = b` is a symmetric condition and both unlike orders take the same `Lpn`.

So a second-argument-only bond is not merely *arrangement-dependent* in the
sense `orderIndependent_iff` analyses — `secondOnly_eq_bondOf_iff` shows it is
**not of the `bondOf` form at all** unless it is constant.  The corpus's whole
chain analysis (`bondSum`, `orderIndependent_iff`, `not_orderIndependent_of_ne`)
is stated over `bondOf`, so a non-constant one falls outside its domain rather
than violating its conclusion.  That is the difference between "this bond breaks
arrangement-invariance" and "this bond is not the kind of object the framework's
bond calculus is about".

**This does NOT say the γγ bond is wrong**, and it does not touch the γγ word
selection, which is `qou-ales`'s.  It says that IF a bond factor reads only one
endpoint, THEN the chain machinery does not apply to it unmodified.  Whether the
measured one-sidedness is a placement artefact or a real feature is open; the
probe records the mechanism as measured, not proved.

## Anti-vacuity

`secondOnly_const_is_bondOf` exhibits the constant case *inside* the family, so
the iff is not vacuously true on one side, and `bondOf_ne_secondOnly_witness`
gives an explicit two-element witness that the exclusion has content.

## Base ring (§7c)

Fully generic: `bondOf` carries no typeclass, and nothing here needs an order,
a `Real`, or any archimedean construct.  The decomposition section asks only for
`CommRing`.

-- Ref: [leitner2026] bean `qou-ix0x`; probe
--      `gamma_gamma_bond_is_pair_independent_probe`
-/

set_option autoImplicit false

namespace QOU.MassTheory.SecondArgBondNotPairFunction

open QOU.MassTheory.ChainBondOrderDependence

variable {R : Type*}

/-- A bond scalar that reads only the **second** nucleon of the ordered pair.
This is the shape the γγ bond factor was measured to have. -/
def secondOnly (f : Bool → R) (_a b : Bool) : R := f b

/-- `bondOf` is symmetric in its two nucleon arguments, by construction. -/
theorem bondOf_comm (Lpp Lpn Lnn : R) (a b : Bool) :
    bondOf Lpp Lpn Lnn a b = bondOf Lpp Lpn Lnn b a := by
  unfold bondOf
  cases a <;> cases b <;> simp

/-- A second-argument-only bond is symmetric exactly when it is constant. -/
theorem secondOnly_comm_iff (f : Bool → R) :
    (∀ a b, secondOnly f a b = secondOnly f b a) ↔ f true = f false := by
  constructor
  · intro h
    exact h false true
  · intro h a b
    unfold secondOnly
    cases a <;> cases b <;> simp [h]

/-- **The exclusion.** A second-argument-only bond lies in the `bondOf` family
only when it is constant. -/
theorem secondOnly_eq_bondOf_iff (f : Bool → R) :
    (∃ Lpp Lpn Lnn : R, ∀ a b, secondOnly f a b = bondOf Lpp Lpn Lnn a b)
      ↔ f true = f false := by
  constructor
  · rintro ⟨Lpp, Lpn, Lnn, h⟩
    have h1 : f true = Lpn := by simpa [secondOnly, bondOf] using h false true
    have h2 : f false = Lpn := by simpa [secondOnly, bondOf] using h true false
    rw [h1, h2]
  · intro h
    refine ⟨f true, f false, f false, ?_⟩
    intro a b
    unfold secondOnly bondOf
    cases a <;> cases b <;> simp [h]

/-- The contrapositive — the form the measurement lands in.  `μ(p,p) ≠ μ(n,n)`
was measured, so the γγ bond factor is not any `bondOf`. -/
theorem not_exists_bondOf_of_ne (f : Bool → R) (hne : f true ≠ f false) :
    ¬ ∃ Lpp Lpn Lnn : R, ∀ a b, secondOnly f a b = bondOf Lpp Lpn Lnn a b :=
  fun hex => hne ((secondOnly_eq_bondOf_iff f).mp hex)

/-- Anti-vacuity: the constant case really is inside the family, so the iff does
not hold merely because its left side is always false. -/
theorem secondOnly_const_is_bondOf (c : R) :
    ∃ Lpp Lpn Lnn : R, ∀ a b, secondOnly (fun _ => c) a b = bondOf Lpp Lpn Lnn a b :=
  (secondOnly_eq_bondOf_iff (fun _ => c)).mpr rfl

/-- Anti-vacuity the other way: an explicit non-constant `f` over `Bool`, so the
excluded case is inhabited too. -/
theorem bondOf_ne_secondOnly_witness :
    ¬ ∃ Lpp Lpn Lnn : Bool, ∀ a b, secondOnly (fun b => b) a b = bondOf Lpp Lpn Lnn a b :=
  not_exists_bondOf_of_ne (fun b => b) (by decide)

section Decomposition

variable {ι : Type*} [CommRing R]

/-- **The cross-arc reconciliation** (`qou-99qc` / #7295), in Lean.

A sibling arc proves the alternating character is order-blind: a 1-dimensional
representation sends a word to a product of scalars, so it sees only the
multiset of letter shifts.  This probe measured a Markov-trace ratio that IS
order-dependent.  The two are consistent, and this says exactly why: whenever
every 1-dimensional block agrees on the two words, the whole difference of a
`y`-weighted character sum is carried by the blocks of dimension `≠ 1`.

Measured companion (`H₆`, `G³`, 60 dps): the 1-dimensional blocks `(6)` and
`(1⁶)` contribute `9.0e-62` in total — the arithmetic floor — against `1.729e-3`
from the rest. -/
theorem weighted_diff_supported_on_multidim
    (s : Finset ι) (dim : ι → ℕ) (y χ χ' : ι → R)
    (h1 : ∀ i ∈ s, dim i = 1 → χ i = χ' i) :
    ∑ i ∈ s, y i * (χ i - χ' i)
      = ∑ i ∈ s.filter (fun i => dim i ≠ 1), y i * (χ i - χ' i) := by
  classical
  rw [← Finset.sum_filter_add_sum_filter_not s (fun i => dim i ≠ 1)
        (fun i => y i * (χ i - χ' i))]
  have hzero : ∑ i ∈ s.filter (fun i => ¬ (dim i ≠ 1)), y i * (χ i - χ' i) = 0 := by
    refine Finset.sum_eq_zero ?_
    intro i hi
    rw [Finset.mem_filter] at hi
    obtain ⟨his, hd⟩ := hi
    have : dim i = 1 := by simpa using hd
    rw [h1 i his this, sub_self, mul_zero]
  rw [hzero, add_zero]

end Decomposition

end QOU.MassTheory.SecondArgBondNotPairFunction
