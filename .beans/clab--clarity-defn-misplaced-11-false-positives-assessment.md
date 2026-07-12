---
# clab
title: 'Clarity: clarity-defn-misplaced bucket assessment — all 11 candidates are false positives (do not restructure)'
status: completed
type: task
priority: normal
created_at: 2026-07-12T00:30:00Z
updated_at: 2026-07-12T00:30:00Z
---

## Assessment (2026-07-12) — clarity-defn-misplaced, all 11 fails read + verdicted

`definition-clarity-audit.ts clarity-defn-misplaced` reported 11 fails. Read every
one; **all 11 are FALSE POSITIVES** — none is a genuinely misplaced first-class
definition. Restructuring any would only game a high-recall heuristic (forbidden,
same spirit as the anti-audit-dodging rule). Verdict per block = **legit**:

| block | kind | why false positive |
|---|---|---|
| `sec:spectral-gauge-intro` | prose | "We define X" = roadmap preview of downstream `definition` blocks |
| `sec:yekutieli-lifting-intro` | prose | roadmap preview |
| `ssec:descent-prelim-intro` | prose | roadmap preview |
| `sec:hadron-algebra-intro` | prose | roadmap preview |
| `conj:q-aubin-lions` | conjecture | "We define $\mathcal{H}=\dots$" = inline local notation |
| `prop:q-spectral-sobolev` | proposition | inline local notation |
| `prop:he4-channel-active-set` | proposition | "We define the channel binding residual" = prop-local construct |
| `cor:jet-prolongation-C` | corollary | "Let $P'$ define …" = hypothesis binding (standard statement structure) |
| `rem:vortex-intensity-modes` | remark | defining phrasing in interpretation, no registered term |
| `rem:breit-wheeler-pair-production-derivation` | remark | defining phrasing, no registered term |
| `rem:observable-beable-correspondence` | remark | `:defterm[Cellular Automaton Interpretation]` names 't Hooft's EXTERNAL cited concept (for the table's `:refterm[CAI]`); promoting to a `definition` would demand a nonsensical `.lean` sibling — correctly a remark |

All 10 "soft" ones have `definesCount: 0` (no registered term is misplaced); the
one with `definesCount: 1` (`observable-beable`) is an external-concept defterm.

## Infrastructure gap (why no sidecar verdict was written)

`definition-clarity-audit.ts` is a **standalone advisory scanner** — NOT wired into
`qa-sweep.ts` and NOT present in any `<block>.qa.json` sidecar (grep-confirmed: no
sidecar carries a `clarity-defn-misplaced` entry; qa-sweep has no `definition-clarity`
import). It also has **no opt-out / allowlist / suppression** mechanism (only the
structural glossary exemption). So there is nowhere to persist a per-block "legit"
verdict. This bean IS the durable record of the assessment.

**Follow-up infra option (owner call, not done here):** add a per-block opt-out to
`definition-clarity-audit.ts` (e.g. an `@clarity-ok:<crit>` annotation or a
suppressions list) so agent-confirmed false-positives stop counting against the
high-recall bucket — would improve signal-to-noise on the clarity EPIC. Not
implemented unilaterally (it changes how the audit gates).

## Definition of done

Done: all 11 read + verdicted legit; no source restructure (correct — they're not
misplaced definitions). The clarity EPIC should skip this bucket.
