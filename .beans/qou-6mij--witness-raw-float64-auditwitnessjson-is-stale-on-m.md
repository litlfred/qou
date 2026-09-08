---
# qou-6mij
title: witness-raw-float64-audit.witness.json is stale on main by 8 drain commits — the drain arc's own scoreboard understates its progress
status: todo
type: bug
priority: normal
created_at: 2026-09-07T16:57:58Z
updated_at: 2026-09-07T16:58:26Z
---

MEASURED 2026-09-07 on origin/main d8cf8983c, incidentally, while re-running the ratchet after merging main into PR #7077. Not that PR's to fix — recording rather than widening it.

COMMITTED (computations/witness-raw-float64-audit.witness.json):
  dirty_witnesses 1009, total_fields 31226, baseline_files 1009, baseline_fields 31226
FRESH RUN (python3 computations/witness_raw_float64_audit.py --strict, exit 0):
  dirty_witnesses  996, total_fields 28152
  NEW dirty 0, REGRESSED 0, drained since baseline 12 files / +2838 fields

So the committed scoreboard UNDERSTATES the arc's own progress by 13 witnesses and ~3074 fields.

PROVENANCE, and this is the part that makes it a bug rather than normal derived-artifact lag: the file was last written at ee4367aea (merge of #7060). EIGHT drain commits have landed on main since, without regenerating it —
  d8cf8983c  clear the three raw-float64 regressions that landed on main today
  2bd43761d  stop narrowing the accumulator's log to float64
  ac4a08bb7  the channel sums themselves were f64
  000ddda97  channel_product_mass rounded residuals to 4 decimals
  fa7ec3da3  the six-term sweep, 331 raw floats -> 0
  d61c1ddce  restore atomic_chirality_residue
  f2b1cbae1  the k-star search computed in float64
  09895fc01  exact coefficients truncated below float64 into Rust

WHY IT MATTERS. The ratchet's contract is that baselines DRAIN and never grow, and this witness is where that is read off. A reader taking the committed file as current sees 1009 where the tree is at 996, i.e. the arc looks stalled while it is in fact working — the inverse of the usual staleness risk and easier to miss for exactly that reason. Also the drained list names files whose own commits are in the eight above (complex-volume-unification, qbeta-reeb-tower-jacobi-anger, atomic-chirality-residue, channel-product-mass), so the evidence that they drained is present in the repo and absent from the scoreboard.

NOT ESTABLISHED: whether the arc's owner regenerates this deliberately at arc close rather than per-commit, in which case this is a cadence choice and not a defect. Ask before sweeping. FIX IF WANTED: re-run the producer and commit, one chore(witness) commit; it is seconds of compute.

Owners of the touching arcs: qou-r47m, qou-kfeg, qou-sv7h.
