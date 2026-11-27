import Mathlib.Tactic

/-!
# Q_β precision ladder: the algebraic primitives

Split out of `QOU.BraidsAndKnots.QBetaCategoricalPrecisionLadder` under the
transcendental-boundary ruling (owner, 2026-11-27, bean `qou-dk7p`; card choice
"Also the convention-C items"). These are the parts of the ladder that need no
square root and no cosine:

* `hbarQ'`, `markovZ'` (convention D), `heckeH'`, `alpha`, `jonesHopfClassicalLimit`;
* `hoefsmitBSq`, the square `b²` of the Hoefsmit coupling, which is rational in `q`;
* the coefficient class `QBetaPrecisionLadderCoefficients` and its canonical
  instance, whose rungs use `b` only through even powers;
* the classical-point values at `q = 1`.

The N=1 cosine factor, the coupling `b = √(q⁴+q²+1)/(q²+1)` itself, and every
factor that uses an odd power of `b` stay in
`QOU.BraidsAndKnots.QBetaCategoricalPrecisionLadder`. The convention-C framing
of the ladder recorded there applies here unchanged.

LaTeX label: `prop:q-beta-categorical-precision-ladder`
-/

namespace QOU.BraidKnot

/-- Quantum Planck constant `ℏ_q = (q − 1) / q`. -/
noncomputable def hbarQ' (q : ℝ) : ℝ := (q - 1) / q

/-- Markov-Jones parameter in **convention D**, `z = q³/(q² + 1)`.

    **Migrated from convention C 2026-08-26 (bean `qou-cxjq`).** This read
    `1/(√q + 1/√q)` = `√q/(q+1)`, convention C.

    AGENTS.md flags this ladder as convention-C-frame throughout, so the
    expectation going in was that its results would not survive. The `q = 1`
    results DO survive, and for a reason worth stating: `q = 1` is the single
    point where the two conventions agree, both equal to `1/2`
    (`QOU.BraidKnot.markovZD_one` / `markovZC_one`). So a theorem evaluated only
    at the classical point is convention-agnostic by accident of sitting exactly
    on the coincidence — not because the ladder is convention-free. Anything
    evaluated away from `q = 1` still needs re-deriving under D. -/
noncomputable def markovZ' (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- Quantum-integer differential `h = q − q⁻¹`. -/
noncomputable def heckeH' (q : ℝ) : ℝ := q - q⁻¹

/-- Single-wrap eigenphase `α = (z − 1) h / 2`. -/
noncomputable def alpha (q : ℝ) : ℝ := (markovZ' q - 1) * heckeH' q / 2

/-- Classical-limit Hopf-link Jones value at `q = 1`: `J_Hopf(1) = -2`.
    This is the unreduced Jones polynomial of the 2-component Hopf
    link evaluated at q = 1. -/
def jonesHopfClassicalLimit : ℝ := -2

/-- The square of the Hoefsmit off-diagonal coupling, `b² = (q⁴ + q² + 1)/(q² + 1)²`.
    Every coefficient `c_k` of the ladder uses `b` only through even powers, so the
    coefficient class is stated with `b²`, which is rational in `q`. The coupling `b`
    itself (a square root) is `hoefsmitB` in `QBetaCategoricalPrecisionLadder`, with
    `hoefsmitB_sq : hoefsmitB q ^ 2 = hoefsmitBSq q`. -/
noncomputable def hoefsmitBSq (q : ℝ) : ℝ := (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2

/-- **Categorical coefficient class for the Q_β precision ladder.**

Holds the per-rung coefficients `c_k` for the factor
`(1 + c_k · b^k · ℏ_q^{2k})` at depth `k ≥ 2`. All rungs through N=5
are now pinned to closed forms derived from two primitives:

  - **b(q)** — Hoefsmit off-diagonal coupling (Kashiwara source)
  - **c_3 = J_Hopf(q=1) = −2** — Hopf Jones polynomial at q=1
    (categorical inter-block source)

The closed forms (per `2026-05-19-qbeta-all-ck-categorical-extension.md`):

  c_2(q) = −1                                  (pure Kashiwara, intra-block)
  c_3(q) = −2 = J_Hopf(q=1)                    (pure Jones, inter-block)
  c_4(q) = c_3(q) · b⁴(q) = −2·b⁴(q)           (Jones × Kashiwara mixing)
  c_5(q) = −(b²(q) + 1/2)                       (Kashiwara b² + Hopf-half offset;
                                                 doc's `c_4` form, off by one rung)

Each instance may extend the class with c_6, c_7, ... once their
closed forms are derived. -/
class QBetaPrecisionLadderCoefficients where
  /-- The k-th rung categorical coefficient `c_k(q)`. -/
  c_k_at_q : ℕ → ℝ → ℝ
  /-- N=2: pure Kashiwara, factor (1 - b²·ℏ_q^4). -/
  c_2_eq : ∀ q, c_k_at_q 2 q = -1
  /-- N=3: pure Jones, c_3 = J_Hopf(q=1). -/
  c_3_eq : ∀ q, c_k_at_q 3 q = jonesHopfClassicalLimit
  /-- N=4: c_4 = c_3 · b⁴ (Jones × Kashiwara, 0.91% empirical residual). -/
  c_4_eq : ∀ q, c_k_at_q 4 q = jonesHopfClassicalLimit * (hoefsmitBSq q)^2
  /-- N=5: c_5 = −(b² + 1/2) (Kashiwara b² + Hopf-half offset; sub-ppt residual). -/
  c_5_eq : ∀ q, c_k_at_q 5 q = -(hoefsmitBSq q) - 1/2
  /-- N=6: c_6 = c_3² · b² = 4·b² (Jones-squared × Kashiwara b²; closes
      6.5× tighter than N=5). EMPIRICAL FIT — not derived. -/
  c_6_eq : ∀ q, c_k_at_q 6 q = jonesHopfClassicalLimit^2 * hoefsmitBSq q
  /-- N=7: c_7 = c_3³ = −8 (Jones cubed). Residual leverage is so small
      at N=7 (10⁻¹⁵ scale) that many c_7 values give acceptable closure;
      this form is chosen for pattern aesthetics, not derivation. -/
  c_7_eq : ∀ q, c_k_at_q 7 q = jonesHopfClassicalLimit^3

/-- **Canonical instance of `QBetaPrecisionLadderCoefficients`** with
    the closed forms from the 2026-05-19 audit. -/
noncomputable instance qBetaPrecisionLadderCoeffsCanonical :
    QBetaPrecisionLadderCoefficients where
  c_k_at_q := fun k q =>
    match k with
    | 2 => -1
    | 3 => jonesHopfClassicalLimit
    | 4 => jonesHopfClassicalLimit * (hoefsmitBSq q)^2
    | 5 => -(hoefsmitBSq q) - 1/2
    | 6 => jonesHopfClassicalLimit^2 * hoefsmitBSq q
    | 7 => jonesHopfClassicalLimit^3
    | _ => 0  -- higher rungs not yet pinned
  c_2_eq := fun _ => rfl
  c_3_eq := fun _ => rfl
  c_4_eq := fun _ => rfl
  c_5_eq := fun _ => rfl
  c_6_eq := fun _ => rfl
  c_7_eq := fun _ => rfl

/-- `ℏ_q = (q−1)/q` vanishes at the classical point `q = 1`. -/
theorem hbarQ_one : hbarQ' 1 = 0 := by
  unfold hbarQ'; norm_num

/-- `h = q − q⁻¹` vanishes at `q = 1`. -/
theorem heckeH_one : heckeH' 1 = 0 := by
  unfold heckeH'; norm_num

/-- Markov–Jones parameter equals `1/2` at `q = 1` — true in **both**
    conventions, since `q = 1` is their only point of contact. -/
theorem markovZ_one : markovZ' 1 = 1 / 2 := by
  unfold markovZ'
  norm_num

/-- The eigenphase `α = (z−1)·h/2` vanishes at `q = 1` (since `h(1)=0`). -/
theorem alpha_one : alpha 1 = 0 := by
  unfold alpha
  rw [heckeH_one]; ring

end QOU.BraidKnot
