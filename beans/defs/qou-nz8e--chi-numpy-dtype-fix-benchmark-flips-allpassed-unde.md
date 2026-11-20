---
# qou-nz8e
title: chi-numpy-dtype-fix-benchmark flips allPassed under numpy 2.4.6
status: todo
pr: 8352
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T02:50:31Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

Found while draining `qou-kx04` (PR #5194). Not fixed — recorded, and the
damaged artifact was NOT committed.

## What happened

`computations/chi_numpy_dtype_fix_benchmark.py` re-run in a sandbox where
numpy had just been installed at **2.4.6**:

```
allPassed        true  -> false
  (assertion)    computed: true, passed: true  ->  computed: false, passed: false
durationMs     408402  -> 32485       (~12x faster: work is being SKIPPED)
```

The committed witness on `main` records `allPassed: true`. Nothing in the
producer changed between the two runs except the environment — my edit touched
only the `save()` call.

The 12x speedup alongside `computed: false` is the tell: the benchmark is not
failing a comparison, it is **declining to compute** under this numpy. A dtype
the benchmark exercises has most likely been removed or had its behaviour
changed in numpy 2.x, and the producer's guard takes a skip path that then
reads as a failure.

## Why it matters beyond this one file

The benchmark exists to pin a numpy **dtype** behaviour. A dtype-pinning
benchmark that silently stops computing under a newer numpy is the case where
a green-to-red flip is the least of the problem: the *skip* path is what
destroys the guarantee, and a run that skipped would look like a pass if the
assertion had been written the other way round.

Also note `per_irrep_pole_deuteron_h6`, hit in the same pass: its committed
witness was built with **sympy 1.12 + scipy 1.17.1**, and this sandbox has
sympy 1.14 and no scipy at all. Its assertions did not flip (the failing
`deuteron_full_tr_M_u_pole_eq_shift_NF` is False on both sides, pre-existing),
but a symbolic producer re-run on a different symbolic stack is not evidence
of anything and that witness was reverted too.

Separately: its committed witness records `scriptFile: per_irrep_pole_atom.py`
while the producer that writes it is `per_irrep_pole_deuteron_h6.py` — a
provenance mismatch worth a look on its own.

## What is needed

A pinned environment (or a recorded numpy floor/ceiling in the producer) before
either witness is regenerated. Neither should be re-run casually: both are now
known to move under an environment change rather than a code change.

## What DID land

The two source-level `q0Anchor` declarations are correct and were verified by
`resolve_q0_anchor` independently of any run — `chi_numpy_dtype_fix_benchmark`
resolves **proton** (absent from the manifest, so it takes the 2026-08-07
standing default), `per_irrep_pole_deuteron_h6` resolves **ambiguous** (listed
in the manifest's ambiguous set: both pin signatures present). The stamps will
land on the next run in a sound environment.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8352, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
