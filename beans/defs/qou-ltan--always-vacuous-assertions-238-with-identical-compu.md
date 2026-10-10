---
# qou-ltan
title: 'Always-vacuous assertions: 238 with identical computed==expected, 58 named as claims'
status: completed
type: task
priority: normal
created_at: 2026-08-26T10:14:14Z
updated_at: 2026-08-26T16:16:07Z
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


## Closed 2026-08-26 (PR #5833, commit 2f15bb3c5)

The framing this bean was opened with -- "58 CLAIM-named tautologies, each
needing a judgement call" -- did not survive measurement, in a useful direction.

**The CLAIM/EXEC name-split was the wrong axis.** It is a name regex, and I
flagged going in that it would misclassify. It does, but the deeper problem is
that the name says nothing about whether anything was verified. Two assertions
with identical names can be sound and vacuous respectively, and the
discriminator is three lines up in the source, not in the name.

**None of the 238 is a false claim.** Measured across 3247 producers, three
shapes:

| shape | n | what it is |
|---|---|---|
| ASSERT-BACKED | 64 | verification really ran, in bare `assert`; add_assertion RECORDS the outcome |
| SELF-REPORT | 90 | "probe_completed" -- vacuous, harmless, noise |
| VERDICT-RECORD | 84 | the author's conclusion stated as a passing assertion; nothing tested |

The ASSERT-BACKED discovery is the one that mattered. The `'0'` cluster --
`ksel2_favard`, `ksel2id_friedrichs`, `ksel2id_sw`, `ksel2id_u1`,
`borel_propertime`, `qborel_confluence`, `rep_tightness` -- looked like ~50
hardcoded verdicts across a probe suite. It is a deliberate convention:
`assert` the symbolic residual is exactly 0, then record ("name", "0", "0") on
the path where the asserts survived. Sound. I nearly wrote it up as the worst
finding in the set.

**The real hazard in those 64 is `python -O`**, which deletes assert statements
outright. Under `-O` the entire verification silently vanishes and the witness
still reports `passed: true`. Latent, not live -- nothing in this repo runs
`-O` -- but it means the evidence for 64 assertions lives in interpreter
control flow rather than anywhere a reader or an audit can see it.

**Deliverables:**

1. `always_vacuous_assertion_scan.py` now emits the classification
   (`--shape`, `--has-local`), so this triage is re-derivable rather than a
   list typed once. 37 VERDICT-RECORDs have a boolean-ish local already in
   scope; that is a CANDIDATE flag, explicitly not a verdict, and the docstring
   says why ("a boolean exists in scope" is not "that boolean is what the
   assertion meant" -- the same over-generalisation I made on `qou-569e`).

2. One fixed by hand: `qbeta_per_block_uniform_rule_verify` emitted exactly one
   assertion, `("rule_normalised_y_lambda_holds", 0, 0)`, commented "trivially
   zero by construction". So the witness said allPassed=true while the
   producer's actual finding -- the un-normalised rule FAILS at q0 by ~28% --
   sat unasserted in `data.finding`. `all_match` was right there and already in
   add_data. Now asserted; now fails.

**Deliberately NOT done:** a sweep. 90 are noise not worth touching, 64 are
sound, and the 84 verdict-records each encode a real conclusion that a machine
rewrite would either destroy or silently invert. The scanner is the durable
output; the queue is now readable by shape.

**Follow-on worth someone's time:** decide whether ASSERT-BACKED should be
migrated to a form the witness can show (e.g. record the residual rather than
"0"), which would close the `-O` hazard and make 64 verifications visible.
Not opened as a bean -- it is a convention change across a probe suite and
should be an owner call, not an agent sweep.
