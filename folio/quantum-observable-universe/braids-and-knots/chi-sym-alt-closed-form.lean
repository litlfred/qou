/-
  Closed-form theorem for χ_sym(β_atom) · χ_alt(β_atom).

  For any atom (Z, N) with Z ≥ 1, N ≥ 1, and braid word β_{Z,N}
  produced by `atom_braid_word_3A`, the product of symmetric and
  alternating Wedderburn characters satisfies the exact identity

        χ_sym(β) · χ_alt(β) = (-1)^{#β} · (1 + H_A^2 / 4)^{2A+1}

  where #β is the total length of the braid word (n_σ + n_σ⁻¹ + n_ud),
  A = Z + N, and H_A = q - q⁻¹.

  Ref: [leitner2026] docs/chi-sym-alt-theorem.md.
-/

import Mathlib.Algebra.Group.Defs
import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic
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
noncomputable def chiPairPerFactor (H_A : ℝ) : FactorType → ℝ
  | .sigma    => -1                  -- 0² - 1² + 1·0·H_A = -1
  | .sigmaInv => -1                  -- H_A² - 1² + 1·(-H_A)·H_A = -1
  | .udHalf   => -(1 + H_A^2 / 4)    -- (H_A/2)² - 1 - (H_A/2)·H_A

/-- χ_sym(β) · χ_alt(β) computed by multiplicativity over the word.
    Defined via list recursion for clean induction. -/
noncomputable def chiPairProduct (H_A : ℝ) : AtomBraidWord → ℝ
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
      simp only [chiPairPerFactor, reduceIte, pow_succ, pow_add]
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

    Ref: [leitner2026] docs/chi-sym-alt-theorem.md § Step 4-5. -/
theorem n_ud_atom_braid (Z N : ℕ) :
    ∃ (w : AtomBraidWord), nUd w = 2 * (Z + N) + 1 := by
  refine ⟨List.replicate (2 * (Z + N) + 1) (FactorType.udHalf, 0), ?_⟩
  -- Induction on the replicate count.
  generalize 2 * (Z + N) + 1 = k
  induction k with
  | zero => simp [nUd]
  | succ n ih =>
    simp [List.replicate_succ, nUd, ih]
    omega

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

/-! ## The colour-weighted alphabet

    `FactorType` above has three constructors. The word `atom_braid_word_3A`
    actually emits has **four** letter types: measured on ⁴He (47 letters), 23
    `σ`, 15 `σ⁻¹`, 8 at `d = -H_A/2`, and **one** at `d = -H_A·(1/2 - δ/4)` with
    `δ = flavor_split_subleading(q₀) ≈ 0.001376` — the colour-weighted p-n
    interface. There is exactly one per atom regardless of `A`, because the p-p
    interface is a plain `σ` and the n-n a plain `σ⁻¹`, already isospin-distinct
    by chirality.

    So everything above is sorry-free and TRUE, about a **colour-blind**
    alphabet — the `pn_convention = "strict_averaged"` word. It is not about the
    word the corpus builds, whose canonical convention is
    `bring_color_weighted` (owner ruling 2026-08-15, R3).

    This section is additive: nothing above changes. The colour-weighted form is
    the theorem and the colour-blind one its `δ = 0` corollary, because that is
    the only direction that exists — setting `δ = 0` collapses the weighted form
    to the blind one, while the blind form has already discarded `δ`.

    Bean `qou-cdqu`; the measurement is
    `computations/chi_sym_alt_closed_form.py` and its witness. -/

/-- Per-factor character product for the Hecke element `σ + d·1`.

    In the 1-dim irreps `σ ↦ q` (sym) and `σ ↦ -q⁻¹` (alt), so the factor acts
    as `(q + d)` and `(-q⁻¹ + d)`; their product is `d² - 1 + d·H_A`. Every
    letter is an instance of this, including the three of `FactorType`. -/
noncomputable def perFactorOfD (H_A d : ℝ) : ℝ := d ^ 2 - 1 + d * H_A

/-- The `d` of each colour-blind letter. -/
noncomputable def dOf (H_A : ℝ) : FactorType → ℝ
  | .sigma    => 0
  | .sigmaInv => -H_A
  | .udHalf   => -H_A / 2

/-- `chiPairPerFactor` is `perFactorOfD` at the letter's own `d`. The three
    hard-coded values above are not three separate facts. -/
theorem chiPairPerFactor_eq_perFactorOfD (H_A : ℝ) (ft : FactorType) :
    chiPairPerFactor H_A ft = perFactorOfD H_A (dOf H_A ft) := by
  cases ft <;> · unfold chiPairPerFactor perFactorOfD dOf; ring

/-- **The stationarity identity.** For any `d`, the per-factor product differs
    from the `ud` value by exactly the SQUARE of the offset:

        perFactorOfD H_A d - perFactorOfD H_A (-H_A/2) = (d + H_A/2)²

    This is the substantive content of this section, and it is a `ring`
    identity — no calculus needed, and stronger than "the first derivative
    vanishes" since it gives the exact remainder.

    It says the `ud` letter sits at a **stationary point** of the per-factor
    product, so perturbing it costs SECOND order. That is why the colour
    weighting, a `6.88e-4` relative shift in `d`, moves the character product by
    only `(7.19e-5)² = 5.17e-9`.

    Measured consequence: `chi_sym_alt_closed_form.py` reported a residual of
    `5.11395e-9` against the colour-blind form on all four atoms; predicted from
    this identity alone, `5.11397e-9`. Six significant figures. Carrying the p-n
    letter as itself takes the residual to `1.2e-14`, the float64 floor of the
    inputs.

    It is also why the gap stayed hidden: the producer ran in float64 under a
    `tolerance = 1e-3` justified by a comment about "numerical noise" in the
    seminormal matrices. There is no such noise, and a real second-order colour
    term sat 200,000× inside that tolerance. -/
theorem perFactorOfD_sub_udHalf (H_A d : ℝ) :
    perFactorOfD H_A d - perFactorOfD H_A (-H_A / 2) = (d + H_A / 2) ^ 2 := by
  unfold perFactorOfD; ring

/-- **The same content with no division, over any commutative ring.**

        4·(d² − 1 + d·H_A) = (2d + H_A)² − H_A² − 4

    This is the sharper statement, and it is the primary one. Multiplying the
    `ℝ` identity above by 4 clears the `/2`, so it needs no `Field`, no
    `CharZero` and no `2 ≠ 0` — plain `ring` over `[CommRing R]`, which is what
    §7c asks for.

    It also says the thing more directly: **all of the `d`-dependence of the
    per-factor product sits inside a perfect square**, `(2d + H_A)²`, and that
    square vanishes exactly at `2d = -H_A`. "The `ud` letter is a stationary
    point" and "the offset enters squared" are the same fact, and this form
    makes the second one manifest without mentioning derivatives, division, or
    a distinguished point.

    Historical note worth keeping: the divided form needed `[Field R]
    [CharZero R]`, because `H_A/2` is undefined in characteristic 2 and the
    identity fails there. This form is fine in characteristic 2 — it degenerates
    to `0 = 0`, which is honest: there is no stationary point to speak of, and
    the statement makes no claim about one. -/
theorem four_mul_perFactorOfD {R : Type*} [CommRing R] (H_A d : R) :
    4 * (d ^ 2 - 1 + d * H_A) = (2 * d + H_A) ^ 2 - H_A ^ 2 - 4 := by
  ring

/-- The `ℝ` per-factor product, in the division-free form. -/
theorem four_mul_perFactorOfD_real (H_A d : ℝ) :
    4 * perFactorOfD H_A d = (2 * d + H_A) ^ 2 - H_A ^ 2 - 4 := by
  unfold perFactorOfD; ring

/-- Corollary: the `ud` value is the extremum, and every other letter's value
    lies on one side of it. -/
theorem perFactorOfD_udHalf_le (H_A d : ℝ) :
    perFactorOfD H_A (-H_A / 2) ≤ perFactorOfD H_A d := by
  have h := perFactorOfD_sub_udHalf H_A d
  nlinarith [sq_nonneg (d + H_A / 2)]

/-- The alphabet the canonical word uses: the three colour-blind letters, plus
    a colour-weighted letter carrying its own `d`.

    Deliberately a NEW inductive rather than a fourth constructor on
    `FactorType`: everything above stays exactly as proved, and `FactorType`
    keeps its `DecidableEq` (which a real-valued field would cost it). -/
inductive ColourFactorType
  | plain (ft : FactorType)
  | pnColour (d : ℝ)

abbrev ColourWord := List (ColourFactorType × ℕ)

noncomputable def chiPairPerFactorC (H_A : ℝ) : ColourFactorType → ℝ
  | .plain ft   => chiPairPerFactor H_A ft
  | .pnColour d => perFactorOfD H_A d

noncomputable def chiPairProductC (H_A : ℝ) : ColourWord → ℝ
  | [] => 1
  | (cf, _) :: rest => chiPairPerFactorC H_A cf * chiPairProductC H_A rest

/-- Count of `udHalf` letters. Matches structurally rather than via `if _ = _`,
    so no `DecidableEq` on the real-carrying type is needed. -/
def nUdC : ColourWord → ℕ
  | [] => 0
  | (.plain .udHalf, _) :: rest => 1 + nUdC rest
  | (_, _) :: rest => nUdC rest

/-- Count of colour-blind letters. -/
def nBlind : ColourWord → ℕ
  | [] => 0
  | (.plain _, _) :: rest => 1 + nBlind rest
  | (_, _) :: rest => nBlind rest

/-- Count of colour-weighted letters. One per atom, in the canonical word. -/
def nPn : ColourWord → ℕ
  | [] => 0
  | (.pnColour _, _) :: rest => 1 + nPn rest
  | (_, _) :: rest => nPn rest

/-- Product over the colour-weighted letters. -/
noncomputable def pnProduct (H_A : ℝ) : ColourWord → ℝ
  | [] => 1
  | (.pnColour d, _) :: rest => perFactorOfD H_A d * pnProduct H_A rest
  | (_, _) :: rest => pnProduct H_A rest

/-- **Closed form on the colour-weighted alphabet.**

        χ_sym(β)·χ_alt(β) = (-1)^{#blind} · (1 + H_A²/4)^{nUd} · Π_{pn} f(d)

    The colour-blind theorem `chiPairProduct_eq` is the case with no `pnColour`
    letters, where `pnProduct = 1` and `#blind = length`. -/
theorem chiPairProductC_eq (H_A : ℝ) (w : ColourWord) :
    chiPairProductC H_A w =
      (-1 : ℝ) ^ nBlind w * (1 + H_A ^ 2 / 4) ^ nUdC w * pnProduct H_A w := by
  induction w with
  | nil => simp [chiPairProductC, nBlind, nUdC, pnProduct]
  | cons hd tl ih =>
    obtain ⟨cf, _g⟩ := hd
    match cf with
    | .plain .sigma =>
      simp only [chiPairProductC, chiPairPerFactorC, chiPairPerFactor,
                 nBlind, nUdC, pnProduct, ih, pow_add, pow_one]
      ring
    | .plain .sigmaInv =>
      simp only [chiPairProductC, chiPairPerFactorC, chiPairPerFactor,
                 nBlind, nUdC, pnProduct, ih, pow_add, pow_one]
      ring
    | .plain .udHalf =>
      simp only [chiPairProductC, chiPairPerFactorC, chiPairPerFactor,
                 nBlind, nUdC, pnProduct, ih, pow_add, pow_one]
      ring
    | .pnColour d =>
      simp only [chiPairProductC, chiPairPerFactorC, nBlind, nUdC, pnProduct, ih]
      ring

/-- **The δ = 0 corollary: the colour-blind form is the special case.**

    A word whose single colour-weighted letter happens to sit at `d = -H_A/2`
    — i.e. `δ = 0`, the `strict_averaged` convention — has its `pnColour` letter
    contribute exactly what a `udHalf` letter would, so the product collapses to
    the colour-blind closed form with the exponent raised by one.

    This is the direction that exists. There is no route back: the colour-blind
    statement has already discarded `d`. -/
theorem chiPairProductC_delta_zero (H_A : ℝ) (w : ColourWord)
    (hpn : pnProduct H_A w = (-(1 + H_A ^ 2 / 4)) ^ nPn w) :
    chiPairProductC H_A w =
      (-1 : ℝ) ^ nBlind w * (1 + H_A ^ 2 / 4) ^ nUdC w *
      (-(1 + H_A ^ 2 / 4)) ^ nPn w := by
  rw [chiPairProductC_eq, hpn]

end QOU.ChiSymAlt
