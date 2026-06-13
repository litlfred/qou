# Orphaned-legacy per-nucleus witness triage (2026-06-13)

**Closes** the "~28 orphaned-legacy witnesses" remainder left by the
`lean_uniqueness_ref` wiring campaign
([workplan 2026-05-31](../workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md),
merged via #2203). Those are the per-nucleus witnesses that lack the
`lean_uniqueness_ref` field **and** lack a live producer (no `scriptFile`, or a
deleted one).

## Verdict — mostly a non-problem

29 witnesses triaged by **(a)** does a current producer write that name, and
**(b)** does anything still consume it:

| Class | Count | Disposition |
|---|---:|---|
| `chi-*` χ-evaluation caches | 24 | **No action** — self-heal on CI regen |
| Doc-referenced / consumed | 3 | **Keep / freeze** |
| Dead (0 producers, 0 consumers) | 2 | **Deprecated** (moved to `_deprecated/`) |

### 1. The 24 `chi-*` witnesses — self-heal (no action)

`chi-{deuteron-h6, helium-3-h9, helium-4-h12, lithium-5-h15, lithium-6-h18,
tritium-h9, neutron-h3, proton-h3}` (at `q0`/`qinv`, `free`/bound, and
`-matrix-m` variants). These are **not** truly orphaned:

- **Live producers exist** — `chi_4he_via_rust_lossless.py`,
  `chi_monotone_transfer.py`, `chi_atom_fmatrix_recoupling.py`,
  `mass_vol_density.py`, `chi_free_via_lr.py`, `aK_via_lp_dual.py`,
  `spectral_selector_validate.py`, … all write these names.
- **Heavily consumed** — 20–31 Python readers each.

They lack a `scriptFile` only because they were last written by a
pre-`WitnessBuilder` producer. On the next CI witness-pipeline regen they pick
up `scriptFile` (and `lean_uniqueness_ref` where the producer is wired) — i.e.
they are the same **stale-on-disk** class identified in the #2203 closing
ledger, not a migration project. **No code change required.**

### 2. Keep / freeze (3)

| Witness | Why keep |
|---|---|
| `deuteron-binding-interface-closure.witness.json` | 2 doc refs + 1 live reader (`binding_energy_categorical_deuteron.py`) — a consumed input; reconstruct its producer opportunistically, otherwise a stable frozen input. |
| `tau-hat-n-proton-level-1-empty.witness.json` | 2 doc refs (referenced as evidence in audits); no code consumer. Freeze as historical evidence. |
| `tritium-interface-decomposition.witness.json` | 1 doc ref; no code consumer. Freeze as historical evidence. |

### 3. Deprecated (2) — moved to `_deprecated/`, not deleted

| Witness | Evidence |
|---|---|
| `proton-mass-spectral-correction.witness.json` | 0 docs, 0 code consumers; only reference is the `derivation-chain-audit` inventory witness (regenerates). |
| `habiro-mirror-pair-li7-be7.witness.json` | 0 docs, 0 code consumers; same single inventory reference. |

Both `git mv`-ed to `folio-assistant/computations/_deprecated/` (the
established convention — that directory already holds deprecated witnesses).
Per owner directive 2026-06-13: **deprecate now, delete later** (git history
preserves them, so a future `git rm` loses nothing). Moving them out of the
active `*.witness.json` glob keeps the audit/validators from counting dead
artifacts.

## Net effect

The "~28 orphaned-legacy migration project" reduces to: **0 reconstruction
work** (24 self-heal, 3 frozen) + **2 deprecations** (this PR). The lingering
audit "missing `lean_uniqueness_ref`" count is now entirely CI-regeneration lag
on live witnesses — self-clearing on the next green witness pipeline.
