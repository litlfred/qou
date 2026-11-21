import UGB.GrobnerShirshov.QSerreCriticalPairs
import UGB.GrobnerShirshov.DiamondLemma
import Mathlib.Tactic.Module
import Mathlib.Tactic.FieldSimp

set_option linter.unusedSectionVars false

/-!
# The q-Serre system for `U_q(su(2))` is a Gröbner–Shirshov basis

`qSerre_is_gs_basis` was an axiom (`NormalForms.lean`), reduced by
`QSerreCriticalPairs.lean` to the eight overlap ambiguities whose overlap is a
single letter. This file resolves all eight and proves the statement.

The route is Shirshov's form of the composition lemma
(`Diamond.isGrobnerShirshovBasis_iff_compositionsTrivial`): for each overlap word
`a b c` it suffices to write the S-polynomial as a `k`-combination of rules in
context whose words lie strictly below `a b c`. Writing `Kᵢ = K⁻¹`,
`E = E_+`, `F = E_-`, `s = (q − q⁻¹)⁻¹` and `rᵢ` for the seven relations, the
eight expressions (derived by hand, checked here) are

| word | S-polynomial |
|---|---|
| `K Kᵢ K`  | `0` |
| `Kᵢ K Kᵢ` | `0` |
| `K Kᵢ E`  | `q⁻² r₃ Kᵢ + E r₁` |
| `K Kᵢ F`  | `q² r₄ Kᵢ + F r₁` |
| `Kᵢ K E`  | `q² r₆ K + E r₂` |
| `Kᵢ K F`  | `q⁻² r₇ K + F r₂` |
| `K E F`   | `r₄ E − q² E r₄ − r₅ K + q⁻² F r₃ + s (r₂ − r₁)` |
| `Kᵢ E F`  | `r₇ E − q⁻² E r₇ − r₅ Kᵢ + q² F r₆ + s (r₂ − r₁)` |

The scalar identities use only `q ≠ 0`.
-/

namespace UGB.GrobnerShirshov.QSerreGS

open UGB.GrobnerShirshov UGB.GrobnerShirshov.Diamond SU2Gen

universe v

variable {k : Type v} [Field k]

theorem toMA_two {m₁ m₂ : Monomial SU2Gen} (c₁ c₂ : k) (h : m₁ ≠ m₂) :
    toMA (two m₁ c₁ m₂ c₂ : AlgElement SU2Gen k) = c₁ • ofW m₁ + c₂ • ofW m₂ := by
  refine toMA_ext fun m => ?_
  rw [toMA_apply, Finsupp.add_apply, Finsupp.smul_apply, Finsupp.smul_apply, ofW_apply,
    ofW_apply]
  simp only [two, @eq_comm _ m₁ m, @eq_comm _ m₂ m]
  by_cases e1 : m = m₁
  · subst e1; simp [h]
  · by_cases e2 : m = m₂
    · subst e2; simp [Ne.symm h]
    · simp [e1, e2]

theorem toMA_four {m₁ m₂ m₃ m₄ : Monomial SU2Gen} (c₁ c₂ c₃ c₄ : k)
    (h12 : m₁ ≠ m₂) (h13 : m₁ ≠ m₃) (h14 : m₁ ≠ m₄) (h23 : m₂ ≠ m₃) (h24 : m₂ ≠ m₄)
    (h34 : m₃ ≠ m₄) :
    toMA (four m₁ c₁ m₂ c₂ m₃ c₃ m₄ c₄ : AlgElement SU2Gen k) =
      c₁ • ofW m₁ + c₂ • ofW m₂ + c₃ • ofW m₃ + c₄ • ofW m₄ := by
  refine toMA_ext fun m => ?_
  rw [toMA_apply, Finsupp.add_apply, Finsupp.add_apply, Finsupp.add_apply,
    Finsupp.smul_apply, Finsupp.smul_apply, Finsupp.smul_apply, Finsupp.smul_apply,
    ofW_apply, ofW_apply, ofW_apply, ofW_apply]
  simp only [four, @eq_comm _ m₁ m, @eq_comm _ m₂ m, @eq_comm _ m₃ m, @eq_comm _ m₄ m]
  by_cases e1 : m = m₁
  · subst e1; simp [h12, h13, h14]
  by_cases e2 : m = m₂
  · subst e2; simp [h23, h24, e1]
  by_cases e3 : m = m₃
  · subst e3; simp [h34, e1, e2]
  by_cases e4 : m = m₄
  · subst e4; simp [Ne.symm h14, Ne.symm h24, Ne.symm h34]
  · simp [e1, e2, e3, e4]

variable (qs : QSerreRelations k)

/-! ## §1  The seven relations in the monoid algebra -/

theorem r1 : toMA (qSerreRule1 (k := k)).relation = (1 : k) • ofW [K, K_inv] + (-1 : k) • ofW [] :=
  toMA_two _ _ (by simp)
theorem r2 : toMA (qSerreRule2 (k := k)).relation = (1 : k) • ofW [K_inv, K] + (-1 : k) • ofW [] :=
  toMA_two _ _ (by simp)
theorem r3 : toMA (qSerreRule3 qs).relation =
    (1 : k) • ofW [K, E_plus] + (-(qs.q ^ 2)) • ofW [E_plus, K] := toMA_two _ _ (by simp)
theorem r4 : toMA (qSerreRule4 qs).relation =
    (1 : k) • ofW [K, E_minus] + (-(qs.q ^ 2)⁻¹) • ofW [E_minus, K] := toMA_two _ _ (by simp)
theorem r5 : toMA (qSerreRule5 qs).relation =
    (1 : k) • ofW [E_plus, E_minus] + (-1 : k) • ofW [E_minus, E_plus]
      + (-(qs.q - qs.q⁻¹)⁻¹) • ofW [K] + ((qs.q - qs.q⁻¹)⁻¹) • ofW [K_inv] :=
  toMA_four _ _ _ _ (by simp) (by simp) (by simp) (by simp) (by simp) (by simp)
theorem r6 : toMA (qSerreRule6 qs).relation =
    (1 : k) • ofW [K_inv, E_plus] + (-(qs.q ^ 2)⁻¹) • ofW [E_plus, K_inv] := toMA_two _ _ (by simp)
theorem r7 : toMA (qSerreRule7 qs).relation =
    (1 : k) • ofW [K_inv, E_minus] + (-(qs.q ^ 2)) • ofW [E_minus, K_inv] := toMA_two _ _ (by simp)

/-! ## §2  Rules in context below a word -/

abbrev sys := qSerreRewritingSystem k qs

theorem site {r : ReductionRule SU2Gen k} (hr : r ∈ (sys qs).rules) (x y : Monomial SU2Gen)
    {v : Monomial SU2Gen} (hlt : degLexLt (x ++ r.lm degLexOrder ++ y) v) :
    JM degLexOrder (sys qs) v (ofW x * toMA r.relation * ofW y) :=
  JM.gen ⟨r, x, y⟩ hr hlt

theorem mem1 : qSerreRule1 ∈ (sys qs).rules := by simp [sys, qSerreRewritingSystem, qSerreRules]
theorem mem2 : qSerreRule2 ∈ (sys qs).rules := by simp [sys, qSerreRewritingSystem, qSerreRules]
theorem mem3 : qSerreRule3 qs ∈ (sys qs).rules := by simp [sys, qSerreRewritingSystem, qSerreRules]
theorem mem4 : qSerreRule4 qs ∈ (sys qs).rules := by simp [sys, qSerreRewritingSystem, qSerreRules]
theorem mem5 : qSerreRule5 qs ∈ (sys qs).rules := by simp [sys, qSerreRewritingSystem, qSerreRules]
theorem mem6 : qSerreRule6 qs ∈ (sys qs).rules := by simp [sys, qSerreRewritingSystem, qSerreRules]
theorem mem7 : qSerreRule7 qs ∈ (sys qs).rules := by simp [sys, qSerreRewritingSystem, qSerreRules]

/-! ## §3  The eight resolutions -/

/-- `K Kᵢ E`: `S = q⁻² r₃ Kᵢ + E r₁`. -/
theorem res_KKiE :
    JM degLexOrder (sys qs) [K, K_inv, E_plus]
      (toMA (qSerreRule1 (k := k)).relation * ofW [E_plus]
        - ofW [K] * toMA (qSerreRule6 qs).relation) := by
  have g1 := site qs (mem3 qs) [] [K_inv] (v := [K, K_inv, E_plus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have g2 := site qs (mem1 qs) [E_plus] [] (v := [K, K_inv, E_plus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have := (g1.smul (qs.q ^ 2)⁻¹).add g2
  convert this using 1
  have hq := qs.q_ne_zero
  rw [r1, r6, r3]
  simp only [mul_add, add_mul, mul_smul_comm, smul_mul_assoc, ← ofW_append,
    List.cons_append, List.nil_append, List.append_nil, smul_add, smul_smul]
  match_scalars <;> field_simp <;> ring

/-- `K Kᵢ F: S = q² r₄ Kᵢ + F r₁` -/
theorem res_KKiF :
    JM degLexOrder (sys qs) [K, K_inv, E_minus]
      (toMA (qSerreRule1 (k := k)).relation * ofW [E_minus]
        - ofW [K] * toMA (qSerreRule7 qs).relation) := by
  have g1 := site qs (mem4 qs) [] [K_inv] (v := [K, K_inv, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have g2 := site qs (mem1 qs) [E_minus] [] (v := [K, K_inv, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have := (g1.smul (qs.q ^ 2)).add g2
  convert this using 1
  have hq := qs.q_ne_zero
  rw [r1, r7, r4]
  simp only [mul_add, add_mul, mul_smul_comm, smul_mul_assoc, ← ofW_append,
    List.cons_append, List.nil_append, List.append_nil, smul_add, smul_smul]
  match_scalars <;> (try field_simp) <;> ring

/-- `Kᵢ K E: S = q² r₆ K + E r₂` -/
theorem res_KiKE :
    JM degLexOrder (sys qs) [K_inv, K, E_plus]
      (toMA (qSerreRule2 (k := k)).relation * ofW [E_plus]
        - ofW [K_inv] * toMA (qSerreRule3 qs).relation) := by
  have g1 := site qs (mem6 qs) [] [K] (v := [K_inv, K, E_plus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have g2 := site qs (mem2 qs) [E_plus] [] (v := [K_inv, K, E_plus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have := (g1.smul (qs.q ^ 2)).add g2
  convert this using 1
  have hq := qs.q_ne_zero
  rw [r2, r3, r6]
  simp only [mul_add, add_mul, mul_smul_comm, smul_mul_assoc, ← ofW_append,
    List.cons_append, List.nil_append, List.append_nil, smul_add, smul_smul]
  match_scalars <;> (try field_simp) <;> ring

/-- `Kᵢ K F: S = q⁻² r₇ K + F r₂` -/
theorem res_KiKF :
    JM degLexOrder (sys qs) [K_inv, K, E_minus]
      (toMA (qSerreRule2 (k := k)).relation * ofW [E_minus]
        - ofW [K_inv] * toMA (qSerreRule4 qs).relation) := by
  have g1 := site qs (mem7 qs) [] [K] (v := [K_inv, K, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have g2 := site qs (mem2 qs) [E_minus] [] (v := [K_inv, K, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have := (g1.smul (qs.q ^ 2)⁻¹).add g2
  convert this using 1
  have hq := qs.q_ne_zero
  rw [r2, r4, r7]
  simp only [mul_add, add_mul, mul_smul_comm, smul_mul_assoc, ← ofW_append,
    List.cons_append, List.nil_append, List.append_nil, smul_add, smul_smul]
  match_scalars <;> (try field_simp) <;> ring

/-- `K E F: S = r₄ E − q² E r₄ − r₅ K + q⁻² F r₃ + s (r₂ − r₁)` -/
theorem res_KEF :
    JM degLexOrder (sys qs) [K, E_plus, E_minus]
      (toMA (qSerreRule3 qs).relation * ofW [E_minus]
        - ofW [K] * toMA (qSerreRule5 qs).relation) := by
  have g1 := site qs (mem4 qs) [] [E_plus] (v := [K, E_plus, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have g2 := site qs (mem4 qs) [E_plus] [] (v := [K, E_plus, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have g3 := site qs (mem5 qs) [] [K] (v := [K, E_plus, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have g4 := site qs (mem3 qs) [E_minus] [] (v := [K, E_plus, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have g5 := site qs (mem2 qs) [] [] (v := [K, E_plus, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have g6 := site qs (mem1 qs) [] [] (v := [K, E_plus, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have := ((((g1.sub (g2.smul (qs.q ^ 2))).sub g3).add (g4.smul (qs.q ^ 2)⁻¹)).add
    ((g5.sub g6).smul (qs.q - qs.q⁻¹)⁻¹))
  convert this using 1
  have hq := qs.q_ne_zero
  rw [r3, r5, r4, r2, r1]
  simp only [mul_add, add_mul, mul_smul_comm, smul_mul_assoc, ← ofW_append,
    List.cons_append, List.nil_append, List.append_nil, smul_add, smul_smul]
  match_scalars <;> (try field_simp) <;> ring

/-- `Kᵢ E F: S = r₇ E − q⁻² E r₇ − r₅ Kᵢ + q² F r₆ + s (r₂ − r₁)` -/
theorem res_KiEF :
    JM degLexOrder (sys qs) [K_inv, E_plus, E_minus]
      (toMA (qSerreRule6 qs).relation * ofW [E_minus]
        - ofW [K_inv] * toMA (qSerreRule5 qs).relation) := by
  have g1 := site qs (mem7 qs) [] [E_plus] (v := [K_inv, E_plus, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have g2 := site qs (mem7 qs) [E_plus] [] (v := [K_inv, E_plus, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have g3 := site qs (mem5 qs) [] [K_inv] (v := [K_inv, E_plus, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have g4 := site qs (mem6 qs) [E_minus] [] (v := [K_inv, E_plus, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have g5 := site qs (mem2 qs) [] [] (v := [K_inv, E_plus, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have g6 := site qs (mem1 qs) [] [] (v := [K_inv, E_plus, E_minus])
    (by simp [degLexLt, lexLt, SU2Gen.rank])
  have := ((((g1.sub (g2.smul (qs.q ^ 2)⁻¹)).sub g3).add (g4.smul (qs.q ^ 2))).add
    ((g5.sub g6).smul (qs.q - qs.q⁻¹)⁻¹))
  convert this using 1
  have hq := qs.q_ne_zero
  rw [r6, r5, r7, r2, r1]
  simp only [mul_add, add_mul, mul_smul_comm, smul_mul_assoc, ← ofW_append,
    List.cons_append, List.nil_append, List.append_nil, smul_add, smul_smul]
  match_scalars <;> (try field_simp) <;> ring

/-- `K Kᵢ K`: the S-polynomial vanishes. -/
theorem res_KKiK :
    JM degLexOrder (sys qs) [K, K_inv, K]
      (toMA (qSerreRule1 (k := k)).relation * ofW [K]
        - ofW [K] * toMA (qSerreRule2 (k := k)).relation) := by
  convert (JM.zero : JM degLexOrder (sys qs) [K, K_inv, K] 0) using 1
  rw [r1, r2]
  simp only [add_mul, mul_add, mul_smul_comm, smul_mul_assoc, ← ofW_append,
    List.cons_append, List.nil_append, List.append_nil]
  module

/-- `Kᵢ K Kᵢ`: the S-polynomial vanishes. -/
theorem res_KiKKi :
    JM degLexOrder (sys qs) [K_inv, K, K_inv]
      (toMA (qSerreRule2 (k := k)).relation * ofW [K_inv]
        - ofW [K_inv] * toMA (qSerreRule1 (k := k)).relation) := by
  convert (JM.zero : JM degLexOrder (sys qs) [K_inv, K, K_inv] 0) using 1
  rw [r1, r2]
  simp only [add_mul, mul_add, mul_smul_comm, smul_mul_assoc, ← ofW_append,
    List.cons_append, List.nil_append, List.append_nil]
  module

/-! ## §4  All compositions are trivial -/

theorem qSerre_compositionsTrivial : CompositionsTrivial degLexOrder (sys qs) where
  overlap oc h₁ h₂ := by
    rcases qSerre_overlap_shape qs oc h₁ h₂ with ⟨hov, -, -⟩ | ⟨-, hl, hr⟩
    · obtain ⟨l1, l2, l3, l4, l5, l6, l7⟩ := qSerre_rule_lc_eq_one qs
      rw [toMA_spoly_ov]
      have hw : oc.word = oc.left ++ oc.overlap ++ oc.right := rfl
      rw [hw]
      rcases qSerre_overlap_enumeration qs oc h₁ h₂ hov with
        ⟨e1, e2, ea, eb, ec⟩ | ⟨e1, e2, ea, eb, ec⟩ | ⟨e1, e2, ea, eb, ec⟩ |
        ⟨e1, e2, ea, eb, ec⟩ | ⟨e1, e2, ea, eb, ec⟩ | ⟨e1, e2, ea, eb, ec⟩ |
        ⟨e1, e2, ea, eb, ec⟩ | ⟨e1, e2, ea, eb, ec⟩ <;>
      · rw [ea, eb, ec, e1, e2]
        simp only [l1, l2, l3, l4, l5, l6, l7, one_smul, List.cons_append, List.nil_append]
        first
          | exact res_KKiK qs | exact res_KKiE qs | exact res_KKiF qs | exact res_KiKKi qs
          | exact res_KiKE qs | exact res_KiKF qs | exact res_KEF qs | exact res_KiEF qs
    · have hlm : oc.rule₁.lm degLexOrder = oc.rule₂.lm degLexOrder := by
        rw [oc.lm₁_decomp, oc.lm₂_decomp, hl, hr]; simp
      rw [toMA_of_isZero (oc.spoly_isZero_of_self (qSerre_rule_eq_of_lm_eq qs h₁ h₂ hlm) hl hr)]
      exact JM.zero
  inclusion ic h₁ h₂ := by
    have hi := qSerre_lm_length qs _ h₁
    have ho := qSerre_lm_length qs _ h₂
    have hd := ic.decomposition
    have hl := congrArg List.length hd
    simp only [List.length_append, hi, ho] at hl
    have hleft : ic.left = [] := List.eq_nil_of_length_eq_zero (by omega)
    have hright : ic.right = [] := List.eq_nil_of_length_eq_zero (by omega)
    have hlm : ic.inner.lm degLexOrder = ic.outer.lm degLexOrder := by
      rw [hd, hleft, hright]; simp
    rw [toMA_of_isZero (ic.spoly_isZero_of_self (qSerre_rule_eq_of_lm_eq qs h₁ h₂ hlm))]
    exact JM.zero

end UGB.GrobnerShirshov.QSerreGS

namespace UGB.GrobnerShirshov

/-- **Theorem** (Bokut–Malcolmson 1996). The seven-rule `q`-Serre system is a
    Gröbner–Shirshov basis for `U_q(su(2))` under the deg-lex order.

    Formerly an axiom in `NormalForms.lean`; proved here from the eight explicit
    resolutions above via the composition lemma. Uses only `q ≠ 0`. -/
theorem qSerre_is_gs_basis (k : Type*) [Field k] (qs : QSerreRelations k) :
    IsGrobnerShirshovBasis SU2Gen k degLexOrder (qSerreRewritingSystem k qs) :=
  (Diamond.isGrobnerShirshovBasis_iff_compositionsTrivial (qSerre_rules_monic k qs)).mpr
    (QSerreGS.qSerre_compositionsTrivial qs)

end UGB.GrobnerShirshov
