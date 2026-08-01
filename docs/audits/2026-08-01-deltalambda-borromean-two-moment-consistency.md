# Δ_λ Borromean/Brunnian magnitude: the two-moment cross-check fails — the μ₃ near-miss is likely coincidental

**Date:** 2026-08-01 · **Axis:** Δ_λ residual-moment closure (binding) · **Tier:**
numerical scope-(a) adversarial cross-check · **Discipline:** 0-fit, μ_A never inverted,
nothing wired, no tier change.

## What was claimed

The Δ_λ residual-moment closure identifies the A-body irreducible residual moment `μ_A`
(forward AME−model, #4320) with the A-component **Brunnian cluster**
`c_A = E₀·(1−τ_{L_A})` at the ρ_F-matched cabled level:

- **A=3** — Borromean 3-cluster at H₉ (three width-3 cables): sign derived (#4360), and
  the magnitude a **"near-miss lead"** — `c₃ = +0.297 MeV = 0.63× μ₃`, O(h⁴), 0-fit (#4364).
- **A=4** — genuine 4-Brunnian `[[A₀₁,A₁₂],A₂₃]` at H₁₂ (four width-3 cables): sign
  derived (`τ_L₄ > 1 ⇒ c₄ < 0`, O(h⁶), `a4_h12_brunnian_deficit_measure_probe.py`).

Both **signs** follow the Milnor parity law `sign(1−τ_A) = (−1)^{A−1}` (μ₃>0, μ₄<0).

## The missing test

The μ₃ near-miss (0.63×) was reported as a **lead on a single moment**. A single moment
matched to 0.6× is weak evidence. The decisive check — which no prior probe ran — is
whether the **same 0-fit framing reproduces both moments at a consistent fraction**.

## Result (0-fit, from the committed witnesses)

[`borromean_two_moment_consistency_probe.py`](../../computations/deltalambda/borromean_two_moment_consistency_probe.py)
(4/4) reads both derived cluster values from their committed witnesses:

| moment | target μ_A | derived c_A (cabled) | fraction c_A/μ_A | order |
|---|---|---|---|---|
| **μ₃** (A=3, H₉) | +0.4708 | +0.2970 | **0.63×** | h⁴·¹ |
| **μ₄** (A=4, H₁₂) | −4.591 | −0.05824 | **0.0127×** (~79× short) | h⁶·¹ |

- **The two fractions are inconsistent by ~50×** (`f₃/f₄ = 49.7`).
- **The A-trend is backwards.** The physical residual moments **grow** with A
  (`|μ₄/μ₃| = 9.75`), while the Brunnian clusters **shrink** (`|c₄/c₃| = 0.20`) — because
  the 4-link is O(h⁶) vs the 3-link's O(h⁴), i.e. **more** h-suppressed. This suppression
  is intrinsic to the topology (first Milnor invariant at length A ⇒ O(h^{2(A−1)})), so it
  **cannot be tuned away without a fit**.

## Decomposition — legitimate topology vs the real coefficient gap

The ~50× is not all "failure": most of it is the framework's **own proved prediction**.
Normalizing out the intrinsic Brunnian order `h^{2(A−1)}` (`ĉ_A := c_A/h^{2(A−1)}`):

- intrinsic h-order factor `1/h² = 22.9×` — the framework's *own* O(h^{2(A−1)}) prediction;
- order-normalized coefficient growth `ĉ₄/ĉ₃ = 4.49` vs the moment growth `9.75` ⇒ a
  **residual coefficient-scaling gap of ~2.17×**.

So `49.7× = 22.9× (intrinsic, predicted) × 2.17× (coefficient, the real open piece)`. A
derived route (s5-so3 `W_λ`; independent κ) would need to supply that ~2.17× *and* reverse
the intrinsic-suppression sign of the A-trend — which fixed-cabling clusters cannot.

## Lean formalization (sorry-free, `lean`-direct exit 0)

[`QOU/MassTheory/BorromeanMomentScalingExclusion.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/BorromeanMomentScalingExclusion.lean)
proves the structural exclusion (not just the numerics):

- `clusterOrd_strictAnti` — for `0 < r < 1`, `κ > 0`, the cluster order `κ·r^k` is
  **strictly antitone** in the level index (clusters strictly decrease as A grows);
- `eq_at_most_once` — a strictly antitone sequence and a strictly monotone one agree at
  **at most one** index;
- `brunnian_identification_at_most_one_A` — hence the identification `c_A = μ_A` (with a
  strictly increasing residual-moment sequence `μ`) holds for **at most one** body-order;
- `clusterOrd_tendsto_zero` — the clusters `→ 0` as `A → ∞`, so they cannot track a growing
  moment sequence (the exclusion is not vacuous).

The physical constants are not fitted: `κ`, `0 < h < 1`, and the *growth* of `μ` enter as
hypotheses; the exclusion is derived from them.

## Conclusion

**The sign leg stands; the magnitude identification does not survive the second moment.**
A framework that reproduces μ₃ to 0.63× but μ₄ to only 0.0127×, and gets the A-scaling
**qualitatively wrong** (clusters shrink where the data grows), is not capturing the
magnitude physics. This **downgrades the μ₃ 0.63× "near-miss" from a lead toward a likely
coincidence** — a single moment landing at 0.6× carries little weight once the next moment
misses by ~80× with the trend inverted.

**What survives:** the **Milnor parity sign law** (μ₃>0, μ₄<0, both derived) is untouched —
that is a genuine 0-fit result. **What fails:** the identification `c_A ≈ μ_A` at fixed
cabling as a *magnitude* closure. Any A-dependent coefficient that would rescue it must
overcome an intrinsic O(h²)-per-order topological suppression running *opposite* to the
data — which cannot be a 0-fit fix.

**Implication for the Δ_λ magnitude:** the residual-moment magnitude is **not** the fixed-
cabling Brunnian cluster. The magnitude closure remains **open**, and the "coefficient
question" the #4364 audit flagged (cable width / tower height) is now shown to be a **first-
order A-scaling failure**, not a small residual — the surviving derive-or-refute routes
(s5-so3 `W_λ`; an independent κ with genuine A-scaling) must reproduce the *growing* moment
trend, which fixed-cabling Brunnian clusters structurally cannot.

## Scope (anti-laundering)

Reads two committed 0-fit witnesses; computes the two-moment consistency; reports the
failure honestly. No fit; μ_A never inverted; nothing wired; no tier change. The finding
is adversarial (it weakens a prior "lead"), per the critical-distance license.

## Cross-references

- A=3 magnitude near-miss (0.63×): `docs/audits/2026-07-26-deltalambda-borromean-magnitude-lift.md` (#4364)
- A=3 sign: `BorromeanThreeBodyCluster.lean` (#4360)
- A=4 Brunnian sign + c₄(H₁₂): `computations/deltalambda/a4_h12_brunnian_deficit_measure_probe.py`
- Milnor parity sign law: `MilnorParitySignLaw.lean`, `docs/audits/2026-07-27-deltalambda-milnor-parity-sign-law.md`
- Residual moments μ₂/μ₃/μ₄: #4320 `AdditiveResidualSimplex`
