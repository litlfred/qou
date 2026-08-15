---
# qou-gscs
title: Colour-weighting re-audit after 127 main commits
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T20:28:27Z
updated_at: 2026-08-15T20:37:33Z
---

Re-audit after 127 main commits.

GUARDS ALL HELD: sync --check in sync (42 modules); test_ctype_consumer_coverage PASS (Parts A, A2, B, C, D, E); qou-mass 20 passed; qou-substrate 46 passed; ctype_pair_expressiveness_probe exit 0; numpy_mpmath_dtype_leak_audit 0 candidates.

NEW FINDING 1 -- d_for_ctype broke its own contract. Its docstring says the caller's type 'carries through unchanged -- do not coerce it', and for sigma/sigma_inv/averaged it does. For averaged_weighted it returned an mpf REGARDLESS, because the cached delta is an mpf and mpmath wins the promotion. So the one ctype this entire arc is about was the one violating the contract. Not free: downstream numpy builds sigma + d*eye in a float64 array, one mpf promotes it to dtype=object, and per-matmul cost jumps -- measured on tritium where the first averaged_weighted crossing is at index 11 of 35. Three call sites carry float() workarounds for it and numpy_mpmath_dtype_leak_audit exists partly to police it. Fixed by downcasting ONLY for a plain-float caller; mpf and sympy paths verified untouched (mpf still 25+ digits, sympy still zero Float atoms).

NEW FINDING 2 -- see the spun-out bean: low-isotope-mass-table.witness.json is a third pre-convention-D artifact with 3 collapsed rows. Regeneration deliberately NOT committed from this sandbox (pyhecke_native absent would substitute the method on the p/n rows).

SWEEP COVERAGE: every *.witness.json in the tree, 16 rows carrying a braid word for a Z>=1,N>=1 atom; 3 collapsed, all in the one file.
