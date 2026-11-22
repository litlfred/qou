import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/-!
# Brane geometric resummation — the ℏ²-damped jet-brane tower is an affine fixed point

Formalizes the algebraic core of `computations/canonical_plus_multibrane.py::brane_geometric_sum`
(eq ★). Under Markov-stabilization jet lift `V̂^{(n)} = z^n·V̂^{(0)}`, the per-level brane
tower scales as `tower^{(n)} = (z²)^{n-1}·tower^{(1)}`, and with the built-in `ℏ_q^{2n}`
jet-brane damping the tower is **geometric** in the ratio `r = ℏ_q²·z²`:

    Σ_{n=1}^∞ ℏ_q^{2n} · tower^{(n)}  =  a · Σ_{k=0}^∞ r^k ,   a := ℏ_q²·tower^{(1)}.

The *un-damped* raw sum diverges at the archimedean substrate `q₀ > 1` (the
`tower_MeV ≈ 2×10⁶` blow-up in `4he-binding-full-pipeline.witness.json`); the ℏ²-damping
is exactly what makes the **archimedean evaluation converge** — the fibre-level
(Habiro-style) resummation evaluated at `q₀`.

**What is proved here (cache-verifiable, `lean`-direct, no analysis / no `Finset` / no
`ring`):** the resummed value `S` is the unique fixed point of the ℏ²-damped **affine
brane self-map** `S ↦ a + r·S` — i.e. it satisfies the self-consistency `S = a + r·S`,
equivalently `S − r·S = a`. This is the defining recurrence the geometric tower obeys
(level-1 term `a` plus the damped-lifted remainder `r·S`).

**Standard consequences (NOT re-proved here — their Mathlib oleans, `ring`/`field_simp`/
`tsum_geometric`, are outside the sandbox cache):** from `S − r·S = a` one gets
`S·(1 − r) = a`, hence for `r ≠ 1` the closed form `S = a/(1 − r) = ℏ_q²·tower^{(1)}/(1 −
ℏ_q²z²)`; and the partial sums `Σ_{k<n} r^k = (1 − rⁿ)/(1 − r)` converge to `1/(1 − r)` as
`n → ∞` when `|r| < 1` (`tsum_geometric_of_norm_lt_one`). At `q₀ ≈ 1.11`,
`r = ℏ_q²z² ` has `|r| < 1`, so the archimedean sum converges.

Base ring `ℝ` (§7c): the archimedean substrate evaluation at `q₀` is the intended use.

-- Ref: [leitner2026] docs/audits/2026-08-02-bloch-wigner-torus-composition-volume-probe.md
-/

namespace QOU.MassTheory

/-- **Brane resummation is an affine fixed point (eq ★, verifiable core).** The resummed
ℏ²-damped brane tower value `S` satisfies the self-consistency `S = a + r·S` (level-1 term
`a := ℏ_q²·tower^{(1)}` plus the damped-lifted remainder `r·S`, `r := ℏ_q²z²`) **iff**
`S − r·S = a`. The latter gives `S·(1 − r) = a`, hence the closed form `S = a/(1−r)` for
`r ≠ 1` (the division step needs `field_simp`, outside the sandbox cache — see module doc). -/
theorem brane_resum_affine_fixed_point (a r S : ℝ) :
    (S = a + r * S) ↔ (S - r * S = a) := by
  constructor <;> intro h <;> linarith

/-- The fixed-point relation in product form: `S = a + r·S → S·(1 − r) = a`. Combined with
`r ≠ 1` this is the closed form `S = a/(1−r)` (the final division needs a field tactic
outside the cache). Proof avoids `ring` by treating `r·S` linearly via `mul_one_sub`. -/
theorem brane_resum_mul_one_sub (a r S : ℝ) (h : S = a + r * S) :
    S * (1 - r) = a := by
  rw [mul_one_sub]; linarith

end QOU.MassTheory
