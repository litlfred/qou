---
# qou-i5jy
title: 'Audit coverage sweep: 5 gates report skips as passes — a deleted package ratchets to -1, and the importability audit drops its own worst case'
status: todo
type: task
created_at: 2026-08-23T07:54:52Z
updated_at: 2026-08-23T19:20:00Z
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

---

## Tier-2 item FIXED 2026-08-23 — `witness_dependency_coverage_audit.py:168`, the empty set that reported 100%

The bean's Tier-2 list is *"same mechanism, 0 instances today"*. I went in
expecting to find that entry mislabelled, because the bean also records
`agg_total = 6 of 2639` and that looked like a live instance. **The bean was
right and I was wrong**: 6 is not 0, so the `100.0` fallback does not fire today.
It is latent, exactly as filed. Fixed anyway, because the latency is the
dangerous part.

### Why a latent one was worth closing

```python
agg_pct = (
    100.0 * results["aggregator_with_upstream"] / agg_total
    if agg_total else 100.0          # :168
)
```

"Aggregator" is a **9-pattern filename substring heuristic**. If it ever stops
matching — a naming-convention change, a pattern list edited, a scan root moved —
`agg_total` goes to 0 and two things happen at once:

1. the percentage prints **`0 (100.0%)`**, and
2. `--strict` passes, because there are no untracked aggregators left to fail on.

So the failure mode is a **clean 100% gate over nothing**, and this script is
gate-wired (`scripts/staleness-gates.sh:57`, advisory). Demonstrated by forcing
the heuristic to match nothing:

*Old:*

```
  aggregator witnesses: 0
  aggregator with upstream tracking: 0 (100.0%)
  aggregator WITHOUT tracking: 0
OK                                     --strict exit code = 0
```

*New:*

```
  aggregator witnesses: 0   (of 2643 scanned, by a 0-pattern name heuristic)
  aggregator with upstream tracking: n/a — NO witness matched the
    aggregator heuristic, so nothing was measured. This is NOT
    100% coverage, and --strict below passes vacuously.
OK                                     --strict exit code = 0
```

### Changes

1. `else 100.0` → `else None`, and the percentage line is skipped entirely
   rather than printed with a flattering number. **No percentage beats a wrong
   one.**
2. The aggregator count now states its own denominator and its method inline:
   `6   (of 2643 scanned, by a 9-pattern name heuristic)`.
3. The vacuous `--strict` pass is **named in the output** rather than left for a
   reader to infer.

### Deliberately NOT changed

The exit code. `--strict` still passes when the set is empty — the same
visible-not-fatal criterion applied to `MISSING` (#1), coverage (#2, #3) and
`SKIP` (#5). Making an empty heuristic fatal is a policy call for the gate's
owner; this bean's criterion is that the emptiness be legible, and now it says
so in words.

### Checked, live figures unchanged

Normal run is behaviourally identical: `scanned 2643 (76 audit-exempt)`,
`with upstream_witness_hashes: 2 (0.1%)`, `aggregator witnesses: 6`,
`aggregator with upstream tracking: 0 (0.0%)`, `WARN: 6 untracked aggregator(s)`.
Note this audit was already honest about its main denominators — it prints
`scanned`, `with`, and `without` — which is why only the empty-set branch needed
work.

---

## Tier-2 item FIXED 2026-08-23 — `block-manifest-audit.ts:284,362`, and the file already knew

Filed in Tier 2 as *"one failed chapter silently skips every block under it"*.
Confirmed, and it is worse than that phrasing: the `catch` sets `out = null`
wholesale, so **one unreadable chapter discards the listing for the entire
paper**, not just its own blocks. That null is then cached.

### The sentence it prints instead

```ts
const listed = await listedInPaper(paperDir);
if (listed === null) continue;   // :362 — silent
...
if (!quiet && !unlisted.length) {
  console.log("block-manifest-audit: every manifest in this diff loads and is listed.");
}
```

A skipped block never reaches `unlisted`, so `unlisted.length` is 0 and the
success line fires. Demonstrated end to end by making one chapter manifest
unparseable and running the **committed** version against a block under it:

```
block-manifest-audit: every manifest in this diff loads and is listed.
exit=0
```

**Both halves of that sentence are false.** A manifest demonstrably does not
load, and nothing was compared against the paper. This runs in CI
(`scripts/check-sidecars.sh:326`, `--diff` mode).

### The file documents this exact harm, ten lines above the defect

> *"silence here is how the 2026-07-18 clarity drain moved five fluid-dynamics
> remarks out of the paper while reporting itself 'manifest-safe'."*

The comment was written to justify reporting unlisted blocks as a warning. Two
`continue`s below it reintroduce precisely the silence it blames — which is the
clearest single illustration this bean has of the pattern being *systemic rather
than careless*.

### After

```
⚠ block-manifest-audit: 1 of 1 block(s) were
  NOT checked against a paper manifest. This is not a pass — nothing was
  compared for them, so a block missing from the paper would not show up here:
    …/gluon-model-comparison.md
      the paper listing at content/quantum-observable-universe could not be
      built: AggregateError: 3 errors building "…/appendix-knot-operations-
      archimedean.ts"
block-manifest-audit: 0 of 1 block(s) checked and listed; 1 NOT checked (above).
```

### Changes

1. Both silent `continue`s now push to an `unchecked[]` list with a **reason** —
   `no paper manifest found in any parent directory`, or the paper listing that
   could not be built and the error that stopped it.
2. `_listedError` records *why* a listing came back null, so the skip names the
   failing chapter file rather than shrugging.
3. The success line is now conditional. With skips it reads
   `N of M block(s) checked and listed; K NOT checked (above)` — a ratio, not a
   universal claim.
4. The caller's comment `// paper manifest unreadable; not this check's business`
   was also **wrong about the condition**: the `catch` fires on a *chapter*
   import failure too, not only the paper manifest. Replaced with what actually
   happens.

### `out = null` deliberately KEPT

The tempting "fix" is to return the partially-built set. That is worse: every
block in the chapters after the failure would be reported **unlisted** — false
positives in a check whose warnings ask an author to edit `sections[].blocks[]`.
The listing genuinely is unusable, so `null` is the honest value. What was
missing was never the null; it was that null read as *fine*. Comment added at
the `catch` saying so, so nobody "simplifies" it later.

### Verified

Normal path unchanged (`every manifest in this diff loads and is listed.`,
exit 0). Type errors identical before and after (8 pre-existing, all from
missing `@types/node` under a standalone `tsc`, none in the edited region). The
chapter manifest used to force the failure was restored from a copy and
`git status` confirmed clean, twice.

---

## Tier-2 item FIXED 2026-08-23 — `incomplete_coverage_audit.py:89,124`, where the conflation reaches an *assertion*

Filed as *"unparseable and clean both return `None`"*. Confirmed verbatim:

```python
except (OSError, UnicodeDecodeError, json.JSONDecodeError):
    return None          # :89  — could not read the file
...
if not results:
    return None          # :94  — read fine, genuinely clean
```

and `main` does `if result is None: continue`, so the two are the same event.

### Why this instance is the sharpest one in the bean

Every other item here mislabels a *printed* number. This one reaches a
**committed assertion**:

```python
.add_assertion(
    name="no_error_kind_entries",
    computed=1.0 if not rows else 0.0, expected=1.0,
    source="Closure gate: when this passes, every production witness has a
            complete row set for its declared … scope.",
)
```

`rows` is empty when nothing has errors **and** when nothing could be read. So a
corpus that failed to parse end to end would emit a witness asserting **closure
over the entire production scope**, `allPassed: true`, with a source sentence
saying exactly that. The gate is strongest precisely where it has read least.

### Changes

1. `_audit_witness` takes an optional `stats` dict and separates the two `None`s
   — same shape as the `coverage_out` parameter added to
   `witness_failed_assertion_audit.scan()` earlier in this bean, so the codebase
   grows one idiom rather than three.
2. The summary prints `scanned / with entries / clean / UNPARSEABLE`, the last
   annotated `<- not clean; not read at all`.
3. A non-zero unparseable count prints an explicit warning that the closure
   assertion fires on an empty row set and therefore rises with unread files.
4. **The assertion's `source` now carries its own denominator** — *"every
   production witness READ BY THIS RUN … 2718 scanned, 2718 clean, 0
   UNPARSEABLE. A non-zero unparseable count means this assertion passed over
   files it never opened."* The claim is now checkable from the artefact alone.
5. `scan_coverage` added to the witness data.

### Measured today — the current pass is genuine

```
  witnesses scanned:                 2718
  witnesses with error_kind entries: 0
  witnesses clean (read, no entries):2718
  witnesses UNPARSEABLE:             0
```

Zero unparseable, so the closure assertion is honestly earned right now. That is
worth stating: the fix does not accuse the current result, it makes the current
result *provable*. Its witness was last computed **2026-06-16** and is refreshed
here by a complete plain run of the corrected producer.

### `computed` left as-is, and a pre-existing float64 noted not fixed

The assertion still fires on `rows` only; I did not make unparseable files flip
it to 0.0. Same visible-not-fatal criterion as the rest of this bean, and the
`source` now states the caveat the number cannot.

Separately, the raw-float64 guard fires on this witness — `.assertions[0]`
`computed` / `expected` / `tolerance` are `1.0` / `1.0` / `0.0`. **Pre-existing,
not introduced here**, and the corpus convention for boolean assertions is the
string-int form used by `producer_importability_audit`
(`computed=str(int(...)), expected="1"`). Converting changes the assertion's
representation for anything reading this witness, so it is recorded rather than
folded into a coverage fix.

---

## Tier-2 item FIXED 2026-08-23 — `q0_cross_layer_fallback_scan.py:88`, the universal claim over unread files

Filed as *"drops files that already passed both pre-filters; 123-file candidate
population never printed."* Both halves confirmed; today's candidate count is
**124** (the corpus moved by one).

The drop is the worst-placed one in this bean: the `continue` after `ast.parse`
fires **only** on files that have already matched a muon prefix *and* a proton
token — that is, precisely the candidate set the scan exists to examine. A
candidate that does not parse is unexamined, and the scan then printed:

```
  None. No producer switches q₀ layer on its error path.
```

### Demonstrated — the same corpus, two answers

Forcing `ast.parse` to fail on every candidate and running the **committed**
version:

```
  files with a MUON literal inside an `except` handler
  AND a proton accessor in the same file : 0

  None. No producer switches q₀ layer on its error path.
--strict exit code = 0
```

**The true answer on this corpus today is 27 hits.** A broken parser turns 27
into a confident "None", at exit 0. Nothing in the old output distinguished the
two runs.

*After*, same forced failure:

```
  No hit among the 0 candidate(s) actually scanned — but 124 candidate(s) did
  NOT parse and were never examined. This is NOT 'no producer switches layer';
  it is 'none found in what was read':
    …
  NOTE: --strict exits 0 here. An unexamined candidate cannot
        produce a hit, so silence below is not evidence.
```

### Changes

1. The scan now counts and prints its funnel:
   `3744 .py walked → 124 CANDIDATES → 124 AST-scanned → 0 UNPARSEABLE`.
   The candidate population was never on screen before.
2. Unreadable files (before pre-filtering) are counted separately from
   unparseable candidates (after) — they are different facts and only the second
   is a coverage hole in this scan's own terms.
3. The `None` message now has two forms. With every candidate scanned it states
   its denominator: *"None, over all 124 candidate(s), every one AST-scanned."*
   With any unparseable it refuses the universal and lists what was skipped.
4. The vacuous `--strict` pass is named in the output.

### Verified

Normal run unchanged in substance: 124 candidates, 0 unparseable, **27 hits**
reported exactly as before, exit 0 without `--strict`. Not gate-wired and writes
no witness, so this fix carries no CI or artefact risk.

---

## Tier-2 item FIXED 2026-08-23 — `silent_self_check_audit.py:319`, where absence was read as *repair*

The `except SyntaxError: continue` is the ordinary version of this bean's shape.
What makes this instance worth its own entry is what the skip feeds:

```python
flagged = {f["script"] for f in findings}
state = "still FLAGGED" if s in flagged else f"fixed — {how}"
```

The regression check reads **"fixed" from ABSENCE among the findings** — and a
file that failed to parse is also absent. So a syntax error in a watched script
is reported as a **repair**, complete with the explanation of how it was
supposedly fixed.

### Demonstrated

Forcing every parse to fail and running the **committed** version:

```
  regression check — each hand-found defect is flagged or fixed:
    computations/chi_at_q0_via_matrix_m_mpfr.py
        fixed — q₀ resume guard + --fresh ported from the hoefsmit producer
    computations/substrate/deuteron_tower_fusion_frame_probe.py
        fixed — exits 1 when allPassed is False (qou-9d6h)
```

Nothing was parsed. Both repairs are certified anyway. The comment above that
block is careful — it explains that a bare count *"reads as a detector
regression the moment a repair lands"* — so the author had already thought about
this verdict being misread in one direction and not the other.

*After*, same forced failure:

```
    computations/chi_at_q0_via_matrix_m_mpfr.py
        UNKNOWN — this file did not parse, so no criterion ran on it
```

### Changes

1. Unparseable files are collected with their reason instead of `continue`-ing
   into silence, and the summary prints `scripts scanned N of M` plus an
   `UNPARSEABLE (no criterion ran)` block.
2. **The regression check gains a third state.** `UNKNOWN` when the watched file
   is among the unparseable — a two-state flagged/fixed test cannot be honest
   when the input can be missing.
3. `scan_coverage` (`scripts_seen`, `scripts_parsed`, `unparseable`) added to the
   witness.

### Verified

Normal run: **3074 of 3074 parsed, 0 unparseable**, 69 candidates (68 before —
the corpus moved), both watched scripts correctly `fixed`. The witness is
refreshed by a clean plain run of the corrected producer; the intermediate
monkeypatched test runs overwrote it and were reverted from a snapshot taken
before any run, with `git status` confirmed clean before the final run.

---

## Tier-2 item FIXED 2026-08-23 — `guarded_off_audit.py:136`, three facts behind one `None`

The last Tier-2 entry, and structurally the twin of `incomplete_coverage_audit`
above — including the same closure assertion:

```python
except (OSError, UnicodeDecodeError):
    return None          # :136 — could not read the file
if "import" not in text:
    return None          # :139 — pre-filtered, never a candidate
...                      #      — and read-and-clean is also None
.add_assertion(name="no_guarded_off_candidates",
               computed=1.0 if not rows else 0.0,
               source="Closure gate: when this passes, every canonical-witness
                       consumer runs unconditionally …")
```

Three different facts, one return value, feeding a closure gate that fires on an
empty row set. Fixed the same way, deliberately: `stats` parameter, printed
funnel, denominator embedded in the assertion `source`, `scan_coverage` in the
witness. Three audits in this bean now share one idiom rather than three.

### Measured

```
  python files seen:                2992
  scanned for guard shapes:         2990
  pre-filtered (no `import`):       2
  UNREADABLE (not scanned at all):  0
  scripts with guard-shape hits:    1
```

Zero unreadable, so the present result is sound; the two pre-filtered files are
now visible rather than folded into the same silence as a read failure.

## The witness is NOT refreshed here — the environment guard caught me

Running the corrected producer produced a correct witness that I did **not**
commit, because `WitnessBuilder` refused it on provenance grounds:

> ⚠ environment: the environment block records **LESS** than the witness on disk
> — downgraded numpy 2.5.0 → 2.4.6; python 3.13.12 → 3.11.15; scipy 1.18.0 →
> 1.17.1. … install it and re-run rather than committing the weaker record; the
> numbers can be identical while the provenance silently degrades.

The committed witness was produced in a **stronger** container than this one.
Refreshing it here would have traded a coverage improvement for a provenance
regression — a straight downgrade of the artefact, with the numbers looking fine.
Witness restored from a pre-run snapshot; **source change committed alone**.

Consequence, stated rather than hidden: the committed `guarded-off-audit.witness.json`
does not yet carry `scan_coverage`. The next run in a current container will add
it. That is the correct order.

### Checked the two witnesses I DID refresh earlier in this bean

Both were produced in an environment **identical** to their predecessors —
`git show <commit>^:<witness>` reports `python 3.11.15 / numpy 2.4.6 / scipy
1.17.1` before and after for `witness-provenance-audit` and
`incomplete-coverage-audit`, and neither run emitted the environment warning. No
downgrade was committed. Verified rather than assumed, because this failure mode
is invisible in the numbers.

---

## STATE OF THIS BEAN — 2026-08-23

**All findings and all Tier-2 items are fixed.** Left `todo`, not `completed`,
for one reason recorded at the bottom.

| item | file | state |
|---|---|---|
| #1 | `extraction_wall_gate.py` | fixed — `MISSING` class, sentinel can no longer ratchet |
| #2 | `producer_importability_audit.py` | **reporting** fixed (`--scope-only`, denominator); **decision** open |
| #3 | `witness_failed_assertion_audit.py` | fixed — denominator printed; 519 re-measured and confirmed |
| #4 | `classify_production_reach.py` | fixed — search health, exit 3 when degraded; claim narrowed first |
| #5 | `scripts/guard_check.py` | fixed — tri-state; a crashed guard skips instead of reverting |
| #6 | `session-start-coord-sweep.sh` | fixed — **new finding**; refs fetched, 24 h window implemented |
| T2 | `witness_dependency_coverage_audit.py` | fixed — empty set no longer 100 % |
| T2 | `block-manifest-audit.ts` | fixed — unchecked blocks reported; CI path |
| T2 | `incomplete_coverage_audit.py` | fixed — unparseable ≠ clean; assertion carries its denominator |
| T2 | `q0_cross_layer_fallback_scan.py` | fixed — candidate funnel printed; no universal over unread files |
| T2 | `silent_self_check_audit.py` | fixed — regression check gains `UNKNOWN` |
| T2 | `guarded_off_audit.py` | fixed — three facts separated; witness deliberately not refreshed |

**Every fix was demonstrated old-vs-new** under a forced failure, not argued
from the source.

### One consistent rule, applied twelve times

*Make the exclusion visible; do not make it fatal.* No exit code changed except
`classify_production_reach` (exit 3, and nothing consumes its status). Every gate
behaves identically on a healthy run. That was deliberate: turning these into
failures is a policy call for each gate's owner, and a sweep that reds twelve
gates at once gets reverted wholesale.

### Why still `todo`

`#2`'s **decision** half is open and is not mine: **359 witnesses** (286 naming
no producer, 73 naming one that is absent) that no staleness mechanism in the
corpus can ever check. The options are `qou-cds3`-adjacent — regenerate,
relocate the producer, or mark provenance-dead — and picking among them is scope,
not coverage. `qou-0uqm` items (2) dynamic reads and (3) machine inventories are
likewise open under their own bean.

### Prior art, restated

Four siblings found this shape independently in three days (see the PRIOR /
PARALLEL ART section and `qou-k3wq`). The corpus also already contained four
correct instances of the pattern before this bean started —
`noncanonical_reentry_audit.py`, `witness_hollowness_audit.py`,
`precision-gates.sh`, `check-sidecars.sh` — plus, found during this work, the
gate-wired `computations/witness_provenance_audit.py`, whose `UNCONFIRMED`
verdict is *"asserted as unchecked"*. **This was never a missing idea. It was an
inconsistently applied one**, and the useful next step is a shared helper rather
than a thirteenth hand-written coverage block.
