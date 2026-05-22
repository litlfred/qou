**Proposition.**
*The atomic mass $\mathcal{M}(Z, N)$ is recovered from the
[unified six-term decomposition](#thm:six-term-mass-formula-complete)
by **per-term physical weights** read off the individual derivations,
without proton-fitting:*

$$
  \mathcal{M}(Z, N)
  \;=\;
  Z\, m_{\mathfrak{p}} + N\, m_{\mathfrak{n}} + Z\, m_e
  \;-\;
  B(Z, N)
$$

*where the binding energy is the term-by-term differential
between bound (`include_inter=True`) and free (`include_inter=False`)
configurations:*

$$
  B(Z, N)
  \;=\;
  \underbrace{E_{0,\beta} \cdot \big(T_1^{\rm free} - T_1^{\rm atom}\big)}_{\text{T1 binding}}
  \;+\;
  \underbrace{\alpha \cdot \big((T_2 + T_3)^{\rm atom} - (T_2 + T_3)^{\rm free}\big)}_{\text{T2/T3 binding}}
  \;+\;
  \underbrace{m_e \cdot \big(T_4^{\rm atom} - T_4^{\rm free}\big)}_{\text{T4 binding}}
  \;+\;
  \underbrace{E_{0,\beta} \cdot (a_K - 1) \cdot T_1^{\rm atom}}_{\text{T5 binding}}
  \;+\;
  \underbrace{\big(T_6^{\rm atom} - T_6^{\rm free}\big)}_{\text{T6 binding (MeV)}}
$$

**Per-term weights and their derivations.**

| term | weight | source |
|------|--------|--------|
| $T_1 = \lvert\mathrm{tr}_M(T_w)\rvert$ | $E_{0,\beta} \approx 0.7823$ MeV | [categorical mass, Markov](#prop:categorical-mass-markov); free-neutron β-decay $Q$ |
| $T_2 = \sum_i \Phi(\lvert\hat V_i\rvert)$ | $\alpha = m_e \cdot 8G \approx 3.7445$ MeV | [binding scale Catalan](#prop:binding-scale-catalan); $\Phi = -\mathrm{Li}_2^q(-\,\cdot\,)$ per [Kashaev limit](#prop:mass-endomorphism-tower) |
| $T_3 = z^2 \sum_{i<j} \Phi(\lvert\hat V_i \hat V_j\rvert)$ | $\alpha$ (same scale) | [Markov trace factorisation](#thm:markov-trace-factorization) |
| $T_4 = \tau(C_{\dim_q})$ | $m_e \approx 0.5110$ MeV | [Frobenius universal](#thm:frobenius-codim-universal) |
| $T_5 = (a_K - 1) \cdot T_1$ | $E_{0,\beta}$ (multiplicative on $T_1$) | [chirality dual-space](#prop:chirality-dual-space-derivation) |
| $T_6 = \sum_{\ell \geq 2} \mathrm{Res}_{\zeta_\ell}/(q_0 - \zeta_\ell)$ | $1$ (already MeV) | [full pole structure](#prop:full-pole-structure-mass-trace) |

*Critically the ratio
$\alpha / E_{0,\beta} = 4.79$ is non-trivial: the brane-tower
contribution $T_2 + T_3$ is on the Borromean–Catalan scale
$m_e \cdot 8G$, while the descended Markov trace $T_1$ is on the
β-decay $Q$ scale.  Earlier proton-fitted assemblies collapsed
the two into a single calibration, balancing at $A = 1$ but
propagating mass error rapidly with $A$.*

*Proof.*
The constituent baseline
$Z\,m_{\mathfrak{p}} + N\,m_{\mathfrak{n}} + Z\,m_e$ is the
free-particle sum from CODATA.  The binding energy is the
algebraic difference of the bound atom's mass formula and its
free baseline.  Each of the six terms contributes additively to
the categorical mass per
[unified six-term decomposition](#thm:six-term-mass-formula-complete);
isolating the **physical scale** of each contribution is exactly
the per-derivation reading above:

- *$T_1$ binding (descended Markov):* the categorical mass
  formula
  $\mathcal{M}(Z, N) = E_{0,\beta} \cdot \mathfrak{m}(\beta_{Z,N})$
  with $E_{0,\beta} = 0.7823$ MeV the free-neutron β-decay $Q$
  per [categorical mass, Markov](#prop:categorical-mass-markov)
  reads $T_1$ in cat units.  The binding contribution is the
  bound–free differential.
- *$T_2 + T_3$ binding (brane tower):* per
  the *atomic-braid mass formula* in the particle-interactions chapter, the binding
  correction is $\alpha \cdot \sum_i \ln\lvert \hat V_i \rvert$
  where $\alpha = m_e \cdot 8G$ is the
  [Borromean–Catalan binding scale](#prop:binding-scale-catalan)
  and $G \approx 0.9160$ is Catalan's constant.  Per
  [the divergence-audit branch's reconciliation](#prop:mass-endomorphism-tower),
  $\alpha\,\ln\lvert V \rvert$ is the leading-order expansion of
  $-\alpha\,\mathrm{Li}_2^q(-\lvert V \rvert)$, so the same $\alpha$
  scale governs both the leading-order and the corrected
  q-dilogarithm form.
- *$T_4$ binding (Frobenius co-Casimir):* the universal
  [Frobenius co-Casimir](#thm:frobenius-codim-universal)
  $T_4 = m_e \cdot \tau(C_{\dim_q})$ has $m_e$ baked into the
  formula.  Empirically the bound–free differential vanishes for
  the atomic-braid $\tau$, so $T_4$ contributes no binding at
  this stage (open question — see remarks).
- *$T_5$ binding (chirality):* per
  [chirality dual-space derivation](#prop:chirality-dual-space-derivation),
  $T_5 = (a_K - 1) \cdot T_1$ as a multiplicative correction on
  $T_1$.  With $T_1$ in cat units and $E_{0,\beta}$ as $T_1$'s MeV
  scale, the binding contribution is
  $E_{0,\beta} \cdot (a_K - 1) \cdot T_1^{\rm atom}$.
- *$T_6$ binding (cyclotomic tail):* per
  [full pole structure](#prop:full-pole-structure-mass-trace),
  $T_6$ comes pre-converted to MeV via the canonical Habiro
  residue evaluation.  No additional scaling needed.

The total $B(Z, N)$ is the sum of these per-term contributions
and is positive for bound systems.  $\square$

**Empirical verification.**

The assembly is implemented in
`folio-assistant/computations/paper_six_term_isotope_sweep.py`
as `assemble_per_derivation_weights(Z, N)` with hardcoded
constants $E_{0,\beta} = 0.78233341$ MeV (CODATA β-decay $Q$),
$\alpha = m_e \cdot 8G = 3.74446989$ MeV, $m_e = 0.51099895$ MeV.
Across the proton..${}^{9}$Be spectrum (12 atoms):

| atom | $A$ | $\mathcal{M}_{\mathrm{AME}}$ (MeV) | $\mathcal{M}_{\mathrm{pred}}$ | err % |
|------|-----|------:|------:|------:|
| p    |  1  |  938.7831 |  938.7831 |  0.000 |
| n    |  1  |  939.5654 |  939.5654 |  0.000 |
| D    |  2  | 1876.1239 | 1876.0406 | -0.004 |
| T    |  3  | 2809.4322 | 2813.7535 | +0.154 |
| ${}^{3}$He  |  3  | 2809.4135 | 2811.1360 | +0.061 |
| ${}^{4}$He  |  4  | 3728.4013 | 3747.9809 | +0.525 |
| ${}^{5}$Li  |  5  | 4669.1510 | 4680.8490 | +0.250 |
| ${}^{6}$Li  |  6  | 5603.0520 | 5616.2553 | +0.236 |
| ${}^{7}$Li  |  7  | 6535.3660 | 6551.0997 | +0.241 |
| ${}^{7}$Be  |  7  | 6536.2270 | 6546.8392 | +0.162 |
| ${}^{8}$Be  |  8  | 7456.8940 | 7480.7621 | +0.320 |
| ${}^{9}$Be  |  9  | 8392.7490 | 8414.1242 | +0.255 |

**Mean $\lvert\delta\mathcal{M}/\mathcal{M}\rvert = 0.184\%$,
max $= 0.525\%$ (${}^{4}$He).**

This matches the standalone
the *atomic-braid mass formula* in the particle-interactions chapter formula's empirical
fit (0.13–0.16% mean across the same spectrum) and **76$\times$ improves**
on the proton-fitted single-$E_0$ assembly (14.7% mean) — the
improvement is entirely from honouring the per-term derivation
weights.

**Open questions.**

1. *$T_4$ binding contribution vanishes empirically.* The
   `term4_frobenius_codim` evaluation gives the same value for
   bound and free configurations, so the differential
   $T_4^{\rm atom} - T_4^{\rm free} = 0$ identically.  Either
   $T_4$ is independent of inter-nucleon crossings by
   construction (in which case it cancels out of the binding
   formula and contributes only to the total mass via the
   $Z\,m_{\mathfrak{p}}$ baseline), or the implementation is
   missing a coupling.  Investigation pending.
2. *$T_6$ Habiro residue witness coverage.* The
   `_load_canonical_t6_MeV` helper currently returns 0 for
   $A \geq 5$ atoms because the Habiro residue witness lacks
   data for them.  Once populated, $T_6$ will start
   contributing to the heavier-atom predictions; expect
   ${\sim}\,$few-keV-level corrections per atom based on the
   $A \leq 4$ pattern.
3. *${}^{4}$He outlier (0.525 %).* Largest residual in the spectrum.
   Worth a focused look — possibly a missing $T_4$ contribution
   that would manifest only at the doubly-magic ${}^{4}$He
   configuration.
