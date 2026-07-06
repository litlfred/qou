# Compute-integration swarm 2 — hidden CODATA literals + WitnessBuilder ports (2026-07-05)

Branch: `claude/compute-integration-swarm2-2026-07-05` · PR #3344
Lane: compute-integration (`computations/**/*.py`, `tools/**/*.py`).
Beans: **46ke** (hidden CODATA literals rollup), **1j39** / **cmiy** (P30
WitnessBuilder rollup — 1j39 is a dedup'd duplicate of cmiy).

## TL;DR

**No mechanical port/pin was applied this session** — and that is the correct
outcome, not a stall. Two independent blockers:

1. **Sandbox is compute-blocked.** `mpmath`, `pyhecke`, `qou_substrate`,
   `clarabel` all `ModuleNotFoundError`. `WitnessBuilder`
   (`tools/qou-substrate/python/qou_substrate/witness.py`) transitively imports
   `mpmath` via `precision.py:77`, so it cannot even be imported here. No
   producer can be run, no witness regenerated, no numerical claim verified.
2. **The safe, bit-identical tail of both beans is exhausted** by three prior
   46ke drains + an active sibling, and by cmiy batches 1–9b. What remains is
   value-changing (owner-gated) or requires running a producer (compute-blocked).
   Per task rule 2 ("any change that alters a computed value or math → STOP and
   document as deferred") the remainder is deferred, documented below.

This doc re-inventories both problem classes on current `main` so the next
**compute-capable** agent can act directly.

---

## Class 1 — hidden CODATA literals (bean 46ke)

### Inventory (fresh grep, 2026-07-05)

| Metric | Count |
|---|---|
| `.py` files containing a CODATA mass fingerprint (excl. registry) | 307 |
| Total literal occurrences | 521 |
| **Live-input** assignments `m_x = <codata literal>` (code, not comment) | 26 |
| — of those, under `computations/_deprecated/` (out of scope) | 17 |
| — active, non-deprecated live-inputs | ~5 |
| Inline **full-precision (≥20-digit) mpf-string** CODATA literals (the only bit-identical-safe pin category) | **0** |

The ~495 non-live-input occurrences are docstrings, `# comment` provenance
notes, and **expected-value comparison targets** (`assert abs(pred - 938.272)
< tol`). Comparison targets are *validation anchors*, not calibration inputs —
routing them through the registry is not required and does not reduce degrees of
freedom; leave them alone.

### Root blocker: the registry constant is itself truncated (→ me3r)

`computations/substrate/codata_constants.py` loads `M_E_MEV` from
`computations/codata-2022-validation-masses.witness.json`, whose stored value is
`"m_e_MeV": "0.51099895"` — **truncated to 8 significant figures**. CODATA-2022
is `m_e c² = 0.51099895069 MeV`. (`U_MEV` was already bumped to CODATA-2022
`_U_MEV_CODATA2022`, so the earlier stale-2018 U concern is closed; the *m_e*
truncation is the live me3r item.)

Disposition of the active (non-deprecated) live-inputs:

| Script:line | Literal | vs `M_E_MEV` (=`0.51099895`) | Disposition |
|---|---|---|---|
| `computations/probes/delta_lambda_bar_involution_probe.py:44` | `0.51099895069` | **fuller** than registry | routing **loses precision** → me3r truncation class (owner-gated) |
| `computations/test_betti_binding.py:13` | `0.510998950` | numerically = 0.51099895 | float64-equal, but mpf-context-**unsafe** (float→exact-mpf changes ~17th digit); asserts → defer, cannot verify |
| `computations/run_jones_markov_atlas_all_atoms.py:80` | `0.510998950` | equal | witness-emitter → mpf-context risk → defer |
| `computations/per_atom_audit_witnesses.py:67` | `0.510998950` | equal | witness-emitter → mpf-context risk → defer |
| `computations/a4_interface_trace_integration_all.py:30` | `0.510998950` | equal | witness-emitter → mpf-context risk → defer |
| `computations/binding_alpha_shift_witness.py:18` | `0.51099895069` (in a docstring) | — | comment, not input; the *live* stale-m_e in this file is bean ce18 |

Why the `0.510998950` cases are not a free pin: replacing a Python `float`
literal with the registry `mpf` constant is value-preserving **only** in a pure
float64 context. In an `mp.dps=50` context (which these witness-emitters use)
`float(0.510998950)` promotes to the float64 binary value, whereas
`mpf("0.51099895")` is the *exact* decimal — they diverge at ~1e-17 relative,
changing the serialized witness. Compute-blocked ⇒ cannot confirm which context
each runs in ⇒ defer per rule 2.

### Prior-drain state (from bean 46ke history)

- PR #2606: `meson_mass_from_hecke.py`, `beta-decay-from-q.py`,
  `canonical_isotope_witness.py` routed (bit-identical); public `U_MEV` export
  added.
- Sibling `claude/codata-46ke-rollup-2026-06-22`: AME-binding literal sweep.
- 2026-06-30 PR: `yekutieli_volume_join.py:456` (m_e) routed bit-identical.

### Deferred / owner-gated (do NOT silently route — changes numbers)

- **me3r** — registry truncation class: `M_E_MEV` (and peers) stored at 8 figs;
  fixing = bump the witness to full CODATA-2022 precision → changes every
  downstream witness → owner-gated. This is the true blocker for the remaining
  m_e live-inputs.
- **ce18** — `binding_alpha_shift_witness.py` stale CODATA-2018 m_e (live input).
- **Deprecated tail** — 17 live-inputs under `computations/_deprecated/`: policy
  is leave alone.
- **Exploratory probe tail** — `option_e_*/probe_*/delta_lambda_*`: low value per
  three prior drains.

**Net for 46ke this session: 0 safe pins available in sandbox.** The productive
next step is *not* more routing — it is the me3r registry-precision fix
(owner-gated), after which the `0.510998950` emitters can be routed + re-run to
verify.

---

## Class 2 — hand-rolled witness emission (beans 1j39 / cmiy)

### Inventory (fresh grep, 2026-07-05)

| Metric | Count |
|---|---|
| `.py` under `computations/`+`tools/` calling `json.dump` | 719 |
| — of those referencing a `.witness.json` payload | 686 |
| `.py` already touching `WitnessBuilder`/`witness_base`/`wrap_legacy`/`stamp_staleness_metadata` | 1262 |
| `witness_dependency_drift.py` (PROV baseline tool) | present |

(Raw call-site greps, not de-duplicated per producer; the bean's canonical PROV
metric is `PROV_MISSING`, last recorded **254** post-batch-9b.)

### Why this is compute-blocked (not merely deferred)

A cmiy port is **not** a source-only edit. The recipe (per cmiy batch notes) is:
edit the producer to build its payload through `WitnessBuilder` / `wrap_legacy`
/ `stamp_staleness_metadata`, **then run the producer** so the witness is
rewritten with provenance (`PROV_OK`). In this sandbox:

- `WitnessBuilder` cannot be imported (`mpmath` missing → `precision.py:77`).
- `computations/substrate/witness_base.py` re-exports from `qou_substrate.witness`
  → same `mpmath` failure.
- Therefore no producer can be run and no witness regenerated.

Committing a source-only edit **without** regenerating would leave the `.py` and
its `.witness.json` inconsistent and unverified — the exact correctness risk rule
2 forbids. So **no cmiy port is safe here.**

### Prior-drain state (from bean cmiy history)

Batches 1–9b done (≈33 scripts): the clean single-output / zero-consumer /
no-assertion vein is **exhausted** (batch 4 note); the assertion-bearing
`substrate/` stamp-tail is **exhausted** (batch 8 note). Remaining tail is the
harder ~9: `binding_qaskey_product_probe`, `lever1_qholonomic_order3_fit`,
3× z2bn (`delta_lambda_borromean_ascaling`,
`sw_period_qinvolution_identification_probe`, …), plus non-substrate multi-emit
/ many-consumer / Hecke-regen cases — all needing the **canonical env**
(pyhecke_native / mpmath), i.e. all compute-blocked here.

Documented migration gotchas (must be honored by the next agent):

1. `wrap_legacy` **drops** flat assertions/`allPassed` → use
   `stamp_staleness_metadata` for assertion-bearing payloads.
2. Regen refreshes stale data (q0 drift) → full regen needed, not
   provenance-only → needs canonical env.
3. Some raw-emit scripts pre-crash (e.g. `magic_A_formula` mpf-format) →
   separate fix.
4. Some producers need a `sys.path` insert for `substrate/` before import.
5. `save()` drift-protection treats `commitSha`/`computedAt`/`durationMs` as
   ephemeral → delete the stale witness first, then run.

**Net for cmiy/1j39 this session: 0 ports (fully compute-blocked).** `1j39` is a
confirmed duplicate of `cmiy` — recommend owner-close `1j39` (resolve is
human-only).

---

## Verification status

- **Compute-blocked in sandbox** — no producer runs, no witness regeneration, no
  numerical verification possible.
- The only file changed by this session is this audit doc; `py_compile` N/A (no
  `.py` edited).
- No sidecar-algorithm compute changed ⇒ Mass-and-Binding appendix sync **not
  required** (exempt).
- No LP/SDP/operator-selection solve touched ⇒ dual-emission rule N/A.

## Recommended next actions (for a compute-capable agent)

1. **me3r** (owner-gated): bump `codata-2022-validation-masses.witness.json`
   `m_e_MeV` and peers to full CODATA-2022 precision; then route + re-run the
   four `0.510998950` emitters and diff witnesses.
2. **cmiy**: in the canonical env, resume the hard tail in small per-cluster
   batches (qaskey / qholonomic / z2bn), honoring gotchas 1–5; drive
   `PROV_MISSING` down from 254.
3. Owner-close duplicate bean `1j39`.
