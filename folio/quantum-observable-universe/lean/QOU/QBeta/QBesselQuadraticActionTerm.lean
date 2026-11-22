/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

# The q-Bessel *quadratic-action term* is too small to be the deuteron binding

**Narrowly-scoped formalize-the-refutation** (compute-author skill §3.4). This file
pins a *single, witnessed numerical gap* so a specific dead ansatz cannot be silently
re-proposed. It is deliberately narrow — read the scope note before citing it.

## What this refutes (and what it does NOT)

The qbk2 exploration asked whether the **second-kind Hahn–Exton q-Bessel
"quadratic action" term**, weighted by the *forced* Markov measure `y_λ`
(substrate-fixed, no free parameter), supplies the deuteron binding
`B(D) = m_e · Σ_λ y_λ χ_λ Δ_λ`. With the forced weights the term collapses to
1–6 % of `B(D)` — at least 15× too small. Mechanism of the deflation: `y_λ`
concentrates on the low Wedderburn blocks (`[6]`, `[5,1]`, `y ≈ 0.059`, small
`ΔG`); the large-`ΔG` blocks (`[3,2,1]`, `ΔG = 8.5`, `y = 0.0073`; `[4,1,1]`,
`ΔG = −9.3`, `y = 0.010`) that drove the earlier on-scale *unweighted* ratio
(2.23×) carry negligible weight. The on-scale appearance was an unweighted-sum
artifact (double-sourced: sibling #2521).

**SCOPE (STRICT — do not over-read).** This refutes *only* the **quadratic-action
functional under the forced `y_λ` measure**. It is **not** a refutation of the
q-heat / Reeb kernel for binding:

* The q-heat/Reeb **kernel survives** as the keystone `W_λ = d_q² / [n]_q!`
  geometric realization (passes the conjugation-symmetry / table prechecks,
  `2026-06-20-keystone-qbessel-heat-kernel-lead.md`).
* A **sibling functional of the same `Z_q` heat trace** — the **log-free-energy**
  `B = E₀ · log(tr_free / tr_atom) = E₀ · Σ_bonds log(1 / f_bond)` (the bond-graph
  route) — is **on-scale, 0.57–2.36×** (`2026-06-10-binding-bond-graph-compute-audit-and-derivation.md`).

So binding likely lives in the **log-determinant / free-energy** functional of the
kernel, *not* in its quadratic-action term. This file kills the quadratic-action
term; it does not touch the surviving log-free-energy direction.

The machinery itself is sound and sorry-free
(`QOU/QBeta/QCasoratianAbel.lean`: the q-Casoratian/Abel law). Only the numerical
*binding-magnitude* claim falls — and a Lean proof of that is just arithmetic on
the witnessed numbers, not an impossibility theorem.

-- Ref: [leitner2026] computations/qbeta/qbessel_reeb_yweighted_gap.py ;
   docs/audits/2026-06-20-qbessel-yweighted-gap-deflation.md
-/
import Mathlib.Tactic

namespace QOU.QBeta.QBesselQuadraticActionTerm

/-- Deuteron binding in electron-mass units, `B(D)/m_e` (the target any candidate
    binding term must reproduce).  ≈ 4.353  (`target_signed` magnitude,
    `2026-05-18-delta-lambda-gating-context.md`). -/
def deuteronTargetMe : ℚ := 4353 / 1000

/-- Magnitude of the forced-`y_λ`-weighted q-Bessel quadratic-action term, larger
    of the two forms tested, `|Σ_λ y_λ χ_λ ΔG| = 0.244` m_e-units (form (B) of the
    deflation witness).  Form (A) `|Σ_λ y_λ ΔG| = 0.056` is smaller still. -/
def quadraticActionTermMe : ℚ := 244 / 1000

/-- Form (A) magnitude, `|Σ_λ y_λ ΔG| = 0.056` m_e-units. -/
def quadraticActionTermFormA : ℚ := 56 / 1000

/-- **Refutation (narrow).** Even *fifteen times* the larger forced-weighted
    q-Bessel quadratic-action term falls short of the deuteron binding: the term is
    at least 15× too small to *be* the binding. This kills the quadratic-action
    functional under the forced `y_λ` measure; the kernel and the log-free-energy
    functional are untouched (see file header).
    -- Ref: [leitner2026] qbessel-reeb-yweighted-gap (forced `y_λ` deflation, 2026-06-20). -/
theorem quadratic_action_term_too_small_for_deuteron :
    15 * quadraticActionTermMe < deuteronTargetMe := by
  unfold quadraticActionTermMe deuteronTargetMe
  norm_num

/-- The smaller form (A) is more than seventy times too small. -/
theorem quadratic_action_form_a_seventy_times_too_small :
    70 * quadraticActionTermFormA < deuteronTargetMe := by
  unfold quadraticActionTermFormA deuteronTargetMe
  norm_num

/-- Equivalent ratio statement: the (larger) quadratic-action term is below one
    fifteenth of the deuteron binding. -/
theorem quadratic_action_term_below_one_fifteenth :
    quadraticActionTermMe < deuteronTargetMe / 15 := by
  unfold quadraticActionTermMe deuteronTargetMe
  norm_num

end QOU.QBeta.QBesselQuadraticActionTerm
