# Triage: five cluster/virial-expansion uploads vs the Δ_λ extensive-term gate

**Date:** 2026-08-30
**Scope:** relevance triage only (a paper-relevance judgement, not an open-item
declaration). Note (post-rebase): main independently migrated these same five to `library/arxiv-*`; the ising arXiv-vs-journal dup was kept by main as `library/ising`. Originally: migrated `uploads/ → library/<doc-id>/` via
`scripts/migrate-uploads-to-library.py --apply`; `ising.pdf` (a journal-version
duplicate of `arxiv-1610.05082v3`, same title/authors/abstract, different file) dropped
on owner instruction.

> **Caveat (measured).** The migration moves the **PDF** into
> `library/<doc-id>/` but does **not** run the folio-assistant sectioner
> (`pdf-structure.py` / `extract-candidates.py`; the `paper-assistant` MCP server
> failed to connect this session). So these five are discoverable by doc-id but
> their `sections/*.md` — corpus-grep path 5 — are **not yet built**. Full-text
> grep on them is a follow-up requiring the folio-assistant pipeline.

## The five (all migrated)

| doc-id | paper | one-line content |
|---|---|---|
| `arxiv-1508.07379v2` | Procacci & Yuhjtman, *Convergence of Mayer and Virial expansions and the Penrose tree-graph identity* (math-ph, 2016) | the **Penrose tree-graph identity** — reorganises the Mayer expansion over connected graphs into a sum over trees, giving convergence bounds on the connected (Ursell) coefficients |
| `s10955-022-02992-6` | *Cluster Expansions: Necessary and Sufficient Convergence Conditions* (J. Stat. Phys. 189, 2022) | **sharp** (necessary AND sufficient) convergence criteria for abstract cluster expansions |
| `arxiv-2205.07095v1` | Rebenko, *Virial Expansions for Correlation Functions in Canonical Ensemble* (math-ph, 2022) | virial expansions for correlation functions in the **canonical** (fixed-N) ensemble |
| `022201-1-online` | Mann & Helmuth, *Efficient algorithms for approximating quantum partition functions* (J. Math. Phys. 62, 2021) | polymer-model / cluster-expansion **algorithms** for approximating quantum partition functions |
| `arxiv-1610.05082v3` | Dousse & Féray, *Weighted dependency graphs and the Ising model* | weighted dependency graphs → CLT for dependent variables, worked on the Ising model |

## Why they bear on the gate

The open Δ_λ gate is **not the per-partition value** (proved 2026-08-02:
`Δ_λ = (−1)^{n(λ)}·dim V_λ`) but the **many-body binding MAGNITUDE** — a
*separate, super-pairwise, additive, extensive* term the six failed closure
ansätze could not supply (the pairwise cap `ρ_A ≤ C(A,2)` is proved; the missing
object is extensive, ∝ A, not intensive). Binding energy is a log-partition-
function (a free energy); its extensive part is precisely the **connected
(Ursell/cluster) sum**. That is exactly the technology these five formalise.

This is a **live line already**, not a new direction — the corpus is already
attacking the extensive term with cluster/Ursell/Mayer/cumulant machinery:

- `computations/deltalambda/ursell_slot_alignment_probe.py` (+ witness)
- `computations/deltalambda/perknot_pn_bond_mayer_grounding_probe.py` (+ witness)
- `computations/deltalambda/cumulant-mev-cluster-expansion.witness.json`
- `computations/deltalambda/helium4_mu4_cluster_moment_probe.py` (+ witness)
- `computations/deltalambda/borromean_3body_cluster_sign_probe.py`
- `computations/deltalambda/ka_additive_cluster_derivation_probe.py`
- `computations/alpha/alpha_cluster_recursion.py`

and **Féray is already in `references.ts`** (`feray2010`, `feray-meliot2012`,
`dolega-feray2014`), so the dependency-graph/CLT thread (paper 5) is a direct
extension of work the paper already cites.

Per-paper hand-off to the live line:

1. **Procacci–Yuhjtman (Penrose tree-graph).** The tool to *bound and resum* the
   connected coefficients that `ursell_slot_alignment` and
   `perknot_pn_bond_mayer_grounding` compute term-by-term. If the extensive term
   is a connected-cluster sum, this is how you show it converges and is
   controlled — the missing rigour under the existing Ursell probes.
2. **Cluster-expansion convergence conditions (J. Stat. Phys.).** Sharp criteria
   for whether the `cumulant-mev-cluster-expansion` series is even well-defined
   in the relevant regime. A convergence *certificate* the current probes lack.
3. **Rebenko (canonical virial).** A nucleus has **fixed A** — the *canonical*
   ensemble, not grand-canonical. This gives correlation-function expansions in
   exactly that setting, the correct ensemble for `helium4_mu4_cluster_moment`.
4. **Mann–Helmuth (quantum partition-function algorithms).** Polymer-model
   algorithms for the log-Z that binding-as-free-energy needs; an algorithmic
   route for the extensive part.
5. **Dousse–Féray (weighted dependency graphs / Ising).** Extends the already-
   cited Féray CLT/dependency-graph thread; ties to the colour-weighted **q-CLT**
   used for the A→∞ mass-table extrapolation.

## Honest limits (what this triage does NOT claim)

- **Not a closure.** These supply *convergence technology and the correct
  ensemble*, not a derived extensive term. Wiring a cluster expansion to the
  categorical Δ_λ is the open work, and the **anti-fit discipline is untouched**:
  an extensive term obtained by fitting the cluster coefficients to AME2020 is a
  fit, must be labelled one, and may not be wired as canonical (AGENTS.md
  "no seventh fit-based ansatz"; Subgoal-2 "open for all" grants permission to
  *derive*, not to launder a fit).
- **Not an open-item declaration.** This is a relevance judgement under the
  Critical-distance license, not a corpus-status claim; the six-path checklist
  was run to *connect* to the live line, above, not to declare anything open.
- **Sectioning pending.** Until the folio-assistant sectioner runs, these five
  are not on corpus-grep path 5, so a future "is X in the corpus?" check will
  miss their text. Named here so that gap is visible.

## Suggested next step (a decision for the author, not taken here)

The highest-leverage single item: apply the **Penrose tree-graph identity**
(paper 1) to the existing `ursell_slot_alignment` connected sum, to test whether
the extensive term admits a *convergent* connected-cluster representation at fixed
A (paper 3's canonical setting). That is a derivation attempt, in scope under
Subgoal-2, and bounded — it either produces a convergent representation or a
documented negative. It is **not** started here; this file only triages.
