---
# qou-l3i4
title: Resolve the hyperelliptic-quintic lean.ref (names a directory, not a decl)
status: completed
type: task
priority: normal
created_at: 2026-08-15T23:26:00Z
updated_at: 2026-08-15T23:27:36Z
---

## RESOLVED 2026-08-15

`brings-surface/hyperelliptic-quintic.ts` carried `qou:QOU.HyperellipticQuintic`, which names the **directory** `QOU/HyperellipticQuintic/` (4 files), not a declaration.

Repointed to `qou:QOU.HyperellipticQuintic.zeta5_residue_monodromy.HyperellipticQuintic`, verified through the canonical resolver → `QOU/HyperellipticQuintic/zeta5_residue_monodromy.lean`.

### Why that file, of the two that declare it

`ScratchZeta5.lean` (94 lines) and `zeta5_residue_monodromy.lean` (124 lines) **both** declare `zeta5`, `HyperellipticQuintic` and `Zeta5MonodromyContext`, in the **same namespace** `QOU.HyperellipticQuintic`. Chose the latter: it is the fuller module (it carries the residue/monodromy content the block's `.md` builds toward), and **nothing imports `ScratchZeta5`**.

### Side finding — `ScratchZeta5.lean` is an orphan scratch duplicate

It is imported by nothing, and it re-declares three names that already exist in a sibling module in the same namespace. Today that is harmless because no single file imports both — but any file that ever imports both gets a duplicate-declaration error, and `globs` compiles it regardless, so it costs build time for content nobody uses.

**Not deleted here.** Removing a file is a content-owner call and out of scope for a ref fix; recorded so it can be dispositioned (delete, or rename its declarations if the scratch variant is deliberately kept). Note the name literally says "Scratch".
