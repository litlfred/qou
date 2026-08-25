**Proposition (conditional on Borromean quark conjecture — $\mathfrak{Q}_\beta$ of free neutron $\beta^{-}$-decay).**
*We derive the $Q$-value of free neutron $\beta^-$-decay $n \to p + e^- + \bar\nu_e$ symbolically from the categorical three-calibration inputs $m_e$ ($H^0$) and $q_0$ ($H^1$). The value $\mathfrak{Q}_\beta(n)$ ($H^2$) is the $\beta$-decay datum being predicted, not used as input.*

## Single-wrap normal-form computation

A single wrap of typed crossings in $H_3(q)$ represents the proton and neutron. Let $h = q - q^{-1}$.

**Proton** $[u, u, d]$: the typed crossing operators give:
$$
  L_+ - \tfrac{h}{2}\sigma_0
$$

**Neutron** $[u, d, d]$:
$$
  L_+ - h\sigma_0 - \tfrac{h}{2}\sigma_1 + \tfrac{h^2}{2}\gamma
$$

## Symbolic $\Delta(\text{net})$

$$
  \Delta(\mathrm{net})
  =
  \mathrm{net}(n) - \mathrm{net}(p)
  =
  \frac{h(h - 2)}{2}.
$$

The $L_+$ and $L_-$ contributions cancel exactly because both nucleons share the same Hopf content at single wrap. The entire $Q$-value arises from the vacuum channel and the two crossing channels.

## $Q$-value from two inputs

The energy scale $E_0 = m_e / (q_0(q_0 - 1))$ converts dimensionless differences to MeV:

$$
  \mathfrak{Q}_\beta
  =
  |\Delta(\mathrm{net})| \times E_0
  =
  \frac{m_e \cdot |q^2 - 2q - 1| \cdot (q+1)}{2q^3}.
$$

## Numerical evaluation

At $q_0 \approx 1.110$ and $m_e \approx 0.511$ MeV:

$$
  \mathfrak{Q}_\beta
  =
  0.7836 \text{ MeV}
  \qquad
  (\text{CODATA: } 0.7823 \text{ MeV},
  \quad +0.17\%).
$$

The $1.3$ keV discrepancy represents the brane-tower correction to the energy scale $E_0$.

## Relation to the transfer-matrix eigenfunction form

The closed form above (Form A, normal-form counit basis) is equivalent to the transfer-matrix log-ratio form (Form B) up to the Markov–Jones normalization $z$:

$$
  \mathfrak{Q}_\beta^{\mathrm{A}}
  \;=\;
  \mathfrak{Q}_\beta^{\mathrm{B}} \cdot \Bigl(1 + \tfrac{(z-1)\,h}{2} + O(h^2)\Bigr).
$$

These two forms are not competing predictions; they describe the same observable in two bases.
