---
# qou-rm57
title: 'Convention-frame audit: 7 derivation documents disagree with canon and do not say why'
status: todo
type: task
priority: normal
created_at: 2026-08-30T14:44:08Z
updated_at: 2026-08-30T14:44:54Z
---

Opened by [`computations/audits/derivation_convention_frame_audit.py`](../computations/audits/derivation_convention_frame_audit.py),
written 2026-08-30 after `qou-46ab` turned up two artifacts disagreeing by
**7.55 %** about one quantity, both of which `derivation_chain_validator.py`
passed — correctly, since it validates *structure* and a convention frame is
not structural.

**Result: 84 documents scanned, 7 with an undeclared frame.**

## The two decisive rows

`1.0653062285923893` appears in **`markov-trace-assembly-proton.derivation.json`
and `p-tr-M-q0.derivation.json`**, and it is measurably the convention-C proton
trace, not a coincidence:

    found        1.0653062285923893
    exact C      1.0653062286131670593652845464313725576506616741348
    rel          1.95e-11   -- agrees to 10 digits, diverges at the 11th
    canon (D)    1.1457596924573009            -- 7.02 % away

So it is the C value **float64-truncated**. That spelling is why `qou-46ab`
never listed these two files: its grep keyed on the exact 19-digit prefix, and
a truncated twin is invisible to it. **This is the same detector-blindness
class the corpus catalogues, one artifact type over.**

The neutron pair `0.9232332299116371` / `0.9232332971695838` (in
`markov-trace-assembly-neutron` and `n-tr-M-q0`) sits 6.53 % from canon — the
same magnitude class as the proton's 7.02 %, so probably the C neutron. **Not
asserted**: I did not locate an exact C neutron reference to check against, and
saying "probably" is the honest state.

`2.12258250945273` and `1.58939344` are larger (85 % and 61 % from canon) and
are most likely intermediate, unnormalised quantities caught by the audit's
nearest-atom-word heuristic. Treat as suspected false positives until read.

## What the audit does and does not claim

Deliberately **high recall, keyed on disagreement with canon** rather than on a
table of convention-C values — hardcoding those twins would be a second
hand-maintained copy of a number, which is the failure being audited. So a
finding says *"this disagrees with `derivation_chain.py::TR_M_AT_Q0` and the
document does not say why"*, never *"this is convention C"*. The cause could be
a stale convention, a stale pin, or a typo.

`--selftest` is the guard: it must FLAG the pre-scoping `markov-peel` document
and CLEAR the scoped one, and exits **2** (not 0) if the revision is
unreachable, so an unrunnable self-test cannot read as a passing one.

## The bug the self-test caught, worth keeping

The first version searched the **whole file** for a convention declaration and
therefore **missed the very case it was written for**. The pre-scoping
`markov-peel` document discusses conventions at length in its *step notes* —
*"under the canonical convention D, z = q³/(q²+1)"* — while never saying which
frame its own numbers are in. A whole-file search read that as a declaration.

**The inversion is the point: the document that talks most about conventions is
the one most likely to be silently in the wrong one**, and a topic-keyed
detector exempts it precisely because it is well-informed. The check now looks
only at document level (`target` / `description`), where a scoping claim
belongs.

## The work

Per file: read it, establish which frame its numbers are actually in, then
either **scope** it (state the frame at document level, as
`markov-peel-atomic-tr-m.derivation.json` now does) or **correct** the value if
it is simply wrong. Do not batch-label — the audit deliberately cannot tell
those two cases apart, and guessing would put a false convention stamp on a
typo.

**Default if nothing is done:** the audit reports and does not gate (exit 0
always). Nothing breaks; the seven keep disagreeing with canon silently, which
is the state that let a 7.55 % contradiction sit in two artifacts unnoticed.


## CORRECTION 2026-08-30 — 6 documents, not 7, and one row class was mine

Two corrections to the numbers above, both found by re-running the audit after
a rebase rather than trusting the first run.

**One of the seven was a PURE FALSE POSITIVE.**
`canonical-tr-m-via-chi-cache.derivation.json` lists every atom in one
sentence — *"proton 1.145759…, neutron 0.987743…, deuteron 0.575172…, tritium
0.229310…"* — and tritium, helium-3 and helium-4 were not in the audit's atom
table at all. The nearest *preceding* atom word for the tritium value is
therefore `deuteron`, and it was reported as a deuteron disagreeing with canon
by 60 %. Its proton / neutron / deuteron values are the **correct convention-D
ones**; nothing was wrong with the document.

Fixed by recognising those names so their values are **skipped** for want of a
reference (`TR_M_AT_Q0` holds p/n/D only) rather than silently reattributed.

    rows       16 -> 13
    documents   7 ->  6   of 84

**And a repair I committed before this one did nothing.** I claimed bare `"d"`
was being accepted as deuteron, made single-letter matching case-sensitive, and
wrote *"rows drop 15 → 12"* into the commit message. The change was a **no-op**
— audit output byte-identical across it — and the 15 → 12 was never measured; I
read it off a truncated `tail`. That commit was squashed into an honest one
(`c7dae15d3d`), which records both halves.

Worth keeping in this bean rather than only in git history: **the audit's own
first two reports each contained an unmeasured number, written by the agent
building the detector for unmeasured numbers.** The discipline that caught both
was the same one the audit exists to enforce — diff the actual output, do not
eyeball a tail.

**The live finding set is the six**, and the two decisive rows above (the
float64-truncated convention-C proton in `markov-trace-assembly-proton` and
`p-tr-M-q0`) are unaffected — they were measured against the exact C value, not
eyeballed.
