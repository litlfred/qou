# Stale-witness infra gap — `low-isotope-mass-table` ¹H tautology

**Date**: 2026-05-16
**Branch**: `claude/isotope-mass-witness-data-x5lCh`
**Trigger**: Owner noticed `low-isotope-mass-table.witness.json` reports
¹H as `row_derivation_status: "derived"` with `M_pred = 938.2725 MeV`,
which violates the three-calibration discipline (`prop:three-calibration-inputs`:
CAL-1 = m_e, CAL-2 = 𝔇_β, CAL-3 = 𝔇_π; m_p and m_n are predictions,
never inputs).

## What happened

1. **2026-04-29** — `build_proton_mass_50dps_chain.py` produced
   `proton-mass-codata-50dps.witness.json` with `m_p_pred_MeV ≈ 937.76`
   (rel_diff vs CODATA = 543.8 ppm, `allPassed = false` at the 1 ppb
   gate). The chain was already SCRIPT_CITED at T1+T4 — but the
   numeric value happened to land within ~0.054 % of CODATA, masking
   the structural gap.
2. **2026-05-09** — `low_isotope_mass_table.py` ran and consumed
   `m_p_pred_MeV` as `M_P_DERIVED_MEV` via
   `float(_proton_w["data"]["m_p_pred_MeV"])`. ¹H got
   `M_pred = m_p_derived + m_e = 938.2725 MeV`, residual −543.8 ppm
   vs CODATA. The row's `row_derivation_status` was set to `"derived"`
   because B(¹H) = 0 trivially and the m_p input "existed".
3. **2026-05-11** — `build_proton_mass_50dps_chain.py` was honesty-
   rewritten to expose the unclosed T1+T4 mass-endomorphism tower
   assembly: it now reports `m_p_pred_MeV = 0.597418 MeV` (rel_diff
   = 0.9994 = 999 M ppb, off by 9 orders of magnitude). The witness
   on disk after this date is structurally honest about the gap.
4. **2026-05-09 → 2026-05-16** — `low-isotope-mass-table.witness.json`
   was **not** regenerated against the new proton witness. The table
   on `main` still cited `m_p_derived_MeV = 937.7615` as if that
   value came from the 2026-05-11 witness on disk; in reality the
   cited witness now contains `0.597418`. Re-running the script
   today against the current proton witness would produce
   `M_pred(¹H) = 1.108 MeV` (vs observed 938.78 MeV; −999 K ppm), but
   no CI step re-runs the script.

## Why the existing infra didn't catch it

`.github/workflows/witness-pipeline.yml` has a "Detect drift in
committed witnesses" step (lines 367–397). The step is sound — it
re-runs a list of validators and `git diff`s their outputs against
what is committed, filtering only the expected drift fields
(`computedAt`, `commitSha`, `scriptCommitSha`, `engineVersion`, …).

**The gap is in *which scripts the workflow re-runs*.** The runlist
is a hardcoded `python3 computations/<NAME>.py`
sequence in the workflow YAML. Scripts not on the runlist are
**never re-executed in CI**, so their `*.witness.json` outputs are
not regenerated and the drift step has nothing to compare. Examples
of scripts that consume upstream witnesses but are not in the
workflow's runlist:

- `low_isotope_mass_table.py` — consumes `proton-mass-codata-50dps`
- `derived_masses.py` — consumes `proton-mass-codata-50dps`, `q-beta-predicted`
- `atomic_mass_via_rho_k.py` — consumes `atomic-tr-m-mpfr-50dps`
- ... and many more.

The pull-request path filters do trigger the workflow on
`*.witness.json` changes, but the workflow then runs its hardcoded
list of validators and reports green if those validators pass —
without ever asking *"which downstream witnesses depend on the
changed file, and have they been regenerated since?"*.

In other words, the witness pipeline knows how to re-run a fixed
set of scripts; it does **not** know the **dependency DAG between
witnesses** and cannot tell which downstream witnesses are stale.

## Anti-staleness mechanism added on this branch

The pattern is now wired into three downstream scripts and exposed
through a shared helper in `witness_base.py`:

- **`low_isotope_mass_table.py`** (1 upstream witness) — uses the
  free function `load_and_hash_upstream(path)` from `witness_base`;
  emits the hash list under `derivation_inputs.upstream_witness_hashes`
  (hand-rolled dict layout).
- **`binding_K_direct.py`** (3 upstream witnesses) — uses
  `WitnessBuilder.add_upstream(path)`; emits under
  `data.upstream_witness_hashes`.
- **`atomic_mass_via_rho_k.py`** (7 upstream witness hits, with
  duplicates over the discovery loop) — uses a thin module-level
  accumulator (`_load_upstream`) that wraps `load_and_hash_upstream`
  for the `wrap_legacy` flow; emits under `data.upstream_witness_hashes`.

Each entry has the shape

```json
{
  "path":             "proton-mass-codata-50dps.witness.json",
  "sha256":           "3c9444...",
  "size_bytes":       1456,
  "commitSha":        "15dd1c2fc5da...",
  "scriptCommitSha":  "6efe798ed026...",
  "computedAt":       "2026-05-11T22:01:30.300450+00:00"
}
```

The sha256 is the bytes-hash of the upstream witness file at the
moment this script consumed it. The commit SHAs and `computedAt` are
read from the upstream witness body and reproduce its provenance.

A companion validator [`witness_dependency_drift.py`](../../computations/witness_dependency_drift.py)
walks every `*.witness.json` looking for `upstream_witness_hashes`
(in either `derivation_inputs.*` or `data.*`) and verifies each
entry's sha256 against the current bytes of the named upstream
file. Drift means: the upstream changed since this witness was last
regenerated — the downstream is stale. Exit code 1 on any drift in
`--strict` mode; report path-by-path on stdout.

This is a **single-file diagnostic**: the validator reads what's on
disk, no producer scripts re-run, no CI environment needed.
Operators can wire it into `witness-pipeline.yml` as a fail-on-drift
gate at their discretion.

### Adoption status (2026-05-16)

| Script | Output witness | Upstream hashes recorded |
|---|---|---|
| `low_isotope_mass_table.py` | low-isotope-mass-table | 1 (proton-mass-codata-50dps) |
| `binding_K_direct.py` | binding-K-direct | 3 (atomic-tr-m-mpfr-50dps, atomic-tr-m-helium4, atomic-tr-m-wenzl-bridge) |
| `atomic_mass_via_rho_k.py` | atomic-mass-via-rho-k | 7 (atomic-tr-m + Model B + legacy mass-table; some duplicates over the discovery loop) |
| (TODO) `derived_masses.py` | (library — no own witness; refactor pattern differs) | — |
| (TODO) `paper_six_term_isotope_sweep.py` | paper-six-term-* | 4-5 candidates |

Total coverage: **3 witnesses / 11 upstream hash records** out of
~50 mass-chain consumers. Adoption can spread one script per PR.

## Sanity guard on `m_p_pred`

Independent of the drift mechanism, the table now refuses to consume
`m_p_pred_MeV` if `rel_diff > M_P_DERIVED_MAX_REL_DIFF` (currently
1 %). The rationale: a chain that lands within 543 ppm of CODATA at
the 1 ppb gate is **not** "almost closed" — it is an unclosed chain
whose numeric output happens to be near the answer for unrelated
reasons (calibration leak somewhere upstream, or coincidence). The
honest output is `derivation_pending` until the chain genuinely
closes.

Tighten the threshold to 1 ppm once `build_proton_mass_50dps_chain.py`
reports `allPassed = true` at any precision rung better than that.

## Audit conclusion

- ¹H's previous `row_derivation_status: "derived"` was a **mis-label**:
  the upstream proton witness has never been clean under the three-
  cal discipline, and the −543.8 ppm error was the m_p chain's
  partial-closure error propagating 1:1 through ¹H (electron mass
  cancels exactly).
- The witness regenerated on this branch reports all 23 rows as
  `derivation_pending`. This is the truthful state under no-
  calibration discipline. ¹H will lift to `derived` only after the
  T1+T4 mass-endomorphism tower assembly closes in
  `build_proton_mass_50dps_chain.py`.
- The infra fix in this PR — `upstream_witness_hashes` field +
  `witness_dependency_drift.py` validator — gives the witness
  pipeline its missing dependency-DAG view, single-script and
  opt-in. Adoption pattern: each script that consumes upstream
  witnesses calls a small helper that records the hash; the
  validator flips on the moment any downstream is regenerated
  against a changed upstream.
