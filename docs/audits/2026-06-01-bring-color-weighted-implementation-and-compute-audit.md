# Bring color-weighted implementation + thorough compute/Bring audit

**Date:** 2026-06-01
**Branch:** `claude/vol-density-bz3-refinement-2026-06-01` (PR #1664)
**Scope:** Per owner directive: "implement bring color weighted. do thorough audit of compute to make sure all is brings/color as appropriate."

## Part 1 — Implementation: `bring_color_weighted_linking_weight(Z, N, q)`

### Files added/modified

- [`computations/_li_2_q_util.py`](../../computations/_li_2_q_util.py) — added two functions:
  - `bring_color_weighted_linking_weight(Z, N, q)` — per-atom Bring-color-tube extension of `linking_weight_family_a(q)`
  - `vol_density_borromean_bring_color_weighted(Z, N, q)` — wrapper for `m_e × VolDensity_bring`
- [`computations/probes/bring_color_weighted_base_scale_probe.py`](../../computations/probes/bring_color_weighted_base_scale_probe.py) — measures shifts vs Family A

### Categorical construction

Each nucleon has 3 color tubes (r, g, b) per Bring's modular structure. Per atom (Z, N):

```
n_u = 2Z + N    (u-quark count: 2 in proton uud, 1 in neutron udd)
n_d = Z + 2N    (d-quark count)
A = Z + N

asym = (N − Z) / (3A)        — odd under flavor exchange (sign: n heavier)
sym  = 2·n_u·n_d / (3A)²     — even under flavor exchange (no p/n sign)

linking_weight_bring(Z, N, q) = linking_weight_A(q) · (1 + δ·asym + δ²·sym)
```

where `δ = flavor_split_subleading(q) = (m_n − m_p)/M_N ≈ 0.00138` at q₀.

Reduces to Family A in the δ→0 substrate-degenerate limit.

### Measured shifts at q₀ (from probe run)

| Atom | linking_weight_bring | shift vs Family A |
|---|---|---|
| proton (1, 0) | 2.531619 | **−458.2 ppm** |
| neutron (0, 1) | 2.533944 | **+459.9 ppm** |
| deuteron (1, 1) | 2.532782 | +0.95 ppm |
| ⁴He (2, 2) | 2.532782 | +0.95 ppm |

| Mass prediction | Family A | Bring | CODATA |
|---|---|---|---|
| m_p (MeV) | 966.050 | **965.607** | 938.272 |
| m_n (MeV) | 966.050 | **966.494** | 939.565 |
| m_avg (MeV) | 966.050 | 966.051 | 938.919 |
| m_n − m_p (MeV) | 0 | **0.887** | 1.293 |

### Verdict

- **m_avg shift = 842.8 ppb** (m_avg goes from +2.890% to +2.890%, essentially unchanged)
- **Required to close +2.89%: ~29 000 000 ppb** — 34 290× larger than what the construction provides
- **STRUCTURALLY INSUFFICIENT for m_avg**, confirming the canonical reference [`lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md) prediction that H₄ + Bring color-tube ≠ closure
- **For p/n split**: predicts 0.887 MeV (68.6% of CODATA's 1.293 MeV). NOT a closure either — the production p/n split (via `flavor_split_subleading` direct, PR #690) is more accurate (0.030%) since it applies δ to m_avg directly, not through linking_weight

### What this implementation IS

- A categorical, parametric extension of `bring_color_weighted` from per-interface (closed_form_tau_M.py:178) to BASE scale
- Reduces cleanly to Family A
- Reveals the structural insufficiency QUANTITATIVELY (34290× too small)
- Available as opt-in via `vol_density_borromean_bring_color_weighted(Z, N, q)`

### What this implementation IS NOT

- NOT a production replacement for `vol_density_borromean(q)`
- NOT a closure of the +2.89% m_avg gap
- NOT wired into mass-table / build-proton-mass / m_p_borromean_verification production chain

## Part 2 — Thorough compute audit: Bring/color appropriateness

### Production scripts using H₄ Wedderburn average (vol_density_borromean → linking_weight_family_a)

19 scripts call `linking_weight_family_a` or `vol_density_borromean`. Of these, 7 are HIGH-impact production:

| Script | Severity | Current | Bring-aware extension |
|---|---|---|---|
| `build_proton_mass_50dps_chain.py` | HIGH | `vol_density_borromean(q)` H₄ | Opt-in via `vol_density_borromean_bring_color_weighted(1, 0, q)` |
| `m_p_borromean_verification_50dps.py` | HIGH | `vol_density_borromean(q)` H₄ | (same) |
| `mass_table_comprehensive.py` | HIGH | `vol_density_borromean(q)` H₄ | Could route per-(Z,N); see below |
| `borromean_volume_propagation_to_m_p.py` | HIGH | H₄ | (same) |
| `applied_uniqueness_mass_table.py` | HIGH | H₄ | (same) |
| `canonical_isotope_witness.py` | HIGH | H₄ | (same) |
| `linking_weight_canonical_object_lwfix.py` | HIGH | acknowledged CAL-4 | Audit-only; no fix |
| `vol_density_per_block_wiring.py` | MED | per-atom tr_M | Already Z,N-aware (alternative path, regresses to −56.7%) |
| `family_a_per_partition_h_decomposition_50dps.py` | MED | proof-of-identity | Proves H₄ identity; no Bring extension needed |
| 10 other probes/audits | LOW | various | Probes that test alternatives; correctly labeled |

**Production-pipeline action**: scripts should accept an optional `pn_convention` parameter or `(Z, N)` tuple, defaulting to the H₄ Family A. The new `vol_density_borromean_bring_color_weighted(Z, N, q)` is the opt-in entry point. **Owner approval required** before changing any production default — H₄ remains canonical-by-default until a categorical Bring extension that closes m_avg is found.

### Bring/color compute scripts (currently exist)

91 scripts mention Bring; key categories:

- **Bring color-tube probes (production-adjacent)**: `binding_bring_enhancement_compare.py`, `probe_k_ud_bring_color_tube_empirical_baseline.py`, `lambda_scale_refinement_h4_correction_bring.py` (flagged HIGH non-canonical per compute audit; exploratory h⁴ "+1" lacks derivation)
- **Bring zero-mode**: `bring_zero_mode_bloch_hunt.py`, `ocneanu_12_bring_zero_mode_variants.py`
- **Bring residue/modular**: `m_p_bring_plus_faddeev_h4_probe.py`, `bring_chiral_fibre_figure.py`
- **`closed_form_tau_M.py`**: default `pn_convention="chi_lambda_braid"` DROPS Bring at interface level; `bring_color_weighted` branch EXISTS but is opt-in

### Lean formalization gaps

- `content/quantum-observable-universe/lean/QOU/Brings/brings_is_qou.lean:65` — placeholder with `sorry`, claims Bring=QOU but proof deferred
- `content/quantum-observable-universe/lean/QOU/Interactions/BringShellBinding.lean` — minimal
- `content/quantum-observable-universe/lean/QOU/BringsSurface.lean` — has axioms (χ=−6, genus 4) but no Bring-color-tube linking_weight class

**No Lean class encodes the Bring-color-tube linking_weight formula.** Would-be class: `BringColorTubeWeighting` with fields for δ-shift, asym, sym contributions. Closure deferred (1-2 weeks per audit `2026-05-24-ew-couplings-substrate-empirical-matches.md` cadence).

### Content blocks: documentary vs computational

- [`content/.../braids-and-knots/inter-nucleon-channel-color-tube.md`](../../content/quantum-observable-universe/braids-and-knots/inter-nucleon-channel-color-tube.md) — describes Bring color-tube p-n interface AS canonical
- Production compute (mass-table, m_p chain) silently uses H₄ Wedderburn instead

This is the **central Bring/compute discrepancy**: the paper SAYS Bring color-tube; the compute USES H₄ uniform. The new `bring_color_weighted_linking_weight` provides the missing bridge — but at 34290× too small to close m_avg.

## Part 3 — Audit summary table

| Item | Status | Severity | Action |
|---|---|---|---|
| `bring_color_weighted_linking_weight(Z, N, q)` | ADDED this session | — | Now available as opt-in |
| `vol_density_borromean_bring_color_weighted(Z, N, q)` | ADDED this session | — | Opt-in wrapper |
| m_avg +2.89% closure | OPEN | HIGH | Bring extension alone insufficient; requires NEW categorical formulation (owner-active Subgoal-1 path) |
| Production scripts default H₄ | DOCUMENTED | MED | Owner approval needed before opt-in default |
| `closed_form_tau_M.py:137` default `chi_lambda_braid` | DOCUMENTED | MED | Opt-in `bring_color_weighted` already exists; no default change |
| Lean: `brings_is_qou.lean:65` sorry | OPEN | MED | 1-2 weeks closure |
| `BringColorTubeWeighting` Lean class | NOT EXISTS | LOW | Future infrastructure (post-categorical-closure) |
| `lambda_scale_refinement_h4_correction_bring.py` empirical h⁴ "+1" | NON-CANONICAL | HIGH | Per compute-audit: needs categorical derivation OR Rule 14 escalation |
| `lambda_scale_substrate_probe.py` PSLQ targeting CODATA | NON-CANONICAL | HIGH | Per compute-audit: shape-probe, falsified, should be archived |
| 91 Bring scripts cited but only ~10 wired | DOCUMENTED | LOW | Most are legitimate probes; documentation drift |

## Part 4 — Recommendations

### Immediate (this branch)

- [x] Add `bring_color_weighted_linking_weight` + probe
- [x] Measure shifts; document structural insufficiency
- [x] Write audit doc
- [ ] Commit + push (next step)

### Short-term (next sessions)

- Update `closed_form_tau_M.py:62-87` docstring to note the new function exists (no longer "queued research task")
- Consider adding `pn_convention="bring_color_weighted"` route through `vol_density_borromean` (opt-in parameter)
- Add Lean class `BringColorTubeWeighting` in QOU.BringsSurface (mirrors the Python function structure)

### Long-term (owner-active research)

- Close `brings_is_qou.lean:65` sorry (1-2 weeks)
- Find a NEW categorical Bring formulation that closes m_avg (the +2.89% gap; current Bring color-tube formulation is 34290× too small)
- Subgoal-1 path: per-isotope Borromean-tower extension + operator-valued branching combiner (owner-active per [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md))

## Cross-references

- Canonical reference (refuted Bring routes): [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md)
- Linking-weight residual confirmation (+2.89% genuine): [`docs/audits/2026-06-01-linking-weight-residual-fix.md`](2026-06-01-linking-weight-residual-fix.md)
- Cheat sheet §5 (canonical derivation): [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
- Session status: [`docs/coordination/2026-06-01-vol-density-bz3-refinement-session-status.md`](../coordination/2026-06-01-vol-density-bz3-refinement-session-status.md)
- Compute non-canonical audit (this session): findings in chat reply / not yet a standalone doc
