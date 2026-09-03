---
# qou-wjbd
title: 'wpdb attempt: prove or refute the word-depth -> partition-depth bridge'
status: in-progress
type: task
priority: normal
created_at: 2026-08-26T03:01:15Z
updated_at: 2026-08-26T03:23:34Z
---

## 2026-08-26 — attempted the bridge. NOT closed. The obstruction is now sharper, and the last reading is dead.

Full write-up:
[`docs/audits/2026-08-26-no-shift-rescues-the-word-partition-bridge.md`](../docs/audits/2026-08-26-no-shift-rescues-the-word-partition-bridge.md).
**It is open. Nothing here closes it.** What changed is that the surviving
candidate is gone and the obstruction is now shift-invariant.

### The one thing in the inherited record that was too optimistic — and it was mine to catch

The second audit tested

    #{lambda |- n : gbDepth = k}  <=  #{w in S_n : l(w) = k}

and reported **fails at n <= 3, holds at n = 4..7**, concluding the Coxeter
reading "is not an exclusion of the identification in general". That verdict is
correct *about the test that was run* and I am not retracting it. But the test
compares the partition strata against `gr_k` of the **whole algebra**, and
`Z^(k)` is a graded piece of the filtration induced on the **centre**. The bound
is sound and very lossy: at n = 6 it compares against `{1, 5, 14, 29, 49, 71,
90, 101, ...}` when the true graded dimensions are
`{1,0,0,0,0,0,0,0,1,1,1,0,1,3,2,1}`.

Computing `dim(Z cap F_k)` instead turns a necessary condition into an
**equality test**. It fails at every n. So the reading was never viable at
n = 4..7 — the earlier pass could not see it through that bound, and that is why
this front looked open for ten days.

### Result 1 — degree 0, and it is filtration-AGNOSTIC (scope (b))

For ANY filtration with `F_{-1} = 0` and `1 in F_0` — true of every reading the
corpus names — `Z^(0) = Z cap F_0` contains the unit, so it is nonzero. The
partition side's degree-0 stratum is EMPTY, because `gbDepth = lambda_1 +
lambda'_1 - 1 >= 1`. So the identification **as written** is false for every n
and every candidate `J^bullet`. Invariant cited: the unit is central and sits in
filtration degree 0; `gbDepth > 0` (Lean `gbDepth_pos`, sorry-free).

This matters because the six sites write it unshifted, and
`phi-q-categorical-truncation-proof` writes the sum starting at `k = 0`
explicitly. It also says what the repair has to be: a shift.

### Result 2 — the sharp measurement (exact, three backends)

`docs/audits/scripts/centre_length_filtration_vs_gbdepth.py`. Builds `H_n(q)` in
the `T_w` basis, solves for the centre, intersects with each `F_k`. **No
floating point anywhere.** `Fraction` over QQ, `F_p` with p = 2^61-1, and
symbolic `QQ(q)` for n <= 4 — three exact backends agreeing. `dim Z = p(n)` at
every sample, certifying the specialisations generic. Specialising q can only
LOWER the rank, so every dimension reported is an upper bound on the generic
value — the direction every exclusion needs, so no genericity is assumed.

| n | p(n) | gbDepth strata | dim Z^(k) (Coxeter) |
|---|---|---|---|
| 2 | 2 | {2:2} | [1,1] |
| 3 | 3 | {3:3} | [1,0,1,1] |
| 4 | 5 | {3:1,4:4} | [1,0,0,0,1,2,1] |
| 5 | 7 | {4:2,5:5} | [1,0,0,0,0,0,1,1,1,2,1] |
| 6 | 11 | {4:2,5:3,6:6} | [1,0,0,0,0,0,0,0,1,1,1,0,1,3,2,1] |

No match at any n. At n = 6 the two dimension MULTISETS already differ
(`{1,1,1,1,1,1,2,3}` vs `{2,3,6}`), so not even an arbitrary permutation of the
index set works.

### Result 3 — no SHIFT repairs it, for all n >= 3 (scope (b))

The table is finite; this is not.

* **Lemma 1.** `Z cap F_0 = R.1`, so `dim Z^(0) = 1`. (`F_0 = R.T_e = R.1`.)
* **Lemma 2.** For n >= 3, `Z cap F_1 = R.1`, so `dim Z^(1) = 0`. Proof: in
  `[a_0 + sum_i a_i T_{s_i}, T_{s_j}]` the commuting pairs (|i-j| >= 2)
  contribute nothing, and for |i-j| = 1 the elements `s_i s_j` and `s_j s_i` are
  DISTINCT of length 2, so the coefficient of `T_{s_i s_j}` is exactly `a_i`.
  Centrality kills every `a_i` with an adjacent `j` — every i once n >= 3.
* **Lemma 3.** The gbDepth spectrum is the CONTIGUOUS interval `[m_n, n]`.
  Proof: depth d is attained iff some `r + s = d + 1` has `rs >= n` and
  `r + s - 1 <= n`; the max product `floor((d+1)^2/4)` is monotone in d.
  (Verified to n = 40.)
* **Theorem.** The word side is nonzero at 0, zero at 1, and nonzero above
  (total `p(n) >= 3`) — so its support has an INTERIOR GAP. The partition side
  has none. A shift is an order isomorphism of the index set, so it transports
  gap-freeness. No shift exists. n = 2 falls to the table.

Lean, sorry-free, `lean`-direct exit 0 against the real import cone,
`#print axioms` clean on all five declarations (propext / Quot.sound /
Classical.choice only):
`content/quantum-observable-universe/lean/QOU/BraidKnot/CentreGradingObstruction.lean`
— `gbDepth_pos`, `gbDepth_ne_zero`, `shift_cannot_fill_a_gap`, `N4_gapfree`,
`coxeter_reading_excluded_at_four`. The algebra-side inputs are carried as
hypotheses (H_n(q) and its centre are not Lean objects here) and the theorem
DERIVES the exclusion from them, per §3b-cond.

### What I did NOT prove — read before citing any of the above

**The identification is NOT refuted in the abstract.** A filtration inducing the
gbDepth grading on the centre exists trivially: filter by the Wedderburn blocks,
`F_k := sum_{gbDepth lambda <= k} R.e_lambda`. What is excluded is that any of
the THREE things the corpus calls `J^bullet` is such a filtration. Saying it the
other way round is exactly the over-claim the scope-(a)/(b) rule exists to stop.

**No mass or binding number is touched.** `J^bullet` enters downstream as an
INDEXING — which body order an `a_D^(n)` belongs to, which stratum a projector
lands in — not as a magnitude. Wedderburn, Markov trace, `tr_M`, `y_lambda`, the
idempotents, `gbDepth`-as-a-definition and `prop:gb-spectral-sequence` are all
unaffected. **And `prop:curvature-rank-gb-stratification`'s own statement, about
words, is not refuted** — what fails is reading a partition grading off it.

### The six consumer sites — recommendation (judgement, not finding)

The second audit's dilemma collapses: branch (i) is now excluded at EVERY n, so
**the citation does no work, at all six sites.** The repair splits, and one half
needs no conditionality:

* **Class A — the site needs only the grading as a DEFINITION.** `Z = sum_lambda
  R.e_lambda` is Wedderburn; bucketing by `gbDepth` is free, and
  `k*(T_w) := max{gbDepth lambda : lambda in supp(T_w)}` is defined from the
  PARTITION support, not from any word rank. Such sites are sound mathematics
  and need only to stop citing the word proposition — no conjecture, no §3b
  propagation. `prf:phi-q-categorical-truncation` looks like this. (But its
  truncation claim is then carried by the partition support alone, and
  `gbDepth_const_on_H3` already showed that support is constant at n = 3 — so it
  is vacuous at the single-nucleon case either way.)
* **Class B — the site needs genuine word-filtration compatibility.**
  `prop:jet-prefix-gb-filtration` (`beta_k^GS in J^{k-3}/J^{k-2}`) and
  `prf:unified-curvature-rank-mass-formula` ("by curvature-rank stratification,
  `e_lambda` has GB-depth `depth(lambda)`"). These ARE the identification and
  should be re-scoped conditional on a named conjecture — which must record that
  all three candidate readings are excluded, so it is open AND currently without
  a candidate construction.

**Deliberately not executed here.** The sites cite the proposition for different
things and mechanical editing across them is how this defect got in. What I did
do is add forward-pointers at the top of both 2026-08-16 audits, since seven
blocks' banners point there — a reader following the existing chain now lands on
this finding without any content-block sidecar being staled.

### Still open, and now more precisely

**Is there a filtration of `H_n(q)`, definable from the Groebner-Shirshov
rewriting data, whose induced grading on the centre is the gbDepth grading?**
Nobody has tested a fourth object. Any candidate must satisfy: its degree-0
piece is the line spanned by the unit (Result 1), so it can match only after a
shift; and the shift must carry a GAP-FREE spectrum onto a sequence beginning
`1, 0` (Result 3). So a candidate has to either fail to be an algebra
filtration, or **put a second central element in `F_1`** — and Lemma 2 proves
the Coxeter one cannot. That is the next thing to test, and it is a much
narrower target than "find the bridge".

### Housekeeping

PR #5799 was CLOSED unmerged at 2026-08-26T03:19Z, mid-session — after this bean
was created. All four commits are pushed to
`claude/isotope-mass-binding-dashboard-kdvhz6` and are safe, but the tranche
currently has no open PR. Did not reopen or duplicate it: the close looks like a
deliberate act and re-opening someone else's closed thread is not mine to do.
