---
# qou-s16e
title: 'T5: no-free-parameter certificate for the mass chain'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-tseries
    - 8f-open
created_at: 2026-08-03T23:27:17Z
updated_at: 2026-10-10T12:01:25Z
parent: qou-8lxd
pr: 8221
---

Prove predict(obs) is a closed term with no numeric literal untraceable to a CODATA-tagged calibration or a proved categorical constant. Half-built: canonical_mass facade + hidden-CODATA-literal rollup (bean 46ke).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-06 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Measured 2026-10-10 — "half-built" UNDERSTATES it, and the bean's own TARGET is the wrong target

Two corrections, the second the load-bearing one.

### 1. The certificate is BUILT, not half-built

`computations/no_free_parameter_certificate.py` exists, runs, and emits
`no-free-parameter-certificate.witness.json`. Live state, read from the witness
(`scriptHash 3c6b46da0fb6`, computed 2026-09-14):

| entry point | modules | unresolved | UNTRACEABLE |
|---|---:|---:|---:|
| `canonical_mass` | 11 | 0 | **0** |
| `per_observable_100x_status` | 10 | 0 | **0** |
| `meson_mass_from_hecke` | 8 | 0 | **0** |
| `binding_K_direct` | 7 | 0 | **0** |
| `qbeta_t4_stokes3_crux_probe` | 2 | 0 | 1 |

17 modules in the closure, **0 unresolved imports**. The one `UNTRACEABLE` is
`A_omega = 3` and it is **red by design** — adjudicated free in the witness
itself, backed by sorry-free `QOU/QBeta/AfreeThetaConstraint.lean` (two anchor
equations in three unknowns), and `scripts/precision-gates.sh:31` says so in
as many words. So nothing here is an open defect.

### 2. `predict(obs)` is NOT a closed term — it is a data lookup

This bean asks to *"prove `predict(obs)` is a closed term with no numeric
literal untraceable to a CODATA-tagged calibration or a proved categorical
constant"*. `qou_mass.api.predict()` contains no such term. It calls
`_lookup_row(Z, N)`, which loads a per-Z JSON shard and returns the stored
`M_pred_MeV` / `err_ppm` **verbatim**. There is no arithmetic to audit.

Measured by importing the committed classifier and pointing its `_resolve` at
`api.py`:

| entry point | closure | literals classified |
|---|---:|---:|
| `canonical_mass` | 11 | 10 |
| `per_observable_100x_status` | 10 | 13 |
| `meson_mass_from_hecke` | 8 | 23 |
| `binding_K_direct` | 7 | **0** |
| **`qou_mass.api`** | **1** | **0** |

**The literal count is not the signal** — `binding_K_direct` classifies 0 over
a 7-module closure, so a bare zero proves nothing. The signal is the **closure
collapsing to 1**: the walk never left the file. Three measured causes, none a
missed case:

- `SEARCH_ROOTS` is four paths under `computations/` and
  `tools/qou-substrate/`; the `qou-mass` tree is not among them.
- Every first-party import in `api.py` is **relative** (`from .prediction
  import …`, `from ._internal.codata_constants import U_MEV`), which a
  bare-name resolver looks for as a sibling of `computations/`.
- Two of those are **deferred inside function bodies** (lines 238, 381), so a
  top-level import walk misses them even with the roots corrected.

### 🛑 Do NOT close this by adding `qou-mass` as a sixth entry point

That is the obvious repair and it would make the false all-clear **more**
convincing rather than more meaningful: `predict()` does no arithmetic at any
closure size, so a literal-classifying audit prints a clean `0 UNTRACEABLE`
however far it walks. Recorded as detector-blindness taxonomy **row 56** (was 55; renumbered 2026-10-10 when main appended its own 55th).

### The path IS traceable — by witness provenance, not literal classification

So this is a detector-scope finding, **not** a finding against `qou-mass`. All
**120** shards under `qou-mass/src/qou_mass/data/isotopes/` (**3558** rows)
carry `scriptFile canonical_isotope_witness.py`, one uniform `scriptHash
e56cabeee1ea`, a `commitSha`, and `q0Anchor proton` — 120/120, no field
missing — and all 120 are **byte-identical** to their `computations/` sources
(sha256, pairwise). There is no free parameter hiding in that path; the
certificate simply cannot be the thing that says so.

### What remains open, and why this bean stays `todo`

1. **The verb.** The certificate's own docstring forecloses it: *"This is a
   **high-recall static detector**, not a proof … A clean run is *evidence*
   the path is parameter-free, **never a theorem** that it is."* T5 asks for a
   proof. What exists is evidence.
2. **The facade path needs a provenance audit, not a literal audit** — does
   every shard row resolve to a producer run whose `scriptHash` is current?
   The three structural facts above are pinned by a guard
   (`computations/audits/predict_path_literal_scope_probe.py`, `--selftest`
   pins the catch and the limit); the staleness question is not.
3. `A_omega = 3` is a genuine free parameter in the θ channel and is not
   closeable here — `AfreeThetaConstraint.lean` proves the underdetermination.

Re-tagged `8f-open`: this is formalisation research, not the mechanical work
the reorg's title-based tagging implied.

## Implementation Note (PR #8221)
- Implemented in `folio/quantum-observable-universe/lean/QOU/Eightfold/TorusZeroVolumeConnectedRankOneBringChiralityMassClosureAndJordanTwentySix.lean` and `computations/probes/torus_zero_volume_connected_rank_one_bring_chirality_mass_closure_and_jordan_twenty_six_probe.py` (witness `computations/probes/torus-zero-volume-connected-rank-one-bring-chirality-mass-closure-and-jordan-twenty-six.witness.json`, `3849d3633186444056f013bfbcda743be84b0a9c`).
