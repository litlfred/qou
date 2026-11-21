---
# qou-k54t
title: The carrier table straddles TWO disagreeing chi sources — A<=4 reads a rust chain whose witness records 8ms for a 15-minute computation
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T11:14:56Z
updated_at: 2026-11-21T04:29:34Z
parent: qou-5vkl
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


## Does this reach the paper? Yes — and the repair moved it TOWARD the paper

I first checked whether any content block cites the four chain witnesses
directly: **zero**. That was the wrong question — content cites *downstream*
witnesses. Of the **35** downstream witnesses, **3 are cited from `content/`**:

| witness | cited by | date | state |
|---|---|---|---|
| `binding-depth-stratified-knot-weighted` | `mass-theory/depth-stratified-frobenius-reciprocity.ts` (`computation.witness`) | 2026-08-29 | `allPassed=false` already |
| `binding-rotation-phase-lead` | `mass-theory/binding-alpha-shift-extension-context.md` — **quoted in prose** | 2026-09-04 | `allPassed=true` |
| `delta-lambda-l1-ceiling-sign-prune` | `lean/QOU/BraidsAndKnots/DeltaLambdaL1Ceiling.lean` (docstring provenance) | 2026-09-05 | `allPassed=true` |

Only the second is a **number a reader sees**. The block states:

> *"Per `binding-rotation-phase-lead.witness.json`, the deuteron's full
> Markov-weighted q-Reeb phase aggregation gives ρ_full(D) = **14.6673**
> MeV/rad."*

## The three-way comparison, and it is not what I expected

Re-running `binding_rotation_phase_lead.py` with `atom-chi-rust-{d,t,3he}`
repaired moved **30 of 36** data fields. For the field the paper quotes,
`aggregations.S3_markov.rho_needed.D`:

| | value | vs the paper's figure |
|---|---|---|
| paper prose | 14.6673 | — |
| witness **as committed** | **177.422** | **12.0964×** |
| witness **re-run today** | **14.9402** | **1.861 %** |

**The committed witness already disagreed with the paper by a factor of 12
before I touched anything.** The repair did not break the paper number — it
brought the witness from 12× away to within 1.9 % of it.

That is an independent consistency check on the repair that I did not
construct: the paper's own recorded figure, written when the chain was
presumably coherent, is reproduced to ~2 % by the fixed inputs and not at all
by the stale ones. It is corroboration, not proof — 1.9 % is not agreement,
and I have not established when or why the committed witness diverged.

Also notable: `S3_markov.rho_needed.3He` was **`null`** in the committed
witness and is **56.6306** now — the ³He leg could not be computed from the
stale caches at all.

## Severity, bounded

The chain feeds 63 producers, but only **one** reader-facing number, and that
number is currently *better* served by the repair than by the committed state.
The `.lean` citation is a docstring provenance line, not a proof dependency.
The `.ts` citation points at a witness already failing.


## The 1.9 % residual — my hypothesis was wrong, and the real timeline is better

I closed the last note guessing the 1.9 % gap between the paper's 14.6673 and
the re-run's 14.9402 "may be the ⁴He leg, which is still stale". **It cannot
be.** `binding_rotation_phase_lead.py` computes `aggs["S3_markov"][name]` per
atom, from that atom's own `chi_free`/`chi_atom` only, and then
`rho[iso] = AME[iso] / vals[iso]`. The deuteron figure depends on
`atom-chi-rust-d` alone — already repaired and verified exact against
canonical. ⁴He does not enter it.

### What the history actually says

`rho_needed.D` across every commit that touched the witness:

| commit | date | value |
|---|---|---|
| `52c68267f2` | witness `computedAt` **2026-06-22** | **14.669** |
| `831980f1ce` | 2026-09-04 — *"q0(a): the nine y_lambda consumers re-run"* | **177.422** |
| `3b0c808122` | 2026-09-07 (this session) | **14.9402** |

`52c68267f2` is **the same commit that wrote 14.6673 into the paper**
(found with `git log -S "14.6673"`). So the prose and its witness agreed to
0.012 % when the figure was written. The number was correct as published.

It broke on **2026-09-04**, at a commit whose own message says it re-ran a set
of consumers — and it broke to **12.0964×**. Today's re-run, with the χ inputs
repaired, restores it to **1.861 %** of the published value.

### So the 1.9 % is the expected part and the 12× was the defect

A ~2 % move is what an intra-nucleon reordering *should* do to a phase
aggregation. A 12× move is not. The published figure was right, the committed
witness was wrong for three days, and the repair recovers the published value
to within the size of the ruling's own effect.

### Mechanism NOT asserted

The breaking commit re-ran consumers with refreshed `y_λ`. Whether the 12×
came from a `y_λ`-against-stale-χ straddle, or from something else in that
pass, is **not measured** — and note the timing does not obviously fit a
word-order cause: 2026-09-04 is the day *before* the intra-ordering ruling, so
the χ that run read were grouped and correct at the time. I have guessed at
two mechanisms this session and been wrong twice; this one stays open.

What is measured is the shape: **published value, three-day 12× excursion,
recovery to 1.9 %** — and that the recovery required repairing the χ source,
not touching the paper.

## The triage rule DECIDES the 34, and the answer is the inconvenient one (2026-09-07)

`computations/probes/one_dim_reps_are_blind_to_intra_order_probe.py` (6/6)
establishes that the intra-ordering ruling leaves exactly the two 1-dimensional
reps invariant — the trivial `(n)` and the sign `(1^n)` — and moves every
higher-dimensional block. That is a theorem, not a heuristic: a 1-dim
character is a product of per-letter scalars, and a product is commutative, so
it is fixed by the letter multiset and blind to the order.

So a producer reading only `(n)` or `(1^n)` is unaffected; anything else is
stale. That was meant to shrink the re-run population. **It does not shrink it
— it decides it, and the decision is "essentially all of them."**

Measured over the 68 `atom-chi-rust-*` readers:

| class | count |
|---|---|
| consumes higher-dimensional blocks — **STALE** | **64** |
| 1-dim selectors only — safe | **0** |
| reads the file but not the chi | 4 |

The four exempt are `q0_witness_read_dataflow_audit.py`,
`binding_log_scale_investigation.py`, `binding_reeb_ratio_rho_free.py`,
`threerow_chi_sparse.py`.

**The 64 is an UPPER BOUND on staleness, not a measurement of it.** The
classifier is a regex over source and takes "consumes all blocks" as the
conservative default — anything not provably 1-dim-only is called stale. A
producer that iterates every block can still have the higher ones cancel in its
output. So the honest reading is: *64 cannot be shown safe by inspection*, and
each still needs either a re-run or an argument.

What the rule is worth is that it closes the hope of an exempt subset. Nobody
should now spend a pass looking for one — there is none above the ULP.

**A second use, unmeasured.** The invariance is also a CHECK on any future
regeneration: if a regeneration moves a 1-dim block by more than the `qou-07ts`
ULP (~2e-50), it changed the letters and not merely their order, which is a
different and larger claim than the ruling makes. The probe asserts this in
both directions already.

## The false green breaks — and one of my own three re-pins was on stale data (2026-09-07)

With the rust family uniform and the chain re-run
(`binding_reeb_phase_decomposition` → `carrier_table_convention_d_rederivation`),
`carrier_saturation_mechanism_probe` goes **10 assertions, 3 FAILURES**:

| assertion | computed | expected | verdict |
|---|---|---|---|
| `anchor_kappaD_reproduced` | 29.0753769712 | 6.4161462 | **FAIL** — the false green |
| `anchor_kappa4He_reproduced` | 702.409002162 | 73.5943 | **FAIL** — the false green |
| `carrier_band_ratio_pinned` | 10.1965869286 | 1.50250 | **FAIL** — *my re-pin, on stale data* |
| `anchor_kappa5Li_reproduced` | 64.1028242404 | 64.10282 | PASS |
| `li6_amplification_reproduced` | 82.8548137339 | 82.85481 | PASS |

**Two of my three re-pins from the previous session were right and one was
not.** ⁵Li (64.10282) and ⁶Li (82.85481) reproduce exactly, because those two
atoms are not among the four whose caches changed. The third, `1.8375 →
1.50250`, was derived from the light atoms while their caches were still on the
grouped word — the same error class this whole arc is about, committed by me
while fixing it.

### But the replacement is NOT 10.1966, because that number straddles two words

`carrier_band_ratio_pinned` is `max/min` of `m_e·S` over A=2…6. ⁵Li and ⁶Li take
their **atom** χ from `chi-lithium-{5,6}-h{15,18}-at-q0-50dps-matrix-m.witness.json`,
and both were last touched **2026-08-15** — twenty-one days before the ruling
(`7db032fb48`, 2026-09-05 07:53:55). Neither carries a `computedAt` or a
`scriptHash` at all, so the witness cannot date itself; git had to.

Split by word, the ratio is not 10.2 under *either*:

| population | max/min |
|---|---|
| all six — **what is pinned** | **10.196587** |
| repaired four (borromean) | 1.899285 |
| stale two (grouped) | 1.063736 |

So the factor of ten is **the gap between the two groups**, not a property of
either: the four light atoms sit at `m_e·S ≈ 0.040–0.077` while the two Li sit
at `0.386–0.411`. Pinning 10.1966 would launder a mixed-word ratio into a
regression anchor, which is worse than leaving the assertion red.

### The producer-side fix exists and the producer already warned about it

`chi_via_rust_lossless.py` regenerates both (`--fresh 5Li 6Li`), and its own
source carries the warning this arc keeps re-deriving:

> `--fresh` EXISTS BECAUSE THE REUSE BRANCH CANNOT SEE A CONVENTION CHANGE. It
> gates on completeness … so a cache computed under a SUPERSEDED CONVENTION is
> "complete" and is served forever. Worse, the hit still calls `_stamp_anchor`,
> which rewrites the file — so a routine re-run leaves it looking freshly
> regenerated while every number in it is stale.

That last clause explains the missing `computedAt`: a re-run *touches* these
files without recomputing them, so their git date is evidence about stamping,
not about the numbers.

## `computedAt` after a ruling does NOT mean computed on post-ruling data (2026-09-07)

Blast radius of the stale ⁵Li/⁶Li caches, measured. A grep for `matrix-m`
returns **24** files, but that matches the whole matrix-M producer family. Only
**4** name the Li caches specifically:

- `deltalambda/carrier_table_convention_d_rederivation.py`  ← the chain
- `deltalambda/carrier_saturation_mechanism_probe.py`       ← the chain
- `deltalambda/li6_h18_amplification_discriminator_probe.py` ← the chain
- **`delta_lambda_empirical_tabulation.py`** ← not previously in scope

So the radius is contained, which is the good news. The fourth one carries the
finding.

`delta-lambda-empirical-tabulation.witness.json` has
`computedAt: 2026-09-06T06:47:25Z` — **after** the intra-ordering ruling
(`7db032fb48`, 2026-09-05 07:53:55). By the ordinary staleness test it is fresh.
It is not: it reads
`chi-lithium-{5,6}-h{15,18}-at-q0-50dps-matrix-m.witness.json`, which were last
touched **2026-08-15** and are still on the grouped word.

**So the producer ran after the ruling and consumed pre-ruling data, and
`computedAt` cannot tell those apart.** It records when the *producer* ran, not
when its *inputs* were computed. This is the `scriptCommitSha` confusion one
level out: a timestamp on the wrong object.

The general form, worth carrying: **a witness is only as fresh as the oldest
cache in its read cone**, and no field in the witness schema records that. The
existing import-cone audit
(`witness_import_cone_staleness_audit.py`) keys on *module* drift, not on
*witness-input* drift, so it does not cover this either.

**Second, smaller observation on the same file:** it reports
`allPassed: True` with `assertions: 0`. A witness asserting nothing is vacuously
green. That may be deliberate for a tabulation rather than a test, but it means
its green says nothing about the staleness above, and a sweep counting green
witnesses counts it.

It needs re-running once the Li caches land; it is not in the chain I have been
re-running, and nothing would have flagged it.

## CORRECTION: all three of my re-pins were on bad data, not one (2026-09-07)

Above I wrote *"Two of my three re-pins from the previous session were right and
one was not."* **That is wrong, and the two I called right are the worse case.**

`rederive_large_a` builds ⁵Li/⁶Li from two halves with different provenance:

| half | source | computed | word |
|---|---|---|---|
| atom χ | `chi-lithium-{5,6}-h{15,18}-…-matrix-m.witness.json` | 2026-08-15 | **grouped** |
| free χ | `chi_free_frobenius` → `chi-{proton,neutron}-h3-at-q0-50dps` | **2026-09-06 03:15** | **borromean** |

The ruling landed 2026-09-05 07:53:55, so the free half is post-ruling and the
atom half is three weeks pre-ruling. **⁵Li's and ⁶Li's `m_e·S` therefore straddle
two braid words inside a single atom's value** — not across atoms, which is what
I described earlier, but within one.

So `anchor_kappa5Li_reproduced` (64.10282) and `li6_amplification_reproduced`
(82.85481) are pinned to **straddled** quantities. They pass today only because
the straddle is itself unchanged.

**Falsifiable prediction, recorded before the answer arrives:** when the Li atom
caches finish regenerating to the borromean word, both will move and both
assertions will FAIL. If they do not move, my account of the mechanism is wrong
and this whole section needs redoing.

## And the A≤4 / A≥5 asymmetry I left "unmeasured" is a two-layer cache

`b47a1b949d`'s own message ended *"Why the quantity is stable for A ≤ 4 and not
A ≥ 5 is unmeasured."* Measured now, and it is not about the physics at all:

    binding-reeb-phase-decomposition.witness.json  computedAt
      on origin/main                               2026-07-06T15:51:08Z
      at b47a1b949d (last session)                 2026-07-06T15:51:08Z
      after this session's re-run                  2026-09-07T13:11:27Z

Two months frozen, through last session's commit. The light atoms (A ≤ 4) read
their per-partition data **from that witness**, so re-running the carrier table
alone could not move them — their input was itself a stale cache. The Li legs
(A ≥ 5) go through `rederive_large_a`, which recomputes from source **every run**
with no intermediate witness, so they picked up drift immediately.

**The general form:** a consumer that reads a witness is insulated from upstream
change; one that recomputes is not. From outside they are indistinguishable —
same script, same invocation, same output shape — and the insulated one is the
dangerous one, because its stability reads as *agreement* rather than as *not
having looked*.

`origin/main`'s carrier witness is itself dated 2026-08-26 with the producers
unchanged since, so main's committed numbers were eleven days stale against
their own inputs before any of this started.


---

## Downstream consequence, from `qou-n5kp` (PR #7161) — a consumer of your 4He regeneration was never re-run

Not a criticism of the regeneration, which is right. Recording where it
landed, because the number a reader sees changed and this bean owns the
input.

`atom-chi-rust-4he.witness.json` was regenerated at `8e52020e64`
(2026-09-07 13:11, this bean). `computations/binding-rotation-phase-lead.witness.json`
was last written at `500e283706` (2026-09-07 11:51, also this bean) — 80
minutes earlier — and reads that chi cache. It was not re-run, so it went
stale the moment the 4He leg moved.

Measured by running the **unmodified** producer from `main` (so this is the
drift alone, not the float64 fix that PR #7161 also lands):

| field | committed at `500e283706` | live inputs |
|---|---:|---:|
| `S1_unweighted.spread_pct` | 528.44 | 1283.29 |
| `S2_dim.spread_pct` | 17254.06 | 402.26 |
| `S3_markov.spread_pct` | 417.02 | 2303.18 |
| **`tightest.aggregation`** | **S3_markov (417 %)** | **S2_dim (402 %)** |

That last row is the probe's own headline — which aggregation gives the
tightest constant binding scale ρ. It names a different aggregation now.

**It is your 4He leg specifically, and the evidence is what did NOT move.**
All four `A3_pair_spread_pct` (T,³He only) and both `DTHe3_spread_*`
(D/T/³He only) reproduce **byte-identically**. Only the *full* spreads — the
ones that include ⁴He — moved. Nothing else in the input cone is implicated.

PR #7161 carries the refreshed witness (it had to re-run the producer to fix
a float64 defect, and the re-run picks the drift up whether or not one wants
it). **No action needed on this bean from my side**; flagging it because the
conclusion moved under a bean that is still `todo`, and whoever finishes the
carrier-table work should know the rotation-phase lead now points at S2_dim.

Two sibling consumers of this producer exist and were NOT re-run or checked
here: `charge_slambda_reeb_phase_crack.py` cites the d0 block's ρ values in
comments, and `he3_tritium_cosh_asymmetry_diagnosis.py` cites
`strong_channel_rho`. Both cite D/T/³He quantities, which are byte-stable,
so they are probably unaffected — but that is an inference from the
byte-identity above, not a measurement of those two files.

## 2026-11-21 (PR #8697)

binding-a3plus-full-theta-assembly and binding-a3plus-joint-ji-combiner re-run on the 2026-09-13 Reeb witness (y_λ unchanged, every Δθ moved). ³He volume-scaled μ₀ |rel_err| 4.9 % → 78.5 %; D 264 % → 19.6 %. Combiner read-check now reads the assembly witness live (was literal 0.7587) and passes.

## 2026-11-21 owner card + #8722

#8697 merged with a scope note: the A≥3 numbers are on atom_braid_word_3A (Borromean intra order, 2026-09-05) whose bond letters the 2026-11-15 γγ ruling supersedes; the old ³He 4.9 % was the grouped word. Comparison arm on the #7741 candidate (nucleon V³, bond V³, two site arms) in #8722: μ₀ |rel_err| 90.8/95.5/95.7/97.0 % (D/T/³He/⁴He) vs production 19.6/82.1/78.5/93.3 %; arms agree to 1e-4; adopts nothing. Real redo waits on #7876.
