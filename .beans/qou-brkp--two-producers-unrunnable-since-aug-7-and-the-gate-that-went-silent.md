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
updated_at: 2026-08-08T09:40:00Z
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
