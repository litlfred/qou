---
# qou-a5dr
title: 'motivic-perpetual-obstruction: Open conjecture for motivic_perpetual_obstruction'
status: completed
type: task
priority: normal
created_at: 2026-08-12T10:23:22Z
updated_at: 2026-08-22T21:33:09Z
---

## Closed 2026-08-22 — it was never open; a shadowing stub said it was

The declaration this bean names is **proved and sorry-free**:

```
#print axioms QOU.LiftingDescent.motivic_perpetual_obstruction
  -> [propext, Classical.choice, Quot.sound]
```

built `lean`-direct against the real import cone (PR #5502). Route A
(prime-ideal collapse) closed it; the library file's own docstring has said so
since 2026-08-12, the day *before* this bean was opened.

**Why the corpus still read "open".** The block's `lean.ref` resolved to the
co-located sibling `lifting-and-descent/motivic-perpetual-obstruction.lean`,
not to the Lake-tree decl — siblings win (AGENTS.md §0a) — and that sibling
still carried the pre-Route-A `sorry` under an **older two-parameter**
`MotivicGaloisCharacter` signature. So the stub was not merely stale, it was a
*different statement*, and every reader following the ref landed on it.

The stub is deleted. Worth generalising: a shadowing stub does not just hide a
proof, it manufactures a false open-item that survives the corpus-grep
checklist — grep found the `sorry` and the grep was right about the file.

Sibling of `qou-ngac`, closed the same way.
