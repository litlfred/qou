import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Tactic

/-!
# QOU.BraidKnot.JucysMurphyCoeff — the ℂ-free core of Identity (B)

Identity (B) — the Plancherel content-square mean, the second half of the keystone-carried
Identity I — is *classically* proved via `Z(ℂ[S_n])` + Jucys–Murphy elements. This file records
the observation (owner question, 2026-06-24) that **ℂ is not needed**, and indeed neither is any
representation theory or `dim(λ)`/SYT/RSK machinery (none of which is in the pinned Mathlib): the
**computational heart** of (B) is a statement about the **identity coefficient of `(Σ involutions)²`
in the group algebra `R[G] = MonoidAlgebra R G` over a *generic* `CommRing R`** (§7c base-ring
discipline — start generic).

`coeff_one_sq_sum_single_involution`: for any group `G` and any finite set `s` of involutions,
the coefficient of `1` in `(Σ_{g∈s} g)²` is `|s|`. Reason: `g·h = 1 ⟺ h = g⁻¹ = g` for
involutions, so only the `|s|` diagonal terms `g·g = 1` contribute.

**Why this is the (B) core.** Applied to the Jucys–Murphy element `X_k = Σ_{i<k}(i k)`
(transpositions are involutions), it gives `coeff_1(X_k²) = #{i<k} = k`, hence
`coeff_1(C₂) = coeff_1(Σ_k X_k²) = Σ_k k = \binom{n}{2}` — the same `\binom{n}{2}` as
`jm_identity_coeff_two` (on main, `IdentityIContentDecomposition.lean`), now with the
*group-algebra coefficient itself* identified over generic `R`, ℂ-free. The remaining bridge to
the partition form `Σ_λ dim(λ)²·Σ_{c∈λ} c(c)²` is the standard regular-representation /
Wedderburn step — over **ℚ** (S_n is a rational group), **not ℂ** — and needs the S_n
block-decomposition infrastructure absent from the pinned Mathlib.

## References
- [manuscript] docs/audits/2026-06-23-keystone-identity-I-content-decomposition.md §"Proof of (B)"
- [manuscript] docs/coordination/s5-so3-keystone.md (Identity I is the one carried RT input)
-/

open MonoidAlgebra Finset

namespace QOU.BraidKnot.JucysMurphyCoeff

variable {R : Type*} [CommRing R]

/-- **ℂ-free core of Identity (B).** In `R[G] = MonoidAlgebra R G` over any `CommRing R`, the
identity coefficient of `(Σ_{g∈s} g)²` is `|s|` whenever every `g ∈ s` is an involution
(`g·g = 1`). Proof: expand the square to `Σ_{g,h} single (g·h) 1`; evaluating at `1` keeps the
terms with `g·h = 1`, i.e. `h = g⁻¹ = g` (involution), so exactly the `|s|` diagonal terms
survive, each contributing `1`. No field, no representation theory — pure group-algebra
combinatorics over generic `R`. -/
theorem coeff_one_sq_sum_single_involution {G : Type*} [Group G] [DecidableEq G]
    (s : Finset G) (hs : ∀ g ∈ s, g * g = 1) :
    ((∑ g ∈ s, single g (1 : R)) ^ 2) (1 : G) = (s.card : R) := by
  have expand : (∑ g ∈ s, single g (1 : R)) ^ 2
      = ∑ g ∈ s, ∑ h ∈ s, single (g * h) (1 : R) := by
    rw [pow_two, Finset.sum_mul]
    refine Finset.sum_congr rfl (fun g _ => ?_)
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl (fun h _ => ?_)
    rw [MonoidAlgebra.single_mul_single, mul_one]
  rw [expand, Finsupp.finset_sum_apply, Finset.card_eq_sum_ones, Nat.cast_sum]
  refine Finset.sum_congr rfl (fun g hg => ?_)
  rw [Finsupp.finset_sum_apply]
  simp only [Finsupp.single_apply, mul_eq_one_iff_inv_eq]
  rw [Finset.sum_ite_eq s g⁻¹]
  have hgi : g⁻¹ = g := inv_eq_of_mul_eq_one_right (hs g hg)
  rw [hgi, if_pos hg, Nat.cast_one]

end QOU.BraidKnot.JucysMurphyCoeff
