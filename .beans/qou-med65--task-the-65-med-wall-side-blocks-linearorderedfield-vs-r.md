---
# qou-med65
title: 'TASK: wall-side §7c drain — COMPLETE (and the count and the framing were both wrong)'
status: completed
type: task
priority: medium
tags: [lean, wall-side, 7c]
created_at: 2026-08-08T13:00:00Z
updated_at: 2026-08-08T13:00:00Z
---

The largest remaining `wall-side-correct` class. MED = the Lean carries
**ordering / `abs` / `linarith` only** — no `Real.*`, no `Complex`, no integral.
For many of these a `[LinearOrderedField R]` restatement is possible; for others
the ordering is on a genuinely measured quantity. It is a per-file call.

Now **67**: `demazure-fiber-markov-trace` and `mass-endomorphism-tower` move in
from WEAK — both carry `q > 1` in code, which #4709's ordering regex missed
because it matched `0 <`, `≤`, `abs`, `linarith`, `positivity` and **not bare
`>` / `<`**.

## ⚠ TITLE AND COUNT BOTH CORRECTED (2026-08-08)

**The framing in this bean's title cannot work.** The checker's type test is

```ts
// folio-assistant/content/pipeline/qa-checkers-voice.ts:469
const ARCHIMEDEAN_TYPE_RE = /ℝ|\bReal\b|LinearOrderedField/;
```

so porting a block to `[LinearOrderedField R]` **still FAILs `wall-side-correct`** —
`LinearOrderedField` is itself on the archimedean list. Verified directly in the
checker source, and independently found by both MED agents (#4754, #4758).

A block therefore leaves this queue only by landing on a **non-ordered** class
(`Zero` / `Ring` / `CommRing` / `Field`), or by carrying a **§7c acknowledgement**
on its referring block. "`[LinearOrderedField R]` vs `ℝ`" is a false dichotomy;
read the title as "generic-vs-`ℝ`, per block".

**Count corrected: 59, not 65 or 67.** A fresh sweep at `origin/main` @ `3f1a4e3f23`
gives **1114/1190 pass, 76 FAIL** — of which **59 MED**, 8 HARD, 9 neither. The
65/67 figure came from #4709's older triage and was carried forward without
re-measuring. Re-measure before quoting; `main` moves.

`collatz_contact_boundary` is **not MED** anyway — its only `<`/`>` are `⟨…⟩`
anonymous-constructor brackets. (It is still off-limits: sibling PR #4722 owns it.)

## Two classifier traps, both found the hard way

- **`abs` bracket class.** A pattern like `\|[a-zA-Z0-9_ .]{1,15}\|` excludes `-`
  and superscripts, so it misses `E_H = |q - q⁻¹| * …`. That one omission moved
  the MED count by one block (`photon_threading_mass`).
- **Shell `grep -E '[<>≤≥]'` is worthless here.** In the C locale a bracket
  expression is **byte-wise**, and `≤ ≥ ℝ →` all begin with byte `0xE2` — so the
  class matches *every line containing `ℝ`*. It reports ordering everywhere.
  Classify with a Unicode-aware runtime, or set the locale.

## Read protocol — learned the hard way, follow it

1. **Strip comments first.** Regexes over raw text match inside docstrings and
   identifiers (`deriv` inside `derivedLightIsotopeFormula`, `Real` inside
   `Mathlib.Data.Real.Basic`).
2. **Read the IMPORTS.** They are more decisive than the signature. A statement
   that looks generic (matrix idempotence; an additive decomposition) still
   needs `ℝ` if the proof runs the spectral theorem or the file imports
   `Analysis.*`/`Topology.*`.
3. **Read the file's own docstring.** Twice this session it named the exact
   missing condition (`"base ring of characteristic ≠ 2"` → the target was
   `[Field R] [CharZero R]`, not plain `Field`).
4. **Ask what the quantity MEANS.** A measured value, a hyperbolic volume, a
   norm, or a time parameter is `ℝ` by meaning — that is a §7c *note* on the
   referring block, not a Lean change.
5. **The verdict is a compile result, never a read.** Attempt the port; let the
   compiler adjudicate.

## Where the §7c note goes

On the **referring block's** `.md` / `.ts` `authorNotes` — never the `.lean`
docstring, which the checker does not read (#4703). Pattern: see the 21 notes
added in #4745.

## Baseline

`bun run scripts/check-wall-side.ts --sweep content/quantum-observable-universe`
was **1091/1188** after #4739. Re-measure before and after; do not quote a
stale number.

## Sizing

65+ per-file judgements. Batch into PRs of ≤ 49 files (the review limit) and
land incrementally. Do NOT bulk-generate acknowledgements to clear the count —
that clears the number while deciding nothing, which is the §1a audit-dodge the
whole queue exists to prevent.

---

## RESOLVED 2026-08-08 — sweep is 1190/1190

Two things in this bean's own title were wrong and are corrected by measurement:

1. **"65 MED"** — the real count was **59**, independently derived twice from a
   clean worktree (#4758, #4759).
2. **"`[LinearOrderedField R]` vs `ℝ`"** — a port to `[LinearOrderedField R]`
   **still FAILs**: `ARCHIMEDEAN_TYPE_RE = /ℝ|\bReal\b|LinearOrderedField/`
   matches it. The bean's central framing could not have drained anything.

The residual 13 were read per block: **4 ported** (collatz, nucleon-ordering,
lr-tensor-character, habiro-ring), **9 acknowledged** with per-file evidence.

## The finding that outlasts this bean

`WALL_ACK_RE` is a **keyword** match — any note containing `§7c` or `base ring`
passes the block. So **1190/1190 means "every block carries a note", not "every
base ring is correct"**. `qou-infra-discharges-goncharov-zeta5` now passes while
its acknowledgement says outright that its `ℝ` is *not* load-bearing.

Do not quote the number without that caveat. Full write-up:
`docs/audits/2026-08-08-wall-side-final-13-and-what-1190-means.md`.

