# EW couplings from substrate — empirical match hypotheses + categorical paths

**Date:** 2026-05-24
**Trigger:** Per author direction, work on three research-grade items:
1. Categorical derivation of g, g' from substrate
2. Investigation of v_framework / v_SM ≈ 1.78 factor
3. Cross-particle-class ratio 171/143 ≈ 1.196 categorical origin

**Status:** Empirical-match probe ([`ew_couplings_substrate_derivation_probe.py`](../../computations/probes/ew_couplings_substrate_derivation_probe.py)) tested ~50 candidate substrate formulas. This audit documents the cleanest matches + identifies which are structurally promising vs likely numerology.

## §1. Clean matches found (< 1% deviation)

| target | candidate formula | predicted | actual | dev |
|---|---|---:|---:|---:|
| **g** (SU(2)_L coupling, 0.6535) | $\sqrt{2 h_0 (1 + h_0^2/2)}$ | 0.6528 | 0.6535 | **−0.10%** |
| **g** (alt) | $h_0 \cdot \pi$ | 0.6552 | 0.6535 | **+0.26%** |
| **g** (alt, leading) | $\sqrt{2 h_0}$ | 0.6458 | 0.6535 | −1.17% |
| **v_ratio** (≈ 1.78) | $\log(6)$ | 1.7918 | 1.7853 | **−0.50%** |
| **v_ratio** (alt) | $4/\sqrt{5}$ | 1.7889 | 1.7853 | −0.66% |
| **171/143** (≈ 1.196) | $6/5$ | 1.200 | 1.196 | **+0.35%** |
| **171/143** (alt) | $\sqrt{\sqrt{2}}$ | 1.189 | 1.196 | −0.55% |
| **g/g'** (1.865) | $\sec(\theta_W) / \tan(\theta_W)$ | 1.865 | 1.865 | exact (circular: uses SM θ_W) |

## §2. Structurally-suggestive interpretations

### g ≈ $\pi \cdot h_0$ (the cleanest non-circular match)

The substrate's natural parameter is $h_0 = q_0 - q_0^{-1} \approx 0.2086$.
The SU(2)_L coupling $g \approx \pi \cdot h_0$ within 0.26%. This has
a clean structural form:
- Linear in substrate parameter $h_0$
- Coefficient is the universal constant $\pi$
- No free parameters

**Categorical hypothesis**: the SU(2)_L gauge coupling at the substrate
is proportional to the substrate's deformation parameter with a $\pi$
normalization. Possible categorical origins:
- $\pi$ from the trace of identity over the unit circle's Lie algebra
- $h_0$ from the Hecke deformation appearing as the connection 1-form
- The product $\pi \cdot h_0$ as the integrated curvature

A formal Lean statement would be:
```lean
class SubstrateGaugeCoupling extends CategoricalHiggsIdempotent where
  /-- The g coupling is π · h_0 (substrate-derived). -/
  g_from_substrate : gauge_coupling_g = Real.pi * h_substrate_value
```

This pushes the structural question to: why is `g = π · h_0` the
correct categorical formula? (Answering needs the connection-1-form
derivation in the Lie crossed module per `yekutieli-mi-derivation-path.md`.)

### v_ratio ≈ log(6) — the "6" is structurally significant

The framework's effective $v_{\text{framework}} / v_{\text{SM}} \approx 1.78$
matches $\log(6) \approx 1.7918$ within 0.5%.

**The "6" is structurally meaningful**: it's $|S_3| = 6$, the order of
the symmetric group on 3 elements — directly relevant to:
- The 3 strands of the Borromean braid $\mathcal{B}_3$
- The 6 GS-NF basis knot operators ($\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-$) per [`knot-operator-bring-action.md`](../../content/quantum-observable-universe/braids-and-knots/knot-operator-bring-action.md)
- The 6-fold symmetry of the trefoil at the EM-side strong-force anchor

**Categorical hypothesis**: the $v$-normalization difference between
the framework's RT chain and SM convention is $\log |\text{knot-operator-group}|$.
This would be a conditional theorem under the `TorusKnotMass` class:
```lean
theorem v_framework_over_v_SM_eq_log_S3
  [TorusKnotMass] : v_framework / v_SM = Real.log 6
```

The logarithm appearing is structurally consistent with the
Chern–Simons-style action $\propto \log |G|$ for finite gauge groups.

### 171/143 ≈ 6/5 — the gauge-vs-scalar ratio

The cross-particle-class normalization ratio matches $6/5 = 1.200$
within 0.35%.

**Structural interpretation candidates:**
- $6 = |S_3|$ (knot operator group); $5 = $ number of conjugacy classes
  of $S_4$ (= partition count for the Wedderburn decomposition at $H_4$)
- $6/5$ = (knot-operator basis size) / (Wedderburn-block count at $H_4$)
- Or: $6 = |B_3|/|S_3|$-like ratio; $5 = $ Wedderburn blocks

**Categorical hypothesis**: scalar/gauge mass-factor ratio captures
the structural ratio
$$\frac{\text{scalar normalization}}{\text{gauge normalization}} = \frac{|\text{operator basis}|}{|\text{Wedderburn blocks at H}_4|}$$

A formal statement:
```lean
theorem scalar_gauge_factor_ratio [TorusKnotMass] :
    scalar_mass_factor / gauge_mass_factor = (6 : ℝ) / 5
```

## §3. Likely numerology (do NOT promote without categorical backing)

The probe also found "matches" at the few-% level that are likely
coincidental:

- $g' \approx h_0 \cdot \varphi$ (golden ratio) at -3.70% — golden ratio
  doesn't have obvious categorical origin in the framework
- $\sqrt{\sqrt{2}}$ matches the scalar/gauge ratio at -0.55% — but
  $\sqrt{\sqrt{2}} = 2^{1/4}$ is just a power of 2, no clean structural
  interpretation
- $(1+h_0)^{\sqrt{3}}$ matches at +16% — too many free parameters
  (exponent $\sqrt{3}$ is not substrate-natural)

The probe tested ~50 candidates total; finding 3-4 sub-1% matches by
chance is not surprising. The criteria for "promote to hypothesis":
1. Match within 1%
2. Formula uses ONLY substrate quantities + universal constants ($\pi, e$, integer)
3. Has a plausible categorical origin in the existing framework

**Three candidates pass this triple test:**
- $g = \pi \cdot h_0$ (uses $h_0$ + $\pi$; categorical origin in connection 1-form)
- $v_{\text{ratio}} = \log(6)$ (uses $|S_3|$ from knot-operator group)
- $171/143 = 6/5$ (uses $|S_3| / |\text{partitions of 4}|$)

## §4. Honest assessment

These are **structurally suggestive** matches but **NOT derivations**.
The next-round work to convert them into rigorous statements:

### (a) Derive g = π·h_0 from connection 1-form integration

The framework's connection 1-form $\alpha$ on the Frobenius-Hopf
substrate has integral $\int \alpha$ over a closed loop. If this
integral equals $\pi \cdot h_0$ at the substrate point, then
$g = \pi \cdot h_0$ would be a categorical theorem. The Yekutieli
MI machinery [`yekutieli-mi-derivation-path.md`](2026-05-24-yekutieli-mi-derivation-path.md)
is the natural setting.

Effort: research-grade, 1-2 weeks.

### (b) Derive v_framework / v_SM = log(6) from knot-operator partition function

If the framework's effective $v$ comes from a partition function on
the knot-operator group $S_3$ (the 6 GS-NF operators), the $\log(6)$
factor would arise as the log of the group order. This connects to
the Chern–Simons partition function on closed 3-manifolds.

Effort: research-grade, 1-2 weeks.

### (c) Derive 171/143 = 6/5 from Wedderburn-block counting

The scalar (H) sector lives on H_4(q)'s Wedderburn decomposition with
5 partition blocks; the gauge (W, Z) sectors live on the knot-operator
basis with 6 generators. The ratio 6/5 reflects this **block-counting
mismatch**.

A clean derivation would compute:
- For scalars: $\text{trace}_{H_4} = \sum_{\lambda \vdash 4} y_\lambda \chi_\lambda$ (5 terms)
- For gauges: $\text{trace}_{\text{operator basis}} = \sum_{op \in S_3} c_{op}$ (6 terms)

with the ratio of these being 6/5 by direct count.

Effort: tractable, 2-3 days (closed-form arithmetic).

## §5. Recommendation

**Promote** the three structural hypotheses to candidate categorical
theorems in `TorusKnotMass` (with `sorry` for the structural derivation):

```lean
namespace QOU.BraidKnot.TorusKnotMass

variable [TorusKnotMass] [CategoricalHiggsIdempotent]

/-- HYPOTHESIS (1% empirical match): g = π·h_0 at substrate. -/
theorem g_eq_pi_h_substrate : ∃ h_0 : ℝ, h_0 = Q_0 - 1/Q_0 ∧
    gauge_coupling_g = Real.pi * h_0 := sorry

/-- HYPOTHESIS (0.5% empirical match): v_framework / v_SM = log(6) = log|S_3|. -/
theorem v_ratio_eq_log_S3 :
    v_framework_GeV / 246 = Real.log 6 := sorry

/-- HYPOTHESIS (0.35% empirical match): scalar/gauge factor = 6/5 = |S_3|/|partitions(4)|. -/
theorem scalar_gauge_eq_six_fifths :
    scalar_mass_factor / gauge_mass_factor = (6 : ℝ) / 5 := sorry

end QOU.BraidKnot.TorusKnotMass
```

**Do NOT** promote to production / no `prop:` block — these are
**conjectures** awaiting categorical derivation.

The `sorry`s represent the OPEN structural derivations (a, b, c above),
not gaps in lower-level Lean reasoning. Per AGENTS.md §3b-cond, these
are class-conditional hypotheses; downstream theorems take them as
instance hypotheses.

## §6. Cross-references

- [PR #1128](https://github.com/litlfred/qou/pull/1128) — empirical 143/171 finding
- [PR #1137](https://github.com/litlfred/qou/pull/1137) — refined `CategoricalHiggsIdempotent` + `TorusKnotMass` classes
- [`docs/audits/2026-05-24-pr1122-retraction-and-existing-canonical-adaptation.md`](2026-05-24-pr1122-retraction-and-existing-canonical-adaptation.md) — adaptation framework
- [`docs/audits/2026-05-24-gauge-vs-scalar-mass-factor-derivation-path.md`](2026-05-24-gauge-vs-scalar-mass-factor-derivation-path.md) — earlier 143/171 audit (paths A/B/C considered, this audit identifies the 6/5 ratio match)
- [`docs/audits/2026-05-24-yekutieli-mi-derivation-path.md`](2026-05-24-yekutieli-mi-derivation-path.md) — categorical machinery for the connection-1-form derivation of g
- [`content/quantum-observable-universe/braids-and-knots/knot-operator-bring-action.md`](../../content/quantum-observable-universe/braids-and-knots/knot-operator-bring-action.md) — 6 GS-NF basis operators (source of the "6" in log(6) and 6/5)
- [`computations/probes/ew_couplings_substrate_derivation_probe.py`](../../computations/probes/ew_couplings_substrate_derivation_probe.py) — empirical match probe (this PR)
