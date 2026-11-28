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

omit ha hb haba hbab in
theorem capRZ {x y : R} (hx : x * x = δ • x) (hxyx : x * y * x = x) (z : R) :
    cr A x * (cr A y * (x * z)) = -(y * (x * z)) := by
  have h := congrArg (· * z) (capR hA hδ hx hxyx)
  simpa only [mul_assoc, neg_mul] using h

omit ha hb haba hbab in
theorem capRIZ {x y : R} (hx : x * x = δ • x) (hxyx : x * y * x = x) (z : R) :
    crI A x * (crI A y * (x * z)) = -(y * (x * z)) := by
  have h := congrArg (· * z) (capRI hA hδ hx hxyx)
  simpa only [mul_assoc, neg_mul] using h

/-- **Cup slide, positive step, right.** -/
theorem slide_pos_right (hX : Commute X b)
    (hyp : ∀ z, X * (cr A a * (X * (a * z))) = cr A a * (a * z)) (z : R) :
    cr A a * (X * (cr A a * (cr A b * (cr A a * (X * (cr A a * (b * z)))))))
      = cr A b * (b * z) := by
  rw [braidZ hA hδ ha hb haba hbab, commZ hX, ← commZ hX (cr A a * (b * z)),
    capRZ hA hδ hb hbab,]
  simp only [mul_neg]
  rw [hyp,
    braidZ hA hδ ha hb haba hbab, capRZ hA hδ ha haba]
  simp only [mul_neg, neg_neg]
  rw [← mul_assoc b a, ← mul_assoc (b * a) b, hbab]

/-- **Cup slide, conjugate step, right.** -/
theorem slide_conj_right (hX : Commute X b)
    (hyp : ∀ z, X * (cr A a * (X * (a * z))) = cr A a * (a * z)) (z : R) :
    cr A a * (X * (crI A a * (cr A b * (cr A a * (X * (crI A a * (b * z)))))))
      = cr A b * (b * z) := by
  rw [k1Z hA hδ ha hb haba hbab, commZ hX, ← commIZ hX (crI A a * (b * z)),
    capRIZ hA hδ hb hbab,]
  simp only [mul_neg]
  rw [hyp,
    braidZ hA hδ ha hb haba hbab, capRZ hA hδ ha haba]
  simp only [mul_neg, neg_neg]
  rw [← mul_assoc b a, ← mul_assoc (b * a) b, hbab]

omit hδ ha hb haba hbab in
theorem eq_of_cr (x : R) : x = A ^ 2 • (1 : R) - A • cr A x := by
  unfold cr
  simp only [smul_sub, smul_smul, mul_inv_cancel₀ hA, one_smul, sq]
  abel

/-- **Naturality across a passed cup.** If `X` commutes with `b`, then `a` commutes with
`σ(b) σ(a) X σ(a)⁻¹ σ(b)⁻¹`. -/
theorem nat_comm (hX : Commute X b) :
    Commute a (cr A b * (cr A a * X * crI A a) * crI A b) := by
  have hs : Commute (cr A a) (cr A b * (cr A a * X * crI A a) * crI A b) := by
    have h : cr A a * (cr A b * (cr A a * (X * (crI A a * (crI A b * 1)))))
        = cr A b * (cr A a * (X * (crI A a * (crI A b * (cr A a * 1))))) := by
      rw [braidZ hA hδ ha hb haba hbab, ← commZ hX (crI A a * (crI A b * 1)),
        r2Z hA hδ hb ha hbab haba]
    show _ = _
    simpa only [mul_assoc, mul_one] using h
  have := ((Commute.one_left (cr A b * (cr A a * X * crI A a) * crI A b)).smul_left
    (A ^ 2)).sub_left (hs.smul_left A)
  rwa [← eq_of_cr hA a] at this

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

/-- **Cup slide for the Hopf word, right.** `ι(W) σ ι(W) e = σ e`. -/
theorem hopf_cup (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) : ∀ m : ℕ,
    incl δ m (hopfW δ A m) * crossing δ A (Fin.last m) * incl δ m (hopfW δ A m) *
        e K δ adjFin (Fin.last m)
      = crossing δ A (Fin.last m) * e K δ adjFin (Fin.last m)
  | 0 => by simp [hopfW, hopfList]
  | m + 1 => by
    have IH := congrArg (incl δ (m + 1)) (hopf_cup hA hδ m)
    simp only [map_mul, incl_e, incl_crossing] at IH
    have hyp : ∀ z, incl δ (m + 1) (incl δ m (hopfW δ A m)) *
        (cr A (e K δ adjFin (Fin.castSucc (Fin.last m))) *
          (incl δ (m + 1) (incl δ m (hopfW δ A m)) * (e K δ adjFin (Fin.castSucc (Fin.last m)) * z)))
        = cr A (e K δ adjFin (Fin.castSucc (Fin.last m))) *
          (e K δ adjFin (Fin.castSucc (Fin.last m)) * z) := fun z => by
      have := congrArg (· * z) IH
      simpa only [mul_assoc, crossing_eq_cr] using this
    have key := slide_pos_right hA hδ (e_sq' δ _) (e_sq' δ _) (adj_low (δ := δ) m) (last_adj δ m)
      (incl_incl_commute δ m (hopfW δ A m)) hyp 1
    rw [hopfW_succ, map_mul, map_mul, incl_crossing]
    simpa only [mul_one, mul_assoc, crossing_eq_cr] using key

/-- **Cup slide for the passing loop, right.** `ι(loop n c) σ ι(loop n c) e = σ e`. -/
theorem loop_cup_cr (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) (n : ℕ) : ∀ c : ℕ,
    incl δ (n + c + 1) (loop δ A n c) * crossing δ A (Fin.last (n + c + 1)) *
        incl δ (n + c + 1) (loop δ A n c) * e K δ adjFin (Fin.last (n + c + 1))
      = crossing δ A (Fin.last (n + c + 1)) * e K δ adjFin (Fin.last (n + c + 1))
  | 0 => hopf_cup hA hδ (n + 1)
  | c + 1 => by
    show incl δ (n + c + 2) (loop δ A n (c + 1)) * crossing δ A (Fin.last (n + c + 2)) *
        incl δ (n + c + 2) (loop δ A n (c + 1)) * e K δ adjFin (Fin.last (n + c + 2))
      = crossing δ A (Fin.last (n + c + 2)) * e K δ adjFin (Fin.last (n + c + 2))
    have hw : incl δ (n + c + 2) (loop δ A n (c + 1)) =
        crossing δ A (Fin.castSucc (Fin.last (n + c + 1))) *
          incl δ (n + c + 2) (incl δ (n + c + 1) (loop δ A n c)) *
          crossingInv δ A (Fin.castSucc (Fin.last (n + c + 1))) := by
      rw [loop, map_mul, map_mul, incl_crossing', incl_crossingInv]
    have IH := congrArg (incl δ (n + c + 2)) (loop_cup_cr hA hδ n c)
    simp only [map_mul, incl_e, incl_crossing] at IH
    have hyp : ∀ z, incl δ (n + c + 2) (incl δ (n + c + 1) (loop δ A n c)) *
        (cr A (e K δ adjFin (Fin.castSucc (Fin.last (n + c + 1)))) *
          (incl δ (n + c + 2) (incl δ (n + c + 1) (loop δ A n c)) *
            (e K δ adjFin (Fin.castSucc (Fin.last (n + c + 1))) * z)))
        = cr A (e K δ adjFin (Fin.castSucc (Fin.last (n + c + 1)))) *
          (e K δ adjFin (Fin.castSucc (Fin.last (n + c + 1))) * z) := fun z => by
      have := congrArg (· * z) IH
      simpa only [mul_assoc, crossing_eq_cr] using this
    have key := slide_conj_right hA hδ (e_sq' δ _) (e_sq' δ _) (adj_low (δ := δ) (n + c + 1))
      (last_adj δ (n + c + 1)) (incl_incl_commute δ (n + c + 1) (loop δ A n c)) hyp 1
    rw [hw]
    simpa only [mul_one, mul_assoc, crossing_eq_cr, crossingInv_eq_crI] using key

/-- **Cup slide**, right loop form: `ι(loop n c) · loop n (c+1) · e = e`. -/
theorem loop_loop_cup (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) (n c : ℕ) :
    incl δ (n + c + 1) (loop δ A n c) * loop δ A n (c + 1) * e K δ adjFin (Fin.last (n + c + 1))
      = e K δ adjFin (Fin.last (n + c + 1)) := by
  show _ * (crossing δ A (Fin.last (n + c + 1)) * incl δ (n + c + 1) (loop δ A n c) *
      crossingInv δ A (Fin.last (n + c + 1))) * _ = _
  have h1 : crossingInv δ A (Fin.last (n + c + 1)) * e K δ adjFin (Fin.last (n + c + 1))
      = (-(A ^ 3)) • e K δ adjFin (Fin.last (n + c + 1)) := crI_mul_self hA hδ (e_sq' δ _)
  have h2 : crossing δ A (Fin.last (n + c + 1)) * e K δ adjFin (Fin.last (n + c + 1))
      = (-(A⁻¹ ^ 3)) • e K δ adjFin (Fin.last (n + c + 1)) := cr_mul_self hA hδ (e_sq' δ _)
  calc _ = incl δ (n + c + 1) (loop δ A n c) * crossing δ A (Fin.last (n + c + 1)) *
        incl δ (n + c + 1) (loop δ A n c) *
        (crossingInv δ A (Fin.last (n + c + 1)) * e K δ adjFin (Fin.last (n + c + 1))) := by
          simp only [mul_assoc]
    _ = (-(A ^ 3)) • (crossing δ A (Fin.last (n + c + 1)) * e K δ adjFin (Fin.last (n + c + 1))) := by
          rw [h1, mul_smul_comm, loop_cup_cr hA hδ n c]
    _ = _ := by
          rw [h2, smul_smul, show -A ^ 3 * -A⁻¹ ^ 3 = (1 : K) by field_simp, one_smul]

/-- An element commuting with `e_i` commutes with `σ_i` and `σ_i⁻¹`. -/
theorem commute_crossing {m : ℕ} {y : TLFin K δ m} {i : Fin m}
    (h : Commute y (e K δ adjFin i)) : Commute y (crossing δ A i) :=
  ((Commute.one_right y).smul_right _).sub_right (h.smul_right _)

theorem commute_crossingInv {m : ℕ} {y : TLFin K δ m} {i : Fin m}
    (h : Commute y (e K δ adjFin i)) : Commute y (crossingInv δ A i) :=
  ((Commute.one_right y).smul_right _).sub_right (h.smul_right _)

/-- **Naturality on the cable.** A cap between two cable strands that the loop passes commutes
with the loop. -/
theorem loop_comm_cable (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) (n : ℕ) : ∀ (c k : ℕ)
    (hk1 : 1 ≤ k) (hk : k + 1 ≤ c),
    Commute (e K δ adjFin (⟨n + k, by omega⟩ : Fin (n + c + 1))) (loop δ A n c)
  | 0, k, _, hk => absurd hk (by omega)
  | c + 1, k, hk1, hk => by
    show Commute (e K δ adjFin (⟨n + k, by omega⟩ : Fin (n + c + 2)))
      (crossing δ A (Fin.last (n + c + 1)) * incl δ (n + c + 1) (loop δ A n c) *
        crossingInv δ A (Fin.last (n + c + 1)))
    by_cases hkc : k + 1 ≤ c
    · have hE : (e K δ adjFin (⟨n + k, by omega⟩ : Fin (n + c + 2)))
          = incl δ (n + c + 1) (e K δ adjFin (⟨n + k, by omega⟩ : Fin (n + c + 1))) := by
        rw [incl_e]; rfl
      have hf : Commute (e K δ adjFin (⟨n + k, by omega⟩ : Fin (n + c + 2)))
          (e K δ adjFin (Fin.last (n + c + 1))) :=
        e_commute_fin (by simp only [Fin.val_last]; omega)
      refine ((commute_crossing hf).mul_right ?_).mul_right (commute_crossingInv hf)
      rw [hE]
      exact (loop_comm_cable hA hδ n c k hk1 hkc).map (incl δ (n + c + 1))
    · obtain rfl : k = c := by omega
      obtain ⟨c', rfl⟩ : ∃ c', k = c' + 1 := ⟨k - 1, by omega⟩
      have hE : (⟨n + (c' + 1), by omega⟩ : Fin (n + (c' + 1) + 2))
          = Fin.castSucc (Fin.last (n + (c' + 1))) := Fin.ext (by simp)
      have hw : incl δ (n + c' + 2) (loop δ A n (c' + 1)) =
          crossing δ A (Fin.castSucc (Fin.last (n + c' + 1))) *
            incl δ (n + c' + 2) (incl δ (n + c' + 1) (loop δ A n c')) *
            crossingInv δ A (Fin.castSucc (Fin.last (n + c' + 1))) := by
        rw [loop, map_mul, map_mul, incl_crossing', incl_crossingInv]
      rw [hE]
      show Commute (e K δ adjFin (Fin.castSucc (Fin.last (n + c' + 1))))
        (crossing δ A (Fin.last (n + c' + 2)) * incl δ (n + c' + 2) (loop δ A n (c' + 1)) *
          crossingInv δ A (Fin.last (n + c' + 2)))
      rw [hw]
      exact nat_comm hA hδ (e_sq' δ _) (e_sq' δ _) (adj_low (δ := δ) (n + c' + 1))
        (last_adj δ (n + c' + 1)) (incl_incl_commute δ (n + c' + 1) (loop δ A n c'))

end Tower

/-! ## The cable and the shifted projector -/

section Cable

variable {K : Type*} [Field K] {δ A : K}

variable (δ) in
/-- The right shift `TL_{m+1} → TL_{n+m+2}`, `e_i ↦ e_{n+1+i}`: the algebra of the cable
strands. -/
noncomputable def sh (n m : ℕ) : TLFin K δ m →ₐ[K] TLFin K δ (n + m + 1) :=
  lift K δ adjFin (fun i => e K δ adjFin (⟨n + 1 + i, by omega⟩ : Fin (n + m + 1)))
    (fun _ => e_sq _)
    (fun i j h => e_adjacent (by simp only [adjFin] at h ⊢; omega))
    (fun i j h => e_farCommute (by simp only [adjFin] at h ⊢; omega))

@[simp] theorem sh_e (n m : ℕ) (i : Fin m) :
    sh δ n m (e K δ adjFin i) = e K δ adjFin (⟨n + 1 + i, by omega⟩ : Fin (n + m + 1)) :=
  lift_e _ _ _ _ _ _ _ i

theorem sh_incl (n m : ℕ) (x : TLFin K δ m) :
    sh δ n (m + 1) (incl δ m x) = incl δ (n + m + 1) (sh δ n m x) := by
  have : (sh δ n (m + 1)).comp (incl δ m) = (incl δ (n + m + 1)).comp (sh δ n m) :=
    hom_ext _ _ _ _ _ (fun i => by
      simp only [AlgHom.comp_apply, incl_e, sh_e]
      congr 1)
  exact AlgHom.congr_fun this x

theorem sh_last (n m : ℕ) :
    sh δ n (m + 1) (e K δ adjFin (Fin.last m)) = e K δ adjFin (Fin.last (n + m + 1)) := by
  rw [sh_e]; congr 1; ext; simp; omega

variable (δ A) in
/-- **The cable** of `b` parallel strands around the first `n + 1`:
`C_0 = 1`, `C_{b+1} = ι(C_b) · loop n b`. -/
noncomputable def cable (n : ℕ) : ∀ b : ℕ, TLFin K δ (n + b)
  | 0 => 1
  | b + 1 => incl δ (n + b) (cable n b) * loop δ A n b

/-- The top cap commutes with `ι(ι Z) · ι(loop n c) · loop n (c+1)`. -/
theorem top_commute (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) (n c : ℕ) (Z : TLFin K δ (n + c))
    : Commute (e K δ adjFin (Fin.last (n + c + 1)))
      (incl δ (n + c + 1) (incl δ (n + c) Z * loop δ A n c) * loop δ A n (c + 1)) := by
  have hZ := (incl_incl_commute δ (n + c) Z).symm
  rw [map_mul]
  show _ * _ = _ * _
  calc _ = incl δ (n + c + 1) (incl δ (n + c) Z) * (e K δ adjFin (Fin.last (n + c + 1)) *
        incl δ (n + c + 1) (loop δ A n c) * loop δ A n (c + 1)) := by
          simp only [mul_assoc]; rw [← mul_assoc _ (incl δ (n + c + 1) _), hZ.eq, mul_assoc]
    _ = incl δ (n + c + 1) (incl δ (n + c) Z) * (incl δ (n + c + 1) (loop δ A n c) *
        loop δ A n (c + 1) * e K δ adjFin (Fin.last (n + c + 1))) := by
          rw [cup_loop_loop hA hδ n c, loop_loop_cup hA hδ n c]
    _ = _ := by simp only [mul_assoc]

/-- **Naturality on the whole cable.** Every element of the cable algebra commutes with the
cable: `sh(x) · C_{m+1} = C_{m+1} · sh(x)`. -/
theorem sh_commute_cable (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) (n : ℕ) :
    ∀ (m : ℕ) (x : TLFin K δ m), Commute (sh δ n m x) (cable δ A n (m + 1)) := by
  intro m
  induction m with
  | zero => intro x; exact commute_of_gens _ _ (fun i => i.elim0) x
  | succ m ih =>
    intro x
    refine commute_of_gens _ _ (fun i => ?_) x
    rw [sh_e]
    show Commute _ (incl δ (n + m + 1) (cable δ A n (m + 1)) * loop δ A n (m + 1))
    by_cases hi : i.val < m
    · have hE : (e K δ adjFin (⟨n + 1 + i, by omega⟩ : Fin (n + (m + 1) + 1)))
          = incl δ (n + m + 1) (sh δ n m (e K δ adjFin (⟨i, hi⟩ : Fin m))) := by
        rw [sh_e, incl_e]; rfl
      refine Commute.mul_right ?_ ?_
      · rw [hE]; exact (ih _).map (incl δ (n + m + 1))
      · have := loop_comm_cable hA hδ n (m + 1) (i.val + 1) (by omega) (by omega)
        convert this using 3
        omega
    · have hE : (⟨n + 1 + i, by omega⟩ : Fin (n + (m + 1) + 1)) = Fin.last (n + m + 1) :=
        Fin.ext (by simp; omega)
      rw [hE]
      cases m with
      | zero => exact top_commute hA hδ n 0 (cable δ A n 0)
      | succ m =>
        exact top_commute hA hδ n (m + 1) (cable δ A n (m + 1))

end Cable

end QOU.HeckeTemperleyLieb.TLCable
