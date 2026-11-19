/-
# Selectivity of the `q = 1` collapse on component count

Bean `qou-itdn`.

At `q = 1` the Jones polynomial of a link `L` with `c` components takes the
value `V_L(1) = (-2)^(c-1)` — a function of the component count ALONE, blind
to both knotting and linking (Jones 1985).  Checked on nine links, exactly, in
`computations/qeq1/q_eq_1_interface_selectivity_probe.py`.

This file formalises what follows from that value, NOT the Jones theorem
itself: the collapse is selective on `c`, and it is selective on nothing else.
The theorem worth having is the *only if* direction — `c = 1` is the unique
component count at which the invariant reaches the unknot's value — because
that is what "the interface is transparent exactly to single-component
objects" means.

The statements are over a linearly ordered strict ring, so they hold for the integer
value as well as any real specialisation; nothing here needs `ℝ`, per §7c.
-/
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace QOU.BraidsAndKnots.ComponentCountSelectivity

variable {R : Type*} [Ring R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The `q = 1` value of the Jones polynomial, as a function of the component
count `c ≥ 1`.  This is a DEFINITION of the quantity whose behaviour we study,
not a claim that the Jones polynomial equals it; that is Jones' theorem and is
cited, not reproved. -/
def jonesAtOne (c : ℕ) : R := (-2) ^ (c - 1)

@[simp] theorem jonesAtOne_one : (jonesAtOne 1 : R) = 1 := by
  simp [jonesAtOne]

@[simp] theorem jonesAtOne_two : (jonesAtOne 2 : R) = -2 := by
  norm_num [jonesAtOne]

@[simp] theorem jonesAtOne_three : (jonesAtOne 3 : R) = 4 := by
  norm_num [jonesAtOne]

/-- The magnitude grows without bound in `c`: `|V_L(1)| = 2^(c-1)`. -/
theorem abs_jonesAtOne (c : ℕ) : |(jonesAtOne c : R)| = 2 ^ (c - 1) := by
  simp [jonesAtOne, abs_pow]

/-- **The selectivity theorem.**  Among links, the `q = 1` invariant reaches the
unknot's value `1` exactly when the link has a single component.

This is the mathematical content of "the `q = 1` layer is transparent to
`c = 1` objects and to nothing else".  The forward direction is the one that
does work: it says no multi-component link can hide at the interface. -/
theorem jonesAtOne_eq_one_iff {c : ℕ} (hc : 1 ≤ c) :
    (jonesAtOne c : R) = 1 ↔ c = 1 := by
  constructor
  · intro h
    by_contra hne
    -- `c ≥ 2`, so `|V| = 2^(c-1) ≥ 2 > 1 = |V|`, a contradiction.
    have h2 : 2 ≤ c := lt_of_le_of_ne hc (Ne.symm hne)
    have hpow : (2 : R) ^ 1 ≤ 2 ^ (c - 1) := by
      apply pow_le_pow_right₀ (by norm_num : (1 : R) ≤ 2)
      omega
    have habs : |(jonesAtOne c : R)| = 2 ^ (c - 1) := abs_jonesAtOne c
    rw [h] at habs
    simp only [abs_one] at habs
    rw [← habs] at hpow
    norm_num at hpow
  · rintro rfl
    simp

/-- The invariant separates single-component from multi-component links. -/
theorem jonesAtOne_ne_one_of_two_le {c : ℕ} (hc : 2 ≤ c) :
    (jonesAtOne c : R) ≠ 1 := by
  intro h
  have := (jonesAtOne_eq_one_iff (R := R) (le_trans (by norm_num) hc)).mp h
  omega

/-- **The negative result, and it is the load-bearing one.**  A quantity that is
a function of the component count alone cannot separate two species that share
a component count.

In the framework's own assignments the proton and the neutron are both the
Borromean linking of three quarks, so `c = 3` for each.  Hence no invariant of
this shape distinguishes them, and in particular the `q = 1` collapse cannot
be a charge-separation mechanism: it does not see charge.  Measured statement
of the same fact, with the corpus citations for the assignments, in the probe
named above. -/
theorem no_separation_of_equal_component_count
    (f : ℕ → R) {c c' : ℕ} (h : c = c') : f c = f c' := by
  rw [h]

/-- In the framework's assignments, the proton and neutron are both Borromean
    3-component links (`c = 3`). -/
def protonComponents : ℕ := 3
def neutronComponents : ℕ := 3

theorem protonComponents_eq_neutronComponents :
    protonComponents = neutronComponents := rfl

/-- Specialised to the proton/neutron pair: any component-count function assigns
them the same value, because the framework gives both `c = 3`. -/
theorem proton_neutron_indistinguishable (f : ℕ → R) :
    f protonComponents = f neutronComponents :=
  no_separation_of_equal_component_count f protonComponents_eq_neutronComponents

end QOU.BraidsAndKnots.ComponentCountSelectivity
