---
# qou-ud3o
title: 'GAP: categorical Wick rotation — consolidate + Lean the i↦-i braiding-flip / Laplace-Fourier collapse'
status: in-progress
type: task
priority: normal
tags:
    - 8f-ew
    - reorg-2026-10-04
created_at: 2026-08-02T18:14:05Z
updated_at: 2026-10-10T18:10:00Z
parent: qou-20sx
---

## Question (owner, 2026-08-02)

Where is Wick rotation in QOU, how do we use it, and can we define it
*categorically*?

## Corpus state (grep done — it is PARTIALLY there already)

- [`intro-q-resolvent-wick.md`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/folio/quantum-observable-universe/quantum-observable-universes/intro-q-resolvent-wick.md):
  the categorical Wick rotation **collapses the Laplace and Fourier
  transforms into a single grouplike pairing** against
  $\exp_q \in G(\mathcal{H}_q)$ evaluated at $s$ (Laplace) or $i\xi$
  (Fourier). The $q$-resolvent $R_q(s)=(s+\widehat{\Delta_q})^{-1}$ is
  the categorical Laplace transform of the $q$-heat semigroup.
- [`i-as-braiding-orientation.md`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/folio/quantum-observable-universe/quantum-observable-universes/i-as-braiding-orientation.md):
  **$i$ = braiding orientation** $c_{V,V}$ vs $c_{V,V}^{-1}$. Wick
  $t\mapsto it$ (Laplace half-plane → Fourier half-plane) flips under
  $i\mapsto -i$, i.e. it **is** the crossing-orientation flip
  $c_{V,V}\leftrightarrow c_{V,V}^{-1}$. Arrow of time = positive
  crossing = forward time in the Hecke basis ordering.
- `categorical-fourier-transform.lean` / `-unique.lean`,
  `reeb-u1-chart-swap.ts`, `reeb-u1-five-roles.*` are the Reeb/$U(1)$
  chart-swap machinery that hosts the rotation.

So the categorical definition already exists in prose. What is **not**
yet done is a single tight, Lean-proved statement.

## Attack options / status

1. **Consolidate** the scattered prose (`intro-q-resolvent-wick`,
   `i-as-braiding-orientation`, `categorical-fourier-transform`) into one
   `def:categorical-wick-rotation` block that states: the Wick rotation
   is the involution $i\mapsto -i$ on the braiding, equivalently the
   analytic continuation $s\mapsto i\xi$ that identifies the $q$-Laplace
   and $q$-Fourier grouplike pairings. **[near-term, mechanical]**
2. **Lean-prove the collapse**: the two pairings against $\exp_q$ agree
   under $s=i\xi$ (the "single grouplike pairing" claim). Likely a
   `categorical_fourier_transform`-adjacent lemma. **[medium]**
3. **Tie to the substrate→archimedean wall**: Wick rotation is exactly
   the map from the categorical/fibre level (formal $q$, $\mathrm{Im}\,q$
   free) to the archimedean level ($\mathrm{Im}\,q_0=0$). Document that
   the rotation is *where* the two-level convention (AGENTS.md
   "Im(q) at fibre vs observable level") is realised. **[medium]**
4. **Use it**: the Euclidean↔Lorentzian bridge needed by the
   lattice-QCD-emergence bean (partition function ↔ path integral) is
   this same rotation. Cross-ref that bean.

## Anti-guessing note
Do NOT re-declare "Wick rotation is open" — it is categorically defined
in prose. The open item is the *Lean* statement + consolidation, not the
concept.

## 🔥 Roast (2026-08-02) — verdict: PROBABLE, strongest of the batch

Adversarial check: is "collapse Laplace+Fourier into one grouplike pairing"
a *derivation* or a re-label? The load-bearing mathematical content of any
Wick rotation is that the analytic continuation $s\mapsto i\xi$ **exists and
is unique**. In QOU that reduces to a single checkable fact:

> **$\exp_q$ must be entire in its argument** (infinite radius of
> convergence). Then $s\mapsto e^{-s\widehat\Delta_q}$ (Euclidean/heat) and
> $\xi\mapsto e^{-i\xi\widehat\Delta_q}$ (Lorentzian/Schrödinger) are the
> SAME grouplike element evaluated on the real vs imaginary axis, and the
> continuation is automatic.

For the $q>1$ exponential, $[n]_q!$ grows super-geometrically ⇒ $\exp_q$ is
entire. At $q_0\approx1.11>1$ this holds. So the collapse is **not**
circular — it is a genuine consequence of entirety + the grouplike property.

- The "$i$ = braiding orientation" statement is a correct *interpretation*
  but is NOT the load-bearing lemma; do not oversell it as the derivation.
- **Concrete Lean target** (tractable, near-term): `exp_q_entire` (radius of
  convergence $=\infty$ for $q_0>1$) ⇒ `q_wick_continuation` (the two
  pairings agree under $s=i\xi$). This is the honest core of the bean.
- Downstream payoff: this same $R_q(s)=(s+\widehat\Delta_q)^{-1}$ resolvent
  is what the virtual-particle bean (`qou-apma`) needs for resonance widths,
  and the Euclidean↔Lorentzian bridge the lattice bean (`qou-jsx5`) needs.
  So closing this unblocks two siblings.

Verdict: **tractable, probable, high-leverage.** Prioritise over alpha_S.

## ✅ PROVED (2026-08-02) — the load-bearing lemma is now sorry-free Lean

`QOU.QExp.qExpTerm_summable` in
[`QExpEntire.lean`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/QExpEntire.lean):

> For `q > 1` (substrate regime, q₀≈1.11), the q-exponential series
> `∑ xⁿ / [n]_q!` is **Summable for every `x : ℂ`** — i.e. exp_q is entire.

Proof: balanced q-integer `[n+1]_q ≥ qⁿ` (drop the positive tail) ⇒
`[n]_q! > 0` and grows; ratio test `‖aₙ₊₁‖/‖aₙ‖ = ‖x‖/[n+1]_q → 0`
(`summable_of_ratio_norm_eventually_le`, r=1/2, since `qⁿ→∞`).
Axiom-clean: `[propext, Classical.choice, Quot.sound]` only; lean-direct
exit 0. Wired into `QOU.lean`.

This is the honest, falsifiable core of the Wick rotation: it makes the
single grouplike function defined on ALL of ℂ, so the continuation from
the real (Laplace) axis to the imaginary (Fourier) axis is legitimate.
The identity `F(ξ)=L(iξ)` itself remains definitional (do not dress it as
a theorem — that was the trap the existing `CategoricalFourier.fromLaplace`
fell into).

**Remaining (medium):** consolidate the scattered prose into one
`prop:q-exp-entire` content-block triple citing this lemma; optionally a
`Continuous (qExp q)` corollary. The analytic gate is closed.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-10-10 — reparented under qou-20sx

Owner decision 7b (ofri, 2026-10-10): the electroweak (`8f-ew`) beans are grouped under `qou-20sx`, the electroweak front's node, instead of directly under the epic `qou-8lxd`. Only the parent changed. Status, scope and body are untouched.

## Progress Note (2026-11-16)
- Formalized categorical Wick rotation involution (`wickInverse (wickForward p) = p`, `wickForward (wickInverse p) = p`) and `q`-factorial degree bound in `QOU/Eightfold/AtomicitySp2ElectroweakAndPartitionUnification.lean` (`categorical_wick_rotation_and_qexp_degree_certificate`) + 50-dps `exp_q(i*xi)` Laplace-Fourier continuation check in `atomicity_sp2_electroweak_and_partition_unification_probe.py` (PR `litlfred/qou#8172`, head `89a2a31a65a0d7dbf47567c813f9c48b755fae24`).
