import UGB.GrobnerShirshov.QSerreGS
import UGB.GrobnerShirshov.NormalFormBasisProof
import Mathlib.Data.List.Chain
import Mathlib.Data.List.Infix

set_option linter.unusedSectionVars false

/-!
# The PBW basis of `U_q(su(2))`

`qSerre_is_gs_basis` (`QSerreGS.lean`) says the seven q-Serre rules form a
Gröbner–Shirshov basis, and every rule is monic (`qSerre_rules_monic`). The
composition lemma (`NFBasis.normalFormBasis_of_isGrobnerShirshovBasis`) then
says the classes of the **normal words** — words containing no leading word of
a rule — are a `k`-basis of the quotient algebra. This file identifies those
normal words.

Writing `F = E_-`, `E = E_+`, `Kᵢ = K⁻¹`, the seven leading words are

    K Kᵢ,  Kᵢ K,  K E,  K F,  E F,  Kᵢ E,  Kᵢ F.

They are all two-letter words, so a word is normal iff every adjacent pair is
allowed (`qSerre_normal_iff_isChain`): after `K` only `K`, after `Kᵢ` only `Kᵢ`,
and `F` may not follow `E`. The allowed words are exactly

    F^c · E^a · K^n        (c, a ∈ ℕ, n ∈ ℤ),

where `K^n` means `Kᵢ^(-n)` for `n < 0` (`pbwWord`). The map
`(c, a, n) ↦ F^c E^a K^n` is a bijection onto the normal words
(`pbwEquiv`), so

**Theorem (`qSerre_pbw_basis`).** The elements `F^c E^a K^n`,
`(c, a, n) ∈ ℕ × ℕ × ℤ`, form a `k`-basis of `U_q(su(2))`.

Note the order: `F` first, then `E`, then the Cartan part. This is forced by
the rank order `E_- < E_+ < K⁻¹ < K` the rules are oriented by; the older
`PBWMonomial.toMonomial` in `NormalForms.lean` puts `E` first and is not a
normal word (`pbw_monomials_are_not_all_normal_forms`).

Nothing here is assumed: the basis is the conclusion of the composition lemma
applied to two proved facts.
-/

universe v

namespace UGB.GrobnerShirshov

open SU2Gen

/-- Adjacent pairs allowed in a q-Serre normal word. -/
def qSerreGood : SU2Gen → SU2Gen → Bool
  | K, K => true
  | K, _ => false
  | K_inv, K_inv => true
  | K_inv, _ => false
  | E_plus, E_minus => false
  | _, _ => true

/-- The Cartan part `K^n`, with `K^(-j-1) = Kᵢ^(j+1)`. -/
def kPow : ℤ → Monomial SU2Gen
  | Int.ofNat j => List.replicate j K
  | Int.negSucc j => List.replicate (j + 1) K_inv

/-- The PBW word `F^c E^a K^n`. -/
def pbwWord (c a : ℕ) (n : ℤ) : Monomial SU2Gen :=
  List.replicate c E_minus ++ List.replicate a E_plus ++ kPow n

section Normal

variable {k : Type v} [Field k]

/-- **Normal words are the chains of allowed pairs.** -/
theorem qSerre_normal_iff_isChain (qs : QSerreRelations k) (m : Monomial SU2Gen) :
    NormalFormMonomial degLexOrder (qSerreRewritingSystem k qs) m ↔
      m.IsChain (fun a b => qSerreGood a b = true) := by
  rw [List.isChain_iff_forall_rel_of_append_cons_cons]
  constructor
  · intro hn a b l₁ l₂ hm
    have hinf : [a, b] <:+: m := ⟨l₁, l₂, by rw [hm]; simp⟩
    by_contra hg
    cases a <;> cases b <;> simp [qSerreGood] at hg <;>
      first
      | exact hn qSerreRule1 (by simp [qSerreRewritingSystem, qSerreRules]) (by simpa using hinf)
      | exact hn qSerreRule2 (by simp [qSerreRewritingSystem, qSerreRules]) (by simpa using hinf)
      | exact hn (qSerreRule3 qs) (by simp [qSerreRewritingSystem, qSerreRules]) (by simpa using hinf)
      | exact hn (qSerreRule4 qs) (by simp [qSerreRewritingSystem, qSerreRules]) (by simpa using hinf)
      | exact hn (qSerreRule5 qs) (by simp [qSerreRewritingSystem, qSerreRules]) (by simpa using hinf)
      | exact hn (qSerreRule6 qs) (by simp [qSerreRewritingSystem, qSerreRules]) (by simpa using hinf)
      | exact hn (qSerreRule7 qs) (by simp [qSerreRewritingSystem, qSerreRules]) (by simpa using hinf)
  · intro hc r hr hinf
    simp only [qSerreRewritingSystem, qSerreRules, List.mem_cons, List.not_mem_nil,
      or_false] at hr
    obtain ⟨s, t, hst⟩ := hinf
    rcases hr with rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
      · simp only [qSerre_lm_1, qSerre_lm_2, qSerre_lm_3, qSerre_lm_4, qSerre_lm_5,
          qSerre_lm_6, qSerre_lm_7] at hst
        have := hc (l₁ := s) (l₂ := t)
          (by rw [← hst]; simp only [List.append_assoc, List.cons_append, List.nil_append]; rfl)
        simp [qSerreGood] at this

end Normal

/-- Every PBW word is a chain of allowed pairs. -/
theorem pbwWord_isChain (c a : ℕ) (n : ℤ) :
    (pbwWord c a n).IsChain (fun x y => qSerreGood x y = true) := by
  have hK : ∀ j, (List.replicate j K).IsChain (fun x y => qSerreGood x y = true) := by
    intro j; induction j with
    | zero => simp
    | succ j ih =>
      rw [List.replicate_succ, List.isChain_cons']
      refine ⟨?_, ih⟩
      cases j <;> simp [qSerreGood, List.replicate_succ]
  have hKi : ∀ j, (List.replicate j K_inv).IsChain (fun x y => qSerreGood x y = true) := by
    intro j; induction j with
    | zero => simp
    | succ j ih =>
      rw [List.replicate_succ, List.isChain_cons']
      refine ⟨?_, ih⟩
      cases j <;> simp [qSerreGood, List.replicate_succ]
  have hk : ∀ n, (kPow n).IsChain (fun x y => qSerreGood x y = true) := by
    intro n; cases n with
    | ofNat j => exact hK j
    | negSucc j => exact hKi (j + 1)
  have ha : ∀ a, (List.replicate a E_plus ++ kPow n).IsChain
      (fun x y => qSerreGood x y = true) := by
    intro a; induction a with
    | zero => simpa using hk n
    | succ a ih =>
      rw [List.replicate_succ, List.cons_append, List.isChain_cons']
      refine ⟨?_, ih⟩
      cases a with
      | succ a => simp [qSerreGood, List.replicate_succ]
      | zero =>
        cases n with
        | ofNat j => cases j <;> simp [kPow, qSerreGood, List.replicate_succ]
        | negSucc j => simp [kPow, qSerreGood, List.replicate_succ]
  unfold pbwWord
  induction c with
  | zero => simpa using ha a
  | succ c ih =>
    rw [List.replicate_succ, List.cons_append, List.cons_append, List.isChain_cons']
    refine ⟨?_, by simpa [List.append_assoc] using ih⟩
    intro y _
    cases y <;> rfl

/-- Every chain of allowed pairs is a PBW word. -/
theorem exists_pbwWord_of_isChain (m : Monomial SU2Gen)
    (h : m.IsChain (fun x y => qSerreGood x y = true)) :
    ∃ c a : ℕ, ∃ n : ℤ, m = pbwWord c a n := by
  induction m with
  | nil => exact ⟨0, 0, 0, rfl⟩
  | cons x l ih =>
    rw [List.isChain_cons'] at h
    obtain ⟨hx, hl⟩ := h
    obtain ⟨c, a, n, rfl⟩ := ih hl
    cases x with
    | E_minus => exact ⟨c + 1, a, n, by simp [pbwWord, List.replicate_succ]⟩
    | E_plus =>
      cases c with
      | succ c => simp [pbwWord, List.replicate_succ, qSerreGood] at hx
      | zero => exact ⟨0, a + 1, n, by simp [pbwWord, List.replicate_succ]⟩
    | K =>
      cases c with
      | succ c => simp [pbwWord, List.replicate_succ, qSerreGood] at hx
      | zero =>
        cases a with
        | succ a => simp [pbwWord, List.replicate_succ, qSerreGood] at hx
        | zero =>
          cases n with
          | ofNat j => exact ⟨0, 0, Int.ofNat (j + 1), by simp [pbwWord, kPow, List.replicate_succ]⟩
          | negSucc j => simp [pbwWord, kPow, List.replicate_succ, qSerreGood] at hx
    | K_inv =>
      cases c with
      | succ c => simp [pbwWord, List.replicate_succ, qSerreGood] at hx
      | zero =>
        cases a with
        | succ a => simp [pbwWord, List.replicate_succ, qSerreGood] at hx
        | zero =>
          cases n with
          | ofNat j =>
            cases j with
            | zero => exact ⟨0, 0, Int.negSucc 0, by simp [pbwWord, kPow]⟩
            | succ j => simp [pbwWord, kPow, List.replicate_succ, qSerreGood] at hx
          | negSucc j =>
            exact ⟨0, 0, Int.negSucc (j + 1), by simp [pbwWord, kPow, List.replicate_succ]⟩

/-- The exponents of a PBW word are recovered by counting letters. -/
theorem pbwWord_counts (c a : ℕ) (n : ℤ) :
    (pbwWord c a n).count E_minus = c ∧ (pbwWord c a n).count E_plus = a ∧
      ((pbwWord c a n).count K : ℤ) - (pbwWord c a n).count K_inv = n := by
  cases n with
  | ofNat j => simp [pbwWord, kPow, List.count_replicate]
  | negSucc j =>
    simp [pbwWord, kPow, List.count_replicate]
    omega

theorem pbwWord_injective {c a c' a' : ℕ} {n n' : ℤ}
    (h : pbwWord c a n = pbwWord c' a' n') : c = c' ∧ a = a' ∧ n = n' := by
  obtain ⟨h1, h2, h3⟩ := pbwWord_counts c a n
  obtain ⟨h1', h2', h3'⟩ := pbwWord_counts c' a' n'
  rw [h] at h1 h2 h3
  exact ⟨h1.symm.trans h1', h2.symm.trans h2', h3.symm.trans h3'⟩

section Basis

variable (k : Type v) [Field k] (qs : QSerreRelations k)

/-- `(c, a, n) ↦ F^c E^a K^n` is a bijection onto the normal words. -/
noncomputable def pbwEquiv :
    ℕ × ℕ × ℤ ≃ {m : Monomial SU2Gen //
      NormalFormMonomial degLexOrder (qSerreRewritingSystem k qs) m} where
  toFun p := ⟨pbwWord p.1 p.2.1 p.2.2,
    (qSerre_normal_iff_isChain qs _).2 (pbwWord_isChain _ _ _)⟩
  invFun m := (m.val.count E_minus, m.val.count E_plus,
    (m.val.count K : ℤ) - m.val.count K_inv)
  left_inv p := by
    obtain ⟨c, a, n⟩ := p
    obtain ⟨h1, h2, h3⟩ := pbwWord_counts c a n
    simp [h1, h2, h3]
  right_inv m := by
    obtain ⟨m, hm⟩ := m
    obtain ⟨c, a, n, rfl⟩ :=
      exists_pbwWord_of_isChain m ((qSerre_normal_iff_isChain qs m).1 hm)
    obtain ⟨h1, h2, h3⟩ := pbwWord_counts c a n
    apply Subtype.ext
    simp [h1, h2, h3]

/-- **The normal words of the q-Serre system are a `k`-basis of the quotient.** -/
theorem qSerre_normalFormBasis [DecidableEq k] :
    NormalFormBasis degLexOrder (qSerreRewritingSystem k qs) :=
  NFBasis.normalFormBasis_of_isGrobnerShirshovBasis
    (qSerre_is_gs_basis k qs) (qSerre_rules_monic k qs)

/-- **PBW theorem for `U_q(su(2))`.** The classes of `F^c E^a K^n`,
`(c, a, n) ∈ ℕ × ℕ × ℤ`, form a `k`-basis of the q-Serre quotient algebra. -/
theorem qSerre_pbw_basis [DecidableEq k] :
    ∃ B : Module.Basis (ℕ × ℕ × ℤ) k (QuotAlg (qSerreRewritingSystem k qs)),
      ∀ p : ℕ × ℕ × ℤ, B p = toQuot (qSerreRewritingSystem k qs)
        (FreeAlg.mk (AlgElement.single (pbwWord p.1 p.2.1 p.2.2) (1 : k))) := by
  obtain ⟨B, hB⟩ := qSerre_normalFormBasis k qs
  refine ⟨B.reindex (pbwEquiv k qs).symm, fun p => ?_⟩
  rw [Module.Basis.reindex_apply, Equiv.symm_symm, hB]
  rfl

end Basis

end UGB.GrobnerShirshov
