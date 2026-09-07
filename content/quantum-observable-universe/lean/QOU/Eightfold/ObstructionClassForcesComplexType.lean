import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Group
import Mathlib.Algebra.Group.TypeTags.Basic

/-!
# QOU.Eightfold.ObstructionClassForcesComplexType — self-duality forces a trivial obstruction

`AmphichiralHolonomyIsSelfDual` pruned route E's **geometric** leg: the holonomy of an
amphichiral knot is self-dual, hence not the complex-type object the flavour gate needs.
What survived was a *non-geometric* boundary-unipotent `PGL(3,ℂ)` representation.

Searching for one of those means decomposing a Ptolemy variety, which is expensive.  This
file replaces that search with an arithmetic obstruction, and the payoff is that a whole
**obstruction class** can be certified complex type at once, without solving anything.

## The argument

A boundary-unipotent `PGL(3,ℂ)` representation `ρ` carries an obstruction class
`σ(ρ) ∈ H²(M, ∂M; ℤ/3)`: lift each generator to `SL(3,ℂ)`, and the failure of the
relations is a 2-cocycle valued in the centre `μ₃`.

Two facts about that class are **topological inputs**, carried here as the explicit
hypotheses of `ObstructionDuality` rather than asserted:

* `obs_dual` — duality negates the class.  Lifting `ρ* = ᵗρ⁻¹` means inverse-transposing
  the lifts, and a central `ζ • 1 ↦ ζ⁻¹ • 1`, so the cocycle inverts.
* `obs_congr` — isomorphic representations have equal classes (the class is an invariant
  of `ρ` up to conjugation).

Given both, self-duality forces `σ = -σ`, so `2σ = 0`; and `2` is invertible mod `3`, so
`σ = 0`.  Contrapositive: **no representation in a non-trivial obstruction class is
self-dual.**  That is `not_selfDual_of_obs_ne_zero`, the form a search actually uses —
it reduces "exhibit a complex-type representation" to "exhibit *any* point of the Ptolemy
variety in a non-trivial class", i.e. to the ideal being proper.

## Scope

This proves an implication about any structure satisfying the two hypotheses, and says
nothing about whether such a representation exists for a given manifold.  Non-emptiness
is a separate, computational question.

**Both hypotheses are now DERIVED, not cited (2026-09-06).**  This section previously
called them "the cited topological facts"; they are two-line computations from the
definition of the cocycle, and neither needs a topological input.

Write `c(g,h)` for the cocycle of a lift `s`, i.e. `s g * s h * (s (g*h))⁻¹`, central by
construction.

* `obs_dual`.  Inverse-transpose `φ : A ↦ ᵗA⁻¹` is a group HOMOMORPHISM, not an
  anti-homomorphism: `(AB)⁻ᵀ = ᵗ(B⁻¹A⁻¹) = A⁻ᵀB⁻ᵀ`.  So the dual lift `φ ∘ s` has
  cocycle `φ(c(g,h))`, and `φ` inverts the centre (`ζ•1 ↦ ζ⁻¹•1`), giving `c⁻¹`.
* `obs_congr`.  A conjugate lift `a * s · * a⁻¹` has cocycle `a * c(g,h) * a⁻¹`, which
  equals `c(g,h)` because `c` is central.

The `obs_dual` step is additionally verified in the RELATIVE setting the Ptolemy
obstruction actually lives in — `H²(M, ∂M; ℤ/3)`, not `H²(Γ; μ₃)`.  Negating the cocycle
acts on the Ptolemy variety exactly as `u ↦ u²`, the nontrivial automorphism of `μ₃`:
`P^c` and `P^{-c}` differ in 10 of 33 equations, and substituting `u ↦ u²` throughout
`P^c` reproduces `P^{-c}` as polynomial sets, on classes 1, 2 and 3
(`computations/ptolemy/ptolemy_duality_galois_check.py`, 3/3).  Corroborated
independently by snappy, whose enumeration quotients `H²` by the units of `ℤ/N` —
at `N = 3` the units are `{1,2}` and `2 = -1`, which is why 27 classes present as 14.

**NOT YET FORMALISED.**  The class is still carried as hypotheses here because turning
the two derivations into Lean needs an explicit cocycle model over Mathlib's group theory,
and the container that derived them could not restore a Mathlib cache to check it.  So
this is a statement about what is now PROVED ON PAPER, not about what Lean has verified —
the declarations below are unchanged and still assume the class.

Empirically consistent: for `4₁` at `n = 3`, obstruction class 0 has 6 solutions of which
4 are self-dual, while the non-trivial class has 2 solutions and **none** are self-dual.
-/

namespace QOU.Eightfold

/-- In `ZMod n` with `n = 2m+1` odd, `x + x = 0` forces `x = 0`: `2` is invertible. -/
theorem eq_zero_of_add_self_eq_zero_odd {n m : ℕ} (hn : n = 2 * m + 1)
    (x : ZMod n) (h : x + x = 0) : x = 0 := by
  have hcast : (2 : ZMod n) * (m : ZMod n) + 1 = 0 := by
    have hz : ((2 * m + 1 : ℕ) : ZMod n) = 0 := by
      rw [← hn]; exact ZMod.natCast_self n
    push_cast at hz
    exact hz
  have key : ((m : ZMod n) + 1) * (x + x) = x := by
    calc ((m : ZMod n) + 1) * (x + x)
        = (2 * (m : ZMod n) + 1) * x + x := by ring
      _ = 0 * x + x := by rw [hcast]
      _ = x := by ring
  rw [h, mul_zero] at key
  exact key.symm

/-- The `ℤ/3` case used by the obstruction argument. -/
theorem eq_zero_of_eq_neg_zmod_three (x : ZMod 3) (h : x = -x) : x = 0 := by
  refine eq_zero_of_add_self_eq_zero_odd (m := 1) rfl x ?_
  -- `rw [h]` would rewrite BOTH occurrences, leaving `-x + -x = 0`, which needs
  -- the very fact being proved.  `linear_combination` uses `h` once.
  linear_combination h

/-- The two topological inputs, named so the theorem below wears what it uses.

`obs` is the obstruction class to lifting a boundary-unipotent `PGL(3,ℂ)` representation
to `SL(3,ℂ)`; `dual` is `ρ ↦ ᵗρ⁻¹`; `Iso` is isomorphism of representations. -/
class ObstructionDuality (Rep : Type*) (Iso : Rep → Rep → Prop) (dual : Rep → Rep)
    (obs : Rep → ZMod 3) : Prop where
  /-- Duality negates the obstruction class. -/
  obs_dual : ∀ ρ, obs (dual ρ) = - obs ρ
  /-- The obstruction class is an isomorphism invariant. -/
  obs_congr : ∀ ρ τ, Iso ρ τ → obs ρ = obs τ

variable {Rep : Type*} {Iso : Rep → Rep → Prop} {dual : Rep → Rep} {obs : Rep → ZMod 3}

/-- A self-dual representation has trivial obstruction class. -/
theorem obs_eq_zero_of_selfDual [inst : ObstructionDuality Rep Iso dual obs]
    (ρ : Rep) (h : Iso ρ (dual ρ)) : obs ρ = 0 :=
  eq_zero_of_eq_neg_zmod_three _ ((inst.obs_congr ρ (dual ρ) h).trans (inst.obs_dual ρ))

/-- **The form a search uses.**  Every representation in a non-trivial obstruction class
fails to be self-dual — hence is of complex type, with no variety decomposition required. -/
theorem not_selfDual_of_obs_ne_zero [ObstructionDuality Rep Iso dual obs]
    (ρ : Rep) (h : obs ρ ≠ 0) : ¬ Iso ρ (dual ρ) :=
  fun hsd => h (obs_eq_zero_of_selfDual ρ hsd)

/-! ## The cocycle model — where the two hypotheses come from

`ObstructionDuality` above carries `obs_dual` and `obs_congr` as hypotheses.  This section
proves their group-theoretic content, so they are no longer bare assumptions: each is a
short computation with the *definition* of the obstruction cocycle, and neither needs a
topological input.

Write `cocycle s g h = s g * s h * (s (g * h))⁻¹` for the failure of a set-theoretic lift
`s` to be multiplicative.  For a lift of a `PGL(n,ℂ)` representation to `SL(n,ℂ)` this
lands in the centre `μ_n`, and its class is the obstruction.

* `cocycle_dual` is `obs_dual`.  Inverse-transpose `φ : A ↦ ᵗA⁻¹` is a group
  **homomorphism**, not an anti-homomorphism — `(AB)⁻ᵀ = ᵗ(B⁻¹A⁻¹) = A⁻ᵀB⁻ᵀ` — so by
  `cocycle_map` the dual lift's cocycle is `φ` applied to the original, and `φ` inverts
  the centre.
* `cocycle_conj_of_comm` is `obs_congr`.  Conjugating a lift conjugates its cocycle, and a
  cocycle commuting with the conjugator is unchanged — which centrality supplies.

**Scope.** This is the group theory, machine-checked.  Instantiating `ObstructionDuality`
for the Ptolemy setting additionally needs the identification `μ₃ ≅ ZMod 3` and the
*relative* class in `H²(M, ∂M; ℤ/3)` rather than `H²(Γ; μ₃)`; that relative step is
verified computationally, not here — negating the cocycle acts on the Ptolemy variety as
`u ↦ u²` (`computations/ptolemy/ptolemy_duality_galois_check.py`, classes 1/2/3). -/

section CocycleModel

variable {Γ G : Type*} [Group Γ] [Group G]

/-- The failure of a set-theoretic lift `s` to be multiplicative. -/
def cocycle (s : Γ → G) (g h : Γ) : G := s g * s h * (s (g * h))⁻¹

/-- A homomorphism applied to a lift carries its cocycle along. -/
theorem cocycle_map (φ : G →* G) (s : Γ → G) (g h : Γ) :
    cocycle (fun x => φ (s x)) g h = φ (cocycle s g h) := by
  simp [cocycle, map_mul, map_inv]

/-- **`obs_dual`, as group theory.**  If `φ` inverts the cocycle's value — as
inverse-transpose does on the centre — then the dual lift's cocycle is the inverse. -/
theorem cocycle_dual (φ : G →* G) (s : Γ → G) (g h : Γ)
    (hφ : φ (cocycle s g h) = (cocycle s g h)⁻¹) :
    cocycle (fun x => φ (s x)) g h = (cocycle s g h)⁻¹ := by
  rw [cocycle_map]; exact hφ

/-- Conjugating a lift conjugates its cocycle. -/
theorem cocycle_conj (a : G) (s : Γ → G) (g h : Γ) :
    cocycle (fun x => a * s x * a⁻¹) g h = a * cocycle s g h * a⁻¹ := by
  simp only [cocycle, mul_inv_rev, inv_inv]
  group

/-- **`obs_congr`, as group theory.**  A cocycle commuting with the conjugator — which
centrality supplies — is unchanged by conjugating the lift. -/
theorem cocycle_conj_of_comm (a : G) (s : Γ → G) (g h : Γ)
    (hc : a * cocycle s g h = cocycle s g h * a) :
    cocycle (fun x => a * s x * a⁻¹) g h = cocycle s g h := by
  rw [cocycle_conj, hc]; group

/-- **The `μ₃ ≅ ZMod 3` bridge.**  `cocycle_dual` says the dual lift's cocycle is the
*inverse*; `obs_dual` says the class *negates*.  Transporting along an isomorphism of the
centre with `Multiplicative (ZMod 3)` is what turns one into the other — inversion in the
group is negation in `ZMod 3`.

With this, the algebraic chain behind `obs_dual` is complete: inverse-transpose is a
homomorphism (`cocycle_map`), it inverts the centre (`cocycle_dual`), and inversion of a
`μ₃` value is negation of a `ZMod 3` value (here).  What is still missing for a genuine
`instance` is only the passage from a *cocycle* to its *cohomology class* — H² machinery
— and the relative-vs-absolute step, which is checked computationally instead. -/
theorem obs_neg_of_inv {Z : Type*} [Group Z] (e : Z ≃* Multiplicative (ZMod 3)) (z : Z) :
    (e z⁻¹).toAdd = - (e z).toAdd := by
  rw [map_inv]; rfl

end CocycleModel

end QOU.Eightfold
