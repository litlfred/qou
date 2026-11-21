import Mathlib.Data.Complex.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fintype.Card

/-!
# QOU.Brings.sw_period_eq_residue_sum — SW period as a residue sum

On the exceptional divisor `S_c ≅ P¹(ℂ)` at a branch point, the `n`-th
prolonged Seiberg–Witten differential `λ_SW^{(n)}` is a meromorphic
1-form with poles only at the branch points, so its period is the sum of
its residues (residue theorem on the compact Riemann surface):

  ∮_{S_c} λ_SW^{(n)} = 2πi · Σ_p Res_p λ_SW^{(n)}.

LaTeX label: `prop:sw-period-residue-sum`.
This is Lemma **L1** of the step-9 binding-closure workplan: it turns the
SW period `a_D^{(n)}` into an algebraic residue sum.

## References

- [leitner2026] §5-brings-surface/sw-period-residue-sum
- [seiberg1994] https://doi.org/10.1016/0550-3213(94)90124-4

**Ground ring**: `ℂ` (archimedean realisation; residues and periods are
genuinely complex-analytic). NOT part of the pre-archimedean formal chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Brings

open scoped BigOperators

/-- **SW period / residue data** for the `n`-th prolonged Seiberg–Witten
    differential: the finite family of residues at the `k` branch-point
    poles, the period, the `2πi` normalisation, and the identity relating
    them.

    The geometric *realisation* — that `λ_SW^{(n)}` is meromorphic with
    exactly these residues — is the manuscript content
    (`prop:mi-sw-abelianisation`); here it is packaged as the structure's
    hypothesis so the residue-sum shape is available downstream.

    **`period_eq` is a hypothesis, not a consequence of the residue theorem
    (corrected 2026-08-29, bean `qou-6v5l`).** The docstrings and the `.md`
    used to justify it as *"the residue theorem on the compact Riemann
    surface `S_c ≅ P¹`"*. That justification is backwards twice over:

    * On a **compact** Riemann surface the residue theorem says the residues
      of a meromorphic 1-form **sum to zero**. It does not say a period
      equals the total residue sum — and if the sum in `period_eq` ranges
      over *all* poles, it forces `period = 0`
      (`period_eq_zero_of_total_residue_vanishes` below).
    * `P¹(ℂ)` has `H₁ = 0`, so it has **no** generating cycle for a period
      to be taken over. Only a cycle that *bounds* has a residue-sum value,
      and then the sum ranges over the **enclosed** poles, a proper subset —
      which subset is exactly the content the corpus does not yet supply.

    So `period_eq` is a genuine, and genuinely unproved, assumption about
    which poles the contour encloses. Keeping it as a structure field is
    correct; what was wrong was calling the residue theorem as its warrant. -/
structure SWPeriodResidue (k : ℕ) where
  /-- The vertical / jet (body) order `n`. -/
  jetLevel : ℕ
  /-- The residues `Res_p λ_SW^{(n)}` at the `k` branch-point poles. -/
  residues : Fin k → ℂ
  /-- The SW period `a_D^{(n)} = ∮ λ_SW^{(n)}`. -/
  period : ℂ
  /-- The `2πi` normalisation constant of the residue theorem. -/
  twoPiI : ℂ
  /-- Residue theorem on the compact surface `S_c ≅ P¹`. -/
  period_eq : period = twoPiI * ∑ p, residues p

/-- **L1.** The Seiberg–Witten period is `2πi` times the sum of its
    residues — an algebraic residue sum.

    **This is a projection, not a derivation**, and is retained only because
    downstream prose cites `prop:sw-period-residue-sum` by this name: its
    statement is literally the type of the `period_eq` field, so it assumes
    exactly what it concludes (AGENTS.md §3b-cond item 5). It has been an
    unadjudicated candidate in `docs/audits/lean-triviality.json` since
    2026-08-07. The content of this file is now
    `period_eq_zero_of_total_residue_vanishes` and its contrapositive below,
    which *derive* a consequence rather than restating an assumption. -/
-- Ref: [leitner2026] §5-brings-surface
theorem sw_period_eq_residue_sum {k : ℕ} (S : SWPeriodResidue k) :
    S.period = S.twoPiI * ∑ p, S.residues p :=
  S.period_eq

/-- **The residue theorem's actual content, and the obstruction it creates.**

On a compact Riemann surface the residues of a meromorphic 1-form sum to
zero. Read `period_eq` with its sum ranging over *all* poles — which is how
`prop:sw-period-residue-sum` states it, `∑_{p ∈ S_c}` — and the period is
therefore **zero at every jet level**, whatever the residues individually are.

That is fatal to the keystone, which needs `a_D^{(n)} = lw(n−1) > 0`
(`lw(1) = 1`, `lw(2) = (q+1)²/(3q)`, `lw(3) = 5/2 + (3/4)h²`, all positive and
derived from the q-hook-length formula in `QOU.Mass.QHookDimension`).

**This is a second route to a conclusion the corpus already holds.**
`prop:sw-classical-jet-exactness` reaches `period = 0` from *exactness*
(`λ_SW^{(n)} = d(X^{(n−1)})`, so every residue vanishes individually) and
scopes it as a scope-(b) exclusion of the classical-jet reading. This lemma
assumes far less — only that the total residue vanishes, not that each one
does — so it survives readings in which individual residues are nonzero, and
it is driven by the *ambient surface* rather than by the jet rule. The two
agree, by different mechanisms. -/
theorem period_eq_zero_of_total_residue_vanishes {k : ℕ} (S : SWPeriodResidue k)
    (h : ∑ p, S.residues p = 0) : S.period = 0 := by
  rw [S.period_eq, h, mul_zero]

/-- **Contrapositive — what a nonzero period costs.** If the SW period is
nonzero at some jet level, then the residues appearing in `period_eq` do
**not** sum to zero. Since the residues of a meromorphic 1-form over *all* its
poles on a compact surface *do* sum to zero, the sum in `period_eq` cannot
range over all of them: it must range over the poles enclosed by a specific
contour, a proper subset.

Naming that subset is the missing geometric content of the keystone — and note
it is not a technicality about contours. The pole locus is the branch locus of
the colour cubic, which is **exactly 6 points**, independent of `n`
(`disc_X = −16z⁶ − 24z⁵ − 35z⁴ − 50z³ − 35z² − 24z − 16`, squarefree; three
conjugate pairs at `|z| ≈ 0.943, 1.000, 1.061`). Any reading on which the
residue family at level `n` is indexed one-to-one by the Wedderburn blocks
`λ ⊢ n` therefore needs `p(n) ≤ 6`, which fails from `n = 5` (`p(5) = 7`,
`p(6) = 11`, `p(n) → ∞`). -/
theorem total_residue_ne_zero_of_period_ne_zero {k : ℕ} (S : SWPeriodResidue k)
    (h : S.period ≠ 0) : ∑ p, S.residues p ≠ 0 := fun hz =>
  h (period_eq_zero_of_total_residue_vanishes S hz)

end QOU.Brings
