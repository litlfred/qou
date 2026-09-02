---
# qou-969b
title: 'folio-assistant: two content audits are unrunnable against a multi-paper folio'
status: todo
type: task
priority: normal
created_at: 2026-09-02T21:49:25Z
updated_at: 2026-09-02T21:50:01Z
---

## What

`folio-assistant/content/pipeline/conjectural-propagation-audit.ts` (line 41) and
`conditional-class-banner-audit.ts` (line 42) both do

    const ROOT = join(REPO_ROOT, "content", requirePaper());

— calling `requirePaper()` with **no explicit argument**. `repo-root.ts:112` then returns the
folio's paper only when there is exactly one, and otherwise throws:

    error: 5 papers found (bach2013-double-slit, fred2005-formal-groups,
    quantum-observable-universe, unital-groebner-bases, visualizer) — name one explicitly.

## Why it matters

These are the two checkers that adjudicate **§3b epistemic status** — whether a provable block
downstream of a conjecture is a propagation violation, and whether a conditional-class block
carries its banner. In a folio with more than one paper they cannot run at all, so those
verdicts are silently unavailable rather than green.

Found while adopting Route A on `wsxl` (PR #6363), where a block moves
`conjecture` → `proposition` and another drops its conditional banner — precisely the change
these two audits exist to check. Both had to be reported as UNKNOWN.

## Neither takes a paper argument

`argv[2]` is the witness output path in both scripts, and `repo-root.ts` reads no environment
variable. So there is no invocation that works; it is not a matter of finding the right flag.

## Fix (platform-side, litlfred/folio-assistant)

Accept a paper name — a `--paper` flag, or an env var read inside `requirePaper` — and thread it
into the `requirePaper()` calls. The error message already knows the paper list, so the
plumbing is one argument deep.

## Scope

NOT fixable in qou: the code is in the platform repo, reachable here only through the
`folio-assistant/` symlink that `scripts/setup-folio-assistant.sh` creates. Recorded so the
verdicts are known-missing rather than assumed-clean.
