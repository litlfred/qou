import QOU.BraidKnot.HabiroNewtonLadder

/-!
# QOU.BraidKnot.AJFigureEight

**The AJ conjecture at the QOU anchor knot, stated concretely.**

Part of the "AJ in QOU, fully and honestly" tranche
(`docs/audits/2026-07-03-aj-conjecture-dialog-assessment.md`).  The corpus's
existing AJ carrier (`QuantumAPolynomial` in
`stochastic-mechanics/phi-q-aj-machinery-identification.lean`) is a
degree-placeholder; with `coloredJones41` now a concrete Lean object
(`QOU.BraidKnot.HabiroNewtonLadder`, sorry-free), the AJ statement can be
made **content-bearing** for the figure-eight: an explicit q-difference
operator structure, the annihilation property against the actual colored
Jones tower, and the strong-AJ q→1 specialization against the explicit
classical A-polynomial
`A_{4₁}(L, M) = M⁴L² − (M⁸ − M⁶ − 2M⁴ − M² + 1)L + M⁴` (CCGLS tables).

## Honest status (§3b)

* The class `StrongAJFigureEight` carries the literature theorem
  (Ref: [nguyen-tran-2021], strong AJ for 4₁) as §3b class fields, and the
  instance below TRANSCRIBES the explicit operator reconstructed and
  verified corpus-side (`computations/aj_figure_eight_operator_construct_verify.py`).
  Machine-checked sorry-free: the operator data, the q=1 specialization to
  the classical A-polynomial (meridian-squared convention), nontriviality
  (char 0), unit nondegeneracy, and the N = 1 annihilation instance.  The
  ONE remaining `sorry` (cited) is the general-N annihilation — the
  creative-telescoping certificate, verified symbolically for N = 1..12 in
  the witness; formalizing the certificate is the queued follow-up.
* The derived theorems genuinely *derive* (∃-packaging, bar transport via
  the proved `coloredJones41_bar_symmetric`) — they do not merely project a
  class field (§3b-cond non-degeneracy).
* For the Borromean `𝓑₃` the AJ input stays OPEN, consistent with
  `phi-q-aj-machinery-identification.lean` (no instance there either).

## Base ring (§7c)

Generic `{K : Type*} [Field K]` throughout (inverses needed); no `ℝ`, no
ordering, no archimedean constructs.  The q→1 specialization is evaluation
at `1 : K` — algebraic, not a limit.
-/

namespace QOU.BraidKnot.AJFigureEight

open Finset
open QOU.BraidKnot.HabiroNewtonLadder

variable {K : Type*} [Field K]

/-- An (inhomogeneous) q-difference operator acting on color towers:
    `order`, coefficient functions `coeff j q m` of the deformation
    parameter `q` and the multiplication variable `m = q^N`, and an
    inhomogeneous part `rhs q m` (`0` for a homogeneous operator). -/
structure QDifferenceOperator (K : Type*) [Field K] where
  /-- The order (L̂-degree) of the operator. -/
  order : ℕ
  /-- Coefficient of the `j`-th shift, as a function of `(q, m)`. -/
  coeff : ℕ → K → K → K
  /-- Inhomogeneous right-hand side, as a function of `(q, m)`. -/
  rhs : K → K → K

/-- `op` annihilates the tower `J` at deformation parameter `q`:
    `∑_j coeff_j(q, q^N) · J(N+j) = rhs(q, q^N)` for every color `N`. -/
def Annihilates (op : QDifferenceOperator K) (q : K) (J : ℕ → K) : Prop :=
  ∀ N : ℕ,
    ∑ j ∈ Finset.range (op.order + 1), op.coeff j q (q ^ N) * J (N + j)
      = op.rhs q (q ^ N)

/-- Non-triviality of `op` at `q`: the top coefficient is not identically
    zero in `m`. -/
def NontrivialAt (op : QDifferenceOperator K) (q : K) : Prop :=
  ∃ m : K, op.coeff op.order q m ≠ 0

/-- A tower `J` is q-holonomic at `q` when some non-trivial q-difference
    operator annihilates it — the existence half of the AJ machinery
    (a THEOREM for all knots, Garoufalidis–Lê 2005; here stated as the
    target predicate). -/
def IsQHolonomic (q : K) (J : ℕ → K) : Prop :=
  ∃ op : QDifferenceOperator K, NontrivialAt op q ∧ Annihilates op q J

/-- The classical A-polynomial of the figure-eight knot, as an explicit
    two-variable polynomial function (CCGLS tables):
    `A_{4₁}(L, M) = M⁴L² − (M⁸ − M⁶ − 2M⁴ − M² + 1)L + M⁴`. -/
def aPolyFigureEight (L M : K) : K :=
  M ^ 4 * L ^ 2 - (M ^ 8 - M ^ 6 - 2 * M ^ 4 - M ^ 2 + 1) * L + M ^ 4

/-- **Strong AJ for the figure-eight (§3b class; literature theorem,
    instance not fabricated).**  Carries, as content-bearing fields, the
    statement proved in the literature (Ref: [nguyen-tran-2021]): an
    explicit order-2 inhomogeneous q-difference operator annihilates the
    colored Jones tower of `4₁` for every `q ≠ 0`, and its homogeneous part
    evaluated at `q = 1` equals the classical A-polynomial up to a nonzero
    unit factor `unit m`.  Instantiating the class = transcribing the
    explicit Garoufalidis–Koutschan operator and discharging these fields
    (queued; empirical reconstruction in
    `computations/aj_figure_eight_operator_construct_verify.py`). -/
class StrongAJFigureEight (K : Type*) [Field K] where
  /-- The annihilating operator (explicit in the literature). -/
  op : QDifferenceOperator K
  /-- The inhomogeneous presentation has order 2. -/
  order_eq : op.order = 2
  /-- Non-trivial at every `q ≠ 0`. -/
  nontrivial : ∀ q : K, q ≠ 0 → NontrivialAt op q
  /-- Annihilates the (concrete, Lean-defined) colored Jones tower of `4₁`
      at every `q ≠ 0`. -/
  annihilates : ∀ q : K, q ≠ 0 →
    Annihilates op q (coloredJones41 q)
  /-- The strong-AJ unit factor relating the `q = 1` specialization to the
      classical A-polynomial.  For the actual operator it is
      `(M²−1)²(M²+1)/M¹⁶` — an L-free factor in `M`, vanishing at the
      degenerate meridians `M² = ±1`, so nondegeneracy (below) is the
      honest condition, not pointwise nonvanishing. -/
  unit : K → K
  /-- The unit factor is not identically zero (the classical limit is not
      the zero polynomial). -/
  unit_nondegenerate : ∃ m : K, m ≠ 0 ∧ unit m ≠ 0
  /-- **Specialization (the AJ content), meridian-squared convention**:
      at `q = 1`, with `m = M²` (the multiplication variable is the
      square of the meridian eigenvalue — the convention the corpus-side
      verification `aj_figure_eight_operator_construct_verify.py`
      identified; the naive `m = M` map does not match), the homogeneous
      part equals `unit M · A_{4₁}(L, M)`. -/
  specializes : ∀ L M : K, M ≠ 0 →
    op.coeff 2 1 (M ^ 2) * L ^ 2 + op.coeff 1 1 (M ^ 2) * L
        + op.coeff 0 1 (M ^ 2)
      = unit M * aPolyFigureEight L M

/-- **Derived (conditional on the literature class): the figure-eight
    colored Jones tower is q-holonomic at every `q ≠ 0`.**  Genuinely
    derived ∃-packaging of the class data (§3b-cond non-degenerate). -/
theorem coloredJones41_qholonomic [inst : StrongAJFigureEight K]
    {q : K} (hq : q ≠ 0) :
    IsQHolonomic q (coloredJones41 q) :=
  ⟨inst.op, inst.nontrivial q hq, inst.annihilates q hq⟩

/-- **Bar transport of annihilators (unconditional — uses the PROVED bar
    symmetry of the tower).**  Any operator annihilating the figure-eight
    tower at `q⁻¹` annihilates the *same numerical tower* as at `q`: by
    `coloredJones41_bar_symmetric` the two towers coincide pointwise, so
    the bar involution moves annihilators without changing the annihilated
    object.  This is the operator-level face of the amphichirality of
    `4₁`. -/
theorem annihilates_bar_transport (op : QDifferenceOperator K)
    {q : K} (hq : q ≠ 0)
    (h : Annihilates op q⁻¹ (coloredJones41 q⁻¹)) :
    Annihilates op q⁻¹ (coloredJones41 q) := by
  intro N
  have hN := h N
  simpa only [coloredJones41_bar_symmetric hq] using hN

/-- **Derived (conditional): q-holonomicity transports across the bar
    involution** — the tower is q-holonomic at `q⁻¹` with the SAME tower
    values as at `q`. -/
theorem coloredJones41_qholonomic_bar [inst : StrongAJFigureEight K]
    {q : K} (hq : q ≠ 0) :
    IsQHolonomic q⁻¹ (coloredJones41 q) :=
  ⟨inst.op, inst.nontrivial q⁻¹ (inv_ne_zero hq),
    annihilates_bar_transport inst.op hq
      (inst.annihilates q⁻¹ (inv_ne_zero hq))⟩

/-- Sanity: the classical A-polynomial reference is the stated explicit
    polynomial (definitional anchor for reviewers diffing against CCGLS). -/
theorem aPolyFigureEight_def (L M : K) :
    aPolyFigureEight L M
      = M ^ 4 * L ^ 2 - (M ^ 8 - M ^ 6 - 2 * M ^ 4 - M ^ 2 + 1) * L + M ^ 4 :=
  rfl

/-! ## The explicit operator — transcription of the verified reconstruction

Coefficients transcribed verbatim from the corpus-side reconstruction
(`computations/aj_figure_eight_operator_construct_verify.py`, witness
`aj-figure-eight-operator-construct-verify.witness.json`): the canonical
minimal-window (m-degrees `[-8..-1]`, nullity 1) order-2 inhomogeneous
annihilator of the figure-eight colored Jones tower, verified there by
exact symbolic annihilation for `N = 1..12` and by the `q → 1`
specialization to the classical A-polynomial. -/

/-- Coefficient functions of the explicit 4₁ annihilator (`j, q, m`). -/
def feCoeff : ℕ → K → K → K
  | 0, q, m => (m - 1) * (m ^ 2 * q ^ 3 - 1) / m ^ 6
  | 1, q, m => -((m * q - 1) ^ 2 * (m * q + 1)
      * (m ^ 4 * q ^ 4 - m ^ 3 * q ^ 3 - m ^ 2 * q ^ 3 - m ^ 2 * q - m * q + 1))
      / (m ^ 8 * q ^ 2)
  | 2, q, m => (m * q ^ 2 - 1) * (m ^ 2 * q - 1) / m ^ 6
  | _ + 3, _, _ => 0

/-- Inhomogeneous part of the explicit 4₁ annihilator. -/
def feRhs (q m : K) : K :=
  (m * q + 1) * (m ^ 2 * q - 1) * (m ^ 2 * q ^ 3 - 1) / (m ^ 7 * q)

/-- The explicit annihilator of the 4₁ tower, as a `QDifferenceOperator`. -/
def figureEightOperator : QDifferenceOperator K where
  order := 2
  coeff := feCoeff
  rhs := feRhs

/-- The strong-AJ unit factor of the `q = 1` specialization:
    `(M⁶ − M⁴ − M² + 1)/M¹⁶ = (M²−1)²(M²+1)/M¹⁶`. -/
def feUnit (M : K) : K := (M ^ 6 - M ^ 4 - M ^ 2 + 1) / M ^ 16

/-- **Specialization, proved**: at `q = 1` under the meridian-squared
    convention the homogeneous part of the explicit operator equals
    `feUnit M · A_{4₁}(L, M)`. -/
theorem figureEightOperator_specializes (L M : K) (hM : M ≠ 0) :
    (figureEightOperator (K := K)).coeff 2 1 (M ^ 2) * L ^ 2
        + (figureEightOperator (K := K)).coeff 1 1 (M ^ 2) * L
        + (figureEightOperator (K := K)).coeff 0 1 (M ^ 2)
      = feUnit M * aPolyFigureEight L M := by
  show feCoeff 2 1 (M ^ 2) * L ^ 2 + feCoeff 1 1 (M ^ 2) * L
      + feCoeff 0 1 (M ^ 2) = feUnit M * aPolyFigureEight L M
  simp only [feCoeff, feUnit, aPolyFigureEight]
  field_simp
  ring

/-- The unit factor is not identically zero (witness `M = 2`). -/
theorem feUnit_nondegenerate [CharZero K] :
    ∃ m : K, m ≠ 0 ∧ feUnit (K := K) m ≠ 0 := by
  refine ⟨2, by norm_num, ?_⟩
  simp only [feUnit]
  rw [div_ne_zero_iff]
  norm_num

/-- **Nontriviality, proved** (char 0): for every `q ≠ 0` the top
    coefficient is nonzero somewhere — witness `m = −1/q²` generically,
    `m = −2/q²` when `q³ = 1`. -/
theorem figureEightOperator_nontrivial [CharZero K] {q : K} (hq : q ≠ 0) :
    NontrivialAt (figureEightOperator (K := K)) q := by
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero _ hq
  have hq3 : q ^ 3 ≠ 0 := pow_ne_zero _ hq
  by_cases h1 : q ^ 3 = 1
  · refine ⟨-2 / q ^ 2, ?_⟩
    show feCoeff 2 q (-2 / q ^ 2) ≠ 0
    have hm : (-2 : K) / q ^ 2 ≠ 0 := by
      exact div_ne_zero (by norm_num) hq2
    have hA : (-2 : K) / q ^ 2 * q ^ 2 - 1 = -3 := by
      rw [div_mul_cancel₀ _ hq2]; ring
    have hB : ((-2 : K) / q ^ 2) ^ 2 * q - 1 = 3 := by
      have : ((-2 : K) / q ^ 2) ^ 2 * q = 4 / q ^ 3 := by
        field_simp
        ring
      rw [this, h1]; norm_num
    simp only [feCoeff]
    rw [div_ne_zero_iff]
    constructor
    · rw [hA, hB]; norm_num
    · exact pow_ne_zero _ hm
  · refine ⟨-1 / q ^ 2, ?_⟩
    show feCoeff 2 q (-1 / q ^ 2) ≠ 0
    have hm : (-1 : K) / q ^ 2 ≠ 0 := by
      exact div_ne_zero (by norm_num) hq2
    have hA : (-1 : K) / q ^ 2 * q ^ 2 - 1 = -2 := by
      rw [div_mul_cancel₀ _ hq2]; ring
    have hB : ((-1 : K) / q ^ 2) ^ 2 * q - 1 ≠ 0 := by
      have hval : ((-1 : K) / q ^ 2) ^ 2 * q = 1 / q ^ 3 := by
        field_simp
      rw [hval, sub_ne_zero]
      intro h
      apply h1
      field_simp at h
      all_goals first
        | exact h
        | exact h.symm
    simp only [feCoeff]
    rw [div_ne_zero_iff]
    exact ⟨mul_ne_zero (by rw [hA]; norm_num) hB, pow_ne_zero _ hm⟩

/-- **Concrete-color annihilation, proved for N = 1**: the transcribed
    operator annihilates the tower at its base color — machine-checked
    (the general-`N` statement is the literature theorem carried by the
    class instance below; `N = 1..12` are verified symbolically in the
    witness). -/
theorem figureEightOperator_annihilates_one {q : K} (hq : q ≠ 0) :
    ∑ j ∈ Finset.range (2 + 1),
        (figureEightOperator (K := K)).coeff j q (q ^ 1)
          * coloredJones41 q (1 + j)
      = (figureEightOperator (K := K)).rhs q (q ^ 1) := by
  show ∑ j ∈ Finset.range 3, feCoeff j q (q ^ 1) * coloredJones41 q (1 + j)
      = feRhs q (q ^ 1)
  have h2 : q ^ 2 ≠ 0 := pow_ne_zero _ hq
  have h3 : q ^ 3 ≠ 0 := pow_ne_zero _ hq
  have h4 : q ^ 4 ≠ 0 := pow_ne_zero _ hq
  have h5 : q ^ 5 ≠ 0 := pow_ne_zero _ hq
  simp only [Finset.sum_range_succ, Finset.sum_range_zero, feCoeff, feRhs,
    coloredJones41, habiroTerm, Finset.prod_range_succ, Finset.prod_range_zero]
  field_simp
  ring

/-- The 4₁ qZeilberger certificate, factored form (poles at `y = x, qx`):
    `Cert(q,x,y) = −y(qx+1)(qx²−1)(q³x²−1)(1−x)(1−qx)/(q·x⁷·(y−x)(y−qx))`.
    Computed and verified corpus-side
    (`computations/aj_figure_eight_certificate.py`). -/
def feCert (q x y : K) : K :=
  -(y * (q * x + 1) * (q * x ^ 2 - 1) * (q ^ 3 * x ^ 2 - 1)
      * (1 - x) * (1 - q * x))
    / (q * x ^ 7 * (y - x) * (y - q * x))

/-- **Boundary identity, proved (fraction form)**: the operator's
    inhomogeneous part is the certificate's boundary value,
    `rhs(q,x) = −Cert(q,x,1)` — the content is the cancellation of the
    `(1−x)(1−qx)` factors, hence the hypotheses. -/
theorem feCert_boundary (q x : K) (hq : q ≠ 0) (hx : x ≠ 0)
    (h1x : x ≠ 1) (hqx : q * x ≠ 1) :
    feRhs q x = -feCert q x 1 := by
  have h1 : (1 : K) - x ≠ 0 := sub_ne_zero.mpr (Ne.symm h1x)
  have h2 : (1 : K) - q * x ≠ 0 := sub_ne_zero.mpr (Ne.symm hqx)
  have hd1 : x ^ 7 * q ≠ 0 := mul_ne_zero (pow_ne_zero _ hx) hq
  have hd2 : q * x ^ 7 * ((1 : K) - x) * (1 - q * x) ≠ 0 :=
    mul_ne_zero (mul_ne_zero (mul_ne_zero hq (pow_ne_zero _ hx)) h1) h2
  simp only [feRhs, feCert, neg_div, neg_neg]
  rw [div_eq_div_iff hd1 hd2]
  ring

/-- **The literature instance (strong AJ for 4₁), transcribed.**  Every
    field except the general-`N` annihilation is machine-checked above;
    the annihilation for all `N` is the theorem proved in the literature
    and verified symbolically for `N = 1..12` in the corpus witness.
    The certificate's mathematical content is Lean-proved sorry-free in
    `QOU.BraidKnot.AJFigureEightCertificate` (`feCert_local_identity_cleared`,
    `feCert_boundary_cleared` — denominator-cleared pure ring identities);
    the residual gap is the shift-ratio/telescope bookkeeping. -/
instance [CharZero K] : StrongAJFigureEight K where
  op := figureEightOperator
  order_eq := rfl
  nontrivial := fun _ hq => figureEightOperator_nontrivial hq
  annihilates := fun _ _ =>
    -- Ref: [nguyen-tran-2021] https://doi.org/10.1007/s40306-020-00401-2
    -- (strong AJ proved for 4_1; corpus-side exact symbolic verification
    --  N=1..12: aj-figure-eight-operator-construct-verify.witness.json;
    --  the N=1 case is figureEightOperator_annihilates_one above)
    sorry
  unit := feUnit
  unit_nondegenerate := feUnit_nondegenerate
  specializes := figureEightOperator_specializes

end QOU.BraidKnot.AJFigureEight
