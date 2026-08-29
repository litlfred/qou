---
# qou-rcgi
title: General-word cycle forcing for q-Collatz — arbitrary-parity-word denominator equation + front-loaded-odd exclusion family
status: in-progress
type: task
priority: normal
created_at: 2026-08-29T16:28:52Z
updated_at: 2026-08-29T16:29:27Z
parent: qou-ifot
---

CORPUS-GREPPED 2026-08-29 (all six paths). Nothing in content/, computations/, docs/, library/, .beans/ or the Lean tree states a cycle-forcing equation for an ARBITRARY parity word. Every landed forcing lemma is either per-word (period-2: qcollatz_period2_{eveneven,oddodd,evenodd}; period-3: EEO, EOO; period-4: EEEO, EEOO, EOEO, EOOO) or adjacent-tail-only (collatz_one_odd_family: E^{k-1}O and the general E^{k-m}O^m). The only occurrence of 'n_w' in the whole Lean tree is a docstring line in collatz_one_odd_family.lean. library/INDEX.md has NO Collatz entry, so the Steiner / Simons-de Weger classical cycle-bound literature is not ingested either.

WHAT IS ALREADY LANDED (do not redo):
- no_cycle_of_q_one_height (collatz_one_odd_family.lean) -- the reusable engine. A cycle forcing D*P = n dies at any q=1 evaluation phi : R ->+* Z with phi(D) not dividing phi(n).
- qcollatz_no_adj_tail_cycle -- the entire adjacent-tail family E^{k-m}O^m excluded whenever 2*3^m < 2^k, via denominator height 2^k - 3^m against numerator height 3^m - 2^m.
- oddTailSum + oddTailSum_map (phi(S_m) = 3^m - 2^m), odd_chain_collapse, even_chain_collapse.

THE DERIVATION THIS BEAN FORMALIZES. Both branches divide by [2]_q, so a step is uniformly [2]*P_{i+1} = a_i*P_i + b_i with (a_i,b_i) = (1,0) even and ([3],1) odd. Iterating k steps:
  [2]^k * P_k = (prod_i a_i) * P_0 + sum_i b_i * (prod_{j>i} a_j) * [2]^i.
A period-k cycle (P_k = P_0) with odd-step set O, |O| = m, therefore forces
  ([2]^k - [3]^m) * P_0 = n_w,   n_w = sum_{i in O} [3]^{m_i} * [2]^i,  m_i = #{j in O : j > i}.
Writing O = {i_0 < ... < i_{m-1}} gives m_{i_t} = m-1-t, so the q=1 height is
  phi(n_w) = sum_{t<m} 3^{m-1-t} * 2^{i_t}.
Two bounds follow from i_t >= t and i_t <= k-m+t:
  3^m - 2^m  <=  phi(n_w)  <=  2^{k-m} * (3^m - 2^m).
The lower bound recovers the landed adjacent-tail numerator exactly (that family is the i_t = t extreme, which is why S_m has height 3^m - 2^m).

THE NEW EXCLUSION FAMILY. If every odd step occurs within d of the front (i_t <= t + d), then phi(n_w) <= 2^d * (3^m - 2^m), and the height engine excludes the word whenever
  2^d * (3^m - 2^m) < 2^k - 3^m.
d = 0 recovers the landed O^m E^{k-m} case; every d >= 1 is new. This is a genuine two-parameter infinite family strictly containing what is on main.

HONEST CEILING -- state it in the docstring, do not oversell. The crude UPPER bound i_t <= k-m+t gives only 3^m*(2^{k-m}+1) < 2^{k+1}, i.e. m <= 1, so it does NOT close the general word. It cannot: the general classical cycle problem is open, and this is its q-analog. The deliverable is scope-(a) -- an enlarged excluded family plus the general forcing equation as reusable infrastructure -- NOT a structural exclusion of all words. No fabricated invariant.
