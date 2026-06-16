# Vol(𝓑₃) uniform usage — comprehensive audit (Subgoal-1 prerequisite)

**Date:** 2026-06-02
**Branch:** `claude/m-avg-subgoal-1-operator-combiner-2026-06-02` (PR #1698)
**Trigger:** Owner pushback on Phase B: "thought we determined this knot-dependent and should not be uniform: Production mass-table uses uniform Vol(𝓑₃)/ℏ² for ALL atoms".

## TL;DR

**Production compute is overwhelmingly uniform-Vol(𝓑₃).**

| pattern | count |
|---|---:|
| Scripts using uniform `Vol(𝓑₃)` (via `vol_density_borromean(q)` or hardcoded `8·G = 8·mp.catalan`) | **87** |
| Scripts using per-knot `vol_density_per_block(vol_K, tr_M_K, q)` | **2** |
| Of those 87, scripts that ALSO touch atom-specific logic (Z, N, isotope, mass_table, deuteron, helium, ...) | **65** |
| Of those 65, scripts that ALSO have per-knot path | **1** (`vol_density_per_block_wiring.py` — alternative-wiring testbed) |

**Net: 64 atom-touching scripts use ONLY uniform Vol(𝓑₃) — the bug.**

## What "per-knot" should mean

Per the cheat sheet `docs/canonical-derivation-cheat-sheet.md` §5, the canonical mass formula is:

```
m(K) = m_e · VolDensity(K, q_0)
VolDensity(K, q) = Vol(K) / ℏ_q² · linking_weight(K, q)
```

`Vol(K)` is the **hyperbolic volume of the SPECIFIC knot/braid K**, not Vol(𝓑₃) uniform. For atoms:

| atom | A | canonical K | Vol(K) at q₀ |
|---|---|---|---|
| proton | 1 | 𝓑₃ (3-strand Borromean) | 8·G = 7.328 ✓ uniform-Vol(𝓑₃) IS correct here |
| neutron | 1 | 𝓑₃ (different word, same braid type) | 8·G = 7.328 ✓ |
| D | 2 | β_D (6-strand atomic braid via `atom_braid_word_3A(1,1)`) | **Vol(β_D), not 8·G** |
| T | 3 | β_T (9-strand atomic braid via `atom_braid_word_3A(1,2)`) | **Vol(β_T), not 8·G** |
| ³He | 3 | β_³He (9-strand) | **Vol(β_³He), not 8·G** |
| ⁴He | 4 | β_⁴He (12-strand) | **Vol(β_⁴He), not 8·G** |

## Existing per-knot infrastructure

The CANONICAL function already exists:

- [`_li_2_q_util.py::vol_density_per_block(vol_K, tr_M_K, q)`](../../computations/_li_2_q_util.py) — takes `vol_K` explicitly, returns the paper-faithful VolDensity(K, q) × Σ_λ factor
- [`vol_density_per_block_wiring.py`](../../computations/vol_density_per_block_wiring.py) — the only consumer; documented in PR #1080+ as the alternative to `vol_density_borromean(q)` (which the function's own docstring labels a "SHORTCUT — global-scalar collapse, NOT the paper's per-block sum")

## Acknowledged in production but unfixed

`mass_table_comprehensive.py:99-111` already TAGS the atoms by methodology:

```python
ATLAS_TAG = {
    "p": "principled-derivation",          # 𝓑₃ → Vol(𝓑₃) is correct
    "n": "principled-derivation",          # 𝓑₃ → Vol(𝓑₃) is correct
    "D": "manual-historical-volume-match",  # KLUDGE: Vol(𝓑₃) wrong
    "T": "manual-historical-volume-match",  # KLUDGE: Vol(𝓑₃) wrong
    "3He": "manual-historical-volume-match",# KLUDGE: Vol(𝓑₃) wrong
    "4He": "magic-A-formula",               # KLUDGE: Vol(𝓑₃) wrong
    "6Li": "deprecated-volume-match",       # KLUDGE: Vol(𝓑₃) wrong
    ...
}
```

So the production CODE already acknowledges the kludge ("manual-historical-volume-match", "magic-A-formula", "deprecated-volume-match", "recursive-on-4He") — but the kludge persists because per-atom Vol(β_K) isn't computed / wired in.

## TIER-1 production scripts to migrate

(Highest impact — these directly produce the production mass-table)

| script | role | uses uniform | needs per-knot |
|---|---|---|---|
| `mass_table_comprehensive.py` | production mass-table (all isotopes) | ✓ | YES |
| `build_proton_mass_50dps_chain.py` | proton mass chain | ✓ (correct for proton) | NO (𝓑₃ is correct) |
| `m_p_borromean_verification_50dps.py` | proton verification | ✓ (correct for proton) | NO |
| `borromean_volume_propagation_to_m_p.py` | proton volume propagation | ✓ (correct for proton) | NO |
| `applied_uniqueness_mass_table.py` | applied mass table | ✓ | YES |
| `canonical_isotope_witness.py` | isotope witness | ✓ | YES |

So really only **3 production scripts** are wrong: `mass_table_comprehensive.py`, `applied_uniqueness_mass_table.py`, `canonical_isotope_witness.py`. The proton-specific scripts are correct (𝓑₃ IS the proton's knot).

## TIER-2 / TIER-3 — probes and audits

64 atom-touching scripts use uniform Vol(𝓑₃). Most are:
- **Binding-energy probes** (e.g. `binding_endomorphism_deuteron.py`, `binding_depth_stratified.py`) — many compute `B = m_e · Vol · Δtr` where Vol IS legitimately knot-dependent (`binding_link_volumes.py` and downstream use per-binding-link volumes already)
- **Audits and probes** investigating specific phenomena where Vol(𝓑₃) is the baseline being compared against alternatives
- **Exploratory probes** that should be re-audited per the production-vs-exploratory discipline

## The Vol(β_K) data gap

For atoms D, T, ³He, ⁴He+, no Python script currently produces a categorical per-atom hyperbolic volume. Production options:

1. **Compute via SnapPy**: `atom_braid_word_3A(Z, N)` produces the 3A-strand braid word; SnapPy's `Manifold(...)` + `volume()` would compute Vol(β_K). Sandbox-blocked here (SnapPy not installed) but feasible in CI / owner local. Existing `knot-volumes.py` uses SnapPy and could be extended.
2. **Compute via categorical formula**: if the Borromean tower has a closed-form per-A volume (e.g. `A · Vol(𝓑₃) + interface corrections`), no SnapPy needed. This is part of the Subgoal-1 owner-active research.
3. **Use existing binding-link volumes** as a starting point: `binding_link_volumes.py` produced Vol(Hopf), Vol(8_11), Vol(L6a4) for binding-knot extension at A=2,3 — but these are BINDING knots, not the atom mass-knot.

## Phase B + Vol-audit verdict

The +2.89% m_p gap (and the catastrophic regression at higher A when switching to per-block tr_M) BOTH have the SAME root cause: **uniform Vol(𝓑₃) is wrong for atoms beyond proton**.

The owner-active Subgoal-1 path is exactly this: per-atom Vol(β_K) + per-atom tr_M(β_K), both fed through `vol_density_per_block(vol_K, tr_M_K, q)`. The infrastructure on the **tr_M side** is ready (`markov_peel.tr_M_atomic(Z, N)` works at all A; operator-valued combiner works at A=2). The infrastructure on the **Vol side** needs Vol(β_K) data.

## Recommendation

1. **Compute Vol(β_K) for D, T, ³He, ⁴He** via SnapPy (sandbox-blocked here; owner local or CI). Produce a `per-atom-hyperbolic-volumes.witness.json` artifact.
2. **Wire `mass_table_comprehensive.py`** + the 2 other Tier-1 scripts to consume per-atom Vol via `vol_density_per_block(vol_K=Vol(β_K), tr_M_K=tr_M_atomic(Z,N), q)`.
3. **Re-run mass-table** with per-knot Vol + per-atom tr_M; compare to CODATA. If m_avg lands in right ballpark, Subgoal-1 closure is in sight. If not, the categorical structure still has open gaps but the diagnostic is sharper.
4. **Migrate Tier-2/3 probes** that use uniform Vol(𝓑₃) on atom-touching paths. Most binding probes already use per-binding-link Vol; mass probes should match.

## Cross-references

- Phase A: [`docs/audits/2026-06-02-subgoal-1-phase-a-baseline.md`](2026-06-02-subgoal-1-phase-a-baseline.md)
- Phase B: [`docs/audits/2026-06-02-subgoal-1-phase-b-per-atom-trM-comparison.md`](2026-06-02-subgoal-1-phase-b-per-atom-trM-comparison.md)
- Scope: [`docs/coordination/2026-06-02-m-avg-subgoal-1-operator-combiner-scope.md`](../coordination/2026-06-02-m-avg-subgoal-1-operator-combiner-scope.md)
- Canonical reference (purged λ_scale, refuted routes): [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md)
- Per-block canonical function: [`computations/_li_2_q_util.py::vol_density_per_block`](../../computations/_li_2_q_util.py)
- Atom braid words: [`computations/mass_at_3A_proper.py::atom_braid_word_3A`](../../computations/mass_at_3A_proper.py)
- Existing per-knot vol witness (proton only): [`computations/knot-volumes.witness.json`](../../computations/knot-volumes.witness.json)
- Per-binding-link vol witness (A=2,3 already): [`computations/binding-link-volumes.witness.json`](../../computations/binding-link-volumes.witness.json)
