import HeckeTemperleyLieb.TLCupCapCorner

/-!
# The simples of the semisimplified Temperley–Lieb tower on every number of strands

Bean `hkmt`. `TLCupCapCorner` shows that, below `k + 1` strands, every simple idempotent of the
Temperley–Lieb algebra is equivalent to the vacuum or to some `p_m` with cups. This file extends
that to **every** number of strands, in the quotient by negligible morphisms.

## The quotient

A morphism `x ∈ TL_{n+1}` is **negligible** when `τ(x y) = 0` for every `y` (`Negl`). Since the
trace is cyclic the negligible elements form a two-sided ideal, so `x ∼ y ↔ x − y` negligible is a
ring congruence (`negCon`), and `Q n` is the quotient algebra. Its idempotents are the objects of
the semisimplified category supported on `n + 1` strands.

## The cup map on the quotient

`capEmb a = δ⁻¹ ι²(a) e_{n+1}` satisfies `τ(capEmb a) = δ⁻¹ ε τ(a)`, and every corner element
`E z E` is a `capEmb c`. Together these give `capEmb a` negligible `↔` `a` negligible
(`negl_capEmb_iff`), with no nondegeneracy hypothesis. So on the quotient `capEmb` is
injective, even where it may fail to be injective on `TL` itself.

## Completeness

`StdLt k N s` is the list of standard objects with labels below `k`: `p_m` for `m + 1 ≤ k`, the
vacuum `δ⁻¹ e_0` on two strands, and `capEmb` of a standard object two strands down.

* `simple_mvn_stdLt`: suppose `δε = 1`, `p_m` is defined for `m ≤ k`, the form is nondegenerate
  below `k + 1` strands, and `τ(p_k) = 0`. Then **every simple idempotent of `Q N`, for every
  `N`, is equivalent to the image of a standard object with labels below `k`**. Below `k + 1`
  strands this is `simple_mvn_std`. From `k + 1` strands up, `ι(p_k)` is negligible, so
  `1 ≡ ι(1 − p_k)` lies in the ideal of the `e_i`, hence of the top `e`. A simple idempotent
  there is equivalent to one of the corner, which is `capEmb` of the level two down.
* `stdLt_ne_zero`: no standard object with labels below `k` is negligible.
* `simple_mvn_stdLt_root`: at a primitive `2(k+2)`-th root of unity `ζ`, `δ = ζ + ζ⁻¹`, all
  hypotheses hold. So the simple objects of the semisimplified category on any number of strands
  are the vacuum and `p_0, …, p_{k−1}`, with cups, and none of these vanishes.

Not proved here: the rectangular hom spaces `Hom(m, n)` for `m ≠ n`. Moving between strand
numbers is again done through the cup–cap corner.

No empirical input; everything is over an arbitrary field.

-- Ref: [jones1983] Index for subfactors, §4 (the basic construction and `e x e = E(x) e`).
-- Ref: [leitner2026] the Temperley–Lieb chapter (bean `hkmt`).
-/

namespace QOU.HeckeTemperleyLieb.TLNegligible

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLCable QOU.HeckeTemperleyLieb.TLSemisimpleQuotient
open QOU.HeckeTemperleyLieb.TLCupCap

/-! ## Standard objects with labels below `k` -/

section Std

variable {K : Type*} [Field K] (δ : K)

/-- **The standard objects with labels below `k`** on `N + 1` strands. -/
inductive StdLt (k : ℕ) : (N : ℕ) → TLFin K δ N → Prop
  | jw (m : ℕ) (hm : m + 1 ≤ k) : StdLt k m (jw δ m)
  | vac : StdLt k 1 (δ⁻¹ • e K δ adjFin (Fin.last 0))
  | cap {n : ℕ} {s : TLFin K δ n} : StdLt k n s → StdLt k (n + 1 + 1) (capEmb δ n s)

/-- Below `k + 1` strands every standard object has labels below `k`. -/
theorem Std.toStdLt {k N : ℕ} {s : TLFin K δ N} (h : Std δ N s) (hN : N + 1 ≤ k) :
    StdLt δ k N s := by
  induction h with
  | jw N => exact StdLt.jw N hN
  | vac => exact StdLt.vac
  | cap _ ih => exact StdLt.cap (ih (by omega))

end Std

/-! ## The negligible congruence -/

section Quotient

variable {K : Type*} [Field K] {δ ε : K} (T : MarkovTower δ ε)

/-- `x` is negligible: `τ(x y) = 0` for every `y`. -/
def Negl (n : ℕ) (x : TLFin K δ n) : Prop := ∀ y, T.τ n (x * y) = 0

theorem negl_zero (n : ℕ) : Negl T n 0 := fun y => by simp

theorem negl_add {n : ℕ} {x y : TLFin K δ n} (hx : Negl T n x) (hy : Negl T n y) :
    Negl T n (x + y) := fun z => by rw [add_mul, map_add, hx, hy, add_zero]

theorem negl_neg {n : ℕ} {x : TLFin K δ n} (hx : Negl T n x) : Negl T n (-x) :=
  fun z => by rw [neg_mul, map_neg, hx, neg_zero]

theorem negl_mul_right {n : ℕ} {x : TLFin K δ n} (hx : Negl T n x) (a : TLFin K δ n) :
    Negl T n (x * a) := fun z => by rw [mul_assoc]; exact hx _

theorem negl_mul_left {n : ℕ} {x : TLFin K δ n} (hx : Negl T n x) (a : TLFin K δ n) :
    Negl T n (a * x) := fun z => by rw [mul_assoc, T.tr_comm, mul_assoc]; exact hx _

/-- **The negligible congruence** on level `n`. -/
def negCon (n : ℕ) : RingCon (TLFin K δ n) where
  r x y := Negl T n (x - y)
  iseqv :=
    { refl := fun x => by rw [sub_self]; exact negl_zero T n
      symm := fun {x y} h => by rw [← neg_sub]; exact negl_neg T h
      trans := fun {x y z} h1 h2 => by
        rw [← sub_add_sub_cancel x y z]; exact negl_add T h1 h2 }
  add' := fun {a b c d} h1 h2 => by
    rw [show a + c - (b + d) = (a - b) + (c - d) by abel]; exact negl_add T h1 h2
  mul' := fun {a b c d} h1 h2 => by
    rw [show a * c - b * d = (a - b) * c + b * (c - d) by noncomm_ring]
    exact negl_add T (negl_mul_right T h1 c) (negl_mul_left T h2 b)

/-- **The semisimplified algebra on `n + 1` strands.** -/
abbrev Q (n : ℕ) := (negCon T n).Quotient

theorem coe_eq_iff {n : ℕ} {x y : TLFin K δ n} :
    ((x : Q T n)) = (y : Q T n) ↔ Negl T n (x - y) := RingCon.eq _

theorem coe_eq_zero_iff {n : ℕ} {x : TLFin K δ n} : ((x : Q T n)) = 0 ↔ Negl T n x := by
  rw [← RingCon.coe_zero, coe_eq_iff, sub_zero]

theorem coe_surj {n : ℕ} (φ : Q T n) : ∃ x : TLFin K δ n, (x : Q T n) = φ := by
  obtain ⟨x, hx⟩ := Quot.exists_rep φ
  exact ⟨x, (RingCon.quot_mk_eq_coe _ x).symm.trans hx⟩

theorem coe_smul' {n : ℕ} (c : K) (x : TLFin K δ n) :
    ((c • x : TLFin K δ n) : Q T n) = c • (x : Q T n) := RingCon.coe_smul _ _ _

theorem coe_J {n : ℕ} {z x : TLFin K δ n} (hx : x ∈ J K z) :
    (x : Q T n) ∈ J K (z : Q T n) := by
  induction hx using Submodule.span_induction with
  | mem w hw =>
    obtain ⟨a, b, rfl⟩ := hw
    exact Submodule.subset_span ⟨a, b, by rw [RingCon.coe_mul, RingCon.coe_mul]⟩
  | zero => rw [RingCon.coe_zero]; exact Submodule.zero_mem _
  | add a b _ _ ha hb => rw [RingCon.coe_add]; exact Submodule.add_mem _ ha hb
  | smul r a _ ha => rw [coe_smul']; exact Submodule.smul_mem _ _ ha

theorem coe_mvn {n : ℕ} {f s : TLFin K δ n} (h : MvN f s) : MvN (f : Q T n) (s : Q T n) := by
  obtain ⟨hf, hs, a, b, ha, hb, hab, hba⟩ := h
  refine ⟨by rw [← RingCon.coe_mul, hf], by rw [← RingCon.coe_mul, hs], a, b, ?_, ?_, ?_, ?_⟩
  · rw [← RingCon.coe_mul, ← RingCon.coe_mul, ha]
  · rw [← RingCon.coe_mul, ← RingCon.coe_mul, hb]
  · rw [← RingCon.coe_mul, hab]
  · rw [← RingCon.coe_mul, hba]

/-- On a nondegenerate level the quotient changes nothing. -/
theorem coe_inj_of_nondegenerate {n : ℕ} (hnd : Nondegenerate T n) {x y : TLFin K δ n}
    (h : (x : Q T n) = (y : Q T n)) : x = y :=
  sub_eq_zero.mp (hnd _ ((coe_eq_iff T).mp h))

theorem capEmb_sub (n : ℕ) (a b : TLFin K δ n) :
    capEmb δ n (a - b) = capEmb δ n a - capEmb δ n b := by
  rw [sub_eq_add_neg, ← neg_one_smul K b, capEmb_add, capEmb_smul, neg_one_smul, ← sub_eq_add_neg]

/-- **`capEmb a` is negligible iff `a` is**, with no nondegeneracy hypothesis. -/
theorem negl_capEmb_iff (hε : δ * ε = 1) {n : ℕ} (a : TLFin K δ n) :
    Negl T (n + 1 + 1) (capEmb δ n a) ↔ Negl T n a := by
  have hδ : δ ≠ 0 := left_ne_zero_of_mul_eq_one hε
  have hε0 : ε ≠ 0 := right_ne_zero_of_mul_eq_one hε
  constructor
  · intro h y
    have h1 := tau_capEmb T n (a * y)
    rw [capEmb_mul δ hδ, h] at h1
    rcases mul_eq_zero.mp h1.symm with h2 | h2
    · exact absurd h2 (inv_ne_zero hδ)
    · exact (mul_eq_zero.mp h2).resolve_left hε0
  · intro h z
    have hE : capEmb δ n a = capEmb δ n 1 * capEmb δ n a * capEmb δ n 1 := by
      rw [← capEmb_mul δ hδ, ← capEmb_mul δ hδ, one_mul, mul_one]
    obtain ⟨c, hc⟩ := corner_surj δ n z
    rw [hE, show capEmb δ n 1 * capEmb δ n a * capEmb δ n 1 * z =
        capEmb δ n 1 * (capEmb δ n a * capEmb δ n 1 * z) by simp only [mul_assoc], T.tr_comm,
      show capEmb δ n a * capEmb δ n 1 * z * capEmb δ n 1 =
        capEmb δ n a * (capEmb δ n 1 * z * capEmb δ n 1) by simp only [mul_assoc], hc,
      ← capEmb_mul δ hδ, tau_capEmb, h, mul_zero, mul_zero]

theorem coe_capEmb_eq_iff (hε : δ * ε = 1) {n : ℕ} (a b : TLFin K δ n) :
    (capEmb δ n a : Q T (n + 1 + 1)) = (capEmb δ n b : Q T (n + 1 + 1)) ↔
      (a : Q T n) = (b : Q T n) := by
  rw [coe_eq_iff, coe_eq_iff, ← capEmb_sub, negl_capEmb_iff T hε]

theorem mvn_coe_capEmb (hε : δ * ε = 1) {n : ℕ} {f s : TLFin K δ n}
    (h : MvN (f : Q T n) (s : Q T n)) :
    MvN (capEmb δ n f : Q T (n + 1 + 1)) (capEmb δ n s : Q T (n + 1 + 1)) := by
  have hδ : δ ≠ 0 := left_ne_zero_of_mul_eq_one hε
  obtain ⟨hf, hs, a, b, ha, hb, hab, hba⟩ := h
  obtain ⟨a, rfl⟩ := coe_surj T a
  obtain ⟨b, rfl⟩ := coe_surj T b
  simp only [← RingCon.coe_mul] at hf hs ha hb hab hba
  rw [← coe_capEmb_eq_iff T hε] at hf hs ha hb hab hba
  simp only [capEmb_mul δ hδ, RingCon.coe_mul] at hf hs ha hb hab hba
  exact ⟨hf, hs, _, _, ha, hb, hab, hba⟩

/-- `ιᵐ` keeps an element in the ideal of the generators. -/
theorem inclIter_genIdeal (r m : ℕ) {u : TLFin K δ r} (hu : u ∈ genIdeal K δ adjFin) :
    inclIter (δ := δ) r m u ∈ genIdeal K δ adjFin := by
  induction m with
  | zero => exact hu
  | succ m ih => exact incl_genIdeal δ (r + m) ih

/-- From `k + 1` strands up, `1` is congruent to an element of the ideal of the generators. -/
theorem exists_unit_mod {k : ℕ} (hS : ∀ m ≤ k, JWSpec δ m) (htop : T.τ k (jw δ k) = 0)
    (N : ℕ) (hN : k ≤ N) :
    ∃ u : TLFin K δ N, u ∈ genIdeal K δ adjFin ∧ Negl T N (1 - u) := by
  obtain ⟨j, rfl⟩ := Nat.exists_eq_add_of_le hN
  refine ⟨inclIter (δ := δ) k j (1 - jw δ k), inclIter_genIdeal k j (hS k le_rfl).2.2.2.1, ?_⟩
  rw [map_sub, map_one, sub_sub_cancel]
  exact jw_negligible_up T (hS k le_rfl) htop j

/-- The vacuum on two strands is not negligible. -/
theorem vac_not_negl (hε : δ * ε = 1) :
    ¬ Negl T 1 (δ⁻¹ • e K δ adjFin (Fin.last 0)) := by
  have hδ : δ ≠ 0 := left_ne_zero_of_mul_eq_one hε
  have hε0 : ε ≠ 0 := right_ne_zero_of_mul_eq_one hε
  intro h
  have h1 := h 1
  have h2 := T.tr_markov 0 1
  rw [map_one, one_mul, T.tr_one, mul_one] at h2
  rw [mul_one, map_smul, h2, smul_eq_mul] at h1
  exact mul_ne_zero (inv_ne_zero hδ) hε0 h1

/-- **No standard object with labels below `k` is negligible.** -/
theorem stdLt_not_negl (hε : δ * ε = 1) {k : ℕ}
    (hτ : ∀ m, m + 1 ≤ k → JWSpec δ m ∧ T.τ m (jw δ m) ≠ 0)
    {N : ℕ} {s : TLFin K δ N} (hs : StdLt δ k N s) : ¬ Negl T N s := by
  induction hs with
  | jw m hm =>
    obtain ⟨hS, h0⟩ := hτ m hm
    exact fun h => h0 ((jw_negligible_iff T hS).mp h)
  | vac => exact vac_not_negl T hε
  | cap _ ih => rwa [negl_capEmb_iff T hε]

theorem stdLt_ne_zero (hε : δ * ε = 1) {k : ℕ}
    (hτ : ∀ m, m + 1 ≤ k → JWSpec δ m ∧ T.τ m (jw δ m) ≠ 0)
    {N : ℕ} {s : TLFin K δ N} (hs : StdLt δ k N s) : (s : Q T N) ≠ 0 := by
  rw [Ne, coe_eq_zero_iff]; exact stdLt_not_negl T hε hτ hs

/-- **Completeness of the simples in the semisimplified tower, on every number of strands.** -/
theorem simple_mvn_stdLt (hε : δ * ε = 1) (k : ℕ) (hS : ∀ m ≤ k, JWSpec δ m)
    (hnd : ∀ m, m + 1 ≤ k → Nondegenerate T m) (htop : T.τ k (jw δ k) = 0)
    (N : ℕ) (φ : Q T N) (hφ : IsSimpleIdem K φ) :
    ∃ s, StdLt δ k N s ∧ MvN φ (s : Q T N) := by
  have hδ : δ ≠ 0 := left_ne_zero_of_mul_eq_one hε
  induction N using Nat.strong_induction_on with
  | _ N ih =>
  by_cases hNk : N + 1 ≤ k
  · -- nondegenerate levels: no negligibles, use `simple_mvn_std`
    obtain ⟨f, rfl⟩ := coe_surj T φ
    have hndN := hnd N hNk
    have hf : IsSimpleIdem K f := by
      refine ⟨coe_inj_of_nondegenerate T hndN (by rw [RingCon.coe_mul, hφ.1]), ?_, fun x => ?_⟩
      · rintro rfl; exact hφ.2.1 (RingCon.coe_zero _)
      · obtain ⟨c, hc⟩ := hφ.2.2 (x : Q T N)
        refine ⟨c, coe_inj_of_nondegenerate T hndN ?_⟩
        rw [RingCon.coe_mul, RingCon.coe_mul, hc, coe_smul']
    obtain ⟨s, hs, hfs⟩ := simple_mvn_std T hε N (fun m hm => hS m (by omega))
      (fun m hm => hnd m (by omega)) f hf
    exact ⟨s, Std.toStdLt δ hs hNk, coe_mvn T hfs⟩
  · -- from `k + 1` strands up: `ι(p_k)` is negligible, so `1 ≡ ι(1 − p_k)`
    obtain ⟨u, hu, hnu⟩ := exists_unit_mod T hS htop N (by omega)
    have hφu : φ = φ * (u : Q T N) := by
      rw [← sub_eq_zero, ← mul_one φ, mul_assoc, one_mul, ← mul_sub, ← RingCon.coe_one,
        ← RingCon.coe_sub, (coe_eq_zero_iff T).mpr hnu, mul_zero]
    rcases N with _ | _ | n
    · -- one strand: `u = 0`, impossible
      exfalso; apply hφ.2.1
      have h1 : u = 0 := by
        rw [level_zero δ u, aug_eq_zero_of_mem_genIdeal hu, zero_smul]
      rw [hφu, h1, RingCon.coe_zero, mul_zero]
    · -- two strands: the vacuum
      have hE : (δ⁻¹ • e K δ adjFin (Fin.last 0)) * (δ⁻¹ • e K δ adjFin (Fin.last 0)) =
          δ⁻¹ • e K δ adjFin (Fin.last 0) := by
        rw [smul_mul_smul_comm, e_sq', smul_smul, mul_assoc, inv_mul_cancel₀ hδ, mul_one]
      have hJ : φ ∈ J K ((δ⁻¹ • e K δ adjFin (Fin.last 0) : TLFin K δ 1) : Q T 1) := by
        rw [hφu]
        exact J_mul_left _ _ (coe_J T (J_smul (inv_ne_zero hδ) (genIdeal_le_J δ 0 hu)))
      have hEQ : ((δ⁻¹ • e K δ adjFin (Fin.last 0) : TLFin K δ 1) : Q T 1) *
          ((δ⁻¹ • e K δ adjFin (Fin.last 0) : TLFin K δ 1) : Q T 1) =
          ((δ⁻¹ • e K δ adjFin (Fin.last 0) : TLFin K δ 1) : Q T 1) := by
        rw [← RingCon.coe_mul, hE]
      obtain ⟨g, hφg, hgE⟩ := exists_mvn_corner hφ hEQ hJ
      have hgs := IsSimpleIdem.of_mvn hφ hφg
      obtain ⟨z, rfl⟩ := coe_surj T g
      obtain ⟨c, hc⟩ := corner_one δ z
      have hg : (z : Q T 1) = (δ⁻¹ * c) •
          ((δ⁻¹ • e K δ adjFin (Fin.last 0) : TLFin K δ 1) : Q T 1) := by
        rw [← hgE, ← RingCon.coe_mul, ← RingCon.coe_mul, ← coe_smul', smul_mul_assoc,
          smul_mul_smul_comm, hc, smul_smul, smul_smul]
        congr 2; ring
      exact ⟨_, StdLt.vac, hφg.trans
        (eq_of_smul_idem hgs.1 hgs.2.1 hEQ hg ▸ MvN.refl hgs.1)⟩
    · -- `n + 3` strands: through the cup–cap corner
      have hJ : φ ∈ J K ((capEmb δ n 1 : TLFin K δ (n + 1 + 1)) : Q T (n + 1 + 1)) := by
        rw [hφu, capEmb_one]
        exact J_mul_left _ _ (coe_J T (J_smul (inv_ne_zero hδ) (genIdeal_le_J δ (n + 1) hu)))
      have hEQ : ((capEmb δ n 1 : TLFin K δ (n + 1 + 1)) : Q T (n + 1 + 1)) *
          ((capEmb δ n 1 : TLFin K δ (n + 1 + 1)) : Q T (n + 1 + 1)) =
          ((capEmb δ n 1 : TLFin K δ (n + 1 + 1)) : Q T (n + 1 + 1)) := by
        rw [← RingCon.coe_mul, capEmb_one_idem δ hδ]
      obtain ⟨g, hφg, hgE⟩ := exists_mvn_corner hφ hEQ hJ
      have hgs := IsSimpleIdem.of_mvn hφ hφg
      obtain ⟨z, rfl⟩ := coe_surj T g
      obtain ⟨h, hh⟩ := corner_surj δ n z
      have hgh : (z : Q T (n + 1 + 1)) = (capEmb δ n h : Q T (n + 1 + 1)) := by
        rw [← hgE, ← RingCon.coe_mul, ← RingCon.coe_mul, hh]
      have hhs : IsSimpleIdem K (h : Q T n) := by
        refine ⟨?_, ?_, fun x => ?_⟩
        · rw [← RingCon.coe_mul, ← coe_capEmb_eq_iff T hε, capEmb_mul δ hδ, RingCon.coe_mul,
            ← hgh, hgs.1]
        · intro h0
          apply hgs.2.1
          rw [hgh, ← RingCon.coe_zero, ← capEmb_zero δ n, coe_capEmb_eq_iff T hε,
            RingCon.coe_zero, h0]
        · obtain ⟨x, rfl⟩ := coe_surj T x
          obtain ⟨c, hc⟩ := hgs.2.2 (capEmb δ n x : Q T (n + 1 + 1))
          refine ⟨c, ?_⟩
          rw [← RingCon.coe_mul, ← RingCon.coe_mul, ← coe_smul', ← coe_capEmb_eq_iff T hε,
            capEmb_mul δ hδ, capEmb_mul δ hδ, capEmb_smul, RingCon.coe_mul, RingCon.coe_mul,
            coe_smul', ← hgh, hc]
      obtain ⟨s, hs, hhs'⟩ := ih n (by omega) _ hhs
      exact ⟨_, StdLt.cap hs, hφg.trans (hgh ▸ mvn_coe_capEmb T hε hhs')⟩

end Quotient

/-! ## At a root of unity -/

section RootOfUnity

variable {K : Type*} [Field K] {ζ : Kˣ} (k : ℕ) (hζ : IsPrimitiveRoot ζ (2 * (k + 2))) {ε : K}
  (T : MarkovTower ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) ε)
  (hε : ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) * ε = 1)
include hζ hε

/-- **The simple objects of the semisimplified Temperley–Lieb category at a root of unity.**
At a primitive `2(k+2)`-th root `ζ`, `δ = ζ + ζ⁻¹`, every simple idempotent of the quotient
by negligibles on any number of strands is equivalent to the vacuum or to some `p_m` with
`m < k`, with cups; and none of these standard objects is negligible. -/
theorem simple_mvn_stdLt_root (N : ℕ)
    (φ : Q T N) (hφ : IsSimpleIdem K φ) :
    ∃ s, StdLt ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) k N s ∧ MvN φ (s : Q T N) ∧ (s : Q T N) ≠ 0 := by
  obtain ⟨s, hs, hφs⟩ := simple_mvn_stdLt T hε k (fun m hm => jwSpec_root k hζ hm)
    (fun m hm => nondegenerate_root k hζ T hε hm) (tau_jw_top k hζ T hε) N φ hφ
  exact ⟨s, hs, hφs, stdLt_ne_zero T hε
    (fun m hm => ⟨jwSpec_root k hζ (by omega), tau_jw_ne_zero k hζ T hε hm⟩) hs⟩

end RootOfUnity

end QOU.HeckeTemperleyLieb.TLNegligible
