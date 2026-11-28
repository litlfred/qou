import HeckeTemperleyLieb.TLQuotientTensor
import HeckeTemperleyLieb.TLCableBraiding

/-!
# The braiding and the balancing twist on the semisimplified Temperley–Lieb quotient

Bean `hkmt`. `TLCableBraiding` builds the cable crossing and the twist inside one
Temperley–Lieb algebra. `TLQuotientTensor` builds the tensor product `tensQ` on the quotient `Q`
by negligible morphisms. This file connects the two.

* `tens_eq_pl`: the tensor product `x ⊗ y` is `x` placed on the first block times `y` placed on
  the second.
* `cross`, `crossInv`: the cable crossing `c_{n,m}` of `n + 1` strands past `m + 1` strands, and
  its inverse.
* `cross_mul_tens`: **naturality**, `c_{n,m} · (x ⊗ y) = (y ⊗ x) · c_{n,m}` (after reindexing
  `m + n + 1 = n + m + 1`). `crossQ_mul_tensQ`: the same on the quotient.
* `twist n = (A³)^{n+1} · Θ_n`: the framed full twist. `twistQ_comm`: it is **central** in every
  `Q n`, so it is natural on every endomorphism. `twist_balance`, `twistQ_balance`: the
  **balancing identity** `θ_{n+m+1} = (θ_n ⊗ θ_m) · c_{m,n} · c_{n,m}`.
* `twist_capEmb`, `twistQ_capQ`: **ribbon compatibility**, the twist commutes with the cup map
  `x ↦ δ⁻¹ ι²(x) e_{n+1}`; the framing `A³` per strand is exactly what makes this hold.
* `jw_mul_twist`: on the simple `p_n` the twist is the scalar `(A³)^{n+1} A^{n(n+1)}`, which at
  `A = ω` is `ω⁻¹ T_{n+1,n+1}` (`TLPositiveLoop.twist_eq_tMatrix`): the same `T`-matrix as the
  modular data of `TLQuotientModularData`.

Not proved here: these maps assembled into Mathlib's `BraidedCategory` and
`QOU.MathlibExt.BalancedCategory` on one category containing every strand count; that needs the
`MonoidalCategory` structure on the glued category.

No empirical input; everything is over an arbitrary field with `A ≠ 0`, `δ = A² + A⁻²`.

-- Ref: [kassel1995] Kassel, *Quantum groups*, XIII.1 and XIV.3.
-- Ref: [leitner2026] the Temperley–Lieb chapter (bean `hkmt`).
-/

namespace QOU.HeckeTemperleyLieb.TLQuotientBraiding

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLPositiveLoop QOU.HeckeTemperleyLieb.TLCable
open QOU.HeckeTemperleyLieb.TLSemisimpleQuotient QOU.HeckeTemperleyLieb.TLNegligible
open QOU.HeckeTemperleyLieb.TLQuotientTensor QOU.HeckeTemperleyLieb.TLCableBraiding
open QOU.HeckeTemperleyLieb.TLCupCap

variable {K : Type*} [Field K] {δ A : K}

/-! ## The tensor product as two placements -/

section Placement

theorem inclIter_eq_pl (n m : ℕ) :
    inclIter (δ := δ) n (m + 1) = pl δ 0 n (by omega) (N := n + (m + 1)) := by
  refine hom_ext _ _ _ _ _ (fun i => ?_)
  rw [inclIter_e, pl_e, E_of_lt (by omega)]
  congr 1; ext; simp

theorem sh_eq_pl (n m : ℕ) : sh δ n m = pl δ (n + 1) m (by omega) (N := n + m + 1) := by
  refine hom_ext _ _ _ _ _ (fun i => ?_)
  rw [sh_e, pl_e, E_of_lt (by omega)]

theorem tens_eq_pl {n m : ℕ} (x : TLFin K δ n) (y : TLFin K δ m) :
    tens δ x y = pl δ 0 n (by omega) x * pl δ (n + 1) m (by omega) y := by
  rw [tens, sh_eq_pl, inclIter_eq_pl]

theorem recast_C {N N' : ℕ} (h : N = N') (s n m : ℕ) :
    recast δ h (C δ A N s n m) = C δ A N' s n m := by
  subst h; rfl

theorem pl_Θ {N : ℕ} (t M : ℕ) (h : t + M ≤ N) (n a : ℕ) (hn : a + n ≤ M) :
    pl δ t M h (Θ δ A M a n) = Θ δ A N (t + a) n := by
  rw [Θ, map_mul, pl_D t M h n a hn, Θ]

theorem recast_pl {N N' : ℕ} (h : N = N') (t M : ℕ) (hM : t + M ≤ N) (x : TLFin K δ M) :
    recast δ h (pl δ t M hM x) = pl δ t M (by omega) x := by
  subst h; rfl

/-- Elements placed on disjoint blocks commute. -/
theorem pl_commute {N : ℕ} (t M u P : ℕ) (hM : t + M ≤ N) (hP : u + P ≤ N) (h : t + M + 1 ≤ u)
    (x : TLFin K δ M) (y : TLFin K δ P) : Commute (pl δ t M hM x) (pl δ u P hP y) := by
  refine commute_of_gens _ _ (fun i => ?_) x
  refine (commute_of_gens _ _ (fun j => ?_) y).symm
  rw [pl_e, pl_e]
  exact E_comm_E (by have := i.isLt; omega)

end Placement

/-! ## The cable crossing on tensor products -/

section Crossing

variable (δ A) in
/-- The cable crossing `c_{n,m}` of `n + 1` strands past `m + 1` strands. -/
noncomputable def cross (n m : ℕ) : TLFin K δ (n + m + 1) := C δ A (n + m + 1) 0 n m

variable (δ A) in
/-- Its inverse. -/
noncomputable def crossInv (n m : ℕ) : TLFin K δ (n + m + 1) := Ci δ A (n + m + 1) 0 n m

variable (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2)

include hA hδ in
theorem cross_mul_inv (n m : ℕ) : cross δ A n m * crossInv δ A n m = 1 :=
  C_mul_Ci hA hδ 0 n m

include hA hδ in
theorem inv_mul_cross (n m : ℕ) : crossInv δ A n m * cross δ A n m = 1 :=
  Ci_mul_C hA hδ 0 n m

include hA hδ in
/-- **Naturality of the braiding**: `c_{n,m} · (x ⊗ y) = (y ⊗ x) · c_{n,m}`. -/
theorem cross_mul_tens {n m : ℕ} (x : TLFin K δ n) (y : TLFin K δ m) :
    cross δ A n m * tens δ x y =
      recast δ (by omega) (tens δ y x) * cross δ A n m := by
  have hl := C_mul_pl_left (N := n + m + 1) hA hδ 0 n m (by omega) x
  have hr := C_mul_pl_right (N := n + m + 1) hA hδ 0 n m (by omega) y
  simp only [Nat.zero_add] at hl hr
  rw [tens_eq_pl, tens_eq_pl, map_mul, recast_pl, recast_pl, cross, ← mul_assoc, hl,
    mul_assoc, hr, ← mul_assoc]
  congr 1
  exact (pl_commute 0 m (m + 1) n _ _ (by omega) y x).symm.eq

variable {ε : K} (T : MarkovTower δ ε)

variable (A) in
/-- The cable crossing in the quotient. -/
noncomputable def crossQ (n m : ℕ) : Q T (n + m + 1) := (cross δ A n m : Q T (n + m + 1))

variable (A) in
/-- Its inverse in the quotient. -/
noncomputable def crossInvQ (n m : ℕ) : Q T (n + m + 1) := (crossInv δ A n m : Q T (n + m + 1))

include hA hδ in
theorem crossQ_mul_inv (n m : ℕ) : crossQ A T n m * crossInvQ A T n m = 1 := by
  rw [crossQ, crossInvQ, ← RingCon.coe_mul, cross_mul_inv hA hδ, RingCon.coe_one]

include hA hδ in
theorem inv_mul_crossQ (n m : ℕ) : crossInvQ A T n m * crossQ A T n m = 1 := by
  rw [crossQ, crossInvQ, ← RingCon.coe_mul, inv_mul_cross hA hδ, RingCon.coe_one]

include hA hδ in
/-- **Naturality of the braiding on the quotient.** -/
theorem crossQ_mul_tensQ {n m : ℕ} (φ : Q T n) (ψ : Q T m) :
    crossQ A T n m * tensQ T φ ψ = recastQ T (by omega) (tensQ T ψ φ) * crossQ A T n m := by
  obtain ⟨x, rfl⟩ := coe_surj T φ
  obtain ⟨y, rfl⟩ := coe_surj T ψ
  rw [tensQ_coe, tensQ_coe, recastQ_coe, crossQ, ← RingCon.coe_mul, ← RingCon.coe_mul,
    cross_mul_tens hA hδ]

end Crossing

/-! ## The balancing twist -/

section Twist

variable (δ A) in
/-- **The framed full twist** on `n + 1` strands: `θ_n = (A³)^{n+1} · Θ_n`, where `A³` is the
framing factor of one strand (`TLPositiveLoop.markov_curl`). -/
noncomputable def twist (n : ℕ) : TLFin K δ n := (A ^ 3) ^ (n + 1) • Θ δ A n 0 n

variable (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2)

include hA hδ in
/-- The twist is central in `TL_{n+1}`. -/
theorem twist_comm (n : ℕ) (x : TLFin K δ n) : Commute (twist δ A n) x := by
  refine (commute_of_gens (AlgHom.id K _) _ (fun i => ?_) x).symm
  have := Θ_mul_E (N := n) hA hδ n 0 i.isLt (by omega)
  rw [Nat.zero_add, E_of_lt i.isLt] at this
  exact ((Commute.smul_right this.symm _))

include hA hδ in
/-- **The balancing identity**: `θ_{n+m+1} = (θ_n ⊗ θ_m) · c_{m,n} · c_{n,m}`. -/
theorem twist_balance (n m : ℕ) :
    twist δ A (n + m + 1) =
      tens δ (twist δ A n) (twist δ A m) * recast δ (by omega) (cross δ A m n) * cross δ A n m := by
  have hb := Θ_balance (N := n + m + 1) hA hδ 0 n m (by omega)
  simp only [Nat.zero_add] at hb
  rw [twist, twist, twist, tens_smul_left, tens_smul_right, smul_smul, tens_eq_pl,
    pl_Θ 0 n _ n 0 (by omega), pl_Θ (n + 1) m _ m 0 (by omega), cross, cross, recast_C,
    smul_mul_assoc, smul_mul_assoc, ← pow_add, show n + 1 + (m + 1) = n + m + 1 + 1 by omega, hb]

variable {ε : K} (T : MarkovTower δ ε)

variable (A) in
/-- The twist in the quotient. -/
noncomputable def twistQ (n : ℕ) : Q T n := (twist δ A n : Q T n)

include hA hδ in
/-- **The twist is central in every quotient**, hence natural on every endomorphism. -/
theorem twistQ_comm (n : ℕ) (φ : Q T n) : twistQ A T n * φ = φ * twistQ A T n := by
  obtain ⟨x, rfl⟩ := coe_surj T φ
  rw [twistQ, ← RingCon.coe_mul, ← RingCon.coe_mul, (twist_comm hA hδ n x).eq]

include hA hδ in
/-- **The balancing identity on the quotient.** -/
theorem twistQ_balance (n m : ℕ) :
    twistQ A T (n + m + 1) =
      tensQ T (twistQ A T n) (twistQ A T m) * recastQ T (by omega) (crossQ A T m n) *
        crossQ A T n m := by
  rw [twistQ, twistQ, twistQ, tensQ_coe, crossQ, crossQ, recastQ_coe, ← RingCon.coe_mul,
    ← RingCon.coe_mul, twist_balance hA hδ]

/-- **The twist on the simple `p_n`** is the scalar `(A³)^{n+1} A^{n(n+1)}`. -/
theorem jw_mul_twist {n : ℕ} (hS : JWSpec δ n) :
    jw δ n * twist δ A n = ((A ^ 3) ^ (n + 1) * A ^ (n * (n + 1))) • jw δ n := by
  rw [twist, mul_smul_comm, jw_mul_Θ hS, smul_smul]

/-- **Matching the modular `T`-matrix**: at `A = ω`, the twist on `p_n` is
`ω⁻¹ · T_{n+1,n+1}` (`TLRootOfUnity.thetaW`). -/
theorem jw_mul_twist_eq_tMatrix (ω : Kˣ) {n : ℕ} (hS : JWSpec δ n) :
    (ω : K) * (((ω : K) ^ 3) ^ (n + 1) * (ω : K) ^ (n * (n + 1))) =
      TLRootOfUnity.thetaW ω (n + 1 + 1) ∧
    jw δ n * twist δ (ω : K) n = (((ω : K) ^ 3) ^ (n + 1) * (ω : K) ^ (n * (n + 1))) • jw δ n :=
  ⟨by rw [mul_comm]; exact twist_eq_tMatrix ω n, jw_mul_twist hS⟩

end Twist

/-! ## Ribbon compatibility: the twist commutes with the cup map -/

section Ribbon

variable (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2)

theorem incl_incl_eq_pl (n : ℕ) (x : TLFin K δ n) :
    incl δ (n + 1) (incl δ n x) = pl δ 0 n (by omega) (N := n + 1 + 1) x := by
  have : (incl δ (n + 1)).comp (incl δ n) = pl δ 0 n (by omega) (N := n + 1 + 1) :=
    hom_ext _ _ _ _ _ (fun i => by
      simp only [AlgHom.comp_apply, incl_e, pl_e]
      rw [E_of_lt (by omega)]; congr 1; ext; simp)
  exact AlgHom.congr_fun this x

include hA hδ in
/-- **The twist commutes with the cup map**: `θ_{n+2} · cup(x) = cup(θ_n · x)`. Adding a
cup–cap pair of strands does not change the twist: the framing `A³` per strand cancels the curl
`σ² e = A⁻⁶ e` of the new pair, and the winding of the old strands around the cap is trivial
(`wind_mul_E`). -/
theorem twist_capEmb (n : ℕ) (x : TLFin K δ n) :
    twist δ A (n + 1 + 1) * capEmb δ n x = capEmb δ n (twist δ A n * x) := by
  have hb := Θ_balance (N := n + 1 + 1) hA hδ 0 n 1 (by omega)
  simp only [Nat.zero_add] at hb
  have hw := wind_mul_E (N := n + 1 + 1) hA hδ 0 n (by omega)
  simp only [Nat.zero_add] at hw
  have hl := C_mul_pl_left (N := n + 1 + 1) hA hδ 0 n 1 (by omega) x
  have hr := C_mul_pl_right (N := n + 1 + 1) hA hδ 0 1 n (by omega) x
  simp only [Nat.zero_add] at hl hr
  have hX : Θ δ A (n + 1 + 1) (n + 1) 1 = X δ A _ (n + 1) * X δ A _ (n + 1) := by
    simp [Θ, D, C, H]
  set P := pl δ 0 n (by omega) (N := n + 1 + 1) x
  set ee := E δ (n + 1 + 1) (n + 1)
  set Xn := X δ A (n + 1 + 1) (n + 1)
  have hXc : Commute Xn P :=
    (commute_of_gens _ _ (fun i => by
      rw [pl_e]
      exact (X_comm_E (δ := δ) (A := A) (N := n + 1 + 1) (i := n + 1) (j := 0 + i)
        (by have := i.isLt; omega)).symm) x).symm
  have hcurl : Xn * (Xn * ee) = (A⁻¹ ^ 3) ^ 2 • ee := by
    rw [X_mul_E_self hA hδ (by omega), mul_smul_comm, X_mul_E_self hA hδ (by omega), smul_smul]
    congr 1; ring
  have hlast : (e K δ adjFin (Fin.last (n + 1)) : TLFin K δ (n + 1 + 1)) = ee :=
    (E_of_lt (by omega : n + 1 < n + 1 + 1)).symm
  have key : Θ δ A (n + 1 + 1) 0 (n + 1 + 1) * (P * ee) =
      (A⁻¹ ^ 3) ^ 2 • (Θ δ A (n + 1 + 1) 0 n * (P * ee)) := by
    rw [hb, hX]
    calc Θ δ A (n + 1 + 1) 0 n * (Xn * Xn) * C δ A (n + 1 + 1) 0 1 n *
          C δ A (n + 1 + 1) 0 n 1 * (P * ee)
        = Θ δ A (n + 1 + 1) 0 n * (Xn * Xn) * (C δ A (n + 1 + 1) 0 1 n *
            (C δ A (n + 1 + 1) 0 n 1 * P)) * ee := by simp only [mul_assoc]
      _ = Θ δ A (n + 1 + 1) 0 n * (Xn * Xn) * P *
            (C δ A (n + 1 + 1) 0 1 n * C δ A (n + 1 + 1) 0 n 1 * ee) := by
          rw [hl]; simp only [mul_assoc]; rw [← mul_assoc (C δ A (n + 1 + 1) 0 1 n), hr]
          simp only [mul_assoc]
      _ = Θ δ A (n + 1 + 1) 0 n * (P * (Xn * (Xn * ee))) := by
          have h3 : Xn * (Xn * (P * ee)) = P * (Xn * (Xn * ee)) := by
            rw [← mul_assoc Xn P, hXc.eq, mul_assoc, ← mul_assoc Xn P, hXc.eq, mul_assoc]
          rw [hw]; simp only [mul_assoc]; rw [h3]
      _ = _ := by rw [hcurl, mul_smul_comm, mul_smul_comm]
  unfold capEmb
  rw [incl_incl_eq_pl, incl_incl_eq_pl, hlast, twist, twist, smul_mul_assoc, map_mul, map_smul,
    pl_Θ 0 n _ n 0 (by omega), mul_smul_comm, key]
  simp only [Nat.add_zero, smul_mul_assoc, smul_smul, mul_assoc]
  congr 1
  field_simp
  ring

variable {ε : K} (T : MarkovTower δ ε) (hε : δ * ε = 1)

include hA hδ in
/-- **Ribbon compatibility on the quotient**: `θ_{n+2} · cup(φ) = cup(θ_n · φ)`, so the twists of
all strand counts are compatible with the stabilisation `stab` of `TLRectangularHom`. -/
theorem twistQ_capQ (n : ℕ) (φ : Q T n) :
    twistQ A T (n + 1 + 1) * TLRectHom.capQ T hε n φ =
      TLRectHom.capQ T hε n (twistQ A T n * φ) := by
  obtain ⟨x, rfl⟩ := coe_surj T φ
  rw [twistQ, twistQ, TLRectHom.capQ_coe, ← RingCon.coe_mul, ← RingCon.coe_mul,
    TLRectHom.capQ_coe, twist_capEmb hA hδ]

end Ribbon

end QOU.HeckeTemperleyLieb.TLQuotientBraiding
