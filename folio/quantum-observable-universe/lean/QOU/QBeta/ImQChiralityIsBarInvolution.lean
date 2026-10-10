/-
# `arg q` is the chirality coordinate only on the unit circle — and the substrate is not on it

Bean `qou-c66b` (`conj:im-q-physical-role`), companion to the probe
`imq_chirality_is_the_bar_involution_probe`. Sequel to
`QOU.QBeta.ImQRealityLocus`, which closed the conjecture's candidate (ii); this
file is the remaining candidate (i).

## Candidate (i), and the identification it makes

The conjecture writes:

> For complex `q = |q|·e^{i arg q}` **near the unit circle**, `arg q` is
> naturally a **chirality coordinate** … The categorical mass formula is
> invariant under `q ↦ q̄` (complex conjugation under modulus projection),
> consistent with mass being chirality-invariant.

So candidate (i) identifies **chirality flip = complex conjugation**.

## What the corpus identifies it with instead

The mirror — the chirality operation on knots — is the **bar involution**
`q ↦ q⁻¹`, in three separate places:

* `mass-theory/archimedean-image-table-table1-data.md` row 4:
  *"J_K̄(q) = J_K(q⁻¹) (mirror; matter/antimatter CPT)"*
* `mass-theory/hq-bi-filtration.md`: *"Bar involution `∗ : q ↦ q⁻¹` ;
  `∗ : H_q^{(n,K)} → H_q^{(n,K*)}` where `K*` is the **mirror knot**"*
* `mass-theory/knot-indexed-convolution-grid-table2-data.md`, same row.

and `braids-and-knots/knot-notation-convention.md` fixes what the mirror means
physically: it flips the sign of the writhe, and the weak isospin **is** that
sign.

## The two coincide exactly on the unit circle, and nowhere else

`conj_eq_inv_iff_modulus_one` below: `q̄ = q⁻¹ ⟺ |q|² = 1`. Candidate (i)
places itself *"near the unit circle"* — the Kashaev regime `q = e^{2πi/N}` —
and **there it is right**. What it is not is a statement about the substrate:
`|q₀| = 1.10998`, so `substrate_off_unit_circle` applies and the two flips are
different maps. Measured, they are `0.20906` apart, **18.83 % of `q₀`**, and
the one the corpus calls the mirror is `q₀⁻¹ = 0.9009182839557414922` — a
**real** number requiring no `Im q` at all.

So at the substrate the role candidate (i) proposes for `arg q` is already
carried, in full, by a real-`q` mechanism the corpus has developed in detail:
the bar involution and its `P_avg`/`P_skew` split — which is `rem:im-q-vs-p-skew`,
the conjecture's *own* exclusions block.

## Second leg: granting the identification anyway

Both complex extensions of `Q_β` are a real non-negative modulus factor times a
rational function with **real coefficients**, so Schwarz reflection gives
`Q_β(q̄) = conj(Q_β(q))` (verified exactly in the probe, residual `0.0` at 50
dps over three points × two extensions). A chirality-**invariant** observable
satisfies `O(q̄) = O(q)`; for `Q_β` that reads `conj(Q_β) = Q_β`, i.e. `Q_β`
real — which `ImQRealityLocus.im_qbeta_zero_iff_e1`/`_e2` turn into `Im q = 0`
on the whole of candidate (ii)'s admissible set. That is
`chirality_invariance_forces_real_q` below.

**The premise is carried, not smuggled.** *"`Q_β` is chirality-invariant"* is a
physics statement — a Q-value is a parity-even energy — not a corpus theorem,
so it is an explicit hypothesis of that theorem and appears nowhere inside a
proof. The first leg needs no such premise: it is arithmetic plus three
citations.

## Scope

Scope-(b) for the first leg, citing the exact identity below. Both legs are
scoped to the **archimedean evaluation at the substrate**, and neither touches
the **fibre**, where `AGENTS.md`'s fibre-vs-observable banner leaves `Im q`
unconstrained and where the Kashaev root-of-unity regime actually lives.
Candidate (i) may well be right on the fibre; what closes is its archimedean
reading.

Nor is this a demotion of chirality. The opposite: the chirality content the
conjecture went looking for in `Im q` is already in the corpus, at real `q`, as
the bar involution's `P_skew` — which `rem:im-q-vs-p-skew` says is *"kept then
discarded"* by the canonical `P_avg` projection.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity
import QOU.QBeta.ImQRealityLocus

namespace QOU.QBeta

/-- **`q̄ = q⁻¹` exactly on the unit circle.** In real coordinates `q = x + iy`,
`q⁻¹ = (x − iy)/s` with `s = x² + y²`, so `q̄ − q⁻¹ = (x − iy)(1 − 1/s)` and both
components carry the same factor `s − 1`. For `q ≠ 0` the two operations agree
iff `s = 1`.

This is the whole first leg: candidate (i)'s identification of chirality with
conjugation is the corpus's identification of it with the bar involution
**precisely on `|q| = 1`**, which is the regime candidate (i) names, and it is
not the regime the substrate is in. -/
theorem conj_eq_inv_iff_modulus_one {x y s : ℝ} (hs : s = x ^ 2 + y ^ 2)
    (hne : x ≠ 0 ∨ y ≠ 0) :
    (x * (s - 1) = 0 ∧ y * (s - 1) = 0) ↔ s = 1 := by
  constructor
  · rintro ⟨hx, hy⟩
    rcases hne with h | h
    · rcases mul_eq_zero.mp hx with h' | h'
      · exact absurd h' h
      · linarith
    · rcases mul_eq_zero.mp hy with h' | h'
      · exact absurd h' h
      · linarith
  · intro h; subst h; simp

/-- **The substrate is off the unit circle.** `q₀` is real with `1 < q₀`, so
`|q₀|² = q₀² > 1`. Hence `conj_eq_inv_iff_modulus_one` does not apply there and
the two chirality candidates are genuinely different maps — measured `0.20906`
apart, 18.83 % of `q₀`. -/
theorem substrate_off_unit_circle {x : ℝ} (hx : 1 < x) : x ^ 2 + (0 : ℝ) ^ 2 ≠ 1 := by
  have hsq : 1 < x ^ 2 := by nlinarith
  simp only [ne_eq]
  intro h
  simp only [ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, add_zero] at h
  linarith

/-- **The corpus's mirror of the substrate is real.** `q ↦ q⁻¹` sends a real
`q > 1` to a real number in `(0, 1)` — so the chirality flip the corpus uses
needs no imaginary part whatsoever, which is the positive form of the first
leg. -/
theorem bar_involution_of_substrate_is_real {x : ℝ} (hx : 1 < x) :
    0 < x⁻¹ ∧ x⁻¹ < 1 := by
  have hx0 : 0 < x := lt_trans one_pos hx
  refine ⟨inv_pos.mpr hx0, ?_⟩
  rw [inv_lt_one_iff₀]
  right; exact hx

/-- **Second leg — granting candidate (i)'s identification collapses it.**
Hypotheses, each doing visible work:

* `hschwarz` — Schwarz reflection, `Q_β(q̄) = conj(Q_β(q))`: an arithmetic fact
  about a real-coefficient rational function times a modulus (probe residual
  `0.0` at 50 dps over three points × two extensions). In components, the
  imaginary part **negates**.
* `hchiral` — **the physics premise**, and the only one: `Q_β` is
  chirality-invariant, so `Q_β(q̄) = Q_β(q)` and the imaginary part is
  **unchanged**. A Q-value is a parity-even energy. It is a hypothesis
  precisely so that it is never assumed inside a proof.
* `hform` — E2's exact imaginary-part numerator from `ImQRealityLocus`.

The first two say the same quantity both negates and does not, so it vanishes;
`im_qbeta_zero_iff_e2` turns that into `Im q = 0` on the substrate branch. Note
the two premises pull in opposite directions and that is the entire content:
neither alone gives anything. -/
theorem chirality_invariance_forces_real_q {x y imAtQ imAtConjQ : ℝ} (hx : 1 / 2 < x)
    (hschwarz : imAtConjQ = -imAtQ) (hchiral : imAtConjQ = imAtQ)
    (hform : imAtQ = y * (2 * x - 1)) : y = 0 := by
  have hz : imAtQ = 0 := by linarith
  exact (im_qbeta_zero_iff_e2 hx).mp (hform.symm.trans hz)

end QOU.QBeta
