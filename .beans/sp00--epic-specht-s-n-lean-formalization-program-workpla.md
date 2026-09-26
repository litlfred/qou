---
# sp00
title: 'EPIC: Specht/S_n Lean formalization program (workplan, phase-ordered)'
status: completed
type: milestone
priority: normal
created_at: 2026-07-05T16:30:00Z
updated_at: 2026-09-26T11:03:17Z
---

Full Specht module theory in Lean (Mathlib-absent). DONE 2026-07-05: specht_submodule_dichotomy (James submodule theorem) FULLY sorry-free (b9sp milestone). Phase order + critical path below; children sp0x. Honesty: each brick is a famous theorem — reduce-or-honest-sorry, NEVER fake (§1a). PHASE A (foundation): sp01 form_nondegenerate -> specht_isSimple. PHASE B (dims): sp02 straightening + sp03 triangular-relocation -> sp04 finrank=numSYT. PHASE C (labelling/capstone): sp05 pairwise_noniso + sp06 exhausts -> sp07 sn_rational_specht_split. PHASE D (independent): sp08 OV seminormal, sp09 FRT hook-length, sp10 burnside(RSK). Wired consumers (SpechtFinrankWired, OVTopAssembly) close automatically once their cores land.

## EPIC COMPLETE — measured 2026-09-06, ~2 months after it actually finished

Every brick is proved and axiom-clean. Measured with `#print axioms` against
freshly-rebuilt oleans, signatures inspected for smuggled premises:

| brick | declaration | was | is |
|---|---|---|---|
| sp01 | `specht_form_nondegenerate` | completed | ✅ |
| sp02 | `standardPolytabloid_straightening` | **todo** | clean |
| sp03 | `standardPolytabloid_triangular` | completed | ✅ |
| sp04 | `specht_finrank_eq_numSYT` | **todo** | clean |
| sp05 | `specht_pairwise_noniso` | **todo** | clean |
| sp06 | `specht_exhausts_irreducibles` | completed | ✅ |
| sp07 | `sn_rational_specht_split` | **todo** | clean, class inhabited |
| sp08 | `seminormalVector_data_exists` | **todo** | clean |
| sp09 | `numSYT_mul_hookProduct` | completed | ✅ |
| sp10 | `burnside_proved` | **todo** | clean, instance supplied |

**Six of ten were recorded open while proved**, and this epic sat `in-progress`
while complete. All non-`Field`/`CharZero` hypotheses were checked: only sp07 and
sp10 carry a class binder, `[SnIsotypicSpechtSplit]`, and
`SnIsotypicSpechtSplitInstance` inhabits it with a clean, genuinely-constructed
instance — so those two are conditional in form and established in fact.

The phase ordering in the plan above was correct and the program ran to its end.
What failed is that nothing re-measured it: a brick closing did not close its
bean, so the plan kept describing a program that had finished. Four bricks were
updated by hand (sp01, sp03, sp06, sp09) and six were not, which is the signature
of a manual process rather than a checked one.

Follow-up: `qou-sxyr` proposes making this class of drift detectable.
