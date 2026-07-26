# A=4 H₁₂ Brunnian deficit-sign measurement — the Route-3 antecedent is REFUTED (τ_L₄ > 1)

**Date:** 2026-07-26
**Branch:** `claude/deltalambda-a4-h12-brunnian-measure-2026-07-26` (PR #4378)
**Probe:** [`computations/deltalambda/a4_h12_brunnian_deficit_measure_probe.py`](../../computations/deltalambda/a4_h12_brunnian_deficit_measure_probe.py)
**Witness:** [`computations/deltalambda/a4-h12-brunnian-deficit-measure.witness.json`](../../computations/deltalambda/a4-h12-brunnian-deficit-measure.witness.json)
**Lean:** [`content/quantum-observable-universe/lean/QOU/MassTheory/HeliumBrunnianDeficitMeasured.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/HeliumBrunnianDeficitMeasured.lean) (lean-direct exit 0, sorry-free)

## The question

The merged A=4 sign wall `QOU.MassTheory.HeliumFourBodyCluster.mu4_ne_brunnian4Cluster`
(#4376) is **scope-(b) CONDITIONAL on** the 4-component Brunnian level deficit being
non-negative — `τ_L₄ ≤ 1`, so `c₄ = E₀·(1 − τ_L₄) ≥ 0`, sign-incompatible with the
derived `μ₄ = −4.591 < 0`. Whether that antecedent actually holds at the substrate
`q₀` for a *genuine* 4-component Brunnian link was the open companion input. This
measures it, forward and 0-fit.

The earlier probe `helium_four_body_cluster_probe.py` measured cabled **block-chain**
words whose Brunnian-ness was never verified — a τ>1 there does not bear on the wall,
because the wall is about the *Brunnian* deficit specifically. This measurement uses a
**verified-Brunnian** word.

## Construction (0-fit, topological constraint only)

The genuine Brunnian 4-braid is the iterated left-normed commutator of pure-braid
band generators `A_{ij} = (σ_{j-1}…σ_{i+1}) σ_i² (σ_{i+1}⁻¹…σ_{j-1}⁻¹)`:

    w₄ = [[A₀₁, A₁₂], A₂₃]        (0-based strands; = [[A₁₂,A₂₃],A₃₄] 1-based).

Brunnian-ness is verified **exactly** via the pure-braid strand-forgetting map
`d_k : P_n → P_{n-1}` (`d_k(A_{ij}) = 1` if `k∈{i,j}`, else reindex): deleting ANY
strand collapses the nested commutator to the identity braid, so every proper
sub-link is the unlink. The probe applies `d_k` at the band level and confirms each
delete-strand sub-deficit is machine-zero. The word is fixed by this **topological**
constraint — nothing is tuned to any target.

## Result

| Level | `τ_L₄ = g_link/g_unlink` | deficit `1−τ_L₄` | sign | leading order | Brunnian check |
|-------|--------------------------|------------------|------|---------------|----------------|
| base n=4 | 1.000145898 | −1.459·10⁻⁴ | **−** | n≈6.06 = O(h⁶) | all 4 delete-strand ≈ 1e-15 ✓ |
| H₁₂ (width-3 cable, 77 λ) | 1.013914085 | −1.391·10⁻² | **−** | (coeff-ratio lift, sign preserved) | all 4 delete-block ≈ 1e-14 ✓ |

- **A=3 validation** (same machinery): band-commutator `[A₀₁,A₁₂]` reproduces the
  Borromean — deficit **+**1.633·10⁻³, O(h⁴) (n≈4.05), all delete-strand sub-links
  trivial. The machinery is correct.
- **Robustness.** The negative A=4 sign is identical across three Brunnian
  representatives (left-normed, right-normed, negative-inner) and across the
  `|χ|`-vs-signed perblock convention (the characters are positive at q₀, so the `|·|`
  is not responsible for the sign). Cabling to H₁₂ **preserves and amplifies** the
  sign (base −1.46e-4 → H₁₂ −1.39e-2, ~95×), consistent with the coefficient-ratio
  lift (the shared h⁶ cancels; only the coefficient scales).
- **Leading Milnor order O(h⁶) = 2·(4−1)** confirmed — one Milnor step above the
  Borromean O(h⁴), exactly the merged file's `brunnian4Order`.
- **Compute ceiling.** A single H₁₂ cabled trace (180-crossing word) took **126.5 s**;
  the base n=4 traces are <0.1 s. The base-level result is the rigorous, decisive one;
  H₁₂ confirms the sign persists in the magnitude regime.

## Interpretation — ANTECEDENT REFUTED (honest, scope-(a))

The genuine Brunnian level deficit is **negative** (`τ_L₄ > 1`) at both levels, so the
antecedent `τ_L₄ ≤ 1` of the merged conditional wall is **measured FALSE**. Two
consequences:

1. **The sign obstruction is removed.** The Brunnian cluster `c₄ = E₀·(1 − τ_L₄) < 0`
   has the **same sign** as the derived `μ₄ = −4.591 < 0`. The sign-exclusion the wall
   asserted under `τ ≤ 1` does not arise at the substrate; on sign grounds the genuine
   4-component Brunnian binding cluster is *compatible* with `μ₄`. The A=4 recipe
   **reopens on sign**.
2. **A Milnor-parity sign flip.** A=3 Borromean (length-3 Milnor) deficit is POSITIVE
   (O(h⁴)); A=4 Brunnian (length-4 Milnor) deficit is NEGATIVE (O(h⁶)). The level trace
   crosses the unlink between the two — a structural observation, 0-fit.

**Scope discipline (per AGENTS.md "refuted/ruled-out" STRICT).** This is a
**scope-(a)** measured negative on the *antecedent* (this genuine Brunnian construction,
this level, this convention — measured, robust), **not** a structural exclusion of
anything. It does **not** claim `μ₄` is derived: the sign obstruction being removed is
not a magnitude derivation. The magnitude test (`|c₄|` vs `|μ₄| = 4.591`; base
|c₄|≈6.1e-4 MeV, H₁₂ |c₄|≈5.8e-2 MeV — both far below) becomes the live question and is
**not fitted** here. Nothing is wired; `μ₄`'s value enters no proof (used only as the
forward target sign). `free_parameters = 0`.

**Relation to the merged wall.** `HeliumFourBodyCluster.mu4_ne_brunnian4Cluster` and
`sign_swap_a3_a4` remain true as *implications* (they are conditional on `τ ≤ 1`), but
their antecedent is measured false, so they do not close the A=4 case. This session
does **not** rewrite them; the companion `HeliumBrunnianDeficitMeasured.lean` records
the measured value and its arithmetic consequences honestly:
`measured_antecedent_fails`, `brunnian4Cluster_neg_of_tau_gt_one`,
`mu4_sign_compatible_measured_brunnian`, `brunnian_deficit_sign_flip_a3_a4`.

## Files

- Probe: `computations/deltalambda/a4_h12_brunnian_deficit_measure_probe.py`
- Witness: `computations/deltalambda/a4-h12-brunnian-deficit-measure.witness.json`
- Lean: `content/quantum-observable-universe/lean/QOU/MassTheory/HeliumBrunnianDeficitMeasured.lean`
