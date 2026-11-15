# Results: the nucleon gluon segment by the γγ rule

Pre-registration: [`preregistration.md`](preregistration.md) (step 1 `a341245311`,
step 2 `a9ca10d266`, both committed before computing). Probe:
`gg_gluon_segment_probe.py`, witness `gg-gluon-segment.witness.json`, **36/36
checks**. Exact over ℚ(q); proton pin as an exact rational; mpmath 60 dps for
display. Convention D, `z_D = q³/(q²+1)`. Diagnostics only. No element is
selected and the dashboard is not re-scored.

## Step 1: what the γγ rule gives

On three strands the γγ rule (`qou-ales`, `GammaGammaWordSelection.vertex`) has
exactly one vertex, `V = σ₀σ₁⁻¹`. That vertex is the corpus `gluonUnit`
(`toCorpus_vertex_zero`). So the rule fixes the **unit** of the gluon segment
uniquely. It does not fix the **number of units**. The output is the family
`{Vᵏ}`, which is not unique, so step 2 runs.

Corpus side-rules that name members:
- k = 1: the 2-letter slot of the 11-crossing budget.
- k = 3: the gluon treated as its own SDP component, selected like the core.
- k = 0: the retired "B₃ IS the gluon structure" convention.

`σ₀²` is not γγ (`gluonPair_not_gammaGamma`). It was not a bare census pick,
though. The corpus derives it by the H₂ PSD-parity rule (owner 2026-08-30,
`GluonVertexPsdParity`), which ranges over σ₀ᵏ and is a different rule.

## Calibration (all pass)

- The bar-parity-split probe reruns at 24/24.
- On `nuc11_interleaved` with the probe's own code:
  - f matches its closed form;
  - f = h·g;
  - g_odd = −h[2]_q(q²+q⁻²)/8;
  - Δtr = −0.1541948850472397056592555;
  - E₀ = `qbeta_e0.canonical()` = 4.22748335562903 MeV;
  - Q_β = 0.65185631006 MeV (the scored cell);
  - χ_(3) = 1.38249446339 / 1.1221068216 and χ_(2,1) = −0.2805933509 / −0.3719563247 (p / n);
  - reading-1 determinants (2,1) = −1.02197249381 and (1³) = −0.739223570776 / −0.910762214553.
- y_(2,1) = 0.2473 and y_(1³) = 0.
- χ_(2,1)(V³) = +1.994186.
- χ_(2,1) from an explicit seminormal 2×2 representation (braid and Hecke relations checked) equals the trace-formula value exactly on every word.
- P1: `CORE·TAIL·Vᵏ` and `V^{3+k}·TAIL` give identical diagnostics. The trace is cyclic, so the placement of the segment is not a degree of freedom.

## Step 2: elements CORE · TAIL_x · Vᵏ, k = 0..3, all reported, no ranking

| k | gluon segment | letters | (a) g_odd | (b) χ_(2,1) p | χ_(2,1) n | reading 3 (p, n) | (c) Q_β at z_D (MeV) | vs CODATA |
|---|---|---|---|---|---|---|---|---|
| 0 | (none) | 9 | **0** | −0.0919840131 | −0.1820008782 | fail, fail | 0.545664266 | −30.25 % |
| 1 | σ₀σ₁⁻¹ | 11 | **0** | **+0.2170281485** | **+0.4294149854** | **pass, pass** | 0.229517012 | −70.66 % |
| 2 | (σ₀σ₁⁻¹)² | 13 | **0** | −0.1345296130 | −0.2661822081 | fail, fail | 0.589192245 | −24.69 % |
| 3 | (σ₀σ₁⁻¹)³ | 15 | **0** | −0.0766187562 | −0.1515989622 | fail, fail | 0.529944226 | −32.26 % |
| ref | σ₀σ₀ (census, nuc11) | 11 | −h[2]_q(q²+q⁻²)/8 ≠ 0 | −0.2805933509 | −0.3719563247 | fail, fail | 0.651856310 | −16.68 % |

χ_(3) > 0 on every row (each Vᵏ has χ_(3) = 1), and y_(1³) = 0. So the (2,1)
character decides reading 3.

**Reading-3 survivors (both nucleons, proton pin): 1 of 4, k = 1**, the element
`(σ₀σ₁⁻¹)⁴ · TAIL`. It is the member the 11-crossing budget names. The k = 3
member, named by the "select it like the core" side-rule, fails.

## What the diagnostics show (consequences, not selection criteria)

- (a) **Every γγ gluon segment removes the trace-level bar obstruction exactly.**
  `g_odd = 0` identically in q for k = 0, 1, 2, 3. With f = h·g, f is bar-odd for
  each of these words. This sharpens `qou-z08b`: the obstruction comes from the
  census σ₀² specifically. A γγ-ruled gluon does not produce it.
- (b) The reading-3 verdicts depend on q. χ_(2,1) = 0 at q = 1 for every row
  (flavour is invisible at order t⁰, as in `quark_template`). The real roots of
  χ_(2,1) above 1, identical for p and n:

  | k | roots above 1 |
  |---|---|
  | 0 | 1.278895 |
  | 1 | 1.429157 (so k = 1 passes on (1, 1.4292), which contains q₀) |
  | 2 | 1.495025 |
  | 3 | 1.201352 and 1.531129 |

  - The k = 0 values and the root 1.278895 reproduce, independently, the
    `quark_template` record. That record had −0.09198 / −0.18200 and q* = 1.27890
    for the corpus template at k = 0. This was not pre-registered as a check and
    is noted as a corroboration only.
- (c) The Q_β values are reported. None was used to choose anything. The single
  reading-3 survivor sits at −70.66 %. Whether the ruled element changes is an
  owner decision (`qou-99qc`). The dashboard rows are untouched (`qou-iagg`).

## Scope

Scope (a) throughout.
- The quark tail is the census tail, held fixed. Its derivation is
  `qou-ales` option 4 and is still open.
- The verdicts are at the proton pin.
- The γγ condition is the H₃ one. The every-strand-count condition is trivial on
  three strands.
- Nothing here rules on σ₀²'s H₂-parity derivation. It records that the γγ rule
  and that rule give different gluon segments.
