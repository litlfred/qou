---
# qou-9f4h
title: 'GAP: derive a structural per-partition truncation selector lambda -> k_lambda, or prove none exists (the rule in the compute is FITTED)'
status: todo
type: task
priority: normal
created_at: 2026-10-10T18:19:11Z
updated_at: 2026-10-11T05:42:03Z
parent: b9cj
---


Opened 2026-10-10 on owner instruction relayed from the project thread
("add bean to derive"). Evidence verified at source before writing this, not
transcribed from the relay.

## The gap

Derive a **structural** per-partition truncation selector `λ ↦ k_λ` for the
brane tower, or prove no such selector exists. This is the open part of
`conj:brane-tower-z-habiro`, and it is **not** closable by any rule selected
against the data.

## Why this is open rather than done: the rule in the compute is FITTED

The live catalogue uses *"`k_λ = 1` on one block, 2 elsewhere"*, published as a
"max-|μ| selector" that "closes all 3 atoms". All three parts of that are
wrong, and the primary source is the rule's own originating probe.

**Origin.** PR #639 cycle 5b, `probe_phiq_per_partition_klambda.py`. Read it
commit-pinned:

    git show 0763606e4f^:_deprecated/probes/probe_phiq_per_partition_klambda.py
    git show 0763606e4f^:_deprecated/probes/probe-phiq-per-partition-klambda.witness.json

🛑 **Cite the pinned form.** The `_deprecated/` tree is **no longer on `main`**
(removed 2026-10-10; it survives on branch `cat/cat-harness/fsh-guts`). A live
`_deprecated/...` path in a docstring or audit doc now resolves to nothing.

**1. It is a fit.** The probe's own docstring states the rule under test:

> *"Candidate rule under test: `k_λ = 1` if λ is the **maximum-|contrib|
> outlier** for the atom; `k_λ =` atom-uniform-`k` otherwise."*

Selection by maximum-|contrib| is selection of the Wedderburn block that
**dominates the quantity being reproduced**. AGENTS.md §"NO FITTING, EXCEPT
CAL-1/2/3": *"Selection against the target — choosing an object because the
choice reproduces the measured value — is a fit even though no continuous
parameter is tuned."*

**2. The "max-|μ|" label is wrong, and the probe's own data refutes it.** For
tritium the flipped block is **`[6, 3]`** (`/data/dominant_partitions/tritium/lambda`),
while the same probe's docstring puts T's `max|μ| = 8.23` at **`[4, 3, 1, 1]`**.
Two different partitions: the rule selected by *contribution* and was later
relabelled by *eigenvalue magnitude*. At one live site the relabel could not
even have been evaluated — `derived_chi_catalogue_build.py` hardcodes
`k_lambda=1` beside `mu_eigenvalues=["?", "?"]`.

**3. "Closes" meant `|tower| < 2` and was never compared to AME.** The probe's
closure print reads *"atoms collapse to small-magnitude towers (|tower| < 2)"*.
It records `ame_MeV` beside each atom and does not test against it. Recomputed
from its committed witness:

| atom | flipped block | tower (fitted) | AME `B` (MeV) | miss |
|---|---|---:|---:|---:|
| deuteron | `[2,2,1,1]` | 0.8764 | 2.2246 | **−60.6 %** |
| tritium | `[6,3]` | 1.9370 | 8.4818 | **−77.2 %** |
| ³He | `[5,4]` | 1.0659 | 7.7181 | **−86.2 %** |

The criterion is satisfied by driving the tower **toward zero**, while the AME
bindings are 2.22 / 8.48 / 7.72 — so the closure test is **anti-correlated**
with the data it was taken to close.

## What has already been ruled out

From `docs/coordination/2026-05-10-non-calibrated-q-beta-mass.md`, the PR #639
cycle ledger — six candidates are in the refuted table of
`docs/audits/2026-06-17-refuted-ansatz-lemmas.md` (scalar-eigenvalue family;
per-eigenvalue operator-valued at uniform `k`; Type-B fold; multiplicity-refined;
pair-knot product-volume; pair-knot Markov-trace), plus from the ledger:

- **LP cost argmax** — refuted (1/3)
- **SDP with diagonal Gram** — refuted (1/3)
- **Hoefsmit content-spread** — refuted
- **Type-B fold depth** — partial (2/3)

## The one route the May ledger never tested

**SDP with the full off-diagonal Gram.** Still recorded `UNTESTED | next probe`
in that ledger, five months on. It means computing Gram entries
`tr_M(b_i · b_j)` *across distinct Wedderburn blocks* via Hoefsmit matrix
products; the diagonal simplification is already refuted, so the off-diagonal
structure is where any remaining signal would be. The ledger's second surviving
route is a **Hoefsmit hook-content asymptotic along a reduced braid word**
(`(q, β)`-aware).

## 🛑 The constraint that makes this hard

**No selection against AME.** A selector chosen because it reproduces a binding
is the defect this bean exists to replace, not a solution to it. Per AGENTS.md
§NO FITTING, rank by derivational cleanliness first and treat accuracy as a
diagnostic: *"a more accurate fitted route is worth LESS than a less accurate
derived one."* A documented honest miss from a derived selector is the
deliverable; a better number from a chosen block is not.

Also note the **discrete-choice trap**: "it is only an integer per block, not a
continuous parameter" is explicitly named as fitting in the same section
("Sweeping a discrete parameter for accuracy"). One free choice per block is
`p(n)` free choices.

## Live state

`k_λ` is emitted by three witnesses and **read numerically by nothing** —
`derived-chi-catalogue`, `derived-chi-catalogue-sweep`, and
`delta-lambda-categorical-verification`. 🛑 **The third is a different object**:
a *jet-prolongation* order (that producer's own docstring, line 18), not a
truncation order. The shared name is a collision, not a third consumer. A
rename to `jet_order_k` was suggested but **not done** — it is a witness field,
so it is a schema change with its own blast radius, and it was offered as a
suggestion rather than an owner pick.

All three producers now label the field a fit in place, and the two documents
that published "closes" / "max-|μ|" are corrected (PR #7586).

## Status

**`todo`, and it stays `todo`.** Per AGENTS.md §13a — *"NEVER close a bean
whose subject is an open conjecture"* — recording that the current rule is a fit
is not deriving a selector. This closes only when a structural `λ ↦ k_λ` is
derived, or its non-existence is proved.

---

## 2026-10-11 — the May towers rest on HARDCODED inputs; the off-diagonal-Gram route is excluded in the block basis; my own table used |tower|

Findings relayed from a sibling session at ofri's request. **Separated below
into what I verified from the repo and what I am carrying on relay**, because
three of them bear on numbers this bean and PR #7586 already published.

### VERIFIED HERE, from the primary source

**1. My own table used `abs(total_tower)`, hiding a sign.** The witness's
signed `total_tower` for tritium is **−1.9370**, against an AME binding of
**+8.4818**. That is the **wrong sign**, not a "77.2 % shortfall" — a different
and worse statement. D (+0.8764) and ³He (+1.0659) are positive; only T flips.
This was my error, in the figures written into three producers and two docs.

**2. Three of the May probe's nine dominant-block entries were never
computed.** `DOMINANT_PARTITION` is a hand-written literal dict:

    "deuteron": {"lambda": [2,2,1,1], "contrib_k1": 0.0,    # negligible
                                      "contrib_k3": -65.0,  # approximate
    "tritium":  {"lambda": [6,3],     "contrib_k3": -27.0,  # approximate

**For deuteron this voids the result.** The rule sets `k_λ = 1` on the cut
block, so the tower is `non_dominant_sum + contrib_k1(cut)`, and the witness
records exactly `0.87640 + 0.00000 = 0.8764`. **The rule's entire effect on
deuteron was a literal `0.0` annotated "negligible".** The deuteron "closure"
is the non-dominant sum alone — it never measured the rule at all.

**3. Under convention D, deuteron's cut is provably a NO-OP** — and this needs
no compute. `[2,2,1,1]` has **four rows**, and
`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows` (sorry-free,
general `n`) gives `y_λ = 0` for every shape with a third row. So under the
canonical convention the block the rule flips for deuteron carries **zero
Ocneanu weight**, and changing its truncation order cannot move the tower. T
`[6,3]` and ³He `[5,4]` are two-row and survive. Structural, and independent of
every number below.

### RELAYED, arithmetically consistent, NOT recomputed here

Sibling session, 60 dps, two independent routes agreeing to 2e-58, rebuilt from
the braid word at `e2204a4a5d55` with Hoefsmit σ and Wenzl `y_λ`. Full report
cited as `/mnt/project-files/mass-endomorphism/klambda/recheck-tower-precision.md`
(not readable from this container).

- **May setup** (convention C, muon CODATA-2018): **D 0.2550**, **T −1.9719**,
  **³He 1.0656**; D's real `contrib_k1` = **−0.62148**, not 0.
- The uncomputed `k=3` entries: **D −32.94** (hardcoded −65), **T −23.50**
  (hardcoded −27).
- The PR #638 witness's `y_λ` are wrong by up to **1.15e-4** relative at `n = 9`.
- **Convention D at the proton pin**: **0.2222 / 2.8116 / −0.0098** — so
  **tritium fails `|tower| < 2`**, i.e. the closure criterion itself fails under
  the canonical convention.
- `argmax|μ|` differs from the cut block for **all three** atoms — D `[3,3]`,
  T `[3,3,3]`, ³He `[3,3,3]`. So the "max-|μ|" mislabel is broader than the
  one-atom discrepancy recorded above; the rule was max-|contrib| throughout.

**The one consistency check available to me without recomputing:**
`0.87640 + (−0.62148) = 0.25492` against the relayed `0.2550`. ✓

### 🛑 The route this bean named as the last untested one is now EXCLUDED — scope (b), in the block basis

This bean's §"The one route the May ledger never tested" named the **full
off-diagonal-Gram SDP**. Relayed exclusion, with its invariant named: the `e_λ`
are **central orthogonal idempotents**, so `tr_M(e_λ e_μ) = δ_λμ · tr_M(e_λ)`
and the Gram is **diagonal by construction** — measured max off-diagonal
`1.7e-52`. The LP then degenerates to "pick the cheapest block" and agrees with
the fitted rule **0 / 3**.

**But scope it, and do not over-read it.** That is an exclusion *in the block
basis*. The ledger's own phrasing is `tr_M(b_i · b_j)` over **braid-word**
elements `b_i`, which are not idempotents and whose Gram need not be diagonal.
So what is excluded is the idempotent/block-basis reading of that sentence, not
every reading of it. Per AGENTS.md §"Before declaring refuted", this is a
legitimate **(b)** for the stated basis and **not** a (b) for the route as the
ledger words it. Before calling the route dead, re-state it — and the sibling
route (Hoefsmit hook-content asymptotic along a reduced braid word) — in the
basis each is meant in.

### What this leaves

The ten refuted candidates stand. The seventh (the live fitted rule) is now
known to rest on invented inputs as well as on selection against the target, and
to be a no-op for deuteron under the canonical convention. The block-basis SDP
is excluded. **No derived selector exists, and the search space is smaller than
this bean recorded yesterday.**

The sibling session reports it is now (a) re-running on the current braid word
under convention D and (b) **pre-registering q-only truncation rules before
scoring them** — which is the right shape under §NO FITTING, since
pre-registration is what makes a rule a prediction rather than a selection.

**Still `todo`.** Nothing here derives a selector; most of it narrows the space
and corrects the record.
