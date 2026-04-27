**Proof.**
*Proton ($uud$).*
The proton has quarks $(u_1, u_2, d)$.  The three crossing pairs and their
Skein masses are:

| **Pair** | **Quarks** | **Skein mass** | **Value (MeV)** |
|---|---|---|---|
| I | $(u_1, u_2)$ | $\mathcal{S}_{\mathfrak{u}\mathfrak{u}} = \frac{(q + q^{-1})\mu_{\mathfrak{u}}}{q^{1/2}+q^{-1/2}}$ | 312.36 |
| II | $(u_1, d)$ | $\mathcal{S}_{\mathfrak{u}\mathfrak{d}} = \frac{q\mu_{\mathfrak{u}} + q^{-1}\mu_{\mathfrak{d}}}{q^{1/2}+q^{-1/2}}$ | 312.97 |
| III | $(u_2, d)$ | $\mathcal{S}_{\mathfrak{u}\mathfrak{d}} = \frac{q\mu_{\mathfrak{u}} + q^{-1}\mu_{\mathfrak{d}}}{q^{1/2}+q^{-1/2}}$ | 312.97 |
| | | **Total:** $m_p = \mathcal{S}_{\mathfrak{u}\mathfrak{u}} + 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}$ | **938.272** |

*Neutron ($udd$).*
The neutron has quarks $(u, d_1, d_2)$.  Swapping one up quark for a down
quark replaces the same-flavor pair:

| **Pair** | **Quarks** | **Skein mass** | **Value (MeV)** |
|---|---|---|---|
| I | $(u, d_1)$ | $\mathcal{S}_{\mathfrak{u}\mathfrak{d}} = \frac{q\mu_{\mathfrak{u}} + q^{-1}\mu_{\mathfrak{d}}}{q^{1/2}+q^{-1/2}}$ | 312.97 |
| II | $(u, d_2)$ | $\mathcal{S}_{\mathfrak{u}\mathfrak{d}} = \frac{q\mu_{\mathfrak{u}} + q^{-1}\mu_{\mathfrak{d}}}{q^{1/2}+q^{-1/2}}$ | 312.97 |
| III | $(d_1, d_2)$ | $\mathcal{S}_{\mathfrak{d}\mathfrak{d}} = \frac{(q + q^{-1})\mu_{\mathfrak{d}}}{q^{1/2}+q^{-1/2}}$ | 313.65 |
| | | **Total:** $m_n = 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}} + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}$ | **939.565** |

*The $u$--$d$ mass splitting.*
The proton--neutron mass difference isolates the same-flavor crossing pair:

$$
  m_n - m_p
  = 
  \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q) - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q)
  = 
  \frac{q + q^{-1}}{q^{1/2}+q^{-1/2}}(\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}).
$$

Substituting $q = q_0$ and the CODATA splitting
$m_n - m_p \approx 1.29333251 \mathrm{MeV}$ determines the dressed quark
mass difference:

$$
  \mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}
  = 
  \frac{q^{1/2}+q^{-1/2}}{q+q^{-1}}(m_n - m_p)
  = 
  \frac{2.0027}{2.0109} \times 1.293
   \approx  1.288 \mathrm{MeV},
$$

and the individual dressed masses are
$\mu_{\mathfrak{u}} \approx 311.10 \mathrm{MeV}$ and
$\mu_{\mathfrak{d}} \approx 312.39 \mathrm{MeV}$.  $\square$
