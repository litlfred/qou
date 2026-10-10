---
# qou-iryu
title: 'CITE: no CR / contact / Sasakian source is held OR registered — U — 34 content files, 10 uncited blocks, ContactDistributionRank.lean:91'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:04:09Z
updated_at: 2026-10-04T15:14:45Z
parent: qou-mub3
---

**Class U — and this is the strongest absence on the arc: nothing is held AND
nothing is registered.**

**Measured 2026-09-04, both directions.**

*Library, all four tiers (`INDEX.md`, `summary.json`, `sections/`, `ocr/`):*
`Sasakian` **0/0**, `Sasaki-Einstein` and `Sasaki–Einstein` **0/0**,
`CR manifold` / `CR structure` / `CR-manifold` **0/0**, `7-manifold` /
`seven-manifold` **0/0**, `quaternionic contact` **0/0**, `quaternionic-Kähler` /
`hyperkähler` **0/0**, `G_2 holonomy` / `nearly Kähler` **0/0**, `S^7` **0/0**;
`pseudoconvex` 1, `exceptional holonomy` 1. `INDEX.md` returns **0** rows for any
of them. (Bare `sasaki` matches 5 section files — **all surnames in
bibliographies**. Grep `Sasakian`, not `Sasaki`.)

*`references.ts`, 828 entries:* **zero** CR-geometry, contact-geometry, Sasakian,
pseudohermitian, Webster-metric or Tanaka sources. No `blair`, `boyer`, `galicki`,
`dragomir`, `tomassini`, `geiges`, `tanaka`, `webster`, `fefferman`, `jerison`.
(`webster-williamson-2014-markov` is a Markov-chain paper, unrelated.)

**Against a corpus that uses the vocabulary in 34 `content/` files.** The blocks
that build the layer carry **no `cites` field at all**:
`models-of-qous/ale`, `models-of-qous/calabi-yau`, `models-of-qous/instanton`,
`models-of-qous/self-dual-curvature`, `quantum-observable-universes/levi-generalisation`,
`brings-surface/defect-legendrian-knot`, `brings-surface/brings-qou-4tuple`,
`quantum-observable-universes/c-quantum-universe`,
`quantum-observable-universes/archimedean-realisations`,
`brings-surface/brings-qou-axiom-map`.

**Where it bites hardest.**
`content/quantum-observable-universe/lean/QOU/Eightfold/ContactDistributionRank.lean:91`
defers explicitly — *"that is a cited fact about contact geometry, not something
[proved here]"* — and the file carries **zero `-- Ref:` lines**. That file is the
formal backbone of the CR-dimension decision
(`docs/audits/2026-09-04-the-cr-dimension-decision-full-context.md`), i.e. of a
live modelling decision with a 23-block / 90-consumer blast radius.

**Named works, cheapest first.** The fact actually being deferred to is
elementary — Darboux, `dim M = 2n+1`, `rank_ℝ H = 2n` for hypersurface type —
so the cheapest adequate source is not the big monograph:

1. **Blair, D. E., *Riemannian Geometry of Contact and Symplectic Manifolds*,
   Birkhäuser Progress in Mathematics 203, 2nd ed. 2010** — Ch. 3 covers contact
   structures, `dim = 2n+1`, the Reeb field and the almost-complex structure on
   the distribution. This alone closes `ContactDistributionRank.lean:91`.
2. **Dragomir, S. & Tomassini, G., *Differential Geometry and Analysis on CR
   Manifolds*, Birkhäuser Progress in Mathematics 246, 2006** — the
   pseudohermitian / Webster-metric / Levi-form package the corpus uses by name
   (`L_Θ = −i dΘ|_H`, signature `(r,s)`, strict pseudoconvexity).
3. **Boyer, C. P. & Galicki, K., *Sasakian Geometry*, Oxford Mathematical
   Monographs, OUP 2008** — needed only if the 5- or 7-dimensional Sasakian route
   (`docs/audits/2026-09-04-contact-distribution-complex-rank-and-dimension-seven.md`
   §2.4) is pursued.

**Two of the three are books, so "upload" may mean "register with ISBN/DOI and no
PDF"** — which is a legitimate outcome here and is what `fulton-harris1991` and
`ratcliffe` already do. The point is that *nothing at all* currently stands behind
the layer.

**Path 6 is empty too:** `Levi distribution`, `ker Θ`, `contact distribution`,
`Levi form`, `CR complex structure` all return **zero** bean files; `Boyer`,
`Galicki`, `Dragomir`, `Bryant` return 0. No agent has worked this.

Found by the citation-gap sweep, `docs/audits/2026-09-04-citation-gap-inventory.md`.
