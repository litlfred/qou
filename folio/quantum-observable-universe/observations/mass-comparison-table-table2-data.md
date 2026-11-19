*The LO output column is the $m_e$-scaled realization of the dimensionless mass ratio (CAL-1 sets the MeV scale by fiat); absolute mass in MeV is not a framework prediction.*

| Particle | Knot formula | QOU / LO output (MeV) | Observed (MeV) | Source |
|----------|-------------|---:|---:|--------|
| Proton | $[u,u,d]_p \oplus \mathcal{L}_H$ | ${{ qou.computations.m-p-substrate-identity-50dps.data.predictions.m_p_MeV | precision: 7 }}$ † | ${{ qou.computations.codata-2022-validation-masses.data.m_p_MeV | precision: 7 }}$ | CODATA 2022 |
| Neutron (Two-Term QED) | $[u,d,d]_p \oplus \mathcal{L}_H$ | ${{ qou.computations.m-p-substrate-identity-50dps.data.two_term_borromean_qed_diagnostics.m_n_two_term_MeV | precision: 7 }}$ | ${{ qou.computations.codata-2022-validation-masses.data.m_n_MeV | precision: 7 }}$ | CODATA 2022 |
| $n$-$p$ split (1-term Kashiwara $b^2$) | | ${{ qou.computations.m-p-substrate-identity-50dps.data.predictions.Delta_m_pn_MeV | precision: 5 }}$ | $1.2933$ | CODATA 2022 |
| $\pi^{\pm}$ | $u \oplus d^{\sigma}$ | $139.570$ | $139.570$ | PDG 2024 |
| $K^{\pm}$ | $u \oplus s^{\sigma}$ | $493.677$ | $493.677$ | PDG 2024 |
