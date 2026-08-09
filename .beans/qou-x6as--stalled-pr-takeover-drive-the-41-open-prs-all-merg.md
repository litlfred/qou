---
# qou-x6as
title: 'Stalled-PR takeover: drive the 41 open PRs (all merge clean) cluster by cluster'
status: todo
type: milestone
created_at: 2026-08-09T02:13:58Z
updated_at: 2026-08-09T02:13:58Z
---


Owner instruction 2026-08-09: *"take over stalled agent PRs"* / *"review and
dispense all 1 2 3 4 5"*.

Measured inventory + clusters + the two measurement traps:
[`docs/coordination/2026-08-09-stalled-pr-takeover.md`](../docs/coordination/2026-08-09-stalled-pr-takeover.md).

**Headline: 41 open PRs — 26 merge cleanly, 15 CONFLICT with main.**
Largest contributes 7,071 lines; median well under 500.

Conflicting: `3807, 4133, 4409, 4548, 4515, 4565, 4582, 4596, 4594, 4600,
4571, 4608, 4532, 4685, 4673`. They need a rebase before anything else can be
said about them.

> **CORRECTION.** This bean first said "all 41 merge cleanly". Wrong — it came
> from `git merge-tree <base> <b1> <b2>`, git's **deprecated** trivial-merge
> form, which does not reliably report conflicts. Use
> `git merge-tree --write-tree origin/main origin/<branch>` and check the
> **exit code**.

## Dispensed (PR #4834)

- **#4766** — coordinated. Its `N_eff ~ 2.5995` exclusion of convention C is
  now a theorem for *every* rank (`zC_not_fibre_family` +
  `zRank_eq_qpow_div_qInt`, sorry-free). Posted the correction that binding
  is **not** settled on C.
- **#4718** — reviewed and A/B measured on current main. Fix is real
  (+12 tests, -2 collection errors) but the *"59 of 86 test files"* headline
  does **not** reproduce, and that figure also ships inside the new
  `conftest.py` docstring. Offered to take it over and correct both.

## Remaining, in recommended order

1. **Infra** (4409, 4451, 4568 + finish 4718) — highest leverage, lowest risk.
2. **Lean bridges** (4685, 4548, 4514, 4532, 4571, 4579, 4435) — sorry-free
   work; gate is `lean-verify.sh` exit 0 + `#print axioms` per changed decl.
3. **Convention/trace/binding** (4766, 4673, 4617) — overlaps #4834; do while
   that context is warm.
4. **SM gap probes** (14 PRs) — mostly honest negatives; the review question
   is scope discipline (a) vs (b), per AGENTS.
5. **c_k / Stokes / Habiro + old keystone** (9 PRs) — oldest, most likely to
   be superseded; check each against main before reviewing.

## Standing constraints

- **Merging needs the owner's explicit per-PR go** (AGENTS §7). "Merges
  clean" is a `git merge-tree` fact, not a correctness claim.
- CI auto-triggers are disabled repo-wide, so each PR needs its own agent-run
  evidence in the merge rationale. Never write "CI green".
- Do **not** close or delete any branch (AGENTS §9).

## Two traps, both hit in the first hour

- `git fetch --depth=1` leaves the clone **shallow** and silently corrupts
  every ahead/behind count. `git fetch --unshallow` before measuring.
- **`git merge-tree` has two forms and the old one lies.** `--write-tree` +
  exit code. The 3-arg form reported 41/41 clean when the truth was 26.
- **A branch's raw files are not what would land** when main also moved those
  files. Verify the merged tree, or you check a version that will never exist.
- PR size must be the **three-dot** diff. The two-dot diff reports ~22,000
  files for a four-file PR because it includes main's own progress.
- `pytest computations/` **mutates the tree** — it regenerated four
  `*.witness.json` files. Check `git status` after any collection run.
