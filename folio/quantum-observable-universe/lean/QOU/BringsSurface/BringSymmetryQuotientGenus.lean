import BraidKnotOctonion.S5CharactersOnBringDeformations
import Mathlib.Tactic

/-!
# Symmetry quotients of Bring's surface: which shapes carry its holomorphic harmonics

Thread "Audit the q-Bessel special-function dictionary" (2026-11-27). The owner asked whether
any shape besides the sphere and the torus is needed for the harmonics, and whether the
answer is exhaustive. This file answers it for the **holomorphic** harmonics (holomorphic
1-forms) of Bring's surface `B` (genus `4`, `Aut⁺(B) ≅ S₅`, signature `(2,4,5)`).

## Results

1. **Riemann–Hurwitz caps the genus of every quotient** (`rh_quotient_genus_le_two`,
   `rh_genus_two_order_le_three`, `rh_positive_genus_order_le_twelve`). For `H ≤ Aut⁺(B)`
   with `|H| = n ≥ 2`, `2·4 − 2 = n(2g' − 2) + R` with ramification `R ≥ 0` a sum of orbit
   terms each at least `n/2`. Hence `g' ≤ 2`; `g' = 2` forces `n ≤ 3`; `g' ≥ 1` forces
   `n ≤ 12`. So **no quotient has genus 3**, and `B/S₅`, `B/A₅` are spheres
   (`quotient_S5_sphere`, `quotient_A5_sphere`). This holds for every subgroup, with no
   enumeration.

2. **The representation on holomorphic 1-forms is forced to be `[2,1,1,1] = std ⊗ sgn`**
   (`h0K_character_forced`). Chevalley–Weil gives `dim H⁰(K)^H = g(B/H)`. A 4-dimensional
   character of `S₅` with no trivial summand (`g(B/S₅) = 0`) and no sign summand
   (`g(B/A₅) = 0`) is `[4,1]` or `[2,1,1,1]`. For a transposition `τ`, `g(B/⟨τ⟩) =
   (χ(1) + χ(τ))/2`, which is `3` for `[4,1]` and is excluded by item 1. So
   `χ_{H⁰(K)} = [2,1,1,1]`. (Direct check: `x₀ = x₁` meets Bring's curve in `2·3 = 6`
   points by Bézout, so `R = 6` and the quotient is a torus, not genus 3.)

3. **Genus of every quotient** (`quotient_genus_table`): for each of the 19 conjugacy classes
   of subgroups of `S₅`, given by how many elements it has in each `S₅` class,
   `|H| · g(B/H) = Σ_classes k_i χ(i)`. The genera are
   * `4` for the trivial group,
   * `2` for `C₂ = ⟨(01)(23)⟩` and `C₃`,
   * `1` (a torus) for `⟨(01)⟩`, `V₄ ◁ A₄`, `C₄`, `C₆`, `S₃ = ⟨(012), (01)(34)⟩` and `A₄`,
   * `0` (a sphere) for the other eleven, including `C₅, D₅, F₂₀, S₄, A₅, S₅`.
   Every value satisfies Riemann–Hurwitz with `R ≥ 0` (`quotient_genus_table_rh`). The list
   of 19 classes and their class distributions come from the probe
   `computations/probes/bring_symmetry_quotient_genus_probe.py` (exhaustive enumeration of the
   156 subgroups of `S₅`). Item 1 is the part that needs no enumeration.

4. **`[2,1,1,1]` is irreducible** (`h0K_irreducible`): no `S₅`-stable splitting of the
   holomorphic harmonics.

## Consequence for the harmonic dictionary

Every holomorphic harmonic of `B` lives in one irreducible `S₅`-module, and the symmetry
quotients that see it are spheres (see nothing), tori (see one dimension), or genus-2 curves
(see two). Nothing of genus `3` or higher occurs. Combined with the classical isogeny
`Jac(B) ~ E⁴` (quoted, not formalised: Riera–Rodríguez 1992, Braden–Disney-Hogg 2024), the
holomorphic harmonics need only the sphere and **one** torus `E`.

## Not established here

* `Jac(B) ~ E⁴` and which elliptic curve `E` is (candidate: the colour curve, Cremona 50a1).
* Chevalley–Weil itself and the Riemann–Hurwitz formula are cited, not formalised. The
  ramification lower bound `n/2` per orbit is taken as the hypothesis `hR`.
* The **Laplace (Maass) spectrum** of `B`. It is transcendental and belongs in
  `QOU/Transcendental/`.

## Caution for an existing file

`QOU/StandardModel/BringPrymRiemannRochGenerations.lean` models `H⁰(B, K) ≅ V_std = [4,1]`.
Item 2 says it is `[4,1] ⊗ sgn`. The two agree on `A₅`. They differ on `S₄`:
`Hom_{S₄}([2,1,1,1], 1) = 0`. Flagged to the χ = −6 thread.

Everything is integer arithmetic. No empirical value enters.

-- Ref: [braden-disney-hogg-2022] H. W. Braden and L. Disney-Hogg, *Bring's Curve: Old and New*.
-- Ref: [chevalley-weil1934] C. Chevalley and A. Weil (1934).
-/

namespace QOU.Brings.SymmetryQuotientGenus

open QOU.Brings.S5Char

/-! ## 1. Riemann–Hurwitz for a genus-4 curve -/

/-- No quotient of a genus-4 curve by a nontrivial group has genus `≥ 3`. -/
theorem rh_quotient_genus_le_two (n g R : ℕ) (hn : 2 ≤ n)
    (h : (6 : ℤ) = (n : ℤ) * (2 * (g : ℤ) - 2) + (R : ℤ)) : g ≤ 2 := by
  by_contra hg
  push_neg at hg
  have h1 : (8 : ℤ) ≤ n * (2 * g - 2) := by
    have : (4 : ℤ) ≤ 2 * g - 2 := by omega
    nlinarith
  omega

/-- A genus-2 quotient of a genus-4 curve comes from a group of order at most `3`. -/
theorem rh_genus_two_order_le_three (n R : ℕ) (h : (6 : ℤ) = (n : ℤ) * (2 * 2 - 2) + (R : ℤ)) :
    n ≤ 3 := by
  omega

/-- A quotient of positive genus comes from a group of order at most `12`, given that each
ramified orbit contributes at least `n/2` to `R`. -/
theorem rh_positive_genus_order_le_twelve (n g : ℕ) (cs : List ℕ) (hn : 2 ≤ n)
    (hR : ∀ c ∈ cs, n ≤ 2 * c)
    (h : (6 : ℤ) = (n : ℤ) * (2 * (g : ℤ) - 2) + (cs.sum : ℤ)) (hg : 1 ≤ g) :
    n ≤ 12 := by
  have hg2 := rh_quotient_genus_le_two n g cs.sum hn h
  interval_cases g
  · -- g = 1: R = 6, so some orbit term c ≤ 6 has n ≤ 2c.
    have hs' : (cs.sum : ℤ) = 6 := by
      try simp only [Nat.cast_one] at h
      linear_combination -h
    have hs : cs.sum = 6 := by exact_mod_cast hs'
    cases cs with
    | nil => simp at hs
    | cons c t =>
      have hc : c ≤ (c :: t).sum := List.le_sum_of_mem (List.mem_cons_self ..)
      have := hR c (List.mem_cons_self ..)
      omega
  · have := rh_genus_two_order_le_three n cs.sum (by
      try simp only [Nat.cast_ofNat] at h
      linear_combination h)
    omega

/-- `B / S₅` is a sphere. -/
theorem quotient_S5_sphere (g : ℕ) (cs : List ℕ) (hR : ∀ c ∈ cs, 120 ≤ 2 * c)
    (h : (6 : ℤ) = 120 * (2 * (g : ℤ) - 2) + (cs.sum : ℤ)) : g = 0 := by
  by_contra hg
  have := rh_positive_genus_order_le_twelve 120 g cs (by norm_num) hR (by exact_mod_cast h)
    (by omega)
  omega

/-- `B / A₅` is a sphere. -/
theorem quotient_A5_sphere (g : ℕ) (cs : List ℕ) (hR : ∀ c ∈ cs, 60 ≤ 2 * c)
    (h : (6 : ℤ) = 60 * (2 * (g : ℤ) - 2) + (cs.sum : ℤ)) : g = 0 := by
  by_contra hg
  have := rh_positive_genus_order_le_twelve 60 g cs (by norm_num) hR (by exact_mod_cast h)
    (by omega)
  omega

/-! ## 2. The character of `H⁰(B, K)` -/

/-- The character `a·[5] + b·[1⁵] + c·[4,1] + d·[2,1³] + e·[3,2] + f·[2²,1] + g·[3,1²]`. -/
def chiOf (a b c d e f g : ℕ) : Fin 7 → ℤ := fun i =>
  a * chiTriv i + b * chiSign i + c * chiStd i + d * chi2111 i + e * chi32 i +
    f * chi221 i + g * chi311 i

/-- **`H⁰(B, K) ≅ [2,1,1,1]`.** A 4-dimensional character with no trivial summand
(`g(B/S₅) = 0`), no sign summand (with the first, `g(B/A₅) = 0`), and transposition quotient
of genus at most 2 (`rh_quotient_genus_le_two`) is `[2,1,1,1]`. -/
theorem h0K_character_forced (a b c d e f g : ℕ)
    (hdim : chiOf a b c d e f g 0 = 4)
    (hS5 : S5Char.inner (chiOf a b c d e f g) chiTriv = 0)
    (hA5 : S5Char.inner (chiOf a b c d e f g) chiSign = 0)
    (htau : chiOf a b c d e f g 0 + chiOf a b c d e f g 1 ≤ 2 * 2) :
    chiOf a b c d e f g = chi2111 := by
  simp [chiOf, S5Char.inner, classSize, chiTriv, chiSign, chiStd, chi2111, chi32, chi221,
    chi311] at hdim hS5 hA5 htau
  have ha : a = 0 := by omega
  have hb : b = 0 := by omega
  have hc : c = 0 := by omega
  have hd : d = 1 := by omega
  have he : e = 0 := by omega
  have hf : f = 0 := by omega
  have hg : g = 0 := by omega
  subst ha hb hc hd he hf hg
  funext i
  fin_cases i <;> simp [chiOf, chiTriv, chiSign, chiStd, chi2111, chi32, chi221, chi311]

/-- With `[4,1]` in place of `[2,1,1,1]` the transposition quotient would have genus `3`. -/
theorem std_transposition_genus_three : (chiStd 0 + chiStd 1) = 2 * 3 := by decide

/-- `[2,1,1,1]` is irreducible: `⟨χ, χ⟩ = 1`. -/
theorem h0K_irreducible : S5Char.inner chi2111 chi2111 = 120 := by decide

/-! ## 3. The genus of every quotient -/

/-- A subgroup class of `S₅`: its order and how many elements it has in each `S₅` class
(order `1⁵, 2·1³, 2²·1, 3·1², 3·2, 4·1, 5`). From the enumeration probe. -/
def subgroupClasses : List (ℕ × (Fin 7 → ℤ)) :=
  [ (1,   ![1, 0, 0, 0, 0, 0, 0]),       -- trivial
    (2,   ![1, 0, 1, 0, 0, 0, 0]),       -- ⟨(01)(23)⟩
    (2,   ![1, 1, 0, 0, 0, 0, 0]),       -- ⟨(01)⟩
    (3,   ![1, 0, 0, 2, 0, 0, 0]),       -- C₃
    (4,   ![1, 2, 1, 0, 0, 0, 0]),       -- ⟨(01), (23)⟩
    (4,   ![1, 0, 3, 0, 0, 0, 0]),       -- V₄ ◁ A₄
    (4,   ![1, 0, 1, 0, 0, 2, 0]),       -- C₄
    (5,   ![1, 0, 0, 0, 0, 0, 4]),       -- C₅
    (6,   ![1, 1, 0, 2, 2, 0, 0]),       -- C₆
    (6,   ![1, 3, 0, 2, 0, 0, 0]),       -- S₃ on {0,1,2}
    (6,   ![1, 0, 3, 2, 0, 0, 0]),       -- S₃ twisted, ⟨(012), (01)(34)⟩
    (8,   ![1, 2, 3, 0, 0, 2, 0]),       -- D₄
    (10,  ![1, 0, 5, 0, 0, 0, 4]),       -- D₅
    (12,  ![1, 4, 3, 2, 2, 0, 0]),       -- S₃ × S₂
    (12,  ![1, 0, 3, 8, 0, 0, 0]),       -- A₄
    (20,  ![1, 0, 5, 0, 0, 10, 4]),      -- F₂₀
    (24,  ![1, 6, 3, 8, 0, 6, 0]),       -- S₄
    (60,  ![1, 0, 15, 20, 0, 0, 24]),    -- A₅
    (120, ![1, 10, 15, 20, 20, 30, 24]) ] -- S₅

/-- `Σ_classes k_i χ(i)`, which is `|H| · dim H⁰(K)^H`. -/
def fixedSum (k : Fin 7 → ℤ) : ℤ :=
  k 0 * chi2111 0 + k 1 * chi2111 1 + k 2 * chi2111 2 + k 3 * chi2111 3 +
    k 4 * chi2111 4 + k 5 * chi2111 5 + k 6 * chi2111 6

/-- **The genus table.** For the 19 subgroup classes in order, `|H| · g(B/H)` with the
genera `4, 2, 1, 2, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0`. -/
theorem quotient_genus_table :
    subgroupClasses.map (fun p => fixedSum p.2) =
      [1 * 4, 2 * 2, 2 * 1, 3 * 2, 0, 4 * 1, 4 * 1, 0, 6 * 1, 0, 6 * 1, 0, 0, 0, 12 * 1,
        0, 0, 0, 0] := by
  decide

/-- Each genus in the table satisfies Riemann–Hurwitz with nonnegative ramification:
`R = 6 − |H|(2g − 2) ≥ 0`, written `6 + 2|H| ≥ 2 · (|H| g)`. -/
theorem quotient_genus_table_rh :
    subgroupClasses.all (fun p => decide (2 * fixedSum p.2 ≤ 6 + 2 * (p.1 : ℤ))) = true := by
  decide

/-- Every group order in the table divides `120`. -/
theorem subgroup_orders_divide :
    subgroupClasses.all (fun p => decide (p.1 ∣ 120)) = true := by decide

/-- Each class distribution counts `|H|` elements. -/
theorem subgroup_class_counts :
    subgroupClasses.all (fun p => decide ((p.2 0 + p.2 1 + p.2 2 + p.2 3 + p.2 4 + p.2 5 +
      p.2 6) = (p.1 : ℤ))) = true := by decide

end QOU.Brings.SymmetryQuotientGenus
