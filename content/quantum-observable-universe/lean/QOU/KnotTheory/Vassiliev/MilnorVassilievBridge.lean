import QOU.KnotTheory.Vassiliev.FiniteTypeInvariant
import QOU.MassTheory.MilnorParitySignLaw
import Mathlib.Tactic

/-!
# The Milnor = leading-Vassiliev bridge (honest conjecture classes)

This file states — as **content-bearing conjecture classes** (§3b-tax: real
`Prop` fields carrying the claim's shape, **no instance**) — the two deep
theorems that connect the finite-type scaffold (`FiniteTypeInvariant.lean`,
`WeightSystem.lean`) to Milnor's link invariants, and hooks them to #4471's
`leadingOrder A = 2(A−1)` (`QOU.MassTheory.MilnorParitySignLaw`).

**None of these deep theorems is proved here, and none is axiomatized.** They
are open in Mathlib; the classes carry the falsifiable content and are left
*instance-less*.  Downstream we prove one *conditional* result (§3b-cond): given
the bridge class, the A-component Brunnian link's first non-vanishing Vassiliev
invariant sits at degree `leadingOrder A` and equals `±μ̄(12…A) = ±1` — the
exact-order refinement #4471's general `MilnorExactOrder` conjecture requires.

## The two conjecture classes

* `SymbolIsWeightSystem` — **Kontsevich universality** (Bar-Natan 1995,
  Kontsevich): the degree-`m` symbol of an order-`≤ m` finite-type invariant
  descends to a weight system on `ChordDiagram m` (mod 1T + 4T), and every
  weight system is so realized.
* `BrunnianVassilievBridge` — the **Milnor = leading-Vassiliev bridge**
  (Bar-Natan 1995; Habegger–Masbaum 2000; Meilhan–Yasuhara): the first
  non-vanishing Vassiliev invariant of an `A`-component Brunnian link is at
  degree exactly `2(A−1)` and equals `±μ̄(12…A) = ±1`.

## References

* Bar-Natan, *On the Vassiliev knot invariants*, Topology 34 (1995) 423–472,
  <https://doi.org/10.1016/0040-9383(95)93237-2>.
* Habegger–Masbaum, *The Kontsevich integral and Milnor's invariants*, Topology
  39 (2000) 1253–1289, <https://doi.org/10.1016/S0040-9383(99)00041-5>.
* Meilhan–Yasuhara, *Milnor invariants and the HOMFLYPT polynomial*, Geom.
  Topol. 16 (2012) 889–917, <https://doi.org/10.2140/gt.2012.16.889>.
-/

namespace QOU.KnotTheory.Vassiliev

universe u v

/-! ## Conjecture class 1 — Kontsevich universality (symbol = weight system) -/

/-- **Conjecture class (primary): the symbol of a finite-type invariant is a
weight system.** For a type `K` of knots with a `VassilievSetup S` and a chord-
diagram assignment `chord` (the double-point pattern of a singular object), the
degree-`m` symbol of every order-`≤ m` invariant descends to a weight system on
`ChordDiagram m` modulo the 1T and 4T relations, and conversely every weight
system arises as such a symbol (Kontsevich integral universality).

Honest scope: this is Kontsevich's theorem, **open in Mathlib**; the class is
content-bearing and **instance-less**.  It is NOT axiomatized. -/
class SymbolIsWeightSystem (K : Type u) (S : VassilievSetup.{u, v} K)
    (chord : ∀ {m : ℕ}, S.Sing m → ChordDiagram m) : Prop where
  /-- Every order-`≤ m` invariant's symbol equals a weight system evaluated on
  the chord diagram of the double-point pattern. -/
  symbol_is_weight : ∀ (m : ℕ) (val : K → ℤ), S.IsFiniteType m val →
    ∃ w : WeightSystem ℤ m, ∀ s : S.Sing m,
      S.symbol val m s = w (AReduced.mk (chord s))
  /-- Every weight system is realized as the symbol of some order-`≤ m`
  invariant (universality / surjectivity of the symbol map). -/
  weight_is_realized : ∀ (m : ℕ) (w : WeightSystem ℤ m),
    ∃ val : K → ℤ, S.IsFiniteType m val ∧
      ∀ s : S.Sing m, S.symbol val m s = w (AReduced.mk (chord s))

/-! ## Conjecture class 2 — the Milnor = leading-Vassiliev bridge -/

/-- **Conjecture class (primary): Milnor = leading Vassiliev for Brunnian
links.** For a family `brunnian : ℕ → K` of `A`-component Brunnian links, the
first non-vanishing Vassiliev invariant of `brunnian A` sits at degree exactly
`2(A−1)` and equals `±μ̄(12…A) = ±1`:

* there is an order-`≤ 2(A−1)` invariant taking value `±1` on `brunnian A`
  (the Milnor μ̄-invariant realized as a Vassiliev invariant); and
* every invariant of strictly lower order vanishes on `brunnian A` (the link is
  Vassiliev-trivial below degree `2(A−1)`).

Honest scope: this is the Bar-Natan / Habegger–Masbaum / Meilhan–Yasuhara
theorem, **open in Mathlib**; the class is content-bearing and **instance-less**.
It is NOT axiomatized — precisely the exact-order input #4471 needs. -/
class BrunnianVassilievBridge (K : Type u) (S : VassilievSetup.{u, v} K)
    (brunnian : ℕ → K) : Prop where
  /-- At degree `2(A−1)` the Milnor μ̄-invariant is realized as a Vassiliev
  invariant taking value `±1` on the `A`-component Brunnian link. -/
  muBar_realized : ∀ A : ℕ, 2 ≤ A → ∃ val : K → ℤ,
    S.IsFiniteType (2 * (A - 1)) val ∧ (val (brunnian A) = 1 ∨ val (brunnian A) = -1)
  /-- The link is Vassiliev-trivial below degree `2(A−1)`: every invariant of
  order `< 2(A−1)` vanishes on it (first non-vanishing invariant is at
  `2(A−1)`). -/
  vassiliev_trivial_below : ∀ A : ℕ, 2 ≤ A → ∀ val : K → ℤ,
    S.IsFiniteType (2 * (A - 1) - 1) val → val (brunnian A) = 0

/-! ## Alignment with #4471 and the conditional exact-order result -/

open QOU.MassTheory.MilnorParitySignLaw in
/-- The Vassiliev degree `2(A−1)` used by the bridge class is #4471's leading
Milnor order `leadingOrder A`. (Alignment check between the two independently
defined quantities.) -/
theorem vassilievDegree_eq_leadingOrder (A : ℕ) :
    2 * (A - 1) = leadingOrder A := rfl

open QOU.MassTheory.MilnorParitySignLaw in
/-- **(CONDITIONAL on `BrunnianVassilievBridge`.)** Given the Milnor =
leading-Vassiliev bridge, the `A`-component Brunnian link (`A ≥ 2`) carries a
Vassiliev invariant of order `leadingOrder A = 2(A−1)` taking value `±1` there
(the μ̄-invariant), and every strictly-lower-order invariant vanishes on it.

This is the exact-order statement #4471's general `MilnorExactOrder` conjecture
needs: the leading Milnor order is *exactly* `2(A−1)` (not merely `≥`), the
missing refinement of `MilnorParitySignLaw`.  The only unproved input is the
class instance (§3b-cond). -/
theorem brunnian_exact_leadingOrder
    {K : Type u} (S : VassilievSetup.{u, v} K) (brunnian : ℕ → K)
    [h : BrunnianVassilievBridge K S brunnian] (A : ℕ) (hA : 2 ≤ A) :
    (∃ val : K → ℤ, S.IsFiniteType (leadingOrder A) val ∧
        (val (brunnian A) = 1 ∨ val (brunnian A) = -1))
      ∧ (∀ val : K → ℤ, S.IsFiniteType (leadingOrder A - 1) val →
        val (brunnian A) = 0) := by
  refine ⟨?_, ?_⟩
  · -- `leadingOrder A` is definitionally `2 * (A - 1)`, so the field applies directly.
    obtain ⟨val, hft, hval⟩ := h.muBar_realized A hA
    exact ⟨val, hft, hval⟩
  · intro val hlow
    exact h.vassiliev_trivial_below A hA val hlow

end QOU.KnotTheory.Vassiliev
