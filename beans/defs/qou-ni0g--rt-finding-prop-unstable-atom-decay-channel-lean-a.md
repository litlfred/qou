---
# qou-ni0g
title: 'RT finding: prop:unstable-atom-decay-channel — Lean assumes the uniqueness it claims; IVT conjunct is on an arbitrary function; narrative is self-contradictory'
status: todo
type: bug
priority: high
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-20T08:40:00Z
parent: qou-ncxf
---

qou-ncxf pass-1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B02).

- Lean: `folio/quantum-observable-universe/knots-particles-confinement/unstable-atom-decay-channel.lean`, the theorem at about line 120. Uniqueness of minimisers follows directly from hypothesis `hsel` (off the boundary, every minimiser equals `lamStar`). The second conjunct is the intermediate value theorem for an arbitrary continuous `E` that is unrelated to the atom. `IsMinimiser`, `OnBoundary` and `E` are free parameters.
- The `.md` statement claims existence and uniqueness of the violated constraint λ*(K,q). The Lean asserts no existence; its uniqueness is assumed.
- The narrative proof (`folio/quantum-observable-universe/knots-particles-confinement/unstable-atom-decay-channel-proof.md`) has two problems. Under the existential form, x = 0 is always feasible, so "unstable" is vacuous; the proof's own scope note concedes this. And it asserts "the LP relaxation is the convex hull of integer solutions", which is false in general.

Needs: a non-vacuous instability definition, plus Lean that derives uniqueness rather than assuming it. Overlaps W8 (de-vacuify) / W10 (class-field debt). Do not close until the statement is re-derived or demoted.
