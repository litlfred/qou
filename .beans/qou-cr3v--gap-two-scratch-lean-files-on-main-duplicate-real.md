---
# qou-cr3v
title: 'GAP: two scratch_*.lean files on main duplicate real modules — 6 un-importable FQN collisions'
status: todo
type: task
priority: normal
created_at: 2026-08-30T09:43:46Z
updated_at: 2026-08-30T09:43:46Z
---

FOUND 2026-08-30 running the /prepare-merge §4a duplicate-decls gate on PR
#6095. Not that branch's regression -- its only .lean appears in ZERO
duplicates -- so filed rather than fixed inline.

MEASURED: duplicated FQNs 63, against the skill's --baseline 57. The six new
collisions come from two files that look like accidental commits:

  content/quantum-observable-universe/lean/QOU/scratch_pmass.lean
      landed 5dd5f65c39 (2026-08-22, qou-7ot6 CODATA drain)
      duplicates QOU/Substrate/ProtonMassSubstrateIdentity.lean
      colliding: QOU.Substrate.ProtonMassSubstrateIdentity.<def>,
                 QOU.Substrate.ProtonMassSubstrateIdentity.proton_mass_substrate_match

  content/quantum-observable-universe/lean/QOU/scratch_skein.lean
      landed e54ffbca0a (2026-08-14, qou-5iat fine-structure)
      duplicates QOU/Torsion/skein_generation.lean
      colliding: QOU.Torsion.SkeinGenerationContext,
                 QOU.Torsion.skein_generation

WHY IT MATTERS rather than being cosmetic: Lean's environment is flat, so two
modules declaring the same FQN cannot both be imported by ANYTHING. Not a
shadowing warning -- the import fails outright. A green lake build says
nothing about it, because no existing module imports both halves; the error
is only reachable by writing a new module that does.

LIKELY FIX: delete both scratch_ files. The name, the location (library root
rather than the subdirectory their twins live in), and the fact that each
duplicates a real module verbatim all point to debris. Verify first by
diffing each against its twin -- if a scratch file carries content the real
module lacks, that content needs migrating before deletion.

NOT DONE HERE because it is two other arcs' territory (qou-7ot6, qou-5iat)
and unrelated to the Toffoli chapter; widening #6095 to cover it would make
that PR harder to review for no gain. Lower the gate baseline back to 57
once drained.
