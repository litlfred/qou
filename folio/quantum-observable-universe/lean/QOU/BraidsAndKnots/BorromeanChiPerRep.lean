/-
  Borromean per-representation character: the standard-irrep character
  χ^{(2,1)}(β_Bor) — algebraic equivalence of its two published forms.

  The content proposition `prop:borromean-markov-trace-closed-form`
  (`borromean-markov-trace-closed-form.md` lines 101–110) records the
  standard (2-dimensional) irrep character of the Borromean braid in two
  forms:

      χ^{(2,1)}(β_Bor) = (−q¹² + 3q¹⁰ − 3q⁸ + 4q⁶ − 3q⁴ + 3q² − 1) / q⁶
                       = 2 − 3h⁴ − h⁶,      h = q − q⁻¹.

  This file proves the **algebraic equivalence of the two forms** (the
  q-rational equals the h-polynomial), which is a pure field identity
  (`field_simp; ring`).

  SCOPE / HONESTY.  This lemma proves the two *forms* agree.  It does NOT
  prove that the character of β_Bor *equals* this value — that fact (the
  per-representation decomposition `χ^{(3)} = χ^{(1³)} = 1`,
  `χ^{(2,1)} = 2 − 3h⁴ − h⁶`) is, at the time of writing, NARRATIVE-ONLY
  in the content `.md` (it requires the seminormal Hecke-representation
  machinery, not present in Lean).  It is independently CONFIRMED
  NUMERICALLY (≤ 4e-50) by `borromean_chi_independent_crosscheck.py`
  (PR #1947) against the skein-validated engine `homfly_ocneanu_trace`.
  See `docs/audits/2026-06-07-borromean-chi-crossmethod-proof-status.md`.

  Companion to `BorromeanMarkovTrace.lean`, which proves the *full*
  tr_M closed form `(4 + h² − 3h⁴ − h⁶)/(h² + 4)` (the standard irrep is
  the only one contributing the h⁴, h⁶ corrections).

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [murasugi1996] ISBN 978-0-8176-3817-7
-/
import Mathlib.Algebra.Order.Field.Rat
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.LinearCombination
import Mathlib.Algebra.Polynomial.Laurent

namespace QOU.BraidsAndKnots

/-! ## `R[h]` layer — the standard-irrep character as a polynomial in `h`

The faithful base of the standard-irrep character is the polynomial
`χ^{(2,1)} = 2 − 3h⁴ − h⁶ ∈ R[h]` — pure `ring`, no division, no field.
Instantiating `R = LaurentPolynomial ℤ`, `h = T − T⁻¹` gives the genuine
`ℤ[q, q⁻¹]` character.  Only the q-rational form (`… / q⁶`) needs `q`
inverted, and lives in the `ℚ` section below. -/

section CommRing
variable {R : Type*} [CommRing R]

/-- The standard-irrep Borromean character as a polynomial in `h`:
    `χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶`.  This is the faithful `R[h]` form
    (no division); `h = q − q⁻¹`. -/
def chi21_borromean (h : R) : R := 2 - 3 * h^4 - h^6

/-- The `R[h]` character `2 − 3h⁴ − h⁶` is even in `h` (bar-invariant under
    `h ↦ −h`, i.e. `q ↦ q⁻¹`): only even powers `h⁴, h⁶` appear. -/
theorem chi21_borromean_even (h : R) :
    chi21_borromean (-h) = chi21_borromean h := by
  unfold chi21_borromean
  ring

/-! ### Yekutieli $B_3$ action projected onto the local $(2,1)$ bond (`qou-h5aw`)
    and NA-Stokes counit bar-parity split (`qou-quv8`, `qou-ch8w`, `qou-yczy`)

    1. **Local $(2,1)$ bond projection (`qou-h5aw`):**
       In the 2-dimensional standard Hook representation $V_{(2,1)}$ of $H_3(q)$,
       a single elementary crossing-commutator plaquette step
       $M = T_1 T_2^{-1} \in \mathrm{SL}_2(R)$ has determinant $\det(M) = 1$ and
       trace $t_{(2,1)}(h) = -1 - h^2$ (`yekutieliBond21Trace`).
       By the $\mathrm{SL}_2$ Cayley–Hamilton cubic trace polynomial
       $\operatorname{tr}(M^3) = t^3 - 3t$ (`sl2CubicTrace`), the 3-fold
       Yekutieli holonomy around the Borromean cycle $B_3 = (T_1 T_2^{-1})^3$
       projects onto the $(2,1)$ bond as
       $$(-1 - h^2)^3 - 3(-1 - h^2) = 2 - 3h^4 - h^6 = \chi^{(2,1)}(\beta_{\text{Bor}}).$$
       Notice that because $T_3'(-1) = 3(-1)^2 - 3 = 0$, the $O(h^2)$ term in
       $t_{(2,1)}(h) = -1 - h^2$ cancels identically in $t^3 - 3t$, explaining why
       $\chi^{(2,1)}(\beta_{\text{Bor}})$ begins at $-3h^4$.

    2. **Bar-parity split of the NA-Stokes counit expansion (`qou-quv8`, `qou-ch8w`, `qou-yczy`):**
       Under the bar-involution $q \mapsto q^{-1}$ ($h = q - q^{-1} \mapsto -h$),
       the leading coupling $\mu_0(h) = c_1 h$ is strictly **bar-odd** ($\sinh$
       channel), whereas the 2nd-order NA-Stokes counit correction $c_2 h^2$ is
       strictly **bar-even** ($\cosh$ channel).  Decomposing the higher-order
       effective coupling $\mu_{\text{eff}}(h) = \mu_{\text{odd}}(h) + \mu_{\text{even}}(h)$
       into its odd ($\sinh$, $c_1 h + c_3 h^3$) and even ($\cosh$, $c_2 h^2 + c_4 h^4$)
       pieces isolates the 2nd-order bar-even counit term via
       $\mu_{\text{eff}}(h) + \mu_{\text{eff}}(-h) = 2 \mu_{\text{even}}(h)$ and
       $\mu_{\text{eff}}(h) - \mu_{\text{eff}}(-h) = 2 \mu_{\text{odd}}(h)$. -/

/-- Trace of a single Yekutieli $T_1 T_2^{-1}$ plaquette step projected onto the
    2-dimensional local $(2,1)$ Hook representation $V_{(2,1)}$ of $H_3(q)$:
    $t_{(2,1)}(h) = -1 - h^2$. -/
def yekutieliBond21Trace (h : R) : R := -1 - h^2

/-- The single-step $(2,1)$ bond trace $-1 - h^2$ is bar-even ($h \mapsto -h$). -/
theorem yekutieliBond21Trace_even (h : R) :
    yekutieliBond21Trace (-h) = yekutieliBond21Trace h := by
  unfold yekutieliBond21Trace
  ring

/-- The $\mathrm{SL}_2$ Cayley–Hamilton cubic trace polynomial
    $T_3(t) = t^3 - 3t$, expressing $\operatorname{tr}(M^3)$ in terms of
    $t = \operatorname{tr}(M)$ for any $2 \times 2$ matrix $M$ with $\det(M) = 1$. -/
def sl2CubicTrace (t : R) : R := t^3 - 3 * t

/-- **Yekutieli $B_3$ projection onto the local $(2,1)$ bond (`qou-h5aw`).**
    Evaluating the $\mathrm{SL}_2$ cubic trace polynomial $t^3 - 3t$ on the
    single-bond trace $t = -1 - h^2$ yields the exact Borromean standard-irrep
    character $\chi^{(2,1)}(\beta_{\text{Bor}}) = 2 - 3h^4 - h^6$, with the
    $O(h^2)$ term cancelling identically because $T_3'(-1) = 0$. -/
theorem yekutieli_b3_local_21_bond_projection (h : R) :
    sl2CubicTrace (yekutieliBond21Trace h) = chi21_borromean h := by
  unfold sl2CubicTrace yekutieliBond21Trace chi21_borromean
  ring

/-- The $O(h^2)$ stationarity identity at the unknot/trivial-braid basepoint
    $t_0 = -1$: $T_3(-1 + \delta) - T_3(-1) = -3\delta^2 + \delta^3$, with zero
    linear term in $\delta$. -/
theorem sl2CubicTrace_stationary_at_neg_one (δ : R) :
    sl2CubicTrace (-1 + δ) - sl2CubicTrace (-1)
      = -3 * δ^2 + δ^3 := by
  unfold sl2CubicTrace
  ring

/-- Bar-odd ($\sinh$-channel) component of the NA-Stokes counit expansion
    (`qou-quv8`, `qou-ch8w`): $\mu_{\text{odd}}(h) = c_1 h + c_3 h^3$. -/
def naStokesMuOdd (c1 c3 h : R) : R := c1 * h + c3 * h^3

/-- Bar-even ($\cosh$-channel) component of the NA-Stokes counit expansion
    (`qou-quv8`, `qou-ch8w`): $\mu_{\text{even}}(h) = c_2 h^2 + c_4 h^4$. -/
def naStokesMuEven (c2 c4 h : R) : R := c2 * h^2 + c4 * h^4

/-- Total 4th-order NA-Stokes effective counit expansion
    $\mu_{\text{eff}}(h) = \mu_{\text{odd}}(h) + \mu_{\text{even}}(h)$. -/
def naStokesMuEff (c1 c2 c3 c4 h : R) : R :=
  naStokesMuOdd c1 c3 h + naStokesMuEven c2 c4 h

/-- `naStokesMuOdd` reverses sign under the bar-involution $h \mapsto -h$. -/
theorem naStokesMuOdd_neg (c1 c3 h : R) :
    naStokesMuOdd c1 c3 (-h) = - naStokesMuOdd c1 c3 h := by
  unfold naStokesMuOdd
  ring

/-- `naStokesMuEven` is invariant under the bar-involution $h \mapsto -h$. -/
theorem naStokesMuEven_neg (c2 c4 h : R) :
    naStokesMuEven c2 c4 (-h) = naStokesMuEven c2 c4 h := by
  unfold naStokesMuEven
  ring

/-- **Bar-parity extraction of the 2nd/4th-order bar-even ($\cosh$) and 1st/3rd-order
    bar-odd ($\sinh$) NA-Stokes counit channels (`qou-quv8`, `qou-ch8w`, `qou-yczy`).** -/
theorem naStokesMuEff_bar_parity_split (c1 c2 c3 c4 h : R) :
    naStokesMuEff c1 c2 c3 c4 h + naStokesMuEff c1 c2 c3 c4 (-h)
      = 2 * naStokesMuEven c2 c4 h
    ∧ naStokesMuEff c1 c2 c3 c4 h - naStokesMuEff c1 c2 c3 c4 (-h)
        = 2 * naStokesMuOdd c1 c3 h := by
  constructor <;> {
    unfold naStokesMuEff naStokesMuOdd naStokesMuEven
    ring
  }

/-- **Surface-ordering curvature double-channel decomposition (`qou-yczy`).**
    If each of the two oriented triangular half-plaquettes of the 2-simplex
    contributes $-z_2$ (where $z_2 = \zeta(2) = \pi^2/6$ in the Archimedean
    evaluation), the total NA-Stokes surface-ordering shift is $-2 z_2$
    ($= -\pi^2/3$), and the shifted Part B evaluation $(-z_2) + (-2 z_2)$ equals
    $-3 z_2$ ($= -\pi^2/2$). -/
theorem naStokes_surface_ordering_double_half_plaquette (z2 : R) :
    (-z2 + -z2 = -2 * z2) ∧ (-z2 + (-2 * z2) = -3 * z2) := by
  constructor <;> ring

end CommRing

/-! ## `Rˣ` layer — the published q-rational form over a commutative ring

The published character
`χ^{(2,1)}(β_Bor) = (−q¹² + 3q¹⁰ − 3q⁸ + 4q⁶ − 3q⁴ + 3q² − 1)/q⁶` divides by
`q⁶`.  Demanding only that `q` be a **unit** of a commutative ring `R`
(`q : Rˣ`, so `↑q⁻¹` is its ring inverse and division by `q⁶` is
multiplication by `(↑q⁻¹)⁶`) keeps the form **division-ring-free**: it now
instantiates over `R = LaurentPolynomial ℤ`, `q = T` (a unit, inverse `T(-1)`),
giving the genuine `ℤ[q, q⁻¹]` character.  This is strictly more general than
the `[Field R]` form below (every non-zero `q` in a field is a unit).

The bridge `chi21_borromean_qform_unit_eq_poly` shows this published form is
exactly the faithful `R[h]` polynomial character `chi21_borromean` at
`h = ↑q − ↑q⁻¹`; the only input is the unit law `↑q · ↑q⁻¹ = 1` (no division,
no field, no ordering). -/

section Unit
variable {R : Type*} [CommRing R]

/-- The published q-rational Borromean character `(−q¹² + ⋯ − 1)/q⁶`, over a
    commutative ring with `q` a unit: division by `q⁶` is `(↑q⁻¹)⁶`. -/
def chi21_borromean_qform_unit (q : Rˣ) : R :=
  (-(↑q : R)^12 + 3*(↑q : R)^10 - 3*(↑q : R)^8 + 4*(↑q : R)^6
    - 3*(↑q : R)^4 + 3*(↑q : R)^2 - 1) * ((↑q⁻¹ : R))^6

/-- **The published q-rational form equals the faithful `R[h]` character.**
    `chi21_borromean_qform_unit q = chi21_borromean (↑q − ↑q⁻¹)` over any
    commutative ring with `q` a unit — division-free, the sole hypothesis is
    `↑q · ↑q⁻¹ = 1`.  Hence the Borromean standard-irrep character is a genuine
    `ℤ[q, q⁻¹]` Laurent polynomial, not merely a rational function over a field.
    (The `linear_combination` coefficient is the exact quotient of
    `qform − chi21_borromean(↑q−↑q⁻¹)` by `↑q·↑q⁻¹ − 1`, machine-derived; the
    residual is closed by `ring`.) -/
theorem chi21_borromean_qform_unit_eq_poly (q : Rˣ) :
    chi21_borromean_qform_unit q = chi21_borromean ((↑q : R) - ↑q⁻¹) := by
  have hab : (↑q : R) * ↑q⁻¹ = 1 := q.mul_inv
  unfold chi21_borromean_qform_unit chi21_borromean
  set a : R := (↑q : R) with ha
  set b : R := (↑q⁻¹ : R) with hb
  linear_combination
    (- a^11*b^5 - a^10*b^4 + 3*a^9*b^5 - a^9*b^3 + 3*a^8*b^4 - 3*a^7*b^5
      - a^8*b^2 + 3*a^7*b^3 - 3*a^6*b^4 + 4*a^5*b^5 - a^7*b + 3*a^6*b^2
      - 3*a^5*b^3 + 4*a^4*b^4 - 3*a^3*b^5 - a^6 + 3*a^5*b - 3*a^4*b^2
      + 4*a^3*b^3 - 3*a^2*b^4 + 3*a*b^5 - 3*a^4 + 12*a^3*b - 16*a^2*b^2
      + 12*a*b^3 - 3*b^4 + 2*a*b + 2) * hab

/-- Bar-invariance over units: `q ↦ q⁻¹` fixes the character, since it sends
    `h = ↑q − ↑q⁻¹ ↦ −h` and `chi21_borromean` is even.  Division-free. -/
theorem chi21_borromean_qform_unit_bar_invariant (q : Rˣ) :
    chi21_borromean_qform_unit q⁻¹ = chi21_borromean_qform_unit q := by
  rw [chi21_borromean_qform_unit_eq_poly q⁻¹, chi21_borromean_qform_unit_eq_poly q, inv_inv]
  rw [show ((↑q⁻¹ : R) - ↑q) = -((↑q : R) - ↑q⁻¹) by ring]
  exact chi21_borromean_even _

/-- The $q$-Laurent form of the single Yekutieli $(2,1)$ bond trace
    $\operatorname{tr}(T_1 T_2^{-1}) = (-q^2) + (1 - q^{-2}) = 1 - q^2 - q^{-2}$
    for $T_1 = \begin{pmatrix} q & 0 \\ 1 & -q^{-1} \end{pmatrix}$ and
    $T_2^{-1} = \begin{pmatrix} -q & 1 \\ 0 & q^{-1} \end{pmatrix}$ (`qou-h5aw`). -/
def yekutieliBond21Trace_qform_unit (q : Rˣ) : R :=
  1 - (↑q : R)^2 - (↑q⁻¹ : R)^2

/-- Over any commutative ring with unit `q : Rˣ`, the matrix trace
    $1 - q^2 - q^{-2}$ of $T_1 T_2^{-1}$ in $V_{(2,1)}$ equals the `R[h]`
    polynomial `yekutieliBond21Trace (q - q⁻¹) = -1 - (q - q⁻¹)²` (`qou-h5aw`). -/
theorem yekutieliBond21Trace_qform_unit_eq_poly (q : Rˣ) :
    yekutieliBond21Trace_qform_unit q = yekutieliBond21Trace ((↑q : R) - ↑q⁻¹) := by
  have hab : (↑q : R) * ↑q⁻¹ = 1 := q.mul_inv
  unfold yekutieliBond21Trace_qform_unit yekutieliBond21Trace
  linear_combination -2 * hab

/-- Combining the $V_{(2,1)}$ matrix trace identity with the $\mathrm{SL}_2$
    Cayley–Hamilton cubic trace polynomial yields the full $q$-Laurent
    Borromean character directly from the single local $(2,1)$ bond trace
    (`qou-h5aw`). -/
theorem yekutieli_b3_local_21_bond_qform_unit (q : Rˣ) :
    sl2CubicTrace (yekutieliBond21Trace_qform_unit q)
      = chi21_borromean_qform_unit q := by
  rw [yekutieliBond21Trace_qform_unit_eq_poly q,
      yekutieli_b3_local_21_bond_projection,
      chi21_borromean_qform_unit_eq_poly q]

end Unit

/-! ## Archimedean (`ℚ`) layer — the q-rational form and the form bridge

The q-rational form divides by `q⁶`, so it lives over a field; here `ℚ`. -/

/- §7c base-ring convention: these are pure algebraic identities with no
   ordering and no `Real.*` constructs, so they are stated over a generic
   `{R : Type*} [Field R]` rather than specialised to `ℚ`. `Field` (not
   merely `CommRing`) is the weakest typeclass that admits the genuine
   inverses (`1/q`, negative `q`-powers). `ℚ` is a `Field`, so every existing
   call site still unifies. -/

/-- The standard-irrep Borromean character in its q-rational form. -/
def chi21_borromean_qform {R : Type*} [Field R] (q : R) : R :=
  (-q^12 + 3*q^10 - 3*q^8 + 4*q^6 - 3*q^4 + 3*q^2 - 1) / q^6

/-- The standard-irrep Borromean character in its h-polynomial form,
    `2 − 3h⁴ − h⁶` with `h = q − q⁻¹` (written `q − 1/q`). -/
def chi21_borromean_hform {R : Type*} [Field R] (q : R) : R :=
  2 - 3*(q - 1/q)^4 - (q - 1/q)^6

/-- **The two published forms of `χ^{(2,1)}(β_Bor)` are equal** for every
    non-zero `q` in any field. Pure field identity. -/
theorem chi21_borromean_qform_eq_hform {R : Type*} [Field R] (q : R) (hq : q ≠ 0) :
    chi21_borromean_qform q = chi21_borromean_hform q := by
  unfold chi21_borromean_qform chi21_borromean_hform
  field_simp
  ring

/-- The `ℚ` h-form is exactly the `R[h]` polynomial character
    `chi21_borromean` evaluated at `h = q − q⁻¹`.  Connects the archimedean
    h-form to the faithful `R[h]` object above. -/
theorem chi21_borromean_hform_eq_poly (q : ℚ) :
    chi21_borromean_hform q = chi21_borromean (q - 1/q) := by
  unfold chi21_borromean_hform chi21_borromean
  ring

/-- The h-form is purely even in `h = q − q⁻¹` (bar-invariant under
    `q ↦ q⁻¹`): replacing `q` by `q⁻¹` sends `h ↦ −h` and the even powers
    `h⁴, h⁶` are unchanged. Stated directly as invariance under `q ↦ 1/q`. -/
theorem chi21_borromean_hform_bar_invariant {R : Type*} [Field R] (q : R) (hq : q ≠ 0) :
    chi21_borromean_hform (1 / q) = chi21_borromean_hform q := by
  have hq' : (1 : R) / q ≠ 0 := one_div_ne_zero hq
  unfold chi21_borromean_hform
  field_simp
  ring

/-! ## Payoff — instantiation over `ℤ[q, q⁻¹]` (no field)

`LaurentPolynomial ℤ` is the universal home of the character: `q = T` is a
unit (inverse `T(-1)`), so `chi21_borromean_qform_unit` evaluates there and the
published `/q⁶` form is the genuine Laurent polynomial `2 − 3h⁴ − h⁶`,
`h = T − T⁻¹`.  Witnesses that the `Rˣ` layer is not vacuous over a non-field. -/

section LaurentWitness
open LaurentPolynomial

/-- `T` is a unit of `ℤ[q, q⁻¹] = LaurentPolynomial ℤ`, with inverse `T(-1)`. -/
noncomputable def TUnit : (LaurentPolynomial ℤ)ˣ :=
  Units.mkOfMulEqOne (T 1) (T (-1)) (by rw [← T_add]; simp)

/-- The published Borromean q-rational character instantiated over the
    non-field `ℤ[q, q⁻¹]`: it is the Laurent polynomial `chi21_borromean` at
    `h = T − T⁻¹`.  Concrete witness of `chi21_borromean_qform_unit_eq_poly`
    over a commutative ring that is not a field. -/
theorem chi21_borromean_qform_unit_laurent :
    chi21_borromean_qform_unit TUnit
      = chi21_borromean ((T 1 : LaurentPolynomial ℤ) - T (-1)) :=
  chi21_borromean_qform_unit_eq_poly TUnit

end LaurentWitness

end QOU.BraidsAndKnots
