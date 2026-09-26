---
# qou-vfy1
title: 221 blocks assert computation.status "verified"; 64 are not supported by the witness they cite
status: in-progress
type: task
priority: normal
created_at: 2026-08-22T05:20:00Z
updated_at: 2026-08-23T20:44:21Z
---

The quantified form of class **C2** in the `qou-3nva` ledger — a block and
its witness disagreeing, with the block winning. Measured corpus-wide
2026-08-22.

## Two findings, one scan

**1. ~~The `status` field should not be in a `.ts` at all.~~ RETRACTED
2026-08-22 — see the correction section at the end. The §4 count is **1**, not
278.** What the scan actually found is **277** `.ts` carrying a `status:` key,
of which **276 sit inside `computation: { … }`** — a field describing the
computation, which §4 does not govern. Finding 2 below is unaffected and is
the real content of this bean.

| value | count |
|---|---:|
| `verified` | 221 |
| `experimental` | 52 |
| `not_run` | 4 |
| `pending` | 1 |

**2. Of the 221 `verified` claims, 64 (29 %) are not supported by the
witness they name.**

| | count |
|---|---:|
| witness `allPassed: true` **with real assertions** | 157 |
| witness `allPassed: true` but **assertions array is empty** (vacuous) | **43** |
| witness reports **`allPassed: false`** | **8** |
| cited witness **missing or unreadable** | 5 |
| **no witness cited at all** | 8 |

The 43 vacuous ones are the interesting bulk: `allPassed: true` over zero
assertions is *true* and means nothing, and it is what a block points at
when it says "verified". Related but distinct from the ~383-witness bean on
the same shape — that one is about the witnesses; this is about the blocks
that **cite them as verification**.

## Limits of the measurement, stated

- **The 157 is an upper bound on genuine support.** Passing assertions do
  not imply the assertions *cover the block's claim*. The campaign found
  several where they do not — one witness's assertions covered clause (1)
  of a three-clause proposition; another's two assertions were both about
  vanishing while the block was cited for a field-membership sentence.
- **The 5 "missing" may over-count**: witness paths were resolved with a
  basename fallback under `computations/`, which will miss anything stored
  elsewhere.
- The scan reads the **first** `status` and the **first** witness path in
  each file.

Reproduce: the script is inline in the session; the shape is
`grep '^\s*status:\s*"' content/**/*.ts` joined against the first
`*.witness.json` named in the same file.

## What would close this

The systemic fix and the cleanup are the same act: **delete the field.**
§4 already says status is derived at build time from the Lean and the
witness, so a `.ts` asserting `verified` is both forbidden and structurally
incapable of being wrong — nothing checks it against the thing it claims.
Removing it makes the 64 unsupported claims disappear by construction,
because the derived status would read the witness.

If the field is kept for any reason, it needs a checker that fails when a
block claims `verified` while its witness is absent, failing, or vacuous —
which is the 64.

Order of work, cheapest first:

1. The **8 blocks citing a witness that reports `allPassed: false`** — a
   direct contradiction, and the smallest set.
2. The **8 with no witness at all** and the **5 unresolvable** — either the
   citation is wrong or the claim is unbacked.
3. The **43 vacuous** — these need the witness fixed (assertions added) or
   the block's claim withdrawn; they are not fixable from the block side.
4. The field's removal corpus-wide, per §4.


## The 21 non-vacuous cases, enumerated (2026-08-22)

The 43 vacuous-witness blocks need the witness fixed, not the block, so
they are left for a separate pass. These 21 are actionable from the block
side. **Correction to the original scan:** it resolved witness paths by
basename under `computations/` only, so it reported 5 "unresolvable" —
**all five actually resolve**, three of them somewhere other than where the
block says. That over-count is now fixed below.

### A. Block says `verified`; witness says `allPassed: false` (8)

| block | witness | failing assertions |
|---|---|---|
| `hadron-level-knot-table` | `hadron-knot-table` | **6** — `LP_stable(c14)`, `LP_stable(o16)`, `LP_stable(ne20)`, … |
| `he4-two-row-dominance` | `he4-canonical-tr-m-block-fingerprint` | **9** — `tr_M_at_q0`, `top5_cumulative_pct`, `trivial_rep_pct`, … |
| `gs-graded-markov-trace-existence` | `markov/markov-pipeline-cross-validation` | **3** — `tr_M_at_q0_archimedean[n]`, `[p]`, `no_atoms_only_in_term6` |
| `mba-sidecar-mirror-cancellation` | `delta-lambda-z-coefficient-and-slope` | 1 — `slope_10A5_refuted_at_A_ge_5` |
| `binding-qbeta-complex-volume` | `qbeta/qbeta-ck-sseries-operator-match` | 1 — `c2_gate` |
| `q-beta-c-2-eq-neg-one-structural` | `qbeta/qbeta-symbolic-chain-alpha-b` | 1 — `alpha_q0_matches_probe_n3_witness` |
| `y-lambda-cyclotomic-factorization` | `probes/y-lambda-cyclotomic-factorization-probe` | 1 — `denominator_factors_as_cyclotomic_product` |
| `deuteron-fusion-frame` | `substrate/deuteron-tower-fusion-frame-probe` | **0** — `allPassed: false` with an empty failing set |

The last is its own oddity and is already beaned separately (`D3`:
"exits 0 while allPassed is False"). The first three are the substantive
ones: a stability table whose witness reports six instabilities, and a
"two-row dominance" claim whose witness fails on the very quantities the
dominance is about.

Note what the three `c_k`/`α`-related rows have in common: each fails a
**gate** assertion — `c2_gate`, `alpha_q0_matches_probe_n3_witness`,
`slope_…_refuted_at_A_ge_5`. The gates are doing their job and the blocks
are ignoring them.

### B. Block says `verified`; cites no witness at all (8)

`mba-sidecar-delta-lambda-closure`, `mba-sidecar-lp-sdp-dual-emission`,
`mba-sidecar-witness-json-pipeline`, `mba-step01-categorical-action`,
`mba-step06-frobenius-pairing`, `qbeta-toroidal-harmonics-basis`,
`frakD-energy-decomposition`, `toroidal-harmonics-delta-lambda`.

Five of the eight are `mba-*` appendix blocks — the maintenance-contract
appendix, where an unbacked `verified` is worse than elsewhere because the
appendix exists to bind propositions to the compute. Independently,
`agent:l01` found `mba-step06`'s cited API (`pyhecke.check_frobenius`)
checks Frobenius *positivity*, not the pairing the block describes, and
`agent:h00`/`i00` flagged `toroidal-harmonics-delta-lambda` as
convention-C-dependent.

### C. Block says `verified`; the cited path is wrong (5 — all resolve elsewhere)

| block | cites | actually at |
|---|---|---|
| `per-braid-mass-tower` | `docs/audits/2026-05-01-per-braid-tower.witness.json` | **exists as cited** (`allPassed: true`, 3 assertions) |
| `wedderburn-weight-canonical` | `docs/audits/2026-05-01-p1-3a-bw-equivalence.witness.json` | **exists as cited** (`allPassed: true`, 2 assertions) |
| `markov-trace-recursive-reducer` | `markov-trace-axiomatic-multi-atom.witness.json` | `computations/**markov/**…` |
| `rho-k-graded-expansion` | `rho-k-markov-multiplicativity.witness.json` | `computations/**_deprecated/**…` |
| `he4-channel-active-set` | `magic-shell-empirical-instantiation.witness.json` | `computations/**_deprecated/**…` |

The first two are **my scan's false positives** — witnesses under
`docs/audits/` that my basename-under-`computations/` fallback could not
see. Recorded so the count is not repeated as 5.

The last two are the real finding in this group: a `verified` block whose
evidence lives under **`_deprecated/`**. That is the same shape
`agent:g01` found citing `confinement-lp.witness.json`, and
`agent:k00` found citing a `_deprecated/` witness at the old muon pin.

### Revised totals

| | |
|---|---:|
| assert `verified` | 221 |
| **contradicted by their own witness** | **8** |
| **no witness at all** | **8** |
| **witness path wrong; 2 of those resolve as written** | 3 real + 2 false positives |
| witness `allPassed: true` over an empty assertions array | 43 |
| passing with real assertions (upper bound — coverage unchecked) | 157 |

So **62** of 221, not 64.

---

## CORRECTION (2026-08-22) — finding 1 was wrong by a factor of ~278

I wrote *"**278** content-block `.ts` files carry"* a §4-forbidden `status`
field. Re-measured by **indentation and parent key** rather than by grepping
the token:

```
3584  .ts scanned under content/quantum-observable-universe/
 277  carry a `status:` key
 276  at 4-space indent, ALL of them inside `computation: { … }`
   1  at block level  ->  mass-endomorphism/qbeta-toroidal-harmonics-basis.ts:13
```

**`computation.status` is not the field §4 forbids.** §4 governs *formalization
status* — the thing derived at build time into `proof-objects.json`. Two
independent checks agree that these are different fields:

1. **Nesting.** All 276 are a key of the `computation` object, not of the block.
2. **Vocabulary.** §4 names the formalization values explicitly:
   `not_started`, `stated`, `has_sorry`, `proved`, `mathlib_ok`. The observed
   values are `verified` / `experimental` / `not_run` / `pending` — a
   **disjoint** set. These describe whether the *computation* was run, not
   whether the *Lean* was proved.

So the §4 violation is a single file — and that file is one of the three whose
manifest does not load at all (it imports `../../ontologist`, which does not
exist), so it is already covered by the manifest-loading work in #5367.

**Finding 2 stands unchanged and is the whole value of this bean.** Whether
`computation.status: "verified"` is *honest* is a real and separate question
from whether the key is allowed, and the answer is that 64 of 221 are not
supported by the witness they name. Two sibling batches hit the same class
independently from the other end: `universal-ilp-algorithm` and the
`lp-dual-stability` family each record `verified` against witnesses whose
assertion arrays are empty, whose `expected` equals `computed` as the same
literal string, or whose LP-dual fields are all `null` with a STUB note.

**Why the error happened, since it is the campaign's own recurring shape.** I
counted a *token* and reported it as a *claim*: "a `.ts` has a `status` field"
is not "a `.ts` has the field §4 forbids". That is the `da-arity-conflation`
failure AGENTS.md §"Grep the claim SHAPE, not only the topic" describes —
resolve the symbol and check what object it belongs to before asserting a rule
is violated. One `grep -c` looked like evidence; one indentation histogram was
the actual check.

## 2026-08-22 — group A verified at the source; two of the eight opened

Opened the witnesses rather than re-reading the scan. Both substantive rows
hold, and one is worse than the table says.

**`hadron-level-knot-table`.** Confirmed exactly:
`computations/hadron-knot-table.witness.json` is `allPassed: false`, 23
assertions, **6 failing** — `LP_stable(c14)`, `(o16)`, `(ne20)`, `(si28)`,
`(ca40)`, `(fe56)`, each `computed=0 expected=1 tolerance=0`. Boolean gates at
zero tolerance, so there is no rounding story: the witness states that six
nuclei are **not** LP-stable while the block records `verified`.

**`he4-two-row-dominance` — the number the block calls witness-verified is the
number the witness refutes.** 12 assertions, **9 failing**:

| assertion | witness computed | block/expected |
|---|---:|---:|
| `top5_cumulative_pct` | **91.13** | 86.5 |
| `tr_M_at_q0` | **0.16097415** | 0.05534835 |
| `trivial_rep_pct` | 5.96 | 2.9 |
| `pct_block_11_1` | 14.24 | 10.2 |
| `pct_block_10_2` | 15.41 | 13.5 |

The `.ts` says *"Empirically (witness): the ratio is **86.6 %**"* and *"the
witness-verified 86.6 % figure"*. 86.6 is the **expected** value of a failing
assertion; the witness's own computed value is 91.13. And `tr_M_at_q0` is off by
a factor of 2.9 — that is a different quantity, not drift.

**Why this one is load-bearing rather than a stale number.** The block's
authorNote records that the Lean follows §3b-cond: the 86.6 % figure is encoded
as a class `HasHe4TwoRowDominance` whose only `sorry` is the empirical instance,
and downstream propositions take it as a `[HasHe4TwoRowDominance]` hypothesis.
So a conditional-class chain is anchored on a premise its own witness marks
failed. Per AGENTS.md §"Conditional-proved ≠ premise-established", the
implication is fine and the premise is not established — here it is actively
contradicted.

**A hazard for anyone re-running this scan.** Two witnesses share the basename
`he4-canonical-tr-m-block-fingerprint.witness.json` — one live, one under
`computations/_deprecated/`. The deprecated copy is `allPassed: true` with
**zero** assertions. A basename-resolving scan that takes the first match can
therefore report this block as *vacuously verified* instead of *nine failures*,
which is the opposite conclusion. I hit exactly that and caught it only by
checking for a second copy; the live path is the one the block cites.

**Not fixed here.** Both need a decision that is not the block's to make: re-run
the producer and see whether the new numbers stand, or withdraw the claim. For
`he4` the choice also governs whether the Lean class keeps its instance.

## 2026-08-22 — all 8 of group A opened. They are three different problems, not one.

The table above reads as eight instances of *"the block ignores a failing
gate"*. Opening each witness at **the path the block actually cites**, they
split three ways, and the disposition differs per class.

### (a) A boolean gate genuinely failed — 6 blocks, substantive

| block | failing assertion | computed → expected |
|---|---|---|
| `hadron-level-knot-table` | `LP_stable(c14 / o16 / ne20 / si28 / ca40 / fe56)` | `0 → 1`, tol **0** |
| `gs-graded-markov-trace-existence` | `no_atoms_only_in_term6` | `1 → 0` |
| `binding-qbeta-complex-volume` | `c2_gate` | `0 → 1`, tol **0** |
| `mba-sidecar-mirror-cancellation` | `slope_10A5_refuted_at_A_ge_5` | `False → True` |
| `y-lambda-cyclotomic-factorization` | `denominator_factors_as_cyclotomic_product` | `3.0 → 0.0` |
| `deuteron-fusion-frame` | `z_canonical_equals_pyhecke_gram_z` | `false → true` |

Zero tolerance on booleans, so there is no rounding story for any of them.

`deuteron-fusion-frame` is the sharpest: the witness's own `verdict` string reads
*"the bond factor z **IS** the corpus Markov-trace parameter (pyhecke.gram z =
1/[2]_v at v = sqrt(q0), **checked live**)"* while the assertion beside it says
that equality is **false**. Prose and assertion in the same file, opposite
directions. Plausibly the convention-C/D Gram question already tracked in
`qou-cds2` — worth joining up rather than triaging alone.

### (b) Tight-tolerance precision failures — not wrong numbers

`gs-graded-markov-trace-existence`, the other two of its three:

```
tr_M_at_q0_archimedean[n]  computed 0.9232332971861534  expected 0.9232332299116376
tr_M_at_q0_archimedean[p]  computed 1.0653062286131670  expected 1.0653061442544502
                           relative tolerance 1e-9
```

These agree to **8 significant figures** and fail a 9-digit gate. That is *"the
pipeline agrees to 8 digits and the gate wanted 9"*, which is a different
finding from a claim being unsupported and needs a different fix — tighten the
pipeline or loosen a gate that was set past what the method delivers. Do not
lump these with (a).

### (c) A gate that may be mis-specified rather than failed

`q-beta-c-2-eq-neg-one-structural`:

```
alpha_q0_matches_probe_n3_witness  computed 5.8235661443920095e-09
                                   expected 0.0   tolerance 1e-30
```

A `1e-30` tolerance on a quantity that lands at `5.8e-9`: nothing short of exact
symbolic agreement passes that gate. Before recording this block as making an
unsupported claim, someone has to say whether `1e-30` was intended — the honest
reading may be that the **gate** is wrong, not the block.

### Schema note for anyone re-running this

`assertions` is **not one shape**. Most witnesses carry a *list of objects*
(`{name, computed, expected, passed, tolerance}`); `deuteron-tower-fusion-frame-probe`
carries a *dict of name → bool*. The original scan assumed the list form, which
is why the table above recorded that block as *"`allPassed: false` with an empty
failing set"* — it is actually **1 of 7 failing**. Any tool reading assertions
must handle both shapes.

### Net

Group A is **6 substantive**, **2 precision-gate**, **1 possible gate defect**
(overlapping: `gs-graded` appears in both (a) and (b)). Still nothing fixed —
every one ends at the same question, *is the witness stale or is the claim
wrong*, and that is a math call.

## 2026-08-22 — the vacuous class re-measured, and it is not a block problem

Re-scanned with both assertion shapes handled. Of blocks that carry
`status: "verified"` **and** cite a witness:

```
96  witness allPassed true, WITH assertions
36  witness allPassed true, ZERO assertions   <- the vacuous class
 8  witness allPassed FALSE                   <- group A, opened above
```

**36, not the 43 recorded earlier.** I expected the difference to be the
dict-shape bug that cost us the `deuteron` row — it is not: all 36 are
list-shaped and genuinely empty. The gap is scan scope, and the 36 is the
figure to use.

**They are 36 blocks over 29 witnesses**, so not 36 independent problems;
`gram-matrix-dual.witness.json` alone backs three.

### The reframing: assertion-free is the corpus baseline, not an anomaly

Measured over every live witness under `computations/` (2,700, excluding
`_deprecated`):

| assertions field | count | share |
|---|---:|---:|
| non-empty list | 1749 | 64.8 % |
| **no `assertions` field** | **521** | **19.3 %** |
| **empty list** | **386** | **14.3 %** |
| dict | 44 | 1.6 % |

**907 of 2,700 (33.6 %) carry no assertions at all.** So "the cited witness
asserts nothing" is not a property of 36 bad blocks — a third of the witness
corpus is *descriptive*, recording computed values rather than checking them.
That is a legitimate thing for a witness to be. The defect is reading
`allPassed` as verification.

### The actual defect, and the corpus already contains its fix

Split those 907 by what they claim:

```
515  allPassed = null   <- honest: no assertions, so no verdict
392  allPassed = true   <- vacuously true over an empty set
```

**Both behaviours ship from the same corpus.** 515 producers decline to claim a
pass when they have nothing to check; 392 emit `true`, which is logically
correct (everything holds of the empty set) and is a false signal to every
consumer that reads `allPassed` as "verified". The 515 are the evidence that
`true` here is a defect rather than a convention — the honest encoding is
already the majority behaviour.

### What this changes about the disposition

The earlier note said the 43 *"need the witness fixed (assertions added) or the
block's claim withdrawn; they are not fixable from the block side"*. Adding
assertions to 29 producers is real work and may not be wanted at all — a
descriptive witness is fine. The cheaper and more general fix is upstream:

**`WitnessBuilder` should emit `allPassed: null`, not `true`, when the assertion
set is empty.** That is a one-line producer-side change matching what 515
witnesses already do, and it converts 392 silent false-positives into an honest
absence of verdict — including the 36 blocks here, without touching any of them.

Only after that is it worth asking, per block, whether a `verified` status
pointing at a deliberately-descriptive witness should say something else.

## 2026-08-22 — I traced the one-liner. It is real, it is already known, and it is NOT safe as I proposed it.

Three corrections to the note above, in increasing order of importance.

### 1. The mechanism, located

[`witness.py:1225`](../tools/qou-substrate/python/qou_substrate/witness.py):

```python
all_passed = all(a.passed for a in self.assertions)
```

`all([])` is `True`. A producer that registers no assertions therefore gets
`allPassed: true` from `build()`. That is the 392.

### 2. The corpus already diagnosed this — I re-derived a known number

`witness.py:1073-1088` carries a comment describing exactly this shape, and
[`test_wrap_legacy_assertions.py`](../tools/qou-substrate/tests/test_wrap_legacy_assertions.py)
is a regression test for it. Their recorded measurement:

> *389 of 2083 witnesses carrying an `allPassed` field (19 %) had it true with
> zero assertions.*

Mine, measured independently today: **392 of 2162 (18 %)**. The same defect, three
witnesses later. I should not have presented this as a new finding — it is a
confirmation, and the credit belongs to whoever wrote that comment.

**What their fix did and did not cover.** It repaired `wrap_legacy` *discarding*
payload assertions — 28 producers whose checks were being thrown away, so that
"a probe whose headline check FAILED reported success". That is a different and
worse bug, and it is fixed. It does **not** touch the case where a producer
genuinely has nothing to assert, which still yields `true` at line 1225.

### 3. The fix I proposed would break consumers — do not apply it as stated

I wrote that `WitnessBuilder` "should emit `allPassed: null`, not `true`". The
one-line change is real, but at least a dozen producers do this:

```python
wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
return 0 if wit["allPassed"] else 1
```

`if None` is **falsy**, so `null` would turn every assertion-free probe into a
non-zero exit — converting a silent false-positive into a loud false-negative.
That is not an improvement.

Note also that those producers compute `allPassed` themselves rather than going
through the builder, so they **reproduce the same `all([])` bug outside it**: a
builder-only change does not reach them.

**What is actually needed**, then, is not one line but a small scoped change:

- keep `allPassed` a bool so truthiness consumers are unaffected, and add an
  explicit `assertionCount` (or `verdict: "descriptive"`) that a consumer can
  check — the signal is what is missing, not the field; **or**
- emit `null` *and* audit the ~dozen hand-rolled `return 0 if … else 1` sites
  first, which is a flag day rather than a one-liner.

Either way it is a witness-schema decision with a measured blast radius, which
is where I am stopping. The value delivered here is that the blast radius is now
known and the earlier recommendation is withdrawn before anyone acted on it.


---

## 2026-08-23 — the checker this bean asks for now exists; 41 unbacked, listed

> "If the field is kept for any reason, it needs a checker that fails when a
> block claims `verified` while its witness is absent, failing, or vacuous —
> which is the 64."

`scripts/check-computation-status.py` now does all three. Step 1 of this bean's
own order-of-work — the **8 blocks citing a witness that reports
`allPassed: false`** — is **DONE**: that class was drained under `qou-bm4i`
(it had grown to 12), and the corpus now reports **0 disagreements across 398
block/witness pairs**.

### Why consumer-side, and why the withdrawn fix stays withdrawn

This bean already established that making `WitnessBuilder` emit
`allPassed: null` is a flag day, not a one-liner: ~a dozen producers hand-roll
`return 0 if wit["allPassed"] else 1`, and `None` is falsy, so it converts a
silent false positive into a loud false negative. That withdrawal stands.

The checker instead reads `len(assertions)` directly. **No schema change, no
producer change, no blast radius** — which is this bean's own preferred framing,
*"the signal is what is missing, not the field"*, implemented on the side that
needs no negotiation.

### Measured now: 41 unbacked (vfy1 measured 43)

The difference is a deliberate refinement, not drift: a block that pairs a
vacuous witness **with** an asserting one is not unbacked, and is no longer
counted. Classification spot-checked on three — `allPassed: true`,
`assertions: []` in each.

Also surfaced: **40** cited witnesses carry no top-level `allPassed` at all.
Counted, not failed — a data-only witness is often legitimate.

`--strict` keeps its original meaning (contradictions only) so existing callers
are unaffected; `--strict-unbacked` is opt-in and covers both. Verified:
`--strict` exits 0, `--strict-unbacked` exits 1.

### The 41, for whoever works them

    alg:bring-brane                            prop:cyclotomic-cl3-orbit-sum-general
    alg:delta-lambda-closure                   prop:cyclotomic-depth3-dimension-synthesis
    alg:gb-filtration                          prop:cyclotomic-l-value-decomposition
    alg:jet-prefix-transport                   prop:cyclotomic-orbit-sum-all-depths
    alg:q-beta-truncation                      prop:cyclotomic-trilog-imaginary-closed-form
    conj:borromean-baryon-mass-formula         prop:delta-max-numerical-scale
    conj:bring-figure-eight-depth-2-witness    prop:delta-max-uniform-bound
    conj:bring-trilog-depth-3-witness          prop:e-infinity-page-identifications
    conj:gs-archimedean-agreement-residue      prop:hecke-mass-trace
    conj:gs-residue-at-root-existence          prop:joint-tower-sdp-confinement
    conj:kashaev-density-equals-sdp-multiplicity  prop:jonquiere-cyclotomic-tate-rationality
    def:markov-axiom-recursive-ascent          prop:markov-pair-z2
    def:wenzl-A-operator                       prop:operator-valued-combiner-convergence
    lem:frobenius-cocasimir-refuted-deuteron   prop:q-beta-spectral-bridge
    prop:binding-scale-catalan                 prop:q-rogers-pentagon-archimedean
    prop:bring-trilog-imaginary-tate-rational  prop:s4-s3-half-symmetric-projection
    prop:categorical-mass-markov               prop:schur-weyl-mass-decomposition
    prop:cl3-zeta5-orbit-sum-identity          prop:wigner-np-pairing
    prop:cl3-zeta5-pslq-independence           rem:figure-8-muon-mass-cross-check
    prop:crossed-module-euler-characteristic   rem:recursive-atom-knot-atlas-registry
                                               thm:six-term-mass-formula-complete

### Note on what "fixing" these means — it is not a re-run

A contradicted block is fixed by correcting the status or the compute. An
**unfalsifiable** one cannot be fixed by re-running anything: its producer has
to grow a real assertion, or the `verified` claim has to come down. Those are
per-block authoring decisions, 41 of them, and none are made here.

One caution carried over from the qou-bm4i drain, because it applies with more
force to this list: **four of those twelve correctly ended at `failed`.** Do not
work this list as a red-to-green exercise. `lem:frobenius-cocasimir-refuted-deuteron`
has "refuted" in its label; several of the `conj:` entries are open problems.
For a good number of these the honest outcome is a status demotion, not a new
assertion.
