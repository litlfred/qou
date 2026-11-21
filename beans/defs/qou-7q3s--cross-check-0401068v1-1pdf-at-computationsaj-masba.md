---
# qou-7q3s
title: Cross-check 0401068v1 (1).pdf at computations/aj_masbaum_crosscheck.py
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:44Z
updated_at: 2026-11-21T14:50:33Z
pr: 8325
parent: qou-8hur
---

Cross-check the QOU 4_1 / trefoil colored-Jones towers against Takata's rearranged Masbaum normalisation (eqs. 1-5) as an independent second transcription; the script's docstring documents a prior mis-attribution in exactly this area.

**From the source**
- eqs. (1)-(2) and (3)-(5) — Masbaum's colored Jones formula for the twist knot K_p, J_{K_p}(n) = sum_k C_{K_p}(k) {n-k}...{n+k}/{n} with C_{K_p}(k) explicit, rearranged so that the summand F(n,k,l) has closed-form ratios f_0 = F(n+1,k,l)/F(n,k,l), f_1 = F(n,k+1,l)/F(n,k,l), f_2 = F(n,k,l+1)/F(n,k,l).
  Use here: An independently published transcription of the same twist-knot coefficients that computations/aj_masbaum_crosscheck.py checks the QOU 4_1 and trefoil towers against, in a different normalisation — so agreement is a genuine second witness against transcription error, which that script's docstring shows is a real failure mode here.
- eq. (16), §4 — Explicit evaluation hat-J_{K_p}(n) of the twist-knot colored Jones at q = exp(2 pi i / n), stated for the volume conjecture 2 pi lim (log|hat-J_K(n)|/n) = Vol(M_K).
  Use here: A directly runnable formula for the Kashaev/volume-conjecture asymptotic on 4_1 = K_{-1}, whose Vol(4_1) = ~~2 Lambda(pi/3)~~ 6 Lambda(pi/3) = 2 Cl_2(pi/3) ≈ 2.0299 [corrected 2026-11-21, finding F8] is the CAL-2 numerical anchor. A finite-n numeric cross-check of Vol(4_1) from this formula is a falsifiable compute-check; it must NOT be used to adopt or re-derive the anchor value.

Source: `library/arxiv-math-0401068v1/0401068v1 (1).pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0401068v1/  ->  [takata2004]
  THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [takata2004] as the citation key when you do it.

### Progress (Round 61)
- Formalized Lean 4 theorems, 80-dps mpmath probe, and 2-commit witness chain in PR #8325 (`5b31e8e9599f35d940975c6c2937ae31bf0eaa65`). Status kept `in-progress` pending PR merge.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8325, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — expo-cite-xcheck drain

Not run this wave. Bean text error: 'Vol(4_1) = 2 Lambda(pi/3)' should be 6Λ(π/3) = 2Cl2(π/3) ≈ 2.0299 (finding F8); use the corrected value when running. Superseded-premise check against docs/coordination/owner-rulings.md (2026-11-21): none beyond F8.

Evidence: branch `claude/expo-cite-xcheck-2026-11-21` (issue #8802); findings in docs/audits/2026-11-21-expo-cite-xcheck-findings.md.


## 2026-11-21T14:50:33Z cross-check result

Probe `computations/probes/takata2004_masbaum_twist_knot_probe.py` (branch claude/expo-cite-xcheck-wave2-2026-11-21), pre-registered, sympy exact plus mpmath 60 dps. ALL PASS after two documented amendments.

- The rearranged Masbaum formula of [takata2004] equals the corpus 4_1 Habiro tower (corpus_fig8 in computations/aj_masbaum_crosscheck.py) for n = 1..6 and the corpus trefoil Rosso-Jones tower for n = 1..5. So the corpus towers now agree with a second published transcription.
- K_2 matches Takata 2008 for 5_2 (n = 2, 3); K_-2 at n = 2 matches the 6_1 Jones polynomial.
- The Theorem 2.2 elimination contains the printed Hoste-Shanahan A_{K_p} for p = 1, -1, 2, and A_{K_-1} equals minus the corpus 4_1 A-polynomial.
- Eq. (16) at q = exp(2 pi i/N) equals the corpus 4_1 tower (N = 5..9, rel 1e-61). The 4_1 Kashaev asymptotic |J_N|/(N^{3/2} e^{N Vol/2pi}) extrapolates to 3^{-1/4} (rel 2e-10). SnapPy Vol(4_1) = 2 Cl_2(pi/3) to 1e-50. Vol was an input only; no anchor value adopted.
- FINDINGS (source): eq. (2) as printed carries an extra (-1)^{k+1} (it gives J(1) = -1); eq. (4) has (1 - q^k) where the ratio is (1 - q^{k+1}). Page images checked. Neither reaches Theorem 2.2, since both factors agree at q = 1.
