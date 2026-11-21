---
# qou-scxq
title: Remark interpreting 0111022v1.pdf at rem:q-dilog-three-contexts
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T16:12:35Z
updated_at: 2026-10-04T15:23:25Z
parent: qou-vva9
---

Record that algebra-closure and shuffle-preservation of q-polylogarithms are normalisation-dependent, and that rem:q-dilog-three-contexts' 'hopf-algebra' tag is currently unbacked for QOU's own normalisation.

**From the source**
- Lemma 2 + Cor. 3 — The rational span of the q-deformed multiple polylogarithms Li_{n_1..n_m}(z_1..z_m;q) is an associative Q-algebra, and the classical symmetry (shuffle) relation Li_1(x,q)Li_1(y,q) = Li_{1,1}(x,y,q) + Li_{1,1}(y,x,q) + Li_2(xy,q) survives the deformation.
  Use here: Gives the precise test QOU's own Li_2^q must pass for the 'hopf-algebra' tag on rem:q-dilog-three-contexts to be earned, and a worked example of a deformation for which it does pass. Consumable as a remark stating that algebra-closure is deformation-dependent and is not automatic for QOU's normalisation.

Source: `library/arxiv-math-0111022v1/0111022v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-math-0111022v1/  ->  [schlesinger2001]
  Some remarks on q-deformed multiple polylogarithms

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [schlesinger2001] as the citation key when you do it.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

rem:q-dilog-three-contexts: paragraph on the hopf-algebra tag citing schlesinger2001 §2 Lemma 2, Cor. 3, recording that the normalisation there (sum z^k/(1-q^k)^2) differs from Li_2^q = sum x^n/(n[n]_q).

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.
