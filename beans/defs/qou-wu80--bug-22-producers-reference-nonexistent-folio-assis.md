---
# qou-wu80
title: 'BUG: 22 producers reference nonexistent folio-assistant/computations path (miga residue)'
status: todo
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T09:00:39Z
updated_at: 2026-10-04T15:15:35Z
parent: qou-5vkl
---

Found while sweeping producers for float64 re-padding (PR #4653).

  repo_root = Path(__file__).resolve().parent.parent.parent   # = PARENT of the repo
  fn = repo_root / "folio-assistant" / "computations" / "atom-chi-rust-t.witness.json"

Two faults: the parent depth is one too many, and the folio-assistant segment is
stale. Verified NOT a setup problem -- the litlfred/folio-assistant repo carries no
computations/ directory, and folio-assistant/computations never existed in qou
history, so scripts/setup-folio-assistant.sh cannot make this resolve. Cloning the
platform repo does not help.

Sibling producers read the same witness correctly:
  w_path = HERE / f"atom-chi-rust-{atom.lower()}.witness.json"

Fix (verified on option_e_v9_all_symmetries.py, exit 0): drop one .parent and the
"folio-assistant" segment. 22 files carry the stale form; 8 were silently
unrunnable because of it. After fixing, 7 of those 8 turn out to re-pad -- so this
bug was MASKING float64 defects by making the producers fail before they could
write.

Care required: fixing the path makes these producers runnable again, and running
them rewrites witnesses. Do the path fix and any witness regeneration as separate,
separately-reviewed steps.
