---
# qou-okh4
title: 'ROAST: the squeeze ''existing bricks'' claim is three cases with three bespoke brick sets, not a reusable library'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:01:39Z
updated_at: 2026-10-04T15:24:12Z
parent: b9cj
---


## The claim being roasted

> "Formalizable — sorry-free for 4₁, Borromean, and the 2-belt Whitehead chain,
> ~one session with the existing bricks."

Mine, said in session. Three things wrong with it.

### 1. "the existing bricks" implies a library. There isn't one.

- 4₁ needed E1 / E5a / E5c / E2 / E3 (`FigureEightVolumeSaddle`, `Clausen`).
- Borromean needed **B-bricks** B1–B5 (`BorromeanVolume.lean`).
- The 2-belt Whitehead chain needed **W-bricks** W1–W5 (`WhiteheadChainVolume.lean`).

Three cases, three bespoke brick sets with a family resemblance. What transfers
is the *architecture* — Riemann sum against the Clausen primitive, saddle, two
envelopes. What does **not** transfer is the code. Saying "with the existing
bricks" invites a reader to budget a session for wiring; the evidence says
budget it for writing a new brick set.

### 2. The "~one session" number is not mine and its author revised it.

I lifted it from `2026-07-27-squeeze-architecture-transfer-scan.md` §1, which
estimated "very likely one session of work with the existing bricks" for the
**Whitehead link** — written while the source was unavailable. When the source
arrived (2026-08-02) the outcome was a *route refinement*: the discharge landed
on the `b ≥ 2` **chain** `W_{a,2,1,0}`, not the link, because at odd `N` the
chain modulus is exactly a phase-free positive sum (vdV Lemma 1). So I quoted a
pre-source estimate for case X as if it were an achieved cost for case Y.

### 3. The strongest counterexample is the case nearest to one already done.

The `b = 1` **Whitehead link proper is still open in-repo** — with the source
in `library/`, with the Clausen/Catalan infrastructure in place, and with two
programmes attempted. It carries outer Fresnel phases (vdV Lemma 4,
Gaussian/erfc) and that is exactly the positivity the squeeze needs. So the one
transfer that had *everything* it needed still failed, on the structural
condition — not on effort.

## The honest restatement

The squeeze architecture is real and has three sorry-free discharges. Its
applicability condition is **a single positive sum at the Kashaev point**, and
that condition is doing all the work: satisfied ⇒ the proof is elementary and
formalizable; not satisfied ⇒ no amount of brick reuse helps. 5₂ and 8₁₁ are
named out of reach in the corpus's own scan for precisely this reason.

So: "architecture transfers, bricks mostly don't, and positivity decides." Cost
for a *new* positive-sum case is a brick set, not a wiring session.

## Why this matters beyond wording

An over-optimistic transfer estimate is how a programme gets committed to a
5–6 session infra build that a one-session preflight would have refuted — the
exact failure the qbeta KLR preflights were invented to prevent (cont. 16,
Composites 1 and 4 both refuted for ~10–13 sessions saved). The preflight
discipline should apply here too: **before budgeting any new squeeze
discharge, first establish that a positive sum exists at the Kashaev point.**
That is a cheap, decisive gate and it is the whole question.
