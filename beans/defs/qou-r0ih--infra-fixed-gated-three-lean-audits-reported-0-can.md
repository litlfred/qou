---
# qou-r0ih
title: 'INFRA (fixed + gated): three Lean audits reported 0 candidates when handed a single file'
status: completed
type: task
priority: normal
created_at: 2026-08-30T14:57:21Z
updated_at: 2026-08-30T14:57:37Z
---

Three audit scripts under `scripts/` take positional roots and call `rglob`,
which matches nothing on a **file** path. So `<script> path/to/One.lean` scanned
nothing, printed a clean result, and exited 0 — an absent check indistinguishable
from a passing one, which is the defect signature this session kept finding
elsewhere.

**How it was found: I hit it.** I ran
`lean-vacuous-existential-audit.py --diff <file>` and reported "vacuity clean"
before noticing the output said `scanned 0 .lean files`. There is no `--diff`
flag either, and its absence is silent — `--diff` is simply taken as a root,
matches nothing, and contributes 0.

| script | given one file | note |
|---|---|---|
| `lean-vacuous-existential-audit.py` | `scanned 0`, exit 0 | the one I hit |
| `lean-self-assuming-audit.py` | `scanned 0`, exit 0 | |
| `lean-one-sided-binder-audit.py` | **no file count at all**, exit 0 | worst: nothing in the output to notice |

`real-sorry-scan.py` already handled file roots correctly
(`if root.is_file() and root.suffix == '.lean'`) and is the pattern followed.

**FIXED (commit `f16fa97cfb`)** — two changes each:
1. a root that is a `.lean` file is scanned as that one file;
2. scanning **zero** files exits **2** with an explicit "this is NOT a pass",
   instead of reporting success. `lean-one-sided-binder-audit.py` additionally
   now prints a scanned-file count, which it never did.

**VERIFIED IN BOTH DIRECTIONS**, because a fix that silently scanned nothing
would look identical to one that worked:
- one file → each reports `scanned 1`;
- `content/quantum-observable-universe/lean/QOU/BraidKnot` → each reports
  `scanned 391`, exit 0;
- an **empty directory** → each exits **2**. That is the control.

**NOT DONE / open.** No CI gate calls these three, so nothing enforces the new
exit-2 behaviour; it only protects a human or agent who runs them by hand. If
they are ever wired into a workflow, the empty-root case is the one to assert
on. Also unchecked: whether other `scripts/*.py` outside the `rglob` shape have
the same absent-check-reads-as-pass property by a different mechanism.
