# Coordination — `respects_archimedean_wall` per-script swaps (deferred)

**Date:** 2026-05-24
**Status:** Bulk codemod attempted on this branch, **reverted** —
documenting why and what the per-script workplan should look like.
**Trigger:** [PR #1110](https://github.com/litlfred/qou/pull/1110)
took `respects_archimedean_wall` from 74 → 37 fails via probe/audit
exemption + 4 audit-tag annotations. The remaining 37 (now 36 after
this PR's display-context exemption) are real production scripts
with `math.X` / `np.X` substrate-compute calls per the user
direction ("float NEVER in production").

## What I tried (and reverted)

A bulk codemod that swapped `math.X / np.X / numpy.X / scipy.X`
→ `mp.X` across 32 production scripts (~100 individual call
sites). Two variants:

- **v1:** straight swap. Cascaded `mpmath.mpf` into downstream
  format strings — `mpmath 1.3.0`'s `mpf.__format__` doesn't
  support `:.Nf` format specs, so `print(f"{x:.4f}")` where
  `x = mp.log(...)` throws `TypeError: unsupported format
  string passed to mpf.__format__`. Broke ≥ 6 of 9 sampled
  scripts at runtime.
- **v2:** swap + wrap `mp.X(...)` inside f-string format
  braces with `float(...)`. Still broke ≥ 4 of 9 sampled
  scripts because `mp.X` results FLOW INTO downstream
  variables that get formatted ELSEWHERE in the script (the
  cascade is multi-line, codemod only sees in-brace usage).

Both reverted. Production scripts are back to working state.

## Why the bulk approach fails

The codebase has a **type-propagation cascade** pattern: substrate
compute chains use `q`, `q_inv`, `h`, `α` etc. as `mp.mpf`. If
any of these flow through a `math.X(...)` call (currently
returning `float`), then THAT call result is also `float`. Once
that float reaches a format spec, formatting works.

Swap `math.X` → `mp.X`: the call result is now `mpf`, the chain
downstream becomes `mpf`, and any format spec on a downstream
variable fails.

The fix per affected script is:
1. Swap the substrate `math.X` → `mp.X` (correct intent)
2. AT THE FINAL DISPLAY SITE, wrap in `float(...)` to coerce for
   format-spec compatibility

This is **per-script architectural work** — requires reading the
script's data flow, identifying the boundary between substrate
compute and display, and inserting `float()` at that boundary.
Not amenable to a single mechanical codemod.

## This PR — what it DOES do

- Adds **display-context exemption** to `checkRespectsArchimedeanWall`,
  mirroring PR #1093's pattern on `checkDoesNotDefaultToFloat`. A
  `math.X(...)` inside `print(f"…{math.X(x):.4f}")`, `assert math.X(x)
  < 1e-6`, or assigned to a `_pct` / `_ppb` / `_ppm` / `_print` /
  `_display` / `_str` / `_repr` variable is **display-context** and
  passes the criterion.
- Effect: 37 → 36 fails (only −1 — most production fails are real
  substrate-compute, not display).
- Adds this coord doc to record the deferred per-script work.

The exemption is small but principled: it aligns
`respects_archimedean_wall` with the same display-context rule
`does_not_default_to_float` uses. The two criteria now treat
"display contexts" consistently, preventing future codemods from
breaking display formats.

## What this PR does NOT do

- Does NOT swap any `math.X` → `mp.X` in production scripts. The
  bulk approach broke runtime; the per-script approach is multi-
  session work.
- Does NOT propose specific PR slicing — see the workplan below
  for one possible approach.

## Per-script workplan (multi-session)

For each of the 36 remaining production fails:

1. **Read the script's module docstring + the offending call site.**
   Confirm the `math.X` is substrate-compute (not display).
2. **Identify the data flow.** Where does the `math.X` result get
   consumed downstream? Does it reach a format-spec print/return/
   serialization site?
3. **Swap `math.X` → `mp.X`.**
4. **At downstream display sites:** wrap the value (or the
   relevant subexpression) in `float(...)` to coerce for
   `:.Nf` format compatibility.
5. **Run the script end-to-end.** Verify no runtime regression
   (`TypeError: unsupported format string passed to mpf.__format__`
   is the diagnostic for missed cascade sites).
6. **Spot-check the witness output**, if any. Some scripts emit
   numerical witnesses where `float()` coercion changes the last
   few digits — confirm the changes are within paper-quoted
   precision (typically 50 dps compute, 10-15 dps display).

Approximate scope:

| script | hits | est. effort |
|---|---:|---|
| 7 single-hit scripts | 7 | ~15 min total |
| 11 two-hit scripts | 22 | ~30 min total |
| 8 three-five hit scripts | 30 | ~1 hour total |
| 4 heavy scripts (6-12 hits) | 38 | ~1 hour each |
| **total** | ~100 | ~6-8 hours focused work |

Suggested PR slicing: 4-5 PRs by category (single-hit, multi-hit,
3-5-hit, heavy). Each gets careful per-script review.

## Related

- [PR #1110](https://github.com/litlfred/qou/pull/1110) — probe/audit
  exemption + audit-tag opt-out (merged; took 74 → 37)
- [PR #1093](https://github.com/litlfred/qou/pull/1093) — display-
  context exemption pattern (merged; the model this PR mirrors for
  `respects_archimedean_wall`)
- AGENTS.md §7c — substrate-vs-archimedean wall directive
- Author direction (2026-05-24): "float NEVER in production"
- 2026-05-24 — `applied_uniqueness_mass_table.py` bug (separate
  cascade pattern — fixed in [PR #1114](https://github.com/litlfred/qou/pull/1114))

## Open question for the author

The per-script swaps WILL introduce `float(...)` calls at display
sites (necessary for mpmath 1.3.0 format compatibility). The user
direction "float NEVER in production" applies to substrate compute
paths. **Is `float(...)` inside an f-string format brace counted
as "production" or "display"?**

- If display (the working interpretation here + in PR #1093 +
  in PR #1088): the per-script swaps are mechanical, the float
  wrap is acceptable display-time.
- If production: then the only fix is to upgrade mpmath to a
  version that supports `:.Nf` on `mpf` (master branch does;
  release 1.3.0 doesn't). That's a dependency pin change with
  its own coordination cost.

The display-interpretation is consistent with the existing
codebase pattern (PR #1093 introduced display-context exemption
for `does_not_default_to_float`). Continuing that pattern here.
