---
# qou-87ms
title: check-sidecars.sh reads only the working tree — a clean run on a committed branch proves nothing
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T21:20:58Z
updated_at: 2026-10-04T15:16:55Z
parent: qou-5vkl
---


## The gap

`scripts/check-sidecars.sh` builds its file list from the **working tree only**:

```bash
mapfile -t files < <( { git diff --name-only HEAD; git diff --cached --name-only; } | sort -u )
[ "${#files[@]}" -eq 0 ] && { echo "check-sidecars: no changed files."; exit 0; }
```

Run as a **pre-commit** preflight (its documented role) this is correct. But it is
also being used, and quoted in PR descriptions, as a **branch-level verification
gate** — and there it is vacuous: once the work is committed the working tree is
clean, so it prints *"no changed files"* and exits 0 without ever looking at the
diff. A green line reading "check-sidecars: clean" is then evidence about the
working tree, not about the branch.

This matters more than usual right now because AGENTS.md §Phase-4 makes the
agent's own verification the merge gate (CI auto-triggers are disabled
repo-wide), and `check-sidecars` is one of the three legs named there.

## Observed instance

PR #4791 (`qou-qint`) reported `check-sidecars.sh` → *clean* in its description.
Checking the sidecars directly instead showed **4 of 4** affected content-block
sidecars were stale — `source_hashes.lean` still recorded main's hashes, and the
same hashes were verifiably *fresh* on `origin/main`, so the branch really had
staled them. Fixed there in `1f671248`; the checker had not been wrong, it had
simply never been asked about those files.

## Suggested fix

Give the script an explicit range mode so it can gate a branch, e.g.

```bash
scripts/check-sidecars.sh --since origin/main     # git diff --name-only origin/main...HEAD
```

keeping the current working-tree default for the pre-commit path. Then update
the AGENTS.md §Phase-4 verification wording to name the range form, so a PR that
says "sidecars clean" means it.

## Related

Same structural pattern — *a checker scoped to changed files never establishes
that anything else complies*:

- `qou-q7cm` — §7c mixing in `GaugeFieldFluidDynamics` / `MassComputationChainRoadmap`,
  pre-existing but only surfaced when the files were touched.
- `qou-orph` / `qou-k448` — orphan library Lean modules nothing checks
  (e.g. `braids-and-knots/chi-std-pernucleon-closed-form.lean`, red on main).

- **Round 97 (`litlfred/qou#8432`)**: Advanced in `feat/round97-monotone-multbound-ncpart-nonuniform-onebody-43c1` (Commit 1 `e883e42fdde30a6d22e385b72041c6f52899312f`, Commit 2 `56d66b28962228fdc58ad152218bdd3754f7c059`, probe sha256 `e41a92695f7287bc24947a7f23e2cb1aff6e02fcb3b0e34fb76f50f0c076b259`).
