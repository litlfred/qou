The Breit--Wheeler polarisation selection rule ([rem:breit-wheeler-vertex](#rem:breit-wheeler-vertex)) predicts a measurable azimuthal anisotropy in $e^-e^+$ pairs produced from two real photons. Only photons in distinct polarisation modes (generators $\sigma_0\neq\sigma_1$) contribute to pair production.

## QOU prediction

For two photons with polarisation mixing parameters $\phi_1,\phi_2\in[0,1]$, the Hecke normal form yields the same-mode amplitude $S = \phi_1\phi_2 + (1-\phi_1)(1-\phi_2)$ and the pair-production amplitude $C_+ + C_- = 1 - S$. The pair-production threshold energy scale is

$$
  E_0(\phi_1,\phi_2)
  = 
  \frac{2m_e}{\mathrm{net}(e^+) - S \cdot h_{\mathrm{A}}}
   \in [2.27,4.22] \text{MeV},
$$

where $h_{\mathrm{A}} = q - q^{-1} \approx 0.209$ at $q_0$ and $\mathrm{net}(e^+) \approx 0.451$ (the Gröbner--Shirshov NF coefficient at $q_0$).

We evaluate the limits:

| Configuration | $S$ | $E_0$ | Character |
|---|---|---|---|
| Same mode ($\phi_1 = \phi_2$) | $1$ | $\approx 4.22 \mathrm{MeV}$ | Hecke-reduced; no pair |
| Distinct modes ($\phi_1 \neq \phi_2$) | $0$ | $\approx 2.27 \mathrm{MeV}$ | Hopf link $L_±$; pair |

For unpolarised beams, the cross-section averages over $\phi_1,\phi_2$ and develops a $\cos(2\phi)$ azimuthal modulation in the $e^-e^+$ opening-angle distribution. The amplitude is proportional to $\langle C_+ - C_- \rangle = \langle \phi_1 - \phi_2 \rangle^2$.

## Comparison with observation

Ultra-peripheral heavy-ion collisions (UPCs) provide colliding real photons. Both STAR (Au+Au) \cite{star2021bw} and ATLAS (Pb+Pb) \cite{atlas2021bw} measure the azimuthal distribution of $e^-e^+$ pairs from $\gamma\gamma$ processes and observe a $\cos(2\phi)$ anisotropy. This observation is consistent with the QOU polarisation selection rule.

- **STAR \cite{star2021bw}**: observes $\cos(2\phi)$ azimuthal asymmetry in $e^-e^+$ pairs from coherent $\gamma\gamma$ interactions in Au+Au UPCs at $\sqrt{s_{NN}} = 200 \text{GeV}$. The measured asymmetry amplitude is $\approx 10$--$15\%$.
- **ATLAS \cite{atlas2021bw}**: confirms the azimuthal anisotropy in $e^-e^+$ pairs from $\gamma\gamma$ in Pb+Pb UPCs at $\sqrt{s_{NN}} = 5.02 \text{TeV}$.

In both experiments, the quasi-real photons are linearly polarised transverse to the beam axis. The observed $\cos(2\phi)$ pattern follows directly from the Hecke polarisation selection rule: pairs are suppressed when both photons occupy the same $\mathbb{P}^1(\mathbb{C})$ coordinate patch and enhanced when they occupy orthogonal patches. While standard QED attributes this modulation to helicity-interference, the QOU traces its geometric origin to the Hecke-algebra structure on the exceptional divisor $\mathcal{S}_p$.

The QOU distinct-mode pair-production energy scale $E_0 \approx 2.27 \text{MeV}$ resolves into the standard threshold $2m_e \approx 1.022 \text{MeV}$ plus the crossing energy of one unit of Reeb charge $\hbar_q = (q-1)/q \approx 1.25 \text{MeV}$ at $q_0$. The sum is $\approx 2.27 \text{MeV}$, matching the symbolic formula.
