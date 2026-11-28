import HeckeTemperleyLieb.TLQuotientModularData

/-!
# The tensor product on the semisimplified Temperley–Lieb quotient

Bean `hkmt`. Side by side placement `x ⊗ y` of a diagram on `n + 1` strands next to one on
`m + 1` strands gives a diagram on `n + m + 2` strands. This file shows that this tensor product
descends to the quotient `Q N` by negligible morphisms.

* `rev`: the left–right mirror of `TL_{n+1}`, `e_i ↦ e_{n-1-i}`. It is an involutive algebra map.
* `tau_rev`: **the Markov trace is mirror invariant.** This is the left Markov property, derived
  from the right one (no extra hypothesis on the tower).
* `negl_rev`, `negl_sh`: negligibility is preserved by the mirror and by adding strands on the
  left; `negl_inclIter` by adding strands on the right.
* `tens`, `negl_tens_left`, `negl_tens_right`: the negligible morphisms form a **tensor ideal**.
* `tensQ`: the tensor product on the quotient, bilinear, multiplicative and unital.
* `tau_tens`, `tauQ_tensQ`: **the trace is multiplicative**, `τ(x ⊗ y) = τ(x) τ(y)`.
* `tens_assoc`, `tensQ_assoc`: associativity, up to reindexing the strand count.

Not proved here: these maps assembled into a Mathlib `MonoidalCategory` on one category
containing every strand count, and a braiding natural in both factors.

No empirical input; everything is over an arbitrary field.

-- Ref: [jones1983] Index for subfactors, §4.
-- Ref: [leitner2026] the Temperley–Lieb chapter (bean `hkmt`).
-/

namespace QOU.HeckeTemperleyLieb.TLQuotientTensor

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLCable QOU.HeckeTemperleyLieb.TLSemisimpleQuotient
open QOU.HeckeTemperleyLieb.TLCupCap QOU.HeckeTemperleyLieb.TLNegligible
open QOU.HeckeTemperleyLieb.TLQuotientModular

variable {K : Type*} [Field K] {δ ε : K}

/-! ## The mirror and the left shift -/

section Mirror

variable (δ) in
/-- The mirror `e_i ↦ e_{n-1-i}` of `TL_{n+1}`. -/
noncomputable def rev (n : ℕ) : TLFin K δ n →ₐ[K] TLFin K δ n :=
  lift K δ adjFin (fun i => e K δ adjFin (Fin.rev i))
    (fun _ => e_sq _)
    (fun i j h => e_adjacent (by simp only [adjFin, Fin.val_rev] at h ⊢; omega))
    (fun i j h => e_farCommute (by simp only [adjFin, Fin.val_rev] at h ⊢; omega))

@[simp] theorem rev_e (n : ℕ) (i : Fin n) : rev δ n (e K δ adjFin i) = e K δ adjFin (Fin.rev i) :=
  lift_e _ _ _ _ _ _ _ i

theorem rev_rev (n : ℕ) (x : TLFin K δ n) : rev δ n (rev δ n x) = x := by
  have : (rev δ n).comp (rev δ n) = AlgHom.id K _ :=
    hom_ext _ _ _ _ _ (fun i => by simp)
  exact AlgHom.congr_fun this x

variable (δ) in
/-- One new strand on the left, `e_i ↦ e_{i+1}`. -/
noncomputable def sh1 (n : ℕ) : TLFin K δ n →ₐ[K] TLFin K δ (n + 1) :=
  lift K δ adjFin (fun i => e K δ adjFin (Fin.succ i))
    (fun _ => e_sq _)
    (fun i j h => e_adjacent (by simp only [adjFin, Fin.val_succ] at h ⊢; omega))
    (fun i j h => e_farCommute (by simp only [adjFin, Fin.val_succ] at h ⊢; omega))

@[simp] theorem sh1_e (n : ℕ) (i : Fin n) : sh1 δ n (e K δ adjFin i) = e K δ adjFin (Fin.succ i) :=
  lift_e _ _ _ _ _ _ _ i

theorem sh1_incl (n : ℕ) (x : TLFin K δ n) :
    sh1 δ (n + 1) (incl δ n x) = incl δ (n + 1) (sh1 δ n x) := by
  have : (sh1 δ (n + 1)).comp (incl δ n) = (incl δ (n + 1)).comp (sh1 δ n) :=
    hom_ext _ _ _ _ _ (fun i => by
      simp only [AlgHom.comp_apply, incl_e, sh1_e]; congr 1)
  exact AlgHom.congr_fun this x

theorem sh1_last (n : ℕ) :
    sh1 δ (n + 1) (e K δ adjFin (Fin.last n)) = e K δ adjFin (Fin.last (n + 1)) := by
  rw [sh1_e]; rfl

theorem rev_incl (n : ℕ) (x : TLFin K δ n) :
    rev δ (n + 1) (incl δ n x) = sh1 δ n (rev δ n x) := by
  have : (rev δ (n + 1)).comp (incl δ n) = (sh1 δ n).comp (rev δ n) :=
    hom_ext _ _ _ _ _ (fun i => by
      simp only [AlgHom.comp_apply, incl_e, rev_e, sh1_e]; congr 1; ext; simp; omega)
  exact AlgHom.congr_fun this x

theorem rev_last (n : ℕ) : rev δ (n + 1) (e K δ adjFin (Fin.last n)) = e K δ adjFin 0 := by
  rw [rev_e]; congr 1; ext; simp

theorem sh1_eq (n : ℕ) (x : TLFin K δ n) :
    sh1 δ n x = rev δ (n + 1) (incl δ n (rev δ n x)) := by
  rw [rev_incl, rev_rev]

end Mirror

/-! ## The left Markov property and mirror invariance -/

section LeftMarkov

variable (T : MarkovTower δ ε)

theorem incl_zero_e : (incl δ (0 + 1) (e K δ adjFin (0 : Fin 1)) : TLFin K δ 2) =
    e K δ adjFin 0 := by rw [incl_e]; rfl

/-- Both left properties at once: `τ(sh₁ w) = τ(w)` and `τ(sh₁ w · e_0) = ε τ(w)`. -/
theorem tau_sh1 : ∀ (n : ℕ) (w : TLFin K δ n),
    T.τ (n + 1) (sh1 δ n w) = T.τ n w ∧
      T.τ (n + 1) (sh1 δ n w * e K δ adjFin 0) = ε * T.τ n w
  | 0, w => by
    rw [level_zero δ w]
    simp only [map_smul, map_one, smul_mul_assoc, one_mul]
    refine ⟨?_, ?_⟩
    · rw [← map_one (incl δ 0), T.tr_incl]
    · have := T.tr_markov 0 1
      rw [map_one, one_mul] at this
      rw [show (0 : Fin 1) = Fin.last 0 from rfl, this, mul_smul_comm]
  | n + 1, w => by
    have IH := tau_sh1 n
    have hw : w ∈ LinearMap.range (incl δ n).toLinearMap ⊔ JJ δ n := by
      rw [sup_eq_top δ _ (hProp δ _)]; exact Submodule.mem_top
    obtain ⟨y, hy', z, hz, rfl⟩ := Submodule.mem_sup.mp hw
    obtain ⟨c, rfl⟩ := hy'
    clear hw
    simp only [AlgHom.toLinearMap_apply]
    have he0 : (e K δ adjFin (0 : Fin (n + 1 + 1)) : TLFin K δ (n + 1 + 1)) =
        incl δ (n + 1) (e K δ adjFin (0 : Fin (n + 1))) := by rw [incl_e]; rfl
    have hc : T.τ (n + 1 + 1) (sh1 δ (n + 1) (incl δ n c)) = T.τ (n + 1) (incl δ n c) ∧
        T.τ (n + 1 + 1) (sh1 δ (n + 1) (incl δ n c) * e K δ adjFin 0) =
          ε * T.τ (n + 1) (incl δ n c) := by
      rw [sh1_incl, T.tr_incl, T.tr_incl, he0, ← map_mul, T.tr_incl]
      exact IH c
    have hz' : T.τ (n + 1 + 1) (sh1 δ (n + 1) z) = T.τ (n + 1) z ∧
        T.τ (n + 1 + 1) (sh1 δ (n + 1) z * e K δ adjFin 0) = ε * T.τ (n + 1) z := by
      induction hz using Submodule.span_induction with
      | mem u hu =>
        obtain ⟨a, b, rfl⟩ := hu
        have hL : T.τ (n + 1) (incl δ n a * e K δ adjFin (Fin.last n) * incl δ n b) =
            ε * T.τ n (b * a) := by
          rw [T.tr_comm, ← mul_assoc, ← map_mul, T.tr_markov]
        simp only [map_mul, sh1_incl, sh1_last]
        refine ⟨?_, ?_⟩
        · rw [T.tr_comm, ← mul_assoc, ← map_mul, T.tr_markov, hL, ← map_mul, (IH (b * a)).1]
        · rw [he0, mul_assoc, ← map_mul, T.tr_comm, ← mul_assoc, ← map_mul, T.tr_markov, hL,
            T.tr_comm, ← mul_assoc, ← map_mul, (IH (a * b)).2, T.tr_comm n a b]
      | zero => simp [mul_zero]
      | add a b _ _ ha hb =>
        simp only [map_add, add_mul, ha.1, hb.1, ha.2, hb.2, mul_add, and_self]
      | smul r a _ ha =>
        simp only [map_smul, smul_mul_assoc, ha.1, ha.2, smul_eq_mul, mul_left_comm, and_self]
    simp only [map_add, add_mul, hc.1, hc.2, hz'.1, hz'.2, mul_add, and_self]

/-- **The Markov trace is mirror invariant.** -/
theorem tau_rev : ∀ (n : ℕ) (w : TLFin K δ n), T.τ n (rev δ n w) = T.τ n w
  | 0, w => by
    rw [level_zero δ w]; simp only [map_smul, map_one]
  | n + 1, w => by
    have IH := tau_rev n
    have hw : w ∈ LinearMap.range (incl δ n).toLinearMap ⊔ JJ δ n := by
      rw [sup_eq_top δ _ (hProp δ _)]; exact Submodule.mem_top
    obtain ⟨y, hy', z, hz, rfl⟩ := Submodule.mem_sup.mp hw
    obtain ⟨c, rfl⟩ := hy'
    clear hw
    simp only [AlgHom.toLinearMap_apply, map_add]
    congr 1
    · rw [rev_incl, (tau_sh1 T n _).1, IH, T.tr_incl]
    · induction hz using Submodule.span_induction with
      | mem u hu =>
        obtain ⟨a, b, rfl⟩ := hu
        simp only [map_mul, rev_incl, rev_last]
        rw [T.tr_comm, ← mul_assoc, ← map_mul, (tau_sh1 T n _).2, ← map_mul, IH,
          T.tr_comm (n + 1) (incl δ n a * _), ← mul_assoc, ← map_mul, T.tr_markov, T.tr_comm n b a]
      | zero => simp
      | add a b _ _ ha hb => rw [map_add, map_add, ha, hb, map_add]
      | smul r a _ ha => rw [map_smul, map_smul, ha, map_smul]

theorem negl_rev {n : ℕ} {x : TLFin K δ n} (h : Negl T n x) : Negl T n (rev δ n x) := fun y => by
  rw [← rev_rev n y, ← map_mul, tau_rev]; exact h _

theorem negl_incl {n : ℕ} {x : TLFin K δ n} (h : Negl T n x) : Negl T (n + 1) (incl δ n x) := by
  intro y
  have hy : y ∈ LinearMap.range (incl δ n).toLinearMap ⊔ JJ δ n := by
    rw [sup_eq_top δ _ (hProp δ _)]; exact Submodule.mem_top
  obtain ⟨y, hy', z, hz, rfl⟩ := Submodule.mem_sup.mp hy
  obtain ⟨c, rfl⟩ := hy'
  clear hy
  simp only [AlgHom.toLinearMap_apply]
  rw [mul_add, map_add, ← map_mul, T.tr_incl, h c, zero_add]
  induction hz using Submodule.span_induction with
  | mem w hw =>
    obtain ⟨a, b, rfl⟩ := hw
    rw [← mul_assoc, ← mul_assoc, ← map_mul, T.tr_comm, ← mul_assoc, ← map_mul,
      T.tr_markov, T.tr_comm, mul_assoc, h, mul_zero]
  | zero => rw [mul_zero, map_zero]
  | add a b _ _ ha hb => rw [mul_add, map_add, ha, hb, add_zero]
  | smul r' a _ ha => rw [mul_smul_comm, map_smul, ha, smul_zero]

theorem negl_sh1 {n : ℕ} {x : TLFin K δ n} (h : Negl T n x) : Negl T (n + 1) (sh1 δ n x) := by
  rw [sh1_eq]; exact negl_rev T (negl_incl T (negl_rev T h))

end LeftMarkov

/-! ## Reindexing and the left shift by several strands -/

section Shift

variable (δ) in
/-- Reindexing along an equality of strand counts. -/
noncomputable def recast {N N' : ℕ} (h : N = N') : TLFin K δ N →ₐ[K] TLFin K δ N' := by
  subst h; exact AlgHom.id K _

theorem recast_e {N N' : ℕ} (h : N = N') (i : Fin N) :
    recast δ h (e K δ adjFin i) = e K δ adjFin (Fin.cast h i) := by
  subst h; rfl

theorem sh_zero (m : ℕ) (y : TLFin K δ m) : sh δ 0 m y = recast δ (by omega) (sh1 δ m y) := by
  have : sh δ 0 m = (recast δ (by omega)).comp (sh1 δ m) :=
    hom_ext _ _ _ _ _ (fun i => by
      simp only [AlgHom.comp_apply, sh_e, sh1_e, recast_e]; congr 1; ext; simp; omega)
  exact AlgHom.congr_fun this y

theorem sh_succ (n m : ℕ) (y : TLFin K δ m) :
    sh δ (n + 1) m y = recast δ (by omega) (sh1 δ (n + m + 1) (sh δ n m y)) := by
  have : sh δ (n + 1) m = (recast δ (by omega)).comp ((sh1 δ (n + m + 1)).comp (sh δ n m)) :=
    hom_ext _ _ _ _ _ (fun i => by
      simp only [AlgHom.comp_apply, sh_e, sh1_e, recast_e]; congr 1; ext; simp; omega)
  exact AlgHom.congr_fun this y

variable (T : MarkovTower δ ε)

theorem negl_recast {N N' : ℕ} (h : N = N') {x : TLFin K δ N} (hx : Negl T N x) :
    Negl T N' (recast δ h x) := by
  subst h; exact hx

/-- Adding strands on the left keeps a negligible morphism negligible. -/
theorem negl_sh (m : ℕ) {y : TLFin K δ m} (hy : Negl T m y) :
    ∀ n, Negl T (n + m + 1) (sh δ n m y)
  | 0 => by rw [sh_zero]; exact negl_recast T _ (negl_sh1 T hy)
  | n + 1 => by rw [sh_succ]; exact negl_recast T _ (negl_sh1 T (negl_sh m hy n))

/-- Adding strands on the right keeps a negligible morphism negligible. -/
theorem negl_inclIter (r : ℕ) {x : TLFin K δ r} (hx : Negl T r x) :
    ∀ m, Negl T (r + m) (inclIter (δ := δ) r m x)
  | 0 => hx
  | m + 1 => negl_incl T (negl_inclIter r hx m)

end Shift

/-! ## The tensor product -/

section Tensor

variable (δ) in
/-- Side-by-side placement: `x` on the first `n + 1` strands, `y` on the last `m + 1`. -/
noncomputable def tens {n m : ℕ} (x : TLFin K δ n) (y : TLFin K δ m) : TLFin K δ (n + m + 1) :=
  inclIter (δ := δ) n (m + 1) x * sh δ n m y

theorem inclIter_commute_sh (n m : ℕ) (x : TLFin K δ n) (y : TLFin K δ m) :
    Commute (inclIter (δ := δ) n (m + 1) x) (sh δ n m y) := by
  refine (commute_of_gens (sh δ n m) _ (fun j => ?_) _).symm
  rw [sh_e]
  refine (commute_of_gens (inclIter (δ := δ) n (m + 1)) _ (fun i => ?_) _).symm
  rw [inclIter_e]
  exact e_commute_fin (by simp; omega)

theorem tens_mul {n m : ℕ} (x x' : TLFin K δ n) (y y' : TLFin K δ m) :
    tens δ x y * tens δ x' y' = tens δ (x * x') (y * y') := by
  simp only [tens, map_mul]
  rw [mul_assoc, ← mul_assoc (sh δ n m y), ← (inclIter_commute_sh n m x' y).eq]
  simp only [mul_assoc]

theorem tens_one (n m : ℕ) : tens δ (1 : TLFin K δ n) (1 : TLFin K δ m) = 1 := by
  simp [tens]

theorem tens_add_left {n m : ℕ} (x x' : TLFin K δ n) (y : TLFin K δ m) :
    tens δ (x + x') y = tens δ x y + tens δ x' y := by simp [tens, add_mul]

theorem tens_add_right {n m : ℕ} (x : TLFin K δ n) (y y' : TLFin K δ m) :
    tens δ x (y + y') = tens δ x y + tens δ x y' := by simp [tens, mul_add]

theorem tens_sub_left {n m : ℕ} (x x' : TLFin K δ n) (y : TLFin K δ m) :
    tens δ (x - x') y = tens δ x y - tens δ x' y := by simp [tens, sub_mul]

theorem tens_sub_right {n m : ℕ} (x : TLFin K δ n) (y y' : TLFin K δ m) :
    tens δ x (y - y') = tens δ x y - tens δ x y' := by simp [tens, mul_sub]

theorem tens_smul_left {n m : ℕ} (c : K) (x : TLFin K δ n) (y : TLFin K δ m) :
    tens δ (c • x) y = c • tens δ x y := by simp [tens]

theorem tens_smul_right {n m : ℕ} (c : K) (x : TLFin K δ n) (y : TLFin K δ m) :
    tens δ x (c • y) = c • tens δ x y := by simp [tens]

/-- `p_n ⊗ p_m` is the cabling block `wB`. -/
theorem tens_jw (n m : ℕ) : tens δ (jw δ n) (jw δ m) = wB δ n m := rfl

variable (T : MarkovTower δ ε)

/-- **The negligible morphisms form a tensor ideal**, left factor. -/
theorem negl_tens_left {n m : ℕ} {x : TLFin K δ n} (hx : Negl T n x) (y : TLFin K δ m) :
    Negl T (n + m + 1) (tens δ x y) :=
  negl_mul_right T (negl_inclIter T n hx (m + 1)) _

/-- **The negligible morphisms form a tensor ideal**, right factor. -/
theorem negl_tens_right {n m : ℕ} (x : TLFin K δ n) {y : TLFin K δ m} (hy : Negl T m y) :
    Negl T (n + m + 1) (tens δ x y) :=
  negl_mul_left T (negl_sh T m hy n) _

/-- **The tensor product on the quotient.** -/
noncomputable def tensQ {n m : ℕ} : Q T n → Q T m → Q T (n + m + 1) :=
  Quotient.lift₂ (fun x y => (tens δ x y : Q T (n + m + 1))) (fun x y x' y' hx hy => by
    have hx' : Negl T n (x - x') := hx
    have hy' : Negl T m (y - y') := hy
    rw [coe_eq_iff]
    have : tens δ x y - tens δ x' y' = tens δ (x - x') y + tens δ x' (y - y') := by
      rw [tens_sub_left, tens_sub_right]; abel
    rw [this]
    exact negl_add T (negl_tens_left T hx' y) (negl_tens_right T x' hy'))

theorem tensQ_coe {n m : ℕ} (x : TLFin K δ n) (y : TLFin K δ m) :
    tensQ T (x : Q T n) (y : Q T m) = (tens δ x y : Q T (n + m + 1)) := rfl

theorem tensQ_mul {n m : ℕ} (φ φ' : Q T n) (ψ ψ' : Q T m) :
    tensQ T φ ψ * tensQ T φ' ψ' = tensQ T (φ * φ') (ψ * ψ') := by
  obtain ⟨x, rfl⟩ := coe_surj T φ; obtain ⟨x', rfl⟩ := coe_surj T φ'
  obtain ⟨y, rfl⟩ := coe_surj T ψ; obtain ⟨y', rfl⟩ := coe_surj T ψ'
  rw [tensQ_coe, tensQ_coe, ← RingCon.coe_mul, tens_mul, ← RingCon.coe_mul, ← RingCon.coe_mul,
    tensQ_coe]

theorem tensQ_one (n m : ℕ) : tensQ T (1 : Q T n) (1 : Q T m) = 1 := by
  rw [← RingCon.coe_one, ← RingCon.coe_one, tensQ_coe, tens_one, RingCon.coe_one]

theorem tensQ_add_left {n m : ℕ} (φ φ' : Q T n) (ψ : Q T m) :
    tensQ T (φ + φ') ψ = tensQ T φ ψ + tensQ T φ' ψ := by
  obtain ⟨x, rfl⟩ := coe_surj T φ; obtain ⟨x', rfl⟩ := coe_surj T φ'
  obtain ⟨y, rfl⟩ := coe_surj T ψ
  rw [← RingCon.coe_add, tensQ_coe, tens_add_left, RingCon.coe_add, tensQ_coe, tensQ_coe]

theorem tensQ_add_right {n m : ℕ} (φ : Q T n) (ψ ψ' : Q T m) :
    tensQ T φ (ψ + ψ') = tensQ T φ ψ + tensQ T φ ψ' := by
  obtain ⟨x, rfl⟩ := coe_surj T φ
  obtain ⟨y, rfl⟩ := coe_surj T ψ; obtain ⟨y', rfl⟩ := coe_surj T ψ'
  rw [← RingCon.coe_add, tensQ_coe, tens_add_right, RingCon.coe_add, tensQ_coe, tensQ_coe]

theorem tensQ_smul_left {n m : ℕ} (c : K) (φ : Q T n) (ψ : Q T m) :
    tensQ T (c • φ) ψ = c • tensQ T φ ψ := by
  obtain ⟨x, rfl⟩ := coe_surj T φ; obtain ⟨y, rfl⟩ := coe_surj T ψ
  rw [← coe_smul', tensQ_coe, tens_smul_left, coe_smul', tensQ_coe]

theorem tensQ_smul_right {n m : ℕ} (c : K) (φ : Q T n) (ψ : Q T m) :
    tensQ T φ (c • ψ) = c • tensQ T φ ψ := by
  obtain ⟨x, rfl⟩ := coe_surj T φ; obtain ⟨y, rfl⟩ := coe_surj T ψ
  rw [← coe_smul', tensQ_coe, tens_smul_right, coe_smul', tensQ_coe]

/-- Tensor products of idempotents are idempotents. -/
theorem tensQ_idem {n m : ℕ} {φ : Q T n} {ψ : Q T m} (hφ : φ * φ = φ) (hψ : ψ * ψ = ψ) :
    tensQ T φ ψ * tensQ T φ ψ = tensQ T φ ψ := by
  rw [tensQ_mul, hφ, hψ]

theorem tens_incl {n m : ℕ} (x : TLFin K δ n) (c : TLFin K δ m) :
    tens δ x (incl δ m c) = incl δ (n + m + 1) (tens δ x c) := by
  simp only [tens, map_mul, sh_incl]; rfl

/-- **The trace is multiplicative on tensor products**: `τ(x ⊗ y) = τ(x) τ(y)`. -/
theorem tau_tens {n : ℕ} (x : TLFin K δ n) : ∀ (m : ℕ) (y : TLFin K δ m),
    T.τ (n + m + 1) (tens δ x y) = T.τ n x * T.τ m y
  | 0, y => by
    rw [level_zero δ y, tens_smul_right, map_smul, map_smul, T.tr_one]
    change augmentation K δ adjFin y • T.τ (n + 1) (incl δ n x * sh δ n 0 1) = _
    rw [map_one, mul_one, T.tr_incl, smul_eq_mul, mul_comm, smul_eq_mul, mul_one]
  | m + 1, y => by
    have IH := tau_tens x m
    have hw : y ∈ LinearMap.range (incl δ m).toLinearMap ⊔ JJ δ m := by
      rw [sup_eq_top δ _ (hProp δ _)]; exact Submodule.mem_top
    obtain ⟨y, hy', z, hz, rfl⟩ := Submodule.mem_sup.mp hw
    obtain ⟨c, rfl⟩ := hy'
    clear hw
    simp only [AlgHom.toLinearMap_apply, tens_add_right, map_add, mul_add]
    congr 1
    · rw [tens_incl]
      exact (T.tr_incl _ _).trans ((IH c).trans (by rw [T.tr_incl]))
    · induction hz using Submodule.span_induction with
      | mem u hu =>
        obtain ⟨a, b, rfl⟩ := hu
        set I := inclIter (δ := δ) n (m + 1) x
        have hI : inclIter (δ := δ) n (m + 1 + 1) x = incl δ (n + m + 1) I := rfl
        have hL : T.τ (m + 1) (incl δ m a * e K δ adjFin (Fin.last m) * incl δ m b) =
            ε * T.τ m (b * a) := by
          rw [T.tr_comm, ← mul_assoc, ← map_mul, T.tr_markov]
        have hcomm : T.τ (n + m + 1) (sh δ n m b * I * sh δ n m a) =
            T.τ (n + m + 1) (tens δ x (a * b)) := by
          calc T.τ (n + m + 1) (sh δ n m b * I * sh δ n m a)
              = T.τ (n + m + 1) (sh δ n m a * (sh δ n m b * I)) := T.tr_comm _ _ _
            _ = T.τ (n + m + 1) (I * (sh δ n m a * sh δ n m b)) := by rw [← mul_assoc, T.tr_comm]
            _ = T.τ (n + m + 1) (tens δ x (a * b)) := by
                rw [tens, show sh δ n m (a * b) = sh δ n m a * sh δ n m b from map_mul _ a b]
        calc T.τ (n + (m + 1) + 1) (tens δ x (incl δ m a * e K δ adjFin (Fin.last m) * incl δ m b))
            = T.τ (n + m + 1 + 1) (incl δ (n + m + 1) I * incl δ (n + m + 1) (sh δ n m a) *
                e K δ adjFin (Fin.last (n + m + 1)) * incl δ (n + m + 1) (sh δ n m b)) := by
              simp only [tens, map_mul, sh_incl, sh_last, hI, mul_assoc]; rfl
          _ = ε * T.τ (n + m + 1) (sh δ n m b * I * sh δ n m a) := by
              rw [T.tr_comm, ← mul_assoc, ← mul_assoc, ← map_mul, ← map_mul, T.tr_markov]
          _ = T.τ n x * T.τ (m + 1) (incl δ m a * e K δ adjFin (Fin.last m) * incl δ m b) := by
              rw [hcomm, IH, hL, T.tr_comm m b a]; ring
      | zero => rw [show tens δ x (0 : TLFin K δ (m + 1)) = 0 by simp [tens]]; simp
      | add a b _ _ ha hb => rw [tens_add_right, map_add, map_add, ha, hb, mul_add]
      | smul r a _ ha => rw [tens_smul_right, map_smul, map_smul, ha, smul_eq_mul, smul_eq_mul,
          mul_left_comm]

/-! ## Associativity, up to reindexing the strands -/

theorem recast_mul {N N' : ℕ} (h : N = N') (x y : TLFin K δ N) :
    recast δ h (x * y) = recast δ h x * recast δ h y := map_mul _ x y

theorem inclIter_inclIter (n m p : ℕ) (x : TLFin K δ n) :
    recast δ (by omega) (inclIter (δ := δ) (n + m + 1) (p + 1) (inclIter (δ := δ) n (m + 1) x)) =
      inclIter (δ := δ) n (m + p + 1 + 1) x := by
  have : (recast δ (by omega)).comp ((inclIter (δ := δ) (n + m + 1) (p + 1)).comp
      (inclIter (δ := δ) n (m + 1))) = inclIter (δ := δ) n (m + p + 1 + 1) :=
    hom_ext _ _ _ _ _ (fun i => by
      simp only [AlgHom.comp_apply, inclIter_e, recast_e]; congr 1)
  exact AlgHom.congr_fun this x

theorem inclIter_sh (n m p : ℕ) (y : TLFin K δ m) :
    recast δ (by omega) (inclIter (δ := δ) (n + m + 1) (p + 1) (sh δ n m y)) =
      sh δ n (m + p + 1) (inclIter (δ := δ) m (p + 1) y) := by
  have : (recast δ (by omega)).comp ((inclIter (δ := δ) (n + m + 1) (p + 1)).comp (sh δ n m)) =
      (sh δ n (m + p + 1)).comp (inclIter (δ := δ) m (p + 1)) :=
    hom_ext _ _ _ _ _ (fun i => by
      simp only [AlgHom.comp_apply, inclIter_e, recast_e, sh_e]; congr 1)
  exact AlgHom.congr_fun this y

theorem sh_sh (n m p : ℕ) (z : TLFin K δ p) :
    recast δ (by omega) (sh δ (n + m + 1) p z) = sh δ n (m + p + 1) (sh δ m p z) := by
  have : (recast δ (by omega)).comp (sh δ (n + m + 1) p) = (sh δ n (m + p + 1)).comp (sh δ m p) :=
    hom_ext _ _ _ _ _ (fun i => by
      simp only [AlgHom.comp_apply, recast_e, sh_e]; congr 1; ext; simp; omega)
  exact AlgHom.congr_fun this z

/-- **Associativity of the tensor product**, up to reindexing the strand count. -/
theorem tens_assoc {n m p : ℕ} (x : TLFin K δ n) (y : TLFin K δ m) (z : TLFin K δ p) :
    recast δ (by omega) (tens δ (tens δ x y) z) = tens δ x (tens δ y z) := by
  simp only [tens, map_mul]
  rw [inclIter_inclIter, inclIter_sh, sh_sh, mul_assoc]

/-! ## On the quotient: trace and associativity -/

/-- **The quotient trace is multiplicative on tensor products.** -/
theorem tauQ_tensQ {n m : ℕ} (φ : Q T n) (ψ : Q T m) :
    tauQ T (n + m + 1) (tensQ T φ ψ) = tauQ T n φ * tauQ T m ψ := by
  obtain ⟨x, rfl⟩ := coe_surj T φ; obtain ⟨y, rfl⟩ := coe_surj T ψ
  rw [tensQ_coe, tauQ_coe, tauQ_coe, tauQ_coe, tau_tens]

/-- Reindexing on the quotient. -/
noncomputable def recastQ {N N' : ℕ} (h : N = N') : Q T N → Q T N' := by
  subst h; exact id

theorem recastQ_coe {N N' : ℕ} (h : N = N') (x : TLFin K δ N) :
    recastQ T h (x : Q T N) = (recast δ h x : Q T N') := by
  subst h; rfl

/-- **Associativity of the tensor product on the quotient**, up to reindexing. -/
theorem tensQ_assoc {n m p : ℕ} (φ : Q T n) (ψ : Q T m) (χ : Q T p) :
    recastQ T (by omega) (tensQ T (tensQ T φ ψ) χ) = tensQ T φ (tensQ T ψ χ) := by
  obtain ⟨x, rfl⟩ := coe_surj T φ; obtain ⟨y, rfl⟩ := coe_surj T ψ
  obtain ⟨z, rfl⟩ := coe_surj T χ
  rw [tensQ_coe, tensQ_coe, tensQ_coe, tensQ_coe, recastQ_coe, tens_assoc]

end Tensor

end QOU.HeckeTemperleyLieb.TLQuotientTensor
