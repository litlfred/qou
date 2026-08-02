---
# qou-ud3o
title: 'GAP: categorical Wick rotation — consolidate + Lean the i↦-i braiding-flip / Laplace-Fourier collapse'
status: todo
type: task
created_at: 2026-08-02T18:14:05Z
updated_at: 2026-08-02T18:14:05Z
parent: qou-ywj9
---

## Question (owner, 2026-08-02)

Where is Wick rotation in QOU, how do we use it, and can we define it
*categorically*?

## Corpus state (grep done — it is PARTIALLY there already)

- [`intro-q-resolvent-wick.md`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/content/quantum-observable-universe/quantum-observable-universes/intro-q-resolvent-wick.md):
  the categorical Wick rotation **collapses the Laplace and Fourier
  transforms into a single grouplike pairing** against
  $\exp_q \in G(\mathcal{H}_q)$ evaluated at $s$ (Laplace) or $i\xi$
  (Fourier). The $q$-resolvent $R_q(s)=(s+\widehat{\Delta_q})^{-1}$ is
  the categorical Laplace transform of the $q$-heat semigroup.
- [`i-as-braiding-orientation.md`](https://github.com/litlfred/qou/blob/claude/agent-task-662242-vag458/content/quantum-observable-universe/quantum-observable-universes/i-as-braiding-orientation.md):
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
