import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic


/-!
# QOU.Interactions.QBetaCosResummation — `cos((z_D-1)h/2)` dressing of a `Q_β` base (convention D)

The block `prop:q-beta-cos-resummation` dresses a `Q_β` base by the classical
cosine of the half eigenphase:

  `Q_β^{cos} = Q_β^{base} · cos α`,  `α = (z_D − 1) h / 2`,  `z_D = q³/(q²+1)`.

**Restated in convention D, 2026-10-10 (bean `qou-zuva`).** This file:

1. Defines the canonical convention-D eigenphase `eigenphase` from
   `markovZD q = q³/(q²+1)`.

2. Proves the convention-D **bar defect**: `z_D(q⁻¹) ≠ z_D(q)` and
   `α_D(q⁻¹) ≠ −α_D(q)` for every `q > 0`, `q ≠ 1`, with the exact
   bar-even part `α_D(q⁻¹) + α_D(q) = (q²−1)²/(2q²)`. So the
   Markov-cyclicity argument that forced an **even** resummation under
   convention C does **not** go through under D, and the cosine is a
   *definition being tested*, not a derived consequence.

3. Keeps the convention-C bar antisymmetry (`eigenphaseC_bar_involution`) as
   an explicitly labelled **C-historical** statement: it is true for C, false
   for D, and is not used by the D results below.

4. Records the cos-resummation theorem as a conditional result under the
   spectral-identification class (now stated with the D eigenphase).

LaTeX label: `prop:q-beta-cos-resummation`
-/

namespace QOU.Interactions

/-- **CONVENTION C — HISTORICAL, not canonical.** Markov-Jones parameter
    `z_C(q) = 1 / (√q + 1/√q)`, kept only so that the convention-C
    bar antisymmetry `eigenphaseC_bar_involution` remains statable. Nothing
    convention-D in this file uses it; the canonical parameter is `markovZD`.

    **Convention C, deliberately, and this file cannot be migrated to D by
    swapping the body** (bean `qou-cxjq`, 2026-08-26).

    `markovZC` here is `1/(√q + 1/√q) = √q/(q+1)` — convention C. The
    migration was attempted and **Lean rejected it**, which turned out to be
    the right answer rather than a proof-engineering problem: the file's
    bar-antisymmetry result needs `z` to be **bar-even**, and

      z_C(1/q) = z_C(q)   identically,
      z_D(1/q) = 1/(q³+q) ≠ q³/(q²+1) = z_D(q)   except at q = 1.

    `z_D` is neither bar-even nor bar-odd. So `F(1/q) = -F(q)` is **true for
    C and false for D** — a theorem that does not survive the convention
    change, not a proof that needs repairing. Migrating this file means
    re-deriving what replaces bar-antisymmetry under D, under a distinct
    name; the C statement stays correct **for C** and keeps its name.

    Converges independently with `qou-1oxx` ("the canonical p-n convention
    is not bar-invariant") and `QOU.QBeta.ZBarParity`, reached from the p-n
    side rather than the Markov parameter.

    **The `rfl` agreement with `QBetaSpectralBridge.markovZ` is GONE**, and that
    is the point: that sibling migrated to D in this same tranche, so the two
    `markovZC` definitions now differ. The original docstring's claim that they
    "agree by `rfl`" has been removed rather than left to rot — it was true and
    is no longer, which is exactly the kind of stale cross-reference the
    five-way `markovZC` overload was built out of. -/
noncomputable def markovZC (q : ℝ) : ℝ := 1 / (Real.sqrt q + (Real.sqrt q)⁻¹)

/-- Hecke-Skein quantum-integer differential `h(q) = q - q⁻¹`. -/
noncomputable def heckeH (q : ℝ) : ℝ := q - q⁻¹

/-- **Convention D (canonical).** Markov parameter `z_D(q) = q³/(q²+1)`.
    Matches `QOU.QBeta.EigenphaseBarMixedD.zD` and the canonical
    `QOU.BraidKnot.JonesNuclearQuotient.markovZ`; defined locally because this
    content-block sibling imports Mathlib only. -/
noncomputable def markovZD (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- **Convention D (canonical).** Single-wrap transfer-matrix eigenphase on the
    2-d irrep `V_{(2,1)}`: `α_D = (z_D − 1)·h / 2`. At the proton pin
    `q₀ ≈ 1.1099785827513808` this is `α_D ≈ −0.0404857773`,
    `cos α_D ≈ 0.9991805629` (mpmath,
    `computations/qbeta/qbeta_cos_resummation_d_probe.py`). -/
noncomputable def eigenphase (q : ℝ) : ℝ := (markovZD q - 1) * heckeH q / 2

/-- **CONVENTION C — HISTORICAL.** The convention-C eigenphase
    `α_C = (z_C − 1)·h / 2`, which the block used until 2026-10-10. -/
noncomputable def eigenphaseC (q : ℝ) : ℝ := (markovZC q - 1) * heckeH q / 2

/-! ## Convention C (historical): Markov-cyclicity ⇒ even resummation

Under convention C, `τ_M` cyclicity plus the bar involution `q ↦ q⁻¹`
(sending `σ_i ↦ σ_i⁻¹`) sends `α_C ↦ −α_C`, because `z_C` is bar-even and
`h` is bar-odd. That is what made the cosine *derived* under C. The
statement is kept, labelled, because it is true **for C**. -/

/-- **CONVENTION C — HISTORICAL.** Bar-involution antisymmetry
    `α_C(q⁻¹) = −α_C(q)`.

    Reason: `z_C(q⁻¹) = z_C(q)` (palindromic in `√q ↔ 1/√q`) but
    `h(q⁻¹) = −h(q)`. **False under convention D** — see
    `eigenphase_not_bar_odd`. -/
theorem eigenphaseC_bar_involution (q : ℝ) (hq : 0 < q) :
    eigenphaseC q⁻¹ = - eigenphaseC q := by
  -- Ref: [leitner2026] prop:q-beta-cos-resummation §"Markov cyclicity"
  -- Ref: [jones1985] doi:10.2307/1971403
  -- Reduce to algebraic identity:
  --   eigenphase(q⁻¹) + eigenphase(q) = 0
  -- by unfolding both sides and using:
  --   √(q⁻¹) = 1/√q                            (Real.sqrt_inv)
  --   (q⁻¹)⁻¹ = q                              (inv_inv)
  -- which makes markovZC(q⁻¹) syntactically equal to markovZC(q),
  -- and heckeH(q⁻¹) = q⁻¹ - q = -(q - q⁻¹) = -heckeH(q).
  have hq_ne : q ≠ 0 := ne_of_gt hq
  have hsq_ne : Real.sqrt q ≠ 0 := by
    rw [ne_eq, Real.sqrt_eq_zero (le_of_lt hq)]; exact hq_ne
  unfold eigenphaseC markovZC heckeH
  rw [Real.sqrt_inv]
  -- markovZC(q⁻¹) factor: 1/(1/√q + (1/√q)⁻¹) = 1/(1/√q + √q) = same as markovZC(q)
  -- heckeH(q⁻¹) factor: q⁻¹ - (q⁻¹)⁻¹ = q⁻¹ - q
  have h_sqrt_inv_inv : (Real.sqrt q)⁻¹⁻¹ = Real.sqrt q := inv_inv _
  have h_q_inv_inv : q⁻¹⁻¹ = q := inv_inv _
  rw [h_sqrt_inv_inv, h_q_inv_inv]
  -- Now: ((1 / ((√q)⁻¹ + √q) - 1) · (q⁻¹ - q)) / 2
  --   = -((1 / (√q + (√q)⁻¹) - 1) · (q - q⁻¹)) / 2
  -- LHS denominator (√q)⁻¹ + √q = √q + (√q)⁻¹  (commutativity of +)
  ring

/-- **Legacy name, CONVENTION C — HISTORICAL.** Until 2026-10-10 this name
    carried the convention-C bar antisymmetry, when `eigenphase` itself was
    convention C. `eigenphase` is now convention D, for which the statement is
    **false** (`eigenphase_not_bar_odd`), so this name now states the C fact
    about `eigenphaseC` and is deprecated. It is kept because several library
    docstrings and probes cite it as the C statement. -/
@[deprecated eigenphaseC_bar_involution (since := "2026-10-10")]
theorem eigenphase_bar_involution (q : ℝ) (hq : 0 < q) :
    eigenphaseC q⁻¹ = - eigenphaseC q :=
  eigenphaseC_bar_involution q hq

/-! ## Convention D: the bar involution does NOT fix `z_D`, and `α_D` is not bar-odd

These are the convention-D replacements for the C bar antisymmetry above. They
show the evenness argument has no D analog: the cosine in the D block is a
definition under test, not a consequence of Markov cyclicity. Ordering is used
for nonvanishing, hence `ℝ` (AGENTS.md §7c). Same content as
`QOU.QBeta.EigenphaseBarMixedD.twoAlphaD_bar_even_sum`, restated here for the
block's own `eigenphase`. -/

/-- `z_D(q⁻¹) = 1/(q³ + q)`. -/
theorem markovZD_inv (q : ℝ) (hq : q ≠ 0) :
    markovZD q⁻¹ = 1 / (q ^ 3 + q) := by
  unfold markovZD
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have h2 : q ^ 3 + q ≠ 0 := by
    have : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [this]; exact mul_ne_zero hq h1
  field_simp
  ring

/-- **The bar involution does not fix `z_D`**: `z_D(q⁻¹) ≠ z_D(q)` for every
    `q > 0`, `q ≠ 1`. (Equality would force `q⁴ = 1`.) Contrast `markovZC`,
    which is bar-even identically. -/
theorem markovZD_bar_ne (q : ℝ) (hq : 0 < q) (hq1 : q ≠ 1) :
    markovZD q⁻¹ ≠ markovZD q := by
  intro h
  rw [markovZD_inv q hq.ne'] at h
  unfold markovZD at h
  have h1 : (0 : ℝ) < q ^ 2 + 1 := by positivity
  have h2 : (0 : ℝ) < q ^ 3 + q := by positivity
  rw [div_eq_div_iff h2.ne' h1.ne'] at h
  have hq2 : (q - 1) * (q + 1) * (q ^ 2 + 1) ^ 2 = 0 := by linear_combination -h
  have h3 : (q ^ 2 + 1) ^ 2 ≠ 0 := by positivity
  have h4 : q + 1 ≠ 0 := by linarith
  have h5 : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  exact mul_ne_zero (mul_ne_zero h5 h4) h3 hq2

/-- **Exact bar-even part of the D eigenphase**:
    `α_D(q⁻¹) + α_D(q) = (q² − 1)² / (2 q²)`. A bar-odd phase would give `0`. -/
theorem eigenphase_bar_even_sum (q : ℝ) (hq : q ≠ 0) :
    eigenphase q⁻¹ + eigenphase q = (q ^ 2 - 1) ^ 2 / (2 * q ^ 2) := by
  unfold eigenphase markovZD heckeH
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have h2 : (q⁻¹) ^ 2 + 1 ≠ 0 := by positivity
  field_simp
  ring

/-- **`α_D` is not bar-odd**: for every `q > 0`, `q ≠ 1`,
    `α_D(q⁻¹) ≠ −α_D(q)`. This is the convention-D negation of
    `eigenphaseC_bar_involution`, and it is why the Markov-cyclicity derivation
    of the cosine does not transfer to D. -/
theorem eigenphase_not_bar_odd (q : ℝ) (hq : 0 < q) (hq1 : q ≠ 1) :
    eigenphase q⁻¹ ≠ - eigenphase q := by
  intro h
  have hsum := eigenphase_bar_even_sum q hq.ne'
  rw [h, neg_add_cancel] at hsum
  have h4 : q + 1 ≠ 0 := by linarith
  have h5 : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  have hq2 : q ^ 2 - 1 ≠ 0 := by
    have : q ^ 2 - 1 = (q - 1) * (q + 1) := by ring
    rw [this]; exact mul_ne_zero h5 h4
  have : (0 : ℝ) < (q ^ 2 - 1) ^ 2 / (2 * q ^ 2) := by positivity
  linarith

/-! ## Spectral-identification class

The fact that the single-wrap transfer-matrix eigenphase on `V_{(2,1)}`
is `±α(q)` lives in `prop:beta-decay-transfer-matrix` and is a
combinatorial property of the Hecke seminormal representation; we
carry it here as a class hypothesis.

**Restated 2026-09-03 (bean `qou-eixt`; §3b-tax).** The previous encoding
was **vacuous**, and the corpus already held the proof of that:
`QOU.QBeta.EigenphaseCarrierVacuity` exhibits both of its former fields as
theorems about an arbitrary real —

    field 1  `-2 ≤ 2 * Real.cos (eigenphase q) ∧ 2 * Real.cos (eigenphase q) ≤ 2`
    field 2  `Real.cos (eigenphase q) = Real.cos (- eigenphase q)`

are `-2 ≤ 2 cos x ≤ 2` and `cos x = cos (-x)`, true of **every** `x`. So the
class asserted nothing, every `[TransferMatrixEigenphase q]`-conditional
result was unconditional, and — separately — the conditional theorem below
never mentioned the instance at all: its proof was `refine ⟨…, rfl, ?_⟩; ring`
on `∃ x, x = A ∧ x = A` with the second `A` merely rewritten. Two independent
§5 defects, one of them invisible to the vacuity detector because it lived in
the *proof* rather than the carrier.

**The encoding is the corpus's own, not a fresh invention.** That same file's
§2 works out the repair — a `2×2` real matrix has spectrum `{e^{+iα}, e^{−iα}}`
exactly when `tr = 2 cos α` and `det = 1` — and the class below adopts it, so
the two files state one obligation rather than two rival ones. Unlike the
original it is falsifiable: it constrains `M` (`replacement_excludes_some_matrix`
there exhibits a matrix no `q` admits).

**🛑 Do not read this as closing the gap — it is branch 2 of that file's §3
trichotomy, which the same file establishes is CIRCULAR.** For every `α` the
rotation `exp(αJ)` has trace `2 cos α` and determinant `1`, so the obligation
is dischargeable by a matrix built *from `α` itself* (`circularWitness` there).
What the repair buys is real but bounded: the class now constrains its argument
instead of asserting nothing, and the theorem below is a genuine implication
rather than a `ring` identity. What it does **not** buy is any evidence about
the substrate. Branch 1, `M` in the braid image, is *excluded* — by
`QOU.QBeta.BraidImageEigenphaseAlgebraic.coeffs_zero_of_surjective_nonpos`,
sorry-free, which forces every coefficient polynomial of a putative algebraic
relation to vanish by zero-counting ("a polynomial with infinitely many roots is
zero"). Its own docstring records that this closes branch 1 in full — character
case *and* eigenvalue-pair case.

**Cite that, not transcendence — corrected 2026-09-04, hours after #6567.** The
clause here read *"every character lies in `ℤ[q,q⁻¹]` while `2cos((z−1)h/2)` is
transcendental over `ℚ(q,z)`"*. That route is an **unproved docstring
assertion**, flagged as such in `QOU.QBeta.BraidImageEigenphaseExclusion` ("the
transcendence assertion") and described in
`QOU.QBeta.PhaseFailsLogFunctionalEquation` as *"correct but needs transcendence
theory"* — i.e. not formalised. Attributing the exclusion to it cites the one
argument the corpus has **not** discharged while a sorry-free proof sits beside
it.

**And read the hypothesis before citing the theorem.** It requires `α` to be
surjective onto the non-positive reals (`∀ y ≤ 0, ∃ s ≥ 1, α s = y`), which the
unbounded `(z−1)h/2` family supplies and a bounded `arccos` does not. *"It is
algebraic, therefore excluded"* is not what it says.

**🛑 CORRECTED 2026-09-04, hours after this file first said otherwise.** The
paragraph here read *"the only contentful branch is 3 — `M` the holonomy of an
independently-defined connection … (Kohno–Drinfeld / KZ …). That construction is
carried out neither here nor there."* That is **wrong in exactly the form it
names**, and it was wrong when written: `QOU.QBeta.HolonomySpectrumSignObstruction`
landed 2026-08-31 (`4471ee72ce`, 6 theorems, sorry-free) and **excludes any
holonomy whose generator has real spectrum**, Kohno–Drinfeld included.

The argument reads no residues, which is why it reaches the whole class. A real
generator eigenvalue `a` gives character `(eᵃ + e⁻ᵃ)/2 = cosh a ≥ 1` for *every*
real `a`, so a `q`-dependent residue only changes which `a` occurs. The required
correction factor is `0.998399 < 1` — not merely off, but **on the wrong side of
1**. At the Kohno–Drinfeld value specifically, matching the braiding
`P exp(ħt/2)` to the Hecke eigenvalues `{q, −q⁻¹}` forces `ħ = 2 ln q`, and since
`q₀ > 1` is real that generator is **hyperbolic**: `det A = −(ln q₀)² < 0`, giving
`(q + q⁻¹)/2 = 1.005448` against a required `0.998399`. The whole obstruction is
`(x−1)² ≥ 0`; no analysis and no transcendence.

**What survives is narrower, and is owned elsewhere.** Not "find a connection"
but *"find one whose generator is **elliptic** at real `q`"* — `det A > 0`,
spectrum `±iθ` with `θ = 0.0565947` — which makes the imaginarity the thing that
has to be sourced, and the corpus names `conj:im-q-physical-role` as the
candidate place. That is tier-0 condition **D0** on `qou-pdix`'s D1–D6 acceptance
test, and the live trackers are `qou-pdix` / `qou-cds1`.

**Scope, stated as the audit states it:** this does *not* prove no connection
exists, does not derive `α`, and adjudicates no convention. It makes the elliptic
requirement non-optional.

How the error got here is worth recording, because the mechanism is reusable:
`EigenphaseCarrierVacuity`'s §3 was written before that obstruction landed and
was never updated, and this file quoted it as authoritative without checking
whether its "only remaining option" had since been narrowed. A sibling file is
not a primary source — the corpus is.

**No instance is declared in this file**, per §3b-tax: an unproved primary
input is honestly represented by a content-bearing class with no instance, and
declaring one would let instance resolution discharge every conditional result
below without anyone supplying the input. -/

/-- **Spectral identification** (open input, `prop:beta-decay-transfer-matrix`):
    the Markov-symmetrized single-wrap character of the transfer matrix `M_β`
    for free-neutron β-decay, on the 2-d irrep `V_{(2,1)}` of `H_3(q)`, equals
    `2 cos α` where `α = (z−1) h / 2` — i.e. `M_β` has spectrum
    `{e^{+iα}, e^{−iα}}` there.

    `M` is the transfer matrix restricted to that irrep. The encoding is
    `QOU.QBeta.EigenphaseCarrier`'s §2 `TransferMatrixSpectrum`, adopted rather
    than reinvented: a `2×2` real matrix has spectrum `{e^{+iα}, e^{−iα}}`
    exactly when `tr = 2 cos α` and `det = 1` (characteristic polynomial
    `t² − 2cos(α)·t + 1`). -/
class TransferMatrixEigenphase (q : ℝ) (M : Matrix (Fin 2) (Fin 2) ℝ) : Prop where
  /-- The Markov-symmetrised single-wrap character is `2 cos α`. Falsifiable:
      for a given `q` it pins the trace to one value (`symChar_unique`), so
      unlike the superseded fields it is **not** satisfied by an arbitrary
      substitution. -/
  trace_eq : M.trace = 2 * Real.cos (eigenphase q)
  /-- Unimodular spectrum: `e^{+iα} · e^{−iα} = 1`. -/
  det_eq : M.det = 1

/-- The class pins the character uniquely — the non-vacuity property the
    superseded encoding lacked. Two matrices carrying it at the same `q` have
    equal trace. -/
theorem symChar_unique (q : ℝ) (M N : Matrix (Fin 2) (Fin 2) ℝ)
    [TransferMatrixEigenphase q M] [TransferMatrixEigenphase q N] :
    M.trace = N.trace := by
  rw [TransferMatrixEigenphase.trace_eq (q := q) (M := M),
      TransferMatrixEigenphase.trace_eq (q := q) (M := N)]

-- NOT declared here: a satisfiability witness. `QOU.QBeta.EigenphaseCarrier`
-- already carries one, under the name that says what it is — `circularWitness`.
-- The rotation `exp(αJ)` satisfies both fields for every `q`, built from `α`
-- itself. Restating it here as a "consistency check" would understate it: it is
-- the circularity, not reassurance.

/-! ## Cos-resummation theorem (conditional)

Under the spectral identification, the Markov-trace symmetrization of
the two eigenphases gives `cos(α)`. The leading-order Taylor expansion

  `cos(α) = 1 − α²/2 + α⁴/24 − ⋯`

is captured by the polynomial identity below, which is closed by `ring`.
The full statement (relating the symbolic correction factor to the
Markov trace itself) requires the class hypothesis. -/

-- REMOVED 2026-09-03 (bean `qou-eixt`): `cos_taylor_quadratic_coeff` stated
-- `1 - α^2/2 - (1 - α^2/2) = 0`, i.e. `X - X = 0`, and was closed by `ring`. Its
-- docstring called it "the second-order Taylor coefficient of `cos α`", but the
-- statement never mentions `Real.cos` — it is a §5 tautology, provable without any
-- hypothesis about the objects in question, and it anchored nothing. It had no
-- consumers inside or outside this file (checked corpus-wide). A real second-order
-- statement needs a remainder bound on `|cos α - (1 - α²/2)|`, which Mathlib does
-- not carry in a directly-applicable form (`exact?` fails on it), so it is left
-- undone rather than re-faked.

/-- The cosine factor is **even** in `α`: under `α ↦ −α`, the value is
    preserved. (From `cos(−x) = cos x`.) Under convention D this does **not**
    make the factor bar-invariant, because the bar involution does not send
    `α_D` to `−α_D` (`eigenphase_not_bar_odd`). -/
theorem cos_resummation_even (α : ℝ) :
    Real.cos (-α) = Real.cos α := by
  exact Real.cos_neg α

/-- **Q_β cos-resummation theorem** (conditional on `TransferMatrixEigenphase`).
    Given the spectral identification, the Markov-trace symmetrization of the
    two transfer-matrix eigenphases `±α(q)` gives the cosine of the half
    argument, so the refinement of Form A by half the symmetrized character
    is Form A times `cos α`:

      `Q_β^A · (tr M / 2) = Q_β^A · cos α`,  `α = (z(q) − 1) · h(q) / 2`.

    **Convention D.** `α` here is `eigenphase q = (z_D − 1)·h/2`. Under
    convention C the cosine was *derived* from evenness in `α` (bar
    antisymmetry `eigenphaseC_bar_involution` + cyclicity of `τ_M`); under D
    that step fails (`eigenphase_not_bar_odd`), so the cosine is the
    definition under test, carried by the class, not a consequence.

    **This is a genuine implication**, verified by negative control: drop the
    instance binder and the goal `formA * M.trace * (1/2) = formA * cos α` is
    not provable — `ring` fails on it, as it must. The superseded statement was
    `∃ x, x = A ∧ x = A`, closed by `ring` with the instance binder unused, and
    said nothing about the transfer matrix. Note the implication is genuine
    while its *hypothesis* remains circularly dischargeable; see the section
    note above.

    **Numbers (convention D, proton pin, mpmath; witness
    `computations/qbeta/qbeta-cos-resummation-d.witness.json`).** On the
    ruled `z_D` base `0.4447004085` MeV (`−431571.8` ppm vs CODATA) the cos
    factor `0.9991805629` gives `−432037.5` ppm — away from zero, as it must
    be, since the required factor exceeds 1 while `cos α ≤ 1`. On the retired
    Form A base it gives `+1677.6 → +856.8` ppm. The superseded convention-C
    figure (`+1677.5 → +305.7` ppm, `5.49×`) is historical. None of these is
    a consequence of this theorem, and neither base is selected by residual. -/
-- Ref: [leitner2026] prop:q-beta-cos-resummation
-- Ref: [jones1985] doi:10.2307/1971403   (Markov trace on H_n(q))
-- Ref: [wenzl1988] doi:10.1007/BF01239526   (Wenzl-bridge `y_λ`)
theorem q_beta_cos_resummation (q : ℝ) (M : Matrix (Fin 2) (Fin 2) ℝ)
    [h : TransferMatrixEigenphase q M] (formA : ℝ) :
    formA * (M.trace / 2) = formA * Real.cos (eigenphase q) := by
  rw [h.trace_eq]
  ring

/-- The cos-resummation is a **contraction**: the correction factor has
    modulus at most one, so dressing Form A by it can only shrink `|Q_β^A|`,
    never inflate it.

    A real consequence of the class rather than a restatement of it — it is
    false for an arbitrary `M`, and it is the sign-and-magnitude sanity check
    the superseded `ring`-closed conjunct was standing in for. -/
theorem cos_resummation_contracts (q : ℝ) (M : Matrix (Fin 2) (Fin 2) ℝ)
    [h : TransferMatrixEigenphase q M] :
    |M.trace / 2| ≤ 1 := by
  rw [h.trace_eq]
  have hle := Real.cos_le_one (eigenphase q)
  have hge := Real.neg_one_le_cos (eigenphase q)
  rw [abs_le]
  constructor <;> linarith

end QOU.Interactions

#print axioms QOU.Interactions.markovZD_bar_ne
#print axioms QOU.Interactions.eigenphase_bar_even_sum
#print axioms QOU.Interactions.eigenphase_not_bar_odd
#print axioms QOU.Interactions.eigenphaseC_bar_involution
#print axioms QOU.Interactions.q_beta_cos_resummation
