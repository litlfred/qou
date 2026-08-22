---
# qou-0uqm
title: witness_provenance_audit's completeness ratio counts 320 never-checked witnesses as complete — exempt and passed render identically
status: todo
type: task
created_at: 2026-08-22T21:14:23Z
updated_at: 2026-08-22T21:14:23Z
---


Split out of `qou-ivhc`, which root-caused how an audit witness carrying the
wrong canonical pin and **zero provenance fields** reported clean for a week.

## The defect

`computations/audits/witness_provenance_audit.py` returns exempt verdicts
**before examining any field**:

```python
def classify(path):
    if any(path.name.endswith(suf) for suf in AUDIT_SUFFIXES):
        return "PROV_AUDIT_EXEMPT", []
```

and then counts every exempt class in the numerator of the headline metric:

```python
completeness_ratio = (n_ok + n_audit + n_no_reader + n_ack) / n_total
```

So `missing_fields: []` means **"not checked"** and is byte-identical to
**"checked and complete"**, and a ratio named *completeness* cannot fall when
coverage falls. `q0-consistency-audit.witness.json` reported
`{"missing_fields": []}` on 2026-08-21 while carrying no `computedAt`,
`scriptFile`, `scriptHash` or `engine` at all.

The exemptions themselves are **correct** — audit/state-tracking witnesses
legitimately record other artefacts' stale values, and applying provenance and
pin rules to them would generate constant false positives. The defect is purely
in how exclusion is reported.

## Fixed (additive only — no verdict, assertion or exit code changed)

1. Each entry gains **`evaluated: true|false`**, so an exempt row is
   distinguishable from a passing one in the emitted JSON.
2. Three figures added beside the existing ratio, which is **kept unchanged** for
   continuity with prior runs:
   - `excluded_not_evaluated`
   - `completeness_ratio_evaluated` — of those actually checked
   - `evaluated_coverage` — what share of the corpus was checked at all
3. The summary now prints the split.

`--strict` gates on `n_missing > 0` and is untouched.

## Measured after the change

```
  total scanned          : 2714
  PROV_OK                : 2350
  PROV_AUDIT_EXEMPT      : 76
  PROV_EXEMPT_NO_READER  : 242
  PROV_EXEMPT_ACKNOWLEDGED: 2
  PROV_MISSING           : 44
  excluded (NOT evaluated): 320  = 76 audit + 242 no-reader + 2 acknowledged
  completeness ratio     : 0.984   (counts all exempt classes as complete)
  ├─ of those EVALUATED  : 0.982   (2350/2394)
  └─ corpus evaluated    : 0.882   (2394/2714) — the rest was never checked
```

**Worth stating plainly: this does not make the corpus look worse.** Provenance
quality among checked witnesses is genuinely good — 0.982, essentially the same
as the old headline. The number that was hidden is **coverage: 0.882**, i.e. 320
witnesses (11.8 %) that no provenance rule has ever been applied to. Those are
two different questions and the single ratio answered only the flattering one.

`PROV_EXEMPT_NO_READER` at **242** is the largest exempt class by far and is worth
its own look: "no reader" is a claim about the corpus that ages, and a witness
that gains a consumer does not lose the exemption automatically.

## Not done

The same shape exists in two sibling detectors and is recorded in `qou-ivhc`:

- `q0_anchor_consistency_audit.py` — `Q0_FLIP: 0` over 663 evaluated of ~2585,
  with 1922 `Q0_ANCHOR_MISSING` unevaluable and not surfaced in the headline.
- `q0_consistency_audit.py` / `witness_constant_staleness.py` — the same
  audit-suffix carve-out, granted by **filename** rather than by content.

Not touched here because the anchor audit's `Q0_FLIP` is a **CI-failing gate**;
adding coverage reporting there is safe by the same additive pattern used above,
but it should be done deliberately rather than folded into this change.
