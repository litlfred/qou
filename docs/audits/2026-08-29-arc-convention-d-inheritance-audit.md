# Convention-D audit of the bk-crossing mass-binding arc's trace numbers

**Date:** 2026-08-29
**Tier:** audit (no new result — a scope/provenance finding)
**Arc:** bk-crossing mass-binding · **Related beans:** `qou-cds1`, `qou-cds2`
**Question:** are the arc's Markov-trace numbers (`b_αα ≈ 2.41 MeV`, the deuteron weights)
computed under **convention D** (`z = q³/(q²+1)`), now canonical (owner ruling 2026-08-15),
or under the excised **convention C** (`z = √q/(q+1)`)?

## Method

Grepped the arc's trace producers for a local `z` / Markov-parameter definition and for the
convention-D (`q**3/(q**2+1)`) and convention-C (`√q/(q+1)`, `1/(√q+1/√q)`) spellings — including
the return-form spellings the detector-blindness taxonomy
([`2026-08-15-detector-blindness-taxonomy.md`](2026-08-15-detector-blindness-taxonomy.md)) catalogues.

## Finding — the arc does not spell `z`; it inherits the convention

- **`c_alpha_alpha_categorical_via_jones_markov.py` (the `b_αα` producer)** computes the trace via
  `markov_trace_for_knot("7^2_1", q₀, "wenzl")` and `… "q_schur"`. It carries **no local `z`
  definition** — the two channel names ("Wenzl Jones-Markov", "q-Schur Plancherel") select a
  convention *inside the shared engine*, not in the arc.
- **The deuteron probes** (`computations/deltalambda/deuteron_*.py`): **zero** hits for either the
  convention-C or convention-D spelling. They too go through the shared trace infrastructure; only
  `deuteron_wall_qborel_resummation_probe.py` imports `pyhecke` directly.
- The Markov parameter therefore lives in `markov_trace_for_knot` → `pyhecke`
  (`tools/pyhecke/python/pyhecke/gram.py`).

## Consequence — the arc inherits an OPEN convention-D question

The arc's convention-D compliance is **not determinable from the arc code** — it reduces entirely
to the shared engine's `z`. And that engine's D-migration is **still in progress**:

- **`qou-cds2` (in-progress)** — "pyhecke.gram.z and the Gram singularity — the ruling": the D
  migration of `gram.z` is blocked on a Gram-matrix singularity under D. Not closed.
- **`qou-cds1` (in-progress)** — the Q_β `c_k` ladder re-derivation under D is likewise open; the
  whole `c_k` axis is flagged C-conditional in `AGENTS.md`.
- `AGENTS.md` records the remaining convention-C surface as **UNMEASURED**, with 13 distinct
  detector-blind spellings — a clean detector run is not evidence the surface is clear.

**Therefore: `b_αα ≈ 2.41 MeV` and the deuteron crossing weights are NOT yet established as
convention-D-valid.** They inherit the C→D question one layer down, at the trace engine. Any use
of these numbers as canonical must wait on `qou-cds2` (engine), and cannot be fixed inside the arc.

## What this does and does not say

- It does **not** claim the arc numbers are wrong — only that their convention is **unresolved**,
  because the engine they call is mid-migration.
- The counter-move, when a result is exact and symbolic, is to **test the answer, not the source**
  (per `AGENTS.md`): e.g. the Markov-peel deuteron denominator factors as `192·q²³·(q²+1)³` under
  D — one `(q²+1)` per peel — which convention C cannot produce. If the arc's `b_αα`/deuteron
  outputs are re-derived symbolically, apply that `(q²+1)`-divisibility test rather than re-grepping
  for `z`.

## Recommendation

Gate any "canonical" use of the arc's `b_αα` / deuteron trace numbers on `qou-cds2` closing the
engine-level D migration. Until then, label them **convention-inherited (D-status open)** in the
arc ledger, exactly as the `c_k` ladder is labelled C-conditional.
