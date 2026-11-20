---
# qou-a71h
title: frobenius-gram-delta-lambda witness is 93% stale on main, and it is NOT the pin, the y_lambda, or the native extension
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T03:50:09Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

## The move

`computations/frobenius-gram-delta-lambda.witness.json`, field
`result.per_isotope.3He.variants["frob  Σ y·‖ρa‖²·dχ"].S`:

    committed on main   -842.1174706      abs_miss 827.014
    every fresh run     -436.2405707      abs_miss 421.137     (-48.2 %)

Found by re-running the producer as a downstream consumer of the y_λ re-derivation
(bean qou-9ugp item (a)); the producer source is UNMODIFIED on this branch.

## Five candidates excluded BY MEASUREMENT, not by argument

| candidate | test | result |
|---|---|---|
| the y_λ re-derivation (item (a)) | restored the 5 witnesses from `852e64fb4e^`, re-ran | **-436.2405707** — unchanged |
| origin/main's y_λ (moved since) | restored h9 + h12 from `origin/main`, re-ran | **-436.2405707** — unchanged |
| the q₀ pin | probe reads y_λ from file; both versions above span the pin change | unchanged |
| `pyhecke_native` present vs absent | `find_spec` meta-path block, **self-tested to confirm the block fired** | **-436.2405707** — unchanged |
| its χ input | `atom-chi-rust-3he.witness.json` is byte-identical to `origin/main` | not the cause |
| its D-leg input | `rho-k-h3a-lp-dual.witness.json` byte-identical to `origin/main` | not the cause |

Note the first native-block attempt was a NO-OP: it used the legacy
`find_module`, which Python 3.11 ignores. It reported "unchanged" and would have
been read as evidence. The second used `find_spec` **and imported the module to
prove the block fired before trusting the run**. A negative from a blocker you
have not proved is active is not a negative.

## So it is import-cone drift, and it is pre-existing

Every INPUT is byte-identical to `origin/main`; the producer is unmodified; the
answer still cannot be reproduced. What changed is inside the probe's own compute
path (the `‖ρa‖²` Frobenius Gram), in code the file-local `git diff` cannot see —
the class AGENTS.md records for `binding_canonical` (`tr_M_atom` 0.388 -> 0.575,
48 %, from a source-stable producer whose callee moved).

Same class as the 9.3e-7 drift found the same day in
`deltalambda-binding-cross-isotope`, three orders of magnitude larger.

## Why it matters

`abs_miss` is the probe's headline: how far the Frobenius-Gram Δ_λ variant sits
from the AME target. 827 -> 421 halves the reported miss. Anything citing this
witness's ³He miss is citing a number the current tree does not produce. The
probe wires nothing, so nothing downstream moves — but it is an input to the
Δ_λ magnitude discussion, which is the arc's one real open problem.

## Not chased further here

Bisecting the cone is a separate task; this branch's scope is the q₀ drain. The
fresh witness is committed because it is what the tree computes — leaving the
stale one would be preferring an unreproducible number.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8313, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
