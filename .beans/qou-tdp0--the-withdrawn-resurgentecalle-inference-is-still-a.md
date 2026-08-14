---
# qou-tdp0
title: The WITHDRAWN resurgent/Ecalle inference is still asserted live in 1ppq-qbeta.md
status: todo
type: task
created_at: 2026-08-14T19:37:12Z
updated_at: 2026-08-14T19:37:12Z
---

Found while fixing the same defect one file over, in PR #5022 (registry §3).
Copilot flagged the registry instance; this is the un-fixed remainder.

## The fact

The 2026-08-09 convergence correction
([`2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md`](../docs/audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md))
**withdrew** the resurgent/Écalle inference for the odd-channel D-ladder. The
KC22 row of `ck-dk-canonical-registry.md` records the withdrawal correctly —
the sentence is struck through and marked `WITHDRAWN 2026-08-09`, with the
reason: the inference was drawn from a *divergence*, and the ladder is
**convergent** (`k²Δ²log|d_k| → 1`, `kΔ² → 0`, so `κ = 0`).

The correction was applied to the KC22 row and **not propagated to the
summaries that restate it**. Two sites:

1. **`ck-dk-canonical-registry.md` §3 (line ~140)** — FIXED in PR #5022. It
   asserted "a genuine c₃ closure, if any, is transcendental/resurgent
   (Écalle class), not a q-difference equation" — nearly verbatim the
   sentence KC22 strikes through.
2. **`docs/coordination/1ppq-qbeta.md:1055-1058`** — **STILL LIVE.** Reads
   "(validator green): the odd-channel element is transcendental/**resurgent**
   (Écalle class) — the low-order (q-)holonomic search class is CLOSED. Do
   not …". This one is worse than a stale summary: it is an **instruction to
   future agents** resting on a retracted premise.

## What is NOT claimed here (scope discipline)

**This is not a refutation of the Écalle/Borel route.** The withdrawal is
specific and narrow: it kills the *inference from divergence*, because the
divergence is not there. It does **not** establish that Borel/Écalle
machinery is inapplicable — a convergent series with a log branch point
(`D(w) = φ(w)log(1−w/ρ) + ψ(w)`, KC22's own closed form) is still a legitimate
object for that machinery, and "Écalle median / M-dictionary lateral" as used
around `1ppq-qbeta.md:2143,2151` is a *normalization technique*, a different
usage that this bean does not touch.

Scope-(a): the defect is that a **withdrawn inference is stated as live**, not
that the surviving route is wrong. Do not convert this into a scope-(b)
exclusion without a proved invariant.

## Work

1. Triage all ~10 `Écalle|resurgent` hits in `docs/coordination/1ppq-qbeta.md`
   (lines ~1055, 1056, 1058, 1170, 1313, 1407, 1532, 1809, 2143, 2151).
   Per hit, classify: (a) the **withdrawn class-membership inference** → fix,
   citing the 2026-08-09 correction; (b) **Écalle/Borel as technique** →
   leave; (c) ambiguous → leave and note.
   Line 1055-1058 is (a) and is the priority.
2. **Then** check whether any open Écalle bean is *motivated* by the withdrawn
   inference rather than by the technique: `qou-a1bi`, `qou-b00b`, `qou-dri7`,
   `qou-xuc4`, `qou-jjka`, `qou-vkg5`, `qou-r2nh`, `qou-u7kc`. This is a
   **question, not a verdict** — a bean pursuing acceleration on the *closed
   form* is unaffected. Record findings on each bean; do not mass-close.
3. Grep wider (`docs/`, `content/`) for the same restatement — the pattern is
   a correction applied to a detail row and not to its summaries, so other
   summary sites are likely.

## Why it matters

Same defect class as PR #5022's two: a summary out-running the detail row that
corrects it. The corpus-grep discipline in AGENTS.md exists because agents
trust status lines; an instruction that says "the search class is CLOSED, do
not …" on a retracted basis will steer work wrongly and is the most expensive
version of this bug.
