---
# qou-anx0
title: 'EPIC: Consolidate All 14 Monograph Appendices/Annexes & Build Dense Witness-Backed Master Reference Tables (Braid Words, Predictions, Propagated Calibration Bounds & CODATA/PDG/AME2020 Errors)'
status: in-progress
type: epic
priority: high
created_at: 2026-11-23T20:30:00Z
updated_at: 2026-11-24T01:19:56Z
parent: qou-hksc
blocked_by:
    - qou-qzvs
    - qou-udad
    - qou-h6ef
    - qou-5lct
---

## Goal (Gated Until Active Derivations Stabilize; Coordinates `qou-mba8`, `qou-lanx`, `qou-7p89`, `qou-t0fc`, `qou-4b6g`, `qou-nmjd`)

Audit and consolidate QOU's currently fragmented **14 back-matter appendices (`331` `.md` blocks)** — presenting concrete `AskUserQuestion` consolidation options first — into a tight, consistent, high-density Reference Back-Matter where prose sprawl is replaced by **automated, 80-dps witness-generated dense master tables** with uniform error-propagation framing across particles, couplings, Q-values, nuclei (`Z = 0..118`), and molecules.

## Current Back-Matter Fragmentation (`331` Blocks Across 14 Appendices)

1. `appendix-knot-operations` (`12` blocks, `K`) + `appendix-knot-operations-archimedean` (`3` blocks, `K'`) — split algebra vs. substrate evaluations.
2. `appendix-nf-witnesses` (`4` blocks — tiny stub!) + `appendix-knot-periodic-table` (`14` blocks, `T`) — split normal-form witnesses vs. periodic-table atlas (`qou-4b6g`, `qou-t0fc`, `qou-yd54`).
3. `appendix-qvalues` (`19` blocks) + `appendix-transfer-matrices` (`45` blocks, `M`) — overlapping transfer-matrix / Q-value derivations.
4. `appendix-mass-binding-algorithms` (`21` blocks, `MBA`) — tracked in **`qou-mba8`** (prune textbook prior art, keep QOU-unique delta only).
5. `appendix-formalisation-notes` (`25` blocks) — evolve & merge directly with **`qou-lanx`** (the Lean Subgraphs & 6 Reservoir Community Contrib Libraries Annex, avoiding a duplicate Lean appendix!).
6. `appendix-surreals` (`100` blocks) + `appendix-surreals-archimedean` (`21` blocks) — `121` blocks across two surreal appendices (`qou-e7ku`, `qou-g4x1`).
7. `appendix-standard-model` (`22` blocks, `SM` — coordinate with `qou-sm8w` & `qou-akee`).
8. `glossary` (`31` blocks, `G`) + `notation` (`13` blocks, `N`) + `index-of-definitions` (`1` block, `D`).

## Required Deliverables When Unblocked

1. **Step 1 — Audit & Present Structured Annex Consolidation Options (`AskUserQuestion` with Full 6-Part Frame):**
   - Propose collapsing the `14` appendices into `~6` crisp, non-overlapping Annexes, e.g.:
     * **Annex A — Master Braid, Mass, Coupling & Nuclear/Atomic Reference Atlas** (merging `knot-operations`, `knot-operations-archimedean`, `nf-witnesses`, `knot-periodic-table`, and tabular outputs of `qvalues`);
     * **Annex B — QOU-Specific Computational & Transfer-Matrix Algorithms** (merging pruned `mass-binding-algorithms` `qou-mba8` + essential non-standard transfer-matrix recurrences from `transfer-matrices` / `qvalues`);
     * **Annex C — Standard Model Parameter & Gauge Ledger** (`appendix-standard-model`, updated post-`qou-sm8w`);
     * **Annex D — Surreal & Non-Archimedean Substrate Lift** (consolidating `surreals` + `surreals-archimedean`, pruning vacuous kernels per `qou-g4x1`);
     * **Annex E — Lean 4 Formalization DAG & Reusable Community Libraries** (evolving `appendix-formalisation-notes` + `qou-lanx`);
     * **Annex F — Notation, Glossary & Definition Index** (`notation` + `glossary` + `index-of-definitions`).

2. **Step 2 — Uniform Dense Master Table Schema & Propagated Calibration Error Bounds (`workdps = 80`, Zero Hand-Maintained Numbers):**
   - Every quantitative master table (Elementary Particles & Couplings; Hadron/Eightfold Spectrum; Weak/Alpha/Beta Decay Q-Values & Lifetimes; Nuclide Binding & Mass Atlas `Z = 0..118`; Benchmark Molecules) MUST use a **single consistent column framing** backed by `.witness.json` liquid/template bindings:
     1. **Species / Observable** (symbol, $(Z, N)$ or $(I, J^P)$, Layer $\mathcal{L}_k$);
     2. **Canonical Braid / Motif Normal Form** (strands $n$, generator word $\beta$ / `HeckeGS` + `ChamberGS` normal form, active Schur/Wedderburn sector);
     3. **Symbolic Formula & Epistemic Tier** (closed-form $\mathbb{Q}(q_0)$ / Clausen / Jackson expression; *Proved / Derived / Conditional*);
     4. **Predicted Value $\pm \sigma_{\mathrm{pred}}$ (with Propagated Calibration Uncertainty!)**: exact 80-dps Jacobian propagation $\sigma_{\mathrm{pred}} = \sqrt{\sum_{a \in \{m_e, \mathcal{D}_\beta, m_\pi\}} (\partial O / \partial C_a)^2 \sigma_{C_a}^2 + \varepsilon_{\mathrm{trunc}}^2}$ from the experimental uncertainties of the three calibration observables $(m_e, \mathcal{D}_\beta, m_\pi)$ (respecting `qou-nmjd`: name the physical calibration observables $(m_e, \mathcal{D}_\beta, m_\pi)$ in prose/headers rather than internal `CAL-1/2/3` repo codes!), plus showing both proton-pinned and muon-pinned $q_0$ sensitivity where relevant;
     5. **Experimental Value $\pm \sigma_{\mathrm{exp}}$** (CODATA-2022 / PDG-2024 / AME2020 / NUBASE2020);
     6. **Residual & Pulls** ($\Delta = O_{\mathrm{pred}} - O_{\mathrm{exp}}$, relative ppm/ppb, $\Delta/\sigma_{\mathrm{exp}}$, and combined pull $\Delta/\sqrt{\sigma_{\mathrm{pred}}^2 + \sigma_{\mathrm{exp}}^2}$).

14-appendix inventory (332 blocks) & error-propagation options brief completed on origin/claude/annex-mba-consolidation-options-20261123 (196f34d7152).
