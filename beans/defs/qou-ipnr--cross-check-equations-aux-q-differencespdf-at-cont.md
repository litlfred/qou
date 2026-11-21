---
# qou-ipnr
title: Cross-check Equations_aux_q-differences.pdf at folio/quantum-observable-universe/lean/QOU/QBeta…
status: completed
pr: 8380
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:31Z
updated_at: 2026-11-21T15:14:21Z
parent: qou-8hur
---

Re-run the attack plan's degree-budget table against the Sec. 4.4 example: compare the corpus's residual (deg c_n = n^2 against t_n = q^{C(n,2)}) with the 'order exactly two' q-Borel growth Rmk 4.12 computes, and record whether the C1 series is, up to gauge, of the multi-level type that example exhibits. This is a comparison to run, not a result to adopt.

Source: `library/equations-aux-q-differences/Equations_aux_q-differences.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/equations-aux-q-differences/  ->  [divizio-ramis-sauloy-zhang]
  Équations aux q-différences

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [divizio-ramis-sauloy-zhang] as the citation key when you do it.

## Progress (2026-11-18, PR #8380)
- [x] Non-vacuous Lean 4.24.0 theorems proved (`0` `sorry`, `0` `axiom`, `0` directory-mode audit advisories)
- [x] 80-dps `mpmath` probe and 2-commit witness stamped (`35b03645ad735c533bdb60a9a19a56165e5833fa`, `scriptHash: 197841ead85d03085a06e8bf1a078fa708f1da7e60c96d98a12ad24512b472a1`)
- [ ] Awaiting Merge Manager merge of `litlfred/qou#8380`

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8380, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21T15:14:21Z cross-check result

Probe: computations/probes/drsz_two_level_qborel_vs_c1_degree_budget_probe.py (commit 3e07cf2a70b, branch claude/expo-cite-xcheck-wave2-2026-11-21). Exact sympy plus mpmath 400 dps. ALL PASS with one amendment, thresholds unchanged. Cite key [divizio-ramis-sauloy-zhang].

- Thm 4.13: Delta = (x s - 1)(x^2 s - 1) and Delta Y = 1 + x hold exactly. The product rule for B_{q;1} holds (B(Y)_n = sum_k q^{-k(n-k)}).
- Source finding 1: (4.11.5) is short by a factor 2. P(q^m) = 2 (-1)^m q^{m(3m+1)/2}(q^-1;q^-1)_m (q^-1;q^-1)_inf for m = 0..5 at q = 2, to 1e-40. The factor comes from the k <-> n-k symmetry of B(Y). Page image (PDF p. 24) read: printed as transcribed.
- Source finding 2: Ex 4.11(2) drops the sign (-1)^n in the Taylor coefficients of prod(1 - q^-n xi) (Euler). Page image read. Harmless for the growth claim, which uses |a_n|.
- The order >= 3 growth claim holds: log2|p_n|/n^2 -> -1/6.
- Corpus comparison: C1's operator has ONE Newton slope at infinity (1/2); DRSZ's Delta has TWO at 0 (1, 2). Newton slopes are invariant under analytic gauge (DRSZ Sec 3), so the C1 series is NOT of the example's multi-level type, up to gauge. The two obstructions also differ in kind: Y's coefficients have level-1 growth deg_q = C(n,2), absorbed exactly by t_n, and its second level shows only as order-2 growth in the Borel plane; C1's coefficients have deg_q = n^2, which no unramified level absorbs (corpus result: ramify, then level 2; ramified_qBorel_budget). Consistent with the closure audit 2026-08-08-rsz-c1-infinity-route-closed.md ("C1 has one slope at infinity").
- Owner rulings: the attack plan carries the convention-C scope note (qou-h6o3); nothing here depends on the c_k ladder or Q_beta, so no superseded premise is used.
