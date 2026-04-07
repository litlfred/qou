All predictions use $\approx$ (derived from $q$, zero fitting parameters).
Experimental values from NNDC/ENSDF with stated uncertainties.
Crossing convention: $(1, -\mathrm{HA})$ throughout (unimodular, $\det T = -1$).

**Table 1 --- $q$-weighted Q-values: $2 \times 2 = 6 \times 6$ formula, MAE $\approx 4.4\%$, zero fitting.**

This is the primary method.  Each generator log-ratio is classified as
unbinding ($u$), rebinding ($r$), or spectator ($uc$), then $q$-weighted:

$$
\mathcal{Q}_q = |q \cdot \Sigma_u + q^{-1} \cdot \Sigma_r + \Sigma_{uc}| \times \kappa_q \times F_{\mathrm{shell}}(q) \times F_{I_{10}}(Z,N;q)
$$

| Nucleus | Transition | $\mathcal{Q}_{\mathrm{exp}}$ (MeV) | $\delta\mathcal{Q}_{\mathrm{exp}}$ | $\mathcal{Q}_q$ (MeV) | $\delta$ | $F$ | Note |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ${}^3\mathrm{H}$ | $\to {}^3\mathrm{He}$ | $0.01861$ | $\pm 0.00001$ | $0.01849$ | $-0.6\%$ | $1.000$ | excellent |
| ${}^{14}\mathrm{C}$ | $\to {}^{14}\mathrm{N}$ | $0.15648$ | $\pm 0.00004$ | $0.15300$ | $-2.2\%$ | $1.000$ | good |
| ${}^{60}\mathrm{Co}$ | $\to {}^{60}\mathrm{Ni}$ | $0.31817$ | $\pm 0.00013$ | $0.33856$ | $+6.4\%$ | $0.590$ | fair |
| ${}^{90}\mathrm{Sr}$ | $\to {}^{90}\mathrm{Y}$ | $0.54590$ | $\pm 0.00007$ | $0.55740$ | $+2.1\%$ | $0.590$ | good |
| ${}^{137}\mathrm{Cs}$ | $\to {}^{137}\mathrm{Ba}$ | $0.51400$ | $\pm 0.00021$ | $0.53750$ | $+4.6\%$ | $0.377$ | good |
| ${}^{210}\mathrm{Bi}$ | $\to {}^{210}\mathrm{Po}$ | $1.16270$ | $\pm 0.00006$ | $1.28191$ | $+10.3\%$ | $0.590$ | fair |

**MAE $\approx 4.4\%$, RMS $\approx 5.4\%$, max $|\delta| \approx 10.3\%$.**

All six benchmarks are within $11\%$ with zero fitting parameters.
Light nuclei (${}^3\mathrm{H}$, ${}^{14}\mathrm{C}$) are within $2.2\%$ and
need no shell corrections; heavy nuclei (${}^{60}\mathrm{Co}$, ${}^{90}\mathrm{Sr}$,
${}^{137}\mathrm{Cs}$, ${}^{210}\mathrm{Bi}$) require the shell factors
$F_{\mathrm{deg2}}$ and $F_{\mathrm{Pauli}}$ from the $6 \times 6$ regular
representation of $H_3(q)$.

**Shell correction factors (derived from $q$, not fitted):**

- $F_{\mathrm{deg2}} = 0.5904$: Rosso--Jones weighted degree-2 torus knot
  suppression for shells $\geq 5$ ($N > 28$), computed as the
  quantum-dimension weighted average
  $(J_{2,9} \cdot \mathrm{tr}(T_{2,9} \cdot \Delta) + J_{3,4} \cdot \mathrm{tr}(T_{3,4} \cdot \Delta)) / ((J_{2,9}+J_{3,4}) \cdot \mathrm{tr}(\Delta))$
  from the $H_3(q)$ Markov trace of the beta-decay operator.
  The two degree-2 knots correspond to the $\mu_2$ ($T_{3,4}$, $s = 2^2$)
  and $\mu_3$ ($T_{2,9}$, $s = 3^2$) branches of the Kummer tower,
  matching the CRT decomposition
  $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$.
- $F_{\mathrm{Pauli}} = 0.6382$: alternating-irrep projection for
  magic-number shells (filled $N$), computed as
  $|\mathrm{tr}_{\mathrm{alt}}(\Delta)| / |\mathrm{tr}(\Delta)|$
  where $\mathrm{tr}_{\mathrm{alt}}$ evaluates with eigenvalue
  $\lambda = -q^{-1}$.
- Both are eigenvalue ratios of $\Delta_\beta = T_{\mathrm{mix}} - T_{nn}$
  in the $6 \times 6$ regular representation of $H_3(q)$, which decomposes as
  $1(\mathrm{sym}) \oplus 2(\mathrm{std}) \oplus 1(\mathrm{alt})$.

**Error propagation note.** The prediction uncertainty $\delta\mathcal{Q}_q$
from $\delta q_0 \approx 1.4 \times 10^{-9}$ is negligible
($\sim 10^{-9}\;\text{MeV}$).  The dominant theoretical uncertainty is
*structural* (model approximations in $F_{\mathrm{shell}}$), not
parametric.  All $\sigma$-separations are therefore
$|\mathcal{Q}_q - \mathcal{Q}_{\mathrm{exp}}| / \delta\mathcal{Q}_{\mathrm{exp}}$.

**Table 2 --- Naive methods (for diagnostic comparison).**

| Nucleus | Transition | $\mathcal{Q}_{\mathrm{exp}}$ | $\mathcal{Q}_{\mathrm{lag}}$ | $\delta_{\mathrm{lag}}$ | $\mathcal{Q}_{\mathrm{dir}}$ | $\delta_{\mathrm{dir}}$ | Parity |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ${}^3\mathrm{H}$ | $\to {}^3\mathrm{He}$ | $0.01861$ | $0.01861$ | $0.0\%$ | $0.01861$ | $0.0\%$ | $oA \to oA$ |
| ${}^{14}\mathrm{C}$ | $\to {}^{14}\mathrm{N}$ | $0.15648$ | $0.06148$ | $-60.7\%$ | $0.01296$ | $-91.7\%$ | $ee \to oo$ |
| ${}^{60}\mathrm{Co}$ | $\to {}^{60}\mathrm{Ni}$ | $0.31817$ | $0.12160$ | $-61.8\%$ | $0.04704$ | $-85.2\%$ | $oo \to ee$ |
| ${}^{90}\mathrm{Sr}$ | $\to {}^{90}\mathrm{Y}$ | $0.54590$ | $0.21399$ | $-60.8\%$ | $0.08053$ | $-85.2\%$ | $ee \to oo$ |
| ${}^{137}\mathrm{Cs}$ | $\to {}^{137}\mathrm{Ba}$ | $0.51400$ | $0.33416$ | $-35.0\%$ | $0.11701$ | $-77.2\%$ | $oA \to oA$ |
| ${}^{210}\mathrm{Bi}$ | $\to {}^{210}\mathrm{Po}$ | $1.16270$ | $0.52809$ | $-54.6\%$ | $0.16573$ | $-85.7\%$ | $oo \to ee$ |

**MAE: $\mathcal{Q}_{\mathrm{lag}} \approx 45\%$,
$\mathcal{Q}_{\mathrm{dir}} \approx 71\%$.**

Energy scales (calibrated from $\mathcal{Q}_{\mathrm{exp}}({}^3\mathrm{H}) = 0.01861\;\text{MeV}$):

- $E_{0,\mathrm{lag}} = 0.0689\;\text{MeV}$
  (cf. $\kappa = m_e/3 = 0.1703\;\text{MeV}$)
- $E_{0,\mathrm{dir}} = 0.0207\;\text{MeV}$
  (cf. $\kappa_q = \ln(q) \cdot m_e/3 = 0.01777\;\text{MeV}$)
- $E_0 = \mathcal{Q}_n / |\Delta\mathrm{net}_{\mathrm{free}}| = 4.406\;\text{MeV}$
  (free neutron calibration, reproduces $\mathcal{Q}_n \approx 0.782\;\text{MeV}$)

**Diagnostic --- why the naive methods undershoot:**

The Lagrangian observable
$\mathcal{L} = \sum_i (\hat{V}_{d,i} - \hat{V}_{p,i})/\hat{V}_{p,i}$
and the Dirac observable
$D = q^{-1}\sum_i \Delta\mathrm{tr}_i/\mathrm{tr}_i + \hbar_q \sum_i \Delta\mathrm{spr}_i/\mathrm{spr}_i$
both sum $A - 1$ generator contributions equally.
For ${}^3\mathrm{H}$ ($A = 3$, two generators) the sum is small and
calibration forces agreement.  For heavier nuclei the converting
neutron affects only $\sim 1$ generator strongly; the remaining $A - 2$
spectator generators contribute near-zero terms that dilute the signal
when summed equally.

The $q$-weighted method ([derivation chain](#rem:qvalue-derivation-chain))
classifies each generator into unbinding ($nn \to pn$, weight $q$),
rebinding ($pn \to pp$, weight $q^{-1}$), or spectator channels,
applying the Iwahori--Hecke eigenvalue asymmetry.  This channel
separation is the categorical content missing from the naive
Lagrangian and Dirac sums.

**Dirac channel decomposition:**

| Nucleus | $D_{\mathrm{sym}}$ | $D_{\mathrm{alt}}$ | $D_{\mathrm{sym}}/D_{\mathrm{full}}$ |
|:---:|:---:|:---:|:---:|
| ${}^3\mathrm{H}$ | $-0.901$ | $0.000$ | $100\%$ |
| ${}^{14}\mathrm{C}$ | $+0.561$ | $+0.067$ | $89\%$ |
| ${}^{60}\mathrm{Co}$ | $+1.998$ | $+0.280$ | $88\%$ |
| ${}^{90}\mathrm{Sr}$ | $+3.572$ | $+0.326$ | $92\%$ |
| ${}^{137}\mathrm{Cs}$ | $+5.165$ | $+0.500$ | $91\%$ |
| ${}^{210}\mathrm{Bi}$ | $+7.167$ | $+0.856$ | $89\%$ |

The symmetric channel ($\lambda = q$) dominates at $\sim 90\%$;
the antisymmetric channel ($\lambda = -q^{-1}$) contributes the
remaining $\sim 10\%$.  For ${}^3\mathrm{H}$, $D_{\mathrm{alt}} = 0$
because the generator spread is zero for a pure $nn \to pn$ transition
on two generators.
