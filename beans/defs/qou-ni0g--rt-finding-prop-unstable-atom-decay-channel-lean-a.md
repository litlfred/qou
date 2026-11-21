---
# qou-ni0g
title: 'RT finding: prop:unstable-atom-decay-channel — Lean assumes the uniqueness it claims; IVT conjunct is on an arbitrary function; narrative is self-contradictory'
status: todo
type: bug
priority: high
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-21T16:00:00Z
parent: qou-ncxf
---

qou-ncxf pass-1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B02).

- Lean: `folio/quantum-observable-universe/knots-particles-confinement/unstable-atom-decay-channel.lean`, the theorem at about line 120. Uniqueness of minimisers follows directly from hypothesis `hsel` (off the boundary, every minimiser equals `lamStar`). The second conjunct is the intermediate value theorem for an arbitrary continuous `E` that is unrelated to the atom. `IsMinimiser`, `OnBoundary` and `E` are free parameters.
- The `.md` statement claims existence and uniqueness of the violated constraint λ*(K,q). The Lean asserts no existence; its uniqueness is assumed.
- The narrative proof (`folio/quantum-observable-universe/knots-particles-confinement/unstable-atom-decay-channel-proof.md`) has two problems. Under the existential form, x = 0 is always feasible, so "unstable" is vacuous; the proof's own scope note concedes this. And it asserts "the LP relaxation is the convex hull of integer solutions", which is false in general.

Needs: a non-vacuous instability definition, plus Lean that derives uniqueness rather than assuming it. Overlaps W8 (de-vacuify) / W10 (class-field debt). Do not close until the statement is re-derived or demoted.

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Re-checked against main 2ae54ab40: the finding still holds as recorded (B02 `prop:unstable-atom-decay-channel`. Note the block now lives at `mass-theory/unstable-atom-decay-channel.{md,ts,lean}` (this bean's `knots-particles-confinement/` path is stale).).
- Disclosed, not fixed: a dated `caveat` authorNote on the block's `.ts` (commit 24c44167e) says exactly what the Lean proves and what it does not. Kind, prose, `uses[]` and Lean untouched.
- The kind change / restatement / demotion is an owner decision (ask-first rule); framed in the coordinator report. Stays open until the claim is re-derived or restated.
- Superseded-premise check (owner 2026-11-21, against docs/coordination/owner-rulings.md on main 2ae54ab40; list: L± photon, virtual photons, pre-Nov-15 γγ letters, T(2,n_s), convention C, single-term trace, trefoil-primary electron, 'c_2 = −1 PROVED', χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean's premises or in the files it names.

## 2026-11-21 (honesty-audits sibling)

Statement restated to what the Lean proves (owner ruling 2026-11-21, PR #8888; record in docs/audits/2026-11-21-roundtrip-blind-audit-pass2.md §3). The `.md` no longer claims more than the `lean.ref` theorem. Left open on purpose: the original, stronger claim is still unproved, and the narrative-proof defects noted above are not yet fixed.
