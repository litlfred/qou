---
# qou-5zbn
title: Cross-check 0111022v1.pdf at prop:cl3-zeta5-orbit-sum-identity
status: completed
pr: 8335
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:34Z
updated_at: 2026-11-21T14:53:46Z
parent: qou-8hur
---

Test whether the orbit-sum / distribution identity used by prop:cl3-zeta5-orbit-sum-identity holds for QOU's Li_2^q = sum x^n/(n [n]_q), as Lemma 4 shows it does for Schlesinger's normalisation. This is a falsifiable numeric check, not an adoption of his result.

**From the source**
- Lemma 4 — q-deformed distribution relation: Li_2(x, q^n) = (1/n) sum_{y^n = x} Li_2(y, q), and similarly for Li_{1,1}.
  Use here: The q-analogue of exactly the classical distribution/multiplication identity sum_k Li_3(zeta_N^k) = (N^{1-3} - 1) zeta(3) that prop:cl3-zeta5-orbit-sum-identity and conj:bring-trilog-depth-3-witness rest on. Worth a compute-check: does the orbit-sum identity QOU uses survive in QOU's own q-normalisation, or only in Schlesinger's? A negative answer would be informative about the pre-/post-archimedean 'accident' classification in rem:transcendental-accounting.

Source: `library/arxiv-math-0111022v1/0111022v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0111022v1/  ->  [schlesinger2001]
  Some remarks on q-deformed multiple polylogarithms

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [schlesinger2001] as the citation key when you do it.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8335, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21T14:53:46Z cross-check result

Probe computations/probes/schlesinger_distribution_li2q_probe.py (head 856abed7f07). ALL PASS.
- The distribution relation survives in QOU's normalisation as sum_{y^n=x} Li_2^q(y) = Li_2^{q^n}(x)/[n]_q. It follows from [nm]_q = [n]_q [m]_{q^n} (checked exactly, n, m <= 6) and holds to 1e-58 at q0, 3/2, 2. Schlesinger's Lemma 4 in his normalisation holds to the same precision (control).
- It couples q to q^n, as Lemma 4 does. The same-q form fails by 5.3% at q0, n = 5.
- N = 5 orbit sum at q0: sum_{k=1}^{4} Li_2^q(zeta_5^k) = Li_2^{q^5}(1)/[5]_q - Li_2^q(1) (rel 7e-61). Its ratio to Li_2^q(1) is -0.83400, not the classical -4/5.
Premise finding: prop:cl3-zeta5-orbit-sum-identity is the classical q = 1 Li_3 identity. It contains no q, so neither normalisation enters it, and rem:transcendental-accounting is not affected.
