---
# 8we6
title: 'u-rung tie decision: genuine c4 rungs — H4 Hoefsmit build for c4^even + c4^odd beyond CAL-anchor (Casoratian W3 sign test)'
status: in-progress
pr: 8191
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-02T12:03:38Z
updated_at: 2026-10-04T15:14:17Z
parent: qou-frzo
---

## 2026-07-02 — re-scoped after sibling 1jrh execution (supersedes original scope)

Original scope ("test Q_beta c_k vs binding ladder share ONE bar-even AW
multiplier at u = b*hbar_q^2") was EXECUTED by the sibling 1jrh session to its
measurable limit: c2^even = -8.00641 and c3^even = +86.66116 measured EXACTLY
(qbeta_c3even_exact_sseries_probe.py, ℚ[√3] closed forms); Casoratian
W2 ≈ +102.67 > 0 (consistent, does not yet decide); W3 GATED — with the two
untrusted c4 inputs it comes out < 0 (scope-(a) indicative lean AGAINST
one-recurrence in u), decision needs genuine c4 rungs.
Read first: docs/audits/2026-07-02-1jrh-c3even-exact-measurement.md +
docs/audits/2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md.

REMAINING WORK (this bean):
1. c4^even — the H3 NF basis is exhausted at k>=4 (Stage-B); needs the H4
   Hoefsmit build of the net-route ladder (4-strand extension of the
   exact-rational s-series machinery).
2. c4^odd — a derivation beyond CAL-anchoring (current c4^odd ≈ -0.97 is
   below trust tier).
3. Then the one-line decisive test: W3 = c3^even*c4^odd - c4^even*c3^odd;
   AW positivity requires W3/W2 > 0; violation refutes one-recurrence in u
   (scope-(a): in the u-ladder form).

Constraint recorded by sibling: even rungs grow ×11, ×21 ⇒ even-side u-ladder
at best asymptotic — disfavors a common AW recurrence IN u; the surviving
object is the fibre kernel R(q,ξ).

## 2026-07-03 — route B PRUNED structurally; route A gated on owner object choice
Owner authorized B+A+C. Route B (same Delta(net), lambda|-4 re-decomposition)
is pruned by a one-line argument BEFORE building: Markov-trace consistency
(tau^(4)|_H3 = tau^(3)) + branching rules make every lambda|-4 reading of the
unchanged element a linear function of known H3 data — no independent N=4
rung possible. Scope-(a) with invariant cited. Route A (sigma_2-support
object) is the only live H4 route; needs 2 owner design choices (4-strand
confinement braid — no canonical B4 in corpus — and 4th-strand type/crossing).
Stability gate: must reproduce c2^even=-8.00641, c3^even=+86.66116 exactly in
the decoupling limit. Route C = F(q) keystone, unchanged.
Audit: ../docs/audits/2026-07-03-8we6-h4-route-b-structural-prune.md

## 2026-07-13 — Route A EXECUTED: all three owner-authorized framings GATE-FAIL

Owner authorized building all 3 candidate framings (PR #3769 session). Probe
`computations/qbeta/qbeta_h4_route_a_gate_probe.py` (+ witness): A1 brane/Hopf
pairwise extension, A2 lepton strand (s1 s2 s1 appended), A3 4-Brunnian core
candidate `(s0 s1^-1 s2 s1^-1)^3` — ALL FAIL the decoupling gate: c2 shifts
exactly +12, +13/6, -40 (sigma_2 content enters the ladder at u^2, not u^4).
No c4^even rung produced; W3 stays gated (item 3 unchanged). Surviving
criterion for any future candidate (cheap a-priori check):
log(Delta(net)_4 / Delta(net)_3) = O(u^4) — appended couplings, pairwise
extensions, and core replacements all violate it at leading order, mechanically
corroborating Stage-B "longer braid words, entangled mid-word".
Audit: docs/audits/2026-07-13-8we6-h4-route-a-three-framings-gate-fail.md

## Status annotation (2026-07-17, session qou-xhjl)

Item 1 (canonical c4_even via H4 route A) executed NEGATIVE 2026-07-13: all
three owner-authorized 4th-strand framings GATE-FAIL (exact rational c2
shifts +12, +13/6, -40 — sigma_2 content enters at u^2, not u^4), plus six
mid-word candidates FAIL/TRIVIAL (9/9 zero survivors). See
docs/audits/2026-07-13-8we6-h4-route-a-three-framings-gate-fail.md.
Surviving cheap admission test: log(Delta(net)_4/Delta(net)_3) = O(u^4).
Per the audit's disposition a genuine c4-first object requires owner-level
framework content (a construction whose low-order cancellation is DERIVED,
not arranged) — bean stays in-progress awaiting that input; do not re-scan.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-03 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (PR #8191)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/ResurgenceCasoratianAndBarSymmetrization.lean` (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 advisory` across all 7 static vacuity/borrowed-name audits) and wired into `QOU.lean`.
- [x] Verified exact rational witness in `computations/probes/resurgence-casoratian-and-bar-symmetrization.witness.json` (`scriptHash: 2c8e09c0d6af`, `scriptCommitSha: e9de8818430aa7aa5b7c9bf66d2b0bab443b968f`, `allPassed: true`, `0` raw `float64` fields).
- [ ] Awaiting Merge Manager merge of PR #8191 (`8351218487c53d0f60e66b9d4c335ccaab315d98`).
