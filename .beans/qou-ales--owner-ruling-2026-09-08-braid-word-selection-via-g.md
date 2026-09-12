---
# qou-ales
title: 'OWNER RULING 2026-09-08: braid-word selection via gamma-gamma production + confinement SDP at q0 — no census'
status: in-progress
type: task
priority: high
created_at: 2026-09-08T07:40:02Z
updated_at: 2026-09-12T10:46:49Z
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


## 2026-09-08 — steps 1+2 landed on PR #7184 (branch claude/ales-gg-word-selection-2026-09-08)
Step 1: QOU/Mass/GammaGammaWordSelection.lean — GammaGammaWord (product of sigma_i sigma_{i+1}^-1 vertices) + SDPSelected (Matrix.PosSemidef on every Wedderburn block + cost-minimal); sorry-free, lean-direct exit 0, no sorryAx. Step 2: computations/probes/frobenius_admissibility_net_row_probe.py — vd7j net-row fix under D at the proton pin, no AME: 0/4238 candidate words survive for p,n,2H,pp,nn,3H,3He,4He, and the reason is the Gram radical (alternating character eps(W) != 0), NOT the net row (1'v != 0 makes it satisfiable). Scope-(a): the Gx=nf demand formulation; the PSD confinement SDP itself has NOT been run. Step 3 (H3 SDPSelected instance, template comparison, diproton sign qou-vbyi) remains OPEN — bean stays in-progress (rule 13a). Audit: docs/audits/2026-09-08-gamma-gamma-word-selection-step1.md.



## 2026-09-11 — step 3 CLAIMED on branch claude/ales-step3-h3-sdp-selector-2026-09-11 (stacks on PR #7184)
Instantiating SDPSelected at H_3 over the gamma-gamma candidate set (Lean sibling module), running the PSD/Frobenius-positivity selection over (sigma_0 sigma_1^-1)^k at the proton pin in a probe, and computing the pp binding sign with the selected bond vs the template. Bean stays in-progress.



## 2026-09-11 — step 3 landed on PR #7192 (branch claude/ales-step3-h3-sdp-selector-2026-09-11, stacks on #7184)
Lean QOU/Mass/GammaGammaSelectorH3.lean (26 theorems, no sorryAx): inside H_3 every gamma-gamma word is (sigma_0 sigma_1^-1)^k; PSD feasibility of a gamma-gamma word reduces to the (2,1) block; the single vertex is NOT Matrix.PosSemidef (off-diagonals q b vs -b/q, b^2 = [3]/[2]^2 > 0 derived); the literal SDPSelected selects the empty word under crossing-count cost. Probe gamma_gamma_h3_psd_selector_probe.py (proton pin, 60 dps, 8/8): literal reading -> identity only; form / Frobenius-positivity readings -> minimal NON-ZERO survivor k = 3 = beta_Bor (nucleon) and G^3 = (sigma_2 sigma_3^-1)^3 (pp bond); with G^3 the log-law diproton is UNBOUND, B_pp = -0.004469 MeV vs template +2.0710 MeV (scope-(a); recorded on qou-vbyi). OPEN, owner call: which reading of PSD the confinement SDP means on braid words (a word's image is never self-adjoint, so the literal reading admits no non-trivial word). Bean stays in-progress. Audit: docs/audits/2026-09-11-gamma-gamma-word-selection-step3.md.


## 2026-09-12 — step 3 MERGED (#7192 → main 6a593ed858, 6/6 replayed); steps 1+2 merged earlier (#7184 → 4605571fda). Bean stays in-progress.
What is on main: Lean QOU/Mass/GammaGammaWordSelection (step 1) and QOU/Mass/GammaGammaSelectorH3 (step 3), both sorry-free; probes frobenius_admissibility_net_row_probe (0/4238 under D, scope-(a)) and gamma_gamma_h3_psd_selector_probe (8/8; literal PSD selects only the identity, form/Frobenius readings select k = 3 = beta_Bor and the pp bond G^3, under which the diproton is unbound by 4.47 keV, scope-(a)); audit records 2026-09-08-…-step1.md and 2026-09-11-…-step3.md. The binding scale is named E_0^full at every point of use (sibling #7188 flagged the 0.99 % E_0 name collision with the Q_beta base E_0^(N=0); register-derived fix, bfb7585871).
Cross-support from #7188 (qbeta_option_e_construction_freedom_probe.py, scope-(a)): re-reading the existing nucleon recipe is exhausted — 37,459,422,000 ordering pairs over 6 multisets, 0 within ±780 ppb of Q_beta, nearest 187× outside — so a closing element must be derived from elsewhere, which is what gamma-gamma + SDP selection is. Level 1 is order-blind (monoidHom_order_blind), so the selector's result is a level-2 (z_D) statement.
STILL OPEN, owner call (asked in chat 2026-09-11, unanswered): which reading of PSD the confinement SDP means on a braid word — literal Matrix.PosSemidef (never met by a non-trivial word, w* = reverse(w)), symmetric-part PSD, or Frobenius positivity chi_lambda >= 0 on y_lambda > 0 blocks (constraint (1) of prop:confinement-sdp; my recommendation). Default while unanswered: words stay template-assigned; the records stand as scope-(a).
NEXT (step 4, branch claude/ales-step4-vertex-order-2026-09-12): the k >= 2 non-symmetry, formalize-first — (i) at q = 1 the vertex is the 3-cycle s_0 s_1 of S_3, so V^3 = 1 exactly there; the k = 3 survivor at q_0 is its q-deformation (within 0.11 of the identity), which is WHY B_pp is only 4.5 keV; (ii) for real 2x2 V with det V = 1 and |tr V| < 2, V^k symmetric ⇔ V^k = ±1, so the literal reading admits a non-trivial gamma-gamma word in H_3 iff some V^k = ±1, i.e. iff theta/pi is rational with cos theta = tr V / 2.


## 2026-09-12 — step 4 on PR #7207 (branch claude/ales-step4-vertex-order-2026-09-12): the k >= 2 non-symmetry closed by algebra; the vertex is the q-deformed 3-cycle
Lean QOU/Mass/GammaGammaVertexOrder.lean (31 theorems, no sorryAx): from the Hoefsmit relations alone det V = 1, tr V = -1 - h^2; Cayley-Hamilton gives V^k = alpha_k V + beta_k 1; on the reals V^k symmetric <=> alpha_k = 0 <=> V^k = +-1 (so the LITERAL PSD reading admits a non-trivial gamma-gamma word in H_3 iff some vertex power is scalar, i.e. iff theta/pi in Q with 2 cos theta = tr V). V^3 = (2h^2 + h^4) V + (1 + h^2) 1, so V^3 = 1 iff h = 0: the k = 3 survivor (beta_Bor, and the pp bond G^3) is the q-deformation of the 3-cycle s_0 s_1 of S_3, which is WHY |V^3 - 1|_F = 0.1126 at q_0 and why the selected pp bond moves the diproton by only 4.47 keV. The step-3 chi_(2,1) table is the Chebyshev recurrence in closed form (chi_3 = 2 - 3h^4 - h^6); its sign pattern (-,-,+,-,-) and alpha_k != 0 for k = 1..5 are proved for every 0 < h^2 <= 1/10, which covers 1 < q <= 23/20 and hence the proton pin (h^2 = 0.0437). Probe gamma_gamma_vertex_order_probe.py (8/8, 60 dps) matches the step-3 witness column to 2.6e-60. Audit: docs/audits/2026-09-12-gamma-gamma-word-selection-step4.md.
Still open: whether some V^k is ever scalar (theta/pi = 0.6747590908..., informational: closest approach |alpha_k| = 0.0355 at k = 40, no claim); the PSD-reading owner call (the literal reading now provably selects nothing non-trivial for k <= 5 at any q in the interval; the Frobenius reading selects k = 3 on the whole interval); the non-gamma-gamma letters. Bean stays in-progress.
