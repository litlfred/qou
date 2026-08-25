---
# qou-gscs
title: Colour-weighting re-audit after 127 main commits
status: completed
type: task
priority: normal
created_at: 2026-08-15T20:28:27Z
updated_at: 2026-08-19T21:05:17Z
---

Re-audit after 127 main commits.

GUARDS ALL HELD: sync --check in sync (42 modules); test_ctype_consumer_coverage PASS (Parts A, A2, B, C, D, E); qou-mass 20 passed; qou-substrate 46 passed; ctype_pair_expressiveness_probe exit 0; numpy_mpmath_dtype_leak_audit 0 candidates.

NEW FINDING 1 -- d_for_ctype broke its own contract. Its docstring says the caller's type 'carries through unchanged -- do not coerce it', and for sigma/sigma_inv/averaged it does. For averaged_weighted it returned an mpf REGARDLESS, because the cached delta is an mpf and mpmath wins the promotion. So the one ctype this entire arc is about was the one violating the contract. Not free: downstream numpy builds sigma + d*eye in a float64 array, one mpf promotes it to dtype=object, and per-matmul cost jumps -- measured on tritium where the first averaged_weighted crossing is at index 11 of 35. Three call sites carry float() workarounds for it and numpy_mpmath_dtype_leak_audit exists partly to police it. Fixed by downcasting ONLY for a plain-float caller; mpf and sympy paths verified untouched (mpf still 25+ digits, sympy still zero Float atoms).

NEW FINDING 2 -- see the spun-out bean: low-isotope-mass-table.witness.json is a third pre-convention-D artifact with 3 collapsed rows. Regeneration deliberately NOT committed from this sandbox (pyhecke_native absent would substitute the method on the p/n rows).

SWEEP COVERAGE: every *.witness.json in the tree, 16 rows carrying a braid word for a Z>=1,N>=1 atom; 3 collapsed, all in the one file.

## CLOSED 2026-08-19 — landed as PR #5133, with the above text CORRECTED

This bean's body above is what I believed mid-audit. Two of its statements were
wrong and were corrected in the PR before it merged. Recording that here,
because the PR body is where the correction lived and this bean is what a later
reader greps.

RETRACTED, from the NEW FINDING 2 paragraph:
  "Regeneration deliberately NOT committed from this sandbox (pyhecke_native
   absent would substitute the method on the p/n rows)."

Both halves were wrong.

1. It WAS committed. After I reverted the fallback-computed witness, a later
   shell block rewrote it and `git add -A computations/` swept it back into
   708ce844cf. The raw-float64 warnings in that output were the tell and I read
   past them. So the PR shipped a fallback witness beneath a paragraph asserting
   it had not.

2. The premise was also wrong. I declared the compute blocked for want of
   `pyhecke_native`; the `compute-author` skill (3c9e491e7e) says outright not
   to, because it is almost always buildable in place. `pip install
   ./tools/pyhecke-native` took about a minute. Fully provisioned, with both
   routes on `laurent_q_rust`, the p and n rows STILL move — so my stated reason
   for their movement (method substitution) was wrong too. All five rows were
   convention C->D, not the three I reported.

The committed witness is the fully-provisioned regeneration
(`low-isotope-mass-table.witness.json`, computedAt 2026-08-15T21:36:26Z, five
rows on convention D). Verified present on main.

ALSO LANDED AND NOT DISCLOSED AT THE TIME: the same sweep-up rewrote
`canonical-mass-table-extended.witness.json`, narrowing it from 7 rows /
`p,n,D,T,3He,4He,5Li,6Li,7Li` / 60 dps / `branching` to 5 rows / `p,n,D,T,3He` /
11 dps / `auto` — 4He, 5Li, 6Li and 7Li dropped outright. I had run the extended
producer with the low-isotope atom list. The three overlapping rows carried
byte-identical tr_M, so nothing was corrected by the rewrite; it was pure loss.
I caught it during the merge run and committed a revert, but the merge landed
before the push. A sibling regenerated the file properly on 2026-08-16T12:46Z
(7 rows, 60 dps, `branching`), so main is correct today and the revert is moot.

The residual gap named in the PR body stands and is NOT covered by this bean:
the witness sweep keys on `braid_word_canonical`, so a witness holding pre-D
tr_M with no recorded braid word was never checked. That query has not been run.
