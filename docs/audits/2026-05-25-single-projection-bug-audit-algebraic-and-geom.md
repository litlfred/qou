# Single-projection bug audit — algebraic AND geometric sides

**Date**: 2026-05-25
**Branch**: `claude/vol-density-derivation-bug-squash-2026-05-25`
**Status**: Audit. Catalogs every production script + active probe in
`computations/` that projects to a SINGLE Wedderburn
block (algebraic side) OR a SINGLE cell / fiber-orbit (geometric
side), instead of the canonical multi-block × multi-fiber distribution
required by `m(K) = m_e · VolDensity(K, q₀)`.

## §0. Two-dimensional structural reduction

The framework's full structure has **two orthogonal axes**:

| Axis | Discrete index | Production projection | Canonical needs |
|------|----------------|----------------------|------------------|
| **Algebraic** (Hecke H_n(q)) | partition λ ⊢ n | single Wedderburn block (ν_SDP integer) | `Σ_λ y_λ · χ_λ(β_atom)` |
| **Geometric** (Bring's quintic / Reeb bundle) | fiber-orbit or cell | single S_3 subgroup orbit OR single-cell | full SO(3) integral OR Reeb-bundle integral |

The single-projection bug pattern manifests on BOTH sides. Sibling PR
[#1224](https://github.com/litlfred/qou/pull/1224) audits the algebraic
side; PR [#1220](https://github.com/litlfred/qou/pull/1220) measures the
empirical c-variance. This audit catalogs the codebase.

## §1. Algebraic-side single-Wedderburn-block scripts

### §1.1 Production / load-bearing

| Script | Pattern | Bug confirmed by |
|--------|---------|-------------------|
| `mass_table_ppb.py` | `B = ν_SDP · m_e · Vol(K)` w/ ν_SDP integer | PR #1220 c-variance |
| `magic_A_formula.py` | `B = ν · m_e · A · 8G` w/ ν_SDP=2 | inherited at all α-cluster atoms |
| `low_isotope_binding_sweep.py` | (DEPRECATION-CANDIDATE) same pattern | called by live importers |
| `alpha_cluster_recursion.py` | `B = n_α·B(⁴He) + n_pairs·c_αα` | non-multiplicative bar-sym h² (PR #1220) |

Each projects to ONE λ ⊢ n; canonical needs all N partitions:

| Atom | n | N = #partitions | Production | Missing |
|------|---|------------------|------------|---------|
| 4He | 12 | **77** | 1 | 76 |
| 8Be | 24 | 1575 | 1 | 1574 |
| 40Ca | 120 | ~10⁹ | 1 | astronomical |

### §1.2 Per-irrep / Frobenius-pairing scripts

| Script | Pattern | Status |
|--------|---------|--------|
| `per_atom_rho_deviation.py` | `ρ_F = single integer (1 or 2)` per atom | shows ρ(3He)=2.062 deviation from ν_SDP=2 |
| `per_irrep_pole_proton_h3.py` | poles per single irrep, no Σ over λ | partition-level diagnostic |
| `rho_k_h3a_frobenius_pairing.py` | Frobenius pairing per single tableau | per-tableau probe (single point in distribution) |
| `rho_k_h3a_wenzl_bridge.py` | Wenzl projector per single λ | single-block evaluation |

These ARE designed as per-irrep diagnostics (so single-block is appropriate
for each call), BUT the framework's downstream consumers treat the output
as a single "the answer" rather than aggregating over λ.

### §1.3 Δ_λ closure attempts (sibling PR #1224 catalogs 14)

All Δ_λ ansatz scripts attempt to ENUMERATE partition contributions
but assume a specific single ansatz per attempt:

| Script | Δ_λ ansatz | Outcome |
|--------|-------------|---------|
| `delta_lambda_empirical_tabulation.py` | 4 ansätze | partial fit |
| `delta_lambda_two_factor_phase2.py` | two-factor | failed |
| `delta_lambda_z4N_phase4.py` | Z_4N | failed |
| `delta_lambda_jsj_phase3.py` | JSJ decomposition | failed |
| `delta_lambda_alexander_phase4.py` | Alexander polynomial | failed |
| `delta_lambda_fr_identity_phase5c.py` | Frobenius-Riemann identity | failed |
| `log_delta_categorical_derivation.py` | log Δ categorical | partial |

Per PR #1224 §1: 14 prior attempts have all failed. The structural
constraint that none have imposed is **multi-atom consistency** —
exactly the constraint PR #1220 measured violation of.

### §1.4 Joint solvers (multi-atom but still single-block)

| Script | Pattern | Limitation |
|--------|---------|------------|
| `joint_tower_sdp_solver_v2.py` | joint SDP across atoms | still per-block within each atom |
| `pn_alpha_lp_dual.py` | LP duality for p/n/α | single-block per nucleon |
| `lambda_scale_all_c_i_family_a.py` | c_i family-A | single hypothesis |

## §2. Geometric-side single-cell / single-fiber scripts

### §2.1 Borromean Geom probes

| Script | Pattern | Bug |
|--------|---------|-----|
| `vol_density_borromean_h4_probe.py` | solve-for-c_4 single hypothesis | single Bring cell, no Σ over fibers |
| `vol_density_borromean_q_locality_probe.py` | q-locality at single q-point | single point not integral |
| `lambda_scale_refinement_h4_correction_bring.py` | Bring h⁴ correction single value | single Bring cell |
| `t3n_binomial_pattern_probe.py` | T(3,n) binomial single pattern | single torus-knot family |
| `h4_h2_cross_algebra_bridge_probe.py` | H_4 ↔ H_2 bridge single mapping | NEG result (sibling commit) |

### §2.2 Reeb-bundle / Yekutieli single-cell residuals

| Script | Pattern | Status |
|--------|---------|--------|
| `per_nucleon_shift_derivation.py` | per-nucleon (= per-cell) shift | residual of purged Yekutieli per-cell |
| `atomic_chirality_residue.py` | per-cell chirality | same residual |
| `reeb_flow_garside_closed_form_verification.py` | Reeb flow Garside single closed form | single Reeb leaf |

The **Yekutieli per-cell λ_scale extension** was PURGED 2026-05-24 (commit
`71d674da1`) as non-canonical. These two residual scripts retain the
"per-cell" framing but at lower-level operations; need audit whether they
should also be retired.

### §2.3 S_3 subgroup vs full SO(3) — explicit gap

The **D10 (spin SU(2)_S) duality tracker row** flags this directly:

> implicit in knot-operator catalogue (S₃ subgroup); full SO(3) gap
> flagged in `2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`

The framework's pipeline uses only the **S_3 discrete subgroup** of
SO(3) — 6 permutations on 3 color sheets — which sees up to ℓ=1
spherical harmonics. The full SO(3) opens ℓ=2 (5-dim irrep) which
contributes the h⁴ = −3/4 Borromean coefficient.

Scripts affected by S_3-only projection:
- `vol_density_borromean_h4_probe.py` (the h⁴ probe; assumes only ℓ ≤ 1
  contributes)
- `tau_hat_n_proton_realisation.py` (τ functor on S_3 orbits)
- `lambda_scale_rd_hoefsmit_symbolic.py` (Hoefsmit per S_3 orbit)
- `lambda_scale_refinements_composed_predictions.py` (composed S_3
  predictions)
- `nv_categorical_derivation_probe.py` (no-volume categorical derivation
  on S_3 orbit)
- `three_parameters_wedderburn_probe.py` (3-parameter Wedderburn — by
  S_3-orbit class)

### §2.4 Bring color-tube weighted averaging

Per [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
§"Bring color-tube weighted averaging": the framework's geometric
averaging across the 10-fold S_3 orbit structure (the "10" in cheat
sheet §Bring) **is** weighted, but the weight assignment might still
be single-orbit-class rather than full continuous SO(3).

Scripts that touch the Bring color-tube structure:
- `path4_rho_K_at_h3A.py`
- `gb_filtration_jet_tracker.py`
- `_li_2_q_util.py`

Status: not directly confirmed buggy; partial audit needed.

## §3. Cross-side unified picture

The framework's full structural reduction:

```
B_canonical(atom) = m_e · Σ_λ ∫_M  y_λ(atom)  ·  χ_λ(β_atom)(g)  ·  dμ_λ(g)
                                  └ algebraic ┘  └─ geometric ─┘
                                  partition λ      SO(3) integral g ∈ G
```

Production simplification:
```
B_prod(atom) = m_e · ν_SDP(λ_dominant) · χ_λ_dominant(β_atom)(g_S3)
                                                            └─ single S_3 orbit
                    └ single integer for single λ_dominant ┘
```

This is a **double simplification**: collapses both the λ-sum AND the
SO(3) integral to a single (λ, orbit) point. The 195% c-variance
(PR #1220) is the joint signature of both projections being wrong
per-atom.

## §4. Bug counts

### §4.1 Algebraic-side single-Wedderburn-block scripts

| Category | Count |
|----------|-------|
| Production / load-bearing | 4 |
| Per-irrep diagnostics | 4 |
| Δ_λ closure attempts | 7+ |
| Joint solvers (multi-atom, single-block) | 3 |
| **Total algebraic single-block** | **~18** |

### §4.2 Geometric-side single-cell / single-fiber scripts

| Category | Count |
|----------|-------|
| Borromean Geom probes (single Bring cell) | 5 |
| Reeb-bundle single-cell residuals | 3 |
| S_3 subgroup (no full SO(3)) | 6 |
| Bring color-tube (partial audit) | 3 |
| **Total geometric single-projection** | **~17** |

### §4.3 Combined

**~35 scripts** in `computations/` exhibit some form of
single-projection bug. The production-load-bearing subset is small
(4 algebraic + 5 geometric = 9 scripts); the rest are probes /
diagnostics that NEED to be single-projection for their per-block-or-
cell purpose but whose downstream consumers may treat them as final
answers.

## §5. Fix priority

### §5.1 Production-load-bearing (must fix for canonical mass table)

1. **mass_table_ppb.py** — single-Wedderburn-block AND S_3-subgroup
   (worst of both worlds). Fix path: full Σ_λ y_λ · χ_λ over all
   λ ⊢ n × full SO(3) integral.
2. **alpha_cluster_recursion.py** — non-multiplicative at bar-sym h²
   (PR #1220). Fix path: replace recursion with per-atom direct SDP.
3. **magic_A_formula.py** — drives 4He which cascades to 7 of 8 KLR
   violations. Fix path: canonical Wigner SU(4) singlet projection
   (Option F, my D11 scaffold).

### §5.2 Geometric closure paths

1. **vol_density_borromean_h4_probe.py** — currently solves for single
   c_4 hypothesis. Replace with full SO(3) integral; cross-check
   h⁴ = −3/4 categorically.
2. **D10 SO(3) extension** — promote from S_3 subgroup to full SO(3)
   in the knot-operator catalogue. Audit: `2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`.

### §5.3 Yekutieli per-cell residuals (cleanup)

`per_nucleon_shift_derivation.py` + `atomic_chirality_residue.py` retain
"per-cell" framing post-purge. Audit whether to retire or refactor.

## §6. Concrete next probes (single-session feasible)

1. **Per-partition χ_λ(β_⁴He) tabulation** — using just-landed tier-3
   `chi_lambda_braid` infrastructure (needs Python wrapper, my audit
   PR #1228 §10.1). Enumerates which of the 77 partitions of 12 have
   non-trivial χ_λ at q_0; sizes the gap from "1 of 77".

2. **Full-SO(3) ℓ=2 contribution to Borromean h⁴** — extend
   `vol_density_borromean_h4_probe.py` to include the SO(3) ℓ=2
   spherical-harmonic contribution; check if it produces h⁴ = −3/4
   categorically. Connects to D10 scaffold (my PR #1168 conj block).

3. **Δ_λ probe-1 (bar-invariance LP)** from sibling PR #1224 §3.1 —
   sibling will likely author; coord through their PR.

4. **Audit-retire residual Yekutieli per-cell scripts** — quick
   review of `per_nucleon_shift_derivation.py` +
   `atomic_chirality_residue.py` to determine if they should join
   the purge from commit `71d674da1`.

## §7. Cross-references

- [`docs/audits/2026-05-25-vol-density-derivation-error-localization-and-klr-path.md`](2026-05-25-vol-density-derivation-error-localization-and-klr-path.md) — companion audit (PR #1228)
- [`docs/audits/2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`](2026-05-24-h4-coefficient-source-trace-and-so3-gap.md) — D10 S_3 → SO(3) gap
- [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md) — VolDensity single-formula framing + Yekutieli per-cell PURGED
- [PR #1214](https://github.com/litlfred/qou/pull/1214) — wiring-status taxonomy + KLR positivity check
- [PR #1220](https://github.com/litlfred/qou/pull/1220) — empirical c-variance measurement
- [PR #1224](https://github.com/litlfred/qou/pull/1224) — Δ_λ closure synthesis (sibling)
- Commit `71d674da1` — Yekutieli per-cell λ_scale extension PURGED
- D10 conj scaffold: `conj:spin-from-so3-fiber.md` (PR #1168)
- D11 conj scaffold: `conj:wigner-su4-from-spin-isospin.md` (PR #1173)
