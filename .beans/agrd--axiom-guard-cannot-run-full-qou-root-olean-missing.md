---
# agrd
title: 'Keystone axiom guard still cannot run: the full QOU root import is not buildable here'
status: todo
type: task
priority: normal
tags:
    - qa-gate
    - lean
    - infrastructure
created_at: 2026-08-10T05:00:00Z
updated_at: 2026-08-10T05:00:00Z
---

`scripts/lean-axiom-guard.py` — the keystone `#print axioms` gate, whose whole purpose is
to catch a declaration that silently starts depending on `sorryAx` — **could not run at
all**, and the reason was invisible.

**Half fixed (2026-08-10).** `scripts/lean-direct-env.sh` built `LEAN_PATH` from
`find .lake …`, i.e. **relative** paths. The guard writes its probe to a **temp file** and
runs `lean` there, so every entry missed and it failed with

    error: unknown module prefix 'QOU'
    No directory 'QOU' or file 'QOU.olean' in the search path entries: …

while `QOU.olean` sat in a listed directory the whole time — a maximally misleading
message. The env script now roots its `find` at the script's own repo and emits absolute
paths, fixing every consumer at once.

**Still broken, and this is the bean.** With the path fixed the guard gets further and
reports a genuinely missing olean:

    object file '…/QOU/BraidsAndKnots/PlancherelNormalisation.olean' … does not exist

The guard imports the **`QOU` root**, which transitively needs the whole tree built. This
container's build state is incomplete, so the gate is still unusable here.

**To do:**
1. Decide whether the guard should import the root at all. It only needs the modules
   containing its registry entries — importing just those would make it runnable without
   a full-tree build, which is the difference between a gate that runs in CI and one that
   nobody can run locally.
2. Failing that, ensure the build step that precedes it actually builds the root.
3. Either way, make the failure mode legible: "cannot run" must not be reachable without a
   loud message, or the gate silently protects nothing — which is exactly the failure this
   gate exists to prevent in the corpus's *proofs*.
