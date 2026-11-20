The Breit--Wheeler polarisation selection rule ([rem:breit-wheeler-vertex](#rem:breit-wheeler-vertex)) is a model statement: in the model, only distinct generators ($\sigma_0 \neq \sigma_1$) contribute to pair production. This block records what the rule implies and how it compares with measurement.

## Model consequences

For two photons with polarisation mixing parameters $\phi_1,\phi_2\in[0,1]$, the Hecke normal form yields the same-mode amplitude $S = \phi_1\phi_2 + (1-\phi_1)(1-\phi_2)$ and the pair-production amplitude $C_+ + C_- = 1 - S$. The pair-production threshold energy scale is

$$
  E_0(\phi_1,\phi_2)
  = 
  \frac{2m_e}{\mathrm{net}(e^+) - S \cdot h_{\mathrm{A}}}
   \in [2.27,4.22] \text{MeV},
$$

where $h_{\mathrm{A}} = q - q^{-1} \approx 0.209$ at $q_0$ and $\mathrm{net}(e^+) \approx 0.451$ (the Gröbner--Shirshov NF coefficient at $q_0$).

Evaluate the limits:

| Configuration | $S$ | $E_0$ | Character |
|---|---|---|---|
| Same mode ($\phi_1 = \phi_2$) | $1$ | $\approx 4.22 \mathrm{MeV}$ | Hecke-reduced; no pair in the model |
| Distinct modes ($\phi_1 \neq \phi_2$) | $0$ | $\approx 2.27 \mathrm{MeV}$ | Hopf link $L_\pm$; pair |

For unpolarised beams, the cross-section averages over $\phi_1,\phi_2$ and develops a $\cos(2\phi)$ azimuthal modulation in the $e^-e^+$ opening-angle distribution. The amplitude is proportional to $\langle C_+ - C_- \rangle = \langle \phi_1 - \phi_2 \rangle^2$.

## Comparison with observation

Ultra-peripheral heavy-ion collisions provide colliding quasi-real photons that are linearly polarised transverse to the beam axis. STAR \cite{star2021bw} reports a fourth-order azimuthal modulation $\cos 4\Delta\phi = (16.8 \pm 2.5)\%$ of $e^-e^+$ pairs in Au+Au collisions at $\sqrt{s_{NN}} = 200\,\mathrm{GeV}$, where $\Delta\phi$ is the angle between the pair transverse momentum and that of one lepton. Lowest-order QED predicts $16.5\%$. ATLAS \cite{atlas2021bw} reports the azimuthal anisotropy of $e^-e^+$ pairs in Pb+Pb collisions at $\sqrt{s_{NN}} = 5.02\,\mathrm{TeV}$.

These measurements do not support the model's selection rule. The measured effect is a fourth harmonic that lowest-order QED reproduces, while the model's averaged amplitude above is a second harmonic. QED also gives nonzero pair production for parallel linear polarisations ([rem:breit-wheeler-vertex](#rem:breit-wheeler-vertex)), so the model's suppression of same-mode pairs is not a property of physical photons. No agreement with data is claimed here.

The model's distinct-mode scale $E_0 \approx 2.27\,\mathrm{MeV}$ does not decompose as $2m_e$ plus one unit of Reeb charge: $\hbar_q = (q-1)/q \approx 0.0991$ is dimensionless, and $m_e\hbar_q \approx 0.0506\,\mathrm{MeV}$, not $1.25\,\mathrm{MeV}$.
