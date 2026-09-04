import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic


/-!
# QOU.Interactions.QBetaCosResummation — `cos((z-1)h/2)` tightening of Form A

The single-wrap `Q_β^A` prediction (per `prop:neutron-qvalue-symbolic`) admits
a tighter symbolic refinement via the **classical cosine** of the half
eigenphase:

  `Q_β^{A,cos} = Q_β^A · cos((z-1) h / 2)`

This file:

1. Axiomatises the spectral identification (transfer-matrix eigenphase
   `α = (z-1) h / 2` on the 2-d irrep `V_{(2,1)}` of `H_3(q)`) as a Lean
   `class`, since the underlying combinatorial fact lives in
   `prop:beta-decay-transfer-matrix` and is not yet machine-proved.

2. Proves the **Markov-cyclicity constraint**: the resummation must be
   **even** in `α`, hence the leading symmetric series is the cosine.

3. Records the cos-resummation theorem as a conditional result under the
   class, with the polynomial identity at `O(α⁴)` discharged by `ring`.

LaTeX label: `prop:q-beta-cos-resummation`
-/

namespace QOU.Interactions

/-- Markov-Jones parameter `z(q) = 1 / (√q + 1/√q)`. (Defined locally to
    avoid a circular import with `QBetaSpectralBridge`.)

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

/-- Single-wrap transfer-matrix eigenphase on the 2-d irrep `V_{(2,1)}`. -/
noncomputable def eigenphase (q : ℝ) : ℝ := (markovZC q - 1) * heckeH q / 2

/-! ## Markov-cyclicity ⇒ even resummation

`τ_M` is cyclic; under the bar involution `q ↦ q⁻¹` the generator
`σ_i` is sent to `σ_i⁻¹`, hence the eigenphase `α ↦ −α`. Any trace
expression in `α` must therefore be **even**: only `α^{2k}` powers
survive in the resummation. -/

/-- Bar-involution symmetry: `α(q⁻¹) = −α(q)`.

    Reason: `z(q⁻¹) = z(q)` (palindromic in `√q ↔ 1/√q`) but
    `h(q⁻¹) = q⁻¹ − q = −h(q)`. So
    `α(q⁻¹) = (z(q⁻¹) − 1) · h(q⁻¹) / 2 = (z(q) − 1) · (−h(q)) / 2
            = −α(q)`. -/
theorem eigenphase_bar_involution (q : ℝ) (hq : 0 < q) :
    eigenphase q⁻¹ = - eigenphase q := by
  -- Ref: [manuscript] prop:q-beta-cos-resummation §"Markov cyclicity"
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
  unfold eigenphase markovZC heckeH
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
the substrate. Per that trichotomy the only contentful branch is 3 — `M` the
holonomy of an independently-defined connection whose monodromy reproduces the
Hecke braiding (Kohno–Drinfeld / KZ, the canonical chain's "Yekutieli
non-abelian Stokes" step) — with branch 1, `M` in the braid image, *excluded*,
because every character lies in `ℤ[q,q⁻¹]` while `2cos((z−1)h/2)` is
transcendental over `ℚ(q,z)`. That construction is carried out neither here
nor there.

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

/-- The cos resummation is **even** in `α`: under `α ↦ −α`, the value is
    preserved. (Trivially from `cos(−x) = cos x`.) -/
theorem cos_resummation_even (α : ℝ) :
    Real.cos (-α) = Real.cos α := by
  exact Real.cos_neg α

/-- **Q_β cos-resummation theorem** (conditional on `TransferMatrixEigenphase`).
    Given the spectral identification, the Markov-trace symmetrization of the
    two transfer-matrix eigenphases `±α(q)` gives the cosine of the half
    argument, so the refinement of Form A by half the symmetrized character
    is Form A times `cos α`:

      `Q_β^A · (tr M / 2) = Q_β^A · cos α`,  `α = (z(q) − 1) · h(q) / 2`.

    Per §"Markov cyclicity" of `prop:q-beta-cos-resummation`, the resummation
    must be even in `α` (by `eigenphase_bar_involution` + cyclicity of `τ_M`),
    so the cosine is the unique entire even analytic function matching the
    spectral-bridge perturbative expansion at every order.

    **This is a genuine implication**, verified by negative control: drop the
    instance binder and the goal `formA * M.trace * (1/2) = formA * cos α` is
    not provable — `ring` fails on it, as it must. The superseded statement was
    `∃ x, x = A ∧ x = A`, closed by `ring` with the instance binder unused, and
    said nothing about the transfer matrix. Note the implication is genuine
    while its *hypothesis* remains circularly dischargeable; see the section
    note above.

    **Empirical evidence** (from `q-beta-tightening-landscape.witness.json`):
    at `q_0 ≈ 1.110`, the cos-resummed prediction has CODATA residual
    `+305.7 ppm`, compared to `+1677.5 ppm` for bare Form A — a `5.49×`
    tightening. That number is evidence *for the open identification*, not a
    consequence of this theorem. -/
-- Ref: [manuscript] prop:q-beta-cos-resummation
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
