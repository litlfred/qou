# The witness-copy hand pass: four classes, and only two of them are defects

**Date:** 2026-09-06 · **Bean:** `qou-psjm` · **Audit:**
[`computations/audits/witness_value_copy_audit.py`](../../computations/audits/witness_value_copy_audit.py)

The audit answers *"does this literal equal a number some producer wrote into a
witness?"* It cannot answer *"and is that wrong?"* — that needed reading. This
records the reading, so the next agent inherits verdicts rather than re-deriving
them.

## What moved

| | before | after |
|---|---|---|
| NARROW findings | 266 | **232** |
| unique `file::literal` keys | 245 | **228** |
| copied from a `_deprecated/` witness | 17 | **13** |

−34 findings: **32** cleared by marking hand-confirmed deliberate sites, **2** by
fixing a false-positive class in the scanner itself.

## The four classes

### A. The literal is the detector's own subject — NOT a defect

A pin audit holds both canonical q₀ values as its **comparison basis**. Sourcing
them from a witness would make the detector agree with whatever it is auditing.
Same for a migration inventory whose purpose is to find code carrying a *retired*
pin — a retired pin has no live producer to read from, which is what makes it
retired.

Marked: `q0_hardcoded_pin_audit.py`, `q0_cross_layer_fallback_scan.py`,
`muon_pin_migration_stage1_inventory.py`.

### B. A classifier's own self-test fixtures — NOT a defect

`witness_regen_classify.py` carries 3 distinct values across 20 sites, all inside
`CASES` / `INFERRED_CASES`. Each pair reproduces a *real observed shape* — the
braid-encoding-audit `-h/2` anchor flip, the deuteron engine-label case — so the
verdict logic is pinned against it. Loading them from a witness would delete what
the test tests.

This is the same argument the audit already accepts for `tests/`, one directory
over. The scanner could not see it: `fixture_lines()` protects *string* literals,
and these are bare floats.

### C. A deliberately-frozen historical pin — NOT a defect

Seven `option_e_*` probes carry `1.1097090249`, each under a comment already
saying why: the probe exists *to show the published 0.11 % near-match was
obtained at this stale q₀*. Re-pinning would silently alter a recorded historical
result and delete the probe's subject.

### D. A producer's output typed into a consumer — **the defect**

The remaining 232. The tell is in the authors' own comments: *"from
`<x>.witness.json`"*, *"canonical cached"*, *"consumed from #3990"*, *"previous
probe"*, and — most explicitly — *"committed reference values (string-limited to
12 digits)"*.

## The flagship: one constant triple, twelve scripts, no shared module

`wlambda_covariance_epic_M1_*` — **12 sibling scripts** each typing in the same
three constants, every one annotated *"merged #5901"*:

```python
M_INF         = mp.mpf('0.300186614161')   # IO leading (CS) margin
SIG_RATIO_INF = mp.mpf('0.679609581496')   # sigma_D/sigma_A limit
RHO_INF       = mp.mpf('0.979796195657')   # IO leading rho_P
```

Twelve digits each, twelve copies, no import. If #5901's producer is re-run,
twelve scripts go stale at once and nothing detects it. This is the single
highest-value drain in the queue and the fix is one shared module.

**A second thing to check while there, which is NOT mine to decide.**
`margin_leg_decomposition.py` annotates `RHO_INF` as `# = 2 sqrt(6)/5`. Measured:

```
literal      0.979796195657
2·√6/5       0.97979589711327123928     rel 3.05e-07
```

They part company at the **6th** significant digit. Three distinct values near
0.9797 live in the corpus (`0.9797938112…`, `0.979796195657`,
`0.979798768510…`) and **none** is `2√6/5`. Either the annotation is a
*conjectured* closed form rather than an identity — in which case the constant
should be carried at the producer's full precision, not 12 digits — or it is an
identity, in which case the scripts should compute `2*mp.sqrt(6)/5` exactly and
the literal is a lossy stand-in. That is a question for the M1 epic's own
session; recorded here, not answered.

## Two scanner defects found by using it

1. **Trailing comments were scanned as code.** `line.strip().startswith("#")`
   catches whole-line comments and misses trailing ones. Exactly 2 findings, both
   real false positives. Fixed by tokenizing — a `#` inside a string literal is
   not a comment and a regex cannot tell the two apart.

2. **There was nowhere to record a verdict.** The sibling reference-literal gate
   honours `# reference-literal-intentional:`; this one honoured nothing, so a
   finding *reviewed and found deliberate* and a finding *nobody has looked at*
   landed in the same baseline bucket, indistinguishable. Added
   `# witness-copy-intentional:`, **AST-bounded**: a marker above an assignment
   covers that assignment's whole extent, so a 200-line fixture table needs one
   marker rather than twenty, and it stops exactly where the statement stops.
   The non-leak half is load-bearing and is self-tested — it is what forced
   `_PROTON_EXACT` to carry its own marker rather than inheriting `_MUON_EXACT`'s.

## What this does not claim

The 232 are **not** all confirmed defects. They are the residue after three
deliberate classes were removed by hand, and class D is where a defect *would*
live. Each still needs its own read before it is rewritten — the failure mode
here is automating the split, which got the type case wrong the first time it was
tried.
