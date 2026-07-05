---
# sp00
title: 'EPIC: Specht/S_n Lean formalization program (workplan, phase-ordered)'
status: in-progress
type: milestone
priority: normal
created_at: 2026-07-05T16:30:00Z
updated_at: 2026-07-05T16:30:00Z
---

Full Specht module theory in Lean (Mathlib-absent). DONE 2026-07-05: specht_submodule_dichotomy (James submodule theorem) FULLY sorry-free (b9sp milestone). Phase order + critical path below; children sp0x. Honesty: each brick is a famous theorem — reduce-or-honest-sorry, NEVER fake (§1a). PHASE A (foundation): sp01 form_nondegenerate -> specht_isSimple. PHASE B (dims): sp02 straightening + sp03 triangular-relocation -> sp04 finrank=numSYT. PHASE C (labelling/capstone): sp05 pairwise_noniso + sp06 exhausts -> sp07 sn_rational_specht_split. PHASE D (independent): sp08 OV seminormal, sp09 FRT hook-length, sp10 burnside(RSK). Wired consumers (SpechtFinrankWired, OVTopAssembly) close automatically once their cores land.
