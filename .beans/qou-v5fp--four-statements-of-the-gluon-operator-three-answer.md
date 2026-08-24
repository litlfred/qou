---
# qou-v5fp
title: Four statements of the gluon operator, three answers - min-cr vs min-|tr_M| disagree
status: todo
type: task
created_at: 2026-08-24T20:59:37Z
updated_at: 2026-08-24T20:59:37Z
---

Found while closing qou-1ngr, 2026-08-24. Separate from qou-jqjx (trace convention); this one is about the objective, not the weights.

The same quantity — which operator step 4 of def:derived-atom selects as the proton's gluon — is stated four times and comes out three ways:

  def:universal-ilp-algorithm, prose instantiation table : sigma_0 sigma_0, 2 crossings
  computations/universal-ilp.witness.json (its OWN witness): sigma_1,        1 crossing
  rem:categorical-proton-properties + the exists/unique proofs: L_- = sigma_1 sigma_0, 2 crossings
  computations/_deprecated/integer-lp-gluon.witness.json    : sigma_0 -> sigma_0, 2 crossings

Two distinct problems underneath.

1. The stated objective is not the objective used. `def:universal-ilp-algorithm` states min cr(K) first, |tr_M(x.K)| as tiebreak WITHIN a crossing shell. The deprecated producer sorts by |tr_M| alone with no crossing preference. They disagree, and the disagreement is exactly on the load-bearing number. Cheapest survivor per crossing shell, retired convention (scratch re-run):

     proton : cr=1 sigma_0 |tr_M|=0.1597 ; cr=2 sigma_0->sigma_0 0.0274 ; cr=3 0.1654 ; cr=4 0.0921
     neutron: cr=2 L_+     |tr_M|=0.3873 ; cr=3 L_+->sigma_1   0.1441 ; cr=4 L_+->L_- 0.1120

   Under min-cr-first the proton takes 1 gluon crossing and the neutron 2 — not 2 and 4. The 2-versus-4 asymmetry, which is what makes the neutron heavier and feeds Q_beta = m_n - m_p - m_e (CAL-2), exists only under pure min-|tr_M|.

2. `computations/universal-ilp.witness.json` is self-certifying. Its assertions compare each computed operator against an `expected` value baked into `universal-ilp.py`, so allPassed=true and status "verified" say nothing about the corpus. It records confinement as sigma_1 at 1 crossing against B_3's 6, and the gluon as sigma_1 at 1 crossing against the blocks' 2 — i.e. the live witness for def:universal-ilp-algorithm does not reproduce a single crossing count the definition's own prose table asserts.

Task: pick one objective, state it once, re-witness the gluon selection against it, and reconcile the four statements. Until then rem:gluon-stabiliser-ledger records the discrepancy in prose rather than resolving it.

Related: qou-jqjx (the trace weight the retired producer used), qou-1ngr (closed - the feasible set itself is fine).


---

## Correction 2026-08-24 — this bean's own crossing-shell table is retired-convention

`qou-jqjx` closed, and it invalidates the numbers above. The table in item 1 was
computed on the deprecated producer's `tr_M(e-) = z^3`. Recomputed on live
convention D (`z = q^3/(q^2+1)`, `tr_M(e-) = h z^2 + z`):

    proton   cr=0 (none) 0.5444  cr=1 s0 0.3391  cr=2 s0.s0 0.6153  cr=3 s0.s0.s0 0.4678
    neutron  cr=0 (none) 0.4083  cr=1 s0 0.2175  cr=2 s0.s0 0.4537  cr=3 s0.s0.s0 0.3124

Three things change, and one gets sharper:

1. **`cr = 0` is now a shell.** The bare nucleon is feasible for both, so
   min-cr-first returns **0 gluon crossings for each**, not 1 and 2.
2. **Under min-|tr_M| the optimum is `sigma_0` at one crossing for BOTH** (0.339
   and 0.218). So the two objectives no longer pick different *counts* per
   nucleon — 0:0 and 1:1 respectively.
3. **The 2-versus-4 asymmetry is gone under either objective**, so item 1's
   framing ("the asymmetry exists only under pure min-|tr_M|") is too weak: it
   exists under neither. That is `qou-jqjx`'s finding, not this bean's, and the
   proton and neutron blocks now carry the withdrawal.

**What survives and is now the whole of this bean:** the objectives still
disagree about *which operator*, and item 2 is untouched —
`universal-ilp.witness.json` still asserts against `universal-ilp.py`'s own
`expected` values, so `status: "verified"` still checks nothing about the
corpus. Picking one objective and re-witnessing against it is still owed. It
just can no longer rescue a mass split, because there is no longer a split to
rescue.
