---
# qou-ctv8
title: Compare the R5-full SDP deuteron winner with the H_6 mass word beyond arity (both close to 3 components)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T21:21:48Z
updated_at: 2026-11-17T11:48:14Z
parent: qou-v2om
---

Opened from PR #5413 (reconciling the two deuteron adjudications of
2026-08-21). This is the positive result the reconciliation turned up and is
the cheapest live direction on the deuteron knot question.

THE OBSERVATION (measured, exact integer cycle counts, no floats):

  object                                     strands  components
  ------------------------------------------ -------  ----------
  R5-full SDP deuteron WINNER [1,2,2,2,2,2,2,-1]   3       3
  all 8 top_k_candidates                           3       3  (all)
  all 8 psd_feasible_subset.top_k                  3       3  (all)
  historical 6_2 [1,-2,1,1,1,-2]                   3       1   psd_feasible=false
  the H_6 mass word (23 letters)                   6       3
  3He SDP winner [1,1,1,1,1,1,2,2]                 3       3
  3He historical L6a4 [-1,2,-1,2,-1,2]             3       3   psd_feasible=true

Source: computations/r5-full-canonical-knot-solver.witness.json,
per_atom_results[*]. Reproduction:
computations/probes/deuteron_frame_arity_reconciliation.py.

WHY IT IS NOT VACUOUS. Over all 2^8 = 256 index sequences of length 8 in B_3
(signs are irrelevant to the component count), 86 give 3 components and 170
give 1 -- exactly 43/128 ~ 33.6%. So "all 8 top_k are 3-component" is a
feature of the SELECTED set, not of the word length. Stated as a base rate,
NOT a significance test: the top_k are ranked by a word-dependent cost and are
not independent draws. Do not upgrade this to a p-value.

WHY IT MATTERS. The corpus's only principled selector (the SDP) and the frame
the mass chain actually runs in (H_6) agree on arity, at a value a third of
the search space would have given by chance. 3He corroborates: the one atom
whose historical assignment is PSD-feasible is the one whose arity matches;
the deuteron's 6_2 fails both together.

THE TASK. Audit B (#5350/#5363) sec 5 item 3 proposed "search the 3-component
census". This is cheaper and comes first: the corpus ALREADY HAS two
3-component objects for the deuteron. Ask whether they are related by anything
beyond arity --
  * Markov trace / HOMFLY (the SDP records markov_trace = 1.4646421342766265
    for its winner; the mass word's tr_M is what the mass chain computes)
  * Wedderburn content: the two-row cap (conventionD_weight_eq_zero_iff) gives
    the deuteron {(6),(5,1),(4,2),(3,3)} at n = 3A = 6; the SDP works in B_3.
    The strand-count mismatch (3 vs 6) is the first thing to resolve -- audit
    B sec 3 Ground 2 already flags that the registry's own
    constituent_product_word is a 6-braid while the 6_2 word is a 3-braid.
  * whether the SDP winner's closure is a NAMED 3-component link.

CONSTRAINTS (STRICT, both inherited from B and from the owner ruling):
  * Do NOT rank candidates by |B_AME - rho * m_e * Vol(K)|. That is the
    forbidden inversion and it is exactly how 6_2 got here
    (mass_table_ppb.py:19-22 self-declares it;
     probes/knot_id_volume_match_adjudication.py is a LIVE probe still doing
     it -- see B sec 8.5).
  * Exact arithmetic. Component counts are integer cycle counts.

CAVEAT ON THE SDP ITSELF. Its own witness description says the search is
"issue #604, deliverable 1: numerical prototype" and that the categorical
uniqueness theorem needs "the multi-term mass formula (T2-T6) wired into the
cost function", which is not done. So the SDP winner is not yet a derived
answer either -- it is the best-motivated candidate, not a result. Do not wire
it to production on the strength of the arity match.

Related: qou-e5jf (adjudication, todo), qou-985x, qou-k8fc (the sigma_1^3
three-role collision), PR #5413.
