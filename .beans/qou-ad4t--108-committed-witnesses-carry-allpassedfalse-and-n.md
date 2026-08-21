---
# qou-ad4t
title: 108 committed witnesses carry allPassed:false and nothing reads them
status: todo
type: bug
created_at: 2026-08-21T15:08:23Z
updated_at: 2026-08-21T15:08:23Z
---

Found while fixing `qou-4e5k`: the witness whose assertion named that defect had
been sitting on main, failing, for twelve days. It is not alone.

## Measured on origin/main, 2026-08-21

Scanned every `*.witness.json` under `computations/` excluding `_deprecated/`:

    2681 dict-shaped witnesses scanned
     108 carry allPassed == false   (4.0%)

By month of `computedAt`:

    2026-05:  1      2026-06: 38      2026-07: 25      2026-08: 44

These are not detector *gaps*. The detectors fired, wrote a correct verdict to
disk, and the file was committed with the failure recorded in it. Nothing
consumes the field.

## The instance that proves it matters

`computations/tr-m-algebraic-q.witness.json`, computedAt 2026-08-09:

    allPassed: false
    symbolic_delta_matches_li2q   computed=1.3381598e-06  tol=1e-12  passed=FALSE

That assertion names, precisely and numerically, a real defect: two definitions
of the colour split δ disagreeing by exactly ℏ³. I rediscovered it independently
twelve days later by measuring a deuteron trace, having no idea the repo had
already written it down. Fixed under `qou-4e5k`; the same witness now reports
6.51e-19 and `allPassed: true`.

Its sibling assertion is the other half of the lesson. `algebraic_q0_matches_transfer`
was **passing** at `6.88e-08` against `tolerance=1e-07` — 69% of a budget whose
`source` string explained the residual away as a *"~1e-8 float64-eval floor of
the exact ℚ(q) form"*. It was not a floor; it was the same δ error. With δ
corrected the value is 3.50e-15, so the "floor" sat ~17 orders above the real
one. **A tolerance chosen to fit an unexplained gap converts a detector into a
rationalisation**, and it will pass forever.

## Why this is worth more than 108 individual fixes

A recorded-but-unread failure is strictly worse than no check, because the
existence of the check is what stops anyone looking. Three of the four items in
this arc's PR were found by hand-measuring things the corpus had already
measured.

Sample of what is sitting there (full list reproducible with the scan below):

    2026-08-15  canonical-derivation-pipeline-compliance   contract: WitnessBuilder usage (P30)
                                                           contract: Witness reproducibility (P32)
    2026-08-15  chi-convention-audit                       no_unknown_convention
                                                           no_unlabeled_chi_witness
    2026-08-19  audits/fitted-labelled-canonical-audit     no_fitted_labelled_canonical
    2026-08-10  probes/canonical-ordering-dof              closed_form_matches_full_trace

The `chi-convention-audit` and `fitted-labelled-canonical-audit` rows are
especially pointed: those are *the corpus's own discipline checks*, red, ignored.

## Next step

Two things, in order:

1. **A gate.** Something must fail when a witness with `allPassed: false` is
   committed. `scripts/precision-gates.sh` is the established hand-run preflight
   and has the right shape; a `--changed` mode makes it cheap. Note the standing
   ruling (AGENTS.md, 2026-08-09) that `witness-staleness.yml` stays
   `workflow_dispatch`-only — so this belongs in the preflight, not in CI, and
   re-proposing the trigger is out of scope.
2. **Triage the 108, oldest first.** Each is one of: a real defect (fix it), a
   tolerance that was always wrong (fix the tolerance and say why), or a probe
   recording an expected negative (which should not be using `allPassed` at all).
   The third category is the one to identify first, because it is the reason the
   field became ignorable.

## Reproduce

    python3 - <<'PY'
    import json, pathlib
    for p in sorted(pathlib.Path("computations").rglob("*.witness.json")):
        if "_deprecated" in str(p): continue
        try: w = json.loads(p.read_text())
        except Exception: continue
        if isinstance(w, dict) and w.get("allPassed") is False:
            fails = [a.get("name") for a in (w.get("assertions") or [])
                     if isinstance(a, dict) and a.get("passed") is False]
            print(str(w.get("computedAt",""))[:10], p, fails)
    PY
