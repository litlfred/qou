---
# qou-f64g
title: 'INFRA (gated + measured): float64 entry points in mpmath probes — 17546 hits, 4 prior beans, no gate until now'
status: in-progress
type: task
priority: high
tags:
    - infra
    - precision
    - probes
    - ci
    - reorg-2026-10-04
created_at: 2026-08-08T09:10:00Z
updated_at: 2026-10-04T15:11:00Z
parent: qou-9nnz
---


## Why this bean exists

There are **four** separate beans about float64 leaking into high-precision work:

* `j0th` — float64 and curve fitting in confinement LPMD
* `qou-gqt5` — 452 float64-padded witness values (fake precision)
* `qou-ny4j` — the committed `z` in the q-beta spectral bridge, 73.6 ppQ off,
  cause diagnosed as a stale/under-converged `q0`
* `qou-t0rf` — float64 entry point in Whitehead `c_sigma` torsion

Four beans, one recurring failure, and **no gate**. Every instance was found by
someone noticing a suspicious digit. Noticing does not scale.

The failure mode is silent by construction: mpmath promotes a float64 operand
without complaint, so the computation runs at ~16 digits while the witness header
still says `dps = 40`. Nothing errors, nothing warns, and the number looks fine
until someone checks it against a second route.

**It bit this lane on 2026-08-08.** Route 22's first run failed two gates at
exactly `4.3e-16` because an off-arc test point was written `1 + 0.4j` — a Python
complex literal — instead of `mpf(1) + 1j*mpf("0.4")`. Same session, the Route 22
probe also used `round(float(...))` three times to pull integers out of mpfs.

## The gate

`scripts/probe-float64-guard.py` + `.github/workflows/probe-float64-gate.yml`.

```sh
python3 scripts/probe-float64-guard.py                    # survey, exit 0
python3 scripts/probe-float64-guard.py --strict           # survey, exit 1 if any
python3 scripts/probe-float64-guard.py --diff <files...>  # GATE, exit 1 on a hit
```

Catches, in `computations/`:

| kind | what |
|---|---|
| `float-into-mpf` | `mpf(0.3)` — the digits are gone before `mpf` sees them |
| `float-in-arithmetic` | a non-exact literal as an arithmetic operand |
| `complex-literal` | `0.4j` — the one that bit Route 22 |
| `float-call` | `float(...)`, usually `round(float(x))`; use `int(nint(x))` |
| `float64-module` | `math` / `cmath` / `numpy` / `scipy` / `statistics` |

**It tests actual representability, not "is a float".** `2.5`, `0.5`, `1e9`, `1j`
are exactly representable — writing them costs nothing, and flagging them buries
the real hits. `0.3`, `0.4`, `1.4`, `0.2j` are not. The check compares the exact
rational the author *wrote* (`Fraction(Decimal(src))`) against the exact rational
the double *holds* (`Fraction(value)`). Floats in **comparisons** are tolerances,
not arithmetic, and are not flagged.

Escape hatch: `# float64-ok: <reason>` on the line.

Diff-scoped, exactly as `lean-orphan-gate.yml` is, and for the same reason —
see the backlog below. Workflow is `workflow_dispatch:` only (CI auto-triggers
disabled repo-wide, owner directive 2026-06-30), so **the local command is the
real gate today**.

## The backlog — measured, not gated

3201 files under `computations/`; **17546 hits in 2184 of them**.

| kind | count |
|---|---|
| `float-call` | 15951 |
| `float64-module` | 1175 |
| `float-in-arithmetic` | 408 |
| `float-into-mpf` | **10** |
| `complex-literal` | **2** |
| `syntax-error` | 2 |

A whole-tree gate would block every PR on that. Do **not** turn it on before the
backlog is worked — same argument as `qou-orph` step 3, and for the same reason:
converting a silent, survivable problem into a red default build is worse than
the status quo until someone has actually looked.

### The 12 sharpest — immediately actionable, each almost certainly a real defect

```
computations/alpha_em/bring_genus4_polarized_epstein_detprime_probe.py:165  mpf(0.3), mpf(1.4)
computations/alpha_em/bring_polarized_epstein_determinant_probe.py:112      mpf(0.3) x2, mpf(1.4) x2
computations/alpha_em/bring_polarized_epstein_determinant_probe.py:114      mpf(0.3), mpf(1.4)
computations/dilog_archimedean_partB_cusp_derivation_probe.py:91           mpf(0.4), mpf(1.3)
computations/probes/gk_d5_cyclic_dilog_4one_probe.py:157                    0.2j
computations/q_pochhammer_seed.py:47                                       0.1j
```

**Deliberately not fixed here.** Every one is in another lane, and changing
`mpf(0.3)` to `mpf("0.3")` moves the value in the 16th digit — which can flip a
tight gate in a lane I do not understand. Naming them precisely is the
deliverable; the owning lane should make the change and re-run its witnesses.

### And two files that do not parse at all

```
computations/option_e_multi_isotope_delta_lambda_probe_v3.py:74
computations/tier_2_hyperbolic_bridge3_pslq.py:85
```

Both `cannot assign to attribute here. Maybe you meant '==' instead of '='?`.
These are **syntax errors** — the files cannot run. Found incidentally because
the guard parses everything it scans. Worth its own look: a probe that cannot
execute has presumably not been executed, and whatever it was supposed to
establish is unestablished.

## To do

1. The 12 sharpest, by owning lane, each with its witness re-run.
2. The two unparseable files.
3. `float-call` (15951) is the bulk and is mostly benign — `float(x)` for a
   printed label costs nothing. Worth a narrower rule that flags only
   `float()` feeding arithmetic or `round()`, rather than draining 15951.
4. `float64-module` (1175): `import math` in a probe that also imports mpmath is
   the dangerous shape. Triage by whether the module's output reaches a witness.
5. Only after 1-4: consider `--strict` in CI.

## A note on the guard's own bugs, since it is a measuring instrument

Two were found and fixed while building it, and both inflated the count:

* **Byte vs character offsets.** `ast` column offsets are UTF-8 **byte** offsets;
  this corpus is full of Greek letters, so slicing the source string directly
  returned the wrong substring — it read `j` out of `1j` on such lines, failed
  the representability test, and produced phantom hits. Cost: ~106 false
  `float-in-arithmetic` and 6 false `complex-literal`.
* **`ast.get_source_segment` is O(file) per call**, so the survey took over five
  minutes and timed out. Slicing pre-split lines: 13.7 s.

A gate that overcounts gets ignored. Both fixes are in the file with comments
saying why.

## Refs

* `j0th`, `qou-gqt5`, `qou-ny4j`, `qou-t0rf` — the four prior beans
* `qou-orph` — the same diff-scoped-gate-plus-measured-backlog shape
* `qou-trns` — where the Route 22 instance surfaced



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
