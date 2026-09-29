/-
# The Hecke quadratic and the e₊/e₋ channels from a bare descent structure — every rank at once

Double brick on the two remaining walls (general-n tower + τ-functor
provenance). The Iwahori–Hecke length-rule action needs remarkably little:
an index type `W` (basis labels), an involutive step map `t : W → W`
(right multiplication by the generator), and a rank function `ℓ` that the
step NEVER fixes (`ℓ(t u) ≠ ℓ(u)`). This file proves, from that bare
**descent structure** alone:

* **`mulStep_quadratic`** — the Hecke quadratic `σ² = h·σ + 1` as an
  operator identity on the function module `W → R`;
* **`channel_plus` / `channel_minus`** — over a field with `q ≠ 0` and
  `h = q − q⁻¹`, the e₊/e₋ channel eigen-pair: `Mv + q⁻¹·v` is a
  `q`-eigendirection and `Mv − q·v` a `(−q⁻¹)`-eigendirection — exactly
  the symmetric/antisymmetric channel objects the archimedean τ-functor
  must send to `(H^{1,0}, H^{0,1})` (forced shadow #3960; B1 dictionary
  #3955), now available at EVERY rank rather than only the concrete rungs;
* **`instances at n = 3, 4`** — the merged concrete tables
  (`H3.mulσ₀/mulσ₁`, `H4.mulσ₀/σ₁/σ₂`) are literally `mulStep` of
  explicit descent structures (finite toggle data checked by `decide`),
  so the abstract theorem *re-derives* all five concrete quadratics.

Every Coxeter system yields a descent structure (`t := (· * sᵢ)`,
`ℓ := cs.length`; involutivity is `simple_mul_simple_self`, the no-fixed
law is `length_mul_simple_ne`) — the Mathlib-Coxeter instantiation lands
in a follow-up module once the `Mathlib.GroupTheory.Coxeter` olean cone is
built in this sandbox (in progress); nothing here depends on it.

HONESTY (STRICT): the braid relation and far commutation at general rank
are NOT provable from a descent structure alone (they involve two
generators — the exchange/Matsumoto layer); concretely proved at n = 3, 4
in the merged files, general rank stays OPEN, as do the
`HeckeBraidedPresentation` / `MarkovStabilization` instances (H_∞
binders). Nothing wired; `1/(8π)` stays phase-4.

Base ring (§7c): `[CommRing R]`; `[Field F]` only for the channels
(needs `q⁻¹`) — no `ℝ`, no ordering, no archimedean construct.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.HeckeH4StabilizationRung
import QOU.Machinery.HeckeH3AlgebraLaws

namespace QOU.Machinery.HeckeGeneral

/-- A **descent structure** on an index type `W`: an involutive step map
(right multiplication by a fixed generator) together with a rank function
the step never fixes. Every Coxeter system gives one on each simple
reflection (`t := (· * sᵢ)`, `ℓ := length`); the finite rungs n = 3, 4
give them by explicit tables (below). -/
structure DescentStructure (W : Type*) where
  /-- The step map `u ↦ u·s` (right multiplication by the generator). -/
  t : W → W
  /-- The rank (length) function. -/
  len : W → ℕ
  /-- The generator is an involution: `u·s·s = u`. -/
  t_invol : ∀ u, t (t u) = u
  /-- The step never fixes the rank: `ℓ(u·s) ≠ ℓ(u)`. -/
  len_ne : ∀ u, len (t u) ≠ len u

variable {W : Type*} {R : Type*} [CommRing R]

/-- The Iwahori–Hecke length-rule action of the generator on the function
module `W → R` (coefficient form): `(v·σ)(u) = v(u·s) + h·v(u)·[s is a
descent of u]`. -/
noncomputable def mulStep (D : DescentStructure W) (h : R) (v : W → R) : W → R :=
  fun u => v (D.t u) + if D.len (D.t u) < D.len u then h * v u else 0

/-- `mulStep` is additive. -/
theorem mulStep_add (D : DescentStructure W) (h : R) (v v' : W → R) :
    mulStep D h (v + v') = mulStep D h v + mulStep D h v' := by
  funext u
  simp only [mulStep, Pi.add_apply]
  split <;> ring

/-- `mulStep` is R-homogeneous. -/
theorem mulStep_smul (D : DescentStructure W) (h c : R) (v : W → R) :
    mulStep D h (c • v) = c • mulStep D h v := by
  funext u
  simp only [mulStep, Pi.smul_apply, smul_eq_mul]
  split <;> ring

/-- **The Hecke quadratic at every rank**: `σ² = h·σ + 1` on the function
module of ANY descent structure. The case split is exactly ascent/descent;
`t_invol` closes the double step and `len_ne` upgrades ¬descent to ascent.
Specializing to a Coxeter system's simple reflections discharges the
`hecke_quadratic` field content of `HeckeBraidedPresentation` at the action
level for all ranks simultaneously. -/
theorem mulStep_quadratic (D : DescentStructure W) (h : R) (v : W → R) :
    mulStep D h (mulStep D h v) = h • mulStep D h v + v := by
  funext u
  simp only [mulStep, Pi.add_apply, Pi.smul_apply, smul_eq_mul, D.t_invol]
  rcases lt_or_gt_of_ne (D.len_ne u) with hlt | hgt
  · -- descent: ℓ(u·s) < ℓ(u); the inner test ℓ(u) < ℓ(u·s) is false
    have h2 : ¬ D.len u < D.len (D.t u) := by omega
    simp only [if_pos hlt, if_neg h2]
    ring
  · -- ascent: ℓ(u·s) > ℓ(u); the outer test is false, the inner true
    have h1 : ¬ D.len (D.t u) < D.len u := by omega
    simp only [if_neg h1, if_pos hgt]
    ring

section Channels

variable {F : Type*} [Field F]

/-- **The e₊ channel at every rank**: for `h = q − q⁻¹`, the vector
`Mv + q⁻¹·v` is a `q`-eigendirection of the generator action — the
symmetric channel. Pure algebra from the quadratic. -/
theorem channel_plus (D : DescentStructure W) (q : F) (hq : q ≠ 0) (v : W → F) :
    mulStep D (q - q⁻¹) (mulStep D (q - q⁻¹) v + q⁻¹ • v)
      = q • (mulStep D (q - q⁻¹) v + q⁻¹ • v) := by
  rw [mulStep_add, mulStep_smul, mulStep_quadratic]
  funext u
  have hinv : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  have hexp : q * (mulStep D (q - q⁻¹) v u + q⁻¹ * v u)
      = q * mulStep D (q - q⁻¹) v u + q * q⁻¹ * v u := by ring
  rw [hexp, hinv, one_mul]
  ring

/-- **The e₋ channel at every rank**: for `h = q − q⁻¹`, the vector
`Mv − q·v` is a `(−q⁻¹)`-eigendirection — the antisymmetric channel.
Together with `channel_plus`, the channel pair the archimedean τ-functor
must send to `(H^{1,0}, H^{0,1})` now exists at every rank. -/
theorem channel_minus (D : DescentStructure W) (q : F) (hq : q ≠ 0) (v : W → F) :
    mulStep D (q - q⁻¹) (mulStep D (q - q⁻¹) v - q • v)
      = (-q⁻¹) • (mulStep D (q - q⁻¹) v - q • v) := by
  have hsub : mulStep D (q - q⁻¹) v - q • v
      = mulStep D (q - q⁻¹) v + (-q) • v := by
    funext u
    simp only [Pi.sub_apply, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
    ring
  rw [hsub, mulStep_add, mulStep_smul, mulStep_quadratic]
  funext u
  have hinv : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  simp only [Pi.add_apply, Pi.smul_apply, Pi.sub_apply, smul_eq_mul]
  have hexp : -q⁻¹ * (mulStep D (q - q⁻¹) v u + -q * v u)
      = -q⁻¹ * mulStep D (q - q⁻¹) v u + q * q⁻¹ * v u := by ring
  rw [hexp, hinv, one_mul]
  ring

end Channels

/-! ## The concrete rungs are instances

The merged n = 3 and n = 4 generator tables are literally `mulStep` of
explicit finite descent structures — the abstract theorem re-derives all
five concrete quadratics. The descent data (step permutation + lengths)
are the preflight-pinned basis words; involutivity and the no-fixed law
are finite checks (`decide`). -/

/-- The n = 3 descent structure for σ₀ on the NF basis
`[γ, σ₀, σ₁, L₊, L₋, e⁻]` (lengths `[0,1,1,2,2,3]`; step = the σ₀ pairing
`0↔1, 2↔3, 4↔5`). -/
def descentH3σ₀ : DescentStructure (Fin 6) where
  t := ![1, 0, 3, 2, 5, 4]
  len := ![0, 1, 1, 2, 2, 3]
  t_invol := by decide
  len_ne := by decide

/-- The merged concrete `H3.mulσ₀` table IS `mulStep` of `descentH3σ₀`. -/
theorem h3_mulσ₀_eq_mulStep (h : R) (v : Fin 6 → R) :
    H3.mulσ₀ h v = mulStep descentH3σ₀ h v := by
  funext i
  fin_cases i <;>
    simp [H3.mulσ₀, mulStep, descentH3σ₀] <;> ring

/-- The n = 3 descent structure for σ₁ (step = the σ₁ pairing
`0↔2, 1↔4, 3↔5`). -/
def descentH3σ₁ : DescentStructure (Fin 6) where
  t := ![2, 4, 0, 5, 1, 3]
  len := ![0, 1, 1, 2, 2, 3]
  t_invol := by decide
  len_ne := by decide

/-- The merged concrete `H3.mulσ₁` table IS `mulStep` of `descentH3σ₁`. -/
theorem h3_mulσ₁_eq_mulStep (h : R) (v : Fin 6 → R) :
    H3.mulσ₁ h v = mulStep descentH3σ₁ h v := by
  funext i
  fin_cases i <;>
    simp [H3.mulσ₁, mulStep, descentH3σ₁] <;> ring

/-- The n = 4 descent structure for σ₂ on the 24-element S₄ NF basis
(lengths by word length; step = the σ₂ pairing from the preflight table). -/
def descentH4σ₂ : DescentStructure (Fin 24) where
  t := ![6, 8, 7, 11, 10, 15, 0, 2, 1, 12, 4, 3, 9, 16, 18, 5, 13, 20, 14, 21, 17, 19, 23, 22]
  len := ![0, 1, 1, 2, 2, 3, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6]
  t_invol := by decide
  len_ne := by decide

/-- The merged concrete `H4.mulσ₂` table IS `mulStep` of `descentH4σ₂` —
the abstract quadratic re-derives `H4.mulσ₂_hecke`. -/
theorem h4_mulσ₂_eq_mulStep (h : R) (v : Fin 24 → R) :
    H4.mulσ₂ h v = mulStep descentH4σ₂ h v := by
  funext i
  fin_cases i <;>
    simp [H4.mulσ₂, mulStep, descentH4σ₂] <;> ring

end QOU.Machinery.HeckeGeneral
