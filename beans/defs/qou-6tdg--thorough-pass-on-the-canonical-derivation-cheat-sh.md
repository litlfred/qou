---
# qou-6tdg
title: 'Thorough pass on the canonical derivation cheat sheet (audit + paper): reflect every 2026-09-15 decision; list gaps/conjectures; name the specific open mass-binding gaps'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-15T19:54:10Z
updated_at: 2026-11-15T23:50:00Z
parent: qou-avtq
---

Owner ask 2026-09-15 (queued for after the chi-as-term-of-ch tranche, session qou-dgce): re-read docs/canonical-derivation-cheat-sheet.md and every paper block it points at; make it reflect the 2026-09-15 decisions (chi split into chi_eu(M0) / chi(M0,V) / dim_q; Descartes condition as g(M0)=4; Wigner axiom for the Millennium blocks; HKR only for the commutative fibre; braided-at-QU / rigid-at-QOU; convention D; proton pin; z_D base). Identify every gap and conjecture on the chain and, for the mass-binding arc specifically, list the open gaps by name (extensive term / coefficient (qou-brng), Q_beta base above 1 (qou-cds1 scope note), element selection under reading 3 (qou-99qc), the deuteron intensive/extensive gap, c_k ladder on the z_D base) with the block, bean and probe that carries each. Also check notation collisions on the sheet (chi_lambda vs chi_eu vs chi_top vs chi(M0,V); tr vs tr_M vs dim_q) and offer options. Session: https://claude.ai/code/session_016Fn6V1VgQwJLVRWd6mUfos


2026-09-15 FIRST PASS DONE (branch claude/chi-arc-e3-followups-2026-09-15): docs/canonical-derivation-cheat-sheet.md §10 added — §10.1 every decision of 2026-09-15 with the artifact to check (A/B/C/D selections, tr(id_A) ruling, Bring-cone link finding, EFT classical-floor negative, Yekutieli hypotheses, running-example spine); §10.2 the open mass-binding gaps BY NAME with bean + status (qou-brng extensive term; qou-q8vl/kj4v/82mc b₃ sign; qou-99qc scored element; qou-cds1/pdix/iagg ladder on z_D; qou-cds2 Gram singularity; qou-oots/za3q Plancherel numerator; qou-ales word selection; qou-e5jf deuteron knot; qou-8p1g tetraplectic; conj:wigner-axiom; the derived-level realisation with no bean; qou-rydq). NOT yet done from the ask: re-reading every paper block the sheet points at for currency (§§1–9 carry older figures — e.g. §3 still writes z = 1/(q^{1/2}+q^{-1/2}), convention C, in the Z-step formula); that pass is the remaining half and is larger than an afternoon. Status stays todo.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** First pass landed (§10, and the §3 convention-C label at line 285). The re-read of §§1–9 against the cited blocks, and the chi_λ/chi_eu/tr/dim_q notation options, are still outstanding.

Evidence: `docs/canonical-derivation-cheat-sheet.md` §10 (line 1124ff), with §10.1 decisions and §10.2 named mass-binding gaps, is on main. A convention-C label was added at §3 line 285 (the `z = 1/(q^{1/2}+q^{-1/2})` line is now flagged C, not corrected). Per the bean's own note, the remaining half (re-reading every block §§1–9 points at for currency, plus the notation-collision options) is not done.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.


## 2026-11-15 — second half completed under owner ruling `Q-AVTQ-3 = 1` (PR #8063)

- Added `§0.1 Notation Disambiguation Table` to `docs/canonical-derivation-cheat-sheet.md` explicitly separating $\chi^\lambda$ (Hecke irreducible character), $\chi_{\mathrm{eu}}(M_0) = 2-2g(M_0) = -6$ (topological Euler characteristic of Bring's curve, $g(M_0)=4$), $\chi(M_0, \mathcal{V})$ (holomorphic sheaf Euler characteristic), $\operatorname{tr}$ (matrix trace), $\operatorname{tr}_M$ (normalized Markov trace at $z_D = q^3/(q^2+1)$), $\dim_q(X) = (\mathrm{ev}\circ\mathrm{ch})([X])$ (quantum rigid dimension), $\mathrm{NS}(A) = e(\xi) \in H^2(\mathcal{S}, \mathbb{Z})$ (global surface contact Euler class, PR #7982), $q_0$ (`Q_50_DIGIT_STR` 50-dps proton pin), and $\beta_{\mathrm{Bor}}$.
- Updated §§0, 1, 2, 3, 6, 9.5, and 10.1 in `docs/canonical-derivation-cheat-sheet.md` so Step 3 ($z_D = q^3/(q^2+1)$), Step 4 ($\chi_{\mathrm{eu}}(M_0) = -6$, $g(M_0)=4$, $\mathrm{NS}(A)=e(\xi)$), the $q_0$ proton-pin reference (`Q_50_DIGIT_STR`), and the Phase-5 Z-step formula inline text reflect canonical convention D and the 2026-09-15 / #7982 notation rulings. Held at `status: in-progress` pending PR #8063 merge and owner closure review.
