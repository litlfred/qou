import HeckeTemperleyLieb.TLMeridianClosure

/-!
# The cup slide and naturality for cabled loops on the Temperley–Lieb tower

Bean `hkmt`. The row `S_{b,j}` is the closure of the Jones–Wenzl projector `p_j` linked once with
a `b`-strand cable carrying `p_{b−1}`. The cable is the product of the single-strand loops of
`TLMeridianClosure`: `cable n b = ι(cable n (b−1)) · loop n (b−1)`. This file proves the two
local moves the Chebyshev recursion for the rows needs.

* `cup_hopf`, `cup_loop`: **cup slide.** Two adjacent cable strands joined by a cap can be
  pulled off the encircled block: `e · ι(loop n c) · σ · ι(loop n c) = e · σ`, equivalently
  `e · ι(loop n c) · loop n (c+1) = e`.

The local relations are proved once in an abstract section (`TLAbstract`) over any ring
holding a Temperley–Lieb pair `a, b` (`a² = δa`, `b² = δb`, `aba = a`, `bab = b`), with the
positive-loop crossings `σ = A − A⁻¹·e`, `δ = A² + A⁻²`.

No empirical input; everything is over an arbitrary field.

-- Ref: [jones1983] https://doi.org/10.1007/BF01389127
-/

namespace QOU.HeckeTemperleyLieb.TLCable

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLPositiveLoop QOU.HeckeTemperleyLieb.TLHopfRow
open QOU.HeckeTemperleyLieb.TLMeridian

/-! ## Local relations in any ring -/

section TLAbstract

variable {K : Type*} [Field K] {R : Type*} [Ring R] [Algebra K R] {δ A : K}

variable (A) in
/-- `σ(x) = A − A⁻¹x`. -/
noncomputable def cr (x : R) : R := A • 1 - A⁻¹ • x

variable (A) in
/-- `σ(x)⁻¹ = A⁻¹ − A x`. -/
noncomputable def crI (x : R) : R := A⁻¹ • 1 - A • x

variable (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2)
include hA hδ

theorem cr_mul_crI {x : R} (hx : x * x = δ • x) : cr A x * crI A x = 1 := by
  unfold cr crI
  simp only [mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, hx, smul_smul]
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

theorem crI_mul_cr {x : R} (hx : x * x = δ • x) : crI A x * cr A x = 1 := by
  unfold cr crI
  simp only [mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, hx, smul_smul]
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

/-- `x σ(y) σ(x) = −x y`. -/
theorem capL {x y : R} (hx : x * x = δ • x) (hxyx : x * y * x = x) :
    x * cr A y * cr A x = -(x * y) := by
  unfold cr
  simp only [mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul, hx,
    ← mul_assoc, hxyx]
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

/-- `x σ(y)⁻¹ σ(x)⁻¹ = −x y`. -/
theorem capLI {x y : R} (hx : x * x = δ • x) (hxyx : x * y * x = x) :
    x * crI A y * crI A x = -(x * y) := by
  unfold crI
  simp only [mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul, hx,
    ← mul_assoc, hxyx]
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

/-- `σ(x) σ(y) x = −y x`. -/
theorem capR {x y : R} (hx : x * x = δ • x) (hxyx : x * y * x = x) :
    cr A x * cr A y * x = -(y * x) := by
  unfold cr
  simp only [mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul, hx,
    ← mul_assoc, hxyx]
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

/-- `σ(x)⁻¹ σ(y)⁻¹ x = −y x`. -/
theorem capRI {x y : R} (hx : x * x = δ • x) (hxyx : x * y * x = x) :
    crI A x * crI A y * x = -(y * x) := by
  unfold crI
  simp only [mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul, hx,
    ← mul_assoc, hxyx]
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

/-- `σ(x)·x = −A⁻³ x`. -/
theorem cr_mul_self {x : R} (hx : x * x = δ • x) : cr A x * x = -(A⁻¹ ^ 3) • x := by
  unfold cr
  simp only [sub_mul, smul_mul_assoc, one_mul, hx, smul_smul]
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

/-- `σ(x)⁻¹·x = −A³ x`. -/
theorem crI_mul_self {x : R} (hx : x * x = δ • x) : crI A x * x = -(A ^ 3) • x := by
  unfold crI
  simp only [sub_mul, smul_mul_assoc, one_mul, hx, smul_smul]
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

/-- The braid relation for the positive-loop crossings of a Temperley–Lieb pair. -/
theorem cr_braid {a b : R} (ha : a * a = δ • a) (hb : b * b = δ • b) (haba : a * b * a = a)
    (hbab : b * a * b = b) : cr A a * cr A b * cr A a = cr A b * cr A a * cr A b := by
  unfold cr
  simp only [mul_sub, sub_mul, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_smul,
    ← mul_assoc, ha, hb, haba, hbab]
  match_scalars <;> (try simp only [hδ]) <;> field_simp <;> ring

end TLAbstract

/-! ## The slide identities -/

section Slides

variable {K : Type*} [Field K] {R : Type*} [Ring R] [Algebra K R] {δ A : K}
  (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) {a b X : R}
  (ha : a * a = δ • a) (hb : b * b = δ • b) (haba : a * b * a = a) (hbab : b * a * b = b)

variable (A) in
/-- The crossing `σ(x)` as a unit. -/
noncomputable def crU (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) {x : R} (hx : x * x = δ • x) : Rˣ :=
  ⟨cr A x, crI A x, cr_mul_crI hA hδ hx, crI_mul_cr hA hδ hx⟩

include hA hδ ha hb haba hbab

theorem braidU : crU A hA hδ ha * crU A hA hδ hb * crU A hA hδ ha
    = crU A hA hδ hb * crU A hA hδ ha * crU A hA hδ hb :=
  Units.ext (by simp only [Units.val_mul]; exact cr_braid hA hδ ha hb haba hbab)

theorem braidZ (z : R) : cr A a * (cr A b * (cr A a * z)) = cr A b * (cr A a * (cr A b * z)) := by
  have h := congrArg (· * z) (congrArg Units.val (braidU hA hδ ha hb haba hbab))
  simpa only [Units.val_mul, mul_assoc] using h

/-- `σ(a)⁻¹ σ(b) σ(a) = σ(b) σ(a) σ(b)⁻¹`. -/
theorem k1Z (z : R) : crI A a * (cr A b * (cr A a * z)) = cr A b * (cr A a * (crI A b * z)) := by
  have hU : (crU A hA hδ ha)⁻¹ * crU A hA hδ hb * crU A hA hδ ha
      = crU A hA hδ hb * crU A hA hδ ha * (crU A hA hδ hb)⁻¹ := by
    calc _ = (crU A hA hδ ha)⁻¹ * (crU A hA hδ hb * crU A hA hδ ha * crU A hA hδ hb)
          * (crU A hA hδ hb)⁻¹ := by group
      _ = (crU A hA hδ ha)⁻¹ * (crU A hA hδ ha * crU A hA hδ hb * crU A hA hδ ha)
          * (crU A hA hδ hb)⁻¹ := by rw [braidU hA hδ ha hb haba hbab]
      _ = _ := by group
  have h := congrArg (· * z) (congrArg Units.val hU)
  simpa only [Units.val_mul, mul_assoc] using h

/-- `σ(a) σ(b)⁻¹ σ(a)⁻¹ = σ(b)⁻¹ σ(a)⁻¹ σ(b)`. -/
theorem r2Z (z : R) : cr A a * (crI A b * (crI A a * z)) = crI A b * (crI A a * (cr A b * z)) := by
  have hU : crU A hA hδ ha * (crU A hA hδ hb)⁻¹ * (crU A hA hδ ha)⁻¹
      = (crU A hA hδ hb)⁻¹ * (crU A hA hδ ha)⁻¹ * crU A hA hδ hb := by
    calc _ = (crU A hA hδ hb)⁻¹ * (crU A hA hδ ha)⁻¹
          * (crU A hA hδ ha * crU A hA hδ hb * crU A hA hδ ha)
          * (crU A hA hδ hb)⁻¹ * (crU A hA hδ ha)⁻¹ := by group
      _ = (crU A hA hδ hb)⁻¹ * (crU A hA hδ ha)⁻¹
          * (crU A hA hδ hb * crU A hA hδ ha * crU A hA hδ hb)
          * (crU A hA hδ hb)⁻¹ * (crU A hA hδ ha)⁻¹ := by rw [braidU hA hδ ha hb haba hbab]
      _ = _ := by group
  have h := congrArg (· * z) (congrArg Units.val hU)
  simpa only [Units.val_mul, mul_assoc] using h

omit ha hb haba hbab in
theorem capLZ {x y : R} (hx : x * x = δ • x) (hxyx : x * y * x = x) (z : R) :
    x * (cr A y * (cr A x * z)) = -(x * (y * z)) := by
  have h := congrArg (· * z) (capL hA hδ hx hxyx)
  simpa only [mul_assoc, neg_mul] using h

omit ha hb haba hbab in
theorem capLIZ {x y : R} (hx : x * x = δ • x) (hxyx : x * y * x = x) (z : R) :
    x * (crI A y * (crI A x * z)) = -(x * (y * z)) := by
  have h := congrArg (· * z) (capLI hA hδ hx hxyx)
  simpa only [mul_assoc, neg_mul] using h

omit hA hδ ha hb haba hbab in
theorem commZ (hX : Commute X b) (z : R) : X * (cr A b * z) = cr A b * (X * z) := by
  have : Commute X (cr A b) := by
    unfold cr; exact ((Commute.one_right X).smul_right _).sub_right (hX.smul_right _)
  rw [← mul_assoc, this.eq, mul_assoc]

omit hA hδ ha hb haba hbab in
theorem commIZ (hX : Commute X b) (z : R) : X * (crI A b * z) = crI A b * (X * z) := by
  have : Commute X (crI A b) := by
    unfold crI; exact ((Commute.one_right X).smul_right _).sub_right (hX.smul_right _)
  rw [← mul_assoc, this.eq, mul_assoc]

/-- **Cup slide, positive step.** If `a X σ(a) X = a σ(a)` and `X` commutes with `b`, then
`b (σ(a) X σ(a)) σ(b) (σ(a) X σ(a)) = b σ(b)`. -/
theorem slide_pos (hX : Commute X b) (hyp : ∀ z, a * (X * (cr A a * (X * z))) = a * (cr A a * z))
    (z : R) :
    b * (cr A a * (X * (cr A a * (cr A b * (cr A a * (X * (cr A a * z)))))))
      = b * (cr A b * z) := by
  rw [braidZ hA hδ ha hb haba hbab, commZ hX, ← commZ hX (cr A a * z),
    capLZ hA hδ hb hbab, hyp, braidZ hA hδ ha hb haba hbab, capLZ hA hδ ha haba, mul_neg,
    neg_neg, ← mul_assoc, ← mul_assoc, hbab]

/-- **Cup slide, conjugate step.** If `a X σ(a) X = a σ(a)` and `X` commutes with `b`, then
`b (σ(a) X σ(a)⁻¹) σ(b) (σ(a) X σ(a)⁻¹) = b σ(b)`. -/
theorem slide_conj (hX : Commute X b) (hyp : ∀ z, a * (X * (cr A a * (X * z))) = a * (cr A a * z))
    (z : R) :
    b * (cr A a * (X * (crI A a * (cr A b * (cr A a * (X * (crI A a * z)))))))
      = b * (cr A b * z) := by
  rw [k1Z hA hδ ha hb haba hbab, commZ hX, ← commIZ hX (crI A a * z),
    capLZ hA hδ hb hbab, hyp, r2Z hA hδ ha hb haba hbab, capLIZ hA hδ ha haba, mul_neg,
    neg_neg, ← mul_assoc, ← mul_assoc, hbab]

end Slides

/-! ## The cup slide on the tower -/

section Tower

variable {K : Type*} [Field K] {δ A : K}

theorem crossing_eq_cr {m : ℕ} (i : Fin m) : crossing δ A i = cr A (e K δ adjFin i) := rfl

theorem crossingInv_eq_crI {m : ℕ} (i : Fin m) :
    crossingInv δ A i = crI A (e K δ adjFin i) := rfl

theorem adj_low (m : ℕ) :
    e K δ adjFin (Fin.castSucc (Fin.last m)) * e K δ adjFin (Fin.last (m + 1))
      * e K δ adjFin (Fin.castSucc (Fin.last m)) = e K δ adjFin (Fin.castSucc (Fin.last m)) :=
  e_adjacent_fin (by simp)

/-- **Cup slide for the Hopf word** (`hW` form). `e ι(W) σ ι(W) = e σ` on the top strand pair,
`W = hopfW m`. -/
theorem cup_hopf (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) : ∀ m : ℕ,
    e K δ adjFin (Fin.last m) * incl δ m (hopfW δ A m) * crossing δ A (Fin.last m) *
        incl δ m (hopfW δ A m)
      = e K δ adjFin (Fin.last m) * crossing δ A (Fin.last m)
  | 0 => by simp [hopfW, hopfList]
  | m + 1 => by
    have IH := congrArg (incl δ (m + 1)) (cup_hopf hA hδ m)
    simp only [map_mul, incl_e, incl_crossing] at IH
    have hyp : ∀ z, e K δ adjFin (Fin.castSucc (Fin.last m)) *
        (incl δ (m + 1) (incl δ m (hopfW δ A m)) *
          (cr A (e K δ adjFin (Fin.castSucc (Fin.last m))) *
            (incl δ (m + 1) (incl δ m (hopfW δ A m)) * z)))
        = e K δ adjFin (Fin.castSucc (Fin.last m)) *
          (cr A (e K δ adjFin (Fin.castSucc (Fin.last m))) * z) := fun z => by
      have := congrArg (· * z) IH
      simpa only [mul_assoc, crossing_eq_cr] using this
    have key := slide_pos hA hδ (e_sq' δ _) (e_sq' δ _) (adj_low (δ := δ) m) (last_adj δ m)
      (incl_incl_commute δ m (hopfW δ A m)) hyp 1
    rw [hopfW_succ, map_mul, map_mul, incl_crossing]
    simpa only [mul_one, mul_assoc, crossing_eq_cr] using key

/-- **Cup slide for the passing loop.** `e ι(loop n c) σ ι(loop n c) = e σ`. -/
theorem cup_loop (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) (n : ℕ) : ∀ c : ℕ,
    e K δ adjFin (Fin.last (n + c + 1)) * incl δ (n + c + 1) (loop δ A n c) *
        crossing δ A (Fin.last (n + c + 1)) * incl δ (n + c + 1) (loop δ A n c)
      = e K δ adjFin (Fin.last (n + c + 1)) * crossing δ A (Fin.last (n + c + 1))
  | 0 => cup_hopf hA hδ (n + 1)
  | c + 1 => by
    show e K δ adjFin (Fin.last (n + c + 2)) * incl δ (n + c + 2) (loop δ A n (c + 1)) *
        crossing δ A (Fin.last (n + c + 2)) * incl δ (n + c + 2) (loop δ A n (c + 1))
      = e K δ adjFin (Fin.last (n + c + 2)) * crossing δ A (Fin.last (n + c + 2))
    have hw : incl δ (n + c + 2) (loop δ A n (c + 1)) =
        crossing δ A (Fin.castSucc (Fin.last (n + c + 1))) *
          incl δ (n + c + 2) (incl δ (n + c + 1) (loop δ A n c)) *
          crossingInv δ A (Fin.castSucc (Fin.last (n + c + 1))) := by
      rw [loop, map_mul, map_mul, incl_crossing', incl_crossingInv]
    have IH := congrArg (incl δ (n + c + 2)) (cup_loop hA hδ n c)
    simp only [map_mul, incl_e, incl_crossing] at IH
    have hyp : ∀ z, e K δ adjFin (Fin.castSucc (Fin.last (n + c + 1))) *
        (incl δ (n + c + 2) (incl δ (n + c + 1) (loop δ A n c)) *
          (cr A (e K δ adjFin (Fin.castSucc (Fin.last (n + c + 1)))) *
            (incl δ (n + c + 2) (incl δ (n + c + 1) (loop δ A n c)) * z)))
        = e K δ adjFin (Fin.castSucc (Fin.last (n + c + 1))) *
          (cr A (e K δ adjFin (Fin.castSucc (Fin.last (n + c + 1)))) * z) := fun z => by
      have := congrArg (· * z) IH
      simpa only [mul_assoc, crossing_eq_cr] using this
    have key := slide_conj hA hδ (e_sq' δ _) (e_sq' δ _) (adj_low (δ := δ) (n + c + 1))
      (last_adj δ (n + c + 1)) (incl_incl_commute δ (n + c + 1) (loop δ A n c)) hyp 1
    rw [hw]
    simpa only [mul_one, mul_assoc, crossing_eq_cr, crossingInv_eq_crI] using key

/-- **Cup slide**, loop form: `e · ι(loop n c) · loop n (c+1) = e`. -/
theorem cup_loop_loop (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) (n c : ℕ) :
    e K δ adjFin (Fin.last (n + c + 1)) * incl δ (n + c + 1) (loop δ A n c) *
        loop δ A n (c + 1) = e K δ adjFin (Fin.last (n + c + 1)) := by
  show _ * _ * (crossing δ A (Fin.last (n + c + 1)) * incl δ (n + c + 1) (loop δ A n c) *
      crossingInv δ A (Fin.last (n + c + 1))) = _
  rw [← mul_assoc, ← mul_assoc, cup_loop hA hδ n c, mul_assoc,
    crossing_mul_crossingInv hA hδ, mul_one]

end Tower

end QOU.HeckeTemperleyLieb.TLCable
