> **DEPRECATED on 2026-05-24.** Workplan executed / point-in-time status snapshot / PR-specific note that has been superseded by subsequent integration into main. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T1 for the deprecation rationale.

# 4-parallel followup tests — synthesis

**Compiled** 2026-05-02 on `claude/4-parallel-followup-tests`.
**Off** PR #511 (`8522e3aae` + `14be9a9e8`).

User picked option 6 (all four 1-4 in parallel). Results:

## Item 1 — GT-MATRIX PSLQ probe

**Driver**: [`gt_matrix_pslq_probe.py`](../../computations/probes/gt_matrix_pslq_probe.py)
**Witness**: [`gt-matrix-pslq-probe.witness.json`](../../computations/probes/gt-matrix-pslq-probe.witness.json)

**Finding**: Leading order $g_A \approx [5]_q/[4]_q = 1.27027852$ vs PDG $1.27510(13)$ — residual $\delta_{\rm GT} = 0.003796$. Best small-rational ansatz for $\delta_{\rm GT}$:

| Form | $a$-value at $q_0$ | rational close? |
|------|------:|---|
| $a \cdot \hbar_q^2 \cdot [5]_q$ | 0.0741 | $\approx 2/27$ (off ~$10^{-5}$) |
| $a \cdot \hbar_q$ | 0.03831 | $\approx 1/26$ (off similarly) |
| $a \cdot \hbar_q^4 \cdot [5]_q$ ($= \delta_{CS}$) | 7.544 | not small-rational |
| $a \cdot \hbar_q^4 \cdot [3]_q$ | 12.94 | not small-rational |

**Honest verdict**: PDG $g_A$ has only ~$10^{-4}$ relative precision, so PSLQ at any $\text{tol} \leq 10^{-4}$ returns spurious noise relations. **Cannot distinguish a clean closed form from CODATA noise** at current measurement precision. The $g_A = [5]_q/[4]_q \cdot (1 + \frac{2}{27}\hbar_q^2[5]_q)$ candidate is **suggestive but not confirmable** until $g_A$ is measured to $\geq 10^{-5}$ precision.

**Status**: 🟡 framework-suggestive; closure blocked on experimental precision.

## Item 2 — NV-1 PSLQ extended basis

**Driver**: [`nv_pslq_extended_basis.py`](../../computations/nv_pslq_extended_basis.py)
**Witness**: [`nv-pslq-extended-basis.witness.json`](../../computations/nv-pslq-extended-basis.witness.json)

**Finding**: Re-ran PSLQ on extended basis $\{q^k, [k]_q, \hbar_q^k, [4]_q^2/[2]_q, [6]_q^2/[2]_q, [8]_q^2/[2]_q, [4]_q[6]_q[8]_q/[2]_q^3, \text{small primes}\}$ at four tolerances. Result:

- 0 genuine $\log(N_v)$ relations at any $\text{tol} \leq 10^{-7}$
- 1 basis-internal coincidence (no $\log(N_v)$ coefficient)

**Verdict**: "Extended basis does NOT close NV-1: no $\log(N_v)$ relation at any tested tolerance. Consistent with the conjectured form **iff** $\mathcal{N}_{\rm sym}(q)$ is transcendental in the basis — $\mathcal{N}_{\rm sym}$ must be authored explicitly before PSLQ can verify."

**Status**: 🔴 NV-1 unchanged. The $\mathcal{N}_{\rm sym}(q)$ Plancherel-normalization constant introduced in `conj:weak-spectral-completeness` (PR #511) is NOT a simple q-arithmetic expression; needs separate derivation from the Higgs-mechanism categorical structure (U2/U4 conjectures from PR #511).

## Item 3 — v4 mass pipeline integration

**Driver**: [`v4_mass_pipeline.py`](../../computations/v4_mass_pipeline.py)
**Witness**: [`v4-mass-pipeline.witness.json`](../../computations/v4-mass-pipeline.witness.json)

**Test**: take `crt_markov_v4` depth-1 single-generator + depth-2 adjacent-pair tower terms, integrate via $\Delta M = \alpha_{\rm bind} \cdot (\text{markov}_{\rm total} - \text{markov}_{\rm desc})$ where $\alpha_{\rm bind} = 8 \cdot m_e \cdot G$ (Catalan binding scale).

**Result** (proton, ²H, ³H, ³He):

| atom | v3 MeV | v3 err | v4 MeV | v4 err | Δv4−v3 |
|------|------:|--:|------:|--:|--:|
| proton | 938.7831 | +0.054% | 938.7831 | +0.054% | 0.000 |
| ²H | 1878.3485 | +0.146% | 1878.3485 | +0.146% | 0.000 |
| ³H | 2817.9139 | +0.320% | 2817.9139 | +0.320% | 0.000 |
| ³He | 2817.1316 | +0.311% | 2817.1316 | +0.311% | 0.000 |

**Finding**: $(\text{markov}_{\rm total}^{(A)} - \text{markov}_{\rm desc})$ evaluates to **exactly zero** in v4's `total_mass_h3a` output for these atoms — meaning v4's "tower-A" form produces no MeV correction in this integration. The §3·A claimed "missing 99% of mass" is **not exposed** by the naïve `total - desc` integration; either:
- The tower-A normalization equals the descended value categorically (in which case v4's diagnostic and v3's prediction are the same observable, and §3·A's "99% missing" is overstated), or
- The integration scale should be the **literal product** $\Phi_q(|V|)$ values (the "B" variant) not the cyclicity-restricted "A" variant — needs categorical derivation of which is correct.

**Status**: 🟡 §3·A integration deferred — needs categorical derivation of the right tower-term-to-MeV scale. The infrastructure (v4) exists; the right calibration constant is open.

## Item 4 — SHELL-7 BB-stratum test

**Driver**: [`shell7_bb_stratum_test.py`](../../computations/shell7_bb_stratum_test.py)
**Witness**: [`shell7-bb-stratum.witness.json`](../../computations/shell7-bb-stratum.witness.json)

**Test**: $f_{\rm magic}(Z, N) \stackrel{?}{=} \sum_{\lambda \vdash 3A,\, \lambda = \lambda'} w_\lambda \cdot \chi_\lambda(\beta_{Z,N})$ at A ∈ {4, 6, 8, 12, 28}.

**Result**: **FALSIFIED**. Pearson r = $-0.057$ between predicted and AME shell-correction values. Predictions diverge by 73 orders of magnitude across A=4..28; AME shell magnitudes vary by < 30 MeV. Specific findings:

- Wrong magnitude (440× off at A=4)
- No magic peaking (8Be should be a negative anomaly; predicted as larger than 4He)
- Wrong scaling ($\hat f \cdot A^{2/3}$ explodes geometrically with A)

**Where the hypothesis breaks**:
1. **SC filter too narrow**: should use full $\kappa = 0$ stratum (transpose-pair-summed), not just self-conjugate
2. **Plancherel weight wrong sign**: $\dim_q^2 / [n]_q!$ at $q_0 > 1$ blows up; magic suppression requires a different normalization (likely the resolvent / q-Laplacian damping in `_partition_table.C_lambda_resolvent_MeV`)
3. **Missing (Z, N) dependence**: P1 proxy sees only A; needs the full character $\chi_\lambda(\beta_{Z,N})$ infrastructure beyond k=11 (currently capped)

**Status**: 🔴 hypothesis falsified; the conjecture in `2026-05-02-shell7-scale-and-gt-matrix-research.md` needs reformulation along the three lines above.

## Net summary

| Item | Result | Audit-flag impact |
|------|--------|-------------------|
| GT-MATRIX | 🟡 framework-suggestive (g_A = [5]_q/[4]_q · (1+δ); δ ≈ 2/27·ℏ_q²·[5]_q at $10^{-5}$ — within CODATA noise) | unchanged: closure blocked on experimental precision |
| NV-1 extended PSLQ | 🔴 inconclusive | unchanged: $\mathcal{N}_{\rm sym}$ needs categorical derivation |
| v4 mass pipeline | 🟡 deferred | §3·A integration: right calibration scale open |
| SHELL-7 BB-stratum | 🔴 falsified | needs reformulation (full κ=0 stratum, different weight, (Z,N) dependence) |

**One concrete deliverable that did emerge**: the $g_A = [5]_q/[4]_q \cdot (1 + \frac{2}{27}\hbar_q^2 \cdot [5]_q)$ ansatz — a clean candidate for a future categorical derivation paralleling $1/\alpha_{\rm EM}$, blocked only on better $g_A$ measurement.

**Next prioritised step (single-target)**: author $\mathcal{N}_{\rm sym}(q)$ — the symmetric-channel Plancherel normalization for the EW sector — as a content block. This single artifact would unlock NV-1 PSLQ verification AND provide the missing scale for v4 integration AND inform the SHELL-7 reweighting. Deriving $\mathcal{N}_{\rm sym}$ from the categorical Higgs mechanism (U2/U4 from PR #511) is research-grade but well-scoped.
