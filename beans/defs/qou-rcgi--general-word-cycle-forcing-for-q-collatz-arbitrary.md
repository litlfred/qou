---
# qou-rcgi
title: General-word cycle forcing for q-Collatz — arbitrary-parity-word denominator equation + front-loaded-odd exclusion family
status: completed
type: task
priority: normal
created_at: 2026-08-29T16:28:52Z
updated_at: 2026-09-08T07:45:43Z
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

LANDED 2026-08-29 on claude/q-collatz-gaps-conjectures-7bz3hg, PR #6042, commit 13d3d51bbb. File: content/quantum-observable-universe/lean/QOU/AppendixSurreals/collatz_general_word.lean.

Delivered (all sorry-free): word_collapse, qcollatz_word_forces (the arbitrary-word forcing equation), wordHol_map, wordNum_map_succ_odd/even, wordNum_map_nonneg, wordNum_map_lower, wordNum_map_upper, wordNum_const_of_front, qcollatz_no_front_loaded_cycle, and the non-vacuity witness front_loaded_beyond_adjacent_tail.

VERIFICATION (CI auto-triggers are off repo-wide, so this is the gate): lean-direct against the real Mathlib import cone, exit 0. #print axioms on qcollatz_word_forces / wordNum_map_lower / wordNum_map_upper / qcollatz_no_front_loaded_cycle / front_loaded_beyond_adjacent_tail returns only [propext, Classical.choice, Quot.sound] -- no sorryAx. Generic [CommRing R] throughout per 7c; no ordering, radical or Real.* construct.

WHAT IT DID NOT DO, recorded so nobody reads more into it. The upper bound is sharp and alone forces m <= 1, so the general word is NOT reached and is not claimed. Two follow-ons a later agent could take:
1. The bound is stated at a single cut D. A word with odd steps front-loaded in SEVERAL blocks (front-loaded within each of many windows) should admit a per-window version of the same induction; nothing here attempts it.
2. qcollatz_no_front_loaded_cycle takes the forced equation as a hypothesis, matching the landed style of qcollatz_no_adj_tail_cycle. Composing it with qcollatz_word_forces to give a single statement in terms of the orbit alone is mechanical and was left undone.

FOLLOW-ON LANDED 2026-08-29, commit below. The bean's own 'follow-on 1' (a per-window version of the bound) is superseded by something better: rather than generalising the bound window-by-window, the EXACT closed form now replaces bounding altogether.

wordNum_map_closed: phi(n_w) = sum_{i<k, w i} 3^(#odd after i) * 2^i, proved by induction (N-subtraction in the exponent handled via a new oddCount_mono, not avoided).

qcollatz_no_cycle_of_height_lt: exclusion with NO shape hypothesis -- for ANY word, positive height strictly below 2^k - 3^m excludes the cycle. Both hypotheses are finite integer computations for concrete w,k, so it is evaluable rather than merely stated.

The two earlier bounds are now visibly the extreme cases of this sum (odd steps earliest -> 3^m - 2^m; latest -> 3^m 2^(k-m) - 2^k). Previously asserted in the docstring; now derivable and numerically confirmed (4000 random words, 0 mismatches; extremes reproduce the bounds at (m,k)=(3,9),(4,11),(5,13)).

Bean 'follow-on 2' (composing the exclusion with qcollatz_word_forces into a single orbit-level statement) is still undone and still mechanical.

Scope unchanged: a criterion, not a proof it is met. For a general word the height can exceed 2^k - 3^m; deciding when it does not IS the open problem.

FOLLOW-ON LIST NOW EMPTY (commit d065c32f74). qcollatz_no_periodic_orbit_of_height_lt and qcollatz_no_front_loaded_periodic_orbit compose each exclusion with qcollatz_word_forces, so the hypotheses are a step relation, a return P k = P 0, and finite integer computations -- what a consumer actually holds -- rather than the intermediate forced cycle equation. One-line compositions, no new mathematics. lean-direct exit 0 first pass; axioms [propext, Classical.choice, Quot.sound], no sorryAx.

## 2026-09-08: twin qou-1lh4 (identical title, empty body, still marked in-progress) cross-referenced; this bean is the record. Audit docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 6 / §7.3 C7.
