---
# qou-7nwg
title: can a colour-only fibre host the 3S1/1S0 distinction at all? the two-nucleon bound/unbound split is spin-tensor, and Schur-Weyl kills spinor C^2
status: in-progress
pr: 8215
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T02:09:31Z
updated_at: 2026-10-04T15:16:51Z
parent: qou-v2om
---


## RE-SCOPED — the premise of this bean was over-stated (2026-08-16)

Filed on my claim that the bound/unbound split is **spin-tensor** (`³S₁–³D₁`
coupling), so a colour-only fibre — Schur–Weyl having killed the spinor `ℂ²` —
structurally could not host it.

That is wrong as stated. For two nucleons in a relative S-wave, antisymmetry ties
spin and isospin: `(S,T) = (1,0)` or `(0,1)`. The split is therefore expressible
**either** as `S` or as `T`, and `T` is available in the Hecke algebra with no
spin degree of freedom at all — the spectral projectors `P±` **are** the
`T=1`/`T=0` split, with scalars the `n=2` Wedderburn weights `y_(2)`, `y_(1,1)`.

The tensor force is the *mechanism* in nuclear physics. It is not the only route
to the *quantum number*.

## The actual question, with the sourced numbers

Machleidt CD-Bonn (arXiv:nucl-th/0006014) §III Eqs. (3.1)–(3.3), Table XI:

| channel | T | T₃ | `a` (fm) | bound |
|---|:--:|:--:|---:|---|
| pp ¹S₀ | 1 | +1 | −17.3 | no |
| nn ¹S₀ | 1 | −1 | −18.9 ± 0.4 | no |
| np ¹S₀ | 1 | 0 | −23.740 ± 0.020 | no |
| np ³S₁ | **0** | 0 | **+5.419 ± 0.007** | **yes** |

Across `T₃` at fixed `T=1`: a ~25 % modulation (`Δa_CIB = 6.44 fm` on ~20 fm),
all unbound. Across `T`: the sign **flips**.

The framework grades its interface by **crossing sign = writhe = `T₃`**
(`WeakIsospinT3Grading.lean`, quoted: pp uses `σ_g`, nn uses `σ_g⁻¹`) — i.e. it
is aimed at the small effect and has no grading by the one that flips the sign.

## So the question is a conjunction, not a fibre question

1. **grade by `T`** — available for free (projectors), no new parameter;
2. **escape `μ ≤ z < 1`** — proved impossible for any single crossing
   (`SingleCrossingAlwaysBinds.lean`); available at writhe-normalised even
   NEGATIVE stacked powers (`qou-pjx4`), whose magnitudes are 6–9× off.

Neither alone suffices. Superseding audit:
[`2026-08-16-interface-graded-by-t3-but-the-physics-is-graded-by-t.md`](../docs/audits/2026-08-16-interface-graded-by-t3-but-the-physics-is-graded-by-t.md).


## Progress Update (PR #8215)
- [x] Pure Lean 4 formalization wired into `QOU.lean` (`FreeNucleonPrecisionStraddleDefect.lean`, `TowerPartitionGrowthAndWeightSubstitution.lean`, `InterfaceScaleFloorAndBandDisjointness.lean`, `SWaveAntisymmetryIsospinGrading.lean`; 0 `sorry`, 0 vacuity advisories across all 6 static audits)
- [x] 50-dps `mpmath` + exact integer-partition DP probe (`computations/probes/free_nucleon_straddle_h3a_band_isospin_probe.py`) and stamped witness (`computations/probes/free-nucleon-straddle-h3a-band-isospin-probe.witness.json`, 0 raw `float64` fields)
- [ ] Awaiting adversarial review and Merge Manager merge of PR #8215 (`ready: 5d009c2bc892c5362b5b72a46c0f7f2e162d8d40`)
