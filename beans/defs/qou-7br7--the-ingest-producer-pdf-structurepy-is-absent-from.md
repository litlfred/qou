---
# qou-7br7
title: 'RETRACTED: pdf-structure.py IS present (find does not follow the folio-assistant symlink). Kept as: the dangling-path selector needs a symlink class.'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T23:25:01Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-n4r9
---

## 🛑 RETRACTED, same day, before anyone acted on it

**The headline was wrong.** `scripts/pdf-structure.py` and
`extract-candidates.py` **are** present and executable in this container:

    -rwxr-xr-x  folio-assistant/scripts/pdf-structure.py       33406 bytes
    -rwxr-xr-x  folio-assistant/scripts/extract-candidates.py  11343 bytes

**Why I concluded otherwise: `folio-assistant` is a SYMLINK, and `find` does
not follow symlinks by default.**

    ls -ld folio-assistant
      folio-assistant -> ../folio-assistant

    find    folio-assistant -name 'pdf-structure*'   ->  0 results
    find -L folio-assistant -name 'pdf-structure*'   ->  folio-assistant/scripts/pdf-structure.py

I ran the unflagged form twice, once at `-maxdepth 3` and once full-depth, and
read two empty results as corroboration. They were the same error twice.
`ls folio-assistant/` worked throughout — the shell resolves the symlink — which
is why the directory listing in the original body looks like evidence the clone
was real. It was; my traversal of it was not.

**The pin hypothesis was also wrong, and checkable.** I guessed the pinned
`428ca5c` predated the producer. Measured against a fresh clone of
`folio-assistant` at `main`: `pdf-structure.py` was added **2026-08-15**
(`0def499`), and `git cat-file -e 428ca5c:scripts/pdf-structure.py` **succeeds**
— it is present at the pin, which is dated 2026-08-23. So there was never a
version gap to bump.

### What does NOT survive

* "The ingest producer is absent from both repos here." **False.**
* "No agent in this container can complete an ingest." **False.**
* The causal story that `migrate`'s empty-mapping fallback is *guaranteed* to
  fire here. Its precondition was the producer's absence, which does not hold.

### What survives, and it is small

* **The code reading stands.** `build_mapping()` really does derive the doc-id
  *from* the generated `structure.json` files and fall back to the basename when
  none claims a PDF, and its comment really does call that fallback benign while
  naming only two causes. A guard on an empty mapping is still a reasonable
  cheap hardening — it is just not urgent and not load-bearing for the 22
  orphans.
* **The bare-path ambiguity is real but minor.** Five beans write
  `scripts/pdf-structure.py`, which reads qou-relative; the file is at
  `folio-assistant/scripts/`. Worth a qualifier, not a bean.

### The part worth keeping — a FOURTH false-positive class for the selector

The dangling-path selector (open beans naming a repo path that no longer exists)
now has four classes, not three:

1. **placeholders** — `computations/X.witness.json`, `computations/substrate/x.py`
2. **moved, not deleted** — `computations/_deprecated/hecke_core_legacy.py` is
   now `computations/hecke_core_legacy.py`
3. **elided paths** — `content/.../lean/...` fragments the regex mangles
4. **🆕 symlink-hidden** — the path exists, under `folio-assistant/`, which is a
   symlink that `os.path.exists` resolves but `find` does not traverse

Measured: of **100** distinct missing paths across open beans, **14 are
symlink-hidden** — `content/pipeline/{validate,qa-sweep,qa-utils,qa-checkers-python,conjectural-propagation-audit}.ts`,
`schemas/{types,constraints,block-qa}.ts` and more. Those are all platform files
that moved to `folio-assistant` in the miga migration and are reachable through
the symlink. A selector that does not resolve it reports every one of them as
deleted.

So the rule for anyone generalising this: **resolve `folio-assistant/` (and any
other symlink) before calling a path missing** — `find -L`, or `os.path.exists`,
which already does the right thing. The Python selector used
`os.path.exists` and was correct; my shell follow-up used `find` and was not,
and the shell result is what I believed.

Left open rather than scrapped, because class 4 is a real improvement to a
selector worth keeping. The original claim is dead.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- The original claim is retracted (title says so). What is left is the selector improvement (resolve symlinks before calling a path missing). Not started.
