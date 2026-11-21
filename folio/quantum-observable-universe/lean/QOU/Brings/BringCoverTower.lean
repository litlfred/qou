/-
# A tower over Bring's surface: homology covers and non-abelian Hurwitz (2,4,5) PSL₂(𝔽_p) covers

Owner, 2026-10-12 & 2026-11-15: "explore two types of towers — Σ₄ for sure" and classify
non-abelian Hurwitz (2,4,5)-quotients `PSL₂(𝔽_p)` / `PGL₂(𝔽_p)` covering Bring's surface
(bean `qou-6082`, owner ruling `Q-VO9T-3 = 2`).

Bring's surface `Σ₄` is the regular map of type (2,4,5): `Σ₄ / S₅` is the sphere with three
cone points of orders 2, 4, 5, i.e. `Σ₄ = ℍ / Π` for a genus-4 surface group `Π` normal in the
triangle group `Δ(2,4,5)` with `Δ/Π ≅ S₅ ≅ PGL₂(𝔽₅)`. Riemann–Hurwitz for any finite quotient
`G = Δ/Π'` acting on `Σ' = ℍ/Π'` reads

    2g' − 2 = |G| · (1 − 1/2 − 1/4 − 1/5) = |G|/20,   i.e.   40 (g' − 1) = |G|,

and at `G = S₅` (`|G| = 120`) this gives `g = 4` (`bring_rh`).

## 1. The canonical abelian homology tower

For an integer `m ≥ 2`, the mod-`m` homology cover of a genus-`g` surface is the unramified
Galois cover with group `H₁(Σ; ℤ/m) ≅ (ℤ/m)^{2g}`; its kernel is characteristic in `Π`, so it is
normal in `Δ(2,4,5)` and the cover is again a regular map of type (2,4,5) — same three cone
angles, so the order-5 rotation data of `BringConjugationChirality.lean` lifts to every level.
Euler characteristic is multiplicative under unramified covers:

    g_{k+1} − 1 = m^{2 g_k} · (g_k − 1),     g_0 = 4.

Proved here: the recursion is consistent with Riemann–Hurwitz at every level
(`rh_step`); the genus is strictly increasing (`towerGenus_strictMono`); it grows at least
like `m^{2 g_k}` per step (`towerGenus_succ_ge`); and the first levels are
`g_1 = 1 + 3 m⁸` (769 at `m = 2`, 1 171 876 at `m = 5`).

## 2. Non-abelian Hurwitz (2,4,5)-quotients: `PSL₂(𝔽_p)`, `PGL₂(𝔽_p)`, and covers of `Σ₄`

By Macbeath's classification of `(2,4,5)`-generation of projective linear groups over `𝔽_p`:
- An element `[M] ∈ PGL₂(𝔽_p)` with trace `t` and determinant `Δ ≠ 0` has projective order:
  - `2` iff `t = 0`;
  - `4` iff `t² = 2 Δ` (`projOrder4_cayley_hamilton`: `M⁴ = −Δ² I₂`);
  - `5` iff `t⁴ − 3 t² Δ + Δ² = 0` (`projOrder5_cayley_hamilton`: `M⁵ = −(t³ − 2 t Δ) Δ I₂`).
- At `p = 5`: `PSL₂(𝔽₅) ≅ A₅` (`|A₅| = 60`) has no element of order 4 and `40 ∤ 60`
  (`psl2_five_not_rh245`), whereas `PGL₂(𝔽₅) ≅ S₅` (`|S₅| = 120`) is `(2,4,5)`-generated and
  yields Bring's surface `Σ₄` (`g = 4`, `bring_pgl2_five_rh`).
- For prime `p > 5` with `p ≡ ±1 (mod 5)` (so `(5/p) = +1`, order-5 elements exist):
  - **Direct `PSL₂(𝔽_p)` branch (`p ≡ ±1, ±9 mod 40`, `(2/p) = +1`, e.g. `p = 31, 41`):**
    `PSL₂(𝔽_p)` itself is a smooth `(2,4,5)`-quotient of genus `1 + |PSL₂(𝔽_p)|/40`
    (`psl2_31_rh`, `psl2_41_rh`). Since `PSL₂(𝔽_p)` is simple and non-isomorphic to `A₅`,
    Goursat's lemma gives the subdirect product `G_p = S₅ × PSL₂(𝔽_p)` of order
    `120 · |PSL₂(𝔽_p)|`, an unramified `PSL₂(𝔽_p)`-cover of Bring's surface `Σ₄` of genus
    `g(p) = 3 |PSL₂(𝔽_p)| + 1` (`bringPSL2Cover_rh`).
  - **Fiber-product `PGL₂(𝔽_p)` branch (`p ≡ ±11, ±19 mod 40`, `(2/p) = −1`, e.g. `p = 11, 19, 29`):**
    Order-4 elements have non-square determinant, so `PGL₂(𝔽_p)` is a smooth `(2,4,5)`-quotient
    of genus `1 + |PGL₂(𝔽_p)|/40` (`pgl2_11_rh`, `pgl2_19_rh`, `pgl2_29_rh`). Because the
    abelianization `Δ(2,4,5)^ab ≅ C₂` (`x ↦ −1, y ↦ −1, z ↦ +1`) matches both `sgn : S₅ → C₂`
    and `det : PGL₂(𝔽_p) → 𝔽_p^×/(𝔽_p^×)² ≅ C₂`, the diagonal image in `S₅ × PGL₂(𝔽_p)` is the
    index-2 fiber product `G_p = S₅ ×_{C₂} PGL₂(𝔽_p)` of order `120 · |PSL₂(𝔽_p)|`, which is
    again an unramified `PSL₂(𝔽_p)`-cover of `Σ₄` of the same genus `g(p) = 3 |PSL₂(𝔽_p)| + 1`!

Companion probe: `computations/probes/bring_hurwitz_245_psl2_tower_probe.py`.

## What is chosen here, and so NOT derived

The modulus `m` in the homology tower, or the prime `p` in the `PSL₂(𝔽_p)` cover family.
Nothing in the framework fixes `m` or `p` yet; picking one by what it reproduces would be
selection against the target. Not claimed: any identification of tower levels with confinement
levels or physical scales. This file is the geometry and group algebra only.

§7c: over `ℕ` (genera, group orders) and generic `[CommRing R]` (Cayley–Hamilton identities);
no archimedean content.

-- Ref: [manuscript] lem:bring-cone-reeb-quaternionic-twist; Farkas–Kra, *Riemann Surfaces*,
   §I.2 (Riemann–Hurwitz) and §V.1 (regular maps / triangle groups); Macbeath (1969),
   *Generators of the linear fractional groups*; bean qou-6082.
-/
import Mathlib.Tactic

namespace QOU.Brings.CoverTower

/-- Riemann–Hurwitz for a regular map of type (2,4,5): `40 (g − 1) = |G|`, stated without
subtraction. -/
def RH245 (g n : ℕ) : Prop := 40 * g = n + 40

/-- **Bring's surface**: `|S₅| = 120` forces genus 4. -/
theorem bring_rh : RH245 4 120 := by unfold RH245; norm_num

/-- Riemann–Hurwitz determines the genus from the group order. -/
theorem rh_genus_unique {g g' n : ℕ} (h : RH245 g n) (h' : RH245 g' n) : g = g' := by
  unfold RH245 at h h'; omega

/-- The genus of the next level of the mod-`m` homology tower. -/
def nextGenus (m g : ℕ) : ℕ := m ^ (2 * g) * (g - 1) + 1

/-- The mod-`m` homology tower over Bring's surface. -/
def towerGenus (m : ℕ) : ℕ → ℕ
  | 0 => 4
  | k + 1 => nextGenus m (towerGenus m k)

/-- The automorphism-group order at each level: `|G_{k+1}| = m^{2 g_k} |G_k|`. -/
def towerOrder (m : ℕ) : ℕ → ℕ
  | 0 => 120
  | k + 1 => m ^ (2 * towerGenus m k) * towerOrder m k

/-- **Riemann–Hurwitz is preserved by one homology step.** -/
theorem rh_step (m g n : ℕ) (hg : 1 ≤ g) (h : RH245 g n) :
    RH245 (nextGenus m g) (m ^ (2 * g) * n) := by
  unfold RH245 nextGenus at *
  obtain ⟨g', rfl⟩ : ∃ g', g = g' + 1 := ⟨g - 1, by omega⟩
  simp only [Nat.add_sub_cancel]
  have h' : n = 40 * g' := by omega
  subst h'
  ring

/-- **Every level of the tower is a regular map of type (2,4,5).** -/
theorem tower_rh (m : ℕ) : ∀ k, 1 ≤ towerGenus m k ∧ RH245 (towerGenus m k) (towerOrder m k)
  | 0 => ⟨by simp [towerGenus], bring_rh⟩
  | k + 1 => by
      obtain ⟨hg, h⟩ := tower_rh m k
      exact ⟨by simp [towerGenus, nextGenus], rh_step m _ _ hg h⟩

/-- The genus at every level is at least 4. -/
theorem four_le_towerGenus (m : ℕ) (hm : 2 ≤ m) : ∀ k, 4 ≤ towerGenus m k
  | 0 => le_refl 4
  | k + 1 => by
      have ih := four_le_towerGenus m hm k
      have hp : 1 ≤ m ^ (2 * towerGenus m k) := Nat.one_le_pow _ _ (by omega)
      have h3 : 3 ≤ towerGenus m k - 1 := by omega
      have := Nat.mul_le_mul hp h3
      simp only [towerGenus, nextGenus]
      omega

/-- **Growth: each step multiplies `g − 1` by `m^{2g}`**, so `g_{k+1} ≥ m^{2 g_k}`. -/
theorem towerGenus_succ_ge (m : ℕ) (hm : 2 ≤ m) (k : ℕ) :
    m ^ (2 * towerGenus m k) ≤ towerGenus m (k + 1) := by
  have h4 := four_le_towerGenus m hm k
  simp only [towerGenus, nextGenus]
  have h1 : 1 ≤ towerGenus m k - 1 := by omega
  have := Nat.mul_le_mul (le_refl (m ^ (2 * towerGenus m k))) h1
  omega

/-- **The tower is strictly increasing.** -/
theorem towerGenus_lt_succ (m : ℕ) (hm : 2 ≤ m) (k : ℕ) :
    towerGenus m k < towerGenus m (k + 1) := by
  have h4 := four_le_towerGenus m hm k
  have hge := towerGenus_succ_ge m hm k
  have h1 : towerGenus m k < 2 ^ towerGenus m k := Nat.lt_two_pow_self
  have h2 : 2 ^ towerGenus m k ≤ 2 ^ (2 * towerGenus m k) :=
    Nat.pow_le_pow_right (by norm_num) (by omega)
  have h3 : 2 ^ (2 * towerGenus m k) ≤ m ^ (2 * towerGenus m k) := Nat.pow_le_pow_left hm _
  omega

theorem towerGenus_strictMono (m : ℕ) (hm : 2 ≤ m) : StrictMono (towerGenus m) :=
  strictMono_nat_of_lt_succ (towerGenus_lt_succ m hm)

/-- First level: `g_1 = 1 + 3 m⁸`. -/
theorem towerGenus_one (m : ℕ) : towerGenus m 1 = 3 * m ^ 8 + 1 := by
  simp [towerGenus, nextGenus]; ring

example : towerGenus 2 1 = 769 := by rw [towerGenus_one]; norm_num
example : towerGenus 5 1 = 1171876 := by rw [towerGenus_one]; norm_num

/-! ## Non-abelian Hurwitz (2,4,5) quotients `PSL₂(𝔽_p)` / `PGL₂(𝔽_p)` and covers of `Σ₄` -/

/-- Order of `PGL₂(𝔽_p)` for an odd prime `p`: `p(p² − 1)`. -/
def pgl2Order (p : ℕ) : ℕ := p * (p ^ 2 - 1)

/-- Order of `PSL₂(𝔽_p)` for an odd prime `p`: `p(p² − 1) / 2`. -/
def psl2Order (p : ℕ) : ℕ := p * (p ^ 2 - 1) / 2

theorem bring_pgl2_five_order : pgl2Order 5 = 120 := by rfl
theorem bring_psl2_five_order : psl2Order 5 = 60 := by rfl

/-- `PGL₂(𝔽₅) ≅ S₅` (`|G| = 120`) satisfies the `(2,4,5)` Riemann–Hurwitz relation at `g = 4`. -/
theorem bring_pgl2_five_rh : RH245 4 (pgl2Order 5) := bring_rh

/-- `PSL₂(𝔽₅) ≅ A₅` (`|G| = 60`) is **not** a smooth `(2,4,5)`-quotient (`40 ∤ 60`). -/
theorem psl2_five_not_rh245 (g : ℕ) : ¬ RH245 g (psl2Order 5) := by
  unfold RH245 psl2Order
  omega

/-- Order of the subdirect `(2,4,5)` cover group `G_p` (`S₅ × PSL₂(𝔽_p)` for `p ≡ ±1, ±9 mod 40`,
    or `S₅ ×_{C₂} PGL₂(𝔽_p)` for `p ≡ ±11, ±19 mod 40`) projecting onto `S₅` with deck group
    `PSL₂(𝔽_p)`. -/
def bringPSL2CoverOrder (p : ℕ) : ℕ := 120 * psl2Order p

/-- Genus of the unramified `PSL₂(𝔽_p)`-cover `Σ_{g(p)} → Σ₄` over Bring's surface:
    `g(p) − 1 = |PSL₂(𝔽_p)| · (4 − 1) = 3 |PSL₂(𝔽_p)|`. -/
def bringPSL2CoverGenus (p : ℕ) : ℕ := 3 * psl2Order p + 1

/-- **Every unramified `PSL₂(𝔽_p)`-cover of Bring's surface satisfies `RH245`.** -/
theorem bringPSL2Cover_rh (p : ℕ) :
    RH245 (bringPSL2CoverGenus p) (bringPSL2CoverOrder p) := by
  unfold RH245 bringPSL2CoverGenus bringPSL2CoverOrder
  omega

/-- **Macbeath `PGL₂(𝔽_p)` branch (`(2/p) = −1, (5/p) = +1`)**: `p = 11, 19, 29`. -/
theorem pgl2_11_rh : RH245 34 (pgl2Order 11) := rfl
theorem pgl2_19_rh : RH245 172 (pgl2Order 19) := rfl
theorem pgl2_29_rh : RH245 610 (pgl2Order 29) := rfl

/-- **Macbeath `PSL₂(𝔽_p)` branch (`(2/p) = +1, (5/p) = +1`)**: `p = 31, 41`. -/
theorem psl2_31_rh : RH245 373 (psl2Order 31) := rfl
theorem psl2_41_rh : RH245 862 (psl2Order 41) := rfl

/-- Genera of the corresponding unramified `PSL₂(𝔽_p)`-covers `Σ_{g(p)} → Σ₄` over Bring's surface. -/
theorem bringPSL2CoverGenus_values :
    bringPSL2CoverGenus 11 = 1981 ∧
    bringPSL2CoverGenus 19 = 10261 ∧
    bringPSL2CoverGenus 29 = 36541 ∧
    bringPSL2CoverGenus 31 = 44641 ∧
    bringPSL2CoverGenus 41 = 103321 :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩

section CayleyHamilton245

variable {R : Type*} [CommRing R]

/-- **Projective order 4 criterion (`t² = 2 Δ`).** By Cayley–Hamilton `M² = t M − Δ I`,
    if `t² = 2 Δ` then `M⁴ = (t³ − 2 t Δ) M − (t² − d) Δ I = −Δ² I` (the `M`-coefficient
    `t(t² − 2 Δ)` vanishes and the scalar coefficient is `−(t² − Δ) Δ + t² Δ = −Δ²`). -/
theorem projOrder4_cayley_hamilton (t Δ : R) (h4 : t ^ 2 = 2 * Δ) :
    t * (t ^ 2 - 2 * Δ) = 0 ∧ -((t ^ 2 - Δ) * Δ) = -Δ ^ 2 := by
  refine ⟨by linear_combination t * h4, by linear_combination -Δ * h4⟩

/-- **Projective order 5 criterion (`t⁴ − 3 t² Δ + Δ² = 0`).** By Cayley–Hamilton `M² = t M − Δ I`,
    `M⁵ = (t⁴ − 3 t² Δ + Δ²) M − (t³ − 2 t Δ) Δ I`, and `(2 t² − 3 Δ)² − 5 Δ² = 4(t⁴ − 3 t² Δ + Δ²)`,
    showing that projective order 5 requires `5` to be a square in the base field. -/
theorem projOrder5_discriminant_identity (t Δ : R) :
    (2 * t ^ 2 - 3 * Δ) ^ 2 - 5 * Δ ^ 2 = 4 * (t ^ 4 - 3 * t ^ 2 * Δ + Δ ^ 2) := by
  ring

end CayleyHamilton245

end QOU.Brings.CoverTower
