---
# qou-5wi6
title: 'F1 research: general-n q-involution identity S(n)=Σdim_q via Stanley q-hook-maj + RSK'
status: in-progress
type: task
priority: normal
created_at: 2026-07-19T01:52:06Z
updated_at: 2026-09-07T08:02:13Z
---

## 2026-09-07 — claimed; the general-n route is the one this bean names, and it is now partly walked

This bean was todo with an EMPTY body, titled 'F1 research: general-n q-involution identity
S(n)=Sum dim_q via Stanley q-hook-maj + RSK'. That is exactly the route walked in PRs #7003/#7010/
#7014 (bean qou-hok7), so recording the state here rather than opening a new bean.

DONE on that route:
- The path decomposition w(T) = [n(l')-n(l)] + 2 maj(T) and the Stanley q-hook-maj collapse are
  CORPUS PRIOR WORK, not new: lever1_descent_transfer_operator.py:18-24 and its verification
  target V2 at :45 (exact to n<=16). Cite those.
- What IS new: deg Z_n = n^2 - H_min(n) with H_min(n) = 2n-1 + sum_{k>=2,T_k<=n-1}(n-T_k), which
  DERIVES the corpus's measured d2 deg = 2 - [n triangular] and explains the triangular exceptions
  (staircase minimises total hook length; H_min(T_k) = k(k+1)(2k+1)/6).
- REV = Omega(sqrt n) proved; REV = O(n^{3/4}) proved via H >= r^2-r+1.

STILL OPEN, and it is this bean's actual subject: the identity for GENERAL n. The .md proposition
is general-n but its Lean sibling proves only n=3,4,5 by decide, and the narrative proof cites
Stanley EC2 + sagan2001, BOTH REGISTERED AND NOT INGESTED. So general-n currently rests on
uningested literature, not on Lean. My closed form is verified computationally to n<=11 only.

Two cheap adjacent gaps found by the same grep: Littlewood's identity is named as a classical
anchor of this exact object in lever1-kernel-maj-involution-identification.witness.json:33 and is
never stated anywhere; and library/arxiv-2105.09342v1 (Dutta et al., q-deformed Plancherel growth,
hook lengths as free-fermion momenta) plus arxiv-1909.06797v5 are INGESTED BUT UNREGISTERED in
references.ts, so no block can cite them today.
