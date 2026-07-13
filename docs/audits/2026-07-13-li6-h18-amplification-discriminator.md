# The ⁶Li H₁₈ amplification discriminator — the geometric 𝒜(A) law BREAKS (R3-b)

**Date:** 2026-07-13 · **Branch:** `claude/mass-binding-errors-9zqpal` ·
**Type:** out-of-sample DISCRIMINATION test of the guarded geometric
amplification law from the θ_λ magnitude audit
([`2026-07-13-theta-lambda-magnitude-derive-or-refute.md`](2026-07-13-theta-lambda-magnitude-derive-or-refute.md) §6/§8).
**No fit, no tuning, no wiring.**
**Probe:** [`computations/deltalambda/li6_h18_amplification_discriminator_probe.py`](../../computations/deltalambda/li6_h18_amplification_discriminator_probe.py)
(witness `li6-h18-amplification-discriminator.witness.json`, 8/8 assertions).

## 1. The registered test

The θ_λ magnitude audit measured the required amplification

$$
\mathcal{A}(K) = \frac{B_{\mathrm{AME}}(K)}{m_e \cdot \sum_\lambda w_\lambda\,|\Delta\theta_\lambda|}, \qquad w_\lambda = y_\lambda \cdot \dim_\lambda
$$

on {D, T, ³He, ⁴He} and found per-added-nucleon ratios
3.143 / 3.295 / 3.320 / 3.167 (~6 % scatter) — the guarded geometric law
`𝒜(A) ≈ 6.0·3.2^{A−2}`, with the composite guarded form
`[3]_q!·(e^{Vol(𝓑₃)/2π})^{A−2}` reproducing all four absolute bindings to
≤ 3.5 %. The audit registered the falsifier **before this run**:
**𝒜(⁶Li) ≈ 650 predicted at A = 6** (649.78 exactly under the composite;
596–650 across the four degenerate ratio candidates). Honest tolerance:
the 4-point per-step scatter compounded over the A=2→6 extrapolation
(1.06⁴ ≈ 1.27, quoted as ±30–40 %); the anchor-scatter band
`𝒜(D)·r⁴, r ∈ [3.143, 3.320]` gives **[589, 734]**.

## 2. Data provenance (corpus-grep first — the 23-min compute was already cached)

| input | source | wall |
|---|---|---|
| ⁶Li atom χ_λ + y_λ (H₁₈, all 385 blocks, 50 dps) | **cached** `chi-lithium-6-h18-at-q0-50dps-matrix-m.witness.json` (producer `rust-chi-q-via-gp-lossless`, sign-only) | 1382 s on its producing branch; **reused, not recomputed** |
| ⁶Li free χ_λ (H₁₈) | computed here: `chi_free_via_lr.chi_free_lr(3,3)` (nucleon-cache + active-set LR parabolic character formula) | **3.9 s** |
| ⁵Li atom χ_λ + y_λ (H₁₅, 176 blocks) — secondary point | **cached** `chi-lithium-5-h15-at-q0-50dps-matrix-m.witness.json` | 67 s original; reused |
| ⁵Li free χ_λ | `chi_free_lr(3,2)` | 0.5 s |
| D/T/³He/⁴He anchors | same cached inputs as the audit (`binding-reeb-phase-decomposition` θ vectors + `chi-*-h*-at-q0-50dps` y_λ) | — |

Total probe wall **4.3 s** (teed log `/tmp/li6_h18.log`; the >5-min
long-compute case never arose because the H₁₈ atom characters were cached).
Machine checks: anchors reproduce the audit exactly (𝒜(D) = 6.0427,
𝒜(⁴He) = 63.051); Σ y·χ_atom reproduces each cached witness's own tr_M to
≤ 9e-51; the LR free path matches the ⁴He MPFR free witness to ≤ 6.4e-6
(the documented sign-only-vs-averaged convention gap, same magnitude as the
≤ 4.4e-6 atom-side gap — perturbs 𝒜 by ≪ 0.01 %, irrelevant at the
order-unity resolution of this test). θ convention identical to
`binding_reeb_phase_decomposition.py` (arccos rotation / arccosh growth,
|Δθ| summed over all blocks, flips included).

## 3. Result — the geometric law BREAKS at A = 5 and A = 6

| observable | A | m_e·S (y·dim) MeV | **measured 𝒜 (y·dim)** | composite pred | rel |
|---|--:|--:|--:|--:|--:|
| D | 2 | 0.36 | 6.04 | 6.12 | +1.3 % |
| T | 3 | 0.22 | 18.99 | 19.65 | +3.4 % |
| ³He | 3 | 0.19 | 19.91 | 19.65 | −1.3 % |
| ⁴He | 4 | 0.449 | 63.05 | 63.06 | +0.02 % |
| **⁵Li** | 5 | 0.408 | **64.56** | 202.4 | **−68.1 %** |
| **⁶Li** | 6 | 0.401 | **79.86** | 649.8 | **−87.7 %** |

> **ERRATUM (2026-07-13, R4-b).** The m_e·S entries for T (0.22) and ³He
> (0.19) above are wrong — inconsistent with this table's own 𝒜 column
> (B_AME/𝒜 = **0.4466** and **0.3877** MeV respectively; recomputed per-λ
> and machine-checked in
> [`2026-07-13-carrier-saturation-crossover-mechanism.md`](2026-07-13-carrier-saturation-crossover-mechanism.md)
> §2, assertion `erratum_T_me_S_matches_A_column`). The 𝒜 column and the
> BREAKS verdict are unaffected. Corrected reading: the carrier is FLAT
> across **all** A = 2..6 (m_e·S ∈ [0.368, 0.449] MeV, max/min 1.22) — it
> never grew geometrically; see the §5 item 2 correction below.

- **𝒜(⁶Li) = 79.86**, vs the predicted ≈ 650: outside the anchor-scatter
  band [589, 734] by a factor **8.1×**, and far outside the generous
  ±40 % outer gate. Not a tolerance question.
- The implied per-nucleon step ratios collapse:
  **3.14 / 3.29 / 3.32 / 3.17 (A ≤ 4) → 1.024 (⁴He→⁵Li) → 1.237 (⁵Li→⁶Li)**.
- Alternate weighting w = y (robustness): 𝒜(⁶Li) = 5.07×10⁵ vs
  𝒜(⁴He) = 2.20×10⁴ — ratio ≈ 4.8/nucleon, also inconsistent with its own
  anchor steps (the y-weighting was never geometric among the anchors
  either; reported for completeness).
- Composite absolute check at A=6: B_pred = 260.3 MeV vs 32.0 (+714 %).

**Verdict: BREAKS — the geometric-in-A amplification is a 4-point artifact
(an A ≤ 4 regime at best), not an extensivity law.**

## 4. Scope-(a) classification (per the AGENTS refutation discipline)

**Scope-limited negative:** the scalar A-law `𝒜(A) ≈ 6.0·3.2^{A−2}` —
and with it the composite guarded form `[3]_q!·(e^{Vol(𝓑₃)/2π})^{A−2}` —
*as a global amplification law for the linear |Δθ| carrier under
w = y·dim*, does not extend past A = 4. This constrains magnitudes and
combinations, **not ingredients**: [3]_q!, e^{Vol(𝓑₃)/2π}, π, μ₀/m_e may
still appear inside an A- or λ-structured closure; the A ≤ 4 agreement
(≤ 3.5 % on four absolute bindings) remains a numerical fact any future
closure may still have to explain *in that regime*. No proved invariant
forbids the ingredients — no scope-(b) claim is made.

## 5. What each side of the discriminator now implies

1. **The ×3.2/nucleon identification hunt is NOT motivated** (the
   "survives" branch is dead): discriminating π vs [3]_q vs μ₀/m_e vs
   e^{Vol(𝓑₃)/2π} at A = 6 is moot because *none* of them is within a
   factor 7 of the measured point (measured/pred = 0.12–0.15 for all
   four). The degenerate-candidate table closes as a package.
2. **The new structural datum is SATURATION, not geometric growth:** the
   carrier m_e·Σ y·dim·|Δθ| plateaus at ≈ 0.40–0.45 MeV across
   A = 4, 5, 6 (0.449 → 0.408 → 0.401 MeV) while B_AME moves
   28.30 → 26.33 → 31.99 MeV. Beyond A = 4 the required 𝒜 is just
   B/(m_e·S) with a *flat* denominator — each 𝒜 step (1.024, 1.237)
   is the B step (0.930, 1.215) divided by the S step (0.909, 0.982) —
   i.e. the per-λ |Δθ| carrier stops carrying additional binding
   information at H₁₅⁺ under this weighting.
   Any future θ_λ closure must explain a *cross-over at A ≈ 4*, not a
   geometric ramp — a strictly harder target than the ratio hunt.
   > **RESOLVED 2026-07-13 (same day, R4-b): there is no carrier
   > crossover.** With the §3 erratum corrected (m_e·S(T) = 0.4466,
   > m_e·S(³He) = 0.3877), the carrier is flat at 0.37–0.45 MeV for
   > **all** A = 2..6 — it never "grew geometrically to A = 4". The
   > structural reason is the Markov-trace normalization
   > `Σ y_λ·dim_λ = tr_M(1) = 1` (`prop:wedderburn-trace-identity`):
   > S = E_p[|Δθ|] is an intensive bounded mean. The geometric ramp and
   > its A ≈ 4 collapse live entirely in the numerator B_AME (the
   > experimental α-peak; corpus-side account: the SU(4) [1ⁿ]
   > truncation). See
   > [`2026-07-13-carrier-saturation-crossover-mechanism.md`](2026-07-13-carrier-saturation-crossover-mechanism.md).
3. **The jet-filtration q-difference-kernel route** (prior audit §8
   item 2) loses its cheap motivation in this specific form: a constant
   per-nucleon factor R(q₀) ≈ 3.2 is exactly what the A = 5, 6 points
   exclude. A kernel whose per-step factor *decays toward 1 with A*
   (e.g. x-dependence in R(q,x) actually mattering) is what the data
   now shape — but proposing one from these 6 points would be shape
   probing; the honest route remains a *derived* R(q,x).
4. **The prior audit's §6 guarded datum + §8 item 1 are RESOLVED**
   (falsified as stated); its §7 table row "geometric-in-A constraint …
   derived PARTIAL — a rigidity constraint on any closure" must now be
   read as **A ≤ 4 only**. The scalar-𝒜 refutation (its §4) is
   *unaffected* — dispersion only grew (6.04 → 79.9 across A = 2..6).
5. **⁵Li caveat:** ⁵Li is particle-unbound (p + ⁴He); its AME total
   binding is nevertheless a well-defined measured numerator, and the
   break is independently established by ⁶Li alone (−87.7 %), which is
   particle-stable. The caveat cannot rescue the law.

## 6. Anti-fit / guard notes

- B_AME(⁵Li, ⁶Li) enter **only** as numerators of the measured
  diagnostic quotients 𝒜 — never as inputs to a wired formula. Nothing
  in this probe is a derivation; nothing is wired to production.
- One pre-registered prediction was tested (𝒜(⁶Li) ≈ 650, tolerance
  stated before the run); no alternative shapes were tried after seeing
  the number (no shape-probing). The ⁵Li secondary point uses the same
  pre-registered composite form at A = 5.
- The composite formula stays a **guarded datum** for A ≤ 4 and is now
  additionally **falsified as an A-law** — it must not be wired at any A.

## Provenance

Probe: `li6_h18_amplification_discriminator_probe.py`
(8/8 assertions, wall 4.3 s; witness
[`li6-h18-amplification-discriminator.witness.json`](../../computations/deltalambda/li6-h18-amplification-discriminator.witness.json)).
Cached inputs: `chi-lithium-6-h18-at-q0-50dps-matrix-m.witness.json`,
`chi-lithium-5-h15-at-q0-50dps-matrix-m.witness.json`,
`binding-reeb-phase-decomposition.witness.json`,
`chi-{deuteron,tritium,helium-3,helium-4}-h{6,9,12}-at-q0-50dps.witness.json`,
`chi-{proton,neutron}-h3-at-q0-50dps.witness.json` (LR nucleon cache),
`chi-helium-4-free-h12-at-q0-50dps.witness.json` (LR regression gate).
Predecessor: [`2026-07-13-theta-lambda-magnitude-derive-or-refute.md`](2026-07-13-theta-lambda-magnitude-derive-or-refute.md).
EXPLORATORY — audit + witness only; no production wiring.
