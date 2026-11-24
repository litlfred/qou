import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Fintype.Basic
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring

/-!
# Symplectic `𝔽₂[S₅]` Structure and Unique Invariant Theta Characteristic on Bring's Curve (`qou-2a2o`, `qou-9l0d`)

Formalizes the finite-symplectic `𝔽₂[S₅]` representation on the mod-2 homology model
`H = V₀ ⊕ V₀* ≅ 𝔽₂⁸` of Bring's genus-4 curve (where `V₀ = {x ∈ 𝔽₂⁵ : ∑ xᵢ = 0}` is the
4-dimensional standard `S₅`-module, split over `𝔽₂` because `5 ≡ 1 (mod 2)`), together with
the affine space of all `2⁸ = 256` quadratic refinements `q : H → 𝔽₂` of its canonical
symplectic intersection form `ω`:

1. **Exact `S₅ → Sp(8, 𝔽₂)` representation (`rho_mul`, `Phi_preserves_omega`, `Phi_preserves_q0`):**
   Every `g ∈ S₅` acts symplectically on `H = V₀ ⊕ V₀*` and preserves the hyperbolic
   quadratic refinement `q₀(u, v) = u · v`.
2. **Constructive classification of all quadratic refinements (`existsUnique_char_of_isQuadRefinement`):**
   Every `q : H → 𝔽₂` satisfying `q(x + y) + q(x) + q(y) = ω(x, y)` is uniquely of the form
   `q_c(x) = q₀(x) + ω(c, x)` for `c ∈ H`.
3. **Genuine uniqueness proof of the `S₅`-invariant spin structure
   (`unique_fiveCycle_invariant_quadRefinement`, `unique_S5_invariant_quadRefinement`):**
   Replaces the insufficient `136 % 5 = 1` congruence check flagged in the `2026-11-21`
   review of `qou-2a2o` / PR `#8150` with a conceptual algebraic theorem: already under the
   order-5 cyclic subgroup `⟨fiveCycle⟩ ⊂ A₅ ⊂ S₅`, `q₀` is the **unique** invariant
   quadratic refinement of `ω` (and `q₀` is even, `Arf(q₀) = 0`).
4. **Exact Braden–Disney-Hogg (2024) orbit-size multisets (`even_orbit_partition_bdh`,
   `odd_orbit_partition_bdh`, `fiveCycle_fixed_points_bdh`):**
   Establishes an explicit isomorphism `b8Equiv : B8 ≃ H8` (`B8 = Bool⁸`) intertwining
   `bFive` / `bSwap` with `Phi fiveCycle` / `Phi swap01` (`ofB8_bFive`, `ofB8_bSwap`,
   `bArf_iff_q0`), and certifies by kernel `decide` the published orbit decompositions of
   Braden & Disney-Hogg (2024):
   * **Even theta characteristics (`Arf = 0`, total `136`, BDH Theorem 5.9):**
     `[1, 5, 5, 5, 10, 10, 10, 30, 30, 30]` (`10` orbits; corrects the erroneous
     `1 + 15 + 60 + 60` claim in unmerged PR `#8150` and bean `qou-9l0d`).
   * **Odd theta characteristics (`Arf = 1`, total `120`, BDH Corollary 5.7):**
     `[20, 20, 20, 60]` (`4` orbits; corrects the erroneous `60 + 60` orbit claim in
     unmerged PR `#8150` and bean `qou-9l0d`).
   * **Order-5 generator `S` orbits (BDH §5.3, Footnote 29):**
     `1` fixed even characteristic (`136 = 1 + 27 × 5`) and `0` fixed odd characteristics
     (`120 = 24 × 5`).

## Honest Scope & Non-Claims

* That `H₁(Σ₄, 𝔽₂)` of Bring's curve is symplectically `S₅`-isomorphic to `V₀ ⊕ V₀*` is cited
  to Braden & Disney-Hogg (2024) §2.2–2.3 & §5.3; Mathlib does not formalize the homology of
  algebraic curves.
* Per bean `qou-9l0d`'s anti-fit note, uniqueness of the `S₅`-invariant even theta
  characteristic (the Szegő / Burns spin structure) is a classical theorem of algebraic
  geometry, not a QOU prediction.
* Per bean `qou-2a2o`, which principal bundle on Bring's surface the brane tower lifts
  remains open.

-- Ref: [braden-disney-hogg-2022] Braden & Disney-Hogg, "Bring's curve: old and new," Eur. J. Math. 10 (2024), Cor. 5.7, Thm. 5.9, Cor. 5.10 (`library/s40879-023-00706-0`).
-- Ref: [atiyah1971] Atiyah, "Riemann surfaces and spin structures," Ann. Sci. ÉNS 4 (1971), 47–62.
-/

namespace QOU.BringsSurface.ThetaSymplectic

open scoped BigOperators

/-! ## §1 — Characteristic-2 helpers and the 4D standard `𝔽₂[S₅]`-module `V₄` -/

abbrev V4 := Fin 4 → ZMod 2
abbrev V5 := Fin 5 → ZMod 2
abbrev H8 := V4 × V4

theorem zmod2_add_self (a : ZMod 2) : a + a = 0 := by
  fin_cases a <;> decide

theorem zmod2_two_mul (a : ZMod 2) : 2 * a = 0 := by
  fin_cases a <;> decide

theorem zmod2_zero_or_one (a : ZMod 2) : a = 0 ∨ a = 1 := by
  fin_cases a <;> simp

theorem zmod2_eq_of_add_eq_zero {a b : ZMod 2} (h : a + b = 0) : a = b := by
  calc a = a + (b + b) := by rw [zmod2_add_self, add_zero]
    _ = (a + b) + b := by ring
    _ = b := by rw [h, zero_add]

theorem v4_add_self (u : V4) : u + u = 0 := by
  funext i
  exact zmod2_add_self (u i)

theorem v4_eq_of_add_eq_zero {u w : V4} (h : u + w = 0) : u = w := by
  funext i
  exact zmod2_eq_of_add_eq_zero (congrFun h i)

theorem h8_eq_of_add_eq_zero {x y : H8} (h : x + y = 0) : x = y := by
  ext i
  · exact zmod2_eq_of_add_eq_zero (congrFun (congrArg Prod.fst h) i)
  · exact zmod2_eq_of_add_eq_zero (congrFun (congrArg Prod.snd h) i)

/-- Zero-sum embedding `V₄ → V₅`: `(u₀, u₁, u₂, u₃) ↦ (u₀, u₁, u₂, u₃, u₀ + u₁ + u₂ + u₃)`. -/
def incl (u : V4) : V5
  | 0 => u 0
  | 1 => u 1
  | 2 => u 2
  | 3 => u 3
  | 4 => u 0 + u 1 + u 2 + u 3

/-- Restriction `V₅ → V₄` onto the first four coordinates. -/
def proj (x : V5) : V4 :=
  fun i => x i.castSucc

theorem proj_incl (u : V4) : proj (incl u) = u := by
  funext i
  fin_cases i <;> rfl

theorem sum5_incl (u : V4) : (∑ k : Fin 5, incl u k) = 0 := by
  rw [Fin.sum_univ_five]
  have h2 : incl u 0 + incl u 1 + incl u 2 + incl u 3 + incl u 4 =
      2 * (u 0 + u 1 + u 2 + u 3) := by
    simp only [incl]; ring
  rw [h2]
  exact zmod2_two_mul _

theorem incl_proj_of_sum_zero {x : V5} (hx : (∑ k : Fin 5, x k) = 0) :
    incl (proj x) = x := by
  rw [Fin.sum_univ_five] at hx
  have hx4 : x 0 + x 1 + x 2 + x 3 = x 4 := by
    apply zmod2_eq_of_add_eq_zero
    simpa [add_assoc] using hx
  funext k
  fin_cases k
  · rfl
  · rfl
  · rfl
  · rfl
  · simp [incl, proj, hx4]

theorem incl_add (u w : V4) : incl (u + w) = incl u + incl w := by
  funext k
  fin_cases k
  · simp [incl]
  · simp [incl]
  · simp [incl]
  · simp [incl]
  · simp only [incl, Pi.add_apply]; ring

/-- Permutation action of `S₅` on `V₅`. -/
def permAct (g : Equiv.Perm (Fin 5)) (x : V5) : V5 :=
  fun k => x (g⁻¹ k)

theorem sum5_permAct (g : Equiv.Perm (Fin 5)) (x : V5) :
    (∑ k : Fin 5, permAct g x k) = ∑ k : Fin 5, x k :=
  Equiv.sum_comp g⁻¹ x

theorem permAct_mul (g h : Equiv.Perm (Fin 5)) (x : V5) :
    permAct (g * h) x = permAct g (permAct h x) := by
  funext k
  simp [permAct, mul_inv_rev]

/-- The 4-dimensional standard `𝔽₂[S₅]`-representation `ρ : S₅ → End(V₄)`. -/
def rho (g : Equiv.Perm (Fin 5)) (u : V4) : V4 :=
  proj (permAct g (incl u))

@[simp]
theorem rho_one (u : V4) : rho 1 u = u :=
  proj_incl u

theorem rho_mul (g h : Equiv.Perm (Fin 5)) (u : V4) :
    rho (g * h) u = rho g (rho h u) := by
  unfold rho
  rw [permAct_mul, incl_proj_of_sum_zero]
  rw [sum5_permAct, sum5_incl]

theorem rho_inv_apply (g : Equiv.Perm (Fin 5)) (u : V4) :
    rho g⁻¹ (rho g u) = u := by
  rw [← rho_mul, inv_mul_cancel, rho_one]

theorem rho_apply_inv (g : Equiv.Perm (Fin 5)) (u : V4) :
    rho g (rho g⁻¹ u) = u := by
  rw [← rho_mul, mul_inv_cancel, rho_one]

theorem rho_add (g : Equiv.Perm (Fin 5)) (u w : V4) :
    rho g (u + w) = rho g u + rho g w := by
  funext i
  simp [rho, proj, permAct, incl_add]

theorem rho_zero (g : Equiv.Perm (Fin 5)) : rho g 0 = 0 := by
  have h := rho_add g 0 0
  rw [add_zero] at h
  exact h.trans (v4_add_self (rho g 0))

theorem rho_smul (g : Equiv.Perm (Fin 5)) (c : ZMod 2) (u : V4) :
    rho g (fun j => c * u j) = fun j => c * rho g u j := by
  rcases zmod2_zero_or_one c with rfl | rfl
  · have h0 : (fun j : Fin 4 => (0 : ZMod 2) * u j) = 0 := by funext j; simp
    rw [h0, rho_zero]
    funext j; simp
  · funext j; simp

/-! ## §2 — Dual representation `ρ*`, symplectic pairing `ω`, and `S₅ → Sp(8, 𝔽₂)` -/

/-- Standard `𝔽₂`-bilinear pairing on `V₄`. -/
def dot4 (u v : V4) : ZMod 2 :=
  u 0 * v 0 + u 1 * v 1 + u 2 * v 2 + u 3 * v 3

theorem dot4_add_left (u₁ u₂ v : V4) :
    dot4 (u₁ + u₂) v = dot4 u₁ v + dot4 u₂ v := by
  simp only [dot4, Pi.add_apply]; ring

theorem dot4_add_right (u v₁ v₂ : V4) :
    dot4 u (v₁ + v₂) = dot4 u v₁ + dot4 u v₂ := by
  simp only [dot4, Pi.add_apply]; ring

/-- Standard basis vectors of `V₄`. -/
def e4 (i : Fin 4) : V4 :=
  fun j => if j = i then 1 else 0

theorem v4_decomp (u : V4) :
    u = (fun j => u 0 * e4 0 j) + (fun j => u 1 * e4 1 j) +
        (fun j => u 2 * e4 2 j) + (fun j => u 3 * e4 3 j) := by
  funext j
  fin_cases j <;> simp [e4]

/-- Contragredient `S₅`-action `ρ*(g) = (ρ(g⁻¹))ᵀ` on `V₄*`. -/
def rhoDual (g : Equiv.Perm (Fin 5)) (v : V4) : V4 :=
  fun i => dot4 (rho g⁻¹ (e4 i)) v

theorem dot4_rho_inv_eq_rhoDual (g : Equiv.Perm (Fin 5)) (u v : V4) :
    dot4 (rho g⁻¹ u) v = dot4 u (rhoDual g v) := by
  conv_lhs => rw [v4_decomp u]
  simp only [rho_add, rho_smul, dot4_add_left]
  simp only [dot4, rhoDual]
  ring

/-- `ρ(g)` and `ρ*(g)` preserve the canonical pairing `dot4`. -/
theorem dot4_rho_rhoDual (g : Equiv.Perm (Fin 5)) (u v : V4) :
    dot4 (rho g u) (rhoDual g v) = dot4 u v := by
  rw [← dot4_rho_inv_eq_rhoDual, rho_inv_apply]

theorem dot4_eq_zero_imp {v : V4} (h : ∀ u : V4, dot4 u v = 0) : v = 0 := by
  funext i
  fin_cases i
  · simpa [dot4, e4] using h (e4 0)
  · simpa [dot4, e4] using h (e4 1)
  · simpa [dot4, e4] using h (e4 2)
  · simpa [dot4, e4] using h (e4 3)

theorem rhoDual_one (v : V4) : rhoDual 1 v = v := by
  apply v4_eq_of_add_eq_zero
  apply dot4_eq_zero_imp
  intro u
  rw [dot4_add_right, ← dot4_rho_inv_eq_rhoDual, inv_one, rho_one, zmod2_add_self]

theorem rhoDual_mul (g h : Equiv.Perm (Fin 5)) (v : V4) :
    rhoDual (g * h) v = rhoDual g (rhoDual h v) := by
  apply v4_eq_of_add_eq_zero
  apply dot4_eq_zero_imp
  intro u
  rw [dot4_add_right, ← dot4_rho_inv_eq_rhoDual, ← dot4_rho_inv_eq_rhoDual,
      ← dot4_rho_inv_eq_rhoDual, mul_inv_rev, rho_mul, zmod2_add_self]

/-- Hyperbolic quadratic form `q₀(u, v) = u · v` on `H = V₄ × V₄`. -/
def q0 (x : H8) : ZMod 2 :=
  dot4 x.1 x.2

/-- Canonical alternating symplectic intersection form `ω((u₁, v₁), (u₂, v₂)) = u₁·v₂ + u₂·v₁`. -/
def omega (x y : H8) : ZMod 2 :=
  dot4 x.1 y.2 + dot4 y.1 x.2

/-- Symplectic `S₅`-action `Φ(g)(u, v) = (ρ(g)u, ρ*(g)v)` on `H = V₄ × V₄`. -/
def Phi (g : Equiv.Perm (Fin 5)) (x : H8) : H8 :=
  (rho g x.1, rhoDual g x.2)

@[simp]
theorem Phi_one (x : H8) : Phi 1 x = x := by
  cases x
  simp [Phi, rho_one, rhoDual_one]

theorem Phi_mul (g h : Equiv.Perm (Fin 5)) (x : H8) :
    Phi (g * h) x = Phi g (Phi h x) := by
  cases x
  simp [Phi, rho_mul, rhoDual_mul]

theorem Phi_inv_apply (g : Equiv.Perm (Fin 5)) (x : H8) :
    Phi g⁻¹ (Phi g x) = x := by
  rw [← Phi_mul, inv_mul_cancel, Phi_one]

theorem Phi_apply_inv (g : Equiv.Perm (Fin 5)) (x : H8) :
    Phi g (Phi g⁻¹ x) = x := by
  rw [← Phi_mul, mul_inv_cancel, Phi_one]

/-- `Φ(g)` preserves `q₀` for every `g ∈ S₅`. -/
theorem Phi_preserves_q0 (g : Equiv.Perm (Fin 5)) (x : H8) :
    q0 (Phi g x) = q0 x :=
  dot4_rho_rhoDual g x.1 x.2

/-- `Φ(g) ∈ Sp(8, 𝔽₂)`: `Φ(g)` preserves the symplectic pairing `ω` for every `g ∈ S₅`. -/
theorem Phi_preserves_omega (g : Equiv.Perm (Fin 5)) (x y : H8) :
    omega (Phi g x) (Phi g y) = omega x y := by
  simp only [omega, Phi, dot4_rho_rhoDual]

theorem omega_self_zero (x : H8) : omega x x = 0 :=
  zmod2_add_self (dot4 x.1 x.2)

theorem omega_symm (x y : H8) : omega x y = omega y x :=
  add_comm _ _

theorem omega_add_left (x₁ x₂ y : H8) :
    omega (x₁ + x₂) y = omega x₁ y + omega x₂ y := by
  simp only [omega, Prod.fst_add, Prod.snd_add, dot4_add_left, dot4_add_right]; ring

theorem omega_add_right (x y₁ y₂ : H8) :
    omega x (y₁ + y₂) = omega x y₁ + omega x y₂ := by
  simp only [omega, Prod.fst_add, Prod.snd_add, dot4_add_left, dot4_add_right]; ring

/-- Nondegeneracy of `ω` on `H = V₄ × V₄`. -/
theorem omega_nondeg {x : H8} (h : ∀ y : H8, omega x y = 0) : x = 0 := by
  ext i
  · fin_cases i
    · simpa [omega, dot4, e4] using h (0, e4 0)
    · simpa [omega, dot4, e4] using h (0, e4 1)
    · simpa [omega, dot4, e4] using h (0, e4 2)
    · simpa [omega, dot4, e4] using h (0, e4 3)
  · fin_cases i
    · simpa [omega, dot4, e4] using h (e4 0, 0)
    · simpa [omega, dot4, e4] using h (e4 1, 0)
    · simpa [omega, dot4, e4] using h (e4 2, 0)
    · simpa [omega, dot4, e4] using h (e4 3, 0)

/-! ## §3 — Quadratic refinements of `ω` (theta characteristics / spin structures) -/

/-- `q : H → 𝔽₂` is a quadratic refinement of the symplectic form `ω`. -/
def IsQuadRefinement (q : H8 → ZMod 2) : Prop :=
  ∀ x y : H8, q (x + y) + q x + q y = omega x y

theorem IsQuadRefinement.map_zero {q : H8 → ZMod 2} (hq : IsQuadRefinement q) :
    q 0 = 0 := by
  have h := hq 0 0
  rw [add_zero, omega_self_zero, add_assoc, zmod2_add_self, add_zero] at h
  exact h

theorem q0_isQuadRefinement : IsQuadRefinement q0 := by
  intro x y
  simp only [q0, omega, Prod.fst_add, Prod.snd_add, dot4_add_left, dot4_add_right]
  have h1 := zmod2_add_self (dot4 x.1 x.2)
  have h2 := zmod2_add_self (dot4 y.1 y.2)
  calc (dot4 x.1 x.2 + dot4 y.1 x.2 + (dot4 x.1 y.2 + dot4 y.1 y.2)) +
        dot4 x.1 x.2 + dot4 y.1 y.2
      = (dot4 x.1 x.2 + dot4 x.1 x.2) + (dot4 y.1 y.2 + dot4 y.1 y.2) +
          (dot4 x.1 y.2 + dot4 y.1 x.2) := by ring
    _ = dot4 x.1 y.2 + dot4 y.1 x.2 := by rw [h1, h2]; ring

/-- The quadratic refinement `q_c(x) = q₀(x) + ω(c, x)` indexed by `c ∈ H`. -/
def qc (c : H8) (x : H8) : ZMod 2 :=
  q0 x + omega c x

theorem qc_zero : qc 0 = q0 := by
  funext x
  simp [qc, omega, dot4]

theorem qc_isQuadRefinement (c : H8) : IsQuadRefinement (qc c) := by
  intro x y
  have h0 := q0_isQuadRefinement x y
  have hw := omega_add_right c x y
  calc qc c (x + y) + qc c x + qc c y
      = (q0 (x + y) + q0 x + q0 y) + (omega c (x + y) + (omega c x + omega c y)) := by
          simp only [qc]; ring
    _ = omega x y + (omega c (x + y) + omega c (x + y)) := by rw [h0, ← hw]
    _ = omega x y := by rw [zmod2_add_self, add_zero]

theorem qc_injective {c₁ c₂ : H8} (h : qc c₁ = qc c₂) : c₁ = c₂ := by
  apply h8_eq_of_add_eq_zero
  apply omega_nondeg
  intro x
  have hx := congrFun h x
  have hadd : q0 x + omega c₁ x + (q0 x + omega c₂ x) = 0 := by
    rw [show q0 x + omega c₁ x = qc c₁ x from rfl,
        show q0 x + omega c₂ x = qc c₂ x from rfl, hx, zmod2_add_self]
  calc omega (c₁ + c₂) x
      = omega c₁ x + omega c₂ x := omega_add_left c₁ c₂ x
    _ = (q0 x + q0 x) + (omega c₁ x + omega c₂ x) := by rw [zmod2_add_self, zero_add]
    _ = q0 x + omega c₁ x + (q0 x + omega c₂ x) := by ring
    _ = 0 := hadd

/-- Explicit scalar multiplication on `H8` over `ZMod 2`. -/
def smulH8 (a : ZMod 2) (x : H8) : H8 :=
  (fun j => a * x.1 j, fun j => a * x.2 j)

/-- **Constructive bijection between quadratic refinements of `ω` and `H = 𝔽₂⁸`.** -/
theorem existsUnique_char_of_isQuadRefinement {q : H8 → ZMod 2} (hq : IsQuadRefinement q) :
    ∃! c : H8, q = qc c := by
  let d : H8 → ZMod 2 := fun x => q x + q0 x
  have hd_add : ∀ x y : H8, d (x + y) = d x + d y := by
    intro x y
    apply zmod2_eq_of_add_eq_zero
    have h1 := hq x y
    have h2 := q0_isQuadRefinement x y
    calc d (x + y) + (d x + d y)
        = (q (x + y) + q x + q y) + (q0 (x + y) + q0 x + q0 y) := by simp only [d]; ring
      _ = omega x y + omega x y := by rw [h1, h2]
      _ = 0 := zmod2_add_self _
  have hd_zero : d 0 = 0 := by
    simp [d, hq.map_zero, q0, dot4]
  have hd_smul : ∀ (a : ZMod 2) (x : H8), d (smulH8 a x) = a * d x := by
    intro a x
    rcases zmod2_zero_or_one a with rfl | rfl
    · have h0 : smulH8 0 x = 0 := by ext j <;> simp [smulH8]
      rw [h0, hd_zero, zero_mul]
    · have h1 : smulH8 1 x = x := by ext j <;> simp [smulH8]
      rw [h1, one_mul]
  let c : H8 := (fun i => d (0, e4 i), fun i => d (e4 i, 0))
  have hqc : q = qc c := by
    funext x
    rcases x with ⟨u, v⟩
    have hu : (u, (0 : V4)) =
        smulH8 (u 0) (e4 0, 0) + smulH8 (u 1) (e4 1, 0) +
        smulH8 (u 2) (e4 2, 0) + smulH8 (u 3) (e4 3, 0) := by
      ext j
      · fin_cases j <;> simp [smulH8, e4]
      · simp [smulH8]
    have hv : ((0 : V4), v) =
        smulH8 (v 0) (0, e4 0) + smulH8 (v 1) (0, e4 1) +
        smulH8 (v 2) (0, e4 2) + smulH8 (v 3) (0, e4 3) := by
      ext j
      · simp [smulH8]
      · fin_cases j <;> simp [smulH8, e4]
    have huv : (u, v) = (u, 0) + (0, v) := by ext j <;> simp
    have hd_eq : d (u, v) = omega c (u, v) := by
      conv_lhs => rw [huv, hd_add, hu, hv]
      simp only [hd_add, hd_smul]
      simp only [omega, dot4, c]
      ring
    apply zmod2_eq_of_add_eq_zero
    calc q (u, v) + qc c (u, v)
        = d (u, v) + omega c (u, v) := by simp only [d, qc]; ring
      _ = 0 := by rw [hd_eq, zmod2_add_self]
  exact ⟨c, hqc, fun c' hc' => qc_injective (hc'.symm.trans hqc)⟩

/-- Equivariance of `qc`: pulling `qc c` along `Φ(g)` shifts its characteristic by `Φ(g⁻¹) c`. -/
theorem qc_comp_Phi (g : Equiv.Perm (Fin 5)) (c x : H8) :
    qc c (Phi g x) = qc (Phi g⁻¹ c) x := by
  simp only [qc, Phi_preserves_q0]
  congr 1
  calc omega c (Phi g x)
      = omega (Phi g (Phi g⁻¹ c)) (Phi g x) := by rw [Phi_apply_inv]
    _ = omega (Phi g⁻¹ c) x := Phi_preserves_omega g _ _

/-! ## §4 — Genuine Uniqueness of the `S₅`-Invariant Spin Structure (`qou-2a2o`) -/

/-- The order-5 cyclic generator `(0 1 2 3 4) ∈ A₅ ⊂ S₅` and transposition `(0 1)`. -/
def fiveCycle : Equiv.Perm (Fin 5) := finRotate 5
def swap01 : Equiv.Perm (Fin 5) := Equiv.swap 0 1

theorem fiveCycle_apply_vals :
    fiveCycle 0 = 1 ∧ fiveCycle 1 = 2 ∧ fiveCycle 2 = 3 ∧
      fiveCycle 3 = 4 ∧ fiveCycle 4 = 0 := by
  decide

theorem fiveCycle_inv_vals :
    fiveCycle⁻¹ 0 = 4 ∧ fiveCycle⁻¹ 1 = 0 ∧ fiveCycle⁻¹ 2 = 1 ∧
      fiveCycle⁻¹ 3 = 2 ∧ fiveCycle⁻¹ 4 = 3 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;>
    rw [Equiv.Perm.inv_eq_iff_eq] <;>
    simp [fiveCycle_apply_vals]

theorem rho_fiveCycle_coords (u : V4) :
    rho fiveCycle u 0 = u 0 + u 1 + u 2 + u 3 ∧
    rho fiveCycle u 1 = u 0 ∧
    rho fiveCycle u 2 = u 1 ∧
    rho fiveCycle u 3 = u 2 := by
  obtain ⟨i0, i1, i2, i3, _⟩ := fiveCycle_inv_vals
  refine ⟨?_, ?_, ?_, ?_⟩
  · change incl u (fiveCycle⁻¹ 0) = _; rw [i0]; rfl
  · change incl u (fiveCycle⁻¹ 1) = _; rw [i1]; rfl
  · change incl u (fiveCycle⁻¹ 2) = _; rw [i2]; rfl
  · change incl u (fiveCycle⁻¹ 3) = _; rw [i3]; rfl

theorem rho_fiveCycle_inv_coords (u : V4) :
    rho fiveCycle⁻¹ u 0 = u 1 ∧
    rho fiveCycle⁻¹ u 1 = u 2 ∧
    rho fiveCycle⁻¹ u 2 = u 3 ∧
    rho fiveCycle⁻¹ u 3 = u 0 + u 1 + u 2 + u 3 := by
  obtain ⟨a0, a1, a2, a3, _⟩ := fiveCycle_apply_vals
  refine ⟨?_, ?_, ?_, ?_⟩
  · change incl u ((fiveCycle⁻¹)⁻¹ 0) = _; rw [inv_inv, a0]; rfl
  · change incl u ((fiveCycle⁻¹)⁻¹ 1) = _; rw [inv_inv, a1]; rfl
  · change incl u ((fiveCycle⁻¹)⁻¹ 2) = _; rw [inv_inv, a2]; rfl
  · change incl u ((fiveCycle⁻¹)⁻¹ 3) = _; rw [inv_inv, a3]; rfl

theorem rhoDual_fiveCycle_coords (v : V4) :
    rhoDual fiveCycle v 0 = v 3 ∧
    rhoDual fiveCycle v 1 = v 0 + v 3 ∧
    rhoDual fiveCycle v 2 = v 1 + v 3 ∧
    rhoDual fiveCycle v 3 = v 2 + v 3 := by
  have c0 := rho_fiveCycle_inv_coords (e4 0)
  have c1 := rho_fiveCycle_inv_coords (e4 1)
  have c2 := rho_fiveCycle_inv_coords (e4 2)
  have c3 := rho_fiveCycle_inv_coords (e4 3)
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp [rhoDual, dot4, c0.1, c0.2.1, c0.2.2.1, c0.2.2.2, e4]
  · simp [rhoDual, dot4, c1.1, c1.2.1, c1.2.2.1, c1.2.2.2, e4]
  · simp [rhoDual, dot4, c2.1, c2.2.1, c2.2.2.1, c2.2.2.2, e4]
  · simp [rhoDual, dot4, c3.1, c3.2.1, c3.2.2.1, c3.2.2.2, e4]

theorem rho_fiveCycle_fixed_iff (u : V4) : rho fiveCycle u = u ↔ u = 0 := by
  constructor
  · intro h
    obtain ⟨c0, c1, c2, c3⟩ := rho_fiveCycle_coords u
    have e0 : u 0 + u 1 + u 2 + u 3 = u 0 := c0.symm.trans (congrFun h 0)
    have e1 : u 0 = u 1 := c1.symm.trans (congrFun h 1)
    have e2 : u 1 = u 2 := c2.symm.trans (congrFun h 2)
    have e3 : u 2 = u 3 := c3.symm.trans (congrFun h 3)
    have u0_zero : u 0 = 0 := by
      rw [← e3, ← e2, ← e1] at e0
      have h4 : u 0 + u 0 + u 0 + u 0 = 0 := by
        calc u 0 + u 0 + u 0 + u 0
            = (u 0 + u 0) + (u 0 + u 0) := by ring
          _ = 0 := by simp [zmod2_add_self]
      exact e0.symm.trans h4
    funext i
    fin_cases i
    · exact u0_zero
    · exact e1.symm.trans u0_zero
    · exact e2.symm.trans (e1.symm.trans u0_zero)
    · exact e3.symm.trans (e2.symm.trans (e1.symm.trans u0_zero))
  · rintro rfl
    exact rho_zero fiveCycle

theorem rhoDual_fiveCycle_fixed_iff (v : V4) : rhoDual fiveCycle v = v ↔ v = 0 := by
  constructor
  · intro h
    obtain ⟨d0, d1, d2, d3⟩ := rhoDual_fiveCycle_coords v
    have ev0 : v 3 = v 0 := d0.symm.trans (congrFun h 0)
    have ev1 : v 1 = 0 := by
      have := d1.symm.trans (congrFun h 1)
      rw [← ev0, zmod2_add_self] at this
      exact this.symm
    have ev2 : v 3 = v 2 := by
      have := d2.symm.trans (congrFun h 2)
      simpa [ev1] using this
    have ev3 : v 3 = 0 := by
      have := d3.symm.trans (congrFun h 3)
      rw [← ev2, zmod2_add_self] at this
      exact this.symm
    funext i
    fin_cases i
    · exact ev0.symm.trans ev3
    · exact ev1
    · exact ev2.symm.trans ev3
    · exact ev3
  · rintro rfl
    obtain ⟨d0, d1, d2, d3⟩ := rhoDual_fiveCycle_coords 0
    funext i
    fin_cases i
    · simpa using d0
    · simpa using d1
    · simpa using d2
    · simpa using d3

theorem Phi_fiveCycle_fixed_iff (c : H8) : Phi fiveCycle c = c ↔ c = 0 := by
  rcases c with ⟨u, v⟩
  simp only [Phi, Prod.mk.injEq, Prod.mk_eq_zero]
  rw [rho_fiveCycle_fixed_iff, rhoDual_fiveCycle_fixed_iff]

/-- **Uniqueness under the order-5 generator `S` (BDH §5.3, Theorem 5.11 strategy).**
Among all `256` quadratic refinements of `ω`, `q₀` is the **unique** refinement invariant
under the 5-cycle `fiveCycle`. -/
theorem unique_fiveCycle_invariant_quadRefinement
    {q : H8 → ZMod 2} (hq : IsQuadRefinement q) :
    (∀ x : H8, q (Phi fiveCycle x) = q x) ↔ q = q0 := by
  obtain ⟨c, rfl, _⟩ := existsUnique_char_of_isQuadRefinement hq
  constructor
  · intro hinv
    have hfun : qc (Phi fiveCycle⁻¹ c) = qc c := by
      funext x
      rw [← qc_comp_Phi, hinv]
    have hc : Phi fiveCycle⁻¹ c = c := qc_injective hfun
    have hc' : Phi fiveCycle c = c := by
      have := congrArg (Phi fiveCycle) hc
      rw [Phi_apply_inv] at this
      exact this.symm
    rw [(Phi_fiveCycle_fixed_iff c).mp hc', qc_zero]
  · intro hq0 x
    rw [hq0]
    exact Phi_preserves_q0 fiveCycle x

/-- **Uniqueness of the `S₅`-invariant theta characteristic (`qou-2a2o`, BDH Corollary 5.10).**
Among all `256` quadratic refinements of `ω`, `q₀` is the **unique** `S₅`-invariant spin
structure, and its Arf parameter is `q₀(0) = 0` (even). -/
theorem unique_S5_invariant_quadRefinement
    {q : H8 → ZMod 2} (hq : IsQuadRefinement q) :
    (∀ g : Equiv.Perm (Fin 5), ∀ x : H8, q (Phi g x) = q x) ↔ q = q0 := by
  constructor
  · intro hS5
    exact (unique_fiveCycle_invariant_quadRefinement hq).mp (hS5 fiveCycle)
  · rintro rfl g x
    exact Phi_preserves_q0 g x

theorem q0_arf_param_even : q0 0 = 0 := rfl

/-! ## §5 — `Bool⁸` Model (`B8 ≃ H8`) and Exact Braden–Disney-Hogg Orbit Partitions (`qou-9l0d`) -/

theorem swap01_apply_vals :
    swap01 0 = 1 ∧ swap01 1 = 0 ∧ swap01 2 = 2 ∧ swap01 3 = 3 ∧ swap01 4 = 4 := by
  decide

theorem swap01_inv_eq : swap01⁻¹ = swap01 :=
  Equiv.swap_inv 0 1

theorem rho_swap01_coords (u : V4) :
    rho swap01 u 0 = u 1 ∧ rho swap01 u 1 = u 0 ∧
    rho swap01 u 2 = u 2 ∧ rho swap01 u 3 = u 3 := by
  obtain ⟨s0, s1, s2, s3, _⟩ := swap01_apply_vals
  refine ⟨?_, ?_, ?_, ?_⟩
  · change incl u (swap01⁻¹ 0) = _; rw [swap01_inv_eq, s0]; rfl
  · change incl u (swap01⁻¹ 1) = _; rw [swap01_inv_eq, s1]; rfl
  · change incl u (swap01⁻¹ 2) = _; rw [swap01_inv_eq, s2]; rfl
  · change incl u (swap01⁻¹ 3) = _; rw [swap01_inv_eq, s3]; rfl

theorem rhoDual_swap01_coords (v : V4) :
    rhoDual swap01 v 0 = v 1 ∧ rhoDual swap01 v 1 = v 0 ∧
    rhoDual swap01 v 2 = v 2 ∧ rhoDual swap01 v 3 = v 3 := by
  have c0 := rho_swap01_coords (e4 0)
  have c1 := rho_swap01_coords (e4 1)
  have c2 := rho_swap01_coords (e4 2)
  have c3 := rho_swap01_coords (e4 3)
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp [rhoDual, swap01_inv_eq, dot4, c0.1, c0.2.1, c0.2.2.1, c0.2.2.2, e4]
  · simp [rhoDual, swap01_inv_eq, dot4, c1.1, c1.2.1, c1.2.2.1, c1.2.2.2, e4]
  · simp [rhoDual, swap01_inv_eq, dot4, c2.1, c2.2.1, c2.2.2.1, c2.2.2.2, e4]
  · simp [rhoDual, swap01_inv_eq, dot4, c3.1, c3.2.1, c3.2.2.1, c3.2.2.2, e4]

/-- 8-bit boolean tuple `Bool⁸` (zero unary `Nat` overhead in kernel reduction). -/
abbrev B8 := Bool × Bool × Bool × Bool × Bool × Bool × Bool × Bool

def bToZ (b : Bool) : ZMod 2 := if b then 1 else 0
def zToB (a : ZMod 2) : Bool := a == 1

theorem zToB_bToZ (b : Bool) : zToB (bToZ b) = b := by
  cases b <;> decide

theorem bToZ_zToB (a : ZMod 2) : bToZ (zToB a) = a := by
  fin_cases a <;> decide

theorem bToZ_xor (a b : Bool) : bToZ (xor a b) = bToZ a + bToZ b := by
  cases a <;> cases b <;> decide

theorem bToZ_and (a b : Bool) : bToZ (a && b) = bToZ a * bToZ b := by
  cases a <;> cases b <;> decide

/-- Explicit bijection `B8 ≃ H8 = V₄ × V₄`. -/
def ofB8 (b : B8) : H8 :=
  let (u0, u1, u2, u3, v0, v1, v2, v3) := b
  (fun i => match i with | 0 => bToZ u0 | 1 => bToZ u1 | 2 => bToZ u2 | 3 => bToZ u3,
   fun i => match i with | 0 => bToZ v0 | 1 => bToZ v1 | 2 => bToZ v2 | 3 => bToZ v3)

def toB8 (x : H8) : B8 :=
  (zToB (x.1 0), zToB (x.1 1), zToB (x.1 2), zToB (x.1 3),
   zToB (x.2 0), zToB (x.2 1), zToB (x.2 2), zToB (x.2 3))

theorem toB8_ofB8 (b : B8) : toB8 (ofB8 b) = b := by
  rcases b with ⟨u0, u1, u2, u3, v0, v1, v2, v3⟩
  simp [toB8, ofB8, zToB_bToZ]

theorem ofB8_toB8 (x : H8) : ofB8 (toB8 x) = x := by
  ext i
  · fin_cases i <;> simp [toB8, ofB8, bToZ_zToB]
  · fin_cases i <;> simp [toB8, ofB8, bToZ_zToB]

def b8Equiv : B8 ≃ H8 where
  toFun := ofB8
  invFun := toB8
  left_inv := toB8_ofB8
  right_inv := ofB8_toB8

/-- `Bool⁸` Arf invariant `q₀`, `fiveCycle` action, and `swap01` action. -/
def bArf (b : B8) : Bool :=
  let (u0, u1, u2, u3, v0, v1, v2, v3) := b
  xor (xor (u0 && v0) (u1 && v1)) (xor (u2 && v2) (u3 && v3))

def bFive (b : B8) : B8 :=
  let (u0, u1, u2, u3, v0, v1, v2, v3) := b
  (xor (xor u0 u1) (xor u2 u3), u0, u1, u2, v3, xor v0 v3, xor v1 v3, xor v2 v3)

def bSwap (b : B8) : B8 :=
  let (u0, u1, u2, u3, v0, v1, v2, v3) := b
  (u1, u0, u2, u3, v1, v0, v2, v3)

theorem bToZ_bArf (b : B8) : bToZ (bArf b) = q0 (ofB8 b) := by
  rcases b with ⟨u0, u1, u2, u3, v0, v1, v2, v3⟩
  simp only [bArf, q0, dot4, ofB8, bToZ_xor, bToZ_and]
  ring

theorem bArf_iff_q0 (b : B8) : bArf b = true ↔ q0 (ofB8 b) = 1 := by
  rw [← bToZ_bArf]
  cases bArf b <;> decide

private theorem v4_ext {f g : V4}
    (h0 : f 0 = g 0) (h1 : f 1 = g 1) (h2 : f 2 = g 2) (h3 : f 3 = g 3) : f = g := by
  funext i
  fin_cases i
  · exact h0
  · exact h1
  · exact h2
  · exact h3

theorem ofB8_bFive (b : B8) : ofB8 (bFive b) = Phi fiveCycle (ofB8 b) := by
  rcases b with ⟨u0, u1, u2, u3, v0, v1, v2, v3⟩
  have cu := rho_fiveCycle_coords (ofB8 (u0, u1, u2, u3, v0, v1, v2, v3)).1
  have cv := rhoDual_fiveCycle_coords (ofB8 (u0, u1, u2, u3, v0, v1, v2, v3)).2
  apply Prod.ext
  · refine v4_ext ?_ cu.2.1.symm cu.2.2.1.symm cu.2.2.2.symm
    conv_lhs => dsimp only [ofB8, bFive]
    conv_rhs => dsimp only [Phi]
    rw [cu.1]; simp only [ofB8, bToZ_xor]; ring
  · refine v4_ext cv.1.symm ?_ ?_ ?_
    · conv_lhs => dsimp only [ofB8, bFive]
      conv_rhs => dsimp only [Phi]
      rw [cv.2.1]; simp only [ofB8, bToZ_xor]
    · conv_lhs => dsimp only [ofB8, bFive]
      conv_rhs => dsimp only [Phi]
      rw [cv.2.2.1]; simp only [ofB8, bToZ_xor]
    · conv_lhs => dsimp only [ofB8, bFive]
      conv_rhs => dsimp only [Phi]
      rw [cv.2.2.2]; simp only [ofB8, bToZ_xor]

theorem ofB8_bSwap (b : B8) : ofB8 (bSwap b) = Phi swap01 (ofB8 b) := by
  rcases b with ⟨u0, u1, u2, u3, v0, v1, v2, v3⟩
  have cu := rho_swap01_coords (ofB8 (u0, u1, u2, u3, v0, v1, v2, v3)).1
  have cv := rhoDual_swap01_coords (ofB8 (u0, u1, u2, u3, v0, v1, v2, v3)).2
  apply Prod.ext
  · exact v4_ext cu.1.symm cu.2.1.symm cu.2.2.1.symm cu.2.2.2.symm
  · exact v4_ext cv.1.symm cv.2.1.symm cv.2.2.1.symm cv.2.2.2.symm

/-- Complete duplicate-free enumeration of `B8` (`2⁸ = 256` elements, depth 8). -/
def allB8 : List B8 :=
  [false, true].flatMap fun u0 =>
  [false, true].flatMap fun u1 =>
  [false, true].flatMap fun u2 =>
  [false, true].flatMap fun u3 =>
  [false, true].flatMap fun v0 =>
  [false, true].flatMap fun v1 =>
  [false, true].flatMap fun v2 =>
  [false, true].map fun v3 => (u0, u1, u2, u3, v0, v1, v2, v3)

/-- Boolean duplicate check (`O(n²)` pure `BEq`, zero `Decidable` coercion). -/
def noDupsB8 : List B8 → Bool
  | [] => true
  | x :: xs => !(xs.contains x) && noDupsB8 xs

/-- Expand a single `B8` seed for `k` generator rounds under `{bFive, bSwap}`. -/
def expandB8Step (xs : List B8) : List B8 :=
  let xs1 := xs.foldl (fun acc x => let y := bFive x; if acc.contains y then acc else y :: acc) xs
  xs.foldl (fun acc x => let y := bSwap x; if acc.contains y then acc else y :: acc) xs1

def bOrbitFrom : ℕ → List B8 → List B8
  | 0, xs => xs
  | k + 1, xs => bOrbitFrom k (expandB8Step xs)

def orbitClosedB8 (orb : List B8) : Bool :=
  orb.all fun x => orb.contains (bFive x) && orb.contains (bSwap x)

/-- Canonical representatives for the `10` even and `4` odd `S₅`-orbits on `B8`. -/
def evenSeeds : List B8 :=
  [ (false, false, false, false, false, false, false, false),
    (false, false, false, false, false, false, false, true),
    (false, true, true, true, false, false, false, false),
    (false, true, true, true, true, false, false, false),
    (false, false, false, false, false, false, true, true),
    (false, false, false, true, false, false, false, false),
    (false, false, false, true, true, true, true, false),
    (false, false, false, true, false, false, true, false),
    (false, false, false, true, false, true, true, false),
    (false, true, true, true, false, false, true, true) ]

def oddSeeds : List B8 :=
  [ (false, false, false, true, false, false, false, true),
    (false, true, true, true, false, false, false, true),
    (false, true, true, true, false, true, true, true),
    (false, false, false, true, false, false, true, true) ]

def evenOrbits : List (List B8) := evenSeeds.map fun s => bOrbitFrom 14 [s]
def oddOrbits : List (List B8) := oddSeeds.map fun s => bOrbitFrom 14 [s]

set_option maxRecDepth 8192 in
/-- **Exact Arf counts `136` even and `120` odd (`2³(2⁴ ± 1) = 136, 120`).** -/
theorem even_and_odd_counts_bdh :
    (allB8.filter fun b => !bArf b).length = 136 ∧
      (allB8.filter fun b => bArf b).length = 120 := by
  decide

set_option maxRecDepth 8192 in
/-- **Braden & Disney-Hogg (2024) Theorem 5.9 (`qou-2a2o`, `qou-9l0d`).**
The `10` generated orbits from `evenSeeds` have exact cardinalities
`[1, 5, 5, 5, 10, 10, 10, 30, 30, 30]` (sum `136`), each is duplicate-free, strictly even
(`bArf = false`), closed under `{bFive, bSwap}` (`S₅`), and all `136` elements across the `10`
orbits are pairwise distinct (partitioning all `136` even spin structures; refutes PR `#8150`'s
`1 + 15 + 60 + 60`). -/
theorem even_orbit_partition_bdh :
    evenOrbits.map List.length = [1, 5, 5, 5, 10, 10, 10, 30, 30, 30] ∧
      evenOrbits.all (fun orb => orb.all (fun b => !bArf b) && orbitClosedB8 orb) = true ∧
      noDupsB8 evenOrbits.flatten = true := by
  decide

set_option maxRecDepth 8192 in
/-- **Braden & Disney-Hogg (2024) Corollary 5.7 (`qou-9l0d`).**
The `4` generated orbits from `oddSeeds` have exact cardinalities `[20, 20, 20, 60]`
(sum `120`), each is duplicate-free, strictly odd (`bArf = true`), closed under `{bFive, bSwap}`
(`S₅`), and all `120` elements across the `4` orbits are pairwise distinct (partitioning all
`120` odd theta characteristics / tritangent planes; refutes PR `#8150`'s `60 + 60`). -/
theorem odd_orbit_partition_bdh :
    oddOrbits.map List.length = [20, 20, 20, 60] ∧
      oddOrbits.all (fun orb => orb.all bArf && orbitClosedB8 orb) = true ∧
      noDupsB8 oddOrbits.flatten = true := by
  decide

set_option maxRecDepth 8192 in
/-- **Braden & Disney-Hogg (2024) Footnote 29:** `bFive` has order `5` on `B8`, fixes **only**
the origin `(false, …, false)` among the `136` even characteristics (`136 = 1 + 27 × 5`), and
fixes **zero** of the `120` odd characteristics (`120 = 24 × 5`). -/
theorem fiveCycle_fixed_points_bdh :
    allB8.all (fun b => bFive (bFive (bFive (bFive (bFive b)))) == b) = true ∧
      ((allB8.filter fun b => !bArf b && (bFive b == b)) ==
        [(false, false, false, false, false, false, false, false)]) = true ∧
      ((allB8.filter fun b => bArf b && (bFive b == b)) == []) = true := by
  decide

end QOU.BringsSurface.ThetaSymplectic
