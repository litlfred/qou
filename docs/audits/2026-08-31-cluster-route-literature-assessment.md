# The "cumulant/connected-diagram route" is a TEMPLATE, not a plug-in theorem — a library assessment (qou-o6ov)

**Date:** 2026-08-31
**Directive (owner):** research.
**Scope:** scope-(a) literature assessment (corpus-grep path 5); no MeV, no compute.
**Follows:** #6354 — the `o(dim)` is a trace-orthogonality overlap decay
`⟨⁅ρ_λ,A_a⁆, A_{a+1}⟩_F / dim_λ → 0`, the sharpest form of the sign cancellation.

## Why this check

Six increments (#6311→#6354) reduced the tr-decay theorem to a **non-commutative,
operator-valued matrix-element overlap decay**, and every audit doc in the arc has named the
proof route "the cumulant / connected-diagram cancellation, tied to the ingested
Procacci–Yuhjtman / Rebenko papers." Before spending more effort, does the library actually
hold a theorem that *applies*?

## What is in the library (verified)

- **Procacci–Yuhjtman (2016) IS ingested** — it is `arxiv-1508.07379v2`, *"Convergence of
  Mayer and Virial expansions and the Penrose tree-graph identity."* (An earlier draft of this
  note claimed it was *not* in the library; that was wrong — the grep hits were the paper's own
  authorship. Corrected before recording.)
- **Rebenko (2022)** `arxiv-2205.07095v1` (virial expansions for correlation functions) and
  **Jansen–Kolesnikov (2022)** `s10955-022-02992-6` (cluster-expansion convergence conditions)
  are also ingested.

## What they actually provide (and the gap)

All three are **classical, commutative** statistical-mechanics results. The core tool — the
**Penrose tree-graph identity** (Procacci–Yuhjtman Thm 2) — rewrites
```
Σ_{g ∈ G_n} ∏_{{i,j}∈E_g} (e^{−βV(x_i−x_j)} − 1)
```
(a sum over connected graphs of products of **scalar pairwise** Mayer weights) as a sum over
spanning trees, to bound the **radius of convergence** of the Mayer/virial series. The existing
`references.ts` note on this entry already scopes it correctly: *"it is a RADIUS-of-convergence
result and says nothing about the sign of any particular cumulant."*

The QOU overlap `⟨⁅ρ_λ,A_a⁆, A_{a+1}⟩_F` is **not** of this form:

- **Non-commutative.** `ρ = ∏σ_{g_i}` and the germs `A_a` are matrices in a Hecke seminormal
  rep; the telescoping `⁅ρ,A_a⁆ = Σ_i σ_{<i}⁅σ_{g_i},A_a⁆σ_{>i}` is a sum of **operator**
  products, not a product of commuting scalar edge-weights. There is no "∏ over edges"
  structure for a partition scheme to act on.
- **A single fixed word, decay in the diagram shape `b`**, not a convergence radius in an
  activity variable.
- **The needed statement is about a cumulant/overlap SIGN vanishing** — exactly what the
  `references.ts` note says the Penrose result does *not* address.

**Conclusion.** The Penrose tree-graph identity is a **structural template** for the arc (the
telescoping resembles a connected-graph → tree expansion), but it is **not a plug-in theorem**
for the overlap decay. Applying it would require a *non-commutative / operator-valued* cluster
expansion with sign control — which none of the three ingested papers provides. The route is
genuinely new work, not a citation.

## A closer lead (not yet assessed for applicability)

`arxiv-math-0411505v2` — *"A non-commutative formula for the colored Jones function"* — is in
the library and is **non-commutative and in the Jones/Hecke setting** (sections: the Jones
polynomial, the quantum determinant / zeta function of a graph, the arc graph of a knot
projection). It is far closer to the QOU object than the classical cluster papers. Whether its
machinery bounds the germ-trace overlap is unassessed, but it is the right neighbourhood and is
the recommended first read for the next attempt.

## Honest outcome

- **Corrects the arc's framing.** "Tied to the ingested Procacci–Yuhjtman/Rebenko papers"
  overstated the connection: those papers are the classical **precedent/analogy**, and their
  central tool is a commutative convergence-radius identity silent on cumulant sign. The
  overlap-decay proof is not an application of them.
- **No ready-made theorem in the corpus** bounds the non-commutative overlap
  `⟨⁅ρ_λ,A_a⁆,A_{a+1}⟩_F/dim_λ → 0`. The nearest tool is the non-commutative colored-Jones
  formula (`arxiv-math-0411505`), unassessed.
- The tr-decay theorem stays **open**; this check saves the next attempt from expecting a
  plug-in and points it at the right (harder, non-commutative) neighbourhood.
