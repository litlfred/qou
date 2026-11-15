---
# qou-wkcj
title: 'Convention-D chirality remark + corner sl2 persistence (n>=4): exclusive at n=4 only, weighted [3]_q:1'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
    - chirality
    - weak
parent: qou-qs0e
blocking:
    - qou-hlx7
created_at: 2026-11-15T10:30:00Z
updated_at: 2026-11-15T10:30:00Z
---

Owner decisions relayed 2026-11-15 by coordinator session_01M5GA1LmsEf8tSMxFjMkmnn after #7855 merged:
(b) add one remark recording convention D's one-sidedness (observation; weak-chirality identification
stays scope (a)); (a) pursue the corner sl2 in H4 and beyond, headline that the n=4 exclusive
one-sidedness does not persist at n=5, and state what survives (weighted / limit version).

Session: https://claude.ai/code/session_01Qmmkt6RTXyN5gg3AQBGRy7
Branch: claude/conventionD-chirality-corner-sl2-2026-11-15

Result: exclusive one-sidedness is an n=4 accident. What survives at every n is a WEIGHTED bias
tau(P+) : tau(P-) = [3]_q : 1 (Lean ConventionDLineWeights.lean, n-independent, from tau(1)=1 and
tau(sigma)=z_D alone). The sl2-carrying parts of the two corners tend to the same ratio
(probe corner_sl2_weighted_persistence_probe.py, n=16: 3.0459 vs [3]_q0 = 3.0437). The bias is
bar-invariant in size and equals 3 at q = 1, so it belongs to convention D, not to |q|>1.
Remark rem:convention-d-chirality-side added in mass-theory (interprets
prop:markov-trace-frobenius-selection).

## 2026-11-15 handoff (stand-down, coordinator thread session_01Qmmkt6dCyH72NJwcLGW2sF)

Done on draft PR #7867 (branch claude/conventionD-chirality-corner-sl2-2026-11-15):
remark rem:convention-d-chirality-side; Lean ConventionDLineWeights.lean (verified, lean-direct
exit 0, no sorryAx); probes corner_sl2_weighted_persistence_probe.py and
corner_sl2_parity_probe.py (all pass); audit §7 and §8.
Open: the remark is NOT machine-validated (folio-assistant clone fetch timed out; manual render
battery only). Stays in-progress: the chirality identification (scope a) is open.

## 2026-11-15 corner doublet vs flavour (owner priority 3)

Probe computations/probes/corner_doublet_vs_flavour_probe.py, audit §9. The H₄ (3,1)
doublet on σ₁'s left line is NOT flavour-as-orientation: σ₃⁻¹|_D = σ₃|_D − h·I fixes both
states; the two states are σ₃'s eigenlines (q, −q⁻¹). Scope (b), invariant = quadratic
relation, conditional on #7836 reading. Branch claude/corner-doublet-vs-flavour-2026-11-15.

## 2026-11-15 validator run (platform pin 82b389982)

`bun run scripts/run-validate.ts folio/quantum-observable-universe` on branch head 1d067551b:
"16 issue(s)" — the same count the pin note records as the baseline at this platform; none of
the 16 names rem:convention-d-chirality-side (its interprets/uses/cites all resolved). All 16
are pre-existing (unresolved cites faddeev1996/manuscript/bokut1978/milnor1950, unlisted blocks,
deferred simulators, one missing Lean decl). The earlier attempt filled the disk via the
folio-assistant clone; re-run with a disk guard succeeded at 14 GB free.
