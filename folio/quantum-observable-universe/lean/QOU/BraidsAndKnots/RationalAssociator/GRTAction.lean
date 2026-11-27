import QOU.BraidsAndKnots.RationalAssociator.DrinfeldKohno
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NoncommRing

/-!
# The right action of `GRT` on associators, and the pentagon

Bean `qou-3fdg` (stage 3b of the rational-associator plan, epic `qou-dk7p`).

Drinfeld (1991, p. 852, after Remark 3) lets `GRT₁` act on the right on associators by
`φ̃(A, B) = φ(g A g⁻¹, B) · g(A, B)` (in Furusho 2010, Lemma 8, this is `φ ∘ g`).
Since `φ(G a G⁻¹, b) = G · φ(a, G⁻¹ b G) · G⁻¹`, the evaluation at a pair is
`φ̃(a, b) = G · φ(a, G⁻¹ b G)` with `G = g(a, b)`.

The free algebra `ℚ⟨X, Y⟩` has no inverse of `g`, so this file works with evaluations: `G`
is a unit of `R` equal to `g(a, b)`, and `actEval φ a b G = φ(G a G⁻¹, b) · G`.

## What is proved

`pentagon_act`: let `t` be a Drinfeld–Kohno family on four strands and let the five coface
evaluations of `g` be units. If

* (`hg`) `g` satisfies the pentagon at `t`, and
* (`hφ`) `φ` satisfies the pentagon at the **transported family** `s` (`transported`),

then `φ̃` satisfies the pentagon at `t`. The transported family is `t` rewritten in
`((12)3)4` coordinates along the associativity constraints of `g`:

* `s₁₂ = t₁₂`,  `s₂₃ = G₁₂₃⁻¹ t₂₃ G₁₂₃`,  `s₁₃ = t₁₃ + t₂₃ − s₂₃`,
* `s₃₄ = G_{12,3,4}⁻¹ t₃₄ G_{12,3,4}`,  `s₂₄ = P⁻¹ (t₂₃ + t₂₄) P − s₂₃`, `P = G_{1,2,34} G_{12,3,4}`.

`dk3_twist`, `transported_d4` and `transported_d0` show that the three-strand cofaces
`{1,2,3}` and `{2,3,4}` of `s` are again Drinfeld–Kohno (the second uses the pentagon of `g`).

## What is not proved here

`hφ` is a hypothesis at `s`, not at `t`. To discharge it from "φ satisfies the pentagon at every
`DK4` family" one needs `s` (with a suitable `s₁₄`) to be a `DK4` family. The five coface
triples of a family span only 10 of the 11 independent degree-2 Drinfeld–Kohno relations; the
missing one is the far relation `[s₁₃, s₂₄] = 0`, which is not proved here. See
`docs/audits/2026-11-27-grt-action-pentagon-derivation.md`. Nothing analytic is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

variable {R : Type*} [Ring R] [Algebra ℚ R]

/-- An evaluation of `p ∈ ℚ⟨X, Y⟩` commutes with everything both arguments commute with. -/
theorem commute_eval {a b x : R} (ha : Commute a x) (hb : Commute b x)
    (p : FreeAlgebra ℚ (Fin 2)) : Commute (eval a b p) x := by
  induction p using FreeAlgebra.induction with
  | grade0 r => simpa using Algebra.commutes r x
  | grade1 i => fin_cases i <;> simpa [eval] using (by assumption : Commute _ x)
  | mul p q hp hq => simpa [map_mul] using hp.mul_left hq
  | add p q hp hq => simpa [map_add] using hp.add_left hq

/-- Evaluation commutes with conjugation by a unit. -/
theorem eval_conj (u : Rˣ) (a b : R) (p : FreeAlgebra ℚ (Fin 2)) :
    eval ((↑u⁻¹ : R) * a * u) ((↑u⁻¹ : R) * b * u) p = (↑u⁻¹ : R) * eval a b p * u := by
  induction p using FreeAlgebra.induction with
  | grade0 r =>
    simp only [AlgHom.commutes]
    rw [mul_assoc, Algebra.commutes r (u : R), Units.inv_mul_cancel_left]
  | grade1 i => fin_cases i <;> simp [eval]
  | mul p q hp hq =>
    rw [map_mul, hp, hq, map_mul]
    simp only [mul_assoc, Units.mul_inv_cancel_left]
  | add p q hp hq => rw [map_add, hp, hq, map_add, mul_add, add_mul]

omit [Algebra ℚ R] in
/-- Conjugating by a unit that commutes with `x` fixes `x`. -/
theorem conj_of_commute {u : Rˣ} {x : R} (h : Commute (u : R) x) :
    (↑u⁻¹ : R) * x * u = x := by
  rw [mul_assoc, ← h.eq, Units.inv_mul_cancel_left]

omit [Algebra ℚ R] in
/-- Conjugating by `v * w`, with `v` commuting with `x`, is conjugating by `w`. -/
theorem conj_mul_of_commute {v w : Rˣ} {x : R} (h : Commute (v : R) x) :
    (↑(v * w)⁻¹ : R) * x * ↑(v * w) = (↑w⁻¹ : R) * x * w := by
  have : (↑(v * w)⁻¹ : R) * x * ↑(v * w) = (↑w⁻¹ : R) * ((↑v⁻¹ : R) * x * v) * w := by
    simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
  rw [this, conj_of_commute h]

/-- The right action `φ̃ = φ ∘ g` at a pair, with `G = g(a, b)` supplied as a unit:
`φ̃(a, b) = φ(G a G⁻¹, b) · G` (Drinfeld 1991, p. 852). -/
noncomputable def actEval (φ : FreeAlgebra ℚ (Fin 2)) (a b : R) (G : Rˣ) : R :=
  eval ((G : R) * a * ↑G⁻¹) b φ * G

/-- `φ(G a G⁻¹, b) · G = G · φ(a, G⁻¹ b G)`. -/
theorem actEval_eq (φ : FreeAlgebra ℚ (Fin 2)) (a b : R) (G : Rˣ) :
    actEval φ a b G = (G : R) * eval a ((↑G⁻¹ : R) * b * G) φ := by
  have h := eval_conj G⁻¹ a ((↑G⁻¹ : R) * b * G) φ
  simp only [inv_inv] at h
  have hb : (G : R) * ((↑G⁻¹ : R) * b * G) * ↑G⁻¹ = b := by
    simp only [mul_assoc, Units.mul_inv_cancel_left, Units.mul_inv, mul_one]
  rw [hb] at h
  unfold actEval
  rw [h]
  simp only [mul_assoc, Units.inv_mul, mul_one]

/-- The family `t` transported to `((12)3)4` coordinates along the constraints of `g`
(given here by the units `Ga = g(t₁₂, t₂₃)`, `Gb = g(t₁₃ + t₂₃, t₃₄)`, `Gc = g(t₁₂, t₂₃ + t₂₄)`).
Returns `(s₁₂, s₁₃, s₂₃, s₂₄, s₃₄)`. -/
noncomputable def transported (t12 t13 t23 t24 t34 : R) (Ga Gb Gc : Rˣ) : R × R × R × R × R :=
  let s23 := (↑Ga⁻¹ : R) * t23 * Ga
  (t12, t13 + t23 - s23, s23,
    (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) - s23, (↑Gb⁻¹ : R) * t34 * Gb)

/-- **Pentagon preservation under the `GRT` action (conditional on the transported family).**
If `g` satisfies the pentagon at a `DK4` family `t` (its five coface evaluations being the units
`Ga … Ge`), and `φ` satisfies the pentagon at the transported family `s`, then
`φ̃(A, B) = φ(g A g⁻¹, B) · g` satisfies the pentagon at `t`. -/
theorem pentagon_act (φ g : FreeAlgebra ℚ (Fin 2)) {t12 t13 t14 t23 t24 t34 : R}
    (hDK : DK4 t12 t13 t14 t23 t24 t34) (Ga Gb Gc Gd Ge : Rˣ)
    (ha : (Ga : R) = eval t12 t23 g) (hb : (Gb : R) = eval (t13 + t23) t34 g)
    (hc : (Gc : R) = eval t12 (t23 + t24) g) (hd : (Gd : R) = eval (t12 + t13) (t24 + t34) g)
    (he : (Ge : R) = eval t23 t34 g)
    (hg : Pentagon g t12 t13 t23 t24 t34)
    (hφ : let s := transported t12 t13 t23 t24 t34 Ga Gb Gc
      Pentagon φ s.1 s.2.1 s.2.2.1 s.2.2.2.1 s.2.2.2.2) :
    actEval φ t12 (t23 + t24) Gc * actEval φ (t13 + t23) t34 Gb =
      actEval φ t23 t34 Ge * actEval φ (t12 + t13) (t24 + t34) Gd * actEval φ t12 t23 Ga := by
  -- the units' pentagon `Gc Gb = Ge Gd Ga`
  have hP : Gc * Gb = Ge * Gd * Ga := by
    ext; simp only [Units.val_mul]; rw [ha, hb, hc, hd, he]; exact hg
  -- commutation facts, all from `DK4`
  have cb12 : Commute (Gb : R) t12 := hb ▸ commute_eval hDK.n12_3.symm hDK.f12_34.symm g
  have cc34 : Commute (Gc : R) t34 :=
    hc ▸ commute_eval hDK.f12_34 hDK.n34_2.symm g
  have cd23 : Commute (Gd : R) t23 :=
    hd ▸ commute_eval hDK.n23_1.symm hDK.n23_4.symm g
  have ca3 : Commute (Ga : R) (t12 + t13 + t23) := by
    rw [ha]
    refine commute_eval ?_ ?_ g
    · have := hDK.n12_3; rw [show t12 + t13 + t23 = t12 + (t13 + t23) by abel]
      exact (Commute.refl t12).add_right this
    · have := hDK.n23_1; rw [show t12 + t13 + t23 = (t12 + t13) + t23 by abel]
      exact this.add_right (Commute.refl t23)
  have ce3 : Commute (Ge : R) (t23 + t24 + t34) := by
    rw [he]
    refine commute_eval ?_ ?_ g
    · rw [show t23 + t24 + t34 = t23 + (t24 + t34) by abel]
      exact (Commute.refl t23).add_right hDK.n23_4
    · rw [show t23 + t24 + t34 = (t23 + t24) + t34 by abel]
      exact hDK.n34_2.add_right (Commute.refl t34)
  have hP' : Gc * Gb = Ge * (Gd * Ga) := by rw [hP, mul_assoc]
  have F1 : (↑(Gc * Gb)⁻¹ : R) * t34 * ↑(Gc * Gb) = (↑Gb⁻¹ : R) * t34 * Gb :=
    conj_mul_of_commute cc34
  have F2 : (↑(Gd * Ga)⁻¹ : R) * t23 * ↑(Gd * Ga) = (↑Ga⁻¹ : R) * t23 * Ga :=
    conj_mul_of_commute cd23
  have F3 : (↑(Gc * Gb)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gc * Gb) =
      (↑(Gd * Ga)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gd * Ga) := by
    rw [hP']; exact conj_mul_of_commute ce3
  simp only [transported, Pentagon] at hφ
  have k1 : ∀ x y : R, x + (y - x) = y := fun x y => by abel
  have k2 : ∀ x y : R, y - x + x = y := fun x y => by abel
  rw [k1, k2] at hφ
  -- the five factors, rewritten
  have eL1 : (↑Gb⁻¹ : R) * eval t12 ((↑Gc⁻¹ : R) * (t23 + t24) * Gc) φ * Gb =
      eval t12 ((↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb)) φ := by
    have a2 : (↑Gb⁻¹ : R) * ((↑Gc⁻¹ : R) * (t23 + t24) * Gc) * Gb =
        (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) := by
      simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
    rw [← eval_conj, conj_of_commute cb12, a2]
  have eR1 : (↑(Gd * Ga)⁻¹ : R) * eval t23 ((↑Ge⁻¹ : R) * t34 * Ge) φ * ↑(Gd * Ga) =
      eval ((↑Ga⁻¹ : R) * t23 * Ga) ((↑Gb⁻¹ : R) * t34 * Gb) φ := by
    have a2 : (↑(Gd * Ga)⁻¹ : R) * ((↑Ge⁻¹ : R) * t34 * Ge) * ↑(Gd * Ga) =
        (↑Gb⁻¹ : R) * t34 * Gb := by
      rw [← F1, hP']; simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
    rw [← eval_conj, F2, a2]
  have eR2 : (↑Ga⁻¹ : R) * eval (t12 + t13) ((↑Gd⁻¹ : R) * (t24 + t34) * Gd) φ * Ga =
      eval (t12 + (t13 + t23 - (↑Ga⁻¹ : R) * t23 * Ga))
        ((↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) - (↑Ga⁻¹ : R) * t23 * Ga +
          (↑Gb⁻¹ : R) * t34 * Gb) φ := by
    have a1 : (↑Ga⁻¹ : R) * (t12 + t13) * Ga = t12 + (t13 + t23 - (↑Ga⁻¹ : R) * t23 * Ga) := by
      have : (↑Ga⁻¹ : R) * (t12 + t13) * Ga =
          (↑Ga⁻¹ : R) * (t12 + t13 + t23) * Ga - (↑Ga⁻¹ : R) * t23 * Ga := by noncomm_ring
      rw [this, conj_of_commute ca3]; abel
    have a2 : (↑Ga⁻¹ : R) * ((↑Gd⁻¹ : R) * (t24 + t34) * Gd) * Ga =
        (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) - (↑Ga⁻¹ : R) * t23 * Ga +
          (↑Gb⁻¹ : R) * t34 * Gb := by
      have b1 : (↑Ga⁻¹ : R) * ((↑Gd⁻¹ : R) * (t24 + t34) * Gd) * Ga =
          (↑(Gd * Ga)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gd * Ga) -
            (↑(Gd * Ga)⁻¹ : R) * t23 * ↑(Gd * Ga) := by
        simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
      have b2 : (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) =
          (↑(Gc * Gb)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gc * Gb) -
            (↑(Gc * Gb)⁻¹ : R) * t34 * ↑(Gc * Gb) := by noncomm_ring
      rw [b1, b2, F3, F2, F1]; abel
    rw [← eval_conj, a1, a2]
  -- assemble
  simp only [actEval_eq]
  have lhs : (Gc : R) * eval t12 ((↑Gc⁻¹ : R) * (t23 + t24) * Gc) φ *
      ((Gb : R) * eval (t13 + t23) ((↑Gb⁻¹ : R) * t34 * Gb) φ) =
      ↑(Gc * Gb) * ((↑Gb⁻¹ : R) * eval t12 ((↑Gc⁻¹ : R) * (t23 + t24) * Gc) φ * Gb) *
        eval (t13 + t23) ((↑Gb⁻¹ : R) * t34 * Gb) φ := by
    simp only [Units.val_mul, mul_assoc, Units.mul_inv_cancel_left]
  have rhs : (Ge : R) * eval t23 ((↑Ge⁻¹ : R) * t34 * Ge) φ *
      ((Gd : R) * eval (t12 + t13) ((↑Gd⁻¹ : R) * (t24 + t34) * Gd) φ) *
      ((Ga : R) * eval t12 ((↑Ga⁻¹ : R) * t23 * Ga) φ) =
      ↑(Ge * (Gd * Ga)) *
        ((↑(Gd * Ga)⁻¹ : R) * eval t23 ((↑Ge⁻¹ : R) * t34 * Ge) φ * ↑(Gd * Ga)) *
        ((↑Ga⁻¹ : R) * eval (t12 + t13) ((↑Gd⁻¹ : R) * (t24 + t34) * Gd) φ * Ga) *
        eval t12 ((↑Ga⁻¹ : R) * t23 * Ga) φ := by
    simp only [mul_inv_rev, Units.val_mul, mul_assoc, Units.mul_inv_cancel_left]
  rw [lhs, rhs, eL1, eR1, eR2, ← hP', mul_assoc, hφ]
  simp only [mul_assoc]

omit [Algebra ℚ R] in
/-- Conjugation by a unit preserves commuting pairs. -/
theorem Commute.unitsConj {a b : R} (u : Rˣ) (h : Commute a b) :
    Commute ((↑u⁻¹ : R) * a * u) ((↑u⁻¹ : R) * b * u) := by
  unfold Commute SemiconjBy
  simp only [mul_assoc, Units.mul_inv_cancel_left]
  rw [← mul_assoc a b, h.eq, mul_assoc]

omit [Algebra ℚ R] in
/-- Conjugation by a unit preserves `DK3` families. -/
theorem DK3.unitsConj {a b c : R} (u : Rˣ) (h : DK3 a b c) :
    DK3 ((↑u⁻¹ : R) * a * u) ((↑u⁻¹ : R) * b * u) ((↑u⁻¹ : R) * c * u) := by
  have hadd : ∀ x y : R, (↑u⁻¹ : R) * x * u + (↑u⁻¹ : R) * y * u = (↑u⁻¹ : R) * (x + y) * u :=
    fun x y => by noncomm_ring
  refine ⟨?_, ?_, ?_⟩ <;> rw [hadd]
  · exact Commute.unitsConj u h.n12_3
  · exact Commute.unitsConj u h.n13_2
  · exact Commute.unitsConj u h.n23_1

omit [Algebra ℚ R] in
/-- **Twisting a three-strand family.** If `(x, y, z)` is a `DK3` family and the unit `G`
commutes with the total `x + y + z`, then `(x, y + z − G⁻¹zG, G⁻¹zG)` is a `DK3` family. -/
theorem dk3_twist {x y z : R} (h : DK3 x y z) (G : Rˣ) (hG : Commute (G : R) (x + y + z)) :
    DK3 x (y + z - (↑G⁻¹ : R) * z * G) ((↑G⁻¹ : R) * z * G) := by
  set z' := (↑G⁻¹ : R) * z * G
  have hx : Commute x (x + y + z) := by
    rw [show x + y + z = x + (y + z) by abel]; exact (Commute.refl x).add_right h.n12_3
  have hy : Commute y (x + y + z) := by
    rw [show x + y + z = y + (x + z) by abel]; exact (Commute.refl y).add_right h.n13_2
  have hz : Commute z (x + y + z) := by
    rw [show x + y + z = z + (x + y) by abel]; exact (Commute.refl z).add_right h.n23_1
  have hz' : Commute z' (x + y + z) := by
    have := Commute.unitsConj G hz; rwa [conj_of_commute hG] at this
  have hy' : Commute (y + z - z') (x + y + z) := (hy.add_left hz).sub_left hz'
  refine ⟨?_, ?_, ?_⟩
  · rw [show y + z - z' + z' = y + z by abel]; exact h.n12_3
  · rw [show x + z' = x + y + z - (y + z - z') by abel]
    exact hy'.sub_right (Commute.refl _)
  · rw [show x + (y + z - z') = x + y + z - z' by abel]
    exact hz'.sub_right (Commute.refl _)

/-- The `{1, 2, 3}` coface of the transported family is a `DK3` family. -/
theorem transported_d4 (g : FreeAlgebra ℚ (Fin 2)) {t12 t13 t23 : R} (h : DK3 t12 t13 t23)
    (Ga Gb Gc : Rˣ) (ha : (Ga : R) = eval t12 t23 g) (t24 t34 : R) :
    let s := transported t12 t13 t23 t24 t34 Ga Gb Gc
    DK3 s.1 s.2.1 s.2.2.1 := by
  have hc : Commute (Ga : R) (t12 + t13 + t23) := by
    rw [ha]
    refine commute_eval ?_ ?_ g
    · rw [show t12 + t13 + t23 = t12 + (t13 + t23) by abel]
      exact (Commute.refl t12).add_right h.n12_3
    · rw [show t12 + t13 + t23 = (t12 + t13) + t23 by abel]
      exact h.n23_1.add_right (Commute.refl t23)
  exact dk3_twist h Ga hc

/-- The `{2, 3, 4}` coface of the transported family is a `DK3` family: it is the conjugate by
`G_{1,23,4} G_{1,2,3}` of the twist of `(t₂₃, t₂₄, t₃₄)` by `G_{2,3,4}`. Uses the pentagon for
`g` at `t`. -/
theorem transported_d0 (g : FreeAlgebra ℚ (Fin 2)) {t12 t13 t14 t23 t24 t34 : R}
    (hDK : DK4 t12 t13 t14 t23 t24 t34) (Ga Gb Gc Gd Ge : Rˣ)
    (ha : (Ga : R) = eval t12 t23 g) (hb : (Gb : R) = eval (t13 + t23) t34 g)
    (hc : (Gc : R) = eval t12 (t23 + t24) g) (hd : (Gd : R) = eval (t12 + t13) (t24 + t34) g)
    (he : (Ge : R) = eval t23 t34 g)
    (hg : Pentagon g t12 t13 t23 t24 t34) :
    let s := transported t12 t13 t23 t24 t34 Ga Gb Gc
    DK3 s.2.2.1 s.2.2.2.1 s.2.2.2.2 := by
  have hP' : Gc * Gb = Ge * (Gd * Ga) := by
    ext; simp only [Units.val_mul]; rw [ha, hb, hc, hd, he, ← mul_assoc]; exact hg
  have cc34 : Commute (Gc : R) t34 := hc ▸ commute_eval hDK.f12_34 hDK.n34_2.symm g
  have cd23 : Commute (Gd : R) t23 := hd ▸ commute_eval hDK.n23_1.symm hDK.n23_4.symm g
  have ce3 : Commute (Ge : R) (t23 + t24 + t34) := by
    rw [he]
    refine commute_eval ?_ ?_ g
    · rw [show t23 + t24 + t34 = t23 + (t24 + t34) by abel]
      exact (Commute.refl t23).add_right hDK.n23_4
    · rw [show t23 + t24 + t34 = (t23 + t24) + t34 by abel]
      exact hDK.n34_2.add_right (Commute.refl t34)
  have key := (dk3_twist hDK.d0 Ge ce3).unitsConj (Gd * Ga)
  have F1 : (↑(Gc * Gb)⁻¹ : R) * t34 * ↑(Gc * Gb) = (↑Gb⁻¹ : R) * t34 * Gb :=
    conj_mul_of_commute cc34
  have F2 : (↑(Gd * Ga)⁻¹ : R) * t23 * ↑(Gd * Ga) = (↑Ga⁻¹ : R) * t23 * Ga :=
    conj_mul_of_commute cd23
  have F3 : (↑(Gc * Gb)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gc * Gb) =
      (↑(Gd * Ga)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gd * Ga) := by
    rw [hP']; exact conj_mul_of_commute ce3
  have e3 : (↑(Gd * Ga)⁻¹ : R) * ((↑Ge⁻¹ : R) * t34 * Ge) * ↑(Gd * Ga) =
      (↑Gb⁻¹ : R) * t34 * Gb := by
    rw [← F1, hP']; simp only [mul_inv_rev, Units.val_mul]; noncomm_ring
  have e2 : (↑(Gd * Ga)⁻¹ : R) * (t24 + t34 - (↑Ge⁻¹ : R) * t34 * Ge) * ↑(Gd * Ga) =
      (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) - (↑Ga⁻¹ : R) * t23 * Ga := by
    have b1 : (↑(Gd * Ga)⁻¹ : R) * (t24 + t34 - (↑Ge⁻¹ : R) * t34 * Ge) * ↑(Gd * Ga) =
        (↑(Gd * Ga)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gd * Ga) -
          (↑(Gd * Ga)⁻¹ : R) * t23 * ↑(Gd * Ga) -
          (↑(Gd * Ga)⁻¹ : R) * ((↑Ge⁻¹ : R) * t34 * Ge) * ↑(Gd * Ga) := by noncomm_ring
    have b2 : (↑(Gc * Gb)⁻¹ : R) * (t23 + t24) * ↑(Gc * Gb) =
        (↑(Gc * Gb)⁻¹ : R) * (t23 + t24 + t34) * ↑(Gc * Gb) -
          (↑(Gc * Gb)⁻¹ : R) * t34 * ↑(Gc * Gb) := by noncomm_ring
    rw [b1, b2, e3, F3, F2, F1]; abel
  rw [F2, e2, e3] at key
  exact key

end QOU.BraidsAndKnots.RationalAssociator
