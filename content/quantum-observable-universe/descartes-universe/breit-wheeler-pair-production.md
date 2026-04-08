The **Breit--Wheeler process** is the categorical pair production
$\gamma\gamma \to e^- e^+$: two photons fuse into an
electron--positron pair.  In the Iwahori--Hecke algebra $H_3(q)$,
the process is the identity

$$
  \gamma_1 \cdot \gamma_2
  \;=\;
  \mathrm{NF}(e^-) + \mathrm{NF}(e^+)
  \;+\; \text{binding energy}
$$

where the photon, electron, and positron are the braid words

$$
  \gamma = \sigma_0, \qquad
  e^- = \sigma_0\sigma_1\sigma_0 \;\text{(trefoil)}, \qquad
  e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1} \;\text{(mirror trefoil)}.
$$

**Bare photon pair.**
Two identical photons give $\gamma\gamma = \sigma_0^2$.
Applying the Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$:

$$
  \mathrm{NF}(\gamma\gamma)
  \;=\; (q - q^{-1})\,H^0 + \nu
$$

with $\mathrm{net}(\gamma\gamma) = 1 + (q - q^{-1}) \approx 1.209$.
This yields a bare pair energy $E_{\mathrm{pair}} \approx 1.006$ MeV,
which is $1.6\%$ below $2m_e = 1.022$ MeV.

**Colored photon pair.**
To match the threshold $2m_e$ exactly, the photon acquires
**color dressing** — a small admixture of both Hecke generators:

$$
  \gamma_{\phi}
  \;=\;
  \mathbf{1} + \phi\,\sigma_0 + \phi\,\sigma_1
$$

where $\phi$ is the **color weight** (a real parameter).
The pair $\gamma_\phi \cdot \gamma_\phi$ has normal form

$$
  \mathrm{NF}(\gamma_\phi^2)
  \;=\;
  (1 + 2\phi^2)\,\nu
  + (2\phi + \phi^2 H_A)\,H^0
  + (2\phi + \phi^2 H_A)\,H^1
  + \phi^2\,L_+
  + \phi^2\,L_-
$$

with net $= (1 + 2\phi)^2 + 2\phi^2 H_A$ where $H_A = q - q^{-1}$.

**Energy alignment.**
Setting $E_{\mathrm{pair}} = 2m_e$ fixes:

$$
  \phi \;=\; 0.0487 \qquad\text{(symmetric color)}.
$$

The color weight generates Hopf link content $L_\pm$ in the photon
pair — physically, the colored photon is no longer a bare unknot
but carries topological structure that supplies the missing
$1.6\%$ of pair production energy.

**Witness**: `breit-wheeler-nucleon-nf.witness.json`.
