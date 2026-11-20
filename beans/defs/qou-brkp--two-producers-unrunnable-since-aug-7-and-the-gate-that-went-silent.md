---
# qou-brkp
title: 'BUG (fixed) + stale witness: a dps remediation broke 2 producers, and its own gate reported them clean'
status: todo
type: bug
priority: high
tags:
    - witnesses
    - infra
    - reorg-2026-10-04
    - precision
    - probes
created_at: 2026-08-08T09:40:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
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

---

## Item 2 — MECHANISM ESTABLISHED (2026-09-05), and three of my own refutations above are wrong

The section immediately above closed item 2 with *"I have NOT established the
MECHANISM"* and offered three untested shapes. **The answer is a fourth shape,
none of the three, and the three "REFUTED" verdicts above are each wrong for a
different, reusable reason.** Probe:
[`computations/probes/trm_provenance_chain_probe.py`](computations/probes/trm_provenance_chain_probe.py)
(11/11), witness `trm-provenance-chain.witness.json`.

### The chain

**`option_e_multi_isotope_delta_lambda_probe_v3.py` does not compute `tr_M`.**
Its line 129 is `"tr_M": mpf(tr_M_data["tr_M_at_q0"])` — the field is copied
verbatim out of `chi-<atom>-at-q0-50dps.witness.json`. Asserted live for all
three atoms (checks `copy/*`). So the option_e move **is** the chi witness's
move, picked up with a 13-day lag: option_e last ran `2026-08-09T00:41`, next
ran `2026-08-23T09:15` in the 563-witness sweep `a0ee2ac5e9`.

The chi witness moved in **`7e4d1aa6d0`** (2026-08-10 18:22:42, computed
18:20:37):

    0.38835714119779098941...  ->  0.57517224391777187082...   +48.1039 %

Across that move, measured per partition:

| | old | new |
|---|---|---|
| every `chi_lambda` | — | **byte-identical** |
| every `y_lambda` | — | **changed** |
| `scriptHash` | `c36a8a393fcd` | `c36a8a393fcd` |
| `scriptCommitSha`, `q0Anchor` (proton), `q0Value`, `dps` (50), `engineVersion` | — | **byte-identical** |

The proximate trigger is one line in a one-hop dependency: **`fcf629cf41`,
committed 18:20:04 — thirty-three seconds before the chi run** — switched
`_Y_LAMBDA_DEFAULT` in `tr_m_wenzl_bridge_mpfr.py` from
`y-lambda-mpfr-witness.json` to `y-lambda-mpfr-proton-witness.json`. The new
chi `y[(6,)]` matches the proton table to all 50 dps.

**But the SIZE is not the pin.** That commit budgets *"13 readers, ~11.5 ppb"*,
which is the μ–p separation — three orders of magnitude too small. Both y_λ
tables had themselves been **regenerated earlier the same day**, and the
regeneration changed the *weights*: at n = 6, `y[(6,)]` went `0.0591877…` →
`0.1153242…`, and the growth is monotone in row length —

    (3,3) x1.071   (4,2) x1.143   (5,1) x1.339   (6,) x1.948

— while every ≥3-row weight collapsed to ~1e-72. The weight mass migrated onto
the ≤2-row (SU(2)-admissible) partitions. **That is the 48 %.**

**Classification: a y_λ weight-table regeneration.** Not a pin swap, not a
convention swap, not a precision change, not a producer-source change. The
default swap is what made the chi producer *see* it 33 seconds later; the
regeneration is what created it.

### Why each of my three refutations failed

1. **"Convention D — refuted", on the `convention` field.** That field reads
   `colour-weighted-averaged-crossing` on both sides and never changed — but it
   names the **p/n colour** convention, not the Markov C-vs-D parameter. A field
   literally called `convention` that does not carry the convention in question.
   Reading it was *uninformative*, not exculpatory. (For the record the Markov
   `z` in the y_λ tables is convention D on both sides today,
   `0.61268805…`/`0.61268803…`, so the conclusion happened to be right and the
   evidence for it was empty.)
2. **"Convention D — refuted", on ordering.** I wrote that `2c68d7f34a` "landed
   19:24:58Z the SAME DAY, so the 0.38835 value was already computed from
   post-convention-D inputs." `19:24:58` is that commit's **commit time**; the
   option_e witness inside it was **computed `2026-08-09T00:41`**, 42.7 hours
   *earlier* and a day and a half *before* the convention-D commit. **Reading a
   commit timestamp as a compute timestamp inverted the ordering argument.**
3. **"Stale inputs — refuted."** I checked whether the chi witnesses changed *at*
   the 2026-08-23 regeneration. They did not — and that is the wrong endpoint.
   What matters is whether they changed **since the consumer last ran**, i.e.
   across 08-09 → 08-23, and they did, on 08-10. **I compared the input's change
   date against the consumer's new run instead of its previous one**, which is
   guaranteed to report "unchanged" for exactly the class of drift being looked
   for.
4. **"Import-cone drift — refuted for THIS producer."** True as stated and
   irrelevant twice over. option_e's dependency on the value runs through a
   **witness JSON file**, which no import-cone audit can see at all
   (`witness_import_cone_staleness_audit.py` walks Python imports); and the real
   drift is in the **chi** producer's cone (`tr_m_wenzl_bridge_mpfr`), not
   option_e's. Checking the consumer's imports for a data dependency answers a
   question nobody asked.

### A fifth trap, found while writing the probe

The ≥3-row weights in the proton y_λ table print as `2.188243022053045885…`
under a 40-character slice and are actually `2.188243…**e-72**`. I read the
truncation as the value and was one commit from filing a live *"the two y_λ
tables disagree on support"* defect. They do not: one serialises a vanishing
quantity as exact `0.0`, the other keeps its 1e-72 residue (checks
`vanishing/*`). **Never read a truncated numeric string as a value.**

### The committed chi witnesses are NOT stale

Checks `current/*`: each chi witness's `y_lambda` agrees with the **live**
default y_λ table to < 1e-45 (worst 6.78e-51), and `selfconsistent/*`:
`tr_M_at_q0 == Σ_λ y_λ·χ_λ` to < 1e-45. So the 08-10 values are current and
re-running the chi producer today would reproduce them.

### Not measured here

AGENTS.md's import-cone worked example attributes a 48 % `tr_M_atom` move to
**`binding_canonical.py` / `tr_m_atom_via_transfer.py`** — a *different*
producer pair from the one measured here, in the same date window at the same
magnitude. That is **consistent with** one upstream y_λ regeneration hitting
both, and it is *not* evidence for it; that pair was not measured and nothing
here claims it. Worth a separate look.

### Bearing on item 1 (unchanged, and now cheaper to ask)

Item 1 remains an owner call and must be asked about the **live**
`0.5751722439…`, not the dead pair the bean names. What is new is that the
number now has a derivation rather than a mystery attached to it: it is
`Σ_λ y_λ·χ_λ` over the ≤2-row partitions with the post-08-10 weights, and it is
reproducible from the committed inputs.

---

## Item 1 — ANSWERED, and it is NOT an owner call (2026-09-05)

The section above ended *"Still an owner call, but a smaller one than the bean
implies"*, and pointed at `qou-r9dv`. **I should have opened it. It answers the
question outright**, and the corpus-grep discipline exists for exactly this.

`aeb31dfb41` (2026-08-23 17:57, `fix(qou-r9dv): the tr_M-atom expectations were
one stale snapshot, not three drifts`) states that

    tr_M^atom(q_0) = 0.5751722439177718708265353439861808891524943528928

is **"confirmed by THREE independent methods, exact to every digit printed":**
the transfer route (`tr_m_atom_via_transfer.py`), the Hoefsmit / markov-peel
arbiter (`atomic_tr_m_mpfr_50dps.py --anchor proton`), and the chi-cache
combiner — and that the arbiter agrees on ³H (`0.2293101021`) and ³He
(`0.4037670369`) too, the same two values this session's probe re-verified.
Verified there against a clean `origin/main` worktree, so not a branch artifact.

A **fourth**, partially independent, agreement: `ka_additive_cluster_derivation
_probe.py:112` carries `TR_D_CACHED = 0.5751722439177718708265353439858617…`,
which agrees with the canonical string to **30 significant digits**
(rel `5.549e-31`, i.e. 16 orders inside the L1 1 ppQ target). Different route,
same number.

**So `0.5751722439…` is right, on four routes, and item 1 is closed as answered
rather than escalated.** Nothing here needs a decision.

### One correction back to `qou-r9dv`

`aeb31dfb41` attributes the move to *"most probably the 2026-08-09 convention
C→D switch in `y_lambda_at`"* — correctly hedged, and now superseded by
measurement. It was the **2026-08-10** `_Y_LAMBDA_DEFAULT` swap (`fcf629cf41`,
18:20:04) landing on a y_λ table that had been **regenerated the same day**;
and `y_lambda_at` is in any case **anchor-neutral and cache-free** (AGENTS.md,
bean `qou-c1ya` — the gate-and-cache shape moved into the dead
`_y_lambda_at_convention_C_HISTORICAL`). What `qou-r9dv` got right, and got
right from three numbers moving *consistently* (`sqrt(0.388357 · 0.0077684) =
0.054927`), is that it was **one** upstream change rather than three drifts.
This session names which one.

### The four deferred hardcodes are labelled, not silently stale

`aeb31dfb41` deliberately left four scripts carrying ~0.3884. Checked on
current `main`: all four now **announce themselves** —
`gap_a3_overshoot_robustness_check.py:52` and
`gap_a3_deuteron_A_D_overshoot.py:54` mark the value `CONVENTION C` and name
the live one; `canonical_tr_m_via_branching.py:537` says both sides of its
comparison have moved and names the three agreeing methods;
`ka_additive_cluster_derivation_probe.py` carries the live value at line 112.
Ten `computations/` files mention `0.3883` in total and none of them is an
unlabelled live use. No action.

---

## 🛑 RETRACTION — item 1's closure above is WITHDRAWN (2026-09-05, same day)

The section *"Item 1 — ANSWERED, and it is NOT an owner call"* closed item 1 on
four routes agreeing on `0.5751722439…`. **Withdrawn.** Full measurement and
scope: bean **`qou-49vn`**.

**The one thing that was never measured is the thing I asserted.** The same
entry, and PR #6861's body, both say *"re-running the chi producer today
reproduces them"*. I did not run it. When I did, an hour later:

| `chi_at_q0_via_hoefsmit_mpfr.py deuteron` | `tr_M_at_q0` |
|---|---|
| cached (resume: 11 partitions already cached) | `0.5751722439177718708265…` |
| `--fresh` | `0.1519683392042316075926…` |

Same container, same commit, same `mpmath 1.3.0` — the flag is the only
difference. A factor of **3.78**. And the markov-peel arbiter, a *different
script*, run today, gives `0.15196833920423160759266569775106614127124096465526`
— agreeing with `--fresh` to 49 of 50 digits, and with the Hoefsmit+Wenzl
bridge at 1e-51.

**Three live routes give `0.152…`; only the cache gives `0.575…`.**

**Why the closure was wrong in method, not just in fact.** `qou-r9dv` /
`aeb31dfb41` is dated **2026-08-23** and is a *baseline*. `d151898dd6`
(2026-08-30, *"pin-specific numerical chi caches — 5/6 atoms certified 1 ppQ"*)
and `41f517bf17` (2026-08-23, *"my own unblock turned a crash into silent cache
poisoning — guarded"*) both landed on this exact cache afterwards. I closed a
live question by quoting a stored number instead of re-deriving it — the
BASELINE trap, committed in the same session in which I wrote five TRAPs into
`compute-precision-auditor/MEMORY.md` warning about it.

**What is NOT retracted.** Item 2's mechanism stands: it is a measurement about
the **2026-08-10** transition (a **y_λ** weight-table regeneration), and every
figure in it is per-partition and internal to that pair of commits. The new
finding is a **χ** change at a *later* boundary and does not touch it. The
`trm_provenance_chain_probe` checks all still pass, because they compare the
committed witness against the committed y_λ table — which is exactly why they
did **not** catch this: **the probe never re-runs the producer.** That is a
real gap in the probe and is named in `qou-49vn`.

**Item 1 is once again OPEN**, and is now a bigger question than the bean posed:
not "which of two numbers", but whether the whole committed `chi-*-at-q0-50dps`
family is cache-carried past two fixes written to distrust that cache. It still
needs the Rust kernel restored before any verdict — see `qou-49vn` step 1.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8324, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
