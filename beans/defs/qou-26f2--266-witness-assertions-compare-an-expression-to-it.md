---
# qou-26f2
title: 266 witness assertions compare an expression to itself and pass by construction
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T23:58:15Z
updated_at: 2026-10-04T15:11:44Z
parent: qou-5vkl
---


Found 2026-08-24 while resolving `qou-v5fp`, which had flagged
`computations/universal-ilp.witness.json` as "self-certifying — its assertions
compare the script to its own `expected` values". That description was too
generous, and the shape is not local to that producer.

## The measurement

`scripts/tautological-assertion-census.py` (added with this bean). AST, not
regex: parse every `.py` under `computations/`, `scripts/`, `tools/`, find each
`add_assertion` call, and compare the `computed` and `expected` argument ASTs
with `ast.dump`. Identical dump = the assertion holds by construction.

    files parsed          3,253   (0 unparseable)
    add_assertion calls   3,482
    TAUTOLOGICAL            266   (7.6%), across 195 files

Shape of the 266:

| both sides are | count |
|---|---|
| numeric literal | 78 |
| string literal | 76 |
| literal True/False | 44 |
| call on a computed value | 41 |
| computed variable / subscript | 27 |

The literal cases are the clearest: `add_assertion("kernel_ran", computed=1,
expected=1)` asserts `1 == 1`. The computed-variable cases are the most
misleading, because they look like real checks —
`hadron_knot_table.py:257` reads `computed=r["tr_M"], expected=r["tr_M"]` with
`source="hecke_core.build_atom_nf -> nf_tr"`, i.e. it advertises a check of the
Markov trace against a named producer and compares the value to itself.

## Why it matters

`allPassed: true` is what `computation.status: "verified"` rests on. Where the
assertions are tautological, `verified` means the script ran, not that anything
it produced was checked. 215 blocks in this corpus carry
`status: "verified"`.

## What was done here, and what was NOT

Fixed exactly one site, `computations/universal-ilp.py`, as part of `qou-v5fp`.
Its block `def:universal-ilp-algorithm` is demoted to `status: "failed"`.

**That repair is not a template.** It happened to be a case where no honest
`expected` exists yet — which operator each level should select is open — so
the fix was to assert a different, independent property (the reported label
re-parses to its own crossing count). Most of the other 265 will be ordinary
mis-wiring where a real expected value exists and was simply not passed, and
those want the value, not a substitute assertion.

Two traps worth stating, both hit while fixing the one:

1. **Longer tautologies.** "Assert the selection is Frobenius-feasible" and
   "assert it is minimum-crossing among feasible" both looked like real checks
   and are true by construction — `universal_ilp` scans crossing number upward
   and takes the first feasible candidate. Re-running the selection rule
   against itself is the same defect spelled out.
2. **Hardcoding a disputed value.** Tempting and wrong where the corpus's own
   claim is under review.

## Suggested disposition

- [ ] Triage the 266 by shape. The literal-vs-literal ones are
      mechanical; the computed-variable ones need a reading each.
- [ ] Decide whether `witness_base.WitnessBuilder.add_assertion` should
      **refuse** structurally-identical arguments outright. It cannot see the
      AST at runtime, but it can compare values and flag the common case where
      a caller passes the same object twice.
- [ ] A `folio-assistant` QA criterion is the durable fix — this is the same
      family as `lean-no-vacuous-instance-data` and
      `lean-no-definitional-laundering`, one language over. Not created yet.

## Caveat on the count

266 is exact for the rule "same AST for `computed` and `expected`". It
is a **lower** bound on assertions that check nothing: a call passing two
different expressions that happen to evaluate to the same thing by
construction — `expected=len(xs)` beside `computed=len(list(xs))` — is not
counted and is just as vacuous. Re-run the census rather than quoting this
number after the corpus moves.


---

## Drain started 2026-08-25 — triaged by IMPACT, not by count

Draining 266 sites in file order would spend most of the effort on probe
scripts nothing cites. Cross-referenced the 195 files against every content
block's `computation.script` instead:

    195 files carry tautologies
     14 of them back a content block at all
     10 of those back a block claiming `status: "verified"`

**Those 10 are the drain.** Everywhere else the tautology is a defect in a
probe; here it is a defect in a *claim*, because `verified` on the block rests
on `allPassed: true` from an assertion that cannot fail.

| taut | block | producer |
|---|---|---|
| 4 | `conj:schwinger-measure-computational-time` | `probes/r2core_schwinger_measure_explore_probe.py` |
| 3 | `thm:topological-mass` | `mass-from-q-symbolic.py` |
| 2 | `prop:confinement-nf-partial-proof` | `shift_from_nf_basis.py` |
| 1 | `conj:staircase-ew-residual` | `staircase_ew_residual_conjecture.py` |
| 1 | `prop:t-beta-markov-frobenius-collapse` | `qbeta/qbeta_markov_trace_norm_probe.py` |
| 1 | `rem:knot-operator-basis-table` | `photon_operator_table.py` |
| 1 | `rem:per-observable-100x-status-dashboard` | `per_observable_100x_status.py` |
| 1 | `conj:flavor-split-habiro-derivation` | `mn_flavor_split_h4_plancherel.py` |
| 1 | `rem:hecke-operations` | `basis_knot_tables.py` |
| 1 | `prop:bar-involution-invariance` | `audits/brundan_kleshchev_audit.py` |

Progress is checked off below as each lands. The remaining ~250 sites stay open
and are *not* urgent by the same argument: no block's status depends on them.

- [x] `conj:schwinger-measure-computational-time` (4)
- [x] `thm:topological-mass` (3)
- [x] `prop:confinement-nf-partial-proof` (2)
- [x] `conj:staircase-ew-residual`
- [x] `prop:t-beta-markov-frobenius-collapse`
- [x] `rem:knot-operator-basis-table`
- [x] `rem:per-observable-100x-status-dashboard`
- [x] `conj:flavor-split-habiro-derivation`
- [x] `rem:hecke-operations`
- [x] `prop:bar-involution-invariance`
- [ ] the ~250 with no block dependency — bulk, low priority

## Checker landed

`assertions_are_falsifiable` is live in folio-assistant
(`content/pipeline/qa-checkers-python.ts`, registered `critical` in the
criteria registry and the script sweep). 202 hits corpus-wide, 98% precision /
75% recall against the AST census; it under-reports by design. So this bean's
backlog is now machine-visible and regressions are caught at the gate.


## Batch 1 landed 2026-08-25 — 3 blocks, 6 assertions

- **`prop:bar-involution-invariance`** (`audits/brundan_kleshchev_audit.py`, 5
  assertions). Read `computed=pn, expected=pn` for `pn = len(partitions_of(n))`.
  Now `expected=KNOWN_P_N[n]` — p(2..6) = 2, 3, 5, 7, 11, independent of the
  enumerator, so it can fail. **Test 1 in the same file already had the right
  shape** (`computed=burnside, expected=dim_hecke`, two routes to n!); the fix
  was to follow the file's own template. The comment states what is now checked
  and what is not: the identification of p(n) with dim Z(H_n) is
  Brundan-Kleshchev's theorem, cited, not computed.
- **`rem:knot-operator-basis-table`** (`photon_operator_table.py`) and
  **`rem:hecke-operations`** (`basis_knot_tables.py`). Both looped
  `computed=data[...], expected=data[...]` over the e⁻ pair counts. Now literal
  expected tables. `photon_operator_table.py` already had a correct
  `expected=36` for `T_{2,3}` immediately below the bad loop.

**These two are regression pins, not derivations, and are labelled as such** in
the source. Pinning the H₃ table's output catches a change in the table, the
basis order, or the NF reduction; it does not independently derive the counts.
That is strictly more than a tautology checks, and the distinction is written
down rather than left for a reader to assume.

Worth recording: the two scripts compute the same quantity by different routes
and **agree** where they overlap — γ 19, σ₀/σ₁ 24, e⁻ 36. Noted in
`basis_knot_tables.py`, since that mutual check is the nearest thing to an
independent derivation available today.

### Witnesses deliberately NOT regenerated

Running the producers here rewrites the witness `environment` block, and this
container is missing `clarabel`, `scipy` and `pyhecke_native` and carries
mpmath 1.3.0 against the recorded 1.4.1. `WitnessBuilder` says so directly:
*"install it and re-run rather than committing the weaker record; the numbers
can be identical while the provenance silently degrades."* Each producer was
run to confirm the new assertions pass, then its witness reverted with
`git checkout`. **Script fixes only in these commits.** The witnesses want
regenerating in a properly provisioned environment.


## Batch 2 landed 2026-08-25 — 2 blocks, 5 assertions, two different remedies

The two cases needed opposite fixes, which is the general lesson: there is no
single repair for this defect.

**`prop:confinement-nf-partial-proof`** (`shift_from_nf_basis.py`, 2). The
assertion NAMES said what to check — `shift_proton_h3_finite`,
`shift_neutron_h3_finite` — while comparing `shift_p` to itself, so they passed
for `inf` and `nan` too, exactly what a name ending `_finite` promises to
exclude. Now `computed=math.isfinite(float(shift_p)), expected=True`. The check
the author intended was written in the name the whole time.

**`thm:topological-mass`** (`mass-from-q-symbolic.py`, 3). Different: no check
exists, and the author knew — the code carried the comment *"self-consistent
(no independent measurement)"*. That comment was correct and `add_assertion`
was the wrong instrument. `P_proton`, `P_neutron` and their ratio each have one
derivation route, so no assertion over them can fail, and carrying them as
assertions made them count toward `allPassed` and hence toward the block's
`verified`.

**They are now `add_data`** with propagated uncertainties and a note saying why
they are not asserted. Nothing is lost; nothing is claimed. The block keeps
real backing from the assertions that do check something — notably the
Borromean mass against `borromean_mass_ratio * M_E_MEV`. Assertion count went
10 → 7, and that is the fix working, not damage.

**Three remedies seen so far, and choosing between them is the work:**

1. *Supply the real expected value* — when it exists independently
   (`KNOWN_P_N`, the e⁻ pair tables).
2. *Assert the property the name claims* — when the intent is recoverable
   (`_finite`).
3. *Demote to data* — when no independent check exists. The one that needs
   saying out loud, because it is the one that looks like giving up and is
   actually the only honest option.

All five files now pass `assertions_are_falsifiable`.


## Batch 3 landed 2026-08-25 — 2 blocks, 5 assertions, and a fourth remedy

**`conj:schwinger-measure-computational-time`**
(`probes/r2core_schwinger_measure_explore_probe.py`, 4) exposed a pattern worth
naming, because it looks like the *opposite* of a vacuity problem.

The script does the real mathematics and checks it — with bare Python
`assert`s:

    assert mom == sp.factorial(k - 1)
    assert diff == 0, f"linear-unit invisibility failed: {diff}"
    assert rel > PIN_SHIFT_MIN

Those are genuine verifications, and they run. But a bare `assert` **crashes
the script and leaves nothing in the witness**, so the witness assertion beside
it recorded `computed=True, expected=True` (or `computed="0", expected="0"`) —
a constant that would pass with the checking code deleted.

So the file was simultaneously rigorous and unverifiable-from-its-own-record.
The fix is to carry the computed result into the assertion:
`moments_are_factorials = all(...)`, `block1_...` now returns its symbolic
`diff`, and the pin-dependence loop accumulates `pin_dependent[name]`. Same
mathematics, now recorded.

**Fourth remedy: move the check from `assert` into the witness.** Distinct from
the other three, and probably common — a script whose author verified properly
and whose witness cannot show it.

**`conj:flavor-split-habiro-derivation`**
(`mn_flavor_split_h4_plancherel.py`, 1). `h4_plancherel_scan_completed` read
`computed=len(candidates), expected=len(candidates)` — passing even when the
scan produced nothing, the one outcome a name ending `_completed` exists to
exclude. The scan is exploratory so the count cannot be pinned in advance;
`len(candidates) > 0` can fail and is what the name claims.

**7 of 10 done.** All seven files pass `assertions_are_falsifiable`.


## Batch 4 landed 2026-08-25 — the impact set is DRAINED, 10/10

- **`prop:t-beta-markov-frobenius-collapse`** (`qbeta_markov_trace_norm_probe.py`).
  `shapes-differ-per-channel` compared `float(max_diff)` to itself with the
  comment *"We just record the differences"* — right, and the reason it should
  not have been an assertion. The name and the `source` both state the
  checkable claim ("non-zero is expected"), so it is now
  `bool(max_diff > 0)` against `True`, with the magnitude kept as data.
- **`rem:per-observable-100x-status-dashboard`** (`per_observable_100x_status.py`).
  A snapshot count has no external expectation, but it has an internal one: the
  summary must agree with the rows serialised beside it. Now
  `computed=len(out["rows"]), expected=out["summary"]["total"]` — which fails if
  rows are filtered after the summary is built, the realistic way this
  dashboard goes wrong.
- **`conj:staircase-ew-residual`** (`staircase_ew_residual_conjecture.py`).
  `k{k}_skipped_due_to_degeneracy` was a skip MARKER dressed as an assertion,
  inflating `allPassed` with a control-flow fact. Demoted to `add_data`. The
  file's `k3_residual_matches_q_one_fifth` already had the right shape.

### One thing worth not misreading

Re-running `qbeta_markov_trace_norm_probe.py` here reports a FAILURE — but it
is **`L2-constraint-at-q0`, computed 3.455e-09 against tolerance 1e-9**, a
pre-existing assertion unrelated to this change. My new assertion passes. The
overshoot is 3.5x tolerance and this container is missing `scipy`, so it is
most likely an environment precision gap rather than a corpus defect — but it
is *not* verified as such, and someone should re-run it properly provisioned
before assuming so. Recorded here rather than left in a terminal scrollback.

## Status: impact set complete

All 10 blocks that claimed `computation.status: "verified"` on the strength of
a tautological assertion now have assertions that can fail. Every one of the 10
producers passes `assertions_are_falsifiable`.

**~250 sites remain**, all in scripts no content block cites. Not urgent by the
argument that opened this drain: no block's status depends on them. They are
now machine-visible — the criterion is `critical` in the registry and runs in
the script sweep — so they surface on the gate rather than needing a census.

### The four remedies, for whoever takes the rest

1. **Supply the real expected value** — when one exists independently
   (`KNOWN_P_N`, the e⁻ pair tables).
2. **Assert the property the name claims** — when intent is recoverable
   (`_finite`, `_completed`, `shapes-differ`).
3. **Demote to data** — when no independent check exists. Looks like giving up;
   is the only honest option, and the author is often already saying so in a
   comment.
4. **Move the check out of a bare `assert`** — when the script verifies
   properly but the witness cannot show it.

### Witnesses

Not regenerated in any batch. Running the producers here rewrites the
`environment` block and this container lacks `clarabel` and `pyhecke_native`
and carries older `mpmath`; `WitnessBuilder` warns that the numbers can be
identical while provenance silently degrades. Every producer was run to confirm
its new assertions pass, then its witness reverted. **The witnesses want
regenerating in a properly provisioned environment** — that is the one
outstanding task from this drain.


---

## Re-measured after merging main, 2026-08-29 — the impact set is EMPTY

2,478 commits of main merged in. Census and impact triage both re-run:

|  | 2026-08-25 | 2026-08-29 (merged) |
|---|---|---|
| files parsed | 3,253 | 3,538 |
| `add_assertion` calls | 3,482 | 3,780 |
| tautological | **266** (7.6%) | **229** (6.1%) |
| files carrying one | 195 | 172 |
| backing a content block | 14 | 2 |
| **backing a block claiming `verified`** | **10** | **0** |

The corpus grew by 285 files and 298 assertions, and the count still fell by
37. The ten `verified` blocks drained in batches 1–4 stayed drained through the
merge, and main introduced no new ones.

**Zero blocks now claim `verified` on the strength of an assertion that cannot
fail.** That was the whole point of triaging by impact rather than by count.

### The two survivors that touch a block, and why neither is urgent

- `conj:casimir-epsilon-vacuum` — `probes/casimir_hoefsmit_additivity_probe.py:190`,
  block status `experimental`. An experimental status over an exploratory probe
  is not a false claim.
- `rem:hadron-level-knot-table` — `hadron_knot_table.py:258`, block status
  `failed`. Worth fixing on its merits: it reads
  `computed=r["tr_M"], expected=r["tr_M"]` under
  `source="hecke_core.build_atom_nf -> nf_tr"`, i.e. it advertises a check
  against a named producer while comparing the value to itself, and the LP
  assertion four lines below is correctly written (`expected=1`).

  **Not fixed here.** The remedy is to pin the tr_M values, which requires
  running the producer, and it does not complete within 580s in this
  container. Its block already says `failed`, so nothing false rests on it
  meanwhile. Needs an environment that can run it.

### Remaining

229 sites across 172 files, none backing a `verified` claim. Machine-visible
via `assertions_are_falsifiable` (folio-assistant, `critical`), so they surface
at the gate rather than needing a census. The four remedies recorded above still
apply; picking between them is still the work.


---

## `rem:hadron-level-knot-table` closed 2026-08-30 — by deletion, not repair

`hadron_knot_table.py:258` read `computed=r["tr_M"], expected=r["tr_M"]` under
`source="hecke_core.build_atom_nf -> nf_tr"`: it advertised a check against a
named producer while comparing the value to itself.

**Removed rather than repaired, and there is nothing to repair it to.** Each
`tr_M` has one derivation route, so no assertion over it can fail — and
`w.add_data("atoms", results)` twenty lines below *already records every one of
these values* at full precision. The assertion contributed a guaranteed pass to
`allPassed` and nothing else. Deleting it loses no information and removes a
claim that was never made.

Note this did NOT need the producer to run, which is why it could be done here
after the earlier attempt timed out at 580s: the fix is a deletion justified by
reading, not a pin requiring values.

The LP-stability assertion four lines below is the model and is left alone —
`computed` is the measured predicate, `expected=1` is fixed, and it can fail.

That leaves `conj:casimir-epsilon-vacuum` (`status: experimental`) as the only
tautology touching a content block, and an experimental status over an
exploratory probe is not a false claim.


---

## Drain resumed 2026-08-30 — 228 → 159

Two classes cleared mechanically. Tool kept at
`scripts/drain-tautological-assertions.py`.

**Class: `computed=len(X), expected=len(X)` — 16 sites.** Names ending
`_completed` / `_scan` / `_prescreen`, passing when the scan found nothing,
which is the one outcome those names exist to exclude. Now `len(X) > 0` against
`True`. Unambiguous: the name states the predicate and the measured quantity is
already there.

**Class A: real `assert`s beside a constant assertion — 46 sites, 44 functions,
16 files.** The `r2core` shape at scale. These scripts do the mathematics and
check it properly with bare `assert`s, which abort on failure and leave
**nothing in the witness**, so the assertion beside them recorded
`computed="0", expected="0"`. Transformation per function: declare
`_ok: list[bool] = []`, rewrite `assert X, m` to `_ok.append(bool(X))` +
`assert _ok[-1], m` (X evaluated once, abort semantics preserved), and retarget
the witness assertion to `all(_ok)` against `True`. `borel_propertime` alone
carried 22 real checks behind one constant.

12 of the 16 run clean; the other 4 are slow probes that time out here, with no
errors.

### Two bugs in my own transform, both caught by RUNNING it

Recording these because both are the failure this bean is about, committed by
the tool written to fix it.

1. **Column shift.** `computed=X, expected=X` often sits on one line.
   Replacing `computed`'s value first moves every later column, so the
   `expected` edit landed inside the keyword and produced `expeTrued=`.
   **`py_compile` accepted it** — `expeTrued=` is valid Python — and it failed
   only at run time with `TypeError: unexpected keyword argument`. Fixed by
   applying replacements right-to-left within a line.

2. **Test fixtures are not tautologies.** The first run rewrote
   `tools/qou-substrate/tests/test_declared_tolerance_literal.py`, where
   `add_assertion("b", computed="1", expected="1")` is deliberately constructed
   to exercise tolerance serialisation. Worse, `_ok.append` landed *after* the
   call, so `all([])` → `True` silently changed what the test asserts.
   Reverted; the tool now refuses `tests/`, `test_`, `conftest`, `fixtures/`.

**Compiling is not running, and running one file is not running the batch.**
Both bugs passed `py_compile` on all 16 files.

### What is left: 159 sites, 141 files

- ~104 where `computed` is a non-literal expression with no recoverable check
- the remainder literal-vs-literal with no `assert` to carry in

Neither class is mechanical. The honest remedy for most is **demote to data** —
and note that is now known to be safe: nothing in the corpus reads witness
assertions by name (every `.assertions` hit is inside `witness.py` itself), so
converting an assertion to data breaks no reader. That was checked, not assumed.

Still zero blocks claim `verified` on any of them.

## 2026-08-30 — DRAIN COMPLETE, and a git hazard worth not repeating

`scripts/tautological-assertion-census.py`: **TAUTOLOGICAL 0 of 3939, across 0
files** (3 remain in test fixtures, where the shape is deliberate). Verified by
re-running the census independently of the agents that reported it. Down from
263 at the start of this arc.

### The hazard: `git commit` with no pathspec on a SHARED index

Three sessions were working one branch in one checkout. Agents were briefed
"stage ONLY your files, NEVER `git add -A` or `git add <dir>`" — and all three
complied. The dispatcher (me) then did:

    git add <4 bean paths>
    git commit -F - <<'EOF' ...

No `git add -A` anywhere. But a sibling had already **staged** 14 files in the
shared index, and `git commit` without a pathspec commits *the whole index*.
So commit `1717c95e6cd`, whose message describes four beans, actually carries
four beans plus a sibling's entire seven-producer drain — 18 files, 2469
insertions.

Content was unharmed (the sibling re-ran every producer and confirmed payloads
byte-identical); the **record** was wrong, which on a corpus that treats
provenance as load-bearing is the part that matters. The sibling repaired it
forward, titling their next commit "the drain record for 7 producers swept
into 1717c95e6cd" rather than rewriting shared history.

**The rule that actually holds:** on a shared checkout, use
`git commit -- <explicit paths>`. `git add <paths>` constrains only what *you*
add, not what is already staged. One sibling agent used the `commit --` form
unprompted and was immune; the briefing that said "never `git add -A`" was
necessary and not sufficient.

Better still: don't share a checkout. This arc also lost an edit and stranded
agent work when another session switched branches under `/workspace/qou`; the
isolated worktree `/workspace/qou-mt7r` fixed that and should be the default.

## The unconditional description has now caused a downstream error (2026-09-07, qou-17mq)

Recording a realised cost, because it raises this bean's priority above
"cosmetic wording".

binding_volume_difference_probe.py fires exactly the failure this bean names:
its add_caveat correctly says observable C (SnapPy on the derived braid
closures) was NEVER EVALUATED -- _snappy_braid_vols returns (None, None, False)
on ImportError, indistinguishable at the call site from a genuine
non-hyperbolic result, and vol_free is null in the committed witness -- but the
module DESCRIPTION still asserts a "triple refutation" with C as one leg,
unconditionally.

A corpus-grep run today on bean qou-17mq read the description, not the caveat,
and reported the triple refutation to me as an established structural fact:
"SnapPy on the derived braid closures returns ~0 at every A -- closures are
non-hyperbolic". Acting on that, I would have written into a bean and a PR
that the inter-cusp-separation route is structurally dead. It is not. It is
unmeasured, and the one thing that would settle it is installing SnapPy --
which a reader who believes the description will never bother to do.

So the caveat is doing its job for a reader who reaches it, and the
description is defeating it for everyone who does not. The asymmetry matters
because the description is what a grep, a summary, and a witness consumer all
surface first.

The narrow fix is to make the description conditional in the same way the
caveat already is -- state a DOUBLE refutation (observables A and B, which did
run and do stand) and name C as not evaluated. Not done here: it would
regenerate that probe's witness on a PR about something else. Flagging rather
than widening.

Cross-ref: qou-17mq carries the full correction and the verification, including
that observables A (log-volume, kappa spans 313%) and B (cosh-inversion
degenerate, all |tr_M| < 2, elliptic) are unaffected and stand.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- **Round 92 (`litlfred/qou#8416`)**: Advanced in `feat/round92-jetmono-jetsign-kzratio-kzunit-kappacorr-43c1` (Commit 1 `b85484a2b9309c11a8832becee2e728a03219677`, Commit 2 `de3ca907bd3d3c7bb260ce5aa08259ade30c6cc9`, probe sha256 `7a5dfeb80aacf1b23a7e663221ecc9f97b20abf96256db6ae736e9dd7742c6f9`).
