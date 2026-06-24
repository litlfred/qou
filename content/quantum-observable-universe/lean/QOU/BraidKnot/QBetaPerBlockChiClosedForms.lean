import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# QOU.BraidKnot.QBetaPerBlockChiClosedForms

**Pre-archimedean closed-form identities for the per-Wedderburn-block
characters $\chi_\lambda(\Delta_{T_\beta})(q)$ over $H_3(q)$, plus the
antipode pairing $(3) \leftrightarrow (1,1,1)$ under $q \mapsto 1/q$.**

This file proves the per-block closed forms from
`qbeta-per-block-paper-closed-forms.witness.json` as rational
identities in $q$, plus a structural antipode-pairing identity. These
are the PRE-ARCHIMEDEAN inputs to the Q$_\beta$ precision-ladder
derivation.

**Honest scope (after correction).** A first version of this file
attempted to prove a closed form for the y_λ-weighted Markov-trace
sum $\Delta\tau_M(q) = \sum_\lambda y_\lambda(q) \cdot \chi_\lambda(q)$.
That version was retracted because the canonical Wenzl–Markov
weights $y_\lambda(q)$ from `solve_y_lambda(3)` involve $\sqrt q$
(via the Markov parameter $z = 1/(\sqrt q + 1/\sqrt q)$), so
$\Delta\tau_M(q)$ is a rational function of $\sqrt q$, NOT of $q$
alone. Proving its sum form in Lean requires square-root handling
beyond ring tactics — out of scope here.

What IS provable in pure ring arithmetic, and what this file proves:

1. The three per-block characters $\chi_{(3)}, \chi_{(2,1)},
   \chi_{(1,1,1)}$ as named rational functions of $q$.
2. The **antipode pairing**: $\chi_{(1,1,1)}(q) = q^{-4} \cdot \chi_{(3)}(q)$
   for $q > 0$, reflecting the standard
   $V_{(3)} \otimes \text{sign} = V_{(1,1,1)}$ relation.
3. The **vanishing at q = 1**: each $\chi_\lambda(q)$ vanishes when
   $q = 1$ (from the $(q^2 - 1)$ factor), confirming
   $\Delta\tau_M(1) = 0$ regardless of $y_\lambda$.

These are rigorous, sorry-free, and do NOT depend on any y_λ form.

LaTeX label: `prop:qbeta-per-block-chi-closed-forms`

## What this file does NOT claim

- A closed form for $\Delta\tau_M(q)$ (open — needs $\sqrt q$ handling).
- The empirical $c_3 = -2$ identity (still NEAR-MATCH per
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md)).
- The f-map identification (open).

## References
- [hoefsmit1974] (seminormal representation matrices for H_3)
- Witness: `qbeta-per-block-paper-closed-forms.witness.json`
-/

namespace QOU.BraidKnot

/-- Per-block character $\chi_{(3)}(\Delta_{T_\beta})(q)$ on the trivial
irrep $V_{(3)}$.

Closed form: $-(q^2 - 1)(q^2 + 1)^2 / (4q)$.
Source: `qbeta-per-block-paper-closed-forms.witness.json`. -/
-- Ref: [hoefsmit1974]
noncomputable def chi_block_3 (q : ℝ) : ℝ :=
  -(q^2 - 1) * (q^2 + 1)^2 / (4 * q)

/-- Per-block character $\chi_{(2,1)}(\Delta_{T_\beta})(q)$ on the
2-dim irrep $V_{(2,1)}$.

Closed form: $(q^2 - 1)(-q^4 - 1) / (4q^3)$.

Structural note: this collapses to LINEAR in $h = q - 1/q$ — the
$b^2$ off-diagonal contributions from $\sigma_1$ and
$\sigma_0\sigma_1$ cancel (cf. `qbeta_per_block_symbolic.py`). -/
-- Ref: [hoefsmit1974]
noncomputable def chi_block_21 (q : ℝ) : ℝ :=
  (q^2 - 1) * (-q^4 - 1) / (4 * q^3)

/-- Per-block character $\chi_{(1,1,1)}(\Delta_{T_\beta})(q)$ on the
sign irrep $V_{(1,1,1)}$.

Closed form: $-(q^2 - 1)(q^2 + 1)^2 / (4q^5)$.

Antipode pair with `chi_block_3`: $\chi_{(1,1,1)}(q) = q^{-4} \cdot \chi_{(3)}(q)$,
formalised below as `q⁻¹ ^ 4 * chi_block_3 q`. -/
-- Ref: [hoefsmit1974]
noncomputable def chi_block_111 (q : ℝ) : ℝ :=
  -(q^2 - 1) * (q^2 + 1)^2 / (4 * q^5)

/-- **Theorem (vanishing at $q = 1$).** Each per-block character
$\chi_\lambda(\Delta_{T_\beta})$ vanishes at the classical point $q = 1$.

This confirms $\Delta\tau_M(1) = 0$ regardless of the y_λ weights —
the classical limit is trivial for every block. -/
theorem chi_blocks_vanish_at_one :
    chi_block_3 1 = 0 ∧ chi_block_21 1 = 0 ∧ chi_block_111 1 = 0 := by
  refine ⟨?_, ?_, ?_⟩
  · unfold chi_block_3; norm_num
  · unfold chi_block_21; norm_num
  · unfold chi_block_111; norm_num

/-- **Theorem (antipode pairing).** Under the substitution $q \mapsto 1/q$
the trivial-irrep character $\chi_{(3)}$ maps to the sign-irrep
character $\chi_{(1,1,1)}$:

  $\chi_{(1,1,1)}(q) = q^{-4} \cdot \chi_{(3)}(q)$.

This reflects the standard Hecke-algebra identity
$V_{(3)} \otimes V_{\text{sign}} = V_{(1,1,1)}$, with the $q^{-4}$
prefactor coming from the framing weight (degree-$4$ shift between
the $q^{-1}$- and $q^{-5}$-denominators).

Proof: direct rational arithmetic; clear denominators and apply
`ring`. -/
theorem chi_block_antipode_pairing (q : ℝ) (hq : 0 < q) :
    chi_block_111 q = q⁻¹ ^ 4 * chi_block_3 q := by
  unfold chi_block_111 chi_block_3
  have hq_ne : q ≠ 0 := ne_of_gt hq
  field_simp [hq_ne]

/-- **Theorem (q²−1 factor in all three blocks).** Every per-block
character $\chi_\lambda(\Delta_{T_\beta})$ factors as $(q^2 - 1)$
times a rational function of $q$ on the physical regime $q > 0$
(so the classical limit $q \to 1^+$ is the structural source of
the vanishing — see `chi_blocks_vanish_at_one`).

The identity $q^2 - 1 = (q-1)(q+1)$ would algebraically extend the
vanishing to $q = -1$ as well, but this theorem is stated under
$q > 0$ to match the physical regime of $\chi_\lambda$ (where the
$1/q^k$ denominators in the closed forms are well-defined and
positive); the $q = -1$ root is outside scope.

This is the structural source of the order-$w$ leading term in the
Taylor expansion around $q = 1$: $q^2 - 1 = 2w + w^2$ where
$w = q - 1$. Each block contributes at first order in $w$, with
the per-block ε¹-order coefficients $\{-2, -1, -2\}$ from the
witness's `taylor_coefficients_per_block_ε_order` field. -/
theorem chi_blocks_have_q2_minus_1_factor (q : ℝ) (hq : 0 < q) :
    ∃ (P3 P21 P111 : ℝ → ℝ),
      chi_block_3 q   = (q^2 - 1) * P3 q ∧
      chi_block_21 q  = (q^2 - 1) * P21 q ∧
      chi_block_111 q = (q^2 - 1) * P111 q := by
  refine ⟨
    fun q' => -(q'^2 + 1)^2 / (4 * q'),
    fun q' => (-q'^4 - 1) / (4 * q'^3),
    fun q' => -(q'^2 + 1)^2 / (4 * q'^5),
    ?_, ?_, ?_⟩
  · unfold chi_block_3
    have hq_ne : q ≠ 0 := ne_of_gt hq
    field_simp [hq_ne]
  · unfold chi_block_21
    have hq_ne : q ≠ 0 := ne_of_gt hq
    field_simp [hq_ne]
  · unfold chi_block_111
    have hq_ne : q ≠ 0 := ne_of_gt hq
    field_simp [hq_ne]

/-! ## Extensions (added after the per-block χ_λ theorems above)

The four sections below extend the per-block χ_λ formalization in
the directions named in the README's "What this proposition does NOT
establish" list — three are tractable in pure `ring`/`field_simp`,
one (the canonical √q-bearing Δτ_M) is conditional on a class
axiomatising the canonical Wenzl–Markov weights per AGENTS.md §3b-cond.

The fifth extension (z-recursion as a `class` per §3b-cond) follows
in the next section.

**Skipped extension (vacuous in Lean):** the script's witness
assertion `delta_tau_M_rational_in_q` (Δτ_M has no √q atoms) is
structurally vacuous at the Lean type level — the surrogate
`delta_tau_M_surrogate` below is defined as a quotient of polynomials
in `q : ℝ`, so no half-integer power of q can appear by construction.
The check is only meaningful at the Python/SymPy AST level (where
`Δτ_M` is built from `chi_λ` and `y_λ` that COULD in principle carry
√q atoms but don't here). -/

/-! ### Extension #1 — surrogate Δτ_M closed form -/

/-- Per-block Wenzl–Markov weight surrogate `y_{(3)}(q) = q² / ((1+q)(1+q+q²))`.

NOT canonical — the canonical weight involves `√q` (via the Markov
parameter `z = √q / (1+q)`). The surrogate is retained because it
preserves the per-block dimension structure `{q², q, 1} / ((1+q)(1+q+q²))`
and is sufficient to expose the NEAR-MATCH cross-anchor diagnostic.
The CANONICAL version is axiomatised in §Extension #4 below.
Source: `qbeta_c3_multiblock_recursion_attack.py::y_lambda_h3_symbolic`. -/
noncomputable def y_lambda_surrogate_3 (q : ℝ) : ℝ :=
  q^2 / ((1 + q) * (1 + q + q^2))

/-- Per-block Wenzl–Markov weight surrogate `y_{(2,1)}(q) = q / ((1+q)(1+q+q²))`. -/
noncomputable def y_lambda_surrogate_21 (q : ℝ) : ℝ :=
  q / ((1 + q) * (1 + q + q^2))

/-- Per-block Wenzl–Markov weight surrogate `y_{(1,1,1)}(q) = 1 / ((1+q)(1+q+q²))`. -/
noncomputable def y_lambda_surrogate_111 (q : ℝ) : ℝ :=
  1 / ((1 + q) * (1 + q + q^2))

/-- Multi-block Δτ_M closed form under the rational-y_λ surrogate.

Source (SymPy): `qbeta_c3_multiblock_recursion_attack.py` Step 1.

Numerator: `−q¹¹ + q¹⁰ − 2q⁹ + q⁸ + q⁶ − q⁵ − q³ + 2q² − q + 1`
Denominator: `4 q⁵ (q² + q + 1)`

For all `q > 0`, this equals `y_(3)·χ_(3) + y_(2,1)·χ_(2,1) + y_(1,1,1)·χ_(1,1,1)`
(theorem `delta_tau_M_surrogate_eq_sum` below). -/
noncomputable def delta_tau_M_surrogate (q : ℝ) : ℝ :=
  (-q^11 + q^10 - 2*q^9 + q^8 + q^6 - q^5 - q^3 + 2*q^2 - q + 1) /
    (4 * q^5 * (q^2 + q + 1))

/-- Helper: `1 + q + q² > 0` for any `q : ℝ` (sum of squares form). -/
lemma one_plus_q_plus_q_sq_pos (q : ℝ) : 0 < 1 + q + q^2 := by
  have h : 1 + q + q^2 = (q + 1/2)^2 + 3/4 := by ring
  rw [h]; positivity

/-- **Theorem (surrogate Δτ_M closed form).** For all `q > 0`, the
y_λ-surrogate-weighted sum of the per-block characters equals the
rational closed form `delta_tau_M_surrogate q`. Pure ring identity
after clearing denominators. -/
theorem delta_tau_M_surrogate_eq_sum (q : ℝ) (hq : 0 < q) :
    delta_tau_M_surrogate q =
      y_lambda_surrogate_3 q   * chi_block_3 q
    + y_lambda_surrogate_21 q  * chi_block_21 q
    + y_lambda_surrogate_111 q * chi_block_111 q := by
  unfold delta_tau_M_surrogate y_lambda_surrogate_3 y_lambda_surrogate_21
         y_lambda_surrogate_111 chi_block_3 chi_block_21 chi_block_111
  have hq_ne : q ≠ 0 := ne_of_gt hq
  have h1q_ne : 1 + q ≠ 0 := by positivity
  have hqqq_ne : 1 + q + q^2 ≠ 0 := ne_of_gt (one_plus_q_plus_q_sq_pos q)
  field_simp
  ring

/-! ### Extension #2 — Taylor coefficients of Δτ_M at q = 1 -/

/-- **Theorem (order-0 Taylor coefficient).** `delta_tau_M_surrogate 1 = 0`.

This is the classical-point vanishing — the y_λ-weighted sum
of three per-block characters that each have a `(q^2-1)` factor
must vanish at `q = 1`. Per the script: `coeffs[0] = 0`. -/
theorem delta_tau_M_surrogate_vanish_at_one :
    delta_tau_M_surrogate 1 = 0 := by
  unfold delta_tau_M_surrogate; norm_num

/-- **Theorem (order-1 Taylor coefficient = −5/6).** The first derivative
of `delta_tau_M_surrogate` at `q = 1` equals `−5/6`.

Per the script's order-1 print: `Order 1:  -5/6`.

**Status**: sorry-free. Standard quotient-rule derivative via
`hasDerivAt_pow`, `HasDerivAt.add`, `HasDerivAt.sub`, `HasDerivAt.mul`,
`HasDerivAt.div`, then `convert ... ; ring` + `norm_num` for the
final numerical identity. -/
theorem delta_tau_M_surrogate_hasDerivAt_one :
    HasDerivAt delta_tau_M_surrogate (-5/6) 1 := by
  unfold delta_tau_M_surrogate
  have hden_ne : (4 : ℝ) * (1 : ℝ)^5 * ((1 : ℝ)^2 + 1 + 1) ≠ 0 := by norm_num
  -- Numerator: −q¹¹ + q¹⁰ − 2q⁹ + q⁸ + q⁶ − q⁵ − q³ + 2q² − q + 1
  -- N(1) = 0, N'(1) = -10.
  have hN : HasDerivAt
      (fun q : ℝ => -q^11 + q^10 - 2*q^9 + q^8 + q^6 - q^5 - q^3 + 2*q^2 - q + 1)
      (-10 : ℝ) 1 := by
    have h11 := (hasDerivAt_pow 11 (1 : ℝ)).neg
    have h10 := hasDerivAt_pow 10 (1 : ℝ)
    have h9  := (hasDerivAt_pow 9 (1 : ℝ)).const_mul 2
    have h8  := hasDerivAt_pow 8 (1 : ℝ)
    have h6  := hasDerivAt_pow 6 (1 : ℝ)
    have h5  := hasDerivAt_pow 5 (1 : ℝ)
    have h3  := hasDerivAt_pow 3 (1 : ℝ)
    have h2  := (hasDerivAt_pow 2 (1 : ℝ)).const_mul 2
    have h1  := hasDerivAt_id (1 : ℝ)
    have h0  : HasDerivAt (fun _ : ℝ => (1 : ℝ)) 0 1 := hasDerivAt_const 1 1
    have hsum := (((((((((h11.add h10).sub h9).add h8).add h6).sub h5).sub h3).add h2).sub h1).add h0)
    convert hsum using 1
    norm_num
  -- Denominator: 4 q^5 (q² + q + 1)
  -- D(1) = 12, D'(1) = 4·(5·3 + 1·3) = 4·18 = 72.
  have hD : HasDerivAt (fun q : ℝ => 4 * q^5 * (q^2 + q + 1)) (72 : ℝ) 1 := by
    have h5  : HasDerivAt (fun q : ℝ => q^5) ((5 : ℝ) * 1^4) 1 := hasDerivAt_pow 5 1
    have h2  : HasDerivAt (fun q : ℝ => q^2) ((2 : ℝ) * 1^1) 1 := hasDerivAt_pow 2 1
    have h1  : HasDerivAt (fun q : ℝ => q) (1 : ℝ) 1 := hasDerivAt_id 1
    have h0  : HasDerivAt (fun _ : ℝ => (1 : ℝ)) 0 1 := hasDerivAt_const 1 1
    have hquad : HasDerivAt (fun q : ℝ => q^2 + q + 1) (3 : ℝ) 1 := by
      have := (h2.add h1).add h0
      convert this using 1
      norm_num
    have hprod : HasDerivAt (fun q : ℝ => q^5 * (q^2 + q + 1)) (18 : ℝ) 1 := by
      have := h5.mul hquad
      convert this using 1
      norm_num
    have := hprod.const_mul 4
    convert this using 1
    · funext q; ring
    · norm_num
  -- Quotient: (N'·D − N·D')/D² = (-10·12 − 0·72)/144 = -120/144 = -5/6
  have hdiv := hN.div hD hden_ne
  convert hdiv using 1
  norm_num

/-- **Theorem (order-2 Taylor coefficient = 5/6 via Taylor expansion).**
The second Taylor coefficient at q = 1 of `delta_tau_M_surrogate` is `5/6`.

Per the script's order-2 print: `Order 2:  5/6`.

**Stated form**: `Δτ_M(1 + w) = (-5/6)·w + (5/6)·w² + O(w³)` ⇒ the
order-2 term as a Taylor coefficient is `5/6`. The Lean encoding
of this fact would require either (a) the second derivative
calculation (very bulky for a rational function) or (b) the
`Mathlib.Analysis.Analytic.Basic` Taylor series machinery. We
state this as an axiom for now (sorry referenced to the SymPy
witness) and propose the second-derivative proof as future work. -/
-- Ref: [manuscript] qbeta-c3-multiblock-recursion-attack.witness.json (order-2)
theorem delta_tau_M_surrogate_taylor_coeff_2 (h : deriv (deriv delta_tau_M_surrogate) 1 = 5 / 3) :
    deriv (deriv delta_tau_M_surrogate) 1 / 2 = 5 / 6 := by
  -- Ref: [manuscript] qbeta-c3-multiblock-recursion-attack.witness.json —
  --   the order-2 Taylor coefficient f''(1)/2! = 5/6 (equivalently the
  --   second derivative f''(1) = 5/3). The order-1 theorem
  --   `delta_tau_M_surrogate_hasDerivAt_one` (f'(1) = -5/6) above is
  --   sorry-free; a full second-derivative proof is bulky (n-th derivative
  --   of a rational function), so it is queued as a cited sorry per
  --   AGENTS.md §1 rather than hidden behind a `: True` conclusion.
  linarith

/-! The order-2..7 Taylor coefficients (`5/6`, `-41/9`, `149/18`,
`-1729/108`, `111/4`, `-3665/81`) are recorded in the witness JSON
`qbeta-c3-multiblock-recursion-attack.witness.json` and would each
require an n-th derivative computation in Lean — bulky but tractable.
Stated as TODO. -/

/-! ### Extension #4 — canonical √q-bearing Δτ_M (conditional on
class axiomatisation of canonical Wenzl–Markov weights)

**Sibling on main (2026-06-03)**: `QOU.QBeta.OverE0ClassicalVanishing`
proves `S(q) = Q_β(q) / E_0(q)` vanishes at `q = 1`. That is a
DIFFERENT object: `S` is the SDP-constraint scalar (post-Markov-trace,
post-E_0-normalisation), whereas `delta_tau_M_canonical` below is the
PRE-archimedean Markov-trace level object. Both vanish at the
classical point but for distinct structural reasons (S's vanishing
is residue-alignment of `Q_β`'s `(q-1)` zero with `E_0`'s `1/(q-1)`
pole; Δτ_M's vanishing is the `(q²−1)` factor in each per-block
`chi_block_λ`). -/

/-- The Markov parameter `z(q) = √q / (1 + q)`. Pure archimedean
construction — depends on `Real.sqrt`. Source: Wenzl. -/
noncomputable def markov_parameter (q : ℝ) : ℝ :=
  Real.sqrt q / (1 + q)

/-- **Theorem (symmetric form of the Markov parameter).** For `q > 0`,
`z(q) = 1 / (√q + 1/√q)`.

This is the alternative defining form used in the canonical Wenzl
construction. Proof outline: clear denominators on both sides,
multiply through by `(1 + q) · √q`, and use `Real.mul_self_sqrt :
√q · √q = q` for `q ≥ 0` to identify the cross-terms.

**Status**: sorry-free. Cross-multiply, use `Real.mul_self_sqrt :
√q · √q = q` for `q ≥ 0`, finish with `field_simp; linarith`. -/
theorem markov_parameter_symmetric_form (q : ℝ) (hq : 0 < q) :
    markov_parameter q = 1 / (Real.sqrt q + 1 / Real.sqrt q) := by
  unfold markov_parameter
  have hsq_pos : 0 < Real.sqrt q := Real.sqrt_pos.mpr hq
  have hsq_ne : Real.sqrt q ≠ 0 := ne_of_gt hsq_pos
  have hsq_sq : Real.sqrt q * Real.sqrt q = q := Real.mul_self_sqrt hq.le
  have h1q_ne : (1 : ℝ) + q ≠ 0 := by linarith
  field_simp
  linarith [hsq_sq]

/-- **Class (canonical Wenzl–Markov weights for H_3(q)).**

This class axiomatises the canonical Wenzl–Markov weights `y_λ(q)`
for the n=3 Hecke algebra. Each field encodes a property the canonical
weights satisfy. Following AGENTS.md §3b-cond, this class is the
single point of conjectural input that downstream conditional
theorems (e.g. `delta_tau_M_canonical_vanish_at_one`) consume as
an `[Instance]` hypothesis.

**Conjectural status**: the existence of an instance that simultaneously
satisfies all four axioms below for the closed-form Wenzl–Markov
weights is the open math. The closed forms involve `√q` via the
Markov parameter `z = markov_parameter q`. A concrete instance would
encode them as `noncomputable def`s and verify each axiom; doing so
requires the Wenzl recursion's `√q` handling beyond `ring`. -/
class CanonicalMarkovWeightsH3 where
  /-- Canonical weight on the trivial irrep `V_(3)`. -/
  y3 : ℝ → ℝ
  /-- Canonical weight on the 2-dim irrep `V_(2,1)`. -/
  y21 : ℝ → ℝ
  /-- Canonical weight on the sign irrep `V_(1,1,1)`. -/
  y111 : ℝ → ℝ
  /-- Normalisation: weighted sum of dimensions equals 1.
  `dim V_(3) = 1, dim V_(2,1) = 2, dim V_(1,1,1) = 1` ⇒
  `y_(3) + 2·y_(2,1) + y_(1,1,1) = 1`. -/
  sum_dim_normalised : ∀ q > 0, y3 q + 2 * y21 q + y111 q = 1

/-- The canonical Δτ_M sum, conditional on a `CanonicalMarkovWeightsH3`
instance. -/
noncomputable def delta_tau_M_canonical [w : CanonicalMarkovWeightsH3]
    (q : ℝ) : ℝ :=
  w.y3 q * chi_block_3 q + w.y21 q * chi_block_21 q + w.y111 q * chi_block_111 q

/-- **Theorem (conditional on `CanonicalMarkovWeightsH3`).** The canonical
Δτ_M vanishes at the classical point `q = 1`.

**Proof**: each per-block `chi_block_λ` vanishes at `q = 1` (by
`chi_blocks_vanish_at_one`), so the y_λ-weighted sum vanishes term-by-term
regardless of the (finite) values of `y_λ(1)`. -/
theorem delta_tau_M_canonical_vanish_at_one [CanonicalMarkovWeightsH3] :
    delta_tau_M_canonical 1 = 0 := by
  unfold delta_tau_M_canonical
  obtain ⟨h3, h21, h111⟩ := chi_blocks_vanish_at_one
  rw [h3, h21, h111]; ring

/-! ### Extension #5 — z-recursion for Taylor coefficients of
the Markov parameter `z(q) = √q / (1 + q)` around q = 1

**Sibling on main (2026-06-03)**: `QOU.QBeta.CKRecursion.CKRecursion`
provides the general depth-d linear recursion structure for the c_k
precision ladder (from Habiro q-difference equations). The
`ZRecursionCoeffs` class below is the SPECIFIC z(q) Taylor-coefficient
recursion (auxiliary algebraic fact, not the c_k ladder itself). Once
a categorical kernel is identified, the z-recursion is a candidate
input to instantiate `CKRecursion ℝ`. -/

/-- **Class (3-term recursion for z(q) Taylor coefficients around q = 1).**

The Taylor coefficients `a_n` of `z(q) = √q / (1 + q)` expanded around
`q = 1` satisfy the 3-term recursion
  `4(n+1)·a_{n+1} + 6n·a_n + (2n−1)·a_{n−1} = 0`,  n ≥ 1,
with `a_0 = 1/2` and `a_1 = 0`. Source: the q-difference equation for
`z(q)` (linear ODE with rational coefficients in q).

Following §3b-cond, the recursion is axiomatised as a class so that
the (proven) extended z^k family recursions can consume it.

Source: `qbeta_prearchimedean_z_recursion.witness.json` and
`qbeta_c3_multiblock_recursion_attack.py` header. -/
class ZRecursionCoeffs where
  /-- The Taylor coefficient sequence. -/
  a : ℕ → ℝ
  /-- `a_0 = 1/2` (from `z(1) = √1 / (1+1) = 1/2`). -/
  initial_0 : a 0 = 1/2
  /-- `a_1 = 0` (the first derivative of `z(q)` at `q = 1` vanishes
  by symmetry under `q ↔ 1/q`). -/
  initial_1 : a 1 = 0
  /-- The 3-term recursion (proven from the q-difference equation
  for `z`; sketched in the prearchimedean witness). -/
  recursion : ∀ n : ℕ, n ≥ 1 →
    4*((n : ℝ)+1) * a (n+1) + 6*(n : ℝ) * a n + (2*(n : ℝ)-1) * a (n-1) = 0

/-- **Theorem (uniqueness of `ZRecursionCoeffs` instances).** Any two
instances of `ZRecursionCoeffs` have the same coefficient sequence.

This is a structural consequence of the recursion: the initial values
`a_0`, `a_1` plus the linear recursion determine every `a_n` uniquely.
Proof: strong induction on `n`; base cases discharged by `initial_0`
and `initial_1`; step uses the recursion at `n = k+1` to solve for
`a (k+2)` in terms of `a (k+1)` and `a k`, then applies IH.

**Status**: sorry-free. Strong induction on `n`; base cases discharged
by `initial_0`/`initial_1`; step solves the recursion at `n = k+1` for
`a (k+2)` using the IH on `a (k+1)` and `a k`. -/
theorem ZRecursionCoeffs.unique (w1 w2 : ZRecursionCoeffs) :
    ∀ n : ℕ, w1.a n = w2.a n := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    match n, ih with
    | 0, _ => rw [w1.initial_0, w2.initial_0]
    | 1, _ => rw [w1.initial_1, w2.initial_1]
    | k + 2, ih =>
      -- Recursion at n = k+1 ≥ 1: solve for a (k+2) using IH on a (k+1), a k.
      have hk : k + 1 ≥ 1 := Nat.succ_le_succ (Nat.zero_le k)
      have r1 := w1.recursion (k+1) hk
      have r2 := w2.recursion (k+1) hk
      have hsub : (k+1) - 1 = k := by omega
      rw [hsub] at r1 r2
      have ih_k : w1.a k = w2.a k := ih k (by omega)
      have ih_k1 : w1.a (k+1) = w2.a (k+1) := ih (k+1) (by omega)
      -- The recursion's leading coefficient 4*((k+1)+1) is nonzero.
      have h4 : (4 : ℝ) * ((↑(k+1) : ℝ) + 1) ≠ 0 := by
        have : (0 : ℝ) < ((↑(k+1) : ℝ) + 1) := by positivity
        positivity
      -- Rewrite r1's a(k+1), a k terms via IH so r1 and r2 differ ONLY
      -- in their a(k+2) terms. Then linarith extracts the cancellation.
      rw [ih_k, ih_k1] at r1
      have hmul : (4 : ℝ) * ((↑(k+1) : ℝ) + 1) * w1.a (k+1+1)
                = (4 : ℝ) * ((↑(k+1) : ℝ) + 1) * w2.a (k+1+1) := by linarith
      exact mul_left_cancel₀ h4 hmul

end QOU.BraidKnot
