---
# qou-apma
title: 'REFINE: virtual particles = transient/unstable vertex flows (Reeb flow + Demazure + width)'
status: todo
pr: 8209
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-lean
    - 8f-open
created_at: 2026-08-02T18:14:05Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

## Framing (owner, 2026-08-02)

"Virtual particles = transient / unstable vertex flows."

## Corpus state (grep done — already framed, this REFINES it)

QOU already localises virtual particles geometrically:

- [`virtual-particles-exceptional-divisor`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/folio/quantum-observable-universe/observations/virtual-particles-exceptional-divisor.md):
  a virtual particle operates in the Reeb bundle over the exceptional
  divisor $\mathcal{S}_p\cong\mathbb{P}^1$ (the **vertex** — cf.
  `prop:vertex-is-exceptional-divisor`), propagates through the recursive
  brane tower $A_0\hookrightarrow A_1\hookrightarrow\cdots$, and is
  reabsorbed before reaching base level $A_0$. Tower level $A_n$ =
  $n$-virtual depth; $\pi_0:A_n\to A_0$ annihilates $\Omega^1$ (off-shell
  = projects no shadow). Lifetime from the level-$n$ Heisenberg
  commutator $\hbar_{q_n}=1-q_n^{-1}$.
- [`vacuum-polarization-virtual-pairs`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/folio/quantum-observable-universe/observations/vacuum-polarization-virtual-pairs.md).
- AGENTS.md §7b item 3: **unstable intermediaries (W/Z, resonances,
  virtual particles) are Demazure sub-crystals** — incomplete
  topological states; their non-symmetric Macdonald evaluation under the
  Observation Frame ($\tau$/Markov trace) reproduces the broken symmetry
  of a short-lived state "without ad-hoc decay machinery."

## The refinement to make explicit: "transient vertex FLOW"

Existing prose gives the *stage* (exceptional divisor = vertex) and the
*lifetime* (Heisenberg bound). What "vertex flow" adds and what to
formalise:

1. **Flow = the Reeb flow on $S^3$ over $\mathcal{S}_p$.** A virtual
   particle is not a state but a *trajectory* of the Reeb/$U(1)$ flow that
   opens at the blow-up locus and closes (reabsorbs) before hitting $A_0$.
   State this: virtual particle $=$ a non-closed Reeb orbit segment on the
   vertex divisor; on-shell $=$ closed orbit.
2. **Transience = Demazure (non-complete crystal).** Tie the "reabsorbed
   before $A_0$" projection to the Demazure sub-crystal characterisation:
   a transient vertex flow is a Demazure operator applied but not
   completed to a full crystal.
3. **Unstable = complex Markov-trace pole (nonzero imaginary part / width).**
   The width $\Gamma$ (decay rate) should be the imaginary part of the
   Markov-trace pole at the fibre level (AGENTS.md: Im(q) free at fibre) —
   the resonance width. Cross-ref the c_k "fibre vs observable Im(q)"
   convention.

## Attack options / status

1. **Consolidate + relabel** existing blocks under one
   `def:virtual-particle-vertex-flow` (or a `remark` interpreting
   `prop:vertex-is-exceptional-divisor`) making the flow/Demazure/width
   triple explicit. **[near-term]**
2. **Lean**: state "off-shell = $\varepsilon(\omega)=0$ ⇒ $\pi_0=0$" (the
   non-observability projection) — likely already close to provable.
   **[medium]**
3. **Width from fibre pole**: connect resonance width to Im of the
   Markov-trace pole (this is the W/Z / hadronic-resonance mass sector —
   cross-ref the SM-26 m_W/m_Z beans). **[long]**

## Anti-guessing note
Do NOT declare "virtual particles are open" — they are framed
(exceptional divisor + brane tower + Heisenberg lifetime). Open item is
the *flow / Demazure / width* consolidation + Lean, not the concept.

## 🔥 Roast (2026-08-02) — one claim CORRECTED, two hold

**CORRECTION — "width = Im of the fibre pole (Im q)" is WRONG / self-
inconsistent.** AGENTS.md pins $\mathrm{Im}(q_0)=0$ at the observable/
archimedean level (`lusztig_q_0_imaginary_part_zero`). But resonance widths
$\Gamma$ ARE observable (measured decay rates). If width $=\mathrm{Im}(q)$
and $\mathrm{Im}(q_0)=0$, the width would vanish — contradiction. So the
"fibre-pole Im(q)" framing must be dropped.

**The correct framing (better, and it unifies with the Wick bean):** a
resonance is a **complex pole of the $q$-resolvent $R_q(s)=(s+\widehat
\Delta_q)^{-1}$ in the *energy/$s$-plane*** — real $q_0$, complex $s$. The
width is $\mathrm{Im}(s_{\text{pole}})$, not $\mathrm{Im}(q)$. This is
non-negotiable-consistent with $\mathrm{Im}(q_0)=0$.

**Why Demazure supplies exactly this:** a *complete* crystal ⇒ $\widehat
\Delta_q$ self-adjoint w.r.t. the Markov-trace inner product ⇒ real spectrum
⇒ stable (real $s$ pole, zero width). A *Demazure sub-crystal* (incomplete)
⇒ the truncated $\widehat\Delta_q$ is **non-self-adjoint / non-normal** ⇒
complex spectrum ⇒ complex $s$-pole ⇒ nonzero width. So:

> transient ⇔ Demazure (incomplete crystal) ⇔ non-self-adjoint $\Delta_q$
> ⇔ complex energy-plane pole of $R_q(s)$ ⇔ finite lifetime $\Gamma=\mathrm{Im}(s)$.

This is a clean, falsifiable chain and it reuses the **same $R_q(s)$** as the
Wick bean (`qou-ud3o`) — so the two beans share machinery.

**Two claims that HOLD:**
1. off-shell $=$ ($\varepsilon(\omega)=0 \Rightarrow \pi_0=0$): explicit
   projection formula already in the corpus; tractable Lean. ✓
2. flow $=$ non-closed Reeb orbit segment on the vertex divisor: consistent
   with `prop:vertex-is-exceptional-divisor`. ✓

Revised attack-3: width from **energy-plane** resolvent pole of the
non-self-adjoint Demazure-truncated $\Delta_q$ — NOT from Im(q). This is the
W/Z / hadronic-resonance sector (cross-ref SM-26 m_W/m_Z beans).

## ✅ PROVED (2026-08-02) — off-shell non-observability, sorry-free

[`VirtualProjection.lean`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/VirtualProjection.lean)
(`QOU.Virtual`), generic domain `K`, module `A`:

- `pi0 e f = (∏ i, e i) • f` — base-level projection of a level-n excitation
  dressed by forms with counits `e i` (the `π_0` of `virtual-particles-
  exceptional-divisor`).
- `pi0_offshell` — off-shell (`∃ i, e i = 0`) ⇒ `π_0 = 0` (no shadow).
- `pi0_eq_zero_iff` — the **biconditional** (non-vacuous): over a domain with
  no zero smul-divisors, `π_0 = 0 ↔ (∃ i, e i = 0) ∨ f = 0`. I.e. the
  excitation is observable (`π_0 ≠ 0`) **iff** `f ≠ 0` and every form has a
  nonzero constant part (on-shell). This is the exact off-shell/on-shell
  dichotomy, not just "product with a zero factor is zero."

Axiom-clean (`propext, Classical.choice, Quot.sound`); no sorry/trivial-True;
wired into `QOU.lean`; lean-direct exit 0. Closes the "clean provable half"
of this bean.

**Still open (from the roast):** the *width* of an unstable excitation as
`Im(s_pole)` of the resolvent `R_q(s)` from a non-self-adjoint Demazure-
truncated `Δ_q` — that needs non-normal spectral theory and stays open here.


## Triaged 2026-10-10 — tagged `8f-open`; NOT a scaffolding task

Read as part of finishing the `8f-lean` front's triage. Verified on the live
post-rename tree and re-classified: the mechanical half of this bean is **done**,
and what remains is research, so it should not be picked up expecting a repair.

**Done and verified.** `folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/VirtualProjection.lean`
(2739 B) carries `pi0` (line 40), `pi0_offshell` (45) and the non-vacuous
biconditional `pi0_eq_zero_iff` (56, under `[IsDomain K] [NoZeroSMulDivisors K A]`).
That is attack option 2 of this bean, closed.

**Open, and it is the hard kind.** The width as `Im(s_pole)` of `R_q(s)` from a
non-self-adjoint Demazure-truncated `Δ_q` needs non-normal spectral theory —
nothing in Mathlib, and the corpus has no carrier. Shares `R_q(s)` with
`qou-ud3o` (Wick), so the two should be attacked together or not at all.

**Option 1 (consolidate + relabel) is NOT done and is the cheap residual.**
Measured: there is no `def:virtual-particle-vertex-flow` block, and
`virtual-particles-exceptional-divisor.md` is the only `virtual-particle*` block
in the tree. So the flow / Demazure / width triple is still implicit. That is a
content change under the ask-first rule, and it should wait for the width half
anyway — relabelling around a mechanism that is not yet derived would fix the
vocabulary to a guess.

**Stale links, recorded not fixed.** This bean's GitHub URLs all point at
`blob/claude/agent-task-662242-vag458/content/...` — a dead branch *and* the
pre-rename `content/` path (main renamed `content/` -> `folio/`). Live paths are
given above. Not swept, because every bean written before the rename has the
same defect and a blanket rewrite is its own tranche.

**The correction already in this bean's roast is the most reusable thing in it**
and is repeated here so a skimmer does not re-derive it: **width is NOT
`Im(q)`.** `Im(q₀) = 0` at the observable level while resonance widths are
measured, so that framing is self-inconsistent. The width is `Im(s_pole)` in the
energy plane at real `q₀`.

## Progress (2026-11-16, PR #8209)
- [x] Non-vacuous Lean 4 theorem proved (`0` `sorry`, `0` vacuity advisories) in `folio/quantum-observable-universe/lean/QOU/Eightfold/RankOneSpinSingletThreeGenerationsLadderChargeAndNearlyKahlerCosets.lean`
- [x] 50-dps `mpmath` probe and witness stamped (`9c4fe9d8065c7167caac7a61ef4becd45df1573f`, `scriptHash: e6bdb7c63ac7`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8209`

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8209, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
