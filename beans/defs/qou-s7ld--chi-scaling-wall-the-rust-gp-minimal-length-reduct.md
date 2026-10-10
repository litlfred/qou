---
# qou-s7ld
title: 'chi scaling wall: the Rust GP minimal-length reduction is the cost, not dim — a dim-free seminormal path-sum makes 5Li/6Li seconds'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-08T04:08:11Z
updated_at: 2026-10-04T15:10:52Z
parent: qou-v2om
---

## Summary (2026-09-07/08, branch claude/chi-scaling-wall-symmetry-symbolic-2026-09-07)

Owner ask: "Investigate why slow — can we optimize / get rid of bottlenecks / use symmetry / use symbolic forms?"

**Bottleneck, measured.** `pyhecke_native.chi_q_via_gp` = T_w expansion → `reduce_basis_to_minimal_length_complete` → q-MN. The expansion support of the atom word is exactly 6^A (36/216/1296/7776/46656 at n=6..18), so it is NOT the cost; at n=12, λ=[12]: expansion+Hoefsmit-per-T_w 62 ms, direct seminormal <1 ms, chi_q_via_gp 7385 ms → >99 % is the minimal-length reduction (Hecke conjugation leaves the 6^A chain and spreads toward n!, BFS cyclic-shift completion, O(|support|) rescan per step).

**Symmetry that removes it.** The borromean atom word touches every seminormal level in exactly one contiguous factor, so χ^λ(T_β) = Σ_{T∈SYT(λ)} Π_j ⟨T|F_j|T⟩ — a transfer-matrix contraction over shapes, dim-free. Implemented in `computations/chi_path_sum_seminormal.py` (mpmath 70 dps, proton pin). Cross-checks: all λ of n=6/9 vs Rust `chi_lambdas_braid_mpfr` ≤1.2e-49 (sign-only and mixed σ/σ⁻¹/averaged words); ⁴He cache 4.7e-50.

**Timings (all partitions):** D 17 ms, T 131 ms, ⁴He 0.66 s, ⁵Li 2.5 s (176 λ), ⁶Li 8.5 s (385 λ). Rust route: 5.6 s per single λ at n=12; ⁵Li did not finish 40/176 λ in 3 h 35 m (qou-d9wf).

**Second finding.** D/T/³He/⁵Li/⁶Li matrix-m caches on main were on the pre-2026-09-05 GROUPED word (match it at 1e-49…1e-41; borromean off by O(1)); only ⁴He was borromean. Grouped word = single-generator segments ⇒ GP reduction has nothing to do — which is why the Aug caches took 69 s and why the "20 ms/λ dim-independent" docstring was believed. All five regenerated on the borromean word (D/T/³He in a separate revertible commit).

Audit: docs/audits/2026-09-07-chi-scaling-wall-level-local-path-sum.md. Not established: complexity class of the reduction; whether the four deltalambda/ consumers' conclusions move; whether the binding producer (qou-sv7h) words are level-local.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
