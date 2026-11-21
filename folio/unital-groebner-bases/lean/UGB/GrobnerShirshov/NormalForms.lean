import UGB.GrobnerShirshov.CompositionLemma
import Mathlib.Data.Nat.Prime.Defs
import Mathlib.Data.List.Lex
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# Normal Forms and PBW-Type Bases

This module specialises the abstract Gröbner–Shirshov framework of
`Basic.lean` and `CompositionLemma.lean` to the two concrete algebras
appearing in the QOU manuscript:

1. **`U_q(su(2))`** — the quantum group with `q`-Serre relations.
   The GS basis yields the Lusztig divided-power (PBW) basis
   `{E_+^a · K^b · E_-^c : a,b,c ≥ 0}`.

2. **`Dist(G)`** — the distribution algebra of a non-commutative
   formal group over `ℤ_p`.  The GS basis yields the flat deformation
   of `Dist(H)` from [fred2005, §3].

## Key results

- `qSerre_is_gs_basis`: the `q`-Serre relations form a GS basis
  under the deg-lex order on `{E_+, K, K⁻¹, E_-}`. Proved in `QSerreGS.lean`
  (it was an axiom in this file until 2026-11-21).
- `pbw_monomials_are_normal_forms`: PBW monomials are exactly the
  normal-form monomials under the `q`-Serre rewriting system.
- `dist_algebra_gs_basis` (removed 2026-11-15, it was false as stated; see §5).

## References

- [fred2005, §3, Proposition 3.8]
- Lusztig, *Introduction to Quantum Groups*, Birkhäuser 1993, Ch. 3.
- Bokut & Malcolmson, *Gröbner–Shirshov bases for quantum enveloping
  algebras*, Israel J. Math. 96 (1996), 97–113.
-/


namespace UGB.GrobnerShirshov

universe u v

/-! ## §1  Generators of `U_q(su(2))` -/

/-- The four generators of the quantum group `U_q(su(2))`. -/
inductive SU2Gen where
  | E_plus   -- raising operator E_+
  | E_minus  -- lowering operator E_-
  | K        -- Cartan element K
  | K_inv    -- Cartan inverse K⁻¹
  deriving DecidableEq, Repr

open SU2Gen

/-- Numeric rank of each generator for the lexicographic order:
    `E_- < E_+ < K_inv < K` (ascending).

    **Corrected twice, both times because the rules constrain it and nothing
    was checking.**

    * qou-ix9e: originally `K = 2 < E_+ = 3`, which made rule 3's leading
      monomial `[E_+, K]` — its own right-hand side — so the system rewrote in
      the direction opposite to the one its docstring claimed.
    * qou-18s7: the five-rule system turned out not to be a Gröbner–Shirshov
      basis at all (see §3), and completing it adds the two `K⁻¹` commutation
      rules, which impose two further constraints that the previous ranking
      violated.

    The five orientation constraints, one per non-inverse rule:

    | rule | needs |
    |---|---|
    | 3 `K·E_+ → q²·E_+·K` | `rank K > rank E_+` |
    | 4 `K·E_- → q⁻²·E_-·K` | `rank K > rank E_-` |
    | 5 `E_+·E_- → E_-·E_+ + …` | `rank E_+ > rank E_-` |
    | 6 `K⁻¹·E_+ → q⁻²·E_+·K⁻¹` | `rank K_inv > rank E_+` |
    | 7 `K⁻¹·E_- → q²·E_-·K⁻¹` | `rank K_inv > rank E_-` |

    Rules 1 and 2 constrain nothing: their leading monomials beat `[]` on
    length. This ranking satisfies all five, and `qSerre_lm_1 … qSerre_lm_7`
    prove every leading monomial outright, so the orientation is checked rather
    than asserted. -/
def SU2Gen.rank : SU2Gen → ℕ
  | E_minus => 0
  | E_plus  => 1
  | K_inv   => 2
  | K       => 3

theorem SU2Gen.rank_injective : ∀ a b : SU2Gen, a.rank = b.rank → a = b := by
  intro a b
  cases a <;> cases b <;> simp [SU2Gen.rank]

/-- Lexicographic comparison of monomials (lists of generators) using
    the rank function.  Compares element-wise left-to-right; shorter
    lists are smaller when one is a prefix of the other. -/
def lexLt : Monomial SU2Gen → Monomial SU2Gen → Prop
  | [], [] => False
  | [], (_ :: _) => True
  | (_ :: _), [] => False
  | (a :: as), (b :: bs) =>
    a.rank < b.rank ∨ (a.rank = b.rank ∧ lexLt as bs)

/-- The **deg-lex order** on monomials in `{E_+, K, K⁻¹, E_-}`:
    first compare by total degree (word length), then lexicographically
    using the rank ordering `E_- < K⁻¹ < K < E_+`.

    This is the standard admissible order for quantum group
    Gröbner–Shirshov computations. -/
def degLexLt (a b : Monomial SU2Gen) : Prop :=
  a.length < b.length ∨ (a.length = b.length ∧ lexLt a b)

theorem lexLt_irrefl : ∀ (a : Monomial SU2Gen), ¬ lexLt a a := by
  intro a
  induction a with
  | nil => simp [lexLt]
  | cons x xs ih =>
    simp [lexLt]
    intro h
    exact ih h

theorem lexLt_trans : ∀ (a b c : Monomial SU2Gen),
    lexLt a b → lexLt b c → lexLt a c := by
  intro a
  induction a with
  | nil =>
    intro b c _ hbc
    cases c with
    | nil =>
      cases b with
      | nil => exact hbc
      | cons _ _ => simp [lexLt] at hbc
    | cons _ _ => exact True.intro
  | cons x xs ih =>
    intro b c hab hbc
    cases b with
    | nil => simp [lexLt] at hab
    | cons y ys =>
      cases c with
      | nil => simp [lexLt] at hbc
      | cons z zs =>
        simp [lexLt] at hab hbc ⊢
        cases hab with
        | inl hxy =>
          cases hbc with
          | inl hyz => left; exact Nat.lt_trans hxy hyz
          | inr hyz => left; exact hyz.1 ▸ hxy
        | inr hxy =>
          cases hbc with
          | inl hyz => left; exact hxy.1 ▸ hyz
          | inr hyz =>
            right; exact ⟨hxy.1.trans hyz.1, ih ys zs hxy.2 hyz.2⟩

theorem lexLt_trichotomy : ∀ (a b : Monomial SU2Gen),
    lexLt a b ∨ a = b ∨ lexLt b a := by
  intro a
  induction a with
  | nil =>
    intro b
    cases b with
    | nil => right; left; rfl
    | cons _ _ => left; exact True.intro
  | cons x xs ih =>
    intro b
    cases b with
    | nil => right; right; exact True.intro
    | cons y ys =>
      simp [lexLt]
      by_cases hxy : x.rank < y.rank
      · left; left; exact hxy
      · by_cases hyx : y.rank < x.rank
        · right; right; left; exact hyx
        · have heq : x.rank = y.rank := Nat.le_antisymm (Nat.not_lt.mp hyx) (Nat.not_lt.mp hxy)
          have hgen : x = y := SU2Gen.rank_injective x y heq
          subst hgen
          cases ih ys with
          | inl h => left; right; exact ⟨rfl, h⟩
          | inr h =>
            cases h with
            | inl h => right; left; exact ⟨rfl, h⟩
            | inr h => right; right; right; exact ⟨rfl, h⟩

-- Auxiliary: same-length lexLt a b → lexLt (a ++ d) (b ++ d)
-- (used in degLexLt_right_compat)
private theorem lexLt_append_right (a b d : Monomial SU2Gen)
    (hlen : a.length = b.length) (h : lexLt a b) :
    lexLt (a ++ d) (b ++ d) := by
  induction a generalizing b with
  | nil =>
    cases b with
    | nil => simp [lexLt] at h
    | cons _ _ => simp at hlen
  | cons x xs ih =>
    cases b with
    | nil => simp at hlen
    | cons y ys =>
      simp [List.length_cons] at hlen
      simp [lexLt] at h ⊢
      rcases h with hrank | ⟨heq, hrest⟩
      · left; exact hrank
      · right; exact ⟨heq, ih ys hlen hrest⟩

-- Positional encoding for monomials: maps a list to ℕ such that
-- lexLt a b ∧ a.length = b.length → lexEncoding a < lexEncoding b.
-- Uses big-endian base-4 representation via SU2Gen.rank.
private def lexEncoding : Monomial SU2Gen → ℕ
  | [] => 0
  | x :: xs => x.rank * (4 ^ xs.length) + lexEncoding xs

-- lexEncoding is bounded by 4^n for lists of length n
private theorem lexEncoding_bound : ∀ (a : Monomial SU2Gen),
    lexEncoding a < 4 ^ a.length := by
  intro a
  induction a with
  | nil => simp [lexEncoding]
  | cons x xs ih =>
    simp only [lexEncoding, List.length_cons, pow_succ]
    have hrank : x.rank ≤ 3 := by cases x <;> simp [SU2Gen.rank]
    have h1 : x.rank * 4 ^ xs.length ≤ 3 * 4 ^ xs.length :=
      Nat.mul_le_mul_right _ hrank
    omega

-- At the same length, lexLt implies strict inequality of encodings
private theorem lexEncoding_lt_of_lexLt_same_length :
    ∀ (a b : Monomial SU2Gen), a.length = b.length → lexLt a b →
      lexEncoding a < lexEncoding b := by
  intro a
  induction a with
  | nil =>
    intro b hlen hlex
    cases b with
    | nil => simp [lexLt] at hlex
    | cons _ _ => simp at hlen
  | cons x xs ih =>
    intro b hlen hlex
    cases b with
    | nil => simp at hlen
    | cons y ys =>
      simp [List.length_cons] at hlen
      simp [lexLt] at hlex
      simp [lexEncoding]
      rcases hlex with hrank | ⟨heq, hrest⟩
      · have hxs_bound := lexEncoding_bound xs
        rw [hlen] at hxs_bound ⊢
        have h1 : (x.rank + 1) * 4 ^ ys.length ≤ y.rank * 4 ^ ys.length :=
          Nat.mul_le_mul_right _ hrank
        have h2 : (x.rank + 1) * 4 ^ ys.length = x.rank * 4 ^ ys.length + 4 ^ ys.length := by
          rw [add_mul, one_mul]
        omega
      · have := ih ys hlen hrest
        rw [heq, hlen]
        omega

-- NOTE (2026-06-25): there is deliberately **no** `lexLt_wf`. The *pure*
-- lexicographic order `lexLt` is NOT well-founded. With `[] < (_ :: _)`,
-- prepending the rank-0 generator `g₀` before a common suffix strictly
-- decreases the word, giving the infinite descending chain
--   `[g₁] > [g₀,g₁] > [g₀,g₀,g₁] > …`
-- so `WellFounded lexLt` is false (and `List.Lex rankRel` is likewise not
-- well-founded — which is why no Mathlib lemma supplies the missing step;
-- such a lemma would be unsound). The admissible, well-founded order is
-- `degLexLt` below (compare total degree / word length first, then `lexLt`
-- among equal-length words, where lex *is* well-founded); its `degLexLt_wf`
-- is proved sorry-free and is what the `WellFoundedRelation` instance uses.
-- A prior `lexLt_wf` carrying an unfillable `sorry` (plus its now-dead private
-- scaffolding `rank_lt_4` / `rankRel` / `rankRel_wf` / `lexLt_implies_listLex`)
-- was removed here. See docs/audits/2026-06-25-ugb-lexlt-wf-false-as-stated.md.

-- Ref: [bergman1978] Bergman, "The diamond lemma for ring theory," Adv. Math. 29 (1978)
theorem degLexLt_wf : WellFounded degLexLt :=
  Subrelation.wf
    (fun {a b} (h : degLexLt a b) => by
      simp [degLexLt] at h
      show Prod.Lex (· < ·) (· < ·)
        (a.length, lexEncoding a) (b.length, lexEncoding b)
      rcases h with hlen | ⟨heq, hlex⟩
      · exact Prod.Lex.left _ _ hlen
      · exact heq ▸ Prod.Lex.right _ (lexEncoding_lt_of_lexLt_same_length a b heq hlex))
    (InvImage.wf (fun a => (a.length, lexEncoding a))
      (Nat.lt_wfRel.wf.prod_lex Nat.lt_wfRel.wf))

theorem degLexLt_trichotomy : ∀ (a b : Monomial SU2Gen),
    degLexLt a b ∨ a = b ∨ degLexLt b a := by
  intro a b
  simp [degLexLt]
  by_cases h1 : a.length < b.length
  · left; left; exact h1
  · by_cases h2 : b.length < a.length
    · right; right; left; exact h2
    · have heq : a.length = b.length := Nat.le_antisymm (Nat.not_lt.mp h2) (Nat.not_lt.mp h1)
      cases lexLt_trichotomy a b with
      | inl h => left; right; exact ⟨heq, h⟩
      | inr h =>
        cases h with
        | inl h => right; left; exact h
        | inr h => right; right; right; exact ⟨heq.symm, h⟩

theorem degLexLt_left_compat (a b c : Monomial SU2Gen) (h : degLexLt a b) :
    degLexLt (c ++ a) (c ++ b) := by
  simp [degLexLt] at h ⊢
  cases h with
  | inl hlen => left; omega
  | inr h =>
    obtain ⟨heq, hlex⟩ := h
    right
    constructor
    · omega
    · induction c with
      | nil => simpa using hlex
      | cons x xs ih =>
        simp [lexLt]
        exact ih

theorem degLexLt_right_compat (a b d : Monomial SU2Gen) (h : degLexLt a b) :
    degLexLt (a ++ d) (b ++ d) := by
  simp [degLexLt] at h ⊢
  cases h with
  | inl hlen => left; omega
  | inr h =>
    obtain ⟨heq, hlex⟩ := h
    right
    constructor
    · omega
    · exact lexLt_append_right a b d heq hlex

/-- The **deg-lex admissible order** on monomials over `SU2Gen`,
    fully proved: well-founded, trichotomous, and compatible with
    concatenation. -/
noncomputable def degLexOrder : AdmissibleOrder SU2Gen where
  lt := degLexLt
  trichotomy := degLexLt_trichotomy
  wf := degLexLt_wf
  left_compat := degLexLt_left_compat
  right_compat := degLexLt_right_compat

/-! ## §2  The `q`-Serre Relations -/

/-- The `q`-Serre relations defining `U_q(su(2))`:

    1. `K · K⁻¹ = 1`  and  `K⁻¹ · K = 1`
    2. `K · E_+ = q² · E_+ · K`
    3. `K · E_- = q⁻² · E_- · K`
    4. `E_+ · E_- − E_- · E_+ = (K − K⁻¹) / (q − q⁻¹)`

    Each relation is oriented so that the left-hand side has the larger
    leading monomial under deg-lex.  This yields four reduction rules. -/
structure QSerreRelations (k : Type v) [Field k] where
  /-- The deformation parameter `q ≠ 0, ±1`. -/
  q : k
  q_ne_zero : q ≠ 0
  q_ne_one : q ≠ 1
  q_ne_neg_one : q ≠ -1

/-! ## §3  GS Basis for `U_q(su(2))` -/

/-! ### §3.1  The rewriting system, built rather than axiomatised

The five oriented relations, with their leading monomials under deg-lex:

1. `K · K⁻¹ → 1`                                    (lm = `[K, K_inv]`)
2. `K⁻¹ · K → 1`                                    (lm = `[K_inv, K]`)
3. `K · E_+ → q² · E_+ · K`                         (lm = `[K, E_plus]`)
4. `K · E_- → q⁻² · E_- · K`                        (lm = `[K, E_minus]`)
5. `E_+ · E_- → E_- · E_+ + (K − K⁻¹)/(q − q⁻¹)`    (lm = `[E_plus, E_minus]`)

**`qSerreRewritingSystem` was an axiom.** It is now built, because an opaque
system cannot be asked whether its rules are monic — and `ugb_pbw_corollary`
needs exactly that in order to *discharge* the unit-leading-coefficient
hypothesis of `normal_form_exists` rather than assume it (beans qou-lzoo,
qou-ix9e).

Building it also made the leading monomials checkable, and the check failed
against the old generator ranking: see the correction note on `SU2Gen.rank`.
`qSerre_lm_1 … qSerre_lm_5` now prove all five outright. -/

section QSerreConstruction

variable {k : Type v} [Field k]

/-- A two-term algebra element `c₁·m₁ + c₂·m₂`. -/
def two (m₁ : Monomial SU2Gen) (c₁ : k) (m₂ : Monomial SU2Gen) (c₂ : k) :
    AlgElement SU2Gen k where
  coeff := fun w => if w = m₁ then c₁ else if w = m₂ then c₂ else 0
  support := {m₁, m₂}
  support_spec := by
    intro w hw
    simp only [Finset.mem_insert, Finset.mem_singleton, not_or] at hw
    rw [if_neg hw.1, if_neg hw.2]

/-- A four-term algebra element. -/
def four (m₁ : Monomial SU2Gen) (c₁ : k) (m₂ : Monomial SU2Gen) (c₂ : k)
    (m₃ : Monomial SU2Gen) (c₃ : k) (m₄ : Monomial SU2Gen) (c₄ : k) :
    AlgElement SU2Gen k where
  coeff := fun w => if w = m₁ then c₁ else if w = m₂ then c₂ else
                    if w = m₃ then c₃ else if w = m₄ then c₄ else 0
  support := {m₁, m₂, m₃, m₄}
  support_spec := by
    intro w hw
    simp only [Finset.mem_insert, Finset.mem_singleton, not_or] at hw
    rw [if_neg hw.1, if_neg hw.2.1, if_neg hw.2.2.1, if_neg hw.2.2.2]

theorem two_support_nonempty (m₁ : Monomial SU2Gen) (c₁ : k) (m₂ : Monomial SU2Gen)
    (c₂ : k) : (two m₁ c₁ m₂ c₂ : AlgElement SU2Gen k).support.Nonempty :=
  ⟨m₁, by simp [two]⟩

theorem four_support_nonempty (m₁ : Monomial SU2Gen) (c₁ : k) (m₂ : Monomial SU2Gen)
    (c₂ : k) (m₃ : Monomial SU2Gen) (c₃ : k) (m₄ : Monomial SU2Gen) (c₄ : k) :
    (four m₁ c₁ m₂ c₂ m₃ c₃ m₄ c₄ : AlgElement SU2Gen k).support.Nonempty :=
  ⟨m₁, by simp [four]⟩

/-- The leading monomial of a two-term element is `m₁`, provided `m₂` is below
it. Maximality is finite: the support has two elements. -/
theorem two_lm {m₁ m₂ : Monomial SU2Gen} (c₁ c₂ : k) (hlt : degLexLt m₂ m₁) :
    leadingMonomial degLexOrder (two m₁ c₁ m₂ c₂ : AlgElement SU2Gen k)
      (two_support_nonempty m₁ c₁ m₂ c₂) = m₁ := by
  apply leadingMonomial_eq_of_max
  · show m₁ ∈ ({m₁, m₂} : Finset (Monomial SU2Gen)); simp
  · intro m hm hne
    have hm' : m = m₁ ∨ m = m₂ := by
      have : m ∈ ({m₁, m₂} : Finset (Monomial SU2Gen)) := hm
      simpa using this
    rcases hm' with rfl | rfl
    · exact absurd rfl hne
    · exact hlt

/-- Likewise for four terms. -/
theorem four_lm {m₁ m₂ m₃ m₄ : Monomial SU2Gen} (c₁ c₂ c₃ c₄ : k)
    (h₂ : degLexLt m₂ m₁) (h₃ : degLexLt m₃ m₁) (h₄ : degLexLt m₄ m₁) :
    leadingMonomial degLexOrder (four m₁ c₁ m₂ c₂ m₃ c₃ m₄ c₄ : AlgElement SU2Gen k)
      (four_support_nonempty m₁ c₁ m₂ c₂ m₃ c₃ m₄ c₄) = m₁ := by
  apply leadingMonomial_eq_of_max
  · show m₁ ∈ ({m₁, m₂, m₃, m₄} : Finset (Monomial SU2Gen)); simp
  · intro m hm hne
    have hm' : m = m₁ ∨ m = m₂ ∨ m = m₃ ∨ m = m₄ := by
      have : m ∈ ({m₁, m₂, m₃, m₄} : Finset (Monomial SU2Gen)) := hm
      simpa using this
    rcases hm' with rfl | rfl | rfl | rfl
    · exact absurd rfl hne
    · exact h₂
    · exact h₃
    · exact h₄

/-- **Rule 1**: `K·K⁻¹ → 1`, i.e. the relation `K·K⁻¹ − 1`. -/
def qSerreRule1 : ReductionRule SU2Gen k :=
  ⟨two [K, K_inv] 1 [] (-1), two_support_nonempty _ _ _ _⟩

/-- **Rule 2**: `K⁻¹·K → 1`. -/
def qSerreRule2 : ReductionRule SU2Gen k :=
  ⟨two [K_inv, K] 1 [] (-1), two_support_nonempty _ _ _ _⟩

/-- **Rule 3**: `K·E_+ → q²·E_+·K`. -/
def qSerreRule3 (qs : QSerreRelations k) : ReductionRule SU2Gen k :=
  ⟨two [K, E_plus] 1 [E_plus, K] (-(qs.q ^ 2)), two_support_nonempty _ _ _ _⟩

/-- **Rule 4**: `K·E_- → q⁻²·E_-·K`. -/
def qSerreRule4 (qs : QSerreRelations k) : ReductionRule SU2Gen k :=
  ⟨two [K, E_minus] 1 [E_minus, K] (-(qs.q ^ 2)⁻¹), two_support_nonempty _ _ _ _⟩

/-- **Rule 5**: `E_+·E_- → E_-·E_+ + (K − K⁻¹)/(q − q⁻¹)`. -/
def qSerreRule5 (qs : QSerreRelations k) : ReductionRule SU2Gen k :=
  ⟨four [E_plus, E_minus] 1 [E_minus, E_plus] (-1)
        [K] (-(qs.q - qs.q⁻¹)⁻¹) [K_inv] ((qs.q - qs.q⁻¹)⁻¹),
   four_support_nonempty _ _ _ _ _ _ _ _⟩

/-- **Rule 6**: `K⁻¹·E_+ → q⁻²·E_+·K⁻¹`.

    One of the two rules the original five were missing; without it the system
    is not confluent — see the completion note in §3. -/
def qSerreRule6 (qs : QSerreRelations k) : ReductionRule SU2Gen k :=
  ⟨two [K_inv, E_plus] 1 [E_plus, K_inv] (-(qs.q ^ 2)⁻¹), two_support_nonempty _ _ _ _⟩

/-- **Rule 7**: `K⁻¹·E_- → q²·E_-·K⁻¹`. The other missing rule. -/
def qSerreRule7 (qs : QSerreRelations k) : ReductionRule SU2Gen k :=
  ⟨two [K_inv, E_minus] 1 [E_minus, K_inv] (-(qs.q ^ 2)), two_support_nonempty _ _ _ _⟩

@[simp] theorem qSerre_lm_1 : (qSerreRule1 (k := k)).lm degLexOrder = [K, K_inv] :=
  two_lm _ _ (Or.inl (by simp))

@[simp] theorem qSerre_lm_2 : (qSerreRule2 (k := k)).lm degLexOrder = [K_inv, K] :=
  two_lm _ _ (Or.inl (by simp))

@[simp] theorem qSerre_lm_3 (qs : QSerreRelations k) :
    (qSerreRule3 qs).lm degLexOrder = [K, E_plus] :=
  two_lm _ _ (Or.inr ⟨by simp, by simp [lexLt, SU2Gen.rank]⟩)

@[simp] theorem qSerre_lm_4 (qs : QSerreRelations k) :
    (qSerreRule4 qs).lm degLexOrder = [K, E_minus] :=
  two_lm _ _ (Or.inr ⟨by simp, by simp [lexLt, SU2Gen.rank]⟩)

@[simp] theorem qSerre_lm_5 (qs : QSerreRelations k) :
    (qSerreRule5 qs).lm degLexOrder = [E_plus, E_minus] :=
  four_lm _ _ _ _
    (Or.inr ⟨by simp, by simp [lexLt, SU2Gen.rank]⟩)
    (Or.inl (by simp)) (Or.inl (by simp))

@[simp] theorem qSerre_lm_6 (qs : QSerreRelations k) :
    (qSerreRule6 qs).lm degLexOrder = [K_inv, E_plus] :=
  two_lm _ _ (Or.inr ⟨by simp, by simp [lexLt, SU2Gen.rank]⟩)

@[simp] theorem qSerre_lm_7 (qs : QSerreRelations k) :
    (qSerreRule7 qs).lm degLexOrder = [K_inv, E_minus] :=
  two_lm _ _ (Or.inr ⟨by simp, by simp [lexLt, SU2Gen.rank]⟩)

/-- The leading coefficient of a two-term element is `c₁`. -/
theorem two_lc {m₁ m₂ : Monomial SU2Gen} (c₁ c₂ : k) (hlt : degLexLt m₂ m₁) :
    (two m₁ c₁ m₂ c₂ : AlgElement SU2Gen k).coeff
      (leadingMonomial degLexOrder (two m₁ c₁ m₂ c₂ : AlgElement SU2Gen k)
        (two_support_nonempty m₁ c₁ m₂ c₂)) = c₁ := by
  rw [two_lm c₁ c₂ hlt]
  simp [two]

/-- Likewise for four terms. -/
theorem four_lc {m₁ m₂ m₃ m₄ : Monomial SU2Gen} (c₁ c₂ c₃ c₄ : k)
    (h₂ : degLexLt m₂ m₁) (h₃ : degLexLt m₃ m₁) (h₄ : degLexLt m₄ m₁) :
    (four m₁ c₁ m₂ c₂ m₃ c₃ m₄ c₄ : AlgElement SU2Gen k).coeff
      (leadingMonomial degLexOrder (four m₁ c₁ m₂ c₂ m₃ c₃ m₄ c₄ : AlgElement SU2Gen k)
        (four_support_nonempty m₁ c₁ m₂ c₂ m₃ c₃ m₄ c₄)) = c₁ := by
  rw [four_lm c₁ c₂ c₃ c₄ h₂ h₃ h₄]
  simp [four]

/-- **Every q-Serre rule is monic** — each relation is written with coefficient
`1` on its leading monomial. This is the fact `ugb_pbw_corollary` needs, and the
reason the system had to be built rather than axiomatised. -/
theorem qSerre_rule_lc_eq_one (qs : QSerreRelations k) :
    (qSerreRule1 (k := k)).lc degLexOrder = 1 ∧
    (qSerreRule2 (k := k)).lc degLexOrder = 1 ∧
    (qSerreRule3 qs).lc degLexOrder = 1 ∧
    (qSerreRule4 qs).lc degLexOrder = 1 ∧
    (qSerreRule5 qs).lc degLexOrder = 1 ∧
    (qSerreRule6 qs).lc degLexOrder = 1 ∧
    (qSerreRule7 qs).lc degLexOrder = 1 :=
  ⟨two_lc _ _ (Or.inl (by simp)),
   two_lc _ _ (Or.inl (by simp)),
   two_lc _ _ (Or.inr ⟨by simp, by simp [lexLt, SU2Gen.rank]⟩),
   two_lc _ _ (Or.inr ⟨by simp, by simp [lexLt, SU2Gen.rank]⟩),
   four_lc _ _ _ _ (Or.inr ⟨by simp, by simp [lexLt, SU2Gen.rank]⟩)
     (Or.inl (by simp)) (Or.inl (by simp)),
   two_lc _ _ (Or.inr ⟨by simp, by simp [lexLt, SU2Gen.rank]⟩),
   two_lc _ _ (Or.inr ⟨by simp, by simp [lexLt, SU2Gen.rank]⟩)⟩

/-- The seven rules — the five of the original presentation, **plus the two
`K⁻¹` commutation rules it was missing**. See the completion note in §3. -/
def qSerreRules (qs : QSerreRelations k) : List (ReductionRule SU2Gen k) :=
  [qSerreRule1, qSerreRule2, qSerreRule3 qs, qSerreRule4 qs, qSerreRule5 qs,
   qSerreRule6 qs, qSerreRule7 qs]

end QSerreConstruction

/-- The rewriting system derived from the `q`-Serre relations — **a definition,
not an axiom**. -/
-- Ref: [bokut2005] https://doi.org/10.1142/S0218196705002347 (q-Serre rewriting system for U_q(su(2)))
def qSerreRewritingSystem (k : Type v) [Field k]
    (qs : QSerreRelations k) : RewritingSystem SU2Gen k :=
  ⟨qSerreRules qs, by simp [qSerreRules]⟩

/-- **The q-Serre rules have unit leading coefficients.**

Discharges the hypothesis `ugb_pbw_corollary` had to carry while the system was
opaque (bean qou-lzoo left it hanging deliberately rather than assert a monicity
axiom; this proves it instead). -/
theorem qSerre_rules_monic (k : Type v) [Field k] (qs : QSerreRelations k) :
    ∀ r ∈ (qSerreRewritingSystem k qs).rules, IsUnit (r.lc degLexOrder) := by
  obtain ⟨h1, h2, h3, h4, h5, h6, h7⟩ := qSerre_rule_lc_eq_one qs
  intro r hr
  simp only [qSerreRewritingSystem, qSerreRules, List.mem_cons, List.not_mem_nil,
    or_false] at hr
  rcases hr with rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · rw [h1]; exact isUnit_one
  · rw [h2]; exact isUnit_one
  · rw [h3]; exact isUnit_one
  · rw [h4]; exact isUnit_one
  · rw [h5]; exact isUnit_one
  · rw [h6]; exact isUnit_one
  · rw [h7]; exact isUnit_one

/-! ### The Gröbner–Shirshov property (Bokut–Malcolmson 1996)

    The `q`-Serre relations form a Gröbner–Shirshov basis for
    `U_q(su(2))` under the deg-lex order.

    **The overlap analysis this docstring used to carry was wrong, and the
    five-rule system it described was not a Gröbner–Shirshov basis** (bean
    qou-18s7). It listed six "S-polynomial computations", of which three —
    `(1,3)`, `(1,4)`, `(3,4)` — are not ambiguities at all: those pairs share a
    *first* letter, and an overlap requires a proper **suffix** of one leading
    word to equal a proper **prefix** of the other. It also recorded `(2,3)` as
    "no overlap", when `[K⁻¹,K]` followed by `[K,E_+]` overlaps at `K` and is in
    fact one of the two ambiguities that **fail**.

    The real analysis, computed exactly over `ℚ(q)` by
    `computations/qserre_gs_basis_check.py`:

    * the **five**-rule system has exactly **5** overlap ambiguities, and two of
      them do not resolve — both decisively, with each pair of reducts genuinely
      irreducible:

      | ambiguity | word | one way | the other |
      |---|---|---|---|
      | R2/R3 | `K⁻¹ K E_+` | `E_+` | `q²·K⁻¹ E_+ K` |
      | R2/R4 | `K⁻¹ K E_-` | `E_-` | `q⁻²·K⁻¹ E_- K` |

      Both are instances of the same gap: nothing rewrites `K⁻¹` past `E_±`, so
      `K⁻¹ E_± K` is stuck.

    * adding the two missing rules (6 and 7, the `K⁻¹` commutation rules) gives
      **8** ambiguities, and **all 8 resolve**.

    The statement `qSerre_is_gs_basis` is about the **completed seven-rule
    system**. It was an axiom here, recording that symbolic check. It is now a
    theorem, proved in `QSerreGS.lean` (which imports this file): each of the
    eight resolutions is written out and machine-checked through the composition
    lemma `Diamond.isGrobnerShirshovBasis_iff_compositionsTrivial`.

    History worth keeping: this is the third claim in this file to be examined by
    making it checkable, and the second to be found false — see
    `pbw_monomials_are_not_all_normal_forms` for the other.

    Reference: Bokut & Malcolmson, Israel J. Math. 96 (1996). -/

/-! ## §4  PBW Basis -/

/-- A **PBW monomial** is a word of the form `E_+^a · K^b · E_-^c`.
    These are exactly the normal-form monomials under the deg-lex
    order with the `q`-Serre rewriting system: no leading monomial
    of any relation appears as a subword. -/
structure PBWMonomial where
  /-- Exponent of `E_+`. -/
  a : ℕ
  /-- Exponent of `K` (can be negative, represented as `b₊ - b₋`). -/
  b_pos : ℕ
  b_neg : ℕ
  /-- Exponent of `E_-`. -/
  c : ℕ

/-- The PBW monomial as an explicit word in the generators. -/
def PBWMonomial.toMonomial (m : PBWMonomial) : Monomial SU2Gen :=
  List.replicate m.a E_plus ++
  List.replicate m.b_pos K ++
  List.replicate m.b_neg K_inv ++
  List.replicate m.c E_minus

/-- The `PBWMonomial` with `b₊ = b₋ = 1` and `a = c = 0` is the word `[K, K⁻¹]`. -/
theorem pbw_word_K_Kinv :
    (⟨0, 1, 1, 0⟩ : PBWMonomial).toMonomial = [K, K_inv] := by
  simp [PBWMonomial.toMonomial]

/-- The element of `k⟨SU2Gen⟩` supported on a single PBW word. -/
def pbwElement (k : Type v) [Field k] (m : PBWMonomial) : AlgElement SU2Gen k :=
  ⟨fun w => if w = m.toMonomial then (1 : k) else 0,
   {m.toMonomial},
   fun w hw => by simp at hw; simp [hw]⟩

/-- **⚠ The PBW normal-form claim, as it was stated, is FALSE.**

    This used to be an axiom:

    > every `PBWMonomial` is in normal form under the `q`-Serre system

    with `PBWMonomial.toMonomial m = E_+^a ++ K^{b₊} ++ K⁻¹^{b₋} ++ E_-^c`. Once
    `qSerreRewritingSystem` became a definition (§3.1) the claim became
    checkable, and it fails. `⟨a,b₊,b₋,c⟩ = ⟨0,1,1,0⟩` is the word `[K, K⁻¹]`,
    which is *exactly* rule 1's leading monomial, so it is reducible.

    The axiom's own justification is where it went wrong. It argued that the PBW
    word "contains no forbidden subword … because generators appear in canonical
    order with each block homogeneous" — but the `K` block is immediately
    followed by the `K⁻¹` block, which produces `[K, K⁻¹]` whenever both are
    non-empty. Homogeneity within blocks says nothing about the joins between
    them, and there are three bad joins, not one:

    | join | when | is the lm of |
    |---|---|---|
    | `[K, K⁻¹]` | `b₊ ≥ 1` and `b₋ ≥ 1` | rule 1 |
    | `[K, E_-]` | `b₊ ≥ 1` and `c ≥ 1` | rule 4 |
    | `[E_+, E_-]` | `a ≥ 1`, `b₊ = b₋ = 0`, `c ≥ 1` | rule 5 |

    So the letter order `E_+ … K … E_- ` is not the normal-form order for this
    system at all. Reading the rules' orientations off §3.1, reduction moves
    `E_-` left past `E_+` (rule 5) and moves `K` right past both (rules 3, 4), so
    the normal words are `E_-^c E_+^a K^b` — with `K` and `K⁻¹` never mixed.

    Nothing downstream is left resting on the false claim: `ugb_pbw_corollary`
    now takes normality as an explicit hypothesis rather than importing it from
    here. Establishing it for the corrected shape is open, and is the genuine
    remaining content of Bokut–Malcolmson Thm 3.2.

    Reference: Bokut & Malcolmson, Israel J. Math. 96 (1996), Theorem 3.2. -/
-- Ref: [bokut2005] https://doi.org/10.1142/S0218196705002347 (PBW monomials as GS normal forms — shape corrected)
theorem pbw_monomials_are_not_all_normal_forms (k : Type v) [Field k]
    (qs : QSerreRelations k) :
    ¬ (∀ m : PBWMonomial,
        isNormalForm degLexOrder (qSerreRewritingSystem k qs) (pbwElement k m)) := by
  intro h
  refine h ⟨0, 1, 1, 0⟩ qSerreRule1
    (by simp [qSerreRewritingSystem, qSerreRules]) [K, K_inv] ?_ ?_
  · show (if ([K, K_inv] : Monomial SU2Gen)
      = (⟨0, 1, 1, 0⟩ : PBWMonomial).toMonomial then (1 : k) else 0) ≠ 0
    rw [pbw_word_K_Kinv]
    simp
  · rw [qSerre_lm_1]

/-! ## §5  Distribution Algebra GS Basis -/

/-- The generators of the distribution algebra `Dist(G)` in
    characteristic `p`.  These are the divided-power generators
    `x^{(n)} = x^n / n!` for each generator `x` of the Lie algebra,
    truncated at `p`-th powers. -/
structure DistAlgGenerators where
  /-- The prime characteristic. -/
  p : ℕ
  /-- `p` is prime. -/
  p_prime : Nat.Prime p
  /-- The number of Lie algebra generators. -/
  num_generators : ℕ

/-! **The former axiom `dist_algebra_gs_basis` was false** (removed
    2026-11-15). It asserted that *every* rewriting system over every field
    is a Gröbner–Shirshov basis; its `DistAlgGenerators` argument was never
    used, so nothing tied `sys` to the relations of `Dist(G)`. The Hecke
    system at `n = 4` is not a GS basis
    (`Hecke.NotAGSBasis.hecke_not_gs_basis_four`), which refutes it; the
    refutation is `dist_algebra_gs_basis_false` in
    `UGB.GrobnerShirshov.HeckeGS` (it cannot live here, because `HeckeGS`
    imports this file).

    The true statement ([fred2005, Proposition 3.8]) needs the concrete
    rewriting system of `Dist(G)` built from the formal group law; it is
    open in Lean. -/

end UGB.GrobnerShirshov
