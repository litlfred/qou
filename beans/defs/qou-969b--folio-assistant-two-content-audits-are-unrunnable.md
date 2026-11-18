---
# qou-969b
title: 'folio-assistant: two content audits are unrunnable against a multi-paper folio'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - close-candidate
created_at: 2026-09-02T21:49:25Z
updated_at: 2026-10-04T15:19:14Z
parent: qou-5vkl
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


## NARROWED 2026-09-02 — the criteria DO run; only the two standalone scripts do not

My original framing said the verdicts of these two audits are unavailable. **That over-stated
it.** The *criteria* they correspond to run fine under `qa-sweep` (which takes an explicit path
and so never calls `requirePaper`), and both PASS on the two blocks in question:

    proof-conditional-class-banner        pass   (qa-checkers-extended.ts)
    proof-no-conj-propagation-violation   pass   (qa-checkers-extended.ts)

So the §3b epistemic-status axis IS checked and green. What is genuinely unavailable is only the
two **standalone, witness-emitting** scripts — `conjectural-propagation-audit.ts` and
`conditional-class-banner-audit.ts` — which produce corpus-wide audit witnesses
(`docs/audits/2026-05-01-p3-1-conjectural-propagation.witness.json` and its banner twin) rather
than per-block sidecar entries. Those witnesses cannot be regenerated from a multi-paper folio.

The bug and its one-argument fix are unchanged. Only the impact claim shrinks: it costs the
corpus-wide witnesses, not the per-block verdicts.

In-progress in Round 98 PR litlfred/qou#8442.
