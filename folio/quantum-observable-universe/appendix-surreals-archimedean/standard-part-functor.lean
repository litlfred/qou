-- Ref: [robinson1966] Robinson, *Non-standard Analysis*, North-Holland.
-- Ref: [alling1987] Alling, *Foundations of Analysis over Surreal Number
--      Fields*, North-Holland.
--
-- Sibling stub for `def:standard-part-functor`.
--
-- The compiled formalisation lives in:
--   QOU/AppendixSurreals/StandardPart.lean
--
-- See `QOU.AppendixSurreals.standardPart`,
--     `QOU.AppendixSurreals.standardPart_spec`,
--     `QOU.AppendixSurreals.standardPart_of_infinitesimal`,
--     `QOU.AppendixSurreals.standardPart_add`,
--     `QOU.AppendixSurreals.standardPart_mul`.
--
-- ## Rewritten 2026-08-10 — the mass-limit corollary was a tautology
--
-- What stood here (bean `qou-6a5i`) was
--
--     theorem archimedean_mass_commutes (m_unbound B_sym B_qCLT : ℝ)
--         (h_qclt_limit : B_sym = B_qCLT)
--         : (m_unbound - B_sym) = (m_unbound - B_qCLT) := by
--       subst h_qclt_limit; rfl
--
-- Two defects:
--
-- 1. **Tautology.** Subtracting equals from equals. AGENTS.md §"Strict Lean
--    Discipline" item 5. Worse, the *entire* content the docstring advertised —
--    that `B_sym` converges to `B_qCLT` — sat in the **discarded hypothesis**
--    `h_qclt_limit`, asserted as fact in prose and assumed away in the proof.
-- 2. **Wrong shape.** The `.md` claims commutation *"as the scale A → ∞"*
--    ([`rem:archimedean-functor-trace-commutativity`](archimedean-functor-trace-commutativity.md)).
--    That is a statement about a **limit**, not about substituting one equal
--    value for another. An equality hypothesis is the `A → ∞` endpoint already
--    handed over, so the limit — the only content — was never stated.
--
-- Now proved: the genuine limit-interchange (`archimedean_mass_commutes`) and
-- the quantitative form (`mass_error_eq_binding_error`), which together say
-- what the `.md` means: the mass evaluation passes through the `A → ∞` limit,
-- and it neither amplifies nor damps the binding error.
--
-- ## Status of the hypothesis (do not read these as establishing q-CLT)
--
-- Both theorems take the convergence `B → B_qCLT` as a **hypothesis**. Per the
-- 2026-08-10 investigation (bean `qou-w2q7`) that hypothesis is *not*
-- established anywhere in the corpus:
--   * the q-CLT proper is a **deprecated conjecture** whose Lean class
--     `QOU.Observations.QCltNonCommutative` has **no instance** and no
--     downstream consumer, and whose output is a limiting *distribution*, not a
--     number;
--   * `B_qCLT` as used by the mass dashboards is an **ansatz** (real inputs,
--     real output) with a factor ~2–3 miss.
-- So these are conditional results in the §3b-cond sense, and the antecedent is
-- open. AGENTS.md §"Conditional-proved ≠ premise-established".

import Mathlib.Analysis.SpecificLimits.Basic

namespace QOU.AppendixSurreals

/-- **The mass evaluation commutes with the `A → ∞` limit.**

If the exact algebraic binding traces `B A` converge to the macroscopic value
`B_qCLT` as the scale `A → ∞`, then the bound masses `m_unbound − B A` converge
to `m_unbound − B_qCLT`.

This is what `rem:archimedean-functor-trace-commutativity` asserts: the
standard-part evaluation passes through the limit. Its content is the
limit-interchange, which the previous equality-substitution version never
stated.

**Conditional**: the convergence `h` is the hypothesis, and it is open — see the
status note at the head of this file. -/
theorem archimedean_mass_commutes (m_unbound : ℝ) (B : ℕ → ℝ) (B_qCLT : ℝ)
    (h : Filter.Tendsto B Filter.atTop (nhds B_qCLT)) :
    Filter.Tendsto (fun A => m_unbound - B A) Filter.atTop
      (nhds (m_unbound - B_qCLT)) :=
  Filter.Tendsto.const_sub _ h

/-- **The mass error is exactly the binding error — no amplification.**

The quantitative companion: whatever discrepancy remains between two binding
routes transfers to the predicted mass one-for-one. This is why a factor-2 miss
in `B_qCLT` is a factor-2 miss in the mass, and it is falsifiable — any
amplifying or damping constant would break the equality. -/
theorem mass_error_eq_binding_error (m_unbound B B' : ℝ) :
    |(m_unbound - B) - (m_unbound - B')| = |B - B'| := by
  rw [show (m_unbound - B) - (m_unbound - B') = -(B - B') by ring, abs_neg]

/-- Two binding routes that agree in the limit give the same limiting mass —
the original claim, now recovered as a corollary of the limit statement rather
than assumed. -/
theorem mass_limit_unique (m_unbound : ℝ) (B B' : ℕ → ℝ) (L : ℝ)
    (hB : Filter.Tendsto B Filter.atTop (nhds L))
    (hB' : Filter.Tendsto B' Filter.atTop (nhds L)) :
    Filter.Tendsto (fun A => (m_unbound - B A) - (m_unbound - B' A))
      Filter.atTop (nhds 0) := by
  have := (archimedean_mass_commutes m_unbound B L hB).sub
    (archimedean_mass_commutes m_unbound B' L hB')
  simpa using this

end QOU.AppendixSurreals
