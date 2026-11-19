*Proof.*
Write $h = q - q^{-1}$.  Then:

$T_{pp} = T(1, 0)$: entries $[[h, 1], [1, 0]]$

$T_{nn} = T(1, -h)$: entries $[[0, 1], [1, -h]]$

$T_{\mathrm{mix}} = T(1, -h/2)$: entries $[[h/2, 1], [1, -h/2]]$

The differences $T_{\mathrm{mix}} - T_{nn}$ and
$T_{pp} - T_{\mathrm{mix}}$ both equal
$[[h/2, 0], [0, h/2]] = \frac{h}{2} \mathbb{I}$.  $\square$

**Explicit entries at the aether parameter $q$:**

$$
  \Delta_\beta(q_0) = 
  \tfrac{1}{2}(q_0 - q_0^{-1}) \mathbb{I}
   \approx 
  \begin{pmatrix}
    +0.1045 & 0 \\
    0 & +0.1045
  \end{pmatrix}
$$

## The decay formula

At generator $\sigma_i$ (affected by the converting nucleon
at position $p$), the transfer matrix product factors as:

$$
  M_i^{\mathrm{par}}(q) = L_i(q) \cdot T_{\mathrm{par}}(q) \cdot R_i(q)
$$

where $L_i$ is the product of matrices to the left of the
converting crossing (unchanged) and $R_i$ to the right
(unchanged).  The daughter matrix product is

$$
  M_i^{\mathrm{dau}}(q) = L_i(q) \cdot (T_{\mathrm{par}}(q) + \Delta_\beta(q)) \cdot R_i(q).
$$

The change in the transfer matrix product is

$$
  \Delta M_i(q) = L_i(q) \cdot \Delta_\beta(q) \cdot R_i(q).
$$

The change in the Markov-traced volume is

$$
  \Delta \hat{V}_i(q)
  = 
  z \cdot (\Delta M_i)_{11} + (\Delta M_i)_{21}.
$$

The $Q$-value
([transition energy](#def:Q-value-transition)) in **eigenfunction-basis
(log-ratio) form** is

$$
  \mathfrak{Q}_\beta^{\mathrm{B}}
  \;:=\;
  \ln \frac{P_{\mathrm{dau}}(q)}{P_{\mathrm{par}}(q)}
  \cdot \frac{E_0}{z}
  \;=\;
  \frac{E_0}{z} \,
  \sum_{i=0}^{p} \ln \frac{\hat{V}_i^{\mathrm{dau}}(q)}{\hat{V}_i^{\mathrm{par}}(q)}.
$$

Here the sum runs only over generators affected by the
converting nucleon (generators $\sigma_i$ with $i > p$ cancel
exactly), and $z = 1/(\sqrt q + 1/\sqrt q)$ is the Markov–Jones
parameter (Hecke–Skein normalization). The $1/z$ factor is
**not a calibration knob**; it is the normalization mapping the eigenfunction observable $\ln V_{\mathrm{pp}}/V_{\mathrm{nn}}$
onto MeV.

Form B is **not a separate observable** from the NF-counit form
$\mathfrak{Q}_\beta^{\mathrm{A}} = |\Delta(\mathrm{net})| \cdot E_0$ of
[symbolic neutron $Q$-value](#prop:neutron-qvalue-symbolic).
The two are basis-change equivalent at leading order via the
bridge identity in
[$\mathfrak{Q}_\beta$ spectral bridge](#prop:q-beta-spectral-bridge):

$$
  \mathfrak{Q}_\beta^{\mathrm{A}}
  \;=\;
  \mathfrak{Q}_\beta^{\mathrm{B}} \cdot \bigl(1 + \tfrac{(z - 1)\,h}{2} + O(h^2)\bigr).
$$

Form B is the natural basis for $N \geq 1$ brane-tower truncation
analysis, whereas Form A
is canonical at $N = 0$ free neutron.
