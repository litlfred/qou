---
# qou-s7ld
title: 'chi scaling wall: the Rust GP minimal-length reduction is the cost, not dim — a dim-free seminormal path-sum makes 5Li/6Li seconds'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-08T04:08:11Z
updated_at: 2026-11-16T19:46:00Z
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


---

## Round 47 Progress (`lane-e925`, 2026-11-16 — PR #8154)

- **PR:** [litlfred/qou#8154](https://github.com/litlfred/qou/pull/8154) (`ffb527fcd5e3aac0c7b00570fecb3e6dded50749`), signed `ready: ffb527fcd5e3aac0c7b00570fecb3e6dded50749` ([comment](https://github.com/litlfred/qou/pull/8154#issuecomment-6925680171)).
- **Resolved Open Question #1 (Are all producer words in the binding sweep level-local?):**
  - Audited all 32 `(intra_order, include_inter, isotope)` binding producer words emitted by `atom_braid_word_3A` across all 8 isotopes ($A = 1..6$) for both `intra_order="borromean"` and `intra_order="grouped"` and both `W_atom` (`include_inter=True`) and `W_free` (`include_inter=False`).
  - Every contiguous level-local segment has generator span $\le 2$ (at most 2 adjacent generators in a single 3-strand block, so local SYT orbit size $\le |S_3| = 6$), with exact segment counts $2A - 1$ (`borromean` $W_{\text{atom}}$), $A$ (`borromean` $W_{\text{free}}$), $3A - 1$ (`grouped` $W_{\text{atom}}$), and $2A$ (`grouped` $W_{\text{free}}$).
- **New sorry-free Lean 4 module `folio/quantum-observable-universe/lean/QOU/Hecke/LevelLocalPathSumSupport.lean`:**
  - Proves `atomWordLength_eq` ($6(2A - 1) + (A - 1) = 12A - 1$ for $A \ge 1$), `borromeanAtomSegments_eq` ($A + (A - 1) = 2A - 1$), `groupedAtomSegments_eq` ($2A + (A - 1) = 3A - 1$), `twChainSupport_values` ($6^A$ chain support at $A = 1..6$), and `twChainSupport_lt_fullSymGroupCard` ($6^5 = 7776 < 15! = 1{,}307{,}674{,}368{,}000$ and $6^6 = 46{,}656 < 18! = 6{,}402{,}373{,}705{,}728{,}000{,}000$).
