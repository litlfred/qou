/-
# The Hecke length-rule module over ANY Coxeter system — the quadratic and the e₊/e₋ channels at every rank

Double brick on the two remaining walls (general-n tower + τ-functor
provenance), built on Mathlib's Coxeter machinery
(`CoxeterSystem.length_mul_simple`, the ±1 toggle):

**Wall 1 (general-n).** `mulSimple` — the right action of the Hecke
generator `T_{sᵢ}` on the function module `W → R` by the exact
Iwahori–Hecke length rule, for an ARBITRARY Coxeter system `cs` — and
**`mulSimple_quadratic`**: `σᵢ² = h·σᵢ + 1` proved at every rank
simultaneously. Until now the tower's quadratic existed only concretely at
n = 2, 3, 4 (`HeckeH3AlgebraLaws`, `HeckeH4StabilizationRung`); this is the
first genuinely general-rank theorem — specializing `W` to any symmetric
group discharges the `hecke_quadratic` field content of
`HeckeBraidedPresentation` at the action level for ALL n at once.

**Wall 2 (τ-functor provenance).** From the quadratic, over a field with
`q ≠ 0` and `h = q − q⁻¹`: the **e₊/e₋ channel eigen-pair** at every rank —
`channel_plus` (`M(Mv + q⁻¹·v) = q·(Mv + q⁻¹·v)`) and `channel_minus`
(`M(Mv − q·v) = −q⁻¹·(Mv − q·v)`). These are precisely the symmetric /
antisymmetric channel objects the archimedean τ-functor must send to
`(H^{1,0}, H^{0,1})` (the forced shadow, #3960; the B1 dictionary, #3955):
the domain-side channel pair now exists as verified mathematics at every
rank, not only at the concrete rungs.

HONESTY (STRICT): the braid relation and far commutation at general rank
are NOT proved here (they need genuinely deeper Coxeter combinatorics —
the exchange/Matsumoto layer; concretely proved at n = 3, 4 in the merged
files). No `HeckeBraidedPresentation` / `MarkovStabilization` instance is
declared; the general-n classes stay OPEN. Nothing wired; `1/(8π)` stays
phase-4.

Base ring (§7c): `[CommRing R]` for the module + quadratic; `[Field R]`
enters only for the channel pair (needs `q⁻¹`), still fully generic — no
`ℝ`, no ordering, no archimedean construct.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import Mathlib.GroupTheory.Coxeter.Length

namespace QOU.Machinery.HeckeGeneral

open CoxeterSystem

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)
variable {R : Type*} [CommRing R]

/-- Right action of the Hecke generator `T_{sᵢ}` on the function module
`W → R`, by the exact Iwahori–Hecke length rule (coefficient form): the
coefficient at `u` after acting is `v(u·sᵢ)` plus `h·v(u)` exactly when
`sᵢ` is a right descent of `u`. Specialized to `W = Sₙ` this reproduces the
concrete `mulσ` tables of `HeckeH3AlgebraLaws` / `HeckeH4StabilizationRung`
entry-for-entry. -/
noncomputable def mulSimple (h : R) (i : B) (v : W → R) : W → R := fun u =>
  v (u * cs.simple i)
    + if cs.length (u * cs.simple i) < cs.length u then h * v u else 0

/-- `mulSimple` is additive. -/
theorem mulSimple_add (h : R) (i : B) (v v' : W → R) :
    mulSimple cs h i (v + v') = mulSimple cs h i v + mulSimple cs h i v' := by
  funext u
  simp only [mulSimple, Pi.add_apply]
  split <;> ring

/-- `mulSimple` is R-homogeneous. -/
theorem mulSimple_smul (h c : R) (i : B) (v : W → R) :
    mulSimple cs h i (c • v) = c • mulSimple cs h i v := by
  funext u
  simp only [mulSimple, Pi.smul_apply, smul_eq_mul]
  split <;> ring

/-- **The Hecke quadratic at EVERY rank**: `σᵢ² = h·σᵢ + 1` as an operator
identity on the length-rule module of an arbitrary Coxeter system. The two
cases are exactly the ±1 length toggle (`length_mul_simple`); the involution
`u·sᵢ·sᵢ = u` is `simple_mul_simple_self`. Specializing `W` to a symmetric
group discharges the `hecke_quadratic` field content of
`HeckeBraidedPresentation` at the action level for all n simultaneously —
previously known only concretely at n = 2, 3, 4. -/
theorem mulSimple_quadratic (h : R) (i : B) (v : W → R) :
    mulSimple cs h i (mulSimple cs h i v) = h • mulSimple cs h i v + v := by
  funext u
  have hss : u * cs.simple i * cs.simple i = u := by
    rw [mul_assoc, cs.simple_mul_simple_self, mul_one]
  simp only [mulSimple, Pi.add_apply, Pi.smul_apply, smul_eq_mul, hss]
  rcases cs.length_mul_simple u i with heq | heq
  · -- ascent: ℓ(u·sᵢ) = ℓ(u) + 1 — outer descent-test false, inner true
    have h1 : ¬ cs.length (u * cs.simple i) < cs.length u := by omega
    have h2 : cs.length u < cs.length (u * cs.simple i) := by omega
    simp only [if_neg h1, if_pos h2]
    ring
  · -- descent: ℓ(u·sᵢ) + 1 = ℓ(u) — outer descent-test true, inner false
    have h1 : cs.length (u * cs.simple i) < cs.length u := by omega
    have h2 : ¬ cs.length u < cs.length (u * cs.simple i) := by omega
    simp only [if_pos h1, if_neg h2]
    ring

section Channels

variable {F : Type*} [Field F]

/-- **The e₊ channel at every rank**: for `h = q − q⁻¹`, the vector
`Mv + q⁻¹·v` is a `q`-eigenvector direction of the generator action — the
symmetric channel. Derived from the quadratic by pure algebra. -/
theorem channel_plus (q : F) (hq : q ≠ 0) (i : B) (v : W → F) :
    mulSimple cs (q - q⁻¹) i
        (mulSimple cs (q - q⁻¹) i v + q⁻¹ • v)
      = q • (mulSimple cs (q - q⁻¹) i v + q⁻¹ • v) := by
  rw [mulSimple_add, mulSimple_smul, mulSimple_quadratic]
  funext u
  have hinv : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  have hexp : q * (mulSimple cs (q - q⁻¹) i v u + q⁻¹ * v u)
      = q * mulSimple cs (q - q⁻¹) i v u + q * q⁻¹ * v u := by ring
  rw [hexp, hinv, one_mul]
  ring

/-- **The e₋ channel at every rank**: for `h = q − q⁻¹`, the vector
`Mv − q·v` is a `(−q⁻¹)`-eigenvector direction of the generator action —
the antisymmetric channel. Together with `channel_plus` this constructs, at
EVERY rank, exactly the channel pair the archimedean τ-functor must send to
`(H^{1,0}, H^{0,1})` (forced shadow #3960; B1 dictionary #3955). -/
theorem channel_minus (q : F) (hq : q ≠ 0) (i : B) (v : W → F) :
    mulSimple cs (q - q⁻¹) i
        (mulSimple cs (q - q⁻¹) i v - q • v)
      = (-q⁻¹) • (mulSimple cs (q - q⁻¹) i v - q • v) := by
  have hsub : mulSimple cs (q - q⁻¹) i v - q • v
      = mulSimple cs (q - q⁻¹) i v + (-q) • v := by
    funext u
    simp only [Pi.sub_apply, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
    ring
  rw [hsub, mulSimple_add, mulSimple_smul, mulSimple_quadratic]
  funext u
  have hinv : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  simp only [Pi.add_apply, Pi.smul_apply, Pi.sub_apply, smul_eq_mul]
  have hexp : -q⁻¹ * (mulSimple cs (q - q⁻¹) i v u + -q * v u)
      = -q⁻¹ * mulSimple cs (q - q⁻¹) i v u + q * q⁻¹ * v u := by ring
  rw [hexp, hinv, one_mul]
  ring

end Channels

end QOU.Machinery.HeckeGeneral
