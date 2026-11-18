---
# qou-2cz1
title: Four local imports in computations/ name a module-level name that does not exist -- two producers cannot be imported, and scriptHash reports them IN SYNC
status: in-progress
type: task
priority: high
created_at: 2026-10-10T07:57:44Z
updated_at: 2026-11-15T13:05:00Z
parent: qou-5vkl
---

Found 2026-10-10 (PR #7546) while unblocking `qou-3kni`'s producer half. **Nothing
in `computations/` was edited** — see "Why no fix is proposed" below; it is not
caution, it is that three of the four have no mechanical answer.

## The finding

Four `from <local-module> import <name>` bindings in `computations/` name a
module-level name that **does not exist**. Two break the script at import time;
two sit inside a function and fire only when that path is taken.

| site | imports | from | status of the name |
|---|---|---|---|
| `snappy_cusp_seeding.py:47` | `IM_PERTURBATION` | `q_pochhammer_seed` | renamed to `IM_PERTURBATION_STR` (NO-FLOAT64, 2026-09-13) |
| `probes/qbeta_g3_annihilator_certification.py:52` | `tet_norm` | `probes/qbeta_g3_fourone_index_assembly` | module defines `tet_abs`; rename plausible, **unconfirmed** |
| `probes/qbeta_g3_annihilator_certification.py:52` | `_dense_mul` | same | **no candidate of any name** |
| `atom_braid_active_partitions.py:128` | `hook_length_dim_lambda` | `hecke/hecke_characters` | absent; no `__getattr__` |

`series_str`, imported on the same line as the two `qbeta_g3` names, **does**
exist (line 152) — so that import statement is half-valid, which is why the file
reads as maintained.

## Why no detector fires, and this is the reusable half

**The consumer's own file hash does not change.** `snappy_cusp_seeding.py`'s
`scriptHash` is `f4733c216049` and its witness records `f4733c216049` — **IN
SYNC** — with `computedAt 2026-08-28`, three weeks before the dependency was
renamed. So the witness claims currency with a producer that **cannot be
imported**, and every `scriptHash`-keyed staleness path reports it healthy.

This is `AGENTS.md`'s **import-cone drift** class, but one step worse than the
case that class was written for. There, a byte-stable producer's *number* moves
because a numeric module in its cone changed. Here the cone change does not move
a number — it stops the producer running at all, which no staleness metric can
express.

`witness_import_cone_staleness_audit.py` does **not** catch it. Run here, its
output is dominated by one mover (`substrate/experimental_constants.py`,
**2135** witnesses) and ranks by *"a cone module changed more recently than the
witness"* — a recency heuristic. It never asks whether the import resolves, and
`snappy_cusp_seeding` does not appear in its report.

**And `import snappy` fails first**, which is how this stayed hidden: every
container that tried to run the script died at line 42 before reaching line 47.
`qou-3kni` recorded the `ModuleNotFoundError` and stopped there, reasonably. The
second, deeper breakage is only visible once SnapPy is installed — and it is
(see below).

## The audit, and what it cost to calibrate

[`computations/audits/local_import_resolution_audit.py`](computations/audits/local_import_resolution_audit.py).
Pure AST: nothing is imported or executed, so **no producer writes a witness**
while it runs — which matters, because `AGENTS.md` records that producers write
*sibling* witnesses and a sweep that imports them leaves a dirty tree reading as
real work. Exits 1 when anything is unresolved, so it can be a gate.
`--selftest` asserts the one known true positive is found and four known-good
imports are not, and **fails** rather than passing quietly.

**The first version reported 34 and 30 were false positives.** Both causes are
blind spots worth recording, because both made the audit *over*-report, and an
over-reporting audit is abandoned as noise:

1. **Star re-export shims out of the tree.** `_precision` and `witness_base`
   are back-compat shims re-exporting from `qou_substrate.*`, so an
   enumeration of their own AST finds neither `set_compute_dps` nor
   `WitnessBuilder`. Now: a module whose exports cannot be fully enumerated is
   **UNDECIDABLE and skipped**, never guessed at. 8 modules.
2. **Ambiguous stems.** `witness_provenance_audit.py` exists in BOTH
   `computations/` and `computations/audits/`, and `setdefault` over
   `sorted()` silently read the wrong one — 7 false positives against a module
   whose names (`written_filenames:224`, `builder_names:270`) are plainly
   there. Which file a bare-name import resolves to depends on `sys.path`
   order, so it is genuinely undecidable statically. Now skipped. 2 modules.

A third class was correctly *not* a defect: `codata_constants` has a module
`__getattr__` implementing the 2026-05-10 `M_P_MEV -> M_P_MEV_VALIDATION`
rename, so its 24 flagged imports **resolve at runtime**. A module-level
`__getattr__` can serve any name, so such a module is undecidable too.

Live result: **5935 bindings checked, 4 unresolved, 8 undecidable, 2 ambiguous.**
Quote the undecidable and ambiguous counts with the 4 — they are the audit's
stated coverage limit, not noise.

## Why no fix is proposed

Only one of the four has a mechanical answer, and even that one is a judgement:

- `IM_PERTURBATION` was a **complex** value (`seeds = [s + IM_PERTURBATION for s
  in real_seeds]`, `s` real). The module now carries `IM_PERTURBATION_STR =
  "0.1"` and reconstructs it as `mpc(0, mpf(IM_PERTURBATION_STR))`. But the
  consumer's neighbourhood is **numpy/float** (`complex(s)` on SnapPy shapes,
  `np.argmin`, `float(seed.real)`), so putting an `mpf` there decides a
  NO-FLOAT64 question about which side of that boundary the perturbation lives
  on. That is a precision decision, not a rename.
- `tet_norm -> tet_abs` is *plausible* and unverified. A norm and an absolute
  value are not the same function in general.
- **`_dense_mul` has no candidate at all.** Something was removed, and guessing
  a replacement for a dense multiply is inventing mathematics.
- `hook_length_dim_lambda` likewise has no candidate in `hecke_characters`.

Per `AGENTS.md` §ASK THE OWNER and the owner's standing *"do not can with any
code changes that are speculation"*, three of these are speculation. Proposing a
patch for one and leaving three would also misrepresent the state.

## What it means for the corpus

- `snappy-cusp-seeding.witness.json` **cannot be regenerated** until this is
  fixed, so `qou-3kni` item 1 has a second blocker its text does not name.
- The two `probes/` scripts have **no witness**, so nothing claims currency —
  but per §"PROBES ARE NOT EXEMPT", a probe's conclusion is written into beans,
  audit docs and PR bodies where *nothing re-derives it*. A probe that cannot
  run is a conclusion that can never be re-checked. Treat any recorded
  `qbeta_g3_annihilator_certification` finding as unverifiable until it runs.
- Same family as `qou-n7ue` (two producers that crash and cannot be
  regenerated) but a **different mechanism**: those raise in logic, these fail
  to resolve a name. And `qou-m6gp` is the same *silent*-failure shape one level
  over — an `ImportError` read as a refutation.

## Options

1. **Fix all four, owner-directed per site.** Needs a decision on the mpf/float
   boundary and on what replaced `_dense_mul` and `hook_length_dim_lambda`.
   Then re-run `snappy_cusp_seeding` and commit the refreshed witness in the
   same commit (`durationMs` recorded as **45**, so the run is free).
2. **Fix only `IM_PERTURBATION`**, as the one with a known replacement, and
   leave the rest flagged. Unblocks `qou-3kni` item 1 and nothing else.
3. **Wire the audit into `scripts/precision-gates.sh`** so the class cannot
   recur, without fixing the four. Cheap, and the four stay visible.
4. **Do nothing.** The audit exists and reports them; a reader who runs it sees
   the list. Default.

**Recommendation (judgement, not a finding): 3 then 1.** Wiring the gate is in
§ASK-THE-OWNER exemption 1 by the same reasoning the warn-only precision hook
was accepted under — it makes a silent wrong state impossible — and it is the
half that stops the next rename doing this again. The four fixes want the owner
per site.

## A taxonomy row

This is a detector blind spot of the kind
`docs/audits/2026-08-15-detector-blindness-taxonomy.md` catalogues: the
staleness metric is a **file hash of the consumer**, and the defect is in the
*dependency's* namespace. Not added to the table in #7546 — that PR had already
corrected the table's row count once and this is a different arc. The two
calibration failures above (star re-export shims; ambiguous bare-name stems)
are candidate rows in their own right.

## Reproduce

    python3 -I computations/audits/local_import_resolution_audit.py --selftest
    python3 -I computations/audits/local_import_resolution_audit.py


## 2026-10-10 — 1 of the 4 is FIXED by a sibling session; 3 remain

`915e5a28c7` (session `016AEU7xkxdUcw9r7adTXgyr`, merged into
`claude/triangulation-citation-chain-2026-10-10`) fixes
`snappy_cusp_seeding.py` and re-runs both producers. Independent convergence:
that work and this measurement happened in parallel, which is the dynamic
AGENTS.md §"Parallel exploration is valuable" describes.

**They made the NO-FLOAT64 judgement this bean declined to guess, and took the
float side:**

```python
-from q_pochhammer_seed import IM_PERTURBATION
+from q_pochhammer_seed import IM_PERTURBATION_STR
-    seeds = [s + IM_PERTURBATION for s in real_seeds]
+    seeds = [s + complex(0, float(IM_PERTURBATION_STR)) for s in real_seeds]
```

**That is the defensible call, and it is not a precision regression**, which is
worth stating because `float(` in a `computations/` script is normally a defect.
The whole enclosing function is float-domain already — `complex(s)` on SnapPy's
shape parameters, `np.argmin` over the distances, `float(seed.real)` into the
witness — so an `mpf` here would have been a lone high-precision value inside a
float64 pipeline, which buys nothing and would have had to be cast back one line
later. It also restores the pre-rename behaviour exactly rather than changing
the computed object. The NO-FLOAT64 question for this arc is whether the
*pipeline* should be mpf, which is a different and larger change.

They also marked both dead labels `[no carrier]` in the Manuscript-references
block with a pointer to `qou-3kni`, and noted in the prose that the producer
"once named" the carrier-less conjecture rather than deleting the history.

### The 3 that remain, unchanged

| site | imports | status |
|---|---|---|
| `probes/qbeta_g3_annihilator_certification.py:52` | `tet_norm` | module defines `tet_abs`; rename **plausible, unverified** — a norm and an absolute value are not the same function |
| same | `_dense_mul` | **no candidate of any name** |
| `atom_braid_active_partitions.py:128` | `hook_length_dim_lambda` | absent from `hecke/hecke_characters`, no `__getattr__` |

The last one is **latent, not import-time**: it sits in a function body, in the
`else:` branch for the empty word (`χ_λ(1) = dim V_λ`), so the module imports
fine and fails only when that path is taken. That is harder to notice, not
easier.

Still no fix proposed for these three. `_dense_mul` in particular has nothing to
rename to — something was removed, and inventing a dense multiply is inventing
mathematics.

### The audit and the gate question are untouched

`computations/audits/local_import_resolution_audit.py` stands, and re-running it
after the merge is the way to confirm the count moved 4 → 3 rather than taking
it from this note. The recommendation above (option 3: wire it into
`scripts/precision-gates.sh` so the class cannot recur) is unaffected by any of
the four being fixed — a gate is about the next rename, not this one.


## 2026-11-15 — #7584 ported onto main (branch `claude/qou2cz1-port-2026-11-15`)

#7584 conflicted with main, which had already fixed the HA literal its own way
(889cb04f4: HA derived from `Q_50_DIGIT_STR` at 60 dps, chi via
`chi_lambda_braid_mpf`, errors recorded instead of swallowed). What landed on top:

1. `atom_braid_active_partitions.py`: the identity branch imports `specht_dim`
   (`hecke/hecke_characters.py:874`), not the absent `hook_length_dim_lambda`.
   The branch is dead on the committed witness (0 chi errors), so no number moves.
2. Same file: `match` now also requires zero chi errors. **Found while porting,
   not in #7584**: without `pyhecke_native` every partition raises
   `NotImplementedError` (mpfr_60dps needs the Rust kernel), observed = 0, and
   the headline assertion still PASSED. Recording the errors was half the fix;
   the bound itself was still vacuous.
3. `probes/qbeta_g3_annihilator_certification.py`: reduced to
   `trefoil_calibrate()` per the 2026-10-10 relayed ruling, taken verbatim from
   #7584 (ac520bba3b). Witness regenerated: 1 assertion, passes; the two
   retired FAILs are gone.

`local_import_resolution_audit.py` on this branch: **UNRESOLVED: 0** (5998
bindings checked). Stays `todo` until merged.

- **Round 92 (`litlfred/qou#8416`)**: Advanced in `feat/round92-jetmono-jetsign-kzratio-kzunit-kappacorr-43c1` (Commit 1 `b85484a2b9309c11a8832becee2e728a03219677`, Commit 2 `de3ca907bd3d3c7bb260ce5aa08259ade30c6cc9`, probe sha256 `7a5dfeb80aacf1b23a7e663221ecc9f97b20abf96256db6ae736e9dd7742c6f9`).
