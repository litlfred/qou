---
# qou-5u4a
title: Cite 0006051v1.pdf at rem:q-dilog-three-contexts
status: todo
type: task
priority: normal
created_at: 2026-08-08T16:12:30Z
updated_at: 2026-08-21T17:04:43Z
---

rem:q-dilog-three-contexts currently states the F_p truncation and the Q_p/C_p convergence with zero citations; Besser Prop. 2.1 is the standard source for the q=1 finite/p-adic polylogarithm relation.

**From the source**
- Prop. 2.1 — For Li_n^{(p)}(z) := Li_n(z) - Li_n(z^p)/p^n one has Li_n^{(p)}(X) subset W, and Li_n^{(p)} reduces mod p to (1 - z^p)^{-1} li_n(z), where li_n(z) = sum_{k=1}^{p-1} z^k/k^n is the finite polylogarithm.
  Use here: Gives the q=1 literature backing for rem:q-dilog-three-contexts' unsourced claim that the (p-1)-truncated F_p dilogarithm and the C_p-convergent dilogarithm are two faces of one object; makes explicit that the correct bridge carries a (1 - z^p)^{-1} factor and a Frobenius-twisted argument, neither of which the block currently records.
- Cor. 2.2 — For a root of unity alpha in X, Li_n(alpha) lies in p^n W and p^{-n} Li_n(alpha) is congruent mod p to -li_n(sigma(alpha))/(1 - alpha).
  Use here: The p-adic valuation of polylogarithms at roots of unity — the direct p-adic analogue of the cyclotomic values Li_3(zeta_5^k) that conj:bring-trilog-depth-3-witness and prop:cl3-zeta5-orbit-sum-identity manipulate archimedeanly. Usable as a remark noting that the orbit-sum relations have a p-adic shadow with a computable valuation, not as an input to any current derivation.

Source: `library/arxiv-math-0006051v1/0006051v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0006051v1/  ->  [besser2000]
  Finite and p-adic polylogarithms

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [besser2000] as the citation key when you do it.
