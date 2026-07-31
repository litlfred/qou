---
# qcz15
title: 'TIER C: q-Collatz-on-QOU derivation gaps (map from QOU, obstruction, Kummer)'
status: todo
type: milestone
priority: low
created_at: 2026-07-25T03:10:00Z
updated_at: 2026-07-25T03:10:00Z
---

The "on a QOU" content — currently narrative or section-3b-conditional axioms.
Substantial; some genuinely hard. Children:
- C8 (most important, big): derive the Skein-Collatz map FROM the QOU structure —
  QuantumObservableUniverse -> Reeb bundle -> Skein module S(q)=Z[q^pm1] -> the
  specific map. Concrete QuantumObservableUniverse-parametrized construction.
  Multi-file; mirror the sibling q-ns "concrete Descartes QOU" grounding pattern.
- C9: prove the obstruction equivalence kappa_C = 0 <=> conjecture (kappa_C a
  residue of the universal chi(A) class, thm:qou-obstruction-reduction) — Lean-link.
- C10: derive Kummer removability (2|chi(A) => [2]_q-divisor removable), currently
  the obstruction_removable_of_even_chi context AXIOM.
- C11: contact-boundary iff (converges <=> <v_[2]> >= 2) is section-3b-conditional
  axiom; derive or keep honestly conditional (it restates the conjecture).
- C12: couple the Markov-trace face tr_M(C_q^k(h)) -> 1 (collatz-three-forms) to
  the map formally.
Anti-laundering: axiomatization is NOT proof (AGENTS.md). Only a real derivation
closes; conditional classes stay labelled conditional.

C9 DONE (Kummer-removability leg): collatz_obstruction_link.lean — qcollatz_kummer_removable_iff_two_dvd_chi (level-2 residue κ_C of the universal χ(A) class vanishes ⟺ 2∣χ(A), specializing kappa_vanishes_iff_chi to the q-Collatz even-branch [2]_q divisor) + qcollatz_kummer_removable_of_chi_neg_six (Descartes χ=-6 instance, stated with χ=-6 as explicit hypothesis since it's Descartes-specific not general-QOU). sorry-free, 0 warnings. HONEST SCOPE: this is the Kummer-removability leg ONLY, NOT κ_C=0 ⟺ full conjecture — convergence still needs the descent measure μ (open wall). Remaining Tier C: C10 (Kummer removability general derivation), C11 (contact-boundary iff), C8 bricks 2-3 (QOU import).

C10 DONE (Kummer removability derived): collatz_contact_boundary.lean refactored — CollatzContactBoundaryContext now EXTENDS QouObstructionReductionContext; kummer_obstruction_removable DEFINED as kappa_vanishes 2 (the manuscript's own "obstruction vanishes = removable" identity); obstruction_removable_of_even_chi is now a DERIVED theorem (from kappa_vanishes_iff_chi, the merged C9), not a raw context-class axiom. One fewer independent axiom; removability reduces to the universal chi(A) obstruction. sorry-free, 0 warnings. Remaining Tier C: C11 (contact-boundary iff, restates conjecture — keep honestly conditional), C8 bricks 2-3 (QOU import).
