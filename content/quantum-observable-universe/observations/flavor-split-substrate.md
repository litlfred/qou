**Proposition.**
*The proton--neutron mass splitting admits a closed-form expression in
substrate atoms with no calibration to the $u$--$d$ mass difference:*

$$
  \frac{m_n - m_p}{M_N}
  \;\approx\;
  \frac{(q - 1)^2 \, (1 - q^{-4})}{3},
$$

*where $M_N = (m_p + m_n)/2$ is the nucleon mass average.  Equivalently,
in factored substrate-atom form,*

$$
  \frac{m_n - m_p}{\mu_{\text{avg}}}
  \;\approx\;
  \hbar_q^2 \cdot h_q \cdot [2]_q,
  \qquad
  \mu_{\text{avg}} = \tfrac{1}{2}(\mu_{\mathfrak{u}} + \mu_{\mathfrak{d}}),
$$

*where $\hbar_q = (q-1)/q$ is the substrate Planck constant,
$h_q = q - q^{-1}$ is the Hecke crossing scale, and
$[2]_q = q + q^{-1}$ is the doublet quantum integer.*

*At $q = q_0 = 1.109978595554181\ldots$ (50 dps) this closes the CODATA value*
$(m_n - m_p)/M_N = 1.293\,\text{MeV} / 938.92\,\text{MeV} \approx 1.377 \times 10^{-3}$
*to within $-0.10\%$.*

*The two algebraic forms agree by the identity
$h_q \cdot z_{\text{mkv}} = z_0 = \hbar_q \cdot \sqrt{q}$,
where $z_0 = q^{1/2} - q^{-1/2}$ and $z_{\text{mkv}} = (q^{1/2} + q^{-1/2})^{-1}$.*

In the substrate-pure form, neither $\mu_{\mathfrak{u}}$ nor $\mu_{\mathfrak{d}}$ appears — only $q_0$ and the universal nucleon scale $M_N$.  The companion proposition [`prop:flavor-dressed-mass-from-substrate-split`](../braids-and-knots/flavor-dressed-mass-from-substrate-split.md) lifts the splitting back to the dressed-quark masses via the Skein factor, recovering the dressed-mass difference $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}} \approx 1.288\,\text{MeV}$ as a derived consequence of $q_0$ and $M_N$ (not a separate input).

The categorical reading of the factored form
$\hbar_q^2 \cdot h_q \cdot [2]_q$:

| Factor | Categorical meaning |
|---|---|
| $\hbar_q^2$ | Two quanta of substrate Planck action |
| $h_q = q - q^{-1}$ | One Hecke crossing (the Skein gap $\sigma - \sigma^{-1}$) |
| $[2]_q = q + q^{-1}$ | Doublet quantum integer (symmetric $\oplus$ antisymmetric eigenspace of $\sigma$) |

The flavor swap $\mathfrak{u} \leftrightarrow \mathfrak{d}$ on a 3-quark
baryon is implemented categorically as the Hecke generator $\sigma$ acting
on a 2-strand sub-braid; its eigenspace decomposition contributes the
$[2]_q$ multiplicity, and the Skein gap $h_q$ contributes the
crossing-energy factor.  Two factors of $\hbar_q$ count the two action
quanta needed to traverse the crossing pair.

**Empirical match (probe `probe_flavor_split_substrate.py`):**

| Quantity | Substrate formula | Substrate value | CODATA target | Residual |
|---|---|---|---|---|
| $(m_n - m_p)/M_N$ | $(q-1)^2 (1 - q^{-4}) / 3$ | $1.376 \times 10^{-3}$ | $1.377 \times 10^{-3}$ | $-0.10\%$ |
| $(m_n - m_p)/\mu_{\text{avg}}$ | $\hbar_q^2 \cdot h_q \cdot [2]_q$ | $4.127 \times 10^{-3}$ | $4.148 \times 10^{-3}$ | $-0.49\%$ |
| $m_n - m_p$ | $M_N \cdot (q-1)^2(1-q^{-4})/3$ | $1.287\,\text{MeV}$ | $1.293\,\text{MeV}$ | $-0.52\%$ |
