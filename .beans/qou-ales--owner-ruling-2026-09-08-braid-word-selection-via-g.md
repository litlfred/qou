---
# qou-ales
title: 'OWNER RULING 2026-09-08: braid-word selection via gamma-gamma production + confinement SDP at q0 — no census'
status: in-progress
type: task
priority: high
created_at: 2026-09-08T07:40:02Z
updated_at: 2026-09-11T14:31:29Z
---

## Ruling (owner, 2026-09-08, chat, verbatim)

> *"All selection of great words should be done through gamma gamma production and the semi-definite product solutions at q_0. Shouldn't use census."*

Charitable reading (agent's, marked as reading): *braid* words. Every canonical braid word (nucleon, atom, meson) is to be SELECTED by the γγ (Breit–Wheeler pair-production) construction — words assembled from pair-production vertices, the σ₀σ₁⁻¹ = γγ̄ reading of gamma_gamma_pair_production_decomposition.py and breit-wheeler-pair-production-derivation.md — with the confinement SDP at q₀ (PSD Wedderburn projections; sdp_gamma_gamma_to_qqbar.py, nucleus_operator_selection_sdp.py, prop:confinement-sdp) picking the canonical T_w. Census volume-matching is excluded as a selection mechanism (re-affirms the 2026-09-05 'no knot-selection routes' ruling).

## What this bears on
- docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §2.2 items 1–3 (β_Bor, the quark→crossing template uu→σ / dd→σ⁻¹ / ud→averaged, the colour-weighted atom word) are exactly the CHOSEN joints this ruling says should be SELECTED by γγ+SDP.
- §3.1 knot-id 'admitted fit' (2026-08-25) and conj:canonical-knot-id-sdp: the SDP route is the one the owner names.
- qou-vbyi (diproton sign): every in-algebra sign direction is closed; the 'structural change' it needs is plausibly this — a pp word selected by γγ+SDP rather than assigned by the template.

## Corpus state (measured 2026-09-08)
- sdp_gamma_gamma_to_qqbar.py: STARTER SCAFFOLD (witness 2026-08-29): H₂ γγ→e⁺e⁻ demo only (σ₀³ tr_M ≈ 0.73 at q₀); H₃ skeleton; 'full SDP solve deferred'. 'NO Vol_hyp. NO census.' is already its stated discipline.
- nucleus_operator_selection_sdp.py: sweeps n_target = |tr_M(W_atom)| taken FROM the existing atom word — circular for selection; its LP is proved degenerate (operator-selection-lp.md: optimum ≡ 0, y₀* = 0, positive-dimensional minimiser face).
- qou-vd7j: the 0/3558 admissibility result is an OVER-DETERMINATION artifact (net row 1ᵀx = A inconsistent with the six Frobenius rows); cheap fix named (drop the redundant row / use the consistent net); heavy-A f64 overflow separate. 'Cheap next step' never done.
- breit-wheeler-pair-production-derivation.md: bare γγ = σ₀² gives E_pair 1.6 % short of 2m_e; 'colored photon' admixture with parameters φ₀, φ₁, φ₀₁ — those parameters must be DERIVED, not fitted to 2m_e (selection against the target is a fit).

## What closing means (formalize-first)
1. State in Lean what makes a word 'γγ-produced' (a product of pair-production vertices) and what the SDP selects (PSD Wedderburn projections at q₀) — before any search.
2. Fix the vd7j net-row over-determination; re-run admissibility; report per-nucleus which words survive, WITHOUT reading AME.
3. Only then compare the surviving word for p, n, ²H, pp, nn to the template words — the diproton sign is the first falsifiable output.
Default if nothing is done: words stay template-assigned; §2.2 stays 'chosen'.

Claimed 2026-09-08 by session on branch claude/ales-gg-word-selection-2026-09-08 (step 1+2 only).
