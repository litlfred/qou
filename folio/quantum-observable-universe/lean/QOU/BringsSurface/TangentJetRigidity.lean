import Mathlib.Algebra.Polynomial.Eval.Degree
import Mathlib.Algebra.Polynomial.Coeff
import Mathlib.Algebra.Ring.GeomSum
import Mathlib.RingTheory.IntegralDomain
import Mathlib.Tactic.LinearCombination

/-!
# `QOU.RiemannSurface.TangentJetRigidity` — finite order and tangent to the identity

Bean `qou-qhcr`, Riemann-surface layer, milestone M1.

The genus-4 capstone `QOU.BringsSurface.RiemannHurwitzCellular.genus_eq_four_of_cellular`
assumes that point stabilisers of a holomorphic group action are **cyclic**. The classical
proof has two steps:

1. **Rigidity.** A holomorphic germ `h` with `h(0) = 0`, `h'(0) = 1` and `h^{∘n} = id` is the
   identity. If `h(z) = z + a z^k + O(z^{k+1})` with `a ≠ 0`, then
   `h^{∘n}(z) = z + n a z^k + O(z^{k+1})`, and `n a ≠ 0` in characteristic zero.
2. **Cyclicity.** Step 1 makes `g ↦ g'(0)` an injective homomorphism from the stabiliser into
   `ℂˣ`, and a finite subgroup of the units of a domain is cyclic.

This file proves the **algebraic core of both**, sorry-free:

* `jet_comp`: jets `X + aXᵏ` and `X + bXᵏ` (mod `X^{k+1}`) compose to `X + (a+b)Xᵏ`.
* `jet_iterate`: the `n`-fold self-composition of `X + aXᵏ` is `X + n·a·Xᵏ`.
* `jet_step`: if `f ≡ X (mod Xᵏ)` and `f^{∘n} = X` with `n ≥ 1`, then `f ≡ X (mod X^{k+1})`,
  over any domain of characteristic zero.
* `eq_X_of_finite_order`: a polynomial map with `f(0) = 0`, `f'(0) = 1` and finite
  compositional order is `X`.
* `isCyclic_of_injective_derivative`: Step 2, from Mathlib's `isCyclic_of_subgroup_isDomain`.

## What is NOT yet proved (roadmap, milestones M1b–M4)

* **M1b.** Transfer to analytic germs: the Taylor jet of `h ∘ g` truncated at order `k` is the
  polynomial composition of the truncated jets, and an analytic germ all of whose jets equal
  those of `id` is `id` near `0` (identity theorem; Mathlib has
  `AnalyticOnNhd.eqOn_of_preconnected_of_eventuallyEq`). This turns `jet_step` into Step 1
  for germs.
* **M2.** Globalise on a connected Riemann surface (Mathlib `ChartedSpace ℂ` plus holomorphic
  atlas): a biholomorphism equal to `id` near a point is `id`.
* **M3.** An equivariant cell structure with `χ = 2 − 2g` (triangulation of a compact surface
  and its quotient). This is the largest gap; Mathlib has no surface topology of this kind.
* **M4.** Irreducible dimensions of `A₅` (`1, 3, 3, 4, 5`).
-/

namespace QOU.RiemannSurface.TangentJetRigidity

open Polynomial

section Jets

variable {K : Type*} [CommRing K]

/-- `f ≡ X + a·Xᵏ (mod X^{k+1})`. -/
def JetEq (k : ℕ) (f : K[X]) (a : K) : Prop :=
  X ^ (k + 1) ∣ f - (X + C a * X ^ k)

/-- For `k ≥ 2`, a jet `X + aXᵏ` is divisible by `X`, and its `k`-th power is `Xᵏ` modulo
`X^{k+1}`. -/
theorem jet_factor {m : ℕ} {f : K[X]} {a : K} (hf : JetEq (m + 2) f a) :
    X ∣ f ∧ X ^ (m + 3) ∣ f ^ (m + 2) - X ^ (m + 2) := by
  obtain ⟨r, hr⟩ := hf
  set u : K[X] := 1 + C a * X ^ (m + 1) + X ^ (m + 2) * r with hu
  have hfu : f = X * u := by rw [hu]; linear_combination hr
  have hu1 : X ∣ u - 1 := ⟨C a * X ^ m + X ^ (m + 1) * r, by rw [hu]; ring⟩
  refine ⟨⟨u, hfu⟩, ?_⟩
  have hpow : u - 1 ∣ u ^ (m + 2) - 1 ^ (m + 2) := sub_dvd_pow_sub_pow _ _ _
  rw [one_pow] at hpow
  obtain ⟨s, hs⟩ := dvd_trans hu1 hpow
  refine ⟨s, ?_⟩
  rw [hfu, mul_pow]
  linear_combination X ^ (m + 2) * hs

/-- Jets of order `k ≥ 2` add under composition. -/
theorem jet_comp {m : ℕ} {f g : K[X]} {a b : K}
    (hf : JetEq (m + 2) f a) (hg : JetEq (m + 2) g b) :
    JetEq (m + 2) (g.comp f) (a + b) := by
  obtain ⟨hXf, hpow⟩ := jet_factor hf
  obtain ⟨q, hq⟩ := hg
  have hg' : g = X + C b * X ^ (m + 2) + X ^ (m + 3) * q := by linear_combination hq
  have hcomp : g.comp f = f + C b * f ^ (m + 2) + f ^ (m + 3) * q.comp f := by
    rw [hg']; simp [add_comp, mul_comp, pow_comp]
  have h3 : X ^ (m + 3) ∣ f ^ (m + 3) * q.comp f :=
    dvd_mul_of_dvd_left (pow_dvd_pow_of_dvd hXf _) _
  have key : g.comp f - (X + C (a + b) * X ^ (m + 2)) =
      (f - (X + C a * X ^ (m + 2))) + C b * (f ^ (m + 2) - X ^ (m + 2))
        + f ^ (m + 3) * q.comp f := by
    rw [hcomp, C_add]; ring
  unfold JetEq at hf ⊢
  rw [key]
  exact dvd_add (dvd_add hf (dvd_mul_of_dvd_right hpow _)) h3

/-- `n`-fold self-composition. -/
noncomputable def iter (f : K[X]) (n : ℕ) : K[X] := (fun p => p.comp f)^[n] X

theorem iter_succ (f : K[X]) (n : ℕ) : iter f (n + 1) = (iter f n).comp f := by
  unfold iter; rw [Function.iterate_succ_apply']

/-- The `n`-fold self-composition of the jet `X + aXᵏ` is `X + n·a·Xᵏ`. -/
theorem jet_iterate {m : ℕ} {f : K[X]} {a : K} (hf : JetEq (m + 2) f a) (n : ℕ) :
    JetEq (m + 2) (iter f n) (n * a) := by
  induction n with
  | zero => simp [JetEq, iter]
  | succ n ih =>
    rw [iter_succ]
    have := jet_comp hf ih
    rw [show a + (n : K) * a = ((n + 1 : ℕ) : K) * a by push_cast; ring] at this
    exact this

end Jets

section CharZero

variable {K : Type*} [CommRing K] [IsDomain K] [CharZero K]

/-- **One step of rigidity.** If `f ≡ X (mod Xᵏ)`, `k ≥ 2`, and `f` has finite compositional
order, then `f ≡ X (mod X^{k+1})`. -/
theorem jet_step {m : ℕ} {f : K[X]} (hf : X ^ (m + 2) ∣ f - X) {n : ℕ} (hn : 1 ≤ n)
    (hord : iter f n = X) : X ^ (m + 3) ∣ f - X := by
  set a := f.coeff (m + 2)
  have hjet : JetEq (m + 2) f a := by
    unfold JetEq
    rw [X_pow_dvd_iff] at hf ⊢
    intro d hd
    rcases Nat.lt_succ_iff_lt_or_eq.mp hd with hlt | heq
    · have := hf d hlt
      simp only [coeff_sub, coeff_add, coeff_C_mul, coeff_X_pow] at this ⊢
      rw [if_neg (by omega)]; simpa using this
    · subst heq
      simp [coeff_X, a]
  have hit := jet_iterate hjet n
  rw [hord, JetEq, X_pow_dvd_iff] at hit
  have hk := hit (m + 2) (by omega)
  simp only [coeff_sub, coeff_add, coeff_C_mul, coeff_X_pow, if_pos, coeff_X] at hk
  have ha : a = 0 := by
    simp at hk
    rcases hk with h | h
    · omega
    · exact h
  rw [X_pow_dvd_iff]
  intro d hd
  rcases Nat.lt_succ_iff_lt_or_eq.mp hd with hlt | heq
  · exact (X_pow_dvd_iff.mp hf) d hlt
  · subst heq
    simp [coeff_X, ← ha, a]

/-- **Rigidity for polynomial maps.** `f(0) = 0`, `f'(0) = 1` and finite compositional order
force `f = X`. -/
theorem eq_X_of_finite_order {f : K[X]} (h1 : X ^ 2 ∣ f - X) {n : ℕ} (hn : 1 ≤ n)
    (hord : iter f n = X) : f = X := by
  have hall : ∀ m : ℕ, X ^ (m + 2) ∣ f - X := by
    intro m
    induction m with
    | zero => simpa using h1
    | succ m ih => exact jet_step ih hn hord
  have hcoeff : ∀ d, (f - X).coeff d = 0 := fun d =>
    (X_pow_dvd_iff.mp (hall d)) d (by omega)
  exact sub_eq_zero.mp (Polynomial.ext (by simpa using hcoeff))

end CharZero

/-- **Step 2.** A finite group with an injective homomorphism into the units of a domain
(for a stabiliser: `g ↦ g'(0)`, injective by Step 1) is cyclic. -/
theorem isCyclic_of_injective_derivative {G R : Type*} [Group G] [Finite G]
    [CommRing R] [IsDomain R] (d : G →* R) (hd : Function.Injective d) : IsCyclic G :=
  isCyclic_of_subgroup_isDomain d hd

end QOU.RiemannSurface.TangentJetRigidity
