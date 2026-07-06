---
# 2s3s
title: Credit existing sorry-free Lean for prop:isovector-chiral-residue (checker false-negative)
status: todo
type: task
priority: normal
tags:
    - compute-wiring
    - tractable-lean
created_at: 2026-07-06T04:31:26Z
updated_at: 2026-07-06T04:31:26Z
---

Swarm triage: sorry-free §3b-cond Lean QOU.BraidKnot.binding_isovector_mirror_from_chiral (rw+ring) matches the .ts ref; compute checkers don't credit it (same resolver false-negative as jones-mobius). Fix via checker/validation, not a probe (kappa is open/gated — a witness would be fabricated). Block has no .md — verify block shape too.

## Root-cause diagnosis (2026-07-06)

Same infra root cause as g2go (LEAN_PACKAGES unconfigured at qa-sweep runtime). ADDITIONAL
wrinkle: this block's ref `qou:QOU.BraidKnot.binding_isovector_mirror_from_chiral` has
module `QOU.BraidKnot` (a directory) and name `binding_isovector_mirror_from_chiral` (a
decl, ≠ filename `BindingIsovectorChiralResidue.lean`). So even once the registry is
configured, `resolveCanonicalLean`'s (a)-direct + (b)-basename both miss — it also needs a
decl→file strategy (scan the Lake tree for the decl), OR the block should carry a
module-level ref. g2go is fixed by the bootstrap alone; 2s3s needs bootstrap + resolver
decl-lookup.
