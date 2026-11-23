---
# qou-mba8
title: Post-Stabilization Algorithms Annex Overhaul & Prior-Art Pruning (app:mass-binding-algorithms + Scattered Algorithm Blocks)
status: todo
type: task
priority: high
created_at: 2026-11-23T20:04:00Z
updated_at: 2026-11-23T20:55:42Z
parent: qou-hksc
blocked_by:
    - qou-qzvs
    - qou-udad
    - qou-h6ef
    - qou-5lct
---

## Goal (Gated Until Active Derivations Stabilize)

Once the in-flight derivation wave (`qou-qzvs`, `qou-udad`, `qou-h6ef`, `qou-5lct`, and `Q-Gap-1..6`) lands and stabilizes, audit `folio/quantum-observable-universe/appendix-mass-binding-algorithms/` (`19` `.md` blocks: `mba-intro`, `mba-chain-map`, `mba-step01..11`, and `5` `mba-sidecar-*` blocks) alongside scattered algorithm blocks in Chapter 12 (`nuclear-reduction-algorithm`, `universal-ilp-algorithm`, `groebner-reduction-methods`, `atomic-nf-witness-procedure`, `step-lp-verification`), Chapter 13 (`mass-identity`), and adjacent computational appendices (`appendix-nf-witnesses` [4 blocks], `appendix-transfer-matrices` [45 blocks], `appendix-knot-operations*` [15 blocks]), **present concrete consolidation/pruning options to the owner (`AskUserQuestion` with full 6-part framing)**, and rebuild a smaller, consistent, tightly structured Algorithms Annex containing **ONLY what is genuinely new, QOU-specific, or non-standard**.

## Core Diagnosis

1. **Re-deriving Standard Literature Algorithms as Boilerplate:**
   - `mba-step02-gs-reduction` re-states standard Hecke Gröbner-Shirshov word reduction (Bokut-Shiao 2001; Kang-Lee-Lee-Oh 2002 Prop. 4.3).
   - `mba-step03-markov-trace` re-states standard inductive Hecke/Temperley-Lieb Markov trace evaluation (Jones 1987; Geck-Lambropoulou 1997; Orellana 1999).
   - `mba-step05-wedderburn` re-states standard seminormal Young-Hoefsmit representation matrices (Hoefsmit 1974; Ram 1991) and symmetry-reduced block-diagonal SDP decomposition (Gatermann-Parrilo 2004).
   - `mba-step07-gb-filtration` re-states standard Buchberger / Conti-Gianni (1991) / Sturmfels-Thomas (1997) toric Gröbner reduction.
   - `mba-step10-confinement-sdp` re-states standard arbitrary-precision primal-dual interior-point solving (`clarabel-mpfr` Goulart-Chen 2024; SDPB Simmons-Duffin 2015) and standard complementary-slackness dual certification.
2. **Stale / Inconsistent Pipeline Ordering & Repo-Jargon Leaks:**
   - Flat `Step 01 .. Step 11` numbering plus an ad-hoc `sec:mba-sidecars` dump (`mba-sidecar-delta-lambda-closure`, `mba-sidecar-mirror-cancellation`, `mba-sidecar-isovector-chiral-residue`, `mba-sidecar-ck-truncation-ladder`) mixes core algorithms, historical sidecar workarounds, and open obstructions, and lags behind stabilized Nakayama-twisted Frobenius (`F3`), solver-free `(1^3)` radical shadow-price evaluation (`ECatLPDualRadical`), and the 5-Layer `ConfinementLayer` (`L_0..L_4`) recursion.
   - Duplicates overlapping algorithm prose in Chapter 12 (`universal-ilp-algorithm`, `groebner-reduction-methods`, `step-lp-verification`).

## Required Workflow When Unblocked

1. **Block-by-Block Classification Audit:**
   - Classify every block in `app:mass-binding-algorithms` + Ch. 12 algorithm blocks into:
     * **Prune / Compress to Citation + Convention Pin:** Standard textbook/prior-art machinery (cite Kang-Lee-Lee-Oh, Geck-Lambropoulou, Hoefsmit, Gatermann-Parrilo, Sturmfels-Thomas, Goulart-Chen/Simmons-Duffin, state QOU's exact parameter convention `h = q - q^{-1}`, `z_D = q^3/(q^2+1)`, `workdps = 80`, and drop redundant derivations).
     * **Retain & Standardize (QOU-Unique Delta Only):** Only the genuinely non-standard QOU constructions — e.g., Convention-D degenerate radical / solver-free `(1^3)` shadow-price extraction, Nakayama-twisted Frobenius pairing at `q != 1`, Bring-surface / Jackson `q^{-2}` integral evaluation at `q_0`, the 5-Layer `ConfinementLayer` (`L_0 -> L_4`) input/output contract, and exact rational/interval Lean `.witness.json` dual-slack verification.
     * **Relocate Obstructions:** Move non-algorithmic physics obstructions (`mba-sidecar-*`) out of the algorithms annex to their proper home chapters or retire superseded ones.
2. **Present Structured Options (`AskUserQuestion`) Before Editing:**
   - Present 3-4 concrete structural options (e.g., compact 5-page QOU-Delta Annex organized by `L_0..L_4` + Witness Verification vs. folding into Ch. 12/13 and retiring `app:mass-binding-algorithms` vs. unified Computational Specification Appendix merging `MBA` + `NF-witnesses`), with exact line/page savings, cross-reference blast radius, and uniform Input/Output/Complexity/Precision algorithm templates.
