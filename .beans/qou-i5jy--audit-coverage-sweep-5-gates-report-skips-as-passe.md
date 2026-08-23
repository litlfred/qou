---
# qou-i5jy
title: 'Audit coverage sweep: 5 gates report skips as passes — a deleted package ratchets to -1, and the importability audit drops its own worst case'
status: todo
type: task
created_at: 2026-08-23T07:54:52Z
updated_at: 2026-08-23T14:55:00Z
---


Systematic sweep for the defect shape recorded in `qou-ivhc` and fixed in
`qou-0uqm`: **an audit reports a clean headline over a population it never
evaluated, rendering "skipped" identically to "passed."** Coverage: 38
audits/gates/validators opened, 26 read in full, all 50 `computations/audits/*.py`
triaged.

Findings 1 and 2 below I **re-verified myself** by reading the source and running
the code; the rest are recorded as reported and are marked accordingly.

## 1. VERIFIED — `computations/extraction_wall_gate.py`: a deleted package reports as IMPROVED, and invites ratcheting the wall to −1

```python
def count_package(pkg: str) -> int:
    root = REPO / "tools" / pkg
    if not root.is_dir():
        return -1                      # :42 sentinel, never distinguished
...
        elif n < b:
            improvements.append((pkg, b, n))   # :77 — -1 < b ALWAYS
```

`tools/witness-schema/` does not exist. Ran it:

```
IMPROVED  witness-schema: 6 → -1 qou-referencing files (run --update-baseline to ratchet)
```

**Taking that instruction sets the baseline to −1**, after which no real count can
ever regress below it — the wall for that package is permanently disabled by a
missing directory. The clean-path headline then launders the sentinel out of the
total:

```python
f"({sum(v for v in counts.values() if v > 0)} files total, ratchet only goes down)"   # :89
```

Evaluated: **8 of 9** declared packages. Separately, five packages that *do* exist
under `tools/` (`hecke-engine-gap`, `-julia`, `-octave`, `qou-substrate`,
`borromean-recurrence-crt`) are not in `PACKAGES` at all, and the output never
states that its scope is a 9-name list.

## 2. VERIFIED — `computations/audits/producer_importability_audit.py`: the audit's own worst case is dropped before the check begins

```python
        sf = d.get("scriptFile")
        if not sf:
            continue                    # :126-127
        cand = wf.parent / os.path.basename(str(sf))
        if cand.exists():               # :129 — no else
            out.setdefault(cand, []).append(wf)
```

Measured independently over the live corpus:

| class | count | fate |
|---|---|---|
| no `scriptFile` field | **286** | dropped silently |
| `scriptFile` not beside the witness | **73** | dropped silently |
| resolved and checked | **2356** | evaluated |
| **evaluated fraction** | **0.868** | |

The audit's stated thesis is that a witness whose producer cannot be imported *"can
never be refreshed and no staleness mechanism sees it."* **A producer that does not
exist at all is the maximal case of that thesis, and it is the one silently
excluded.** Reported examples of producers existing nowhere:
`wall-violations.witness.json` (its `scriptFile` is prose — *"legacy orphan — no
current producer"*), `joint-tower-sdp-rust.witness.json` (`joint_tower_sdp.rs`),
`mu3-submodularity-vacuous-deuteron.witness.json` (a `.lean` file). Everything
else in this script's reporting is exemplary — `optional-dep`, `heavy-at-import`
and `in-repo-wiring` are each counted separately; the hole is upstream of all of it.

## 3–5. Reported, not independently re-verified

- **`witness_failed_assertion_audit.py:230`** — 519 of 2715 witnesses (19.1 %)
  carry neither a non-empty `assertions[]` nor `allPassed: False`, so they are
  structurally incapable of being counted red. Neither number appears in the
  output, and the docstring quotes the full corpus as the denominator.
- **`classify_production_reach.py:60-75`** — if both `rg` and `grep` fail or time
  out, `_rg` returns an empty set, which flows to `production: False` →
  `NOT-PRODUCTION` → the printed action *"eligible for `precision_tier='float64'`
  + deprecated"*. A search-tool failure therefore produces the verdict that
  authorises a float64 carve-out, with no coverage figure printed beside it.
- **`scripts/guard_check.py:18,29`** — both content guards sit inside bare
  `except: pass`, then the function `return True`s. `auto_commit_batches.py:6`
  commits whatever it prints, so *"passed the guard"* and *"the guard crashed"* are
  the same line of stdout.

Tier 2 (same mechanism, 0 instances today): `incomplete_coverage_audit.py:89,124`
(unparseable and clean both return `None`), `q0_cross_layer_fallback_scan.py:88`
(drops files that already passed both pre-filters; 123-file candidate population
never printed), `block-manifest-audit.ts:284,362` (one failed chapter silently
skips every block under it), `witness_dependency_coverage_audit.py:168` (prints
**100.0 %** over an empty set; `agg_total = 6` of 2639),
`silent_self_check_audit.py:319`, `guarded_off_audit.py:136`.

## The corpus already contains the right pattern — four times

This is not a missing idea, it is an inconsistently applied one. Checked and
sound, and worth copying rather than reinventing:

- **`noncanonical_reentry_audit.py:376`** — prints `parse errors (skipped) : N`
  **and** `--strict` fails on `(all_violations or parse_errors)`. The in-repo gold
  standard.
- **`witness_hollowness_audit.py:89`** — unparseable is an **offence**, not a skip.
- **`scripts/precision-gates.sh`** — exits 2 with *"This is NOT a gate failure.
  Nothing was examined"*.
- **`scripts/check-sidecars.sh`** — *"0 changed file(s) — this check examined
  NOTHING"*.

`q0_hardcoded_pin_audit.py` merges "verified consistent" with "literal presumed
unreached" but **names the merge** in both the console label and the witness key —
disclosed, therefore not a defect by this bean's criterion.

## Priority

**#1 first, and it is small.** The `-1` sentinel is a two-line fix (treat a missing
package as an error or an explicit `MISSING` class, never as an improvement) and it
currently offers, in its own output, an instruction that would silently disable a
ratchet. #2 is the highest-value correctness item but needs a decision about what
to *do* with 359 unresolvable witnesses, which is `qou-cds3`-adjacent scope.

Nothing edited. No witnesses written.

---

## Finding #1 FIXED 2026-08-23 — `extraction_wall_gate.py`

The `-1` sentinel no longer masquerades as a file count.

**Before**

```
IMPROVED  witness-schema: 6 → -1 qou-referencing files (run --update-baseline to ratchet)
```

**After**

```
MISSING   witness-schema: tools/witness-schema/ does not exist — NOT counted,
          NOT an improvement (baseline 6 retained)
```

### Changes

1. `MISSING = -1` named, with a comment recording *why* it must never be compared
   against a baseline (`-1 < b` for every real `b`).
2. Absent packages are partitioned out **before** the regression/improvement
   comparison and reported in their own class.
3. **`--update-baseline` can no longer persist the sentinel.** It was the real
   harm: the old message invited the flag, and the flag wrote `witness-schema: -1`
   into `tools/extraction-wall-baseline.json`, after which no real count could
   ever exceed it and that package's wall was permanently disabled by a missing
   directory. Absent packages now retain their prior baseline, so the wall
   re-arms if the directory returns.
4. The clean-path headline no longer filters `v > 0` (which laundered the
   sentinel out of the total) and now prints scope:
   `scope: 8 of 9 declared package(s) evaluated; 1 absent`.
5. The `--update-baseline` listing prints what was **written**, not what was
   measured — for an absent package those differ, and printing `-1` beside
   "baseline written" is how the sentinel got trusted in the first place.

### Verified on both paths

Report path shows `MISSING`, not `IMPROVED`. Update path writes
`witness-schema: 6` and prints `NOTE: 1 package(s) absent, baseline left
unchanged for them`. The real baseline file was backed up before each
`--update-baseline` test and restored — `git status` clean afterwards, confirmed
both times. That flag would otherwise have ratcheted the four genuinely regressed
packages upward and weakened the wall.

### Deliberately NOT changed

- **The exit code.** A missing package still does not fail the gate. Making
  `MISSING` a failure is a policy call for the gate's owner — a package may have
  been removed on purpose — and this bean's criterion is that exclusion be
  *visible*, not that it be *fatal*.
- **`PACKAGES` scope.** Five directories under `tools/` are not in the list
  (`hecke-engine-gap`, `-julia`, `-octave`, `qou-substrate`,
  `borromean-recurrence-crt`). Adding them changes what the wall covers, which is
  a scope decision, not a reporting fix. The new `scope:` line at least states the
  denominator now.

Finding #2 (`producer_importability_audit.py`, 0.868 evaluated) is untouched: it
needs a decision about what to do with 359 unresolvable witnesses, which is
`qou-cds3`-adjacent.

---

## Finding #4 VERIFIED, and NARROWED — the "authorises a float64 carve-out" framing was too strong

I relayed #4 as: a search-tool failure *"produces the verdict that authorizes a
float64 carve-out."* Reading `classify_production_reach.py` in full, **the
mechanism is real but the consequence is overstated**, and the correction matters
because the file is unusually disciplined.

### What is true

```python
def _rg(pattern, *, fixed=False) -> set[str]:
    for cmd in (["rg", "-l", ...], ["grep", "-rl", ...]):
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
        if out.returncode in (0, 1):
            return {...}
    return set()          # ← "no matches" and "never searched" are the same value
```

Confirmed: if both tools are absent, both time out, or both exit non-0/1, `_rg`
returns an empty set and **nothing in the output distinguishes that from a clean
search**. The frontier in `classify()` then never expands, so the walk finds no
`PRODUCTION_STEMS` hit. That is a genuine instance of this bean's pattern.

### What is NOT true

**1. It does not flip the verdict on its own.** The fall-through is
`{"production": defines_const, …}`, and `defines_const` comes from reading the
producer's source for `LAMBDA_*` / `ALPHA_*` / `Q_*` (`:124-127`) — **independent
of `_rg`**. So a producer that defines a production constant is still classified
`production: True` even with the search fully broken. The blast radius is limited
to producers that define no such constant.

**2. It does not authorise anything.** The file's header has an explicit
*"## What it does NOT do"* section:

> It does not decide. A `NOT-PRODUCTION` verdict here is **necessary** evidence
> for the deprecate-with-tier route, **not sufficient authority** for it … Read
> the printed evidence; do not paste the verdict into a witness unread.

That is precisely the misuse I described it as enabling, disclaimed in advance by
the script itself.

### The residual finding, stated at its real size

`_rg`'s silent fallback degrades the *evidence* — `direct_readers` comes back
empty and looks like a measured result — while the header's mitigation is a
**human-discipline instruction, not a mechanism**. Cheap fix, same as everywhere
else in this bean: distinguish the two, e.g. return `None` on total tool failure
and print `search unavailable — evidence incomplete` rather than an empty reader
list.

Worth saying plainly: this script is one of the **better-behaved** files I have
read in this corpus. It states its own limits, prints its evidence, and refuses to
be treated as authority. The `_rg` fallback is the one place where it silently
does the thing it warns readers not to do.

### Status of the other relayed findings

- **#5 `guard_check.py`** — verified by reading both files. Both content guards sit
  in bare `except: pass` then `return True`, and the sole consumer
  (`auto_commit_batches.py:7`) filters on the stdout prefix `"Reverting"`, so
  *guard passed* and *guard crashed* are byte-identical and both get committed.
  Stands as reported.
- **#3 `witness_failed_assertion_audit.py`** — not independently re-measured. The
  mechanism (only a non-empty `assertions[]` or explicit `allPassed: False` can be
  counted) is visible in the source; the 519/2715 figure is relayed.

---

## Finding #5 FIXED 2026-08-23 — `scripts/guard_check.py`: a crashed guard is now a third outcome, not a pass

The guard had two verdicts where it needed three. Both content checks sat in bare
`except: pass` and fell through to `return True`, so a file the guard never
managed to evaluate was reported as having passed it.

**The obvious fix is worse than the defect.** Returning `False` on a guard error
routes the file to `:46`, `subprocess.call(['git', 'checkout', '--', filepath])`
— which discards the working-tree edit. An unevaluated file is not a failed
file, and must not be destroyed as though it were.

### Verdicts

| verdict | stdout | working tree |
|---|---|---|
| `PASS` (`True`) | filename → caller commits | left modified |
| `BLOCK` (`False`) | `Reverting <path> (<reason>)` | **reverted** (unchanged) |
| `SKIP` (`None`) | *nothing* | **untouched** — neither committed nor reverted |

`SKIP` diagnostics go to **stderr** on purpose: stdout is a filename list that
`auto_commit_batches.py:7` feeds straight to `git add`, so a new stdout line
would become a pathspec.

### The caller had to change too

`if check_file(filepath): … else: git checkout` sends `None` down the **revert**
branch, because `None` is falsy. The three-way dispatch is now explicit
(`is PASS` / `is BLOCK` / else skip). Adding the return value without this would
have converted every guard crash into a deletion.

### Measured, old vs new, under an identical forced failure

Throwaway repo, `git` shimmed to fail on `diff --numstat` only, with one
tiny edit and one **300-line delta** — the exact thing the guard exists to block.

*Old:*

```
stdout: content/big.md      ← 300-line delta, committed
        content/ok.md
exit=0, no warning
```

*New:*

```
stdout: (empty)
stderr: SKIP content/ok.md: guard could not run `git diff --numstat …`
        guard_check: 1 file(s) SKIPPED — left uncommitted and unreverted
exit=0; working tree intact, edit preserved verbatim
```

So the old failure mode was not merely "unevaluated file passes" — the guard's
**blocking criterion was silently disabled** and the file it was built to stop
was handed to the committer. Normal-path behaviour is unchanged: all three
`BLOCK` reasons still revert, `PASS` still prints the filename.

### Also fixed

- Bare `except:` → `except Exception:`, so Ctrl-C during the guard is no longer
  swallowed into a pass.
- `diff_out.split('\t')` unpacked into exactly three fields and called `int()`
  on them unguarded; unparseable numstat now returns `SKIP` instead of raising
  into the same swallowed pass. `200` is now `MAX_LINE_DELTA`.

### Deliberately NOT changed

- **Exit status stays 0 when files are skipped.** The caller runs this under
  `subprocess.check_output`, which raises on non-zero — a fatal skip would abort
  the batch and commit *nothing*. A skip cannot be mistaken for a pass here
  anyway: the file is absent from stdout **and** left dirty in the working tree,
  so the next run retries it.
- **The `"Reverting"` stdout prefix contract** with `auto_commit_batches.py:7`,
  left byte-identical. Only one consumer exists (swept: no hook or CI wiring).

---

## Finding #6 NEW + FIXED 2026-08-23 — `scripts/session-start-coord-sweep.sh` reported "no sibling activity" over a ref namespace it never fetched

Found while verifying my own push for #5, not by sweeping for it. **The most
load-bearing instance of this bean's pattern found so far**, because it governs
multi-agent coordination rather than a single artefact.

### The mechanism, in three lines that are each correct alone

```sh
git fetch origin main                                    # :26 — main ONLY
...
refs/remotes/origin/claude 2>/dev/null                   # :39 — reads sibling refs
...
if [ -n "$RECENT_SIBLINGS" ]; then                       # :60 — heading printed ONLY if non-empty
```

This clone's configured refspec is `+refs/heads/main:refs/remotes/origin/main`
— main only, which is the default for the ephemeral containers this campaign
runs in. So `refs/remotes/origin/claude/*` is **never updated by any fetch**: it
is a frozen snapshot from clone time, and in a fresh container it is very nearly
empty. `RECENT_SIBLINGS` comes back empty, and `:60` then omits **the entire
heading**.

The agent does not read "0 siblings found". It reads a coord sweep with a main
section and a beans section and **no sibling section at all**, and concludes the
namespace is quiet. Absence of refs renders as absence of siblings, and the one
line that would have disclosed the gap is deleted by the same condition that
creates it.

### Measured, after fixing the fetch

| | |
|---|---|
| sibling branches the sweep reported | **0** |
| updated in the last 24 h | **97** |
| known on origin | **4775** |

Among the 97 unreported, two are in this campaign's own scope:
`claude/q0-literal-transcription-drain-2026-08-23` (*"q0 literals: 8 more sites
were never blocked; ratchet 69 → 61"*) and
`claude/cds1-ladder-d-rederivation-2026-08-23` (*"narrow my own claim: the
closure is the CHARACTER case…"*) — the `qou-cds1` sibling this branch has been
deferring to, whose progress was invisible here.

### Second, independent defect in the same block — the 24 h window was never implemented

`:36` commented *"updated in last 24h"* and `:61` printed the heading
**"Recent sibling branches on origin (last 24h)"**, but the code was
`--sort=-committerdate … | head -8` with **no date filter of any kind**. The
label happened to be true whenever the 8 most recent were fresh, and would
silently print June branches under a "last 24h" heading whenever they were not.
Unenforced, not merely currently-wrong.

### Fixes

1. **Fetch the refs the sweep reads**, with the refspec passed *explicitly*
   (`+refs/heads/claude/*:refs/remotes/origin/claude/*`) so correctness does not
   depend on how the clone was configured — the failure mode being fixed.
   `--prune` drops deleted siblings; bounded by `timeout 45` (with a fallback
   when `timeout` is absent) because this is a SessionStart hook.
2. **The 24 h window is now applied in code**, against
   `%(committerdate:unix)`. Subjects are rebuilt from field 4 onward so a `|` in
   a commit subject cannot truncate the line.
3. **The section is always emitted**, empty or not:
   `_0 of N known sibling branch(es) updated in the last 24h._` A measured zero
   is now distinguishable from an unmeasured one.
4. **A failed sibling fetch says so** — `**NOT REFRESHED** … Do NOT read an
   empty list as "no siblings"` — instead of degrading into a clean-looking
   empty section.

Tested on all three paths (normal, sibling-fetch failure via a `git` shim, and
`bash -n`); exit 0 on each. This is a SessionStart hook, so a crash would break
every session in the repo — hence testing the degraded path before committing
rather than after.

### Related, NOT fixed — flagged for the owner

The bean section prints **1853 of 3837 beans** every session (~247 KB): 1421
`todo` + 302 `in-progress` + 122 `scrapped` + 7 `open` + 1 `draft`; only
`completed` (1960) and `done` (24) are filtered. The parenthetical *"non-completed"*
accurately describes what the code does, so this is **not** a mislabel of the
kind this bean tracks — it is a session-start context-budget decision (most-recent
N? `in-progress` only? exclude `scrapped`?) and it belongs to the hook's owner,
not to a coverage fix. Recorded with the measurement so the choice can be made
on numbers.

---

## Finding #4 FIXED 2026-08-23 — `classify_production_reach.py` now distinguishes "no readers" from "never searched"

The residual after the narrowing above: `_rg` returned `set()` both when a
pattern genuinely matched nothing and when neither `rg` nor `grep` could be run.
Those are opposite facts — *no readers* is evidence toward `NOT-PRODUCTION`,
*never searched* is no evidence at all.

### Demonstrated, not asserted

Same stem, `PATH` stripped of both `rg` and `grep`, old code vs new.

*Old, total search failure:*

```
  verdict : NOT-PRODUCTION  (reaches no production location within depth)
  readers : NONE (leaf)
  action  : eligible for precision_tier='float64' + deprecated, ...
exit=0
```

**Byte-identical to a successful run.** The output that licenses a float64
carve-out was produced by gathering none of the evidence for it.

*New, same conditions:*

```
  readers : NONE (leaf)
  SEARCH  : *** INCOMPLETE *** one or more reachability searches
            could not be run ... An empty 'readers' above is NOT
            evidence of non-reachability — it is no evidence.
  action  : eligible for precision_tier='float64' + deprecated, ...

search coverage: 0/2 reachability searches ran
WARNING: 2 search(es) did NOT run. ... Any NOT-PRODUCTION verdict above
         that rests on an empty reader set is unsupported.
exit=3
```

Normal run is unchanged apart from a new `search coverage: 2/2 reachability
searches ran` line, and still exits 0.

### Changes

1. `_SearchHealth` counts searches attempted vs failed. `_rg` increments
   `failed` on the fall-through path — the one place where the empty set means
   "not searched" — with a comment saying so at the `return`.
2. `classify()` snapshots the failure count per stem, so `search_degraded` is
   about *that* stem rather than the whole run, and is set on **both** return
   paths.
3. The per-stem warning prints **before** the `action:` line, which is the line
   that would otherwise be acted on.
4. Run-level `search coverage: ran/attempted`, always printed — so a healthy run
   states its coverage too, rather than coverage only appearing when it is bad.
5. **Exit 3 when degraded.** No script or CI consumes this script (checked: it
   is referenced only from `.beans/`, i.e. invoked by hand), so the exit code is
   free to carry the signal. This follows the in-repo gold standard
   `scripts/precision-gates.sh` — *"This is NOT a gate failure. Nothing was
   examined"* — and the wording deliberately echoes it.

### Signature deliberately NOT changed

I proposed above that `_rg` "return `None` on total tool failure". It would have
forced `Optional[set]` through `readers_of` and both `classify` paths, where a
missed `None` check degrades into a `TypeError` mid-walk — replacing a silent
wrong answer with a crash in a script whose whole purpose is to print evidence.
Recording the health beside the result keeps every existing signature and every
existing call site intact. The bean's earlier suggestion is superseded, not
forgotten.

---

## Finding #2 — reporting half FIXED 2026-08-23; the decision half remains the owner's

The bean split this item into a *measurement* defect and a *decision* it is
blocked on. The measurement half needed no decision and is done; the 359
witnesses still need one.

### First, a narrowing of my own claim

I wrote that the dropped witnesses are *"dropped silently."* In the **output**,
yes. In the **header**, no — the METHOD paragraph already says *"For each
committed `*.witness.json` **that names a `scriptFile`**"*, which discloses the
286-witness precondition up front. What it does not disclose is what happens
when the named producer is not beside the witness (the other 73), and neither
disclosure reaches the printed report, which is what a reader acts on. The
report showed `producers checked N` with **no denominator at all**, so nothing
on screen let a reader compute coverage. That is the defect, and it is narrower
than "silently excluded."

### Re-measured, and the earlier figures hold

`--scope-only`, against the current corpus:

```
    witnesses scanned                2719
    witnesses w/ producer resolved   2360   [86.8% EVALUATED]
    witnesses NOT evaluated          359
      no scriptFile field            286
      producer not beside witness    73
      unparseable                    0
```

The two classes match my earlier independent measurement **exactly** (286 / 73);
the totals moved 2715 → 2719 and 2356 → 2360 because `main` advanced between
the two runs. So the figure in this bean is confirmed, not merely repeated.

### Changes

1. `_producers` returns `(out, scope)` and **counts** every witness it declines
   to map, instead of `continue`-ing past it.
2. `_print_scope` prints the denominator in the report, above the existing
   counts, with the note that a witness whose producer cannot be located is the
   **maximal case of this audit's thesis, not an exemption from it** — plus
   three worked examples per class, so the reader sees the shape of what was
   dropped rather than only its size.
3. **`--scope-only`** computes the accounting and exits without importing
   anything or writing a witness. The full audit spawns a subprocess import per
   producer; coverage should not cost that.
4. The units are named. `scope` counts **witnesses**; `producers checked` counts
   **distinct producer files** and is necessarily smaller — one producer can
   emit several witnesses. Printing the two adjacently without saying so was an
   invitation to read a coverage figure as a producer count.
5. `wb.add_data("scope", scope)` so the artefact carries the denominator too.

### The repo's own float64 guard caught my first version

The initial patch stored `evaluated_fraction = round(resolved/scanned, 4)`, and
the raw-float64 guard fired on the `--limit 3` verification run:

> `⚠ raw-float64: … 1 raw float64 field(s) would enter the witness —
> .data.scope.evaluated_fraction`

Correct, and the right fix was not to serialize it more carefully but to **not
store a ratio at all**: the two integers are exact, the fraction is derivable,
and a coverage ratio needs no precision policy. The percentage is now computed
in `_print_scope` for display only. Recorded because it is this bean's pattern
inverted — a guard that fired, on the right field, with the right instruction.

### Verification discipline

`producer-importability-audit.witness.json` was snapshotted to scratchpad
**before** any run, and restored from that snapshot after each `--limit 3`
verification (a 3-producer run must never be committed as the audit's witness).
`git status` confirmed byte-clean afterwards both times. `--scope-only` writes
no witness at all, which is why it is the path used for the numbers above.

### STILL THE OWNER'S CALL — unchanged by this commit

What to *do* with the 359. They are not a reporting problem now, they are a
corpus problem: 286 witnesses name no producer, and 73 name one that is not
where the witness says it is (e.g. `qbeta-closed-form-wiring-n4-to-n10.witness.json
-> qbeta_closed_form_wiring_n4_to_n10.py`, absent). Each is a committed number
that **no staleness mechanism in the corpus can ever check**. Options are
`qou-cds3`-adjacent (regenerate / relocate the producer / mark provenance-dead),
and picking among them is a scope decision, not a coverage fix. The exit code is
likewise unchanged: `--strict` still fails only on `in-repo-wiring`.

---

## Finding #3 RE-MEASURED and FIXED 2026-08-23 — the 519 is confirmed, and it was the right class

Relayed, not measured, when this bean was filed. Re-measured now using the
module's **own** `_iter_witnesses`, so the denominator matches the numerator's
scan exactly rather than approximating it.

```
witnesses scanned .............................. 2719
  recorded RED (the headline) .................. 116
  NO SIGNAL (no assertions[], no allPassed) .... 519      <- 19.1%
  allPassed:true + empty assertions[] .......... 433      <- distinct, benign
  unparseable .................................. 0
```

**519 confirmed exactly**, and — the part worth checking — it is the *meaningful*
class. I expected the relayed figure to be a conflation of "structurally
incapable of being counted red" with the benign "`allPassed: true` and nothing
failed". It is not: those 433 are a **separate** population, and the 519 are
witnesses carrying no signal of either kind, which the audit is genuinely blind
to. The relayed number and its interpretation both survive.

### The docstring claim also holds — verified at `:63`

> `108 of 2681 live witnesses are red as of 2026-08-21`

`2681` is the whole corpus. The red rate belongs over the **evaluable** subset,
which is smaller by 519. Annotated in place with a dated `NOTE` rather than
overwritten — the original is a dated measurement and the correction is about
its denominator, so both should read straight.

### Changes

1. `scan()` takes an optional `coverage_out` dict and fills it **in the same
   walk**. This script is a gate in `scripts/precision-gates.sh`; making it walk
   2719 files twice to report its own coverage would be a poor trade.
2. The signature is extended, not changed — `scan()` and `scan(scan_root)` still
   behave identically, so no caller breaks.
3. The report prints the denominator, and names the excluded class as *"a
   different schema, not a clean result"* pointing at the header section that
   explains why the conservatism is deliberate.
4. Self-test still 8/8, including the case that pins this exclusion
   (`{}` → no offence).

### Exit semantics deliberately unchanged

`--strict` is wired into `scripts/precision-gates.sh:145`. It still fails on
`new or grown` only. Coverage is **reported**, not made fatal — same criterion
applied to `MISSING` in finding #1.

### PRE-EXISTING RED, inherited from main — not introduced here

Running `--strict` surfaced a failing gate:

```
GROWN (1):
  computations/delta-lambda-canonical-residual.witness.json: 1 -> 2
RED: a witness may not be committed with a recorded assertion failure.
```

Attribution checked three ways before reporting it as not mine: the witness is
byte-identical between `origin/main` and this branch, the baseline file is too,
and running the gate in a **pristine `origin/main` worktree** reproduces the same
single `GROWN` entry. So `main` is red on this gate independently of this
branch's 50+ commits.

Not fixed here. The remedy is one of the three the gate itself names — fix the
producer, the tolerance, or the schema misuse — and choosing among them requires
knowing what `delta-lambda-canonical-residual` should assert, which is the
q₀-migration campaign's own subject matter (last touched by *"migration: batch to
116/254 at the proton pin"*), not an audit-coverage question. **Flagged so it is
not mistaken for something this bean's commits caused, and so nothing downstream
reads this gate as green.**

---

## PRIOR / PARALLEL ART — four siblings found this shape independently (2026-08-23)

Surfaced only after fixing finding #6; the blind coord sweep is why it was not
known while findings #1–#5 were being fixed. Recorded here so this bean is not
read as sole authorship, per the lesson in `qou-a613`.

- **`changed-files-helper-2026-08-22`** (`qou-pt9b`) — *"a skip is not a pass —
  say what was compared, and how much"*, on four **shell** gates. Verbatim this
  bean's thesis, different surface.
- **`codata-gate-cost-2026-08-22`** (`qou-s2gm`, `qou-p8lx`) — *"precision-gates.sh
  changed silently passes"*; *"main is RED on this script — say so, before someone
  reads it as theirs"* — independently the same move as #3's pre-existing-red
  disclosure, same day.
- **`ratchet-selftest-tautology-fix-2026-08-23`** (`qou-1brv`) — *"the ratchet
  self-test could not fail — one shared predicate"*.
- **`wrap-legacy-computation-clobber-2026-08-21`** — *"the register could report AT
  RISK 0 without examining anything"*.

Four independent rediscoveries in three days is itself evidence the shape is
**systemic rather than incidental**. It also changes what is worth doing next: a
fifth sweep has low marginal value, whereas `qou-pt9b` has already built a shared
"what did this change touch, and how much of it did we compare" helper for the
shell gates, and the Python audits have no equivalent. Full triage: `qou-k3wq`.
