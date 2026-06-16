# Truncation audit — where the level-0-only (3-term) tower is used

**User correction (2026-05-02):** The mass-tower formula isn't a
3-term truncation (descended + singletons + pairs at level 0
only). The full form per `rem:mass-endomorphism-jet-tower` is

$$\mathfrak{m}(W) = |\mathrm{tr}_M(W)| + \sum_{n=0}^{N}\!\left(\sum_{\xi \in \mathcal{S}^{(n)}_1}\!\Phi_q(|\mathrm{tr}_M(\xi)|) + z^2\!\!\!\sum_{(\xi,\xi') \in \mathcal{S}^{(n)}_2}\!\!\!\Phi_q(|\mathrm{tr}_M(\xi\xi')|)\right) + R_N$$

where the **sum is over jet levels n = 0, 1, …, N** and $R_N$ is
a geometric-series tail bound from
[`prop:jet-tower-convergence`](../../content/quantum-observable-universe/braids-and-knots/jet-tower-convergence.md).

This audit identifies every compute script and content block that
uses the **truncated** form (level 0 only, no jet sum).

## Compute (`computations/`)

### Truncated (level 0 only — needs jet-level extension)

| Script | Function | Notes |
|--------|----------|-------|
| `crt_markov.py` | `tower_mass_symbolic_eval` | descended + single + adjacent-pair at level 0 |
| `mass_endomorphism.py` | `mass_from_tower` | per-generator at level 0 |
| `mass_endomorphism_atom.py` | atom-level extension | level 0 |
| `mass_endomorphism_atom_exact.py` | exact variant | level 0 |
| `mass_at_3A_proper.py` | H_{3A} proper | level 0 |
| `per_braid_tower_hybrid.py` ⬅ **mine** | hybrid | level 0 only |
| `per_braid_tower_hybrid_full.py` ⬅ **mine** | full-Plancherel hybrid | level 0 only |
| `per_braid_tower_q_hecke.py` ⬅ **mine** | q-Hecke per-braid | level 0 only |
| `p2_2a_descended_wiring_witness.py` ⬅ **mine** | descended wiring | level 0 only |
| `atom_mass_physical_filter.py` | physical-filter mass | level 0 |
| `confinement_adaptive.py` | adaptive confinement | level 0 |
| `electron_chiral_probe.py` | electron probe | level 0 |
| `habiro_exact_mass_endomorphism.py` | Habiro exact | level 0 |
| `heavy_atom_opts.py` | heavy-atom optimizations | level 0 |
| `inter_nucleon_crossing_sweep.py` | crossing sweep | level 0 |
| `mass_endomorphism_magic_interpolation.py` | magic interpolation | level 0 |
| `per_block_phi_q.py` | per-block Φ_q | level 0 |
| `pair_factorisation_probe.py` | pair factorisation | level 0 |

**18 scripts truncated to level 0.** All recent additions from this
audit pass (per_braid_*) included.

### Jet-aware (already use the full form)

| Script | Mechanism |
|--------|-----------|
| `multi_level_jet_sum.py` | explicit jet-level loop |
| `jet_level_geometric_series.py` | geometric-series tail |
| `jet_level1_and_residual_search.py` | level-1 + residual |
| `binding_per_block_log.py` | per-block log + jet |
| `binding_full_jm_cells.py` | full Jucys–Murphy cells |
| `binding_full_content_pair.py` | full content pairing |
| `mass_formula_6term_mpfr_50dps.py` | 6-term jet-aware |
| `adjacent_vs_full_probe.py` | jet-stratified probe |
| `d_knot_extended_search.py` | extended search |
| `_phi_q_util.py` | Φ_q utility |
| `explore_items_1_and_2.py` | exploration |

**11 scripts already jet-aware.** The framework's tooling exists;
my per-braid hybrid family was the regression that needs fixing.

## Paper content (`content/quantum-observable-universe/`)

### Statement-level truncation

The paper has **two statements** of the mass tower:

| Block | Form | Status |
|-------|------|--------|
| [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md) | **truncated** (per-generator, 3 terms) | Original statement |
| [`rem:mass-endomorphism-jet-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-jet-tower.md) | **full jet form** (sum over n + tail) | The proper refinement |
| [`prop:per-braid-mass-tower`](../../content/quantum-observable-universe/braids-and-knots/per-braid-mass-tower.md) ⬅ **mine** | was truncated; now updated to full jet form | Just fixed (this commit) |

**Action: every block citing `prop:mass-endomorphism-tower` should
also cite the jet-tower remark to capture the full form.**

### Blocks citing the tower (15 found)

| Block | Tower citation | Form used |
|-------|---------------|-----------|
| `atom-knot-mass-derivation.md` | `prop:mass-endomorphism-tower` | truncated implied |
| `chirality-dual-space-derivation.md` | both | full implied |
| `descended-level-zero.md` | descended (level 0) | level 0 only by design |
| `e-infinity-page-identifications.md` | both | full |
| `frobenius-limits-substrate-cost.md` | tower | truncated |
| `graded-trace-residue-split.md` | tower | full (graded form) |
| `ilp-solution-count-unwrap.md` | tower | mixed |
| `jet-tower-convergence.md` | tail bound | jet-aware |
| `kashaev-volume-conjecture.md` | tower | tau-image, full |
| `knot-mass-formula-unified.md` | tower | unified, full |
| `mass-endomorphism-jet-tower.md` | itself | full |
| `motivic-mass-measure.md` | tower | mixed |
| `np-discrepancy-resolution.md` | tower | truncated |
| `phi-q-piece.md` | tower | full |
| `local-shadow-ordering.md` | tower | mixed |

Blocks that read as "truncated" or "mixed" likely need explicit
citation of the jet form.

## Implication for the 1ppb workplan

The hybrid validation results (0.65% spread across 10 atoms,
0.53 MeV ³He/³H split) were obtained with a **level-0-only
tower**. The jet-tower remark's empirical evidence is striking:

| Atom | adjacent-only @ level 0 | all-pairs @ level 0 | (further with jet sum?) |
|------|-----------------------:|--------------------:|-------------------------|
| 6Li  | 2.00% | 0.57% | ? |
| 9Be  | 1.91% | 0.70% | ? |
| 12C  | 2.34% | 0.83% | ? |
| 16O  | 2.45% | 0.86% | ? |

(My current hybrid uses **all-pairs at level 0**, matching the
~0.7% per-atom error column. The same atoms in my hybrid show
cal/m_e ~0.985, residual ~0.6% from the 0.992 anchor — consistent.)

**The cal/m_e spread of 0.65–1.06% I've been reporting is
DOMINATED by the missing jet-level n ≥ 1 terms.** Adding jet
levels n = 1 (and possibly 2) should drive the spread down toward
the calibration floor (~22 ppb).

### Workplan revision

| Phase | Was | Now (correct) |
|------:|-----|---------------|
| A.1 | Full Schur-Weyl over p(3A) | ✅ landed (showed: descended is exponentially small; doesn't move spread) |
| **A.3** | Pentagon ascension at all levels | 🔴 **upgraded to PRIORITY** — extending the tower to jet levels n ≥ 1 is the actual cal/m_e spread closer |
| A.2 | Φ_q normalisation derivation | unchanged (still research) |

### Concrete next step

Implement `per_braid_mass_hybrid_jet(Z, N, N_jet=1)` that:

1. Computes level-0 contribution (current hybrid).
2. Adds level-1 contribution: per-nucleon and per-pair sub-braid
   traces evaluated on the jet prolongation $A_1 = A_0 \otimes \Omega^1(A_0)$.
3. Adds geometric-series tail bound estimate.
4. Compares cal/m_e spread vs level-0-only.

The jet prolongation in the per-braid framework needs concrete
realization — the existing `multi_level_jet_sum.py` and
`jet_level_geometric_series.py` may have the recipe to lift.

## Headline

**18 compute scripts and ~5 content blocks are using the truncated
3-term tower form** (level 0 only). The framework's jet-aware tooling
(11 scripts + the jet-tower remark) is correct and should be the
template. Wiring the per-braid hybrid into the jet-tower form is the
prerequisite for closing the cal/m_e spread below 0.65% toward the
~22 ppb calibration floor.
