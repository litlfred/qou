---
# qou-k54t
title: The carrier table straddles TWO disagreeing chi sources — A<=4 reads a rust chain whose witness records 8ms for a 15-minute computation
status: todo
type: task
priority: normal
created_at: 2026-09-07T11:14:56Z
updated_at: 2026-09-07T11:45:28Z
---

## The question this answers

Last turn's loose thread: in `carrier_table_convention_d_rederivation.py`,
`𝒜 = B_AME/(m_e·S)` moved ~30 % for ⁵Li and ⁶Li under the intra-ordering
regeneration but was **unchanged** for ²H, ³H, ³He and ⁴He, though every atom's
caches were regenerated. I recorded it as unexplained. It is not a structural
invariance.

## The light atoms are bit-identical, not merely within tolerance

Comparing the witness at `c3b11a07f5` (2026-08-26) against today's re-run:

| atom | `m_e·S` before | after | ratio |
|---|---|---|---|
| ²H | 0.346713766129367267 | 0.346713766129367267 | **1.0** |
| ³H | 0.47196856312508015 | 0.47196856312508015 | **1.0** |
| ³He | 0.314121863371399832 | 0.314121863371399832 | **1.0** |
| ⁴He | 0.384481710104210974 | 0.384481710104210974 | **1.0** |
| ⁵Li | 0.256849955461560025 | 0.410756668087517243 | 0.6253092778 |
| ⁶Li | 0.296554673175081457 | 0.386145182858856575 | 0.7679874988 |

Identical to 18 digits. So for A ≤ 4 the quantity does not depend on the
regenerated data **at all**.

## Because the two halves of the table read DIFFERENT χ SOURCES

`rederive()` takes both characters from a cache:

```python
rows = reeb["data"]["per_atom"][atom]["by_partition"]
r_free = mp.mpf(str(r["chi_free"])) / d
r_atom = mp.mpf(str(r["chi_atom"])) / d
```

Only `y_λ` is recomputed. So the chain is

    A ≤ 4:  atom-chi-rust-{d,t,3he,4he}  ->  binding-reeb-phase-decomposition
            (2026-07-06)                 ->  carrier table
    A ≥ 5:  the regenerated nucleon caches -> chi_free_via_frobenius (live)
                                          -> carrier table

Two different producers, and **they disagree**. Comparing
`atom-chi-rust-4he.data.atom` against `chi-helium-4-h12-at-q0-50dps`, both
claiming `χ^λ(β_⁴He)` at q₀, over the same 77 partitions:

- **exact agreements: 2 / 77**
- max relative difference **827.91**
- the ratio rust/canonical ranges **−826.91 … +815.44**

**The only two that agree are `(12)` and `(1¹²)`** — the two one-dimensional
representations. That is the diagnostic signature. A normalisation or a
convention scale would move every block by *one* ratio, including those two.
A 1-dimensional character is a product of per-letter scalars, so it is fixed by
the letter **multiset** and blind to the **order** — and I verified earlier that
the grouped and borromean words are exactly the same multiset reordered
(lengths 23/35/35/47, `Counter` equality). So the two witnesses hold the same
letters in a different order: **one is grouped, one is borromean.**

## 🛑 And the timestamp says the opposite — do not read `computedAt` here

`atom-chi-rust-*` are stamped **2026-09-05T08:59–09:25**, *after* the ruling
commit `7db032fb48` (07:53:55), and `compute_atom_chi_rust.py` calls
`atom_braid_word_3A(Z, N, include_inter=...)` with no `intra_order`, i.e. the
borromean default. By provenance they look current.

They are not. **Their recorded `durationMs` is 8–11.** Eight milliseconds is
not 77 characters at 50 dps — and the commit they carry, `369a9d828a`
(09:03:09), is *"witness(qou-t0wm): refresh scriptHash on D/T/3He — the
docstring warning left them self-stale"*, a **metadata refresh**. The payload
was never recomputed; only its stamps were.

Measured directly: a genuine `compute_atom_chi_rust.py 4He` has been running
**over 15 minutes** against that recorded 8 ms. Whatever produced the committed
file, it was not this producer computing anything.

This is the same error class this corpus has recorded twice before — reading a
`computedAt` as the date a value changed — arriving through a third route:
**a metadata-refresh commit that moves the stamp and not the number.**

## What this means for work already landed

The three anchors re-pinned earlier today (`qou-8jfh`) were ⁵Li/⁶Li, on the
**live** side, and two independent routes agreed on the new values — that stands.
But the table as a whole is now **internally inconsistent**: A ≥ 5 on the
borromean word, A ≤ 4 on the grouped one. `anchor_kappaD_reproduced`
(6.4161462) and `anchor_kappa4He_reproduced` (73.5943) are **passing against
stale data on both sides of the comparison** — a false green, not a check.

## What is NOT established

- Which of the two χ witnesses is right. Both are post-ruling by stamp; only one
  can be borromean, and the multiset argument says they differ in order, not
  which order is correct.
- Whether `compute_atom_chi_rust.py` re-run to completion reproduces the
  canonical caches. That run is **still in flight** and is the direct test.
- Whether other consumers of `atom-chi-rust-*` are affected. `git grep` finds it
  in at least five further producers (`binding_depth_stratified_rust.py`,
  `binding_depth_stratified_knot_weighted.py`,
  `binding_depth_stratified_selfconj.py`, `binding_heat_kernel_weight_probe.py`,
  `audits/q0_witness_read_dataflow_audit.py`). Untriaged.

## Note on the middle link

Re-running `binding_reeb_phase_decomposition.py` moved all 148 values, but only
by **7.99e-7 … 3.21e-6** — consistent with its inputs being stale rather than
refreshed. That run was **reverted, not committed**: the container records
numpy 2.5.0 → 2.4.6, python 3.13.12 → 3.11.15 and scipy 1.18.0 → 1.17.1
against the witness on disk, and committing it would weaken the provenance
record for a 1e-6 move.


## 🛑 RETRACTION — the `durationMs` argument above is WRONG

I wrote: *"Their recorded `durationMs` is 8–11. Eight milliseconds is not 77
characters at 50 dps … The payload was never recomputed; only its stamps
were."* **That reasoning is invalid — I read the wrong field.**

`durationMs` is not the computation time. The committed ⁴He witness records, in
its own data block:

    atom.compute_time_sec  977.7418208122253   (16.3 min)
    free.compute_time_sec  454.92478799819946   (7.6 min)

a genuine **~24-minute** computation, alongside `durationMs: 8`. And a
deuteron run I performed today records `durationMs: 9` while being a real,
complete run. So `durationMs` measures something else (witness assembly), and
it **cannot discriminate a computed witness from a refreshed one** in either
direction.

The claim that the ⁴He payload "was never recomputed" is withdrawn. It was
recomputed, for 24 minutes.

**Contaminated:** this bean's body above, and commit `6e9557d5ce`, both pushed.
Nothing else quotes it.

## The CONCLUSION survives — established by the direct test instead

The cheap case settles it. `compute_atom_chi_rust.py D` (n=6, 11 partitions)
run today, three-way against the canonical borromean cache:

| comparison | exact | max \|rel\| |
|---|---|---|
| rust **OLD** (committed) vs canonical | **2 / 11** | 21.335035 |
| rust **NEW** (run today) vs canonical | **11 / 11** | **1.0924651e-49** |
| rust OLD vs rust NEW | 2 / 11 | 21.335035 |

So the producer, run today, reproduces the canonical caches **exactly**, and
the committed values are the grouped word. The straddle is real; only my
argument for it was wrong. The 2-of-11 that agreed in the OLD comparison are
again the two one-dimensional reps, so the multiset/order signature holds.

## 🛑 And the MECHANISM is unexplained — my second theory is also wrong

I supposed the runs might have fallen between the two ruling commits. They did
not. **`7db032fb48` (07:53:55) is the commit that introduced
`intra_order: str = "borromean"` as the default**, and every rust run is
stamped 08:59–09:25, *after* it. `deb9ff5728` (09:06:48) only touches
docstrings.

So a producer defaulting to borromean, run an hour after that default landed,
wrote grouped values. **I do not know why**, and I am not guessing a third
time. One untested candidate worth recording, because the same commit
introduces it: `_NUCLEON_WORDS_Q0` is a **module-level cache**, documented as
*"built on first use"*. A long-lived process that populated it before the
change would keep returning grouped words for its whole lifetime regardless of
the source on disk. That is a hypothesis, not a finding — testing it means
reproducing the process lifetime, which I have not done.

## Repaired so far

`atom-chi-rust-{d,t,3he}` regenerated today and now match the canonical
caches. `atom-chi-rust-4he` is in flight (~24 min by its own recorded
`compute_time_sec`).

Until it lands the rust family is itself split — D/T/³He borromean, ⁴He
grouped — which is a *worse* straddle than before, so this must not be left
half-done.


## 🛑 CORRECTION — "five other consumers" was a truncated grep, not a count

I reported the blast radius as *"at least five further producers"* and listed
five. That list was the output of a `head -5`; I reported the truncation as the
count. Measured properly (`git grep -ln atom-chi-rust -- '*.py'`, excluding
`_deprecated`):

| | count |
|---|---|
| files referencing `atom-chi-rust` | **67** |
| of those, actually pulling χ values (`chi_lambda` / `by_partition`) | **63** |
| mention-only | 4 — `q0_witness_read_dataflow_audit`, `binding_log_scale_investigation`, `binding_reeb_ratio_rho_free`, `threerow_chi_sparse` |
| readers that emit a committed witness of their own | **35** |
| of those 35, dated **pre-ruling** | **34** |
| dated on/after 2026-09-06 | **1** |

So the surface is **63 producers**, not five — an order of magnitude out, and
in the direction that matters.

## What that does and does not license

It does **not** license calling 34 witnesses stale-and-wrong. A pre-ruling date
is expected wherever nobody re-ran a producer, and whether each output *moves*
is unmeasured.

What is different here from an ordinary staleness date: these 63 read a source
that is **now measured to have moved**, and moved by a lot — the committed rust
caches disagreed with canonical on 9 of 11 deuteron blocks (max 21.3) and 75 of
77 ⁴He blocks (max 827.9). That is stronger evidence than a timestamp, because
the input change is demonstrated rather than inferred. It still is not a
per-producer measurement.

The right next step is the dating pass already committed as
`computations/audits/date_failing_witnesses_against_pre_regeneration.py`,
pointed at this population rather than at the failing set — it distinguishes
"would move" from "already recorded as moved" without re-running 63 producers.
