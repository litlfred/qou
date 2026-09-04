---
# qou-zovy
title: 'ROUTE F: drain the three-depth notation collision in the notation register'
status: todo
type: task
priority: normal
created_at: 2026-09-04T20:42:09Z
updated_at: 2026-09-04T20:43:04Z
---

ROUTE F of epic qou-2q85. Cheap hygiene, worth doing regardless of which route is chosen, and it is the direct countermeasure to an error class that produced SEVEN corrections in one session.

THREE FILTRATIONS ARE ALL INDEXED BY SOMETHING CALLED 'DEPTH':
  1. TRANSCENDENCE / iterated-integral depth n - G^(n) adjoins Li_n^q; tau_arch(G^(n)) subset P_n. Moved ADDITIVELY by the q-shuffle.
  2. KNOT / Hecke cell K - refined by the partition cell lambda_K |- n_K.
  3. GB / CURVATURE-RANK k = depth(lambda) - 1 - where depth(lambda) is PARTITION depth (max hook length per conj:two-filtration-bridge).

PROPOSED FIX: name them distinctly in notation/notation-register-table3-data.md and notation-collisions.md - transcendence depth n, cell lambda_K, curvature-rank k - and stop using the bare word 'depth' for (3).

AND RECORD THE HARD FACT ALONGSIDE IT: filtration (3) is currently attached to NO well-defined object. docs/audits/2026-08-16-three-gb-filtrations-one-name.md finds three inequivalent readings of J^bullet (rewrite count - not obviously well defined; image of the l-th power of the rewrite ideal - PROVABLY ZERO for every l >= 1; Coxeter-length span - fails the dimension count), and the 2026-08-26 supersession (qou-wjbd) excludes the third for every n >= 2 with no re-indexing repairing it. A reader who fixes only the NAMES will still think there is a filtration there.

SEE ALSO qou-hnri, which carries the same finding from the collision side. This bean is the ACTION; that one is the measurement.
