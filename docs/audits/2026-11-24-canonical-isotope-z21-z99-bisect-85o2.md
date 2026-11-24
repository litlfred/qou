# Audit Ledger: `canonical-isotope-witness` `Z00..Z118` Bisect & `2.19×` Stage-Mismatch Proof (`qou-85o2`)

**Date:** 2026-11-24  
**Beans:** `qou-85o2` (under Stability Swarm Epic `qou-s028`)  
**Verification Probe:** [`isotope_shard_2x_cause_probe.py`](../../computations/isotope_shard_2x_cause_probe.py)  
**Witness:** [`isotope-shard-2x-cause-probe.witness.json`](../../computations/isotope-shard-2x-cause-probe.witness.json)

---

## 1. Ordered Investigation & Exact 80-dps Measurements

Bean `qou-85o2` noted that 98 `canonical-isotope-witness-Z*.witness.json` shards (`Z21..Z118`) carry `computedAt = 2026-08-23T17:15–17:16` (`commitSha = 35d18af5f783`), predating commit `a24fdac8a1a6` (`2026-08-24T11:04:30Z`), and that a spot re-run at `Z = 26, N = 19` (`⁴⁵Fe`) gave `qclt_binding = 120.70 MeV` against the shard's recorded `55.088 MeV` — an apparent factor of `2.19×` where the standard-channel pn-bond log-ratio predicted `~0.73×`.

Following `qou-85o2`'s ordered steps at `mp.dps = 80` (`mpmath 1.4.1`, zero `float64`):

1. **Three-run reproducibility at `Z = 26, N = 19` (`⁴⁵Fe`):**
   Three independent 80-dps evaluations of `channel_binding.qclt_binding(26, 19, colour_weighted=True, dps=80)` and `coulomb_energy_mev(26, 45)` are bit-identical across all 80 digits:
   - `qclt_binding` (post-`a24fdac8a1a6`): `120.7011740021478585985088464697731429118 MeV`
   - `coulomb_energy_mev(26, 45)`: `111.6741340440589905433608355207346172917 MeV`
   - `L4 = qclt_binding - coulomb_energy_mev`: `9.027039958088868055148010949038525620105 MeV`

2. **Exact algebraic explanation of `2.191048078` (pipeline stage mismatch):**
   In `canonical_isotope_witness.py:345–352`, the `L4-qclt-colour-weighted` prediction ($A > 40$) is
   $$\mathrm{prediction}_{\mathrm{L4}}(Z, N) = B_{\mathrm{qCLT}}(Z, N) - E_{\mathrm{Coulomb}}(Z, A).$$
   The spot-check divided the **pre-Coulomb** post-update strong term (`120.7011740021 MeV`) by the **post-Coulomb** pre-update recorded `L4` residual (`55.0883274584 MeV`):
   $$\frac{120.7011740021478586}{55.0883274583714925} = \mathbf{2.19104807827}.$$
   Comparing **like-for-like** across `a24fdac8a1a6`:
   - `qclt_binding`: `166.76246150243048 -> 120.70117400214786 MeV`, ratio **`×0.7237911521`** (within **`0.62%`** of the pure pn-bond log-ratio $\ln f_{pn}(z) / \ln f_{pn}(z_{\mathrm{pre}}) = \mathbf{0.72830816}$, the `0.62%` offset coming deterministically from the complete-graph `pp` and `nn` weights $\binom{26}{2} = 325$ and $\binom{19}{2} = 171$ alongside $26 \times 19 = 494$ `pn` bonds).
   - `L4` residual: `55.08832745837149 -> 9.02703995808887 MeV`, ratio **`×0.1638648369`**, amplified by subtracting the unchanged `111.6741340441 MeV` Coulomb repulsion.

3. **Single-cause per-file attribution in the import cone (`2026-08-23T17:15 .. HEAD`):**
   - `a24fdac8a1a6` (`2026-08-24T11:04:30Z`) touched two Python modules in the import cone:
     - `computations/channel_binding.py`: self-test comment + sanity threshold only -> **`0 MeV`** contribution (`bit-identical`).
     - `computations/substrate/hecke_core_symbolic.py`: updated symbolic Markov trace weight `z` from $z_{\mathrm{pre}} = \sqrt{q}/(q+1)$ to $z = q^3/(q^2+1)$ -> **`46.06128750028262 MeV`** (`100%` of the move; reproduces committed `55.0883274583714925` to `rel = 1.20e-16`).
   - Subsequent commits on `channel_binding.py` (`7d0af73553aa`, `884e4ab20d62`), `hecke_core_symbolic.py` (`8faa2a7662de`, `22a1b067651c`, `e4729528a96c`, `95747468b4fc`), and `coulomb_energy.py` (`48f446490cc8`) changed `qclt_binding(26, 19)` and `coulomb_energy_mev(26, 45)` by **`0` (`< 1e-68`)**.

---

## 2. Exhaustive `3,243`-Row Census Across All `119` Shards (`Z00..Z118`)

Evaluating the exact 80-dps pre-`a24fdac8a1a6` closed form against **every** `L4-qclt-colour-weighted` row across all 119 shards (`3,558` AME rows total) establishes two corpus-wide findings beyond the 8-row sample in PR `#6390`:

| Shard Range | Shards | `computedAt` (`commitSha`) | `L4` Rows ($A > 40$) | Reproduced `< 1.0` float64 ulp of `qclt_pre` |
|---|---:|---|---:|---:|
| `Z00..Z20` | `21` | `2026-08-24T14:40` (`f8dae9f5eb2a`) | `91` | **`91 / 91` (`100%`)** |
| `Z21..Z99` | `79` | `2026-08-23T17:15–16` (`35d18af5f783`) | `2,892` | **`2,892 / 2,892` (`100%`)** |
| `Z100..Z118` | `19` | `2026-08-23T17:16` (`35d18af5f783`) | `260` | **`260 / 260` (`100%`)** |
| **Total (`Z00..Z118`)** | **`119`** | — | **`3,243`** | **`3,243 / 3,243` (`100%`, `max = 0.988745 ulp`)** |

1. **Timestamp-vs-ancestry finding on `Z00..Z20`:** Although `Z00..Z20` carries `computedAt = 2026-08-24T14:40` (3h36m after `a24fdac8a1a6`), its `commitSha = f8dae9f5eb2a` was on a branch that had **not** yet merged `a24fdac8a1a6`. Consequently, all **`91` `L4` rows in `Z11..Z20`** (e.g. `Z = 20, N = 21`, `⁴¹Ca`: recorded `92.3501784691 MeV` vs post-update `48.6240890742 MeV`) are **also** pre-`a24fdac8a1a6`. All `119` shards (`3,243 / 3,243` `L4` rows) are uniform on $z_{\mathrm{pre}}$.
2. **Why shards are NOT mass-regenerated in this PR (honoring the `2026-11-21` owner gate in `qou-85o2`):**
   - Under $z = q^3/(q^2+1)$, **`1,634 / 3,243` (`50.39%`)** of `L4` rows flip to **negative net binding** (`qclt_binding < coulomb_energy_mev`, reaching **`-379.5023466 MeV`** at `Z = 118, N = 175`, $^{293}\mathrm{Og}$).
   - Two upstream binary64 truncations remain live in the shard pipeline: `float(qclt_binding(...))` at `canonical_isotope_witness.py:347` and `mp.mpf(str(_Q0))` from binary64 `q_parameter.Q` at `channel_binding.py:122` (`|q_cb - q_at(80)| = 7.59167e-18`).
   - All 120 shard + index files are mirrored under `qou-mass/src/qou_mass/data/isotopes/`, so any future owner-authorized shard refresh should land only after fixing both binary64 truncations and deciding how `canonical_isotope_witness.py` scopes negative asymptotic `L4` residuals.
