---
# qou-brkp
title: 'BUG (fixed) + stale witness: a dps remediation broke 2 producers, and its own gate reported them clean'
status: in-progress
type: bug
priority: high
tags:
    - precision
    - probes
    - witnesses
    - infra
created_at: 2026-08-08T09:40:00Z
updated_at: 2026-09-04T21:36:37Z
---


## What happened

Commit `2bcbefee49` — *"fix(compute): raise dps before module-scope constants in
14 producers; make the gate position-aware"* — **broke 2 of the 14 files it
edited**, and they have been unrunnable since 2026-08-07.

The remediation inserted

```python
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
mp.dps = 50
```

**between a dict literal's opening brace and its first entry**:

```python
AME_MeV = {

mp.dps = 50
    "deuteron":  mpf("2.224566"),
}
```

`SyntaxError: cannot assign to attribute here.` The instinct was right and the
comment is correct; the insertion point was not.

* `computations/option_e_multi_isotope_delta_lambda_probe_v3.py:74`
* `computations/tier_2_hyperbolic_bridge3_pslq.py:85`

Both fixed here — the raise moved above the assignment — and both now run to
`exit 0`. This was safe to fix without owning the lane: the files could not
execute at all, so there was no passing behaviour to perturb.

## ⚠ Why nothing noticed: the gate went silent on the files it broke

The same commit built a position-aware detector,
`computations/mpf_import_time_dps_audit.py`. Its `scan_file` opened with

```python
try:
    tree = ast.parse(path.read_text(encoding="utf-8"))
except Exception:
    return []
```

**A file that does not parse returns zero findings — indistinguishable from
clean.** So the audit written to enforce dps-before-constants reported "nothing
wrong" for precisely the two files its own fix had destroyed. It could not have
caught this, and it will report clean for any future file that stops parsing.

Fixed here: a parse failure is now a `syntax-error` finding, and an unreadable
file an `unreadable` one. Self-tested against a deliberately broken file.

**The general lesson, and it is not specific to this audit:** a checker that
returns "no findings" on input it could not process is worse than no checker,
because it converts breakage into silence. Worth grepping the other audits for
the same `except: return []` shape.

Found incidentally by `scripts/probe-float64-guard.py` (bean `qou-f64g`), which
parses everything it scans and reports parse failures as findings.

## The stale witness — and what the staleness is NOT

`option-e-multi-isotope-delta-lambda-probe-v3.witness.json` was last computed
**2026-07-18**. Regenerating it now changes numbers at the **5th significant
digit**:

| | committed (2026-07-18) | regenerated |
|---|---|---|
| `tr_M` (deuteron) | `0.38828642407478887671…` | `0.38835720735922143663…` |
| `rel_error_pct` | `17.35639320698963…` | `17.34533468550543…` |

164 substantive lines change. **The witness in the repo does not reproduce.**

Two obvious explanations were tested and **both are wrong**:

1. **Not precision.** The natural reading is "the module-scope constants were
   built at dps=15 and now they are at 50". Tested by A/B: removing the
   module-scope raise and re-running gives **byte-identical** values. `main()`
   already set `mp.dps = 50` at line 107, so the working precision never
   changed; only two small literals were affected, and the computation is not
   sensitive to them at 1e-16.
2. **Not the inputs.** The three `chi-*-at-q0-50dps.witness.json` files it reads
   were touched once since, by `edbf6b3f32`, which added **metadata only** —
   `q0Anchor`, `scriptFile`, `commitSha` — and changed no numbers.

That leaves the other commit in the window, `4181efee6d` (*"repair the
migration-residue import/path breakage in 22 producers"*), which changed where
this script looks for its inputs:

```
-    repo_root = Path(__file__).resolve().parent.parent.parent
-        repo_root / "folio-assistant" / "computations"
+    repo_root = Path(__file__).resolve().parent.parent
+        repo_root / "computations"
```

so before the repo split it was reading from a different location. **That is a
hypothesis, not a finding** — the pre-split path does not exist in this repo, so
it cannot be tested from here. The owning lane should confirm it before treating
either number as correct.

## To do — for the owning lane, not this one

1. **Decide which `tr_M` is right.** The regenerated witness is committed here
   because a witness that does not reproduce is worse than one that does, but
   the 1e-4 shift is unexplained and the conclusions drawn from the old numbers
   (`rel_error_pct`, the "best offset family" ranking) may move.
2. Confirm or refute the pre-split-path hypothesis above.
3. Check the other 12 files from `2bcbefee49` — they parse, but "parses" is not
   "the raise landed in the right place". The now-fixed audit will say.
4. Grep the other audits for `except: return []` on parse.

## Refs

* `2bcbefee49` (the breaking commit), `4181efee6d`, `edbf6b3f32`
* `qou-f64g` (the float64 guard that surfaced this), `j0th`, `qou-gqt5`,
  `qou-ny4j`, `qou-t0rf`

---

## 2026-08-08 — cross-reference: this is an instance of `qou-w3dm`, plus what it adds

`qou-w3dm` landed on main at 07:40Z, from a sibling's #4513 prepare-merge gate:
**508 of 2749 witnesses (18%) carry a drifted `scriptHash`.** Witness staleness
is a main-side *class*, not a one-off, and this bean is an instance of it. Do not
work them separately without checking there.

**What this instance adds that the class scan cannot see.** `qou-w3dm` detects
drift by comparing `sha256(producer)[:12]` against the recorded `scriptHash` — a
purely static check. It would flag these two files as drifted, but it could not
tell you the more serious thing: **the producers could not run at all**, so the
drift was not merely un-refreshed, it was un-refreshable. A scriptHash scan and
a "does it parse" scan are different instruments, and this pair needed the
second. Worth adding a parse check to the `qou-w3dm` sweep — it is one line and
it separates "stale" from "impossible".

**And a provenance correction that lands on this bean's evidence.** Commit
`5ec185ed14` (main, 07:27Z) repaired five `chi-*` `scriptFile` claims: they
recorded `delta_lambda_empirical_tabulation.py` and the real producers are
`per_irrep_pole_deuteron_h6.py` / `per_irrep_pole_atom.py`. Zero numeric lines
changed.

That does not disturb the conclusion above — but it does change *why* it holds.
This bean's "not the inputs" finding must rest on the chi witnesses' **numbers**
being unchanged, which they are, and **not** on their provenance metadata, which
was wrong until this morning. Anyone re-deriving the argument from `scriptFile`
would have been reading a misattribution.

So the tally of what has been eliminated as the cause of the 1e-4 shift is
unchanged — not precision (A/B, byte-identical), not the inputs (numbers
unchanged across both touching commits) — and the pre-split-path hypothesis
remains the only candidate, still untested.

**The 5₂ sum rule remains verified to 80 dps, unproved.**

## 2026-09-04 — items 1 and 2: the premise is stale, the path hypothesis is moot, and the mechanism is NOT established

Worked item 2 ("confirm or refute the pre-split-path hypothesis"). The hypothesis
turns out to be unnecessary, and both items 1 and 2 rest on numbers that stopped
being live three weeks ago.

### The values this bean reasons about are superseded

    2026-07-18  committed    tr_M(deuteron) = 0.38828642407478887671...
    (this bean's "regenerated") 0.38835720735922143663...   <- became COMMITTED 2026-08-10
    2026-08-23  LIVE         tr_M(deuteron) = 0.57517224391777187082653534398618088915249435289286

The bean frames item 1 as choosing between two values differing at the 5th
significant figure (1e-4). Since 2026-08-23 the live value differs from both by
**48%**. Neither of the bean's candidates is a live option, so item 1 as written
("decide which tr_M is right") no longer has its two candidates in front of it.

Witness history is exactly two commits:
    2c68d7f34a  2026-08-10 19:24:58Z  -> 0.38835720735922143663...
    a0ee2ac5e9  2026-08-23             -> 0.57517224391777187082...
                (fix(qou-fl9i): regenerate 563 witnesses)

### Item 2: the pre-split-path hypothesis is MOOT, and still untestable here

Untestable, as the bean says: `folio-assistant/` is a symlink to the platform
repo and has no `computations/`, so the pre-split input location does not exist
in this checkout.

But it is also **unnecessary**: the value moved again on 2026-08-23, long after
the split, so no pre-split path is needed to explain the current number. Item 2
can be closed as moot rather than answered.

### THREE candidate explanations tested and REFUTED

**Convention D — refuted.** The chi-* witnesses carry a `convention` field, and it
reads `colour-weighted-averaged-crossing` at 2026-08-08 (efcaf79ed2), at
2026-08-10 (7e4d1aa6d0, the "convention D propagates downstream" commit) and at
HEAD. It never changed. Ordering confirms it independently: 7e4d1aa6d0 landed
18:22:42Z and the option_e regeneration 2c68d7f34a landed 19:24:58Z the SAME DAY,
so the 0.38835 value was already computed from post-convention-D inputs.

**Stale inputs — refuted.** The three chi-* witnesses this producer reads last
changed 2026-08-10. They were unchanged across the 2026-08-23 regeneration.

**Import-cone drift via `tr_m_atom_via_transfer.py` — refuted for THIS producer.**
`option_e_multi_isotope_delta_lambda_probe_v3.py` imports only stdlib, mpmath,
`_path_bridge` and `_precision`; it reads the chi-* witnesses as DATA FILES. That
module is not in its import cone. Worth stating because AGENTS.md documents the
identical number pair -- `tr_M_atom` moving `0.388 -> 0.575`, 48% -- as
import-cone drift in **`binding_canonical.py`**, a different producer. Same two
numbers, same quantity, different consumer: either one underlying quantity moved
corpus-wide, or it is a coincidence. Not settled here, and worth someone's time.

### What DID change, and why it does not explain the size

Between the two witness commits the producer changed exactly once,
`34b2a75d43` (fix(qou-fl9i): raise 822 sub-canonical mp.dps sites):

    -    mp.dps = 50
    +    set_compute_dps()
    +import _path_bridge
    +from _precision import set_compute_dps

That is the whole diff. `set_compute_dps()` resolves to 70 dps in this tree, so
the change is 50 -> 70.

**A 50 -> 70 dps raise cannot move a value by 48%.** So `qou-fl9i` is the
OCCASION of the regeneration -- it is the commit that re-ran the producer -- and
I have NOT established the MECHANISM. Stating that as an open negative rather
than dressing the occasion up as a cause.

The remaining shapes worth testing, none of them done here:
  - the added `import _path_bridge` changes `sys.path` and hence what some
    resolution inside the run picks up;
  - the on-disk chi-* files at regeneration time differed from the committed
    ones (a producer had written siblings, per the AGENTS.md sibling-witness
    hazard);
  - the 0.388 value was itself wrong and 0.575 is the correction -- which is
    what commit aeb31dfb41 the same day, "the tr_M-atom expectations were one
    stale snapshot, not three drifts" (qou-r9dv), asserts about a related
    quantity.

The third is the one I would test first: it would make item 1 answer itself.

### Bearing on item 1

Item 1 asks which tr_M is right. It cannot be answered against the pair the bean
names, because neither is live. Re-scoped, the question is whether 0.5751722439...
is correct, and `qou-r9dv` may already have answered it for the same quantity.
Still an owner call, but a smaller one than the bean implies -- and it should be
asked about the LIVE number.
