---
# qou-5h5x
title: 'D4: convention-D completion — class B drained, class A (gram.py) documented blocked'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-14T16:21:57Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-cdx1
---

## The question this settles

A prior session stalled asking what "convention D is complete" means, given
that it **cannot literally complete** while `gram.py` is frozen on convention C
(`qou-w8zz`, D1). Owner directive 2026-08-14: **prepmerge PR #4928 as quickly
as possible, bean the rest.** So completion for the PR is:

> **class B drained** (everything reachable by re-running a producer),
> **class A documented and beaned** (the singular-Gram family, which needs a
> design decision, not a sweep).

The PR does **not** wait on class A.

## The measurement that justifies merging

The PR body's stop-line was *"merging now lands `main` half-migrated — some
witnesses D, some C — which is worse than either convention held
consistently."* That premise was **measured and is false**: `main` is *already*
half-migrated on its own, and the branch strictly reduces the split.

Scanned every `computations/**/*.json` (excluding `_deprecated/`) at both refs
with the same detector — fingerprints + `scan_doc` + `scan_doc_symbolic`:

| ref | convention-C witnesses | files scanned |
|---|---|---|
| `origin/main` | **72** | 4173 |
| PR #4928 (post-merge, pre-cascade) | **39** | 4198 |

37 fixed, 4 apparently regressed — and all four (`markov-stab-trace-axis-probe`,
`option-b-h3-h4-bratteli-probe`, `qbeta-c3-per-block-categorical-probe`,
`y-lambda-mpfr-proton`) were cleared by the pass-3 cascade in the same session.

So the honest framing is: **the branch does not create a split, it halves an
existing one.** Holding it makes `main` worse, not better.

## Class A — what is deliberately NOT done, and why

The `ℓ(λ) ≥ 3` blocks are the radical under convention D, so **any object built
over the full block set inherits a null direction**. Three instances, one shape:

1. **`pyhecke/gram.py`** — `G_INV = np.linalg.inv(G)` runs at import; under D
   `det G = 0`. numpy raises nothing and returns garbage
   (`||G G_INV − I|| = 1.64`). Frozen on C **on purpose**, with a 90-line
   banner. `qou-w8zz`.
2. **`tools/hecke-engine/src/gram.rs`** — already D, survives only via the
   pre-2026-05-19 `TR_M[5] = z^3` bug. Coupled to (1). `qou-m7py`.
3. **`aK_via_lp_dual_full`** — LP collapses to the trivial point, `y0* = -0.0`
   on all six atoms. `qou-fu8c`.

In each the live content is the two-row block and the right object is on the
quotient. That is a design decision for the owner, not a mechanical sweep —
which is exactly why it is class A and not part of this PR.

## Residual honesty — the count is a LOWER BOUND

Only **10 of 64** changed witnesses declare a `markov_convention` field. The
detector keys on `y_λ` tables; a convention-dependent quantity that is not a
`y_λ` table (`tr_M`, `z`, and everything derived) is invisible to it, because a
bare trace value looks identical under either convention. Nothing syntactic
fixes that — only producer provenance can. `qou-ng7j`.

So "39" and "72" are both lower bounds of unknown slack. The *comparison*
between them is still sound (same detector, same corpus), which is what the
merge decision rests on.

## Definition of done for this bean

- [ ] `markov_convention` provenance on every witness a producer writes
      (turns the lower bound into a total) — `qou-ng7j`
- [ ] class A resolved: `qou-w8zz` + `qou-m7py` + `qou-fu8c` share one quotient
      construction
- [ ] the 6 remaining orphans (`chi-*-matrix-m`) — need the `hecke-engine` CLI,
      not a Python producer


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

Premise has MOVED but the bean is not closed. Its 'class A (gram.py)
documented blocked' no longer holds -- `pyhecke.gram` is convention D and the
registry's `intra_module_split_waivers` is EMPTY with a note saying the split
is closed. What survives is its definition of 'complete', which is now
answerable. Live, and cheap: re-read it against the registry.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## 2026-10-10: all three done-when items re-measured on `main` `ac111c1814`

§9 of the status doc marked this LIVE-and-cheap because the class-A premise had
moved. It has. Each box below is measured, not read off a sibling bean.

### Class A — **2 of 3 resolved, and `gram.py` resolved HONESTLY**

| item | bean | state |
|---|---|---|
| `pyhecke/gram.py` singular under D | `qou-w8zz` | **`completed`** |
| `hecke-engine/src/gram.rs` `TR_M[5]=z³` bug load-bearing | `qou-m7py` | `todo` |
| `aK_via_lp_dual_full` LP collapses | `qou-fu8c` | **`completed`** |

`gram.py` is now convention D and **`G_INV` is GONE rather than rebound** — read
at the source, lines 19–20 and 107: *"`G_INV` is GONE rather than renamed — under
D the form is singular"*, and *"`G_INV` is left UNDEFINED rather than rebound."*
That is the right resolution and not the one this bean feared: the module does
not compute an inverse from rounding noise and export it, and the one test that
broke is an assertion `G @ G_INV ≈ I`, *"an identity convention D makes FALSE —
the test reporting the mathematics correctly."* The 90-line banner this bean
cites has become a 150-line historical record carrying both conventions'
eigenvalues (C: `−0.855067, +0.101797, +0.855067×3, +3.476950`; D: `−0.752702,
0.000000, +0.752702×3, +4.230339` — the explicit zero is the radical).

So **the only class-A item left is the Rust side**, `qou-m7py`.

### Done-when #1 (`markov_convention` provenance) — 1.3 %, and the field is UNVOCABULARIED

The bean's figure was *"only 10 of 64 changed witnesses declare a
`markov_convention` field"*. Corpus-wide it is far worse, and there is a second
defect the bean does not name. Scanned all **3510** non-`_deprecated`
`computations/**/*.witness.json`:

    declaring markov_convention anywhere : 44  (1.3 %)
    distinct spellings                   : 23   for 4 states
    bare "D"                             : 13

**A free-text field cannot turn a lower bound into a total**, which is what
this bean's done-when asks of it. The 23 spellings include `"D"`,
`"D canonical"`, `"D (z = q^3/(q^2+1))"`, `"D  (z = q^3/(q^2+1))"` (double
space), `"D — the ruled functional, z_D = q^3/(q^2+1)"`, `"D (N = 2)"`,
`"both, compared — D canonical"`, `"n/a (counit only)"` and
`"convention-free — no z is specialised"`.

**And the one live consumer had a latent defect, now fixed.**
`per_observable_100x_status.py` — the L2 dashboard AGENTS.md directs readers to
quote — compared the stamp character-for-character:

    matched = str(conv).strip().upper() == CANONICAL_MARKOV_CONVENTION   # "D"

Measured: **10 of the 11 spellings that MEAN convention D** classified as
`INHERITED_C`, i.e. a correctly-stamped *canonical* artifact reported as
carrying the *excised* convention, on the headline dashboard. It has never
fired wrongly only because the cache it reads carries the bare `"C"`, which the
old check got right — **zero wrong verdicts is not a sound check** (taxonomy row
34). The moment `qou-cds1` lands and that cache is re-stamped with anything
longer than one character, the dashboard calls the ruled result convention C.

Fixed with `_normalise_markov_convention` + `MARKOV_CONVENTION_SPELLINGS` as
fixtures (all 23 measured spellings, 0 FAIL). Deliberately conservative: an
unrecognised spelling returns `"unparsed"`, never `D` and never `C`, so a new
spelling fails loudly. Producer re-run: **every number byte-identical**, the one
payload change being the new `cache_convention_normalised: "C"` field, and the
live verdict correctly unchanged at `INHERITED_C`.

### Done-when #3 (the `chi-*-matrix-m` orphans) — a CATEGORY ERROR, not an orphan set

The box reads *"the 6 remaining orphans (`chi-*-matrix-m`) — need the
`hecke-engine` CLI, not a Python producer"*. Measured: there are **11**, not 6,
and **none of them is a convention orphan**:

    11 chi-*matrix-m witnesses; 11 carry NO markov_convention stamp
                                 0 carry a detectable z value (C or D)

That is correct, because **`χ_λ` is convention-free**. `z` enters the Markov
trace only through the weights — `tr_M = Σ_λ y_λ χ_λ` — so a character matrix
has no Markov-parameter dependence. Confirmed at the producer rather than
inferred: `chi_path_sum_seminormal.py` contains **zero** occurrences of `z`,
`markov`, `ocneanu` or `y_lambda`. The `convention` field these witnesses *do*
carry reads `"sign-only-crossings"` — a **braid-word** convention, a different
axis.

So #3 is not work on the C→D axis at all. Whether these should be produced by
the Rust CLI is a real question; it is not this bean's.

### Where that leaves "complete"

Of the three boxes: **#2 is 2/3 done** (only `qou-m7py` left), **#3 is void on
this axis**, and **#1 is the real remainder** — and it is now a *vocabulary*
problem rather than a coverage one. Coverage without a controlled vocabulary
buys nothing, since the only consumer that reads the field could not parse 10
of 11 D-spellings. Staying `todo` on #1 and #2; `qou-ng7j` carries the
vocabulary half.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8280, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
