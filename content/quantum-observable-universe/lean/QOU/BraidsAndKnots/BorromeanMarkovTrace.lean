/-
  Borromean Markov trace: exact closed form, stated over `R[h]`.

  The Markov trace of the Borromean braid `β_Bor = (σ₁⁻¹σ₂)³` on `H_3(q)`,
  evaluated via the Jones polynomial of the Borromean rings, is the unique
  value `t` satisfying the multiplicative relation

      [2]_q² · t = 4 + h² − 3h⁴ − h⁶,    [2]_q² = h² + 4,   h = q − q⁻¹.

  Equivalently, when `[2]_q²` is invertible (e.g. over `ℝ`/`ℚ` at real `q`),

      tr_M(β_Bor, q) = (4 + h² − 3h⁴ − h⁶) / (h² + 4).

  FAITHFUL BASE RING.  Every character / closed-form / reconstruction /
  bar-symmetry identity below is a *polynomial identity in `h`* — provable
  by `ring` with NO division and NO field.  It is therefore stated over a
  generic `{R : Type*} [CommRing R] (h : R)`, i.e. over the polynomial ring
  `R[h]`.  Instantiating `R = LaurentPolynomial ℤ`, `h = T − T⁻¹` recovers
  the genuine `ℤ[q, q⁻¹]` statements (`h ∈ ℤ[q,q⁻¹]`, integer coefficients).
  This is the **fibre** object (formal `q`); only the quotient form and the
  positivity `[2]_q² > 0` descend to the **archimedean** leg, isolated in
  the final `ℚ` section.

  Derivation (used to obtain the numerator/denominator):
    1. Jones polynomial: V(𝓑₃, t) = −t⁻³ + 3t⁻² − 2t⁻¹ + 4 − 2t + 3t² − t³
    2. In u = q² + q⁻²: V = −u³ + 3u² + u − 2
    3. [2]_q² = (q + q⁻¹)² = u + 2
    4. tr_M = V / [2]² = (−u³ + 3u² + u − 2) / (u + 2)
    5. Polynomial division: = −u² + 5u − 9 + 16/(u + 2)
    6. Substituting u = h² + 2: tr_M·(h² + 4) = 4 + h² − 3h⁴ − h⁶

  h-expansion (purely even):
    tr_M = 1 + 0·h² − (3/4)·h⁴ − (1/16)·h⁶ + (1/64)·h⁸ + ...

  The h² coefficient is EXACTLY ZERO. The first topological invariant
  of the Borromean linking structure appears at h⁴ = −3/4.

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [murasugi1996] ISBN 978-0-8176-3817-7
-/
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.LinearCombination

namespace QOU.BraidsAndKnots

/-! ## `R[h]` layer — multiplicative identities over a generic commutative ring

Everything in this section holds over `{R : Type*} [CommRing R] (h : R)`,
i.e. in the polynomial ring `R[h]`.  No division, no field, no ordering —
the `tr_M` closed form is encoded as the multiplicative relation
`[2]_q² · t = numerator` (see `IsBorromeanMarkovTrace`). -/

section CommRing
variable {R : Type*} [CommRing R]

/-- The numerator of tr_M(β_Bor) as a polynomial in h: `4 + h² − 3h⁴ − h⁶`. -/
def trM_borromean_num (h : R) : R := 4 + h^2 - 3 * h^4 - h^6

/-- The denominator `[2]_q² = h² + 4` as a polynomial in h. -/
def trM_borromean_den (h : R) : R := h^2 + 4

/-- **The defining multiplicative relation for the Borromean Markov trace.**
    A value `t : R` *is* the Borromean Markov trace at `h` iff

      `[2]_q² · t = numerator`,   i.e.   `(h² + 4)·t = 4 + h² − 3h⁴ − h⁶`.

    This replaces the division-form `tr_M := num/den`, characterising `tr_M`
    WITHOUT inverting `[2]_q²`, so it makes sense over any `R[h]`.  Over a
    field where `h² + 4 ≠ 0` it pins `t = num/den` uniquely (see
    `trM_borromean_isTrace` in the `ℚ` section). -/
def IsBorromeanMarkovTrace (h t : R) : Prop :=
  trM_borromean_den h * t = trM_borromean_num h

/-- At `h = 0` (q = 1), `t = 1` solves the defining relation: `4·1 = 4`. -/
theorem isBorromeanMarkovTrace_one_at_zero :
    IsBorromeanMarkovTrace (0 : R) 1 := by
  unfold IsBorromeanMarkovTrace trM_borromean_den trM_borromean_num
  ring

/-- The Jones polynomial of the Borromean rings in u = q² + q⁻². -/
def jones_borromean_in_u (u : R) : R := -u^3 + 3 * u^2 + u - 2

/-- [2]_q² = (q + q⁻¹)² in terms of u = q² + q⁻². -/
def bracket2_sq_in_u (u : R) : R := u + 2

/-- The polynomial division: V / [2]² = quotient + 16/(u+2).
    Equivalently: V = (u+2) · (−u² + 5u − 9) + 16. -/
theorem jones_division (u : R) :
    jones_borromean_in_u u =
    bracket2_sq_in_u u * (-u^2 + 5*u - 9) + 16 := by
  unfold jones_borromean_in_u bracket2_sq_in_u
  ring

/-- The substitution u = h² + 2 maps the Jones polynomial
    to the numerator of tr_M. -/
theorem jones_to_trM_num (h : R) :
    jones_borromean_in_u (h^2 + 2) = trM_borromean_num h := by
  unfold jones_borromean_in_u trM_borromean_num
  ring

/-- The substitution u = h² + 2 maps [2]² to the denominator. -/
theorem bracket2_to_trM_den (h : R) :
    bracket2_sq_in_u (h^2 + 2) = trM_borromean_den h := by
  unfold bracket2_sq_in_u trM_borromean_den
  ring

/-- The h⁴ coefficient of the numerator is −3.
    Since the denominator's leading term is 4,
    the h⁴ coefficient of tr_M is −3/4. -/
theorem h4_coefficient_of_num (h : R) :
    trM_borromean_num h = 4 * (1 : R) + 1 * h^2 + (-3) * h^4 + (-1) * h^6 := by
  unfold trM_borromean_num
  ring

/-- **The `h² = 0` cancellation, multiplicatively.**
    The numerator splits as `[2]_q²·1 + (−3h⁴ − h⁶)` — i.e. the `h⁰…h²`
    part of the numerator is *exactly* the denominator `4 + h²`, so a `t`
    satisfying the defining relation has `t − 1` divisible by `[2]_q²` with
    a pure-`h⁴` tail (`tr_M = 1 + (−3h⁴ − h⁶)/[2]_q²`, no `h¹,h²,h³`).
    Pure `ring`, no division. -/
theorem h2_coefficient_cancellation (h : R) :
    trM_borromean_num h = trM_borromean_den h * 1 +
    (-3 * h^4 - h^6) := by
  unfold trM_borromean_num trM_borromean_den
  ring

/-- **Closed form, multiplicative (`R[h]`).**  Any `t` satisfying the
    defining relation `IsBorromeanMarkovTrace h t` satisfies

      `[2]_q² · (t − 1) = −3h⁴ − h⁶ = h⁴·(−3 − h²)`.

    This is the division-free statement of
    `tr_M = 1 + (−3h⁴ − h⁶)/[2]_q²`: it says `tr_M − 1` factors through
    `h⁴` once `[2]_q²` is cleared, with no `h⁰…h³` correction (the
    structural `h² = 0` fact). -/
theorem borromean_markov_trace_closed_form_mul (h t : R)
    (ht : IsBorromeanMarkovTrace h t) :
    trM_borromean_den h * (t - 1) = h^4 * (-3 - h^2) := by
  unfold IsBorromeanMarkovTrace trM_borromean_den trM_borromean_num at ht ⊢
  linear_combination ht

/-! ### Bar-(anti-)symmetric structure, over `R[h]`

The bar-involution sends `q ↦ q⁻¹`, equivalently `h = q − q⁻¹ ↦ −h`.
The numerator `4 + h² − 3h⁴ − h⁶` and denominator `h² + 4` are *even*
polynomials in `h`, so the defining relation is invariant under `h ↦ −h`:
the SAME trace value `t` solves the relation at `h` and at `−h`.  Hence the
bar-anti-symmetric companion vanishes structurally (the `ℚ`/field statement
`Q_borromean_eq_zero` below is the archimedean shadow of this). -/

/-- The numerator polynomial `4 + h² − 3h⁴ − h⁶` is even in `h`. -/
theorem trM_borromean_num_even (h : R) :
    trM_borromean_num (-h) = trM_borromean_num h := by
  unfold trM_borromean_num
  ring

/-- The denominator polynomial `h² + 4` is even in `h`. -/
theorem trM_borromean_den_even (h : R) :
    trM_borromean_den (-h) = trM_borromean_den h := by
  unfold trM_borromean_den
  ring

/-- **Bar-invariance of the defining relation.**  A value `t` is the
    Borromean Markov trace at `h` iff it is the trace at `−h`.  Division-free
    consequence of the evenness of numerator and denominator. -/
theorem isBorromeanMarkovTrace_neg (h t : R) :
    IsBorromeanMarkovTrace (-h) t ↔ IsBorromeanMarkovTrace h t := by
  unfold IsBorromeanMarkovTrace
  rw [trM_borromean_num_even, trM_borromean_den_even]

end CommRing

/-! ## Archimedean (`ℚ`) layer — quotient form and positivity

The genuine *division* form `tr_M := num/den` and the *ordering* fact
`[2]_q² > 0` are archimedean: they live over an ordered field, here `ℚ`.
Each result below is recovered from the `R[h]` multiplicative core above by
clearing `[2]_q²` (which is a unit since `[2]_q² = h² + 4 > 0`). -/

/-- The Borromean Markov trace as a rational function of h (archimedean
    quotient form).  Pinned by `IsBorromeanMarkovTrace` once `[2]_q²` is
    invertible — see `trM_borromean_isTrace`. -/
noncomputable def trM_borromean (h : ℚ) : ℚ := trM_borromean_num h / trM_borromean_den h

/-- The denominator is always positive (hence non-zero) for real h. -/
theorem trM_borromean_den_pos (h : ℚ) : trM_borromean_den h > 0 := by
  unfold trM_borromean_den
  nlinarith [sq_nonneg h]

/-- The denominator is non-zero. -/
theorem trM_borromean_den_ne_zero (h : ℚ) : trM_borromean_den h ≠ 0 := by
  exact ne_of_gt (trM_borromean_den_pos h)

/-- **The quotient form satisfies the multiplicative defining relation.**
    Bridges the `ℚ` division form to the `R[h]` characterisation
    `IsBorromeanMarkovTrace`: `[2]_q² · (num/den) = num`. -/
theorem trM_borromean_isTrace (h : ℚ) :
    IsBorromeanMarkovTrace h (trM_borromean h) := by
  unfold IsBorromeanMarkovTrace trM_borromean
  have hne := trM_borromean_den_ne_zero h
  field_simp

/-- At h = 0 (q = 1), the Markov trace is exactly 1. -/
theorem trM_borromean_at_h_zero : trM_borromean 0 = 1 := by
  unfold trM_borromean trM_borromean_num trM_borromean_den
  norm_num

/-- Main result: the Borromean Markov trace, combining all steps.
    V(𝓑₃) / [2]_q² = (4 + h² − 3h⁴ − h⁶) / (h² + 4)
    with the h² coefficient being exactly zero (cancellation).

    Quotient-form shadow of `borromean_markov_trace_closed_form_mul`; the
    division here is legitimate because `[2]_q² = h² + 4 ≠ 0`. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem borromean_markov_trace_closed_form (h : ℚ) (hne : trM_borromean_den h ≠ 0) :
    trM_borromean h = 1 + (-3 * h^4 - h^6) / trM_borromean_den h := by
  unfold trM_borromean
  rw [h2_coefficient_cancellation]
  field_simp

/-- **Structural h² = 0 and h⁴ leading-order corollary.**
    The Borromean Markov trace minus its h=0 value (which is 1)
    factors through h⁴ — i.e. there is no h⁰, h¹, h², h³ correction:
    $$\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q) - 1
       = h^4 \cdot \frac{-3 - h^2}{h^2 + 4}.$$
    The leading h⁴ coefficient is therefore the value of the right
    factor at h = 0, which is $-3/4$.

    This makes the h² = 0 structural fact explicit (no Taylor-series
    machinery needed; it follows by algebraic division of the
    rational expression).  Archimedean shadow of
    `borromean_markov_trace_closed_form_mul`.

    Audit chain: `docs/audits/2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md`
    (T1 closure). -/
theorem trM_minus_one_factors_through_h_to_the_fourth
    (h : ℚ) (hne : trM_borromean_den h ≠ 0) :
    trM_borromean h - 1 = h^4 * (-3 - h^2) / trM_borromean_den h := by
  rw [borromean_markov_trace_closed_form h hne]
  field_simp
  ring

/-- The leading h⁴ coefficient of (tr_M − 1) is exactly −3/4,
    obtained by evaluating the right factor at h = 0. -/
theorem h4_leading_coefficient_eq_neg_three_quarters :
    (-3 - (0 : ℚ)^2) / trM_borromean_den 0 = -3 / 4 := by
  unfold trM_borromean_den
  norm_num

/-- The Borromean Markov trace is invariant under the bar-involution
    `h ↦ −h` (equivalently `q ↦ q⁻¹`).  Archimedean shadow of
    `isBorromeanMarkovTrace_neg`. -/
theorem trM_borromean_bar_invariant (h : ℚ) :
    trM_borromean (-h) = trM_borromean h := by
  unfold trM_borromean
  rw [trM_borromean_num_even, trM_borromean_den_even]

/-- The bar-anti-symmetric companion of the Borromean Markov trace:
    `Q_borromean(h) := (tr_M(h) − tr_M(−h)) / 2`.

    Defined by analogy with `Q_m` from PR #1153 for the torus family
    `T(2, 2m)`, where `Q_m(h) = (q^{2m+1} − q^{−(2m+1)}) / (2 [2]_q)`
    is the odd-h projection of the full Markov trace. -/
noncomputable def Q_borromean (h : ℚ) : ℚ :=
  (trM_borromean h - trM_borromean (-h)) / 2

/-- **The bar-anti-symmetric companion of the Borromean Markov trace
    vanishes identically.** Direct consequence of
    `trM_borromean_bar_invariant`.

    Categorical interpretation: the Borromean braid 𝓑₃ carries no
    bar-anti-symmetric (Coulomb / EM-channel) component in its
    Markov trace. This contrasts with the torus family `T(2, 2m)`,
    whose `Q_m` is non-zero and equals `sinh((2m+1) η) / (2 cosh η)`
    at substrate (PR #1153).

    Closes the `Q_borromean_eq_zero : True := trivial` placeholder
    in `QOU.BraidKnot.BarSymmetricBarAntiSymmetricIdentities` (added
    by commit `d4d640ce7`, flagged as the next concrete Lean gap by
    PR #1196's audit). -/
theorem Q_borromean_eq_zero (h : ℚ) : Q_borromean h = 0 := by
  unfold Q_borromean
  rw [trM_borromean_bar_invariant]
  ring

/-! ### Linking-weight bridge formula — explicit inconsistency with Family A

PR #1272 audit (2026-05-25): the framework's `linking_weight(𝓑₃, q)`
has been computed via two independent routes — both Lean-proved — that
turn out to give different values. This section makes the
inconsistency explicit at the Lean level so future work can address
it categorically rather than by silent normalisation choices.

The `+5/2` leading constants and the `/2` in the family-A weight are
archimedean (rational coefficients), so this section also lives over `ℚ`.

**Route 1 — Family A (Wedderburn dim sum on H_4)**:
  λ_A(q) := (1/4) · Σ_{λ ⊢ 4} dim_q V_λ = 5/2 + (3/4)·h²
(Lean-proved in `lambda-scale-substrate-form.lean §lambdaA_qForm_eq_hForm`.)

**Route 2 — Jones bridge (H_3 Markov trace of β_Bor, rescaled)**:
  linking_weight_bridge(h) := 5/2 + 4·(trM_borromean(h) − 1)
(The +5/2 leading and the factor 4 force `linking_weight(q=1) = 5/2`
to match Family A's leading at h=0; the formula is a *bridge*
between the H_3 Markov trace and Family A's H_4 Wedderburn count,
not a derivation.)

The two routes disagree by an explicit rational function in h, derived
below.  Identifying which is the categorically-correct `linking_weight`
is the open Reading-A research direction.

Ref: PR #1272 — `gamma-gamma-pair-production-decomposition.witness.json`
Ref: `docs/audits/2026-05-25-non-abelian-stokes-reading-a-exploration.md`
-/

/-- The Jones-bridge form of `linking_weight(𝓑₃, q)`, written in h:

    `linking_weight_bridge(h) := 5/2 + 4·(trM_borromean(h) − 1)`

    The `+5/2` and the factor `4` are CHOSEN to align with Family A's
    leading at h=0; they are not derived from the Markov trace itself.

    See `family_a_h_minus_bridge_explicit` below for the explicit
    rational-function disagreement with Family A. -/
noncomputable def linking_weight_bridge (h : ℚ) : ℚ :=
  5/2 + 4 * (trM_borromean h - 1)

/-- **Bridge simplification theorem.**  The bridge formula, written
    as a single rational function in h:

    `linking_weight_bridge(h) = 5/2 − (12·h⁴ + 4·h⁶) / (h² + 4)`

    Derivation: `4 · (trM − 1) = 4 · (num − den) / den
    = 4 · (−3h⁴ − h⁶) / (h² + 4) = −(12h⁴ + 4h⁶) / (h² + 4)`. -/
theorem linking_weight_bridge_simplified (h : ℚ)
    (hne : trM_borromean_den h ≠ 0) :
    linking_weight_bridge h =
      5/2 - (12 * h^4 + 4 * h^6) / (h^2 + 4) := by
  unfold linking_weight_bridge trM_borromean trM_borromean_num
  -- trM_borromean_den h = h^2 + 4 by definition; unfold rewrites the
  -- division denominator to that form so field_simp can clear it.
  show 5/2 + 4 * ((4 + h^2 - 3 * h^4 - h^6) / trM_borromean_den h - 1)
       = 5/2 - (12 * h^4 + 4 * h^6) / (h^2 + 4)
  unfold trM_borromean_den
  field_simp
  ring

/-- The Family-A linking-weight in h-form (mirror of
    `lambdaA_hForm` from `lambda-scale-substrate-form.lean`, restated
    here over ℚ for consistency with `trM_borromean`). -/
def linking_weight_family_a_h (h : ℚ) : ℚ :=
  5/2 + (3/4) * h^2

/-- **The explicit Family-A-vs-Jones-bridge disagreement.**

    For every h with `h² + 4 ≠ 0` (i.e. for all rational h, since
    `h² + 4 > 0`):

      `linking_weight_family_a_h(h) − linking_weight_bridge(h)
        = (3/4)·h² + (12·h⁴ + 4·h⁶) / (h² + 4)`

    Numerically at the substrate `h₀ ≈ 0.209` this gap is `≈ 0.0385`,
    which matches the empirical residual reported in PR #1272's
    γγ-decomposition probe witness.

    **Categorical interpretation.**  Family A (Wedderburn dim sum on
    H_4) and the Jones bridge (H_3 Markov trace of β_Bor, additively
    rescaled to match Family A at h=0) are different theorems about
    different objects — both correct, both Lean-proved.  The
    docstring of Python's `borromean_markov_trace_h2` previously
    claimed they agree at h² order via the bridge; this is FALSE
    under the Kauffman-Jones standard normalisation `[2]_q² =
    q² + 2 + q⁻²` (which IS the convention used here).  Under a
    non-standard normalisation `(q^{1/2} + q^{-1/2})² = q + 2 + q⁻¹`
    they appear to agree at h², but that is a normalisation
    coincidence — see `docs/audits/2026-05-25-non-abelian-stokes-
    reading-a-exploration.md` and PR #1272's correction commit.

    The open question is which of the two objects is the
    categorically-correct `linking_weight` for the mass formula
    `m(𝓑₃) = m_e · Vol(𝓑₃)/ℏ_q² · linking_weight(q)`.  Neither
    matches the CODATA-anchor target exactly; the Jones bridge is
    ~47% closer than Family A. -/
theorem family_a_h_minus_bridge_explicit (h : ℚ)
    (hne : trM_borromean_den h ≠ 0) :
    linking_weight_family_a_h h - linking_weight_bridge h =
      (3/4) * h^2 + (12 * h^4 + 4 * h^6) / (h^2 + 4) := by
  rw [linking_weight_bridge_simplified h hne]
  unfold linking_weight_family_a_h
  field_simp
  ring

/-- **Strict positivity of the Family-A-vs-Jones gap for non-zero h.**

    For every non-zero rational h, the Family-A-minus-bridge
    difference is strictly positive, confirming that Family A is
    structurally HIGHER than the Jones bridge at every q ≠ 1.

    This formalises the empirical observation in PR #1272's witness
    that Family A's residual versus the CODATA target (+0.0808 at
    q₀) exceeds the Jones bridge's residual (+0.0424) — the two
    routes never coincide for h ≠ 0. -/
theorem family_a_h_minus_bridge_pos (h : ℚ) (hne : h ≠ 0) :
    linking_weight_family_a_h h - linking_weight_bridge h > 0 := by
  rw [family_a_h_minus_bridge_explicit h (trM_borromean_den_ne_zero h)]
  have h2_pos : h^2 > 0 := by positivity
  have h2_plus_4_pos : h^2 + 4 > 0 := trM_borromean_den_pos h
  -- (3/4)·h² > 0 (strictly, since h ≠ 0)
  -- (12h⁴ + 4h⁶) / (h² + 4) ≥ 0
  -- Sum > 0
  have term1_pos : (3 : ℚ)/4 * h^2 > 0 := by positivity
  have term2_nn : (12 * h^4 + 4 * h^6) / (h^2 + 4) ≥ 0 := by
    apply div_nonneg
    · positivity
    · linarith
  linarith

end QOU.BraidsAndKnots
