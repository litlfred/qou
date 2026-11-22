import QOU.Basic

/-!
# QOU.FlavorDressing.FlavorSplitSubstrateMass

Lean carrier for `conj:flavor-split-substrate-mass`.

The conjecture says that the nucleon mass split is given, to leading
order, by the substrate flavor-split formula:

```
(m_n − m_p) / M_N  ≈  (q − 1)² · (1 − q⁻⁴) / 3,      M_N = (m_p + m_n)/2.
```

It is a conjecture, not a theorem. The derivation sketch in
`prf:flavor-split-substrate` reaches it through the per-quark ansatz of
Step 2, which is a fitted step with no derivation on record, and
`QOU.FlavorDressing.PivotSplitOrder.ansatz_ne_pivotSplit` excludes that
ansatz for additive-strand splits with a power-of-`q` nucleon ratio.

Per AGENTS.md §3b-cond the conjecture is axiomatised as a `class` with
**no instance**. Every downstream result that uses it takes the class as
an explicit instance hypothesis, so the conditional dependency is visible
in the type.

The class reads the conjecture's `≈` as equality of the leading-order
term. That is the strongest reading, so every result proved from it is
conditional on the leading-order statement and says nothing about the
higher-order correction. At the physical masses the equality is not met
exactly (`rem:flavor-split-substrate-codata-comparison`), so the class is a
model hypothesis: results proved from it are statements about the model
under this reading, not about measured masses.

This is the archimedean side of the §7c wall: the statement compares
real masses and uses the ordering `1 < q`, so it is stated over `ℝ`.

LaTeX: `\label{conj:flavor-split-substrate-mass}`
-/

namespace QOU.FlavorDressing

/-- The closed form of the substrate flavor split,
    `(q − 1)² · (1 − q⁻⁴) / 3`. The identity between this closed form and
    the factored form `ℏ_q² · h_q · [2]_q / 3` is `prop:flavor-split-substrate`;
    this definition only names the expression. -/
noncomputable def flavorSplitClosedForm (q : ℝ) : ℝ :=
  (q - 1) ^ 2 * (1 - q ^ (-4 : ℤ)) / 3

/-- **Conjecture `conj:flavor-split-substrate-mass`** (no instance).

    For nucleon masses `m_p`, `m_n` and substrate parameter `q`, the split
    `m_n − m_p` equals `M_N · flavorSplitClosedForm q` with
    `M_N = (m_p + m_n)/2`, at leading order. The two setup fields record the
    regime in which the conjecture is stated. -/
-- Ref: [leitner2026] mass-theory/flavor-split-substrate-mass
class FlavorSplitSubstrateMass (m_p m_n q : ℝ) : Prop where
  /-- The substrate parameter is above the classical point. -/
  q_gt_one : 1 < q
  /-- The nucleon mass scale `M_N = (m_p + m_n)/2` is positive. -/
  M_N_pos : 0 < (m_p + m_n) / 2
  /-- The conjecture itself: `m_n − m_p = M_N · (q − 1)²(1 − q⁻⁴)/3`. -/
  nucleon_split : m_n - m_p = (m_p + m_n) / 2 * flavorSplitClosedForm q

end QOU.FlavorDressing
