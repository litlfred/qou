# Changelog

All notable changes to `qou-mass` are recorded here.

The version policy is in
[`src/qou_mass/_version.py`](src/qou_mass/_version.py): **MAJOR** for any
witness-JSON change (modulo timestamps), any removed or renamed public symbol,
or any default change; **MINOR** for new public symbols, optional kwargs or
observables; **PATCH** for fixes, performance and docs.

## 1.0.0 — 2026-08-15

**MAJOR — every bundled `tr_M` value changes.** This is a data release: no
public symbol is added, removed or renamed, and no signature changes. The
bundled witness that `canonical_braid()` and the fast paths read has been
regenerated, and under the version policy a witness-JSON change is MAJOR on
its own.

### The bundled shard was a pre-convention-D artifact

`data/canonical-mass-table-extended.witness.json` was a hand-copied
**2026-05-19** vintage (`scriptHash 9c80f63797ce`, engine
`markov_peel+mpmath`). Since then the corpus moved to **trace convention D**
(`z = q³/(q²+1)`, the SU(2)/Temperley–Lieb Markov parameter). The shard was
never regenerated, so the package shipped convention-C traces.

Regenerated against the current pipeline. `tr_M_q0_canonical_50dps` moves on
every row:

| atom | 1.0.0 | 0.1.0a1 | change |
|---|---|---|---|
| p | 1.14575978228784 | 1.06530622859239 | +7.6 % |
| n | 0.98774375668766 | 0.92323329716958 | +7.0 % |
| ²H | 0.57509095868245 | 0.38828647154771 | +48 % |
| ³H | 0.22931014718283 | 0.10405211867553 | +120 % |
| ³He | 0.40376713848383 | 0.20654085856226 | +95 % |
| ⁴He | 0.16097419322912 | 0.05534834587670 | +191 % |
| ⁵Li | 0.11300280953161 | 0.02944139370040 | +284 % |
| ⁶Li | 0.04505204699243 | 0.00788963720285 | +471 % |

`prediction_MeV_50dps` for the nucleons moves far less — 938.2718526 →
938.2720894 MeV for the proton, 939.5651847 → 939.5654228 MeV for the neutron
(~0.25 ppm) — because the convention change is largely absorbed downstream of
the trace.

**If you have recorded `tr_M` values from 0.1.0a1, they are convention C and
are not comparable to 1.0.0 values.** The predicted masses are comparable.

### `canonical_braid()` no longer collapses the proton–neutron interface

`BraidWord.crossing_types` previously reported every averaged crossing as
`"averaged"`. The canonical classifier distinguishes two:

- `averaged` — colour-blind, `d = −h/2`, the intra-nucleon interfaces;
- `averaged_weighted` — colour-weighted, `d = −h(½ − δ/4)` with
  δ = the substrate flavour split, carried by the one proton–neutron bond.

Collapsing them erased the p–n asymmetry from the reported word. Every
multi-nucleon row is affected; p and n are unchanged, having no p–n bond:

```
²H   averaged 5 -> averaged 4 + averaged_weighted 1
³H   averaged 7 -> averaged 6 + averaged_weighted 1
³He  averaged 7 -> averaged 6 + averaged_weighted 1
⁴He  averaged 9 -> averaged 8 + averaged_weighted 1
⁵Li  averaged 11 -> averaged 10 + averaged_weighted 1
⁶Li  averaged 13 -> averaged 12 + averaged_weighted 1
```

Code that matches on `crossing_types` with `== "averaged"` will now miss the
interface crossing. Match on the `averaged` prefix, or handle both labels.

### Fixed

- **`predict()` raised `TypeError` for every atom.** `api.py` computed
  `err_pct * 1e4` where `err_pct` is a `Decimal` — the witness is loaded with
  `parse_float=Decimal` to preserve precision, and Decimal does not mix with
  float. Every call reaching the `ppm_vs_codata` branch died, which is most
  of them. Now scaled by `Decimal(10_000)`, keeping the exactness that
  `parse_float=Decimal` was chosen for. This was live in 0.1.0a1 and is
  unrelated to the data change above; it was found by running the test suite
  during this release.
- The producer's witness `description` read `unknown method 'branching'` for
  its own default method, and likewise for `auto` — the provenance string
  disclaimed the run that wrote it. Both now described.
- `--method auto` aborted the A < 2 rows outright when the optional
  `pyhecke_native` Rust extension was absent. It now falls back to the sympy
  `laurent_q` path and records the substitution in `method_used`. An explicit
  `--method laurent_q_rust` still errors, since there the kernel was asked for
  by name.

### Vendored `_internal/` is now generated, not hand-copied

Every one of the 14 hand-copied modules under `_internal/` had drifted from
its source in `computations/` — `witness_base` by 815 lines, `q_parameter` by
418, and `canonical_braid_crossings` by a whole generation (it predated the
current crossing classifier). None of the drift was adaptation; the
vendored-only lines were simply older docstrings.

`scripts/sync-qou-mass-vendor.py` now generates them. It computes the
transitive import cone from named entry points (42 modules) rather than
reading a hand-kept list, copies them flat, and applies exactly two
transforms — flatten the `substrate/` `hecke/` `markov/` layout, and remove
the `_path_bridge` shim that only makes sense inside `computations/`. It also
carries the 17 `*.witness.json` files those modules load at runtime.

`--check` makes drift a test failure instead of a discovery months later.
**Do not hand-edit anything under `_internal/`** — run `--apply`.

### `canonical_braid()` has a live path

Previously it answered only for the eight atoms in the bundled shard and
returned an empty word for anything else — the explicit word was deferred as
"P3 vendoring work", and its test was skipped. Both are done.

Outside the shard's range the word is now **computed** from the vendored
`_internal.canonical_braid_crossings`. ⁷Li, which the shard does not carry:

```python
>>> qou_mass.canonical_braid(Z=3, N=4)
BraidWord(n_strands=21, ...)   # 83 crossings
# sigma 40, sigma_inv 28, averaged 14, averaged_weighted 1
```

The shard is still consulted first, deliberately: it is the recorded
artifact, so preferring it keeps answers reproducible against a published
witness instead of varying with the installed dependency set. The live path
is the fallback.

Unblocking it needed one upstream fix, a **layering inversion** in
`computations/substrate/codata_constants.py`. That module located
`ame2020.json` as `_WITNESS_DIR.parent / "qou-mass" / "src" / "qou_mass" /
"data"` — the compute layer reaching into the package layer that vendors it,
by repo-relative path. In-repo it resolved; inside the wheel the repo segment
appeared twice and every AME lookup raised `FileNotFoundError`. It now
searches the known layouts and, on failure, names every path it tried.

`qou-substrate` and `pyhecke` became install dependencies: the vendored
modules are shims that re-export from them, so they are hard requirements of
the live path, not accelerators. Without them `canonical_braid()` degrades to
a strand count rather than raising.

## 0.1.0a1

Initial alpha: `predict()`, `compute_tr_M()`, `canonical_braid()`.
