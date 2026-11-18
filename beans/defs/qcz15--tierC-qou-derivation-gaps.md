---
# qcz15
title: 'TIER C: q-Collatz-on-QOU derivation gaps (map from QOU, obstruction, Kummer)'
status: in-progress
type: feature
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T03:10:00Z
updated_at: 2026-11-18T11:37:12Z
parent: qcz14
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

STALE-REFRESH 2026-08-29, verified against main. Per-child state:
- C8 (derive the map FROM the QOU) DONE -- all three bricks landed; see qcz17.
- C9 (obstruction equivalence kappa_C = 0 <=> conjecture) LANDED: AlgebraicSubstrate/collatz_obstruction_link.lean, qcollatz_kummer_removable_iff_two_dvd_chi + the Descartes instance at chi = -6. Sorry-free.
- C10 (Kummer removability) LANDED AS A DERIVATION, which is the point: obstruction_removable_of_even_chi is no longer a context-class axiom -- it is now proved from kappa_vanishes_iff_chi. This is the one Tier-C item that moved from axiom to theorem.
- C11 (contact-boundary iff) STILL CONDITIONAL, and its residual is now NAMED rather than diffuse: what remains assumed is the kappa_0 = chi(A) trace-gap input inherited from QouObstructionReductionContext. The iff itself still restates the conjecture, so keeping it honestly conditional is correct; the chippable part is the trace-gap input alone.
- C12 (couple the Markov-trace face tr_M(C_q^k(h)) -> 1 to the map) UNTOUCHED and is now the largest unformalized Tier-C item: collatz-three-forms.md states the categorical convergence over H_n(q) in prose and its .ts carries NO lean ref at all.
Tier C is therefore 3 done / 1 conditional-with-named-residual / 1 untouched.

C12 CARRIER LANDED 2026-08-29, PR #6042, commit d09d3357e7. File: folio/quantum-observable-universe/lean/QOU/AppendixSurreals/collatz_three_forms.lean. rem:collatz-three-forms now has a machine-checked carrier at four separated tiers.

PROVED (sorry-free, axiom-audited): integer_threshold_eq_two (v=1 never suffices, v=2 always does, no v<2 can, for every q>0 -- no transcendental quantity); one_lt_contactThreshold + contactThreshold_lt_two + contactThreshold_mem_Ioo; the residue face at q=-1 over generic CommRing (qi2_at_divisor, qi3_at_divisor, odd_branch_at_divisor); expected_halvings_eq_two (the block's displayed E[v_2(3n+1)] = sum k 2^-k = 2, via Mathlib's geometric series); classical_limit_is_critical.

OPEN, carried honestly: MarkovTraceConvergence, a 3b-tax PRIMARY conjecture class with two content-bearing fields (the display equation, and the unique-attractor clause) and NO instance.

THE COUPLING C12 ACTUALLY ASKED FOR: no_nontrivial_periodic_trace derives FROM the conjecture that the step operator admits no periodic orbit whose trace differs from the unknot value -- the categorical shadow of the arc's arithmetic cycle-exclusion results. The two faces are now related by a theorem rather than by prose. identity_orbit_trace_one shows unconditionally that the target is attained (and depends on NO axioms at all), so the conjecture's conclusion is not vacuously unreachable.

DEFECT FOUND AND FIXED EN ROUTE (commit 876f70faa3): QOU.Substrate.contact_threshold_lt_two in QOU/QCollatz.lean was titled 'The contact threshold 1 < v* < 2' while its statement and proof establish only v* < 2. The lower half existed NOWHERE in the corpus, and it is the half that rules out a single halving, so it was load-bearing for this very block's 'the integer threshold is exactly 2'. Docstring corrected; the missing half proved in the new file.

STILL NOT DONE on C12, and deliberately: collatz-three-forms.ts is untouched, so the block still carries no lean ref. Wiring one needs pipeline validation and folio-assistant is NOT set up in this container (bun present, folio-assistant/ absent), so I did not guess at the ref shape. Note every other collatz library file in the arc is likewise unreferenced from any content block, so this matches the arc's existing pattern rather than leaving C12 uniquely unwired. A later agent with the pipeline should decide whether the arc's library files get content-block refs as a class.

C11 LOCALISED 2026-08-29 (bean qou-7kfp, commits d7a5da7355 + 369528b64d). The residual is now a precisely-bounded target instead of a diffuse 'conditional': exactly the one equation kappa_0 = chi(A), with the surrounding trace apparatus proved decorative and the two literature inputs proved unable to reach it. Tier C is now: C8/C9/C10/C12 done, C11 localised-but-open (needs a real Hochschild computation), nothing untouched.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-29 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 69 Update (2026-11-18T11:37:12Z)
- Addressed in PR `litlfred/qou#8454` (HEAD `23a754272622fa31774e4f5d1455018224c86d36`, C1 `bcdf148ad3ef8ce5d5b1c640e65680b5b11b62b6`).
