---
# qou-jy1r
title: 'Three proposition siblings are vacuous: MassIdentity.exists, MassIdentity.unique, CategoricalAction.unique'
status: todo
type: task
priority: normal
tags:
    - lean
    - vacuity
created_at: 2026-11-22T10:08:04Z
updated_at: 2026-11-22T12:02:12Z
parent: qou-uwyf
---

Found by the triviality re-probe (docs/audits/2026-11-22-triviality-decl-not-found-triage.md §7). Each closes by trivial/aesop because the conclusion follows from the hypotheses by rewriting alone:
- QOU.MassIdentity.exists (prop:mass-identity-exists, mass-endomorphism/mass-identity-exists.lean): [Nonempty R] : Nonempty R.
- QOU.MassIdentity.unique (prop:mass-identity-unique): (h : m1 = m2) : ‖m1‖ = ‖m2‖. The block claims that scaling the Frobenius pairing by c scales the mass by |c|.
- QOU.CategoricalAction.unique (prop:categorical-action-unique): (h1 : S1 = act Φ swap) (h2 : S2 = act Φ swap) : S1 = S2. The block claims any 1→1 factoring as ev∘(id⊗Φ)∘coev equals tr Φ.
Not in any vacuity audit on main (qou-qc6s and qou-puwe cover def:mass-identity, not these). The disposition is per block (prove the block's claim, state it with a cited sorry, or demote), so it is the owner's call per AGENTS.md. Nothing has been edited.


## 2026-11-22 — PR #9005
MassIdentity.unique restated as the scaling law t1 = c*t2 -> ||t1|| = ||c||*||t2|| (NormedDivisionRing, norm_mul); lean -DautoImplicit=false exit 0, standard axioms only. New self-assuming audit rules catch the other two: rule 5 instance-is-conclusion (MassIdentity.exists) and rule 6 rewrite-by-own-hypotheses (CategoricalAction.unique, among 24 candidates). OPEN: both hold by definition; whether to demote their blocks to remarks is an owner decision (asked 2026-11-22). Keep this bean open until decided.


## 2026-11-22 — resolved by owner cards, PR #9005
- MassIdentity.exists: block demoted to rem:mass-identity-exists (card 'Demote both to remarks'); the Lean sibling and the proof block are removed.
- CategoricalAction.unique: restated as independence of the choice of right dual (card 'Upgrade unique, demote exists'); sorry-free, standard axioms.
- MassIdentity.unique: scaling law (earlier commit).
All three are done on the branch; complete this bean when #9005 merges.
