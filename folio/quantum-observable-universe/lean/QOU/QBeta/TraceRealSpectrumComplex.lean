/-
# A real trace does not imply a real spectrum — and `Δ_L` is elliptic

Bean `qou-cds1`. This file records the formal content of a **correction** to
Step 21 of that bean, and the positive finding that came out of it.

## The error being corrected

Step 21 argued that no phase can live in the Gröbner–Shirshov jet tower because
every tower quantity it examined — `w_sym(k)`, `w_alt(k)`, and the Plancherel
traces `Σ_λ W_λ χ^λ(𝒪)` — is **real** at real `q` (characters of `H_k(q)` lie in
`ℤ[q,q⁻¹]`, Geck–Pfeiffer). That is true and it is beside the point.

The ladder needs an **elliptic generator**: a traceless part with `det > 0`, i.e.
a *complex-conjugate spectrum* (`HolonomySpectrumSignObstruction`, Step 18).
**Realness of the trace says nothing about realness of the spectrum.**
`real_trace_real_det_but_complex_spectrum` below exhibits a real `2 × 2` matrix
with real trace, real determinant and a genuinely complex spectrum. So the Step-21
argument, which ranged over *traces*, could never have settled a question about
*spectra*, and its conclusion "no phase can hide in the tower" over-reached.

## What survives Step 21, unchanged

The vanishing itself, and in a **stronger** form than stated there. If the weight
is transpose-invariant (`W_{λ'} = W_λ`, proved from hook-multiset invariance) and
the operator is bar-odd (`χ^{λ'}(𝒪) = −χ^λ(𝒪)`), then `Σ_λ W_λ χ^λ(𝒪) = 0` —
`QOU.QBeta.decay_combination_zero`, which needs no `H₃`-inducedness. What that
kills is the tower's *`W`-weighted trace* `Σ_λ W_λ χ^λ` of a bar-odd operator. It never touched
the operator's spectrum.

## The positive finding

Computed in `qbeta_decay_operator_elliptic_spectrum_probe.py` at the proton pin,
in the two-dimensional `(2,1)` block:

| operator | `tr² − 4·det` | `det` of traceless part | spectrum |
|---|---|---|---|
| `Δ_S` (short model; the ladder's closed forms) | `+0.043706` | `−0.010927` | real — **hyperbolic** |
| `Δ_L = NF(n) − NF(p)` (long model; **what production runs on**) | `−0.035837` | `+0.008959` | **ELLIPTIC** |

So an elliptic operator **does** exist in the corpus, and it is exactly the
object the owner pointed at — *the thing that does the decay*, rather than the
decay. It is not in the braid image (it is a **difference** of two normal forms,
an algebra element, not a group element), so
`BraidImageEigenphaseExclusion` never applied to it; and it lives in the `(2,1)`
block, which `χ^{(2,1)}(Δ_S) = 0` makes invisible for the short model.

**Its eigenphase is 2.020445 rad against a required 0.056595 — a factor 35.7.**
So it does not supply *the* ladder phase. What it does is retire "branch 3 is out
of named candidates": the corpus contains an elliptic generator, and Step 21
missed it by looking at traces.

Scope-(a) for the finding, scope-(b) for the correction. Nothing derived,
proposed, wired or readmitted.
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

namespace QOU.QBeta

/-- A real `2 × 2` matrix is **elliptic** — complex-conjugate spectrum — exactly
when its characteristic discriminant `tr² − 4·det` is negative. Stated on the
scalars so it needs no matrix machinery: the eigenvalues solve
`x² − (tr)x + det = 0`. -/
def IsElliptic (tr det : ℝ) : Prop := tr ^ 2 - 4 * det < 0

/-- Equivalently, the traceless part has positive determinant — the `det A > 0`
that `HolonomySpectrumSignObstruction` requires. -/
theorem isElliptic_iff_traceless_det_pos (tr det : ℝ) :
    IsElliptic tr det ↔ 0 < det - tr ^ 2 / 4 := by
  unfold IsElliptic
  constructor <;> intro h <;> linarith

/-- **The correction, formally.** There is a real trace and a real determinant
whose matrix has a genuinely complex spectrum. So "every trace in the tower is
real" cannot decide whether a tower operator is elliptic — which is precisely
where Step 21 over-reached.

The witness is `Δ_L`'s measured `(2,1)` block, rounded: `tr = −0.0914`,
`det = 0.0110`. -/
theorem real_trace_real_det_but_complex_spectrum :
    IsElliptic (-914 / 10000) (110 / 10000) := by
  unfold IsElliptic
  norm_num

/-- And the short model is **not** elliptic, on the same measured data
(`tr ≈ 0`, `det ≈ −0.0109`) — so the two models genuinely differ in kind, not
just in value. -/
theorem short_model_not_elliptic :
    ¬ IsElliptic 0 (-109 / 10000) := by
  unfold IsElliptic
  norm_num

/-- An elliptic pair has strictly positive determinant, so its eigenvalues have
a well-defined common modulus `√det` and the eigenphase `θ` satisfies
`cos θ = tr / (2√det)`. Recorded so the reported `θ = 2.020445` has its
definition next to it. -/
theorem isElliptic_det_pos {tr det : ℝ} (h : IsElliptic tr det) : 0 < det := by
  unfold IsElliptic at h
  nlinarith [sq_nonneg tr]

end QOU.QBeta
