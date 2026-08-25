The energy scale $E_0$ is derived from CAL-1 ($m_e$) and CAL-2 ($q_0$) alone. It consumes no $\beta$-decay calibration. It has a natural interpretation in terms of the $q$-deformed Planck scale: it represents the energy of one Hecke reduction step. This is the physical cost of resolving a single $\sigma_i^2 \to h\sigma_i + \mathbf{1}$.

## Derived form

$$
  \boxed{
  E_0
  =
  m_e \cdot c_q^2 \cdot \hbar_q
  =
  \frac{m_e}{(q-1)^2} \cdot \frac{q-1}{q}
  =
  \frac{m_e}{q(q-1)}
  }
$$

At $q_0 \approx 1.110$, $E_0 \approx 4.186$ MeV.

**Input-error propagation.**
The input errors are CAL-1 $\sigma_{m_e}/m_e \approx 0.3$ ppb and CAL-2 $\sigma_{q_0}/q_0 \approx 1.22$ ppb. The $q_0$ amplification factor is $\partial \ln E_0 / \partial \ln q_0 = (1 - 2q_0)/(q_0 - 1) \approx -11.09$ at $q_0 = 1.110$.

$$
  \sigma_{E_0} / E_0
  \approx
  \sqrt{(0.3\,\mathrm{ppb})^2 + (11.09 \times 1.22\,\mathrm{ppb})^2}
  \approx 13.5\,\mathrm{ppb}.
$$

This yields $\sigma_{E_0} \approx 5.7 \times 10^{-8}$ MeV. This error is negligible at the keV scale of $\beta$-decay observables.

## Calibration-cross-check

A historical calibrated $E_0$ definition used CAL-3 ($\mathfrak{Q}_\beta$) as input via $E_0^{(\text{cal})} = \mathfrak{Q}_\beta^{\text{CODATA}} / \lvert\Delta(\mathrm{net})\rvert \approx 4.155$ MeV. This form is no longer used in the prediction pipeline. It consumes CAL-3 as input rather than treating it as a prediction.

The 0.74% gap between the derived $E_0 \approx 4.186$ MeV and the cross-check $\approx 4.155$ MeV stems from the brane-tower truncation residual at $N=0$. By the structural bound, this residual is $O(\hbar_q^2/(1 - \hbar_q^2)) \approx 1\%$ at $N=0$.

## Physical meaning

$$
  m_e \cdot c_q^2 \cdot \hbar_q
  =
  \frac{m_e \cdot c_q^2}{t_P}
$$

This quantity is the electron's rest energy per Planck time. It serves as the natural energy quantum for a single interaction step in a universe where the lightest charged particle has mass $m_e$, the speed of information is $c_q = 1/(q-1)$, and one Planck time is $t_P = 1/\hbar_q$.

Each Hecke reduction step $\sigma_i^2 \to h\sigma_i + \mathbf{1}$ corresponds to one Planck tick of interaction. The physical energy cost of this step is $E_0$.

## Calibration by free neutron decay

The free neutron decay $n \to p + e^- + \bar\nu_e$ provides the simplest hadronic process exercising a single Hecke step. It involves one crossing change $\mathfrak{d} \to \mathfrak{u}$ inside one nucleon. The Q-value $\mathfrak{Q}_\beta = 0.782$ MeV is the energy released by this crossing change. Dividing by the dimensionless Hecke NF difference $\lvert\Delta\mathrm{net}\rvert \approx 0.188$ gives $E_0 = \mathfrak{Q}_\beta / \lvert\Delta\mathrm{net}\rvert \approx 4.179$ MeV.

## Calibration inputs in Planck units

Using the three $q$-constants $c_q, \hbar_q, t_P$, the categorical three-calibration inputs become:

| Input | $H^k$ degree | What it fixes | In $q$-Planck units |
|-------|:-----------:|--------------|---------------------|
| $m_e$ | $H^0$ | The mass unit | $E_0/(c_q^2 \hbar_q)$ (the size) |
| $m_\mu/m_e$ | $H^1$ | $q_0$ | The shape (dimensionless) |
| $\mathfrak{Q}_\beta(n)$ | $H^2$ | The $\beta$-decay scale | $E_0$ in MeV |

Once $q_0$ is fixed, $c_q$, $\hbar_q$, $t_P$, and $G_q$ are determined. The mass scale $E_0$ sets the correspondence between the $q$-Planck system and SI units. The $1\%$ residual between $E_0$ and $m_e c_q^2 \hbar_q$ represents the brane tower contribution.
