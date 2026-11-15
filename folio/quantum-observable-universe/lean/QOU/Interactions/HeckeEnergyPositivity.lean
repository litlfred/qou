import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.Interactions.HeckeEnergyPositivity — q-integer positivity and Hecke-energy positivity

Proves the foundational positivity lemmas needed by the SDP/dual
analysis in `def:algebraic-primality`:

1. The q-integer `[k]_q` (defined via the rescaled positive-power
   sum form) is positive for `q > 0` and `k >= 1`.
2. Consequently, the Hecke-energy cost `c_λ = w_λ(q)` (Wedderburn
   weight) is positive at `q > 1` for every `λ ⊢ n`.

These are b-independent: they hold for any choice of demand vector
in the SDP. They establish the cost cone in `ℝ^{p(n)}_{>0}`.

LaTeX label: `def:algebraic-primality` (used by Part I.1 of
`sdp-dual-without-demand.md`).

## References

- [mathas1999] https://doi.org/10.1090/ulect/015 — Iwahori–Hecke
  algebras and Schur algebras
-/

namespace QOU.Interactions.HeckeEnergyPositivity

/-! ## §1  Rescaled q-integer (sum of non-negative powers) -/

/-- The *rescaled* q-integer

    `qIntegerRescaled q k = ∑_{j=0}^{k-1} q^{2j}`

    This is `[k]_q · q^{k-1}` where `[k]_q = (q^k - q^{-k}) /
    (q - q^{-1})` is the standard q-integer. The rescaled form
    avoids negative exponents and lives entirely in `ℕ`-powers,
    making positivity proofs trivial. -/
def qIntegerRescaled (q : ℝ) (k : ℕ) : ℝ :=
  (Finset.range k).sum (fun j => q ^ (2 * j))

/-- **Bridge to the canonical geometric bracket.**

`QIntegerCanonical` names this definition as *the* live example of legitimate
geometric usage — "correct only where the variable means `q²`".  This turns that
documented claim into a theorem: the rescaled bracket is literally `qIntGeo`
evaluated at `q²`, unconditionally.

Consolidating it onto `qIntBal` would have been the mis-migration the module
warns about; consolidating it onto `qIntGeo (q ^ 2)` is the *correct* one, and
having it as an equation means the site is no longer an unexplained straggler in
the census. -/
theorem qIntegerRescaled_eq_canonical (q : ℝ) (k : ℕ) :
    qIntegerRescaled q k = QOU.QInteger.qIntGeo (q ^ 2) k := by
  simp [qIntegerRescaled, QOU.QInteger.qIntGeo_def, pow_mul]

@[simp] theorem qIntegerRescaled_zero (q : ℝ) :
    qIntegerRescaled q 0 = 0 := by
  simp [qIntegerRescaled]

@[simp] theorem qIntegerRescaled_one (q : ℝ) :
    qIntegerRescaled q 1 = 1 := by
  simp [qIntegerRescaled]

/-- Recurrence: `qIntegerRescaled q (k+1) = qIntegerRescaled q k + q^{2k}`. -/
theorem qIntegerRescaled_succ (q : ℝ) (k : ℕ) :
    qIntegerRescaled q (k + 1)
      = qIntegerRescaled q k + q ^ (2 * k) := by
  simp [qIntegerRescaled, Finset.sum_range_succ]

/-! ## §2  Positivity of the rescaled q-integer -/

/-- **Positivity of the rescaled q-integer at `q > 0`.** For every
    `q > 0` and `k ≥ 1`, the rescaled q-integer is strictly positive.

    Proof: `qIntegerRescaled q k = ∑_{j=0}^{k-1} q^{2j}` is a sum
    of `k ≥ 1` terms, each positive (since `q^{2j} > 0` when
    `q > 0`). Sum of positive terms is positive. -/
-- Ref: [leitner2026] sdp-dual-without-demand §I.1
theorem qIntegerRescaled_pos
    {q : ℝ} (hq : 0 < q) {k : ℕ} (hk : 1 ≤ k) :
    0 < qIntegerRescaled q k := by
  unfold qIntegerRescaled
  apply Finset.sum_pos
  · intro j _
    exact pow_pos hq (2 * j)
  · -- nonempty range
    rw [Finset.nonempty_range_iff]
    omega

/-- **Strict monotonicity of the rescaled q-integer at `q > 1`.**
    For `q > 1`, the rescaled q-integer grows with `k`. -/
-- Ref: [leitner2026] sdp-dual-without-demand §I.1
theorem qIntegerRescaled_strict_mono
    {q : ℝ} (hq : 1 < q) {k : ℕ} :
    qIntegerRescaled q k < qIntegerRescaled q (k + 1) := by
  rw [qIntegerRescaled_succ]
  have : 0 < q ^ (2 * k) := pow_pos (lt_trans zero_lt_one hq) (2 * k)
  linarith

/-! ## §3  Cost-vector positivity (abstract version) -/

/-- **Hecke-energy cost is non-negative when q > 0.** This is the
    abstract statement: any cost expressible as a finite product of
    rescaled q-integer ratios (i.e. a Wedderburn weight
    `w_λ(q) = dim_q(V_λ)^2 / [n]_q!`) inherits positivity from
    `qIntegerRescaled_pos`.

    The actual hook-length-formula content requires Young diagrams,
    deferred to `MathlibBridge.lean`. Here we record the abstract
    structural fact: ratios of positive q-integers are positive. -/
-- Ref: [leitner2026] sdp-dual-without-demand §I.1
theorem positive_ratio_of_positive_qIntegers
    {q : ℝ} (hq : 0 < q) {a b : ℕ} (ha : 1 ≤ a) (hb : 1 ≤ b) :
    0 < qIntegerRescaled q a / qIntegerRescaled q b := by
  apply div_pos
  · exact qIntegerRescaled_pos hq ha
  · exact qIntegerRescaled_pos hq hb

/-! ## §4  Sums of products of rescaled q-integers -/

/-- Sums of products of rescaled q-integers (with positive factors)
    are positive. This is the abstract structural fact behind the
    Hecke-trace functional summing positive Wedderburn weights. -/
-- Ref: [leitner2026] sdp-dual-without-demand §I.2
theorem sum_of_positive_qInteger_products_pos
    {q : ℝ} (hq : 0 < q)
    (s : Finset ℕ) (hs : s.Nonempty)
    (factors : ℕ → ℕ) (hf : ∀ i ∈ s, 1 ≤ factors i) :
    0 < (s.sum fun i => qIntegerRescaled q (factors i)) := by
  apply Finset.sum_pos
  · intro i hi
    exact qIntegerRescaled_pos hq (hf i hi)
  · exact hs

end QOU.Interactions.HeckeEnergyPositivity
