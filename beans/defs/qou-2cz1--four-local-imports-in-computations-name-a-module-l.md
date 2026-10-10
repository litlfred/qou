---
# qou-2cz1
title: Four local imports in computations/ name a module-level name that does not exist -- two producers cannot be imported, and scriptHash reports them IN SYNC
status: todo
type: task
priority: high
created_at: 2026-10-10T07:57:44Z
updated_at: 2026-10-10T07:57:44Z
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
