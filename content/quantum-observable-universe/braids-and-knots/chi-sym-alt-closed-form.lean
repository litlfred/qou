/-
  Closed-form theorem for χ_sym(β_atom) · χ_alt(β_atom).

  For any atom (Z, N) with Z ≥ 1, N ≥ 1, and braid word β_{Z,N}
  produced by `atom_braid_word_3A`, the product of symmetric and
  alternating Wedderburn characters satisfies the exact identity

        χ_sym(β) · χ_alt(β) = (-1)^{#β} · (1 + H_A^2 / 4)^{2A+1}

  where #β is the total length of the braid word (n_σ + n_σ⁻¹ + n_ud),
  A = Z + N, and H_A = q - q⁻¹.

  Ref: [manuscript] docs/chi-sym-alt-theorem.md.
-/

import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.GroupPower.Basic
import Mathlib.Data.Int.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Omega
import Mathlib.Tactic.NormNum

namespace QOU.ChiSymAlt

/-- Factor types arising in atom_braid_word_3A. -/
inductive FactorType
  | sigma           -- (c=1, d=0): pure σ
  | sigmaInv        -- (c=1, d=-H_A): pure σ⁻¹
  | udHalf          -- (c=1, d=-H_A/2): ud quark pair
  deriving DecidableEq, Repr

/-- The atom's braid word is a finite list of (factor-type, generator-index) pairs. -/
abbrev AtomBraidWord := List (FactorType × ℕ)

/-- Per-factor product χ_sym · χ_alt in the two 1-dim Hecke irreps.

    For the Hecke relation σ² = H_A σ + 1 with eigenvalues {q, -q⁻¹},
    χ_sym(σ) = q, χ_alt(σ) = -q⁻¹, and char factors over the word.
    Hence χ_sym(cσ+d) · χ_alt(cσ+d) = (cq+d)(-c/q+d) = d² - c² + cd·H_A. -/
def chiPairPerFactor (H_A : ℝ) : FactorType → ℝ
  | .sigma    => -1                  -- 0² - 1² + 1·0·H_A = -1
  | .sigmaInv => -1                  -- H_A² - 1² + 1·(-H_A)·H_A = -1
  | .udHalf   => -(1 + H_A^2 / 4)    -- (H_A/2)² - 1 - (H_A/2)·H_A

/-- χ_sym(β) · χ_alt(β) computed by multiplicativity over the word.
    Defined via list recursion for clean induction. -/
def chiPairProduct (H_A : ℝ) : AtomBraidWord → ℝ
  | [] => 1
  | (ft, _) :: rest => chiPairPerFactor H_A ft * chiPairProduct H_A rest

/-- Number of ud-half factors in a braid word. -/
def nUd : AtomBraidWord → ℕ
  | [] => 0
  | (ft, _) :: rest => (if ft = .udHalf then 1 else 0) + nUd rest

/-- Core lemma: the character product equals (-1)^(length) times the
    ud-half scalar raised to its count. -/
theorem chiPairProduct_eq (H_A : ℝ) (w : AtomBraidWord) :
    chiPairProduct H_A w =
      (-1 : ℝ)^w.length * (1 + H_A^2 / 4)^(nUd w) := by
  induction w with
  | nil => simp [chiPairProduct, nUd]
  | cons hd tl ih =>
    obtain ⟨ft, _g⟩ := hd
    rw [chiPairProduct, nUd, List.length_cons, ih]
    -- Three cases on the factor type.
    match ft with
    | .sigma =>
      show chiPairPerFactor H_A .sigma *
           ((-1 : ℝ)^tl.length * (1 + H_A^2 / 4)^(nUd tl)) =
           (-1 : ℝ)^(tl.length + 1) *
           (1 + H_A^2 / 4)^((if FactorType.sigma = .udHalf then 1 else 0) + nUd tl)
      simp only [chiPairPerFactor, if_neg (by decide : FactorType.sigma ≠ .udHalf),
                 Nat.zero_add, pow_succ]
      ring
    | .sigmaInv =>
      show chiPairPerFactor H_A .sigmaInv *
           ((-1 : ℝ)^tl.length * (1 + H_A^2 / 4)^(nUd tl)) =
           (-1 : ℝ)^(tl.length + 1) *
           (1 + H_A^2 / 4)^((if FactorType.sigmaInv = .udHalf then 1 else 0) + nUd tl)
      simp only [chiPairPerFactor, if_neg (by decide : FactorType.sigmaInv ≠ .udHalf),
                 Nat.zero_add, pow_succ]
      ring
    | .udHalf =>
      show chiPairPerFactor H_A .udHalf *
           ((-1 : ℝ)^tl.length * (1 + H_A^2 / 4)^(nUd tl)) =
           (-1 : ℝ)^(tl.length + 1) *
           (1 + H_A^2 / 4)^((if FactorType.udHalf = .udHalf then 1 else 0) + nUd tl)
      simp only [chiPairPerFactor, if_pos rfl, pow_succ]
      ring

/-- Auxiliary: (-1 : ℝ)^n equals +1 iff n is even, else -1. -/
theorem neg_one_pow_eq_if (n : ℕ) :
    ((-1 : ℝ))^n = if n % 2 = 0 then 1 else -1 := by
  induction n with
  | zero => simp
  | succ k ih =>
    by_cases hk : k % 2 = 0
    · have : (k + 1) % 2 = 1 := by omega
      rw [this]
      rw [pow_succ, ih, if_pos hk]
      norm_num
    · have : (k + 1) % 2 = 0 := by omega
      rw [this]
      rw [pow_succ, ih, if_neg hk]
      norm_num

/-- The closed-form theorem in its original stated form. -/
theorem chi_pair_closed_form (H_A : ℝ) (w : AtomBraidWord) :
    chiPairProduct H_A w =
      (if w.length % 2 = 0 then 1 else (-1 : ℝ)) *
      (1 + H_A^2 / 4)^(nUd w) := by
  rw [chiPairProduct_eq, neg_one_pow_eq_if]

/-- Pure-existence lemma: for every `Z, N ∈ ℕ` there exists a braid
    word whose ud-half count equals `2·(Z+N) + 1`.

    **Scope note (Copilot PR#401 review).**  This lemma is *purely
    existential* and is proven by exhibiting a trivial witness (a list
    of exactly `2·(Z+N) + 1` ud-half factors).  It does **not** prove
    that the specific word emitted by `atom_braid_word_3A` has this
    count — that equality is argued informally in
    `docs/chi-sym-alt-theorem.md` § Step 4-5 by inspection of the
    Python source, and is formalization work left for future iteration.

    When fully formalised, the intended statement becomes:
      `nUd (atomBraidWord Z N) = 2·(Z+N) + 1`
    with `atomBraidWord` a Lean port of `mass_at_3A_proper.atom_braid_word_3A`.

    Ref: [manuscript] docs/chi-sym-alt-theorem.md § Step 4-5. -/
theorem n_ud_atom_braid (Z N : ℕ) :
    ∃ (w : AtomBraidWord), nUd w = 2 * (Z + N) + 1 := by
  refine ⟨List.replicate (2 * (Z + N) + 1) (FactorType.udHalf, 0), ?_⟩
  -- Induction on the replicate count.
  generalize 2 * (Z + N) + 1 = k
  induction k with
  | zero => simp [nUd]
  | succ n ih => simp [List.replicate_succ, nUd, ih]

/-- Existence of a word realizing the closed form.  Combines
    `chi_pair_closed_form` and `n_ud_atom_braid`: some word with
    ud-half count `2·(Z+N) + 1` exists and satisfies the closed form.

    **Scope note (Copilot PR#401 review).**  As with
    `n_ud_atom_braid`, this is existential only.  Linking it to the
    concrete `atom_braid_word_3A` output requires formalising that
    Python function in Lean.  The physical content (word length
    parity sign = -1 for all concrete atoms D, T, ³He, ⁴He) is
    verified numerically in
    `computations/derivation_checks.py`; see
    docs/chi-sym-alt-theorem.md Verification table. -/
theorem chi_sym_alt_closed_form (Z N : ℕ) (H_A : ℝ) :
    ∃ (w : AtomBraidWord), nUd w = 2 * (Z + N) + 1 ∧
      chiPairProduct H_A w =
        (if w.length % 2 = 0 then 1 else (-1 : ℝ)) *
        (1 + H_A^2 / 4)^(2 * (Z + N) + 1) := by
  obtain ⟨w, hw⟩ := n_ud_atom_braid Z N
  refine ⟨w, hw, ?_⟩
  rw [chi_pair_closed_form, hw]

end QOU.ChiSymAlt
