---
# qou-q7lf
title: 'hadron_knot_table crashes: mpmath dtype=object reaches scipy.sparse (qou-5qwb class)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T08:10:16Z
updated_at: 2026-10-04T15:20:41Z
parent: qou-5vkl
---

Found while sampling the convention-C witness backlog (`qou-z11r`, PR #5510).
`computations/hadron_knot_table.py` does not run to completion on main.

## Two failures, in order

1. `ModuleNotFoundError: No module named 'scipy'` -- environment only. Per
   AGENTS.md ("if this container is simply missing a library, install it and
   re-run rather than committing the weaker record") I installed scipy 1.17.1
   rather than accepting it. That revealed the real one:

2. ```
   File ".../scipy/sparse/_sputils.py", line 56, in upcast
     raise TypeError(f'no supported conversion for types: {args!r}')
   TypeError: no supported conversion for types: (dtype('float64'), dtype('O'))
   ```
   via `hecke_core_legacy._build_ysn_matrices` -> `csr_matrix`.

## Why this is the qou-5qwb class, not a scipy problem

`dtype('O')` is numpy's object dtype, which is what an **mpmath value** becomes
when it lands in an ndarray. This is the same promotion that cost a 4000x
slowdown in `hoefsmit_numpy` (`qou-5qwb`) and that makes flipping
`q_parameter.Q` to `mpf` unsafe -- documented in #5453 §3. Here it does not
merely deoptimise; scipy.sparse refuses the mixed float64/object pair outright,
so the producer aborts and writes nothing.

So an `mpf` is reaching `_build_ysn_matrices` where a float is expected. The
fix is at that boundary -- carry the value as float into the sparse
constructor, or keep the YSN build entirely in mpmath and off scipy.sparse --
not by widening anything.

## Consequence for the C->D triage

`hadron-knot-table.witness.json` carries z_C and CANNOT be re-run to find out
whether that is stale output or a live C producer, so it stays unclassified in
`qou-z11r`. Any other producer in that 58 whose YSN path goes through
`hecke_core_legacy` is likely blocked the same way -- worth checking before
budgeting the sweep, since a "just re-run the producer" plan silently does not
apply to them.

Not fixed in #5510: out of that PR's scope (its subject is the q0 pin on
`atom_per_generator_volumes_mpfr` and the per-interface probe naming).

SECOND CRASH SITE, and it is not the one recorded above (measured 2026-08-23, scipy 1.17.1, clean origin/main worktree). This bean names hecke_core_legacy._build_ysn_matrices -> csr_matrix, i.e. sparse CONSTRUCTION. Here construction SUCCEEDS and the failure is one step later, in sparse MULTIPLICATION:

  hadron_knot_table.py:222 -> :179 compute_atom
  hecke_core_legacy.py:2270 binding_energy
  hecke_core_legacy.py:1435 unified_iterative_correction
      Msig = sig_sparse.T.dot(M_run.T).T    # = M_run @ sig_sparse
  scipy/sparse/_compressed.py:404 _matmul_multivector
  TypeError: no supported conversion for types: (dtype('float64'), dtype('O'))

So there are at least two independent scipy-sparse boundaries in this path, and fixing the constructor alone will not clear the producer. Whoever takes this should expect the same failure to recur at each sparse op until the whole hecke_core_legacy sparse branch is addressed.

WHY IT IS NOT A ONE-LINE FIX, unlike the two sibling crashes I did fix. vhat_per_crossing_chain's np.linalg.lstsq had an exact closed form hiding behind it (span{sigma,I} by the Hecke quadratic), so the numpy call was removable outright -- PR #5607. There is no equivalent here: the sparse path exists for an O(dim*nnz) vs O(dim^3) speedup across a whole mass table, and there is no scipy.sparse over mpf. The real options are (a) dense mpmath -- correct, possibly far slower, needs measuring before committing to it; (b) route to the canonical surface instead of hecke_core_legacy; (c) declare the producer exploratory-only and stop treating its crash as a defect.

CONTEXT FOR (b)/(c): computations/hecke_core_legacy.py carries a DEPRECATION-CANDIDATE banner ('Phase-5 exploratory surface, kept in place because 9 live importers still depend on its symbols'). Measured today: 10 importers under computations/ excluding _deprecated. So this is not a corner of the tree that can be quietly rewritten, and the choice among (a)/(b)/(c) is a scoping decision rather than a repair. Not picked unilaterally.

CROSS-REF: PR #5510's own body already flags the scoping consequence -- 'any producer whose YSN path goes through hecke_core_legacy is likely blocked the same way, and a just-re-run-the-producer plan silently does not apply to it.' The second crash site above strengthens that: it is not one boundary to patch, it is the sparse branch.

SUPERSEDED 2026-08-24 (note added by the qou-geqa census, not by this bean's owner). The SECOND CRASH SITE recorded above -- unified_iterative_correction doing sparse MULTIPLICATION and dying on (float64, object) -- is FIXED on main. Two commits landed 2026-08-24, after this bean's last update (2026-08-23T23:08):

  da645cf0f32  fix(hecke_core_legacy): the sparse crossing loop died on mpf coefficients
  46dcfc62a57  fix(qou-n7ue): hadron_knot_table no longer crashes -- two defects, and an honest cost

The live code computes `exact_chain` BEFORE the loop, routes an exact chain off scipy entirely, and accumulates over sigma's nonzeros in COO -- O(dim*nnz), the same complexity the float64 branch gets from sparse BLAS -- rather than coercing c/d to float, which its own comment refuses by citing AGENTS.md. So the option (a)/(b)/(c) scoping question this bean raises was answered by a fourth route: keep the sparsity, lose only the BLAS.

MEASURED on main 2026-08-24: the three A=1 atoms complete; deuterium, the first bound atom, then ran a FULL 50 MINUTES and was killed by its own timeout (exit 124), with ZERO tracebacks. It neither crashed nor finished. Keep those apart: "does not crash" is established by the CODE above (an exact chain provably never reaches a scipy call), and the run corroborates rather than proves it -- no finite run excludes a crash at minute 51. What the run establishes on its own is the COST: >50 min for one bound atom of nineteen. Do not expect the 19-atom table to finish.

Recorded because this bean cost a downstream agent a wrong retraction: reading it as current, I withdrew a correct claim that hadron_knot_table runs. A bean is a status note, and AGENTS.md's rule for status notes applies to it -- the corpus is the source of truth. The one-line check is `git log origin/main -- computations/hecke_core_legacy.py`.

The C->D triage consequence stated above may also need revisiting: hadron-knot-table.witness.json can now in principle be re-run, given a large enough budget, so it need not stay unclassified in qou-z11r on crash grounds.
