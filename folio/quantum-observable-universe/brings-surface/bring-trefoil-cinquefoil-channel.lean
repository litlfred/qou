import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.RingTheory.RootsOfUnity.Complex


/-!
# QOU.BringChiralCinquefoil — the trefoil + cinquefoil channel in Bring's Σ₄

The geometric scaffold behind the H₂S Bring `1/√5`
([`conj:h2s-angle-s3-braid-holonomy`](../molecular-construction/h2s-angle-s3-braid-holonomy.md)).
Two **distinct** torus knots live in Bring's genus-4 Seifert fibre `Σ₄`,
linked by the ambient `Aut(B) = S₅` — *not* one fibre with two symmetries:

  * **3-fold — the chiral channel.** The color-tube cubic (3 roots `r,g,b`,
    branch monodromy `B₃ ↠ H₃`) is the **trefoil `T_{2,3}`** (Seifert genus 1),
    the `c_λ=0` `(2,1)` chirality cell.
  * **5-fold — the √5.** `S₅` contains a cyclic `ℤ₅`; the hyperelliptic quintic
    `𝒳₅ : y² = x⁵ − 1` is embedded (not a cover) by the first Lagrange resolvent
    `w₁` of that `ℤ₅ ⊂ S₅`, its 5 branch points one `ℤ₅`-orbit. This is the
    **cinquefoil `T_{2,5}`** (Seifert genus 2).

Both embed in `Σ₄` (genus 1, 2 ≤ 4), they are distinct, and the `ℤ₅`-orbit
quadratic Gauss sum `g = Σ_k ζ₅^{k²}` satisfies `g² = 5` (`p = 5 ≡ 1 (mod 4)`),
the unique source of `ζ₅`'s irrationality over `ℚ` — the √5 carried by `w₁`.

LaTeX label: `prop:bring-trefoil-cinquefoil-channel`

**Ground ring**: `ℕ` (genus combinatorics) and `ℂ` (`ζ₅`, Gauss sum).

Self-contained per the block-level convention (`x5-z5-automorphism.lean`): the
genus formula and `ζ₅` are re-defined locally. **All three theorems are proved
sorry-free** — the genus/embedding/distinctness combinatorics by `decide`,
`ζ₅⁵ = 1` and the Gauss-sum `g² = 5` from `Complex.isPrimitiveRoot_exp` plus the
cyclotomic relation. Verified under Lean 4.24.0 + Mathlib.
-/

namespace QOU.BringChiralCinquefoil

open Complex

/-- Genus of Bring's genus-4 Seifert fibre `Σ₄`. -/
def bringsGenus : ℕ := 4

/-- Seifert genus of the torus knot `T_{m,n}`: `g = (m-1)(n-1)/2`. -/
def torusKnotGenus (m n : ℕ) : ℕ := (m - 1) * (n - 1) / 2

/-- **The trefoil + cinquefoil channel** (the provable scaffold).

    The chiral channel is the trefoil `T_{2,3}` (Seifert genus 1) and the `ζ₅`
    carrier is the cinquefoil `T_{2,5}` (Seifert genus 2); both embed in Bring's
    `Σ₄` (genus ≤ 4) and they are **distinct** torus knots. This is the discrete
    content the audit doc records — two torus knots in one `Σ₄`, not one fibre
    with two symmetries. -/
-- Ref: [leitner2026] brings-surface/bring-trefoil-cinquefoil-channel
theorem bring_trefoil_cinquefoil_channel :
    torusKnotGenus 2 3 = 1 ∧ torusKnotGenus 2 5 = 2 ∧
      torusKnotGenus 2 3 ≤ bringsGenus ∧ torusKnotGenus 2 5 ≤ bringsGenus ∧
      torusKnotGenus 2 3 ≠ torusKnotGenus 2 5 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> decide

/-- Primitive fifth root of unity `ζ₅ = exp(2πi/5)` (local copy, matching
    `x5-z5-automorphism.lean`). -/
noncomputable def zeta5 : ℂ :=
  Complex.exp (2 * Real.pi * Complex.I / 5)

/-- `ζ₅⁵ = 1` — the 5-fold (cinquefoil / `ℤ₅ ⊂ S₅`) symmetry around which the
    chiral residue's monodromy is taken. -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
theorem zeta5_pow_five : zeta5 ^ 5 = 1 := by
  unfold zeta5
  rw [← Complex.exp_nat_mul]
  have h5 : (5 : ℕ) * (2 * (Real.pi : ℂ) * Complex.I / 5) =
      2 * (Real.pi : ℂ) * Complex.I := by
    push_cast
    ring
  rw [h5]
  exact Complex.exp_two_pi_mul_I

/-- **The quintic √5 — `g² = 5` (proved).** The quadratic Gauss sum over the
    cinquefoil's `ℤ₅`-orbit, `g = Σ_{k=0}^{4} ζ₅^{k²}` (written out as the five
    powers `0,1,4,9,16`), squares to `5`. This is the unique source of `ζ₅`'s
    irrationality over `ℚ` and the √5 the H₂S Bring constant `1/√5` is built
    from; the first Lagrange resolvent `w₁` of `ℤ₅ ⊂ S₅` carries it.

    Proof: `ζ₅` is a primitive 5th root (`Complex.isPrimitiveRoot_exp`), so
    `1 + ζ₅ + ζ₅² + ζ₅³ + ζ₅⁴ = 0` (`geom_sum_eq_zero`) and `ζ₅⁵ = 1`. Reducing
    `ζ₅⁹ = ζ₅⁴`, `ζ₅¹⁶ = ζ₅` gives `g = 1 + 2ζ₅ + 2ζ₅⁴`, and
    `g² − 5 = (4ζ₅³+8)(ζ₅⁵−1) + 4(1+ζ₅+ζ₅²+ζ₅³+ζ₅⁴)` — a polynomial identity
    closed by `linear_combination`. The archimedean root `g = +√5`
    (`p = 5 ≡ 1 mod 4`) is the sign refinement; `g² = 5` is the field-theoretic
    core that fixes the irrational scale. -/
-- Ref: [washington1997] Washington, *Introduction to Cyclotomic Fields* (GTM 83),
--   quadratic Gauss sum g_p² = (−1)^{(p−1)/2}·p; p = 5 ≡ 1 (mod 4) ⇒ g² = 5.
theorem quintic_gauss_sum_sq_eq_five :
    (1 + zeta5 ^ 1 + zeta5 ^ 4 + zeta5 ^ 9 + zeta5 ^ 16) ^ 2 = 5 := by
  have hprim : IsPrimitiveRoot zeta5 5 := by
    have key : zeta5 = Complex.exp (2 * (Real.pi : ℂ) * Complex.I / (↑(5 : ℕ))) := by
      unfold zeta5; norm_num
    rw [key]
    exact Complex.isPrimitiveRoot_exp 5 (by norm_num)
  have h5 : zeta5 ^ 5 = 1 := zeta5_pow_five
  have hsum : 1 + zeta5 + zeta5 ^ 2 + zeta5 ^ 3 + zeta5 ^ 4 = 0 := by
    have hg := hprim.geom_sum_eq_zero (by norm_num)
    rw [Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_succ,
        Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_zero] at hg
    linear_combination hg
  have e9 : zeta5 ^ 9 = zeta5 ^ 4 := by
    have h : zeta5 ^ 9 = zeta5 ^ 5 * zeta5 ^ 4 := by ring
    rw [h, h5, one_mul]
  have e16 : zeta5 ^ 16 = zeta5 := by
    have h : zeta5 ^ 16 = (zeta5 ^ 5) ^ 3 * zeta5 := by ring
    rw [h, h5, one_pow, one_mul]
  rw [e9, e16]
  linear_combination (4 * zeta5 ^ 3 + 8) * h5 + 4 * hsum

end QOU.BringChiralCinquefoil
