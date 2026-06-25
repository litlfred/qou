import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-!
# QOU.AlgebraicSubstrate.AdelicReebRestrictedProduct

The Reeb infinitesimal `ε` decomposes as a **restricted product** of local
infinitesimals `ε_v`, one per place `v` of `ℚ` (Tate-thesis factorisation),
and the surreal `ω`-order `ordw` is **additive over places**:

  `ordw_𝔸(f) = Σ_v ordw_v(f_v)`   (finite sum, restricted-product condition).

Two consequences are formalised here, over an *abstract* common value group
`Γ` — the structural content the owner flagged as "consistent surreal orders
across primes and infinity": for the per-place orders to sum coherently they
must all land in **one** linearly ordered value group, namely the `ω`-grade
of `𝐍𝐨`.

1. `adelic_reeb_order_additive` — the global order of a product is the sum of
   the local orders of its factors (Tate factorisation).
2. `adelic_reeb_squeeze_local_to_global` — if every place weakly dominates and
   at least one place strictly dominates, the global order strictly dominates.
   This is the adelic lift of the per-prime surreal squeeze
   (`lem:surreal-squeeze`): it is *not only* the global `ε`-squeeze that forbids
   rogue zeros, but a separate squeeze at each prime.

The restricted-product condition is encoded by an explicit finite set `S` of
*active* places (those where the local order differs from the archimedean
reference); off `S` the local order is the tame `0`. This is exactly the
"finite sum by restricted-product" qualifier of `rem:adelic-tate-squeeze`.

LaTeX label: `prop:adelic-reeb-restricted-product`

## References

- [tate1967] Tate, "Fourier analysis in number fields and Hecke's zeta-functions".
- [conway1976] Conway, *On Numbers and Games* (the surreal value group).
-/


set_option autoImplicit false
-- The additive theorem does not consume the order instances; silence the
-- (harmless) unused-section-variable linter rather than split the section.
set_option linter.unusedSectionVars false

namespace QOU.AlgebraicSubstrate

universe u

-- `Γ` is the common value group — a linearly ordered abelian group. The bundled
-- `LinearOrderedAddCommGroup` was removed when Mathlib flattened the ordered-
-- algebra hierarchy (≥ v4.24.0); the unbundled triple below is its replacement
-- (verified to compile EXIT=0 against the v4.24.0 Mathlib cache).
variable {ι : Type u} {Γ : Type*}
  [AddCommGroup Γ] [LinearOrder Γ] [IsOrderedCancelAddMonoid Γ]

/-- The global `ω`-order of an adelic observable, as the finite sum of its
    local `ω`-orders over the set `S` of active places (restricted-product
    condition: only finitely many places are active). `ord v` is the local
    `ordw_v`; `Γ` is the common value group (the `ω`-grade of `𝐍𝐨`). -/
def globalOrd (S : Finset ι) (ord : ι → Γ) : Γ := ∑ v ∈ S, ord v

/-- **Tate factorisation / additivity.** The global `ω`-order of a product is
    the sum of the local `ω`-orders of its factors. Multiplicativity of the
    adelic observable corresponds to pointwise addition of local orders. -/
-- Ref: [tate1967] Fourier analysis in number fields (restricted-product factorisation)
theorem adelic_reeb_order_additive
    (S : Finset ι) (a b : ι → Γ) :
    globalOrd S (a + b) = globalOrd S a + globalOrd S b := by
  simp only [globalOrd, Pi.add_apply, Finset.sum_add_distrib]

/-- **Local-to-global surreal squeeze.** If the local order of `a` weakly
    dominates that of `b` at every active place, and *strictly* dominates at
    some place `v₀`, then the global order of `a` strictly dominates that of
    `b`. Applied with `a = δ²·ε⁻¹`, `b = ε³` and the per-place squeeze
    (`lem:surreal-squeeze` at each `v`), this gives the global adelic squeeze
    `ordw_𝔸(δ²·ε⁻¹) > ordw_𝔸(ε³)` of `rem:adelic-tate-squeeze`. -/
-- Ref: [conway1976] On Numbers and Games (ordered value group)
theorem adelic_reeb_squeeze_local_to_global
    (S : Finset ι) (a b : ι → Γ)
    (hle : ∀ v ∈ S, b v ≤ a v)
    (v₀ : ι) (hv₀ : v₀ ∈ S) (hlt : b v₀ < a v₀) :
    globalOrd S b < globalOrd S a :=
  Finset.sum_lt_sum hle ⟨v₀, hv₀, hlt⟩

end QOU.AlgebraicSubstrate
