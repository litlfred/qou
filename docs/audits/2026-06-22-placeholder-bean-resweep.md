# Placeholder-bean re-sweep — claimed ~1038 → honest 81 actionable (2026-06-22)

**Date:** 2026-06-22
**Tooling:**
[`scripts/count-actionable-placeholders.ts`](../../scripts/count-actionable-placeholders.ts)
(honest counter) +
[`scripts/resweep-placeholder-beans.ts`](../../scripts/resweep-placeholder-beans.ts)
(driver).
**Status:** backlog-hygiene sweep. No paper content, Lean, or compute changed —
only `.beans/` metadata + the two scripts + this doc.

## Why

The 2026-06-22 orchestrator bean sweep created ~39 "Resolve N placeholders/TODOs
in `<scope>`" beans whose counts came from a naive marker grep. A manual audit of
`aj81` (qou/stochastic-mechanics, claimed 5) found the count was **0 actionable** —
every "marker" was a false positive (the phrase "sorry-**free**", `.qa.json`
reviewer notes, or legitimate §3b conjecture-class `sorry`s that must be retained).
Draining such beans blindly is busywork at best and a §3b violation at worst.

## The honest counter

`count-actionable-placeholders.ts` excludes the false-positive classes the sweep
counted:

- `.qa.json` / `.witness.json` sidecars (reviewer notes mention "sorry"/"placeholder");
- the word `sorry` in comments / docstrings / strings (e.g. "sorry-free") — Lean
  comments and strings are stripped before counting;
- a `sorry` carrying a `-- Ref:` citation (**decl-aware**: the `-- Ref:` above a
  multi-line signature is credited, which a fixed-window check misses);
- `.md` prose mentions.

It counts only **uncited `sorry`** + bare **`TODO`/`FIXME`** markers.

## Result — ~13× inflation

| | claimed | honest |
|---|---|---|
| **total across the placeholder beans** | **~1038** | **81** |

Disposition (`resweep-placeholder-beans.ts --apply`): **26 beans completed**
(honest 0 — false-positive-only), **10 annotated** with the real residual, **3
skipped** (`aj81` already audited; `i6p9` = `qou/lean` whole-tree overlap that
double-counts the subdir beans; `ixx4` = single-file scope).

### Beans with a genuine residual (annotated, left open)

| bean | scope | claimed | honest |
|---|---|---|---|
| `doth` | schema | 25 | 22 |
| `zslh` | qou/mass-theory | 103 | 8 |
| `95jh` | qou/lean/BraidKnot | 213 | 7 |
| `b3pe` | qou/lean/Archimedean | 87 | 4 |
| `ldup` | unital-groebner-bases | 29 | 4 |
| `mlt7` | qou/mass-endomorphism | 15 | 2 |
| `1osq` | qou/lean/Substrate (in-progress) | 5 | 1 |
| `8ehe` | qou/lean/MathlibExt | 5 | 1 |
| `ekb8` | qou/lean/Interactions | 17 | 1 |
| `xj99` | qou/quantum-observable-universes | 7 | 1 |

Even these honest counts overstate *agent-drainable* work: several residual items
are gated (documented `True:=trivial` / `∃,True:=sorry` vacuity-audit-axis stubs;
bib-human-review title verifications) rather than mechanical placeholder removals.

## Re-running

`resweep-placeholder-beans.ts` is idempotent (skips completed / already-swept
beans), so it can be re-run after future sweeps:

```bash
bun scripts/resweep-placeholder-beans.ts          # dry-run
bun scripts/resweep-placeholder-beans.ts --apply  # write via the beans CLI
```
