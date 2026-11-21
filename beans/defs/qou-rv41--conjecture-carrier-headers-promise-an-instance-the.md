---
# qou-rv41
title: Conjecture-carrier headers promise an instance the file no longer has
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-03T04:11:52Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-5p7n
---

MEASURED 2026-09-03 against origin/main d502ed06ce.

THE DEFECT. Three conjecture carriers share one generated header boilerplate whose claims are false of the current files:

  folio/quantum-observable-universe/lean/QOU/Archimedean/BorelZagierQouVolumes.lean
  folio/quantum-observable-universe/lean/QOU/Archimedean/SingleVolumeIrrationality.lean
  folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/GActionOnSubstrate.lean

Each header says the class 'carries a placeholder field; the noncomputable instance is the conjectural witness whose sorry represents the open conjecture', and that the field schema is 'a structural placeholder; refine the fields to match the conjecture's actual content'. All three claims are false:

  * the fields ARE content-bearing (BorelZagier: 3 volumes + qLinearIndependent, a real forall; SingleVolume: 3 volumes + 3 Irrational fields; GAction: the four axioms);
  * there is NO instance in any of the three;
  * in two of them the header is contradicted by the file's OWN FOOTER 45 lines below, which records the axiom+instance as removed and says 'No instance is provided - that is the honest open state'.

WHY IT MATTERS. The header describes the audit-dodge shape (a sorry-carrying instance) while the file is actually in the correct 3b-tax state. An agent reading the header concludes the opposite of the truth, in the direction of thinking a fabricated closure is present. The header also promises 'unconditional Lean theorems modulo this single conjectural input', which is self-contradictory and is exactly the 'conditional-proved != premise-established' confusion AGENTS.md has a STRICT section about.

FIXED: headers rewritten to describe the actual state; titles no longer say '(placeholder)'. lean-direct exit 0 on all three. Comment-only change.

ALSO CORRECTED: the b9cj ledger labelled DiophantineBirthday 'famous-open (aspirational)'. Its own block says in bold that it should NOT be recorded as an open conjecture - Roth proved it in 1955; what is missing is a FORMALISATION. That block already records three prior epistemic mislabelings of itself; this would have been a fourth.

FOUR FALSE POSITIVES FROM MY OWN SHAPE SCANS, recorded so the next agent does not rebuild them. Each looked like a critical finding:
  1. 'EMPTY CARRIER' x2 - body extraction stopped at the first column-0 line, which in these files is INSIDE a docstring (display math starts at column 0).
  2. 'NO CLAIM FIELD' x3 - per-line field regex missed types on the NEXT line ('qLinearIndependent :' with its forall below).
  3. 'HAS 2 INSTANCES' on He4DemandClosure - real, but NOT a defect: the class is parameterised by coeffs and the instances are honest proofs at [] (vacuous) and [c] (from Fact (0 <= c)). Neither closes the conjecture; the real He-4 coefficient list is neither shape.
  4. 'instances=2' on HyperbolicVolumeIndependence etc - the regex matched PROSE LINES BEGINNING WITH THE WORD 'instance'. The one real instance there is the honest axiom-conditional pattern.

Net: 0 defects found by shape, 3 found by reading. The repo's own tool (content/pipeline/lean-vacuity-axiom-audit.ts, criteria proof-no-empty-prop-carrier / proof-claims-unencoded, plus the agent review ledger) exists precisely because this cannot be done by regex. Use it, not a fifth regex.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-03 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Verified on main 2ae54ab40: none of the three headers (`BorelZagierQouVolumes.lean`, `SingleVolumeIrrationality.lean`, `GActionOnSubstrate.lean`) still contains 'carries a placeholder field' or 'structural placeholder' (grep count 0 each). The defect this bean records is fixed on main. Recommend completed (judgement); left in-progress for the owner of qou-5p7n because the DiophantineBirthday ledger correction was not re-checked.
