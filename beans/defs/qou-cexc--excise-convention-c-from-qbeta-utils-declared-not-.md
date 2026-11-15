---
# qou-cexc
title: 'DONE: excise convention C from qbeta_utils — declared, not silent'
status: completed
type: task
priority: high
created_at: 2026-08-26T05:26:03Z
updated_at: 2026-08-26T05:26:03Z
---

Parent: `qou-cds1`. Owner directive, 2026-08-26: *"do not use convention C
producer. excise"*.

## What "excise" was implemented as, and why not deletion

C cannot simply be deleted: `substrate_ladder_quantities` has **48 in-repo
consumers**, the committed `c_k` artifacts were all computed at C, and the trace
convention registry **deliberately registers the C evaluator** so R9 asserts the
disputed state rather than leaving it undetected. Deleting C would break 13
consumers, orphan every committed number, and take R9's assertion with it.

So C is excised as a DEFAULT, not as a possibility: **nobody can get a C `z`
without naming it**, and every site that wants one is now greppable.

* `substrate_ladder_quantities(q)` returns a guarded mapping. The five
  convention-FREE keys (`h`, `hbar_q`, `b`, `u`, `Q_A_over_me`) are always
  present -- measured, 35 of the 48 consumers use only those and are untouched.
  `z` and `alpha` are the ONLY places a Markov convention enters the whole
  ladder, and they are **withheld** unless the caller passes
  `convention="C"|"D"`. Withheld keys RAISE (with the reason, the alternatives
  and the two governing Lean theorems) rather than returning `None`, and `.get`
  is overridden so a silent `None` cannot reach mpmath arithmetic.
* `markov_parameter` -> `markov_parameter_convention_C`. Value unchanged; only
  the name now says what it is.
* `c3_target_at` gained an explicit `convention="C"` default -- named rather
  than inherited, so its committed targets stay reproducible to the digit.
* The 13 z/alpha consumers now pass `convention="C"` explicitly. They are the
  deliberate comparison arms (several are literally convention-sensitivity
  probes) and their numbers are unchanged BY CONSTRUCTION.

## The registry trap — measured, not assumed

The registry registers this symbol under `evaluators.z` and **R9 calls it BY
NAME**. Renaming without updating the row degrades R9 from
`CONFIRMED convention C by evaluation` to
`WARNING: could not evaluate (AttributeError)` -- and **the validator still
exits 0**, so the lost assertion looks green. Measured: 22 -> 23 warnings.

That is the exact failure the registry's own note warns about ("the exact
failure that took R9 red on main when gram.py migrated and its row did not"),
one step subtler: a rename loses the assertion SILENTLY where a convention flip
would have gone red. Registry row updated; R9 back to
`CONFIRMED convention C by evaluation (|d| = 1.945e-51)`, warnings back to 22.

## Verification

* `convention="C"` is **bit-identical** (`==`, not approx) to the previous
  inline spelling. The two algebraically-equal spellings differ by 1.6e-61 at
  60 dps, so the original was kept verbatim rather than "tidied".
* `convention="D"` gives `alpha_D = -0.040485777340643`, matching qou-cds1's
  independently recorded `-0.040485777340642764919`.
* Ran four consumers end to end (incl. `qstar_anchor_interval_convention_probe`,
  the deepest path, through `c3_target_at`): all exit 0. Across two witnesses,
  59 and 98 non-meta fields compared against HEAD: **the only field that moved
  was `.engineVersion`** (this container's mpmath). Zero mathematical numbers.
* Registry validator PASS, 0 errors, 22 warnings = baseline.
* All 13 changed `.py` files parse.

## Two self-inflicted bugs caught before commit, recorded because both recur

1. An inline `#` comment appended inside a single-line call **swallowed the
   closing paren** -- 12 files broken at once. A syntax sweep caught it; a
   grep-and-eyeball would not have.
2. The same regex rewrote a call name **inside an f-string label**, injecting
   `"C"` into `f"..."` and breaking the quoting.

Both are the cost of a regex edit across many files. The lesson is not "don't
do that" -- it is that the syntax sweep is not optional after one.
