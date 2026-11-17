---
# qou-5rou
title: Cross-check Ohtsuki-99.pdf at computations/probes/keystone_colored_sigma235_wrt.py
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T00:10:45Z
updated_at: 2026-11-17T10:54:12Z
pr: 8315
parent: qou-8hur
---

Expand the corpus's Sigma(2,3,5) series in h = q-1 and compare lambda_1 against ±6 and lambda_2 against 39, after fixing the orientation convention against Lin-Wang's right-handed-trefoil normalisation; apply the lambda_2 in 3Z sieve as a precondition. This validates the transcription that the whole colored-WRT keystone step rests on. The external values are comparison targets, never inputs to be wired.

**From the source**
- Section 5, Example (1), p. 304 — If M is the Poincare homology 3-sphere Sigma(2,3,5), realised as +1-surgery on the right-handed trefoil, then lambda_2(M) = 39. (Companion: Sigma(2,3,7) from +1-surgery on the left-handed trefoil has lambda_2 = 63.)
  Use here: A parameter-free external number for the second Ohtsuki coefficient of S^3/2I. Expanding the corpus's Sigma(2,3,5) false theta in h = q-1 must reproduce it (together with lambda_1 = 6 lambda_Casson = ±6, the trefoil having a_2 = 1). This is the falsifiable check the keystone transcription lacks. Caveat that must be settled before the comparison means anything: Lin-Wang's orientation is +1-surgery on the RIGHT-handed trefoil, and their own Remark on the same page gives lambda_2(Mbar) = lambda_2(M) + lambda_1(M) under orientation reversal — so the corpus's orientation convention has to be fixed first, or the check will fail for a bookkeeping reason rather than a mathematical one.
- Theorem 1.1 (p. 293) and Corollary 5.1 (p. 303), strengthened at Theorem 7.1 — lambda_2(M) is an integer divisible by 3 for every integral homology 3-sphere M; lambda_1(M) is in 6Z (lambda_1 = 6 times the Casson invariant, Murakami).
  Use here: An integrality sieve on any lambda_n the corpus extracts from its own Sigma(2,3,5) series: a transcription that yields a non-integer, or an integer not divisible by 3 at n=2, is wrong independently of any numerical tolerance. Cheap, exact, and it fails loudly — the right kind of gate for a transcription check. Consistent with the quoted value (39 = 3 x 13).

Source: `library/lin-wang-1999-on-ohtsukis-invariants-of-integral-homology-3/lin-wang-1999-on-ohtsukis-invariants-of-integral-homology-3-spheres.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/lin-wang-1999-on-ohtsukis-invariants-of-integral-homology-3/  ->  [lin-wang1999]
  On Ohtsuki's invariants of integral homology 3-spheres

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [lin-wang1999] as the citation key when you do it.

### Progress (Round 60)
- Formalized Lean 4 theorems, 80-dps mpmath probe, and 2-commit witness chain in PR #8315 (`bfd875bed8570b98aa208b007cb51288416e1d03`). Status kept `in-progress` pending PR merge.
