---
# qou-ivhc
title: q0_consistency_audit is POLARITY-INVERTED after the proton ruling — it classifies the canonical pin as a stale-q0 bug, and has a --strict CI-gate mode
status: completed
type: task
priority: normal
created_at: 2026-08-22T15:27:20Z
updated_at: 2026-08-22T21:04:47Z
---


Found while tracing `qou-cds3`'s finding that 22 witnesses hold a muon value in a
`proton`-named field. The worst of those was
`computations/audits/q0-consistency-audit.witness.json`; this bean is its cause.

## The inversion

`computations/audits/q0_consistency_audit.py` docstring, verbatim:

> Canonical q₀ is the proton-anchored, habiro-refined value
> **C = 1.10997859555733471…** (`q_parameter.Q`). The stale value is the
> pre-habiro proton solution **A = 1.10997858275138…**, differing from C at the
> 8th sig-fig (~1.2e-8). Scripts that hardcoded A — instead of importing the
> canonical q₀ from `q_parameter` — silently keep computing at the stale
> constant.

Measured today:

```
q_parameter.Q_MP  = 1.10997858275138080759166909561076
Q_50_DIGIT_STR    = 1.10997858275138080759166909561076
```

So **`A` — the value this audit calls stale and flags as a bug — IS
`q_parameter.Q` today.** And `C`, which it calls canonical and attributes to
`q_parameter.Q`, is the hand-typed muon constant (`qou-khac`), itself measured
**8.54e-11 stale** against what `q_muon_at()` now derives.

The docstring's parenthetical *"(`q_parameter.Q`)"* is therefore false on its own
terms: the symbol it names holds the other value.

## Why this is not cosmetic

Three multipliers, in increasing order of consequence:

1. **It classifies correct code as a defect.** A hit on the canonical pin
   assigned to a live constant is classified `production-hardcode — real bug`.
   Every script that correctly hardcodes or reproduces `1.10997858275138…` is
   counted as a migration failure.

2. **It is built to become a CI gate.** From the same docstring: *"Run with
   `--strict` to exit non-zero when any production-hardcode remains (CI gate once
   the backlog is cleared)."* Enabling that gate today would **fail the build for
   using the canonical value**, and the backlog can never clear, because the
   thing it counts is now the correct thing to do.

3. **Its witness asserts the wrong canonical pin, with no way to notice.**
   `q0-consistency-audit.witness.json` carries
   `canonical_proton_q0 = 1.10997859555733471…` — a *muon* value in a field named
   `canonical_proton_q0` — and has **no `computedAt`, no `scriptFile`, no
   `scriptHash`, no `engine`**. Nothing in the provenance machinery can flag it as
   stale, because it records no provenance at all. It is one of only two audits in
   the tree whose witness is written by `out.write_text(json.dumps(...))` directly
   rather than through `WitnessBuilder`.

## Why it went unnoticed — and it is a taxonomy row

The audit was **correct when written**. Before 2026-05-28 the muon-anchored value
*was* the pin (`q_muon_at`'s own docstring: *"This was the pin until 2026-05-28;
now superseded by `q_at()` (m_p anchor)"*), and the 2026-08-15 owner ruling made
the proton pin canonical. The audit's polarity was never revisited.

The general shape, worth adding to
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`: **a detector that encodes
which value is canonical becomes an anti-detector the moment the ruling moves.**
It does not go quiet and it does not fail — it keeps reporting confidently, with
the sign flipped, and its report reads exactly like a real backlog. Every other
row in that taxonomy is a detector that *misses* something; this is one that
*asserts the opposite*.

## Not run, deliberately

`main()` writes the witness unconditionally (`:182`, no dry-run flag), so running
it would regenerate the inverted artefact and refresh its timestamp. The static
evidence above is decisive without it. Whoever fixes this should invert the
polarity **before** the next run, or the run will overwrite the current witness
with an equally wrong one that merely looks fresher.

## What it needs

1. Swap `A` and `C` throughout — canonical is the proton pin, stale is the
   pre-ruling muon value — and re-derive the `tr_M` leaf literals it screens for,
   which are quoted at the old canonical and are presumably inverted too.
2. Read the canonical value from `q_parameter` **at runtime** instead of quoting a
   literal in the docstring and the scan table. The whole defect is that the audit
   hardcodes the thing it exists to stop others hardcoding.
3. Emit through `WitnessBuilder` so the witness carries `computedAt`/`scriptHash`
   and the staleness gates can see it.
4. Do **not** enable `--strict` in CI until 1–3 land.

Related: `qou-cds3` (the 22 mislabelled witnesses, of which this is one),
`qou-khac` (the muon constant this audit calls canonical is itself stale by
8.54e-11).

---

## Summary of Changes (2026-08-22) — FIXED

`computations/audits/q0_consistency_audit.py` inverted and re-run.

### What changed

1. **Polarity swapped.** `OLD_Q0_PATTERNS` now scans for the pre-ruling **muon**
   family (`10997859555`, covering both the hand-typed `…55733…` and the
   `…55418…` variant); it previously scanned for the proton pin.
   `STALE_TRM_PATTERNS` swapped to the muon-anchored tr_M leaves.
   **No number was recomputed** — both sets were already written down in this
   file's own comments (`…062286/…332971/…864715` vs `…0614425445/…2332299/…2864240`),
   so the swap introduces no new numeric claim.
2. **The canonical pin is now read at runtime** from `q_parameter.Q_50_DIGIT_STR`
   instead of being quoted. This is the point: the file already *named*
   `q_parameter` as the canonical source at `canonical_q0_source` and then
   hardcoded a different (muon) literal beside it. Quoting the pin is the defect
   the audit exists to catch, and the literal went stale exactly that way.
3. **Provenance added** — `computedAt`, `scriptFile`, `scriptHash`, `engine`. The
   witness previously had none of these, so no staleness gate could see it.
4. Docstring rewritten to record the inversion, its cause, and that
   `legit-muon-xcheck` now carries more load (every muon literal matches the
   stale pattern, so intentional cross-checks rely on that classifier).

### Verified

Re-run output:

```
canonical_proton_q0  = 1.1099785827513808075916690956107688798744991218736   (runtime)
computedAt           = 2026-08-22T19:30:16Z
scriptHash           = 1ea40576a700
total_hits           = 488
  production-hardcode  288
  legit-muon-xcheck    113
  stale-docstring       87
```

**Regression check — the whole point.** Hits firing on the canonical proton pin:
**0**. Eight hits *mention* it, and all eight are lines carrying **both** values,
where the match is on the muon pattern and the proton digits are incidental
context — e.g. `_EXPECTED_PREFIX = {"muon": "1.109978595557", "proton":
"1.109978582751"}` (classified `legit-muon-xcheck`, correctly) and
`q₀_proton = 1.10997858275138…  q₀_muon = 1.10997859555418…` (`stale-docstring`).

### The 288 are a real backlog, and it is the SOURCE-side twin of `qou-cds3`

Sample: `a4_interface_kl_subpath_closure.py:27` and
`a4_option_e_color_tube_closure.py:23` both open with
`Q0_STR = "1.10997859555733471989976322048…"` — the stale hand-typed muon
constant, assigned to a live constant. `qou-cds3` measured 424 **witnesses**
carrying hand-typed muon values; this is the same migration surface in **source**,
at 288 sites.

Sharpest single instance: `tools/qou-substrate/tests/test_q0_anchor.py` **asserts**
`payload["q0Value"].startswith("1.109978595557")` — a test in the substrate
package that pins the stale muon value as the anchor and would fail if the
canonical pin were emitted.

### Note: the corpus already had a correct sibling audit

`computations/audits/q0_anchor_consistency_audit.py` carries
`_EXPECTED_PREFIX = {"muon": "1.109978595557", "proton": "1.109978582751"}` — the
right polarity. So two near-identically-named audits sat side by side, one correct
and one inverted, for a week. Worth a look at whether they should be one file;
not merged here, since that is a scoping decision rather than a defect fix.

### Still not done

`--strict` must stay **off in CI**. It now fails correctly rather than
incorrectly, but 288 real hits means enabling it gates the build on the whole
muon→proton source migration, which is `qou-cds3`'s unauthorised bulk sweep.

---

## Follow-up 2026-08-22 — the two q0 audits, and what "Q0_FLIP: 0" actually covers

### Correcting my own note above: they are NOT duplicates

I suggested `q0_anchor_consistency_audit.py` and `q0_consistency_audit.py` might
want merging. **Wrong — they audit different layers and both are needed:**

| | scans | asks |
|---|---|---|
| `q0_consistency_audit.py` (237 L) | **source `.py`** | is a stale q₀ *literal* hardcoded? |
| `q0_anchor_consistency_audit.py` (310 L) | **witness JSON** | does `q0Anchor` agree with `q0Value`? |

Complementary, not redundant. Merging them would be a regression.

One real but minor issue there: its docstring still frames the pins as
*"muon-anchored **canonical** vs proton-anchored physical"*, which the 2026-08-15
ruling reversed. Its `_EXPECTED_PREFIX = {"muon": "1.109978595557", "proton":
"1.109978582751"}` is correct and both anchors reach `Q0_OK`, so this is stale
prose, **not** a functional inversion like the one this bean fixed. Left alone.

### Ran it. `Q0_FLIP: 0` — over a 24 % denominator

```
Q0_OK             663
Q0_ANCHOR_MISSING 1922      <- 71 % of the corpus, unevaluable
Q0_AUDIT_EXEMPT     76
Q0_AMBIGUOUS        18
Q0_INDEPENDENT      35
Q0_FLIP              0
```

"Zero flips" is a real result about the **663 witnesses that declare an anchor**.
The other **1922 declare none**, so the detector cannot form a verdict on them —
and nothing in the headline says so. A reader taking `Q0_FLIP: 0` as "no anchor
defects in the corpus" is reading a number computed over less than a quarter of it.

### Q0_OK does not mean the payload is right — and this is `qou-cds3`'s 22

`probes/flavor-split-alpha-dilog-expansion.witness.json` is **Q0_OK**:

```
q0Anchor              = "muon"
q0Value               = 1.10997859555733…     <- agrees with q0Anchor, hence OK
data/proton_anchor/q0 = 1.10997859555733…     <- the SAME muon value, in a field named proton_anchor
```

The audit is **correct by its own rule**: it compares the *envelope* fields
`q0Anchor` and `q0Value`, and those agree. It never inspects the payload, so a
probe that computed both anchors and labelled one of them wrong passes cleanly.

That is precisely the class `qou-cds3` measured at **22 witnesses** (a muon value
in a `proton`-named field), and it is invisible **to both** q0 audits by
construction: the source audit scans `.py` not JSON, and the anchor audit scans
the envelope not the payload. Neither is broken; the gap is between them.

`h4-form-AB-cross-anchor-stability` is the same shape, also Q0_OK.

### And the two audits do not check each other

`q0-consistency-audit.witness.json` — the artefact this bean just fixed, which
until today asserted a muon value as `canonical_proton_q0` — is classified
**`Q0_AUDIT_EXEMPT`** by the anchor audit. So the audit whose own witness carried
the wrong canonical pin was exempt from the audit that checks pins. Not
necessarily wrong (audit witnesses describing *other* witnesses' pins plausibly
need an exemption), but worth stating: the exemption is why nothing caught it.

### What this suggests, not done here

A payload-level check — "no field whose *name* says `proton` may hold a value
matching the muon prefix, and vice versa" — would catch all 22 and costs a few
lines in the anchor audit, whose prefix map already has both values. I did not add
it: the anchor audit is a **CI-failing** gate (`Q0_FLIP`), adding a new failing
verdict to it is a scope change, and the 22 would then fail CI before anyone has
authorised the fix (`qou-cds3`'s sweep is still ungated). Recorded as the obvious
next step for whoever owns that gate.

---

## `--payload-check` added 2026-08-22 — the seam is now visible without gating on it

Added an **opt-in, diagnostic-only** payload check to
`computations/audits/q0_anchor_consistency_audit.py`. It reports fields whose
*name* says one anchor while the *value* carries the other's pin — the class
`Q0_OK`/`Q0_FLIP` cannot see, because they compare only the envelope
(`q0Anchor` vs `q0Value`).

```
  fields whose NAME and VALUE disagree on the anchor: 20
  witnesses affected: 20
    h4-form-AB-cross-anchor-stability     /parameters/q_proton    name=proton value=muon
    flavor-split-alpha-dilog-expansion    /data/proton_anchor/q0  name=proton value=muon
    qbeta-c6-c10-crossanchor-falsification /data/q_proton         name=proton value=muon
    … 17 more, every one name=proton value=muon
```

**Findings are printed, never written to the witness, and cannot change the exit
code.** `Q0_FLIP` stays the only gate — the 20 known hits would otherwise fail CI
before `qou-cds3`'s migration is authorised.

### One bug of mine, caught by reconciling against the earlier count

My first version keyed on the **immediate** JSON key and found 16. That misses
`/data/proton_anchor/q0`, where the anchor is named on the *parent* and the key is
just `q0`. Fixed to use the **innermost anchor-bearing path segment**, which reads
`/data/proton_anchor/q0` as proton and `/q0_pins/muon` as muon. 16 → **20**.

### 20 vs the 22 in `qou-cds3` — reconciled exactly, not hand-waved

- **−1**: `audits/q0-consistency-audit.witness.json` was one of the 22; this bean
  fixed it earlier today, so its `canonical_proton_q0` now holds the real proton
  pin and it is correctly no longer a hit.
- **−1**: `habiro-interpolation-wlambda.witness.json`
  (`/data/archimedean_F_lambda/proton_q0/q0 = 1.1099785955541805`) is
  **structurally invisible to this audit**. Its 14-char prefix is
  `1.109978595554`, and `_EXPECTED_PREFIX["muon"]` is `1.109978595557` — so the
  audit's prefix map recognises only **one** of the muon values. `qou-khac`
  established there are **three**.

That second one is a finding, not an oversight in my check: **the anchor audit is
built on a two-pin model** (`{muon, proton}`), and the muon side has since
fragmented. I did **not** widen `_EXPECTED_PREFIX` — it feeds the CI-failing
`Q0_FLIP` verdict, and changing what that constant matches changes gate behaviour
for every witness, which is not a diagnostic-flag-sized decision.

### Correcting a claim I made while building it

I wrote that the check is "not written to the witness and the artefact stays
byte-stable". The first half is true; the second is **not** — `WitnessBuilder`
records `invocation` and `reproduce`, so running with the flag writes
`… --payload-check` into the artefact. The committed witness is therefore from a
**plain** run, so it records the canonical invocation. Worth knowing before using
any flag on a witness-emitting audit.

---

## Root cause of the SURVIVAL: audit artefacts are exempt from every audit that would check them

The polarity bug is fixed. This entry answers the other question — *how did a
witness asserting the wrong canonical pin, with no provenance at all, sit
undetected for a week in a corpus with this much audit machinery?*

Three independent detectors each excluded it, **each correctly by its own rule**:

| detector | verdict for `q0-consistency-audit.witness.json` | mechanism |
|---|---|---|
| `witness_provenance_audit.py` | `PROV_AUDIT_EXEMPT`, `missing_fields: []` | `AUDIT_SUFFIXES` = `("-audit.witness.json", "-scan…", "-compliance…")` |
| `q0_anchor_consistency_audit.py` | `Q0_AUDIT_EXEMPT` | same audit-witness carve-out |
| `witness_constant_staleness.py` | exempt | *"audit / state-tracking witnesses are exempt … sometimes an OLD q₀ on purpose"* |

**The reporting is the trap, not the exemption.** In `witness_provenance_audit`:

```python
def classify(path):
    if any(path.name.endswith(suf) for suf in AUDIT_SUFFIXES):
        return "PROV_AUDIT_EXEMPT", []
```

The empty `missing_fields` is returned **before a single field is examined**. It
means *"not checked"* and reads, in the emitted JSON and in any aggregate view,
exactly like *"checked and complete"* — which is how this witness reported clean
on 2026-08-21 while carrying **no `computedAt`, no `scriptFile`, no `scriptHash`,
no `engine`** at all. **74 witnesses** currently sit in that bucket.

Each exemption is defensible on its own: audit witnesses are meta-artefacts that
legitimately record other artefacts' stale values, so applying staleness and pin
rules to them would produce constant false positives. **The defect is in the
union.** Nothing audits the auditors, and the carve-out is keyed on a *filename
suffix*, so it is granted by naming rather than by content.

### The pattern, and it is a taxonomy row

Third instance today of one shape — a detector reporting a clean number over a
population it never evaluated:

1. `Q0_FLIP: 0` — true of the 663 witnesses that declare an anchor; **1922 declare
   none** and are unevaluable, which the headline does not say.
2. `missing_fields: []` — returned by early-exit for 74 audit witnesses, before
   any field is read.
3. And the seam this bean already recorded: `Q0_OK` compares the envelope and
   never the payload, so 20 witnesses with `name=proton value=muon` pass.

In each case the detector is **correct** and its *summary statistic* is
misleading, because "excluded" and "passed" are rendered identically. Distinct
from the existing taxonomy rows, which are detectors blind to a *shape*; these are
detectors blind to their own *coverage*. Suggested row: **an exemption that emits
an empty finding-list is indistinguishable from a pass — report exclusions as a
separate count, never as zero findings.**

Cheap general fix, not applied here (it touches three producers and one is a CI
gate): have exempt paths emit `missing_fields: null` / a `not_evaluated` marker
rather than `[]`, and print exclusions on their own line in the summary.

## Status

Closing this bean. All four items from §"What it needs" are done:

1. **Polarity swapped** ✓ — stale is now the muon family; no number recomputed.
2. **Canonical read at runtime** ✓ from `q_parameter.Q_50_DIGIT_STR`.
3. **Provenance emitted** ✓ — `computedAt`, `scriptFile`, `scriptHash`, `engine`
   added directly. I did **not** convert the script to `WitnessBuilder`: it would
   nest the payload under `data` and change the artefact's shape, and while the
   only Python reader (`witness_constant_staleness.py`) merely names it in a
   docstring exemption, the shape change buys nothing the explicit fields do not
   already provide. Recorded as a deliberate choice, not an omission.
4. **`--strict` left off in CI** ✓ — it now fails correctly, on 288 real hits.

Plus `--payload-check` on the anchor audit, making the 20-witness seam measurable
without gating on it.

Follow-ups left for others, all recorded above: the three-valued muon prefix map
(`qou-khac`), the exemption-vs-pass reporting fix, and the 288 source-side
hardcodes (`qou-cds3`'s unauthorised sweep).

---

## ⚠ RETRACTION 2026-08-23 — my `test_q0_anchor.py` claim was WRONG

I wrote, in this bean and in commit `188768f8e`:

> Sharpest: `tools/qou-substrate/tests/test_q0_anchor.py` **asserts**
> `q0Value.startswith("1.109978595557")` — a test in the substrate package that
> pins the stale muon value as the anchor and would fail if the canonical pin
> were emitted.

**That file is not inverted and would not fail correct code.** Verified by
reading it:

- The muon assertions are **round-trips on payloads the test stamps itself**:
  `stamp_staleness_metadata(..., q0_anchor="muon", q0_value="1.10997859555733…")`
  followed by `assert payload["q0Value"].startswith("1.109978595557")`. That
  tests the stamping machinery, not which pin is canonical.
- It carries an explicit instruction not to make the "fix" I proposed: *"Do NOT
  'correct' this to the `q_muon_at()` value … a muon-tagged producer computes
  with the witness string, so a derived label would disagree with the number the
  witness reports."*
- And it already contains a **`RETRACTED 2026-08-15`** block removing the two
  tests that genuinely were wrong, whose note reads: *"The tests encoded the wrong
  invariant and would have failed correct code."*

So the file had already been fixed, three days before I called it a defect. I
matched on the literal `startswith("1.109978595557")` without reading what the
surrounding test was asserting — the same shape as the `F3a` retraction in
`qou-a613`: keying on a string and not checking what it was there **for**.

The genuine instances of this class are in `qou-fd0e`, and none of them is that
file.
