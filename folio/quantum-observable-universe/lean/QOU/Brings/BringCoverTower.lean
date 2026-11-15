/-
# A tower over Bring's surface: homology covers of the (2,4,5) orbifold

Owner, 2026-10-12: "explore two types of towers — Σ₄ for sure" (bean `qou-6082`).

Bring's surface `Σ₄` is the regular map of type (2,4,5): `Σ₄ / S₅` is the sphere with three
cone points of orders 2, 4, 5, i.e. `Σ₄ = ℍ / Π` for a genus-4 surface group `Π` normal in the
triangle group `Δ(2,4,5)` with `Δ/Π ≅ S₅`. Riemann–Hurwitz for any finite quotient
`G = Δ/Π'` acting on `Σ' = ℍ/Π'` reads

    2g' − 2 = |G| · (1 − 1/2 − 1/4 − 1/5) = |G|/20,   i.e.   40 (g' − 1) = |G|,

and at `G = S₅` (`|G| = 120`) this gives `g = 4` (`bring_rh`).

## The canonical tower

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

## What is chosen here, and so NOT derived

The modulus `m`. Nothing in the framework fixes it yet. The C₅ structure would suggest
`m = 5`; the 2-torsion of the (2,4,5) orbifold `m = 2`. Picking one by what it reproduces would
be selection against the target. The theorems hold for every `m ≥ 2`.

Not claimed: any identification of tower levels with confinement levels or with physical
scales. This file is the geometry only.

§7c: over `ℕ` (genera, group orders); no archimedean content.

-- Ref: [manuscript] lem:bring-cone-reeb-quaternionic-twist; Farkas–Kra, *Riemann Surfaces*,
   §I.2 (Riemann–Hurwitz) and §V.1 (regular maps / triangle groups); bean qou-6082.
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

end QOU.Brings.CoverTower
