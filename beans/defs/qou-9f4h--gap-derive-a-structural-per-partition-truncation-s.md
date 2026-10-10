---
# qou-9f4h
title: 'GAP: derive a structural per-partition truncation selector lambda -> k_lambda, or prove none exists (the rule in the compute is FITTED)'
status: todo
type: task
priority: normal
created_at: 2026-10-10T18:19:11Z
updated_at: 2026-10-10T18:22:21Z
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
