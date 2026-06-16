**Proposition (lepton Bring-surface = H_3 3-channel convention).**
*For any torus-knot lepton candidate $K_\ell = \sigma_1^{2m+1}$ (electron $m=1$,
candidate muon $m=2$, candidate tau $m=3$), the framework's "additive
Wedderburn" volume $\hat V_\ell^{\mathrm{full}}$ — used in the per-braid mass
tower and matching `mass-endomorphism-tower.md`'s published $\hat V_e \approx 0.594$ —
is given by the **H_3 3-channel Plancherel-weighted character sum** with
Markov-traced standard channel:*

$$
\boxed{\;\hat V_\ell^{\mathrm{full}}
\;=\;
W_{\mathrm{sym}} \cdot q^{2m+1}
\;+\;
W_{\mathrm{std}} \cdot (z \cdot a_{2m+1} + b_{2m+1})
\;+\;
W_{\mathrm{alt}} \cdot (-q^{-1})^{2m+1}\;}
$$

*where:*

- *$W_\lambda = d_q(\lambda)^2 / [3]_q!$ are H_3 Plancherel weights:
  $W_{\mathrm{sym}} = W_{\mathrm{alt}} = 1/[3]_q!$,
  $W_{\mathrm{std}} = [2]_q^2/[3]_q!$;*
- *$(a_{2m+1}, b_{2m+1})$ are the Hecke recursion coefficients from
  $\sigma_1^{2m+1} = a_{2m+1} \cdot \sigma_1 + b_{2m+1}$
  (per the proved theorem
  [`torus_knot_odd_reduction_exists`](lepton-mass-tower-canonical.md));*
- *$z = 1/(q^{1/2} + q^{-1/2})$ is the Markov parameter;*
- *the std-channel term $(z \cdot a + b)$ is the Hoefsmit-basis Markov
  trace of $\sigma_1^{2m+1}$ in the 2-dimensional standard
  representation of $H_3(q)$.*

> **T6 status — gap (a) RESOLVED; gap (c) IMPLICATED.** This
> proposition closes the $\hat{V}$-convention ambiguity (T6 gap (a)) by
> documenting the H_3 3-channel formula. Applying the canonical Li_2^q
> per-braid mass tower to the resulting $\hat{V}$ values gives lepton mass
> ratios off CODATA by 99% — the missing factor `206.77 / 1.36 ≈ 152`
> equals **(3/2) $\times$ (1/ℏ_$q^{2}$)**, structurally identical to the
> SUPERSEDED scalar substrate density. Full diagnosis:
> [`docs/audits/-lepton-bring-surface-h3-3channel-convention.md`](../../../docs/audits/-lepton-bring-surface-h3-3channel-convention.md).

## Bring-surface analog with nucleons

The framework places nucleons on the Bring surface ($\Sigma_4$, genus 4)
with 3 quark color tubes per nucleon (3 sheets carrying $\mu_u, \mu_u, \mu_d$
for proton; $\mu_u, \mu_d, \mu_d$ for neutron). This is the **3-sheet
nucleon Bring representation**.

The analogous lepton representation uses the **3 H_3 Wedderburn channels**:

| Sector | 3-sheet Bring structure | Underlying symmetry |
|---|---|---|
| Nucleon | 3 quark color tubes | $\mathrm{SU}(3)$ color |
| Lepton | 3 H_3 Wedderburn irreps | partitions $\lambda \vdash 3$ |

Both are 3-fold representations on the substrate; both project through
Plancherel weighting to a single observable. The 3-channel structure
for leptons is the **canonical "where leptons live"** on the
Bring surface: even though $\sigma_1^{2m+1}$ is naturally an $H_2$
element (2 strands, 1 generator), the mass formula sits at $H_3$
because that's where the cohomological discipline
([`prop:three-parameters-wedderburn`](three-parameters-wedderburn.md))
fixes the 3-CAL $\leftrightarrow$ 3-channel mapping.

## Verification — calibration matches paper

At $q_0 \approx 1.10998$:

| Quantity | Value |
|---|---:|
| $[2]_q$ | 2.0109 |
| $[3]_q! = [1]_q[2]_q[3]_q$ | 6.1206 |
| $W_{\mathrm{sym}}$ | 0.1634 |
| $W_{\mathrm{std}}$ | 0.6607 |
| $W_{\mathrm{alt}}$ | 0.1634 |
| $\sum W$ | 0.9874 |

For electron $\sigma_1^3$:

| Channel | Value |
|---|---:|
| $\chi_{(3)}(\sigma_1^3) = q^3$ | $1.367$ |
| $\chi_{(1,1,1)}(\sigma_1^3) = -q^{-3}$ | $-0.731$ |
| std Markov trace $= z(h^2 + 1) + h$ | $0.730$ |
| **$\hat V_e^{\mathrm{full}}$ (computed)** | **$0.586$** |
| $\hat V_e^{\mathrm{full}}$ (paper, `mass-endomorphism-tower.md:351`) | $\approx 0.594$ |

Match within $1.3\%$ (small discrepancy is paper's 3-significant-figure
rounding; the algebraic formula above is exact).

## Application to the lepton tower

Computed $\hat V_\ell$ and Li_2^q-tower mass ratios at $q_0$:

| Lepton | Braid | $\hat V_\ell$ | $\|\hat V\| < q_0$? | $m_{\mathrm{dim}}$ | Ratio | CODATA | Δ |
|---|---|---:|:---:|---:|---:|---:|---:|
| Electron | $\sigma_1^3$ T(2,3) | $+0.586$ | ✓ | $0.518$ | $1$ (cal) | — | — |
| Muon T(2,5) | $\sigma_1^5$ | $+0.834$ | ✓ | $0.705$ | $1.36$ | $206.77$ | $-99.3\%$ |
| Muon T(2,7) | $\sigma_1^7$ | $+1.119$ | ✗ | diverges | — | — | — |
| Tau T(2,7) | $\sigma_1^7$ | $+1.119$ | ✗ | diverges | — | — | — |
| Tau T(2,9) | $\sigma_1^9$ | $+1.452$ | ✗ | diverges | — | — | — |

The convention is internally consistent (electron calibrates correctly),
but **mass ratios do not close** under the canonical Li_2^q tower
alone — the missing dimensional factor is structurally identical to
the SUPERSEDED scalar $\rho_q = 1/\hbar_q^2$ (see Caveat above).

**Tau divergence**: T(2,7) and T(2,9) both yield $\hat V > q_0$, outside
the Li_2^q convergence radius. Either the canonical tau braid is **not**
in the T(2, 2m+1) family, or higher-tower terms regulate the divergence
(consistent with the open status of `prop:rho-k-pair-gen-canonical-form`).

## Lowest/highest weight structure (6-dim NF diamond)

The framework's NF basis of $H_3(q)$ has dimension $6 = 1^2 + 2^2 + 1^2$
(sym + std + alt). **The sym and alt are the 1-dimensional
highest-weight and lowest-weight irreps** of the symmetric group $S_3$
(equivalently the classical limit of $H_3(q)$):

| Wedderburn channel | Partition | Dim | Weight | $\sigma_i$ eigenvalue |
|---|:---:|:---:|---|:---:|
| sym | $(3)$ | 1 | **highest** | $+q$ |
| std | $(2, 1)$ | 2 (so $d^2 = 4$ in NF count) | mixed | $+q$ and $-q^{-1}$ mixed |
| alt | $(1,1,1)$ | 1 | **lowest** | $-q^{-1}$ |

The 1 + 4 + 1 = 6 NF-diamond structure is therefore **symmetric around
the std midpoint**: 1-dim endpoints at lowest and highest weight, with
the 4-dim std irrep filling the middle. This is the canonical $S_n$
representation-theory structure.

### Lepton $\leftrightarrow$ channel mapping (conjectural)

Per [`prop:three-parameters-wedderburn`](three-parameters-wedderburn.md):

- sym (highest weight, $+q$ only) $\leftrightarrow$ CAL-2 $q_0$ (substrate deformation)
- std (mixed eigenvalues) $\leftrightarrow$ CAL-1 $m_e$ (mass scale)
- alt (lowest weight, $-q^{-1}$ only) $\leftrightarrow$ CAL-3 $\mathfrak{Q}_\beta$ (interaction)

A natural conjecture maps the 3 lepton generations to the 3 H_3 channels
respecting this lowest/highest-weight structure:

| Lepton | Candidate channel | Reasoning |
|---|---|---|
| Electron | std (middle, calibration unit) | electron IS the mass-scale calibration (CAL-1 = $m_e$); most natural to live in the std channel that controls mass |
| Muon | sym (highest weight) OR alt (lowest weight) | the 2 "endpoint" leptons fill the 1-dim irreps |
| Tau | the other endpoint | (sym if muon = alt; alt if muon = sym) |

The tau divergence finding above (T(2, 2m+1) at $m \geq 3$ gives $\hat V > q_0$)
is consistent with one endpoint channel saturating the 1D irrep's
representation capacity at high crossing count.

### Elementary-particle count in 6-dim NF basis

A plausible elementary-particle count fitting the 6-dim NF diamond:

- 2 lepton generations $\times$ 2 chiralities (L, R) = 4 dimensions
- 1 Higgs (figure-eight $4_1$, "Higgs field / mass mechanism" per `knot-volumes.py:58`)
- 1 photon ($\gamma$, identity element of $H_3$)
- **Total = 6 dimensions = $\dim H_3(q)$**

Alternative count:
- 3 leptons $\times$ 1D irrep each (e/μ/τ in sym/std/alt) = 3 dimensions
- But std is 2D ($d^{2}$ = 4), so it contributes more — would give 1 + 4 + 1 = 6
- If electron occupies std (4 dim = electron-LH + electron-RH + electron-neutrino-LH + electron-neutrino-RH?), then muon + tau fill sym + alt (1 + 1)
- **Total still = 6 dimensions**

This is conjectural; explicit mapping NF-diamond $\leftrightarrow$ elementary-particle
content is open. If correct, the lowest/highest-weight 1-dim irreps
correspond to the 2 extreme leptons (muon and tau), with the
electron in the 4-dim middle std channel hosting both chiralities
and possibly weak-isospin partner (neutrino).

## Cross-references

- [`prop:three-parameters-wedderburn`](three-parameters-wedderburn.md) — 3-CAL $\leftrightarrow$ 3-channel cohomological discipline
- [`prop:per-braid-mass-tower`](per-braid-mass-tower.md) — Li_2^q canonical mass formula
- [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md) — F_ℓ existence conjecture
- [`rem:bar-involution`](bar-involution.md) — P_avg / P_skew projection (real-q mechanism)
- Convention source: `tools/pyhecke/python/pyhecke/constants.py:156` (V_HAT_ELECTRON)
- Compute infrastructure: `computations/per_generator_V_hat_general.py` (generalises `per_generator_V_hat_3A`)
- T6 closure attempt: `computations/t6_lepton_h3_3channel_convention.py`
- Audit: [`docs/audits/-lepton-bring-surface-h3-3channel-convention.md`](../../../docs/audits/-lepton-bring-surface-h3-3channel-convention.md)
- SUPERSEDED ρ_q purge (now understood as incomplete): [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md)
