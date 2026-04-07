All predictions use $\approx$ (derived from $q$, zero fitting parameters).
Experimental values from NNDC/ENSDF with stated uncertainties.
Three categorical methods compared: Lagrangian ($\mathcal{Q}_{\mathrm{lag}}$),
Dirac ($\mathcal{Q}_{\mathrm{dir}}$), and $q$-weighted ($\mathcal{Q}_{q\text{-wt}}$),
each calibrated from ${}^3\mathrm{H}$ via $E_0 = \mathcal{Q}_{\mathrm{exp}}({}^3\mathrm{H}) / |\mathcal{O}({}^3\mathrm{H})|$.
Crossing convention: $(1, -\mathrm{HA})$ throughout (unimodular, $\det T = -1$).

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
  (free neutron calibration, reproduces $\mathcal{Q}_n = 0.782\;\text{MeV}$ exactly)

**Diagnostic --- why both methods undershoot:**

The Lagrangian observable
$\mathcal{L} = \sum_i (\hat{V}_{d,i} - \hat{V}_{p,i})/\hat{V}_{p,i}$
and the Dirac observable
$D = q^{-1}\sum_i \Delta\mathrm{tr}_i/\mathrm{tr}_i + \hbar_q \sum_i \Delta\mathrm{spr}_i/\mathrm{spr}_i$
both sum $A - 1$ generator contributions.
For ${}^3\mathrm{H}$ ($A = 3$, two generators) the sum is small and
calibration forces agreement.  For heavier nuclei the converting
neutron affects only $\sim 1$ generator strongly; the remaining $A - 2$
spectator generators contribute near-zero terms that dilute the signal
when summed equally.

The $q$-weighted method (see `rem:qvalue-derivation-chain`)
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
