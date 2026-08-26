---
# qou-ltan
title: 'Always-vacuous assertions: 238 with identical computed==expected, 58 named as claims'
status: todo
type: task
priority: normal
created_at: 2026-08-26T10:14:14Z
updated_at: 2026-08-26T10:14:57Z
---

## The shape

    builder.add_assertion(
        "crystal_pole_counter_well_defined",
        computed=len(results),
        expected=len(results),      # <- THE SAME EXPRESSION
    )

This cannot fail. Not "cannot fail when a collection is empty" -- cannot fail
for any data, ever. It is the compute-side `theorem X : X = X := rfl`, which
AGENTS.md bans outright in Lean: *"Tautological conclusions are banned: X = X
:= rfl ... any proposition that is provable without using any hypothesis about
the mathematical objects in question."* There is no equivalent rule, and was no
checker, for the Python side.

It is a strictly stronger defect than `qou-cm7l`, which needs a zero count to
become vacuous. This one is vacuous on arrival.

## Measured, 2026-08-26

Scanner: `computations/audits/always_vacuous_assertion_scan.py`. AST over the
3227 tracked producers, normalised through `_source_normalise.code_only`, so a
docstring cannot match. Flags `add_assertion(computed=X, expected=Y)` where
`ast.dump(X) == ast.dump(Y)`.

    3227   producers scanned
     238   assertions where computed and expected are the SAME expression

**238 is not 238 defects.** Split by whether the assertion's NAME states a
proposition or merely records that something ran:

      58   CLAIM        the name asserts something; the body is a tautology
      71   EXEC-MARKER  the name says "executed"/"completed"; honest about itself
     109   OTHER        neither pattern matched

Worked examples of the 58:

| assertion name | body |
|---|---|
| `hecke_quadratic_verified_symbolically` | `1 == 1` |
| `crystal_pole_counter_well_defined` | `len(results) == len(results)` |
| `R_alg_is_algebraic` | `1 == 1` |
| `unknot_is_1` | `1.0 == 1.0` |
| `no_placeholder_literals_consumed` | `True == True` |
| `correction_tower_converges` | `1 == 1` |
| `edge_set_is_max_contact_packing` | `'1' == '1'` |
| `no_flat_torus_object_meets_all_three_axes` | `0.0 == 0.0` |

Each records `passed: true` in its witness. A reader -- or an audit -- sees a
verified claim where nothing was tested.

## Three caveats, all load-bearing

1. **The CLAIM/EXEC split is a name REGEX and will misclassify.** It is a
   triage aid, not a verdict. Each of the 58 needs a human read before being
   called a defect.
2. **A tautological assertion does not mean the VALUE is wrong.** Often the
   quantity was computed correctly and then recorded through an assertion that
   happens to compare it with itself -- e.g.
   `no_derived_scalar_f_closes_A3` is `round(best_maxabs, 0) == round(best_maxabs, 0)`,
   where `best_maxabs` is genuinely computed. The defect is that the assertion
   tests nothing, not that the number is false. Do not "fix" these by changing
   numbers.
3. **Some of the 71 EXEC-MARKERs are defensible.** Recording "this gate ran" is
   legitimate provenance. What is not legitimate is that it lands in the
   witness as a *passed assertion*, indistinguishable from a real one. That is
   a schema question (a `recorded` kind distinct from `assertion`), not a
   per-producer fix.

## Relationship to the sibling beans

* `qou-cm7l` -- vacuous only when a count is zero. 16 hits (see the correction
  below). Weaker; needs a trigger.
* `qou-ltan` (this) -- vacuous always. 238 hits, 58 name-claiming. Stronger; no
  trigger needed.
* `qou-poi1` -- the ratchet blind spot that surfaced both, by making me run a
  producer nobody had run.

## Correction to qou-cm7l's count, from broadening its scanner

`qou-cm7l` reported **9** hits. Its detector required BOTH sides to be plain
`Name` nodes, so it missed `computed=len(rows)` -- an empty collection is 0 just
as surely as an unincremented counter is. Found while reading an insertion
point: `all_nuclides_wedderburn_spectral_v2` carries **two** vacuous-at-zero
assertions and only one was reported.

Broadened to accept `len(<anything>)` on either side: **16 hits, not 9.** Seven
were invisible. Quote 16.

## NOT attempted here

Fixing any of the 58. That is 58 files, each needing a judgement call about
whether the tautology is harmless provenance or a false claim, and it is not
the scope of the pin-migration PR that surfaced it.
