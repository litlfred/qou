---
# qou-4m9u
title: Which seminormal family is correct? python off-diagonal vs rust (braid defect 0.7315)
status: todo
type: task
priority: high
created_at: 2026-08-31T03:29:28Z
updated_at: 2026-08-31T03:30:08Z
---

Blocks qou-sv7h step 2 and qou-i7ju. Evidence: PR #6337,
docs/audits/2026-08-31-ysn-matrices-are-not-a-representation.md.
Detector: computations/audits/ysn_braid_relation_audit.py (exit 1 today).

## The question

`hecke_core_legacy._build_ysn_matrices` and
`pyhecke_native.seminormal_matrices_mpfr` return DIFFERENT matrices for the same
partition and the same q. Only the Rust one satisfies the braid relation
(2.005e-50 vs 0.7315, on 7 of 7 partitions, dims 2..16). Which is intended, and
where exactly does the Python one go wrong?

## What is already narrowed

- **Not a precision problem.** 0.7315 is ~70% of matrix scale; float64 eps is
  2.2e-16.
- **Not the generator indexing.** Both index 0 -> sigma_1; python builds
  `for k in range(1, n)`, rust documents "sigma_1 .. sigma_{n-1}". dim matches
  the SYT count in both.
- **Not sigma_1.** Both give diag(q, -1/q) and agree to 3e-17 (float64 floor)
  on lambda=(4,2).
- **Not the eigenvalues.** At lambda=(2,1) BOTH sigma_2 have trace h and
  determinant -1, so both are individually valid Hecke generators.
- **It IS the off-diagonal.** py 0.9835938505 vs rust 0.8675840670, with
  diagonals (-0.1039637101, 0.3130240088) vs (-0.4036277384, 0.6126880371).
- The defect is CONSTANT at 0.7315 across partitions and dims -> one formula,
  not an accumulation.

## Where to look

`_build_ysn_matrices` around the axial-distance block:

    a_rho = h / q_int(rho)
    a_neg = h - a_rho
    bsq   = a_rho * a_neg + 1.0
    off   = math.sqrt(abs(bsq)) * (1.0 if bsq > 0 else -1.0)

Check `off` and the `rho` (axial distance) convention against Hoefsmit. Note
rust's diagonal entry 0.6126880371 is EXACTLY z_D = q^3/(q^2+1), the canonical
convention-D Markov parameter -- suggesting the two builds may differ by a
CONVENTION (C vs D) rather than by a bug, in which case the python one is a
convention-C artifact and is covered by the 2026-08-15 excision ruling. Test
that hypothesis before assuming an arithmetic slip.

## Do not skip

- Whichever family wins, `sdp_cross_channel.py` also consumes
  `_build_ysn_matrices`, so the SDP term of binding_energy is in scope and has
  NOT been assessed.
- Landing a fix RE-RUNS 33 files' worth of downstream numbers. Report what
  moved, per file, before merging.
