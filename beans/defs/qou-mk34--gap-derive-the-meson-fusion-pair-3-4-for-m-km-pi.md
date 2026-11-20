---
# qou-mk34
title: 'GAP: derive the pair (3,4) in m_K^2/m_pi^2 = [3]_q[4]_q from a definition of K and pi (currently scan-selected)'
status: todo
type: task
priority: normal
created_at: 2026-11-20T08:13:33Z
updated_at: 2026-11-20T08:13:33Z
parent: qou-3l2l
---

**Open, by six-path corpus-grep 2026-11-20** (audit docs/audits/2026-11-20-mk-mpi-derivation-status.md §2, PR #8529).

What is proved (QOU.BraidKnot.MesonFusionIndexSelection, sorry-free, generic CommRing):
- qCG_unnormalised_general: [m]_q[m+d]_q = sum_{k<m}[d+1+2k]_q for all m,d. The credited
  meson_qCG_3x4 is its m=3,d=1 instance (meson_qCG_3x4_is_family_instance), so the Lean credit on
  the strong core carries no selection information.
- scanPair_four_not_dictionary_index: 4 is not a quark torus-knot index (all odd) nor a meson
  total crossing (6,8,10) of the lepton-meson dictionary; kaon constituents are (3,5). Scope (b)
  for the index reading only.

Measured (computations/meson/mk_mpi_derivation_status_probe.py, 70 dps, proton q0): core alone
-101553.36 ppb (385.26x miss); in {[a][b]: a<=b<=12} (3,4) ranks 1/78 at 203.10 ppm, runner-up
(2,6) at 26742 ppm; local gap 7.61 %, chance-within-deviation ~0.53 %. Dictionary-indexed
readings miss by 27-89 %.

What would close it: a definition of K and pi as Hecke/Wedderburn objects (strands, partitions,
quark content s vs u/d) from which [3]_q[4]_q follows without reference to PDG. Choosing another
pair because it fits better is forbidden (selection against target). Until closed, the row
m_K/m_pi is not parameter-free regardless of the alpha_em sorry.
